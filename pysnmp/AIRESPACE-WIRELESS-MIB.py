# SNMP MIB module (AIRESPACE-WIRELESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AIRESPACE-WIRELESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:16 2024
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

(airespace,) = mibBuilder.importSymbols(
    "AIRESPACE-REF-MIB",
    "airespace")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

bsnWireless = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2)
)
bsnWireless.setRevisions(
        ("2011-09-27 00:00",
         "2010-02-09 00:00",
         "2006-04-10 00:00",
         "2005-10-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class WEPKeytype(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 32),
    )



class ProfileState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fail", 0),
          ("pass", 1))
    )



class BsnTxtSignatureMacInfo(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bsnSignatureMacAll", 0),
          ("bsnSignatureMacBoth", 2),
          ("bsnSignatureMacIndividual", 1))
    )



class BsnSignaturePatternOffSetStart(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sigPattStartFrm", 0),
          ("sigPattStartFrmBody", 1))
    )



# MIB Managed Objects in the order of their OIDs

_BsnEss_ObjectIdentity = ObjectIdentity
bsnEss = _BsnEss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1)
)
_BsnDot11EssTable_Object = MibTable
bsnDot11EssTable = _BsnDot11EssTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1)
)
if mibBuilder.loadTexts:
    bsnDot11EssTable.setStatus("current")
_BsnDot11EssEntry_Object = MibTableRow
bsnDot11EssEntry = _BsnDot11EssEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1)
)
bsnDot11EssEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnDot11EssIndex"),
)
if mibBuilder.loadTexts:
    bsnDot11EssEntry.setStatus("current")


class _BsnDot11EssIndex_Type(Unsigned32):
    """Custom type bsnDot11EssIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 517),
    )


_BsnDot11EssIndex_Type.__name__ = "Unsigned32"
_BsnDot11EssIndex_Object = MibTableColumn
bsnDot11EssIndex = _BsnDot11EssIndex_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 1),
    _BsnDot11EssIndex_Type()
)
bsnDot11EssIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssIndex.setStatus("current")


class _BsnDot11EssSsid_Type(DisplayString):
    """Custom type bsnDot11EssSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BsnDot11EssSsid_Type.__name__ = "DisplayString"
_BsnDot11EssSsid_Object = MibTableColumn
bsnDot11EssSsid = _BsnDot11EssSsid_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 2),
    _BsnDot11EssSsid_Type()
)
bsnDot11EssSsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssSsid.setStatus("current")


class _BsnDot11EssSessionTimeout_Type(Unsigned32):
    """Custom type bsnDot11EssSessionTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_BsnDot11EssSessionTimeout_Type.__name__ = "Unsigned32"
_BsnDot11EssSessionTimeout_Object = MibTableColumn
bsnDot11EssSessionTimeout = _BsnDot11EssSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 4),
    _BsnDot11EssSessionTimeout_Type()
)
bsnDot11EssSessionTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssSessionTimeout.setStatus("current")


class _BsnDot11EssMacFiltering_Type(Integer32):
    """Custom type bsnDot11EssMacFiltering based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnDot11EssMacFiltering_Type.__name__ = "Integer32"
_BsnDot11EssMacFiltering_Object = MibTableColumn
bsnDot11EssMacFiltering = _BsnDot11EssMacFiltering_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 5),
    _BsnDot11EssMacFiltering_Type()
)
bsnDot11EssMacFiltering.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssMacFiltering.setStatus("current")


class _BsnDot11EssAdminStatus_Type(Integer32):
    """Custom type bsnDot11EssAdminStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnDot11EssAdminStatus_Type.__name__ = "Integer32"
_BsnDot11EssAdminStatus_Object = MibTableColumn
bsnDot11EssAdminStatus = _BsnDot11EssAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 6),
    _BsnDot11EssAdminStatus_Type()
)
bsnDot11EssAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssAdminStatus.setStatus("current")


class _BsnDot11EssSecurityAuthType_Type(Integer32):
    """Custom type bsnDot11EssSecurityAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              128)
        )
    )
    namedValues = NamedValues(
        *(("authCiscoLeap", 128),
          ("authOpen", 0),
          ("authSharedKey", 1))
    )


_BsnDot11EssSecurityAuthType_Type.__name__ = "Integer32"
_BsnDot11EssSecurityAuthType_Object = MibTableColumn
bsnDot11EssSecurityAuthType = _BsnDot11EssSecurityAuthType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 7),
    _BsnDot11EssSecurityAuthType_Type()
)
bsnDot11EssSecurityAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnDot11EssSecurityAuthType.setStatus("current")


class _BsnDot11EssStaticWEPSecurity_Type(Integer32):
    """Custom type bsnDot11EssStaticWEPSecurity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnDot11EssStaticWEPSecurity_Type.__name__ = "Integer32"
_BsnDot11EssStaticWEPSecurity_Object = MibTableColumn
bsnDot11EssStaticWEPSecurity = _BsnDot11EssStaticWEPSecurity_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 8),
    _BsnDot11EssStaticWEPSecurity_Type()
)
bsnDot11EssStaticWEPSecurity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssStaticWEPSecurity.setStatus("current")


class _BsnDot11EssStaticWEPEncryptionType_Type(Integer32):
    """Custom type bsnDot11EssStaticWEPEncryptionType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notset", 4),
          ("wep104", 0),
          ("wep128", 3),
          ("wep40", 2))
    )


_BsnDot11EssStaticWEPEncryptionType_Type.__name__ = "Integer32"
_BsnDot11EssStaticWEPEncryptionType_Object = MibTableColumn
bsnDot11EssStaticWEPEncryptionType = _BsnDot11EssStaticWEPEncryptionType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 9),
    _BsnDot11EssStaticWEPEncryptionType_Type()
)
bsnDot11EssStaticWEPEncryptionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssStaticWEPEncryptionType.setStatus("current")
_BsnDot11EssStaticWEPDefaultKey_Type = WEPKeytype
_BsnDot11EssStaticWEPDefaultKey_Object = MibTableColumn
bsnDot11EssStaticWEPDefaultKey = _BsnDot11EssStaticWEPDefaultKey_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 10),
    _BsnDot11EssStaticWEPDefaultKey_Type()
)
bsnDot11EssStaticWEPDefaultKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssStaticWEPDefaultKey.setStatus("current")


class _BsnDot11EssStaticWEPKeyIndex_Type(Integer32):
    """Custom type bsnDot11EssStaticWEPKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BsnDot11EssStaticWEPKeyIndex_Type.__name__ = "Integer32"
_BsnDot11EssStaticWEPKeyIndex_Object = MibTableColumn
bsnDot11EssStaticWEPKeyIndex = _BsnDot11EssStaticWEPKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 11),
    _BsnDot11EssStaticWEPKeyIndex_Type()
)
bsnDot11EssStaticWEPKeyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssStaticWEPKeyIndex.setStatus("current")


class _BsnDot11EssStaticWEPKeyFormat_Type(Integer32):
    """Custom type bsnDot11EssStaticWEPKeyFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 2),
          ("default", 0),
          ("hex", 1))
    )


_BsnDot11EssStaticWEPKeyFormat_Type.__name__ = "Integer32"
_BsnDot11EssStaticWEPKeyFormat_Object = MibTableColumn
bsnDot11EssStaticWEPKeyFormat = _BsnDot11EssStaticWEPKeyFormat_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 12),
    _BsnDot11EssStaticWEPKeyFormat_Type()
)
bsnDot11EssStaticWEPKeyFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssStaticWEPKeyFormat.setStatus("current")


class _BsnDot11Ess8021xSecurity_Type(Integer32):
    """Custom type bsnDot11Ess8021xSecurity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnDot11Ess8021xSecurity_Type.__name__ = "Integer32"
_BsnDot11Ess8021xSecurity_Object = MibTableColumn
bsnDot11Ess8021xSecurity = _BsnDot11Ess8021xSecurity_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 13),
    _BsnDot11Ess8021xSecurity_Type()
)
bsnDot11Ess8021xSecurity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11Ess8021xSecurity.setStatus("current")


class _BsnDot11Ess8021xEncryptionType_Type(Integer32):
    """Custom type bsnDot11Ess8021xEncryptionType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 4),
          ("wep104", 0),
          ("wep128", 3),
          ("wep40", 2))
    )


_BsnDot11Ess8021xEncryptionType_Type.__name__ = "Integer32"
_BsnDot11Ess8021xEncryptionType_Object = MibTableColumn
bsnDot11Ess8021xEncryptionType = _BsnDot11Ess8021xEncryptionType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 14),
    _BsnDot11Ess8021xEncryptionType_Type()
)
bsnDot11Ess8021xEncryptionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11Ess8021xEncryptionType.setStatus("current")


class _BsnDot11EssWPASecurity_Type(Integer32):
    """Custom type bsnDot11EssWPASecurity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnDot11EssWPASecurity_Type.__name__ = "Integer32"
_BsnDot11EssWPASecurity_Object = MibTableColumn
bsnDot11EssWPASecurity = _BsnDot11EssWPASecurity_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 16),
    _BsnDot11EssWPASecurity_Type()
)
bsnDot11EssWPASecurity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssWPASecurity.setStatus("deprecated")


class _BsnDot11EssWPAEncryptionType_Type(Integer32):
    """Custom type bsnDot11EssWPAEncryptionType based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("tkipmic", 5),
          ("wep104", 0),
          ("wep128", 3),
          ("wep40", 2))
    )


_BsnDot11EssWPAEncryptionType_Type.__name__ = "Integer32"
_BsnDot11EssWPAEncryptionType_Object = MibTableColumn
bsnDot11EssWPAEncryptionType = _BsnDot11EssWPAEncryptionType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 17),
    _BsnDot11EssWPAEncryptionType_Type()
)
bsnDot11EssWPAEncryptionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssWPAEncryptionType.setStatus("deprecated")


class _BsnDot11EssIpsecSecurity_Type(Integer32):
    """Custom type bsnDot11EssIpsecSecurity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnDot11EssIpsecSecurity_Type.__name__ = "Integer32"
_BsnDot11EssIpsecSecurity_Object = MibTableColumn
bsnDot11EssIpsecSecurity = _BsnDot11EssIpsecSecurity_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 18),
    _BsnDot11EssIpsecSecurity_Type()
)
bsnDot11EssIpsecSecurity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssIpsecSecurity.setStatus("current")


class _BsnDot11EssVpnEncrTransform_Type(Integer32):
    """Custom type bsnDot11EssVpnEncrTransform based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("aes256Cbc", 4),
          ("aesCbc", 3),
          ("des", 2),
          ("none", 1),
          ("tripleDes", 0))
    )


_BsnDot11EssVpnEncrTransform_Type.__name__ = "Integer32"
_BsnDot11EssVpnEncrTransform_Object = MibTableColumn
bsnDot11EssVpnEncrTransform = _BsnDot11EssVpnEncrTransform_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 19),
    _BsnDot11EssVpnEncrTransform_Type()
)
bsnDot11EssVpnEncrTransform.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssVpnEncrTransform.setStatus("current")


class _BsnDot11EssVpnAuthTransform_Type(Integer32):
    """Custom type bsnDot11EssVpnAuthTransform based on Integer32"""
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
        *(("hmacMd5", 2),
          ("hmacSha1", 0),
          ("none", 1))
    )


_BsnDot11EssVpnAuthTransform_Type.__name__ = "Integer32"
_BsnDot11EssVpnAuthTransform_Object = MibTableColumn
bsnDot11EssVpnAuthTransform = _BsnDot11EssVpnAuthTransform_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 20),
    _BsnDot11EssVpnAuthTransform_Type()
)
bsnDot11EssVpnAuthTransform.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssVpnAuthTransform.setStatus("current")


class _BsnDot11EssVpnIkeAuthMode_Type(Integer32):
    """Custom type bsnDot11EssVpnIkeAuthMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("certificate", 2),
          ("presharedKey", 3),
          ("xauthEnablePsk", 0))
    )


_BsnDot11EssVpnIkeAuthMode_Type.__name__ = "Integer32"
_BsnDot11EssVpnIkeAuthMode_Object = MibTableColumn
bsnDot11EssVpnIkeAuthMode = _BsnDot11EssVpnIkeAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 21),
    _BsnDot11EssVpnIkeAuthMode_Type()
)
bsnDot11EssVpnIkeAuthMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssVpnIkeAuthMode.setStatus("current")


class _BsnDot11EssVpnSharedKey_Type(OctetString):
    """Custom type bsnDot11EssVpnSharedKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_BsnDot11EssVpnSharedKey_Type.__name__ = "OctetString"
_BsnDot11EssVpnSharedKey_Object = MibTableColumn
bsnDot11EssVpnSharedKey = _BsnDot11EssVpnSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 22),
    _BsnDot11EssVpnSharedKey_Type()
)
bsnDot11EssVpnSharedKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssVpnSharedKey.setStatus("current")


class _BsnDot11EssVpnSharedKeySize_Type(Unsigned32):
    """Custom type bsnDot11EssVpnSharedKeySize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_BsnDot11EssVpnSharedKeySize_Type.__name__ = "Unsigned32"
_BsnDot11EssVpnSharedKeySize_Object = MibTableColumn
bsnDot11EssVpnSharedKeySize = _BsnDot11EssVpnSharedKeySize_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 23),
    _BsnDot11EssVpnSharedKeySize_Type()
)
bsnDot11EssVpnSharedKeySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnDot11EssVpnSharedKeySize.setStatus("current")


class _BsnDot11EssVpnIkePhase1Mode_Type(Integer32):
    """Custom type bsnDot11EssVpnIkePhase1Mode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("agressive", 0),
          ("main", 1))
    )


_BsnDot11EssVpnIkePhase1Mode_Type.__name__ = "Integer32"
_BsnDot11EssVpnIkePhase1Mode_Object = MibTableColumn
bsnDot11EssVpnIkePhase1Mode = _BsnDot11EssVpnIkePhase1Mode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 24),
    _BsnDot11EssVpnIkePhase1Mode_Type()
)
bsnDot11EssVpnIkePhase1Mode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssVpnIkePhase1Mode.setStatus("current")


class _BsnDot11EssVpnIkeLifetime_Type(Integer32):
    """Custom type bsnDot11EssVpnIkeLifetime based on Integer32"""
    defaultValue = 57600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1800, 345600),
    )


_BsnDot11EssVpnIkeLifetime_Type.__name__ = "Integer32"
_BsnDot11EssVpnIkeLifetime_Object = MibTableColumn
bsnDot11EssVpnIkeLifetime = _BsnDot11EssVpnIkeLifetime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 25),
    _BsnDot11EssVpnIkeLifetime_Type()
)
bsnDot11EssVpnIkeLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssVpnIkeLifetime.setStatus("current")


class _BsnDot11EssVpnIkeDHGroup_Type(Integer32):
    """Custom type bsnDot11EssVpnIkeDHGroup based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              14)
        )
    )
    namedValues = NamedValues(
        *(("group1", 1),
          ("group14", 14),
          ("group2", 0),
          ("group5", 4))
    )


_BsnDot11EssVpnIkeDHGroup_Type.__name__ = "Integer32"
_BsnDot11EssVpnIkeDHGroup_Object = MibTableColumn
bsnDot11EssVpnIkeDHGroup = _BsnDot11EssVpnIkeDHGroup_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 26),
    _BsnDot11EssVpnIkeDHGroup_Type()
)
bsnDot11EssVpnIkeDHGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssVpnIkeDHGroup.setStatus("current")


class _BsnDot11EssIpsecPassthruSecurity_Type(Integer32):
    """Custom type bsnDot11EssIpsecPassthruSecurity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnDot11EssIpsecPassthruSecurity_Type.__name__ = "Integer32"
_BsnDot11EssIpsecPassthruSecurity_Object = MibTableColumn
bsnDot11EssIpsecPassthruSecurity = _BsnDot11EssIpsecPassthruSecurity_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 27),
    _BsnDot11EssIpsecPassthruSecurity_Type()
)
bsnDot11EssIpsecPassthruSecurity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssIpsecPassthruSecurity.setStatus("deprecated")


class _BsnDot11EssVpnPassthruGateway_Type(IpAddress):
    """Custom type bsnDot11EssVpnPassthruGateway based on IpAddress"""
    defaultHexValue = "00000000"


_BsnDot11EssVpnPassthruGateway_Object = MibTableColumn
bsnDot11EssVpnPassthruGateway = _BsnDot11EssVpnPassthruGateway_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 28),
    _BsnDot11EssVpnPassthruGateway_Type()
)
bsnDot11EssVpnPassthruGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssVpnPassthruGateway.setStatus("current")


class _BsnDot11EssWebSecurity_Type(Integer32):
    """Custom type bsnDot11EssWebSecurity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnDot11EssWebSecurity_Type.__name__ = "Integer32"
_BsnDot11EssWebSecurity_Object = MibTableColumn
bsnDot11EssWebSecurity = _BsnDot11EssWebSecurity_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 29),
    _BsnDot11EssWebSecurity_Type()
)
bsnDot11EssWebSecurity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssWebSecurity.setStatus("current")


class _BsnDot11EssRadioPolicy_Type(Integer32):
    """Custom type bsnDot11EssRadioPolicy based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("dot11aOnly", 2),
          ("dot11abOnly", 6),
          ("dot11agOnly", 5),
          ("dot11bOnly", 1),
          ("dot11bgOnly", 4),
          ("dot11gOnly", 3))
    )


_BsnDot11EssRadioPolicy_Type.__name__ = "Integer32"
_BsnDot11EssRadioPolicy_Object = MibTableColumn
bsnDot11EssRadioPolicy = _BsnDot11EssRadioPolicy_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 30),
    _BsnDot11EssRadioPolicy_Type()
)
bsnDot11EssRadioPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssRadioPolicy.setStatus("current")


class _BsnDot11EssQualityOfService_Type(Integer32):
    """Custom type bsnDot11EssQualityOfService based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bronze", 0),
          ("gold", 2),
          ("platinum", 3),
          ("silver", 1))
    )


_BsnDot11EssQualityOfService_Type.__name__ = "Integer32"
_BsnDot11EssQualityOfService_Object = MibTableColumn
bsnDot11EssQualityOfService = _BsnDot11EssQualityOfService_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 31),
    _BsnDot11EssQualityOfService_Type()
)
bsnDot11EssQualityOfService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssQualityOfService.setStatus("current")


class _BsnDot11EssDhcpRequired_Type(Integer32):
    """Custom type bsnDot11EssDhcpRequired based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnDot11EssDhcpRequired_Type.__name__ = "Integer32"
_BsnDot11EssDhcpRequired_Object = MibTableColumn
bsnDot11EssDhcpRequired = _BsnDot11EssDhcpRequired_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 32),
    _BsnDot11EssDhcpRequired_Type()
)
bsnDot11EssDhcpRequired.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssDhcpRequired.setStatus("current")


class _BsnDot11EssDhcpServerIpAddress_Type(IpAddress):
    """Custom type bsnDot11EssDhcpServerIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_BsnDot11EssDhcpServerIpAddress_Object = MibTableColumn
bsnDot11EssDhcpServerIpAddress = _BsnDot11EssDhcpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 33),
    _BsnDot11EssDhcpServerIpAddress_Type()
)
bsnDot11EssDhcpServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssDhcpServerIpAddress.setStatus("current")


class _BsnDot11EssVpnContivityMode_Type(Integer32):
    """Custom type bsnDot11EssVpnContivityMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnDot11EssVpnContivityMode_Type.__name__ = "Integer32"
_BsnDot11EssVpnContivityMode_Object = MibTableColumn
bsnDot11EssVpnContivityMode = _BsnDot11EssVpnContivityMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 34),
    _BsnDot11EssVpnContivityMode_Type()
)
bsnDot11EssVpnContivityMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssVpnContivityMode.setStatus("deprecated")


class _BsnDot11EssVpnQotdServerAddress_Type(IpAddress):
    """Custom type bsnDot11EssVpnQotdServerAddress based on IpAddress"""
    defaultHexValue = "00000000"


_BsnDot11EssVpnQotdServerAddress_Object = MibTableColumn
bsnDot11EssVpnQotdServerAddress = _BsnDot11EssVpnQotdServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 35),
    _BsnDot11EssVpnQotdServerAddress_Type()
)
bsnDot11EssVpnQotdServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssVpnQotdServerAddress.setStatus("deprecated")


class _BsnDot11EssBlacklistTimeout_Type(Integer32):
    """Custom type bsnDot11EssBlacklistTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BsnDot11EssBlacklistTimeout_Type.__name__ = "Integer32"
_BsnDot11EssBlacklistTimeout_Object = MibTableColumn
bsnDot11EssBlacklistTimeout = _BsnDot11EssBlacklistTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 37),
    _BsnDot11EssBlacklistTimeout_Type()
)
bsnDot11EssBlacklistTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssBlacklistTimeout.setStatus("current")
_BsnDot11EssNumberOfMobileStations_Type = Counter32
_BsnDot11EssNumberOfMobileStations_Object = MibTableColumn
bsnDot11EssNumberOfMobileStations = _BsnDot11EssNumberOfMobileStations_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 38),
    _BsnDot11EssNumberOfMobileStations_Type()
)
bsnDot11EssNumberOfMobileStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnDot11EssNumberOfMobileStations.setStatus("current")


class _BsnDot11EssWebPassthru_Type(Integer32):
    """Custom type bsnDot11EssWebPassthru based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnDot11EssWebPassthru_Type.__name__ = "Integer32"
_BsnDot11EssWebPassthru_Object = MibTableColumn
bsnDot11EssWebPassthru = _BsnDot11EssWebPassthru_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 39),
    _BsnDot11EssWebPassthru_Type()
)
bsnDot11EssWebPassthru.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssWebPassthru.setStatus("current")


class _BsnDot11EssCraniteSecurity_Type(Integer32):
    """Custom type bsnDot11EssCraniteSecurity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnDot11EssCraniteSecurity_Type.__name__ = "Integer32"
_BsnDot11EssCraniteSecurity_Object = MibTableColumn
bsnDot11EssCraniteSecurity = _BsnDot11EssCraniteSecurity_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 40),
    _BsnDot11EssCraniteSecurity_Type()
)
bsnDot11EssCraniteSecurity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssCraniteSecurity.setStatus("current")


class _BsnDot11EssBlacklistingCapability_Type(Integer32):
    """Custom type bsnDot11EssBlacklistingCapability based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnDot11EssBlacklistingCapability_Type.__name__ = "Integer32"
_BsnDot11EssBlacklistingCapability_Object = MibTableColumn
bsnDot11EssBlacklistingCapability = _BsnDot11EssBlacklistingCapability_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 41),
    _BsnDot11EssBlacklistingCapability_Type()
)
bsnDot11EssBlacklistingCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssBlacklistingCapability.setStatus("current")


class _BsnDot11EssInterfaceName_Type(DisplayString):
    """Custom type bsnDot11EssInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BsnDot11EssInterfaceName_Type.__name__ = "DisplayString"
_BsnDot11EssInterfaceName_Object = MibTableColumn
bsnDot11EssInterfaceName = _BsnDot11EssInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 42),
    _BsnDot11EssInterfaceName_Type()
)
bsnDot11EssInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssInterfaceName.setStatus("current")


class _BsnDot11EssAclName_Type(DisplayString):
    """Custom type bsnDot11EssAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BsnDot11EssAclName_Type.__name__ = "DisplayString"
_BsnDot11EssAclName_Object = MibTableColumn
bsnDot11EssAclName = _BsnDot11EssAclName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 43),
    _BsnDot11EssAclName_Type()
)
bsnDot11EssAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssAclName.setStatus("current")


class _BsnDot11EssAAAOverride_Type(Integer32):
    """Custom type bsnDot11EssAAAOverride based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnDot11EssAAAOverride_Type.__name__ = "Integer32"
_BsnDot11EssAAAOverride_Object = MibTableColumn
bsnDot11EssAAAOverride = _BsnDot11EssAAAOverride_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 44),
    _BsnDot11EssAAAOverride_Type()
)
bsnDot11EssAAAOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssAAAOverride.setStatus("current")


class _BsnDot11EssWPAAuthKeyMgmtMode_Type(Integer32):
    """Custom type bsnDot11EssWPAAuthKeyMgmtMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnDot11EssWPAAuthKeyMgmtMode_Type.__name__ = "Integer32"
_BsnDot11EssWPAAuthKeyMgmtMode_Object = MibTableColumn
bsnDot11EssWPAAuthKeyMgmtMode = _BsnDot11EssWPAAuthKeyMgmtMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 45),
    _BsnDot11EssWPAAuthKeyMgmtMode_Type()
)
bsnDot11EssWPAAuthKeyMgmtMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssWPAAuthKeyMgmtMode.setStatus("deprecated")


class _BsnDot11EssWPAAuthPresharedKey_Type(OctetString):
    """Custom type bsnDot11EssWPAAuthPresharedKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
    )


_BsnDot11EssWPAAuthPresharedKey_Type.__name__ = "OctetString"
_BsnDot11EssWPAAuthPresharedKey_Object = MibTableColumn
bsnDot11EssWPAAuthPresharedKey = _BsnDot11EssWPAAuthPresharedKey_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 46),
    _BsnDot11EssWPAAuthPresharedKey_Type()
)
bsnDot11EssWPAAuthPresharedKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssWPAAuthPresharedKey.setStatus("deprecated")


class _BsnDot11EssFortressSecurity_Type(Integer32):
    """Custom type bsnDot11EssFortressSecurity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnDot11EssFortressSecurity_Type.__name__ = "Integer32"
_BsnDot11EssFortressSecurity_Object = MibTableColumn
bsnDot11EssFortressSecurity = _BsnDot11EssFortressSecurity_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 47),
    _BsnDot11EssFortressSecurity_Type()
)
bsnDot11EssFortressSecurity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssFortressSecurity.setStatus("current")


class _BsnDot11EssWepAllowSharedKeyAuth_Type(Integer32):
    """Custom type bsnDot11EssWepAllowSharedKeyAuth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnDot11EssWepAllowSharedKeyAuth_Type.__name__ = "Integer32"
_BsnDot11EssWepAllowSharedKeyAuth_Object = MibTableColumn
bsnDot11EssWepAllowSharedKeyAuth = _BsnDot11EssWepAllowSharedKeyAuth_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 48),
    _BsnDot11EssWepAllowSharedKeyAuth_Type()
)
bsnDot11EssWepAllowSharedKeyAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssWepAllowSharedKeyAuth.setStatus("current")


class _BsnDot11EssL2tpSecurity_Type(Integer32):
    """Custom type bsnDot11EssL2tpSecurity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnDot11EssL2tpSecurity_Type.__name__ = "Integer32"
_BsnDot11EssL2tpSecurity_Object = MibTableColumn
bsnDot11EssL2tpSecurity = _BsnDot11EssL2tpSecurity_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 49),
    _BsnDot11EssL2tpSecurity_Type()
)
bsnDot11EssL2tpSecurity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssL2tpSecurity.setStatus("current")


class _BsnDot11EssWPAAuthPresharedKeyHex_Type(OctetString):
    """Custom type bsnDot11EssWPAAuthPresharedKeyHex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BsnDot11EssWPAAuthPresharedKeyHex_Type.__name__ = "OctetString"
_BsnDot11EssWPAAuthPresharedKeyHex_Object = MibTableColumn
bsnDot11EssWPAAuthPresharedKeyHex = _BsnDot11EssWPAAuthPresharedKeyHex_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 50),
    _BsnDot11EssWPAAuthPresharedKeyHex_Type()
)
bsnDot11EssWPAAuthPresharedKeyHex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssWPAAuthPresharedKeyHex.setStatus("deprecated")


class _BsnDot11EssBroadcastSsid_Type(Integer32):
    """Custom type bsnDot11EssBroadcastSsid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnDot11EssBroadcastSsid_Type.__name__ = "Integer32"
_BsnDot11EssBroadcastSsid_Object = MibTableColumn
bsnDot11EssBroadcastSsid = _BsnDot11EssBroadcastSsid_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 51),
    _BsnDot11EssBroadcastSsid_Type()
)
bsnDot11EssBroadcastSsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssBroadcastSsid.setStatus("current")


class _BsnDot11EssExternalPolicyValidation_Type(Integer32):
    """Custom type bsnDot11EssExternalPolicyValidation based on Integer32"""
    defaultValue = 1

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


_BsnDot11EssExternalPolicyValidation_Type.__name__ = "Integer32"
_BsnDot11EssExternalPolicyValidation_Object = MibTableColumn
bsnDot11EssExternalPolicyValidation = _BsnDot11EssExternalPolicyValidation_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 52),
    _BsnDot11EssExternalPolicyValidation_Type()
)
bsnDot11EssExternalPolicyValidation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssExternalPolicyValidation.setStatus("current")


class _BsnDot11EssRSNSecurity_Type(Integer32):
    """Custom type bsnDot11EssRSNSecurity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnDot11EssRSNSecurity_Type.__name__ = "Integer32"
_BsnDot11EssRSNSecurity_Object = MibTableColumn
bsnDot11EssRSNSecurity = _BsnDot11EssRSNSecurity_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 53),
    _BsnDot11EssRSNSecurity_Type()
)
bsnDot11EssRSNSecurity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssRSNSecurity.setStatus("deprecated")


class _BsnDot11EssRSNWPACompatibilityMode_Type(Integer32):
    """Custom type bsnDot11EssRSNWPACompatibilityMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnDot11EssRSNWPACompatibilityMode_Type.__name__ = "Integer32"
_BsnDot11EssRSNWPACompatibilityMode_Object = MibTableColumn
bsnDot11EssRSNWPACompatibilityMode = _BsnDot11EssRSNWPACompatibilityMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 54),
    _BsnDot11EssRSNWPACompatibilityMode_Type()
)
bsnDot11EssRSNWPACompatibilityMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssRSNWPACompatibilityMode.setStatus("deprecated")


class _BsnDot11EssRSNAllowTKIPClients_Type(Integer32):
    """Custom type bsnDot11EssRSNAllowTKIPClients based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_BsnDot11EssRSNAllowTKIPClients_Type.__name__ = "Integer32"
_BsnDot11EssRSNAllowTKIPClients_Object = MibTableColumn
bsnDot11EssRSNAllowTKIPClients = _BsnDot11EssRSNAllowTKIPClients_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 55),
    _BsnDot11EssRSNAllowTKIPClients_Type()
)
bsnDot11EssRSNAllowTKIPClients.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssRSNAllowTKIPClients.setStatus("deprecated")


class _BsnDot11EssRSNAuthKeyMgmtMode_Type(Integer32):
    """Custom type bsnDot11EssRSNAuthKeyMgmtMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnDot11EssRSNAuthKeyMgmtMode_Type.__name__ = "Integer32"
_BsnDot11EssRSNAuthKeyMgmtMode_Object = MibTableColumn
bsnDot11EssRSNAuthKeyMgmtMode = _BsnDot11EssRSNAuthKeyMgmtMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 56),
    _BsnDot11EssRSNAuthKeyMgmtMode_Type()
)
bsnDot11EssRSNAuthKeyMgmtMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssRSNAuthKeyMgmtMode.setStatus("deprecated")


class _BsnDot11EssRSNAuthPresharedKey_Type(OctetString):
    """Custom type bsnDot11EssRSNAuthPresharedKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
    )


_BsnDot11EssRSNAuthPresharedKey_Type.__name__ = "OctetString"
_BsnDot11EssRSNAuthPresharedKey_Object = MibTableColumn
bsnDot11EssRSNAuthPresharedKey = _BsnDot11EssRSNAuthPresharedKey_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 57),
    _BsnDot11EssRSNAuthPresharedKey_Type()
)
bsnDot11EssRSNAuthPresharedKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssRSNAuthPresharedKey.setStatus("deprecated")


class _BsnDot11EssRSNAuthPresharedKeyHex_Type(OctetString):
    """Custom type bsnDot11EssRSNAuthPresharedKeyHex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BsnDot11EssRSNAuthPresharedKeyHex_Type.__name__ = "OctetString"
_BsnDot11EssRSNAuthPresharedKeyHex_Object = MibTableColumn
bsnDot11EssRSNAuthPresharedKeyHex = _BsnDot11EssRSNAuthPresharedKeyHex_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 58),
    _BsnDot11EssRSNAuthPresharedKeyHex_Type()
)
bsnDot11EssRSNAuthPresharedKeyHex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssRSNAuthPresharedKeyHex.setStatus("deprecated")


class _BsnDot11EssIPv6Bridging_Type(Integer32):
    """Custom type bsnDot11EssIPv6Bridging based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnDot11EssIPv6Bridging_Type.__name__ = "Integer32"
_BsnDot11EssIPv6Bridging_Object = MibTableColumn
bsnDot11EssIPv6Bridging = _BsnDot11EssIPv6Bridging_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 59),
    _BsnDot11EssIPv6Bridging_Type()
)
bsnDot11EssIPv6Bridging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssIPv6Bridging.setStatus("deprecated")
_BsnDot11EssRowStatus_Type = RowStatus
_BsnDot11EssRowStatus_Object = MibTableColumn
bsnDot11EssRowStatus = _BsnDot11EssRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 60),
    _BsnDot11EssRowStatus_Type()
)
bsnDot11EssRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssRowStatus.setStatus("current")


class _BsnDot11EssWmePolicySetting_Type(Integer32):
    """Custom type bsnDot11EssWmePolicySetting based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disable", 0),
          ("invalid", 3),
          ("required", 2))
    )


_BsnDot11EssWmePolicySetting_Type.__name__ = "Integer32"
_BsnDot11EssWmePolicySetting_Object = MibTableColumn
bsnDot11EssWmePolicySetting = _BsnDot11EssWmePolicySetting_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 61),
    _BsnDot11EssWmePolicySetting_Type()
)
bsnDot11EssWmePolicySetting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssWmePolicySetting.setStatus("current")


class _BsnDot11Ess80211ePolicySetting_Type(Integer32):
    """Custom type bsnDot11Ess80211ePolicySetting based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disable", 0),
          ("invalid", 3),
          ("required", 2))
    )


_BsnDot11Ess80211ePolicySetting_Type.__name__ = "Integer32"
_BsnDot11Ess80211ePolicySetting_Object = MibTableColumn
bsnDot11Ess80211ePolicySetting = _BsnDot11Ess80211ePolicySetting_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 62),
    _BsnDot11Ess80211ePolicySetting_Type()
)
bsnDot11Ess80211ePolicySetting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11Ess80211ePolicySetting.setStatus("current")


class _BsnDot11EssWebPassthroughEmail_Type(Integer32):
    """Custom type bsnDot11EssWebPassthroughEmail based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnDot11EssWebPassthroughEmail_Type.__name__ = "Integer32"
_BsnDot11EssWebPassthroughEmail_Object = MibTableColumn
bsnDot11EssWebPassthroughEmail = _BsnDot11EssWebPassthroughEmail_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 63),
    _BsnDot11EssWebPassthroughEmail_Type()
)
bsnDot11EssWebPassthroughEmail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssWebPassthroughEmail.setStatus("current")


class _BsnDot11Ess7920PhoneSupport_Type(Integer32):
    """Custom type bsnDot11Ess7920PhoneSupport based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("apCacLimit", 2),
          ("both", 3),
          ("clientCacLimit", 1),
          ("disable", 0))
    )


_BsnDot11Ess7920PhoneSupport_Type.__name__ = "Integer32"
_BsnDot11Ess7920PhoneSupport_Object = MibTableColumn
bsnDot11Ess7920PhoneSupport = _BsnDot11Ess7920PhoneSupport_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 64),
    _BsnDot11Ess7920PhoneSupport_Type()
)
bsnDot11Ess7920PhoneSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11Ess7920PhoneSupport.setStatus("current")


class _BsnDot11EssRadiusAuthPrimaryServer_Type(DisplayString):
    """Custom type bsnDot11EssRadiusAuthPrimaryServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_BsnDot11EssRadiusAuthPrimaryServer_Type.__name__ = "DisplayString"
_BsnDot11EssRadiusAuthPrimaryServer_Object = MibTableColumn
bsnDot11EssRadiusAuthPrimaryServer = _BsnDot11EssRadiusAuthPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 95),
    _BsnDot11EssRadiusAuthPrimaryServer_Type()
)
bsnDot11EssRadiusAuthPrimaryServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssRadiusAuthPrimaryServer.setStatus("current")


class _BsnDot11EssRadiusAuthSecondaryServer_Type(DisplayString):
    """Custom type bsnDot11EssRadiusAuthSecondaryServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_BsnDot11EssRadiusAuthSecondaryServer_Type.__name__ = "DisplayString"
_BsnDot11EssRadiusAuthSecondaryServer_Object = MibTableColumn
bsnDot11EssRadiusAuthSecondaryServer = _BsnDot11EssRadiusAuthSecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 96),
    _BsnDot11EssRadiusAuthSecondaryServer_Type()
)
bsnDot11EssRadiusAuthSecondaryServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssRadiusAuthSecondaryServer.setStatus("current")


class _BsnDot11EssRadiusAuthTertiaryServer_Type(DisplayString):
    """Custom type bsnDot11EssRadiusAuthTertiaryServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_BsnDot11EssRadiusAuthTertiaryServer_Type.__name__ = "DisplayString"
_BsnDot11EssRadiusAuthTertiaryServer_Object = MibTableColumn
bsnDot11EssRadiusAuthTertiaryServer = _BsnDot11EssRadiusAuthTertiaryServer_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 97),
    _BsnDot11EssRadiusAuthTertiaryServer_Type()
)
bsnDot11EssRadiusAuthTertiaryServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssRadiusAuthTertiaryServer.setStatus("current")


class _BsnDot11EssRadiusAcctPrimaryServer_Type(DisplayString):
    """Custom type bsnDot11EssRadiusAcctPrimaryServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_BsnDot11EssRadiusAcctPrimaryServer_Type.__name__ = "DisplayString"
_BsnDot11EssRadiusAcctPrimaryServer_Object = MibTableColumn
bsnDot11EssRadiusAcctPrimaryServer = _BsnDot11EssRadiusAcctPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 98),
    _BsnDot11EssRadiusAcctPrimaryServer_Type()
)
bsnDot11EssRadiusAcctPrimaryServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssRadiusAcctPrimaryServer.setStatus("current")


class _BsnDot11EssRadiusAcctSecondaryServer_Type(DisplayString):
    """Custom type bsnDot11EssRadiusAcctSecondaryServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_BsnDot11EssRadiusAcctSecondaryServer_Type.__name__ = "DisplayString"
_BsnDot11EssRadiusAcctSecondaryServer_Object = MibTableColumn
bsnDot11EssRadiusAcctSecondaryServer = _BsnDot11EssRadiusAcctSecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 99),
    _BsnDot11EssRadiusAcctSecondaryServer_Type()
)
bsnDot11EssRadiusAcctSecondaryServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssRadiusAcctSecondaryServer.setStatus("current")


class _BsnDot11EssRadiusAcctTertiaryServer_Type(DisplayString):
    """Custom type bsnDot11EssRadiusAcctTertiaryServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_BsnDot11EssRadiusAcctTertiaryServer_Type.__name__ = "DisplayString"
_BsnDot11EssRadiusAcctTertiaryServer_Object = MibTableColumn
bsnDot11EssRadiusAcctTertiaryServer = _BsnDot11EssRadiusAcctTertiaryServer_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 1, 1, 100),
    _BsnDot11EssRadiusAcctTertiaryServer_Type()
)
bsnDot11EssRadiusAcctTertiaryServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnDot11EssRadiusAcctTertiaryServer.setStatus("current")
_BsnMobileStationTable_Object = MibTable
bsnMobileStationTable = _BsnMobileStationTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4)
)
if mibBuilder.loadTexts:
    bsnMobileStationTable.setStatus("current")
_BsnMobileStationEntry_Object = MibTableRow
bsnMobileStationEntry = _BsnMobileStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1)
)
bsnMobileStationEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnMobileStationMacAddress"),
)
if mibBuilder.loadTexts:
    bsnMobileStationEntry.setStatus("current")
_BsnMobileStationMacAddress_Type = MacAddress
_BsnMobileStationMacAddress_Object = MibTableColumn
bsnMobileStationMacAddress = _BsnMobileStationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 1),
    _BsnMobileStationMacAddress_Type()
)
bsnMobileStationMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationMacAddress.setStatus("current")
_BsnMobileStationIpAddress_Type = IpAddress
_BsnMobileStationIpAddress_Object = MibTableColumn
bsnMobileStationIpAddress = _BsnMobileStationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 2),
    _BsnMobileStationIpAddress_Type()
)
bsnMobileStationIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationIpAddress.setStatus("current")
_BsnMobileStationUserName_Type = DisplayString
_BsnMobileStationUserName_Object = MibTableColumn
bsnMobileStationUserName = _BsnMobileStationUserName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 3),
    _BsnMobileStationUserName_Type()
)
bsnMobileStationUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationUserName.setStatus("current")
_BsnMobileStationAPMacAddr_Type = MacAddress
_BsnMobileStationAPMacAddr_Object = MibTableColumn
bsnMobileStationAPMacAddr = _BsnMobileStationAPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 4),
    _BsnMobileStationAPMacAddr_Type()
)
bsnMobileStationAPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationAPMacAddr.setStatus("current")


class _BsnMobileStationAPIfSlotId_Type(Integer32):
    """Custom type bsnMobileStationAPIfSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_BsnMobileStationAPIfSlotId_Type.__name__ = "Integer32"
_BsnMobileStationAPIfSlotId_Object = MibTableColumn
bsnMobileStationAPIfSlotId = _BsnMobileStationAPIfSlotId_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 5),
    _BsnMobileStationAPIfSlotId_Type()
)
bsnMobileStationAPIfSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationAPIfSlotId.setStatus("current")


class _BsnMobileStationEssIndex_Type(Integer32):
    """Custom type bsnMobileStationEssIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_BsnMobileStationEssIndex_Type.__name__ = "Integer32"
_BsnMobileStationEssIndex_Object = MibTableColumn
bsnMobileStationEssIndex = _BsnMobileStationEssIndex_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 6),
    _BsnMobileStationEssIndex_Type()
)
bsnMobileStationEssIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationEssIndex.setStatus("current")
_BsnMobileStationSsid_Type = DisplayString
_BsnMobileStationSsid_Object = MibTableColumn
bsnMobileStationSsid = _BsnMobileStationSsid_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 7),
    _BsnMobileStationSsid_Type()
)
bsnMobileStationSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationSsid.setStatus("current")
_BsnMobileStationAID_Type = Unsigned32
_BsnMobileStationAID_Object = MibTableColumn
bsnMobileStationAID = _BsnMobileStationAID_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 8),
    _BsnMobileStationAID_Type()
)
bsnMobileStationAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationAID.setStatus("current")


class _BsnMobileStationStatus_Type(Integer32):
    """Custom type bsnMobileStationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("aaaPending", 1),
          ("associated", 3),
          ("authenticated", 2),
          ("blacklisted", 8),
          ("disassociated", 5),
          ("idle", 0),
          ("powersave", 4),
          ("probing", 7),
          ("tobedeleted", 6))
    )


_BsnMobileStationStatus_Type.__name__ = "Integer32"
_BsnMobileStationStatus_Object = MibTableColumn
bsnMobileStationStatus = _BsnMobileStationStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 9),
    _BsnMobileStationStatus_Type()
)
bsnMobileStationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationStatus.setStatus("current")


class _BsnMobileStationReasonCode_Type(Integer32):
    """Custom type bsnMobileStationReasonCode based on Integer32"""
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
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              99,
              101,
              105,
              106,
              200,
              201,
              202,
              203)
        )
    )
    namedValues = NamedValues(
        *(("akmpInvalid", 43),
          ("cipherSuiteRejected", 46),
          ("class2FrameFromNonAssStation", 7),
          ("class2FrameFromNonAuthStation", 6),
          ("deauthenticationLeaving", 3),
          ("disassociationAPBusy", 5),
          ("disassociationDueToInactivity", 4),
          ("disassociationStaHasLeft", 8),
          ("groupCipherInvalid", 41),
          ("inSufficientBandwidth", 202),
          ("inValidQosParams", 203),
          ("invalidInformationElement", 40),
          ("invalidRsnIeCapabilities", 45),
          ("maxAssociatedClientsReached", 101),
          ("maxAssociatedClientsReachedOnRadio", 105),
          ("maxAssociatedClientsReachedOnWlan", 106),
          ("missingReasonCode", 99),
          ("previousAuthNotValid", 2),
          ("qosPolicyMismatch", 201),
          ("staReqAssociationWithoutAuth", 9),
          ("unSpecifiedQosFailure", 200),
          ("unicastCipherInvalid", 42),
          ("unspecified", 1),
          ("unsupportedRsnVersion", 44))
    )


_BsnMobileStationReasonCode_Type.__name__ = "Integer32"
_BsnMobileStationReasonCode_Object = MibTableColumn
bsnMobileStationReasonCode = _BsnMobileStationReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 10),
    _BsnMobileStationReasonCode_Type()
)
bsnMobileStationReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationReasonCode.setStatus("current")


class _BsnMobileStationMobilityStatus_Type(Integer32):
    """Custom type bsnMobileStationMobilityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("anchor", 2),
          ("exportanchor", 6),
          ("exportforeign", 7),
          ("foreign", 3),
          ("handoff", 4),
          ("local", 1),
          ("unassociated", 0),
          ("unknown", 5))
    )


_BsnMobileStationMobilityStatus_Type.__name__ = "Integer32"
_BsnMobileStationMobilityStatus_Object = MibTableColumn
bsnMobileStationMobilityStatus = _BsnMobileStationMobilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 11),
    _BsnMobileStationMobilityStatus_Type()
)
bsnMobileStationMobilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationMobilityStatus.setStatus("current")
_BsnMobileStationAnchorAddress_Type = IpAddress
_BsnMobileStationAnchorAddress_Object = MibTableColumn
bsnMobileStationAnchorAddress = _BsnMobileStationAnchorAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 12),
    _BsnMobileStationAnchorAddress_Type()
)
bsnMobileStationAnchorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationAnchorAddress.setStatus("current")


class _BsnMobileStationCFPollable_Type(Integer32):
    """Custom type bsnMobileStationCFPollable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("implemented", 1),
          ("notimplemented", 0))
    )


_BsnMobileStationCFPollable_Type.__name__ = "Integer32"
_BsnMobileStationCFPollable_Object = MibTableColumn
bsnMobileStationCFPollable = _BsnMobileStationCFPollable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 13),
    _BsnMobileStationCFPollable_Type()
)
bsnMobileStationCFPollable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationCFPollable.setStatus("current")


class _BsnMobileStationCFPollRequest_Type(Integer32):
    """Custom type bsnMobileStationCFPollRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("implemented", 1),
          ("notimplemented", 0))
    )


_BsnMobileStationCFPollRequest_Type.__name__ = "Integer32"
_BsnMobileStationCFPollRequest_Object = MibTableColumn
bsnMobileStationCFPollRequest = _BsnMobileStationCFPollRequest_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 14),
    _BsnMobileStationCFPollRequest_Type()
)
bsnMobileStationCFPollRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationCFPollRequest.setStatus("current")


class _BsnMobileStationChannelAgilityEnabled_Type(Integer32):
    """Custom type bsnMobileStationChannelAgilityEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("implemented", 1),
          ("notimplemented", 0))
    )


_BsnMobileStationChannelAgilityEnabled_Type.__name__ = "Integer32"
_BsnMobileStationChannelAgilityEnabled_Object = MibTableColumn
bsnMobileStationChannelAgilityEnabled = _BsnMobileStationChannelAgilityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 15),
    _BsnMobileStationChannelAgilityEnabled_Type()
)
bsnMobileStationChannelAgilityEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationChannelAgilityEnabled.setStatus("current")


class _BsnMobileStationPBCCOptionImplemented_Type(Integer32):
    """Custom type bsnMobileStationPBCCOptionImplemented based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("implemented", 1),
          ("notimplemented", 0))
    )


_BsnMobileStationPBCCOptionImplemented_Type.__name__ = "Integer32"
_BsnMobileStationPBCCOptionImplemented_Object = MibTableColumn
bsnMobileStationPBCCOptionImplemented = _BsnMobileStationPBCCOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 16),
    _BsnMobileStationPBCCOptionImplemented_Type()
)
bsnMobileStationPBCCOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationPBCCOptionImplemented.setStatus("current")


class _BsnMobileStationShortPreambleOptionImplemented_Type(Integer32):
    """Custom type bsnMobileStationShortPreambleOptionImplemented based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("implemented", 1),
          ("notimplemented", 0))
    )


_BsnMobileStationShortPreambleOptionImplemented_Type.__name__ = "Integer32"
_BsnMobileStationShortPreambleOptionImplemented_Object = MibTableColumn
bsnMobileStationShortPreambleOptionImplemented = _BsnMobileStationShortPreambleOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 17),
    _BsnMobileStationShortPreambleOptionImplemented_Type()
)
bsnMobileStationShortPreambleOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationShortPreambleOptionImplemented.setStatus("current")
_BsnMobileStationSessionTimeout_Type = Unsigned32
_BsnMobileStationSessionTimeout_Object = MibTableColumn
bsnMobileStationSessionTimeout = _BsnMobileStationSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 18),
    _BsnMobileStationSessionTimeout_Type()
)
bsnMobileStationSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationSessionTimeout.setStatus("current")


class _BsnMobileStationAuthenticationAlgorithm_Type(Integer32):
    """Custom type bsnMobileStationAuthenticationAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              128)
        )
    )
    namedValues = NamedValues(
        *(("openAndEap", 128),
          ("openSystem", 0),
          ("sharedKey", 1),
          ("unknown", 2))
    )


_BsnMobileStationAuthenticationAlgorithm_Type.__name__ = "Integer32"
_BsnMobileStationAuthenticationAlgorithm_Object = MibTableColumn
bsnMobileStationAuthenticationAlgorithm = _BsnMobileStationAuthenticationAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 19),
    _BsnMobileStationAuthenticationAlgorithm_Type()
)
bsnMobileStationAuthenticationAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationAuthenticationAlgorithm.setStatus("current")


class _BsnMobileStationWepState_Type(Integer32):
    """Custom type bsnMobileStationWepState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_BsnMobileStationWepState_Type.__name__ = "Integer32"
_BsnMobileStationWepState_Object = MibTableColumn
bsnMobileStationWepState = _BsnMobileStationWepState_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 20),
    _BsnMobileStationWepState_Type()
)
bsnMobileStationWepState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationWepState.setStatus("current")
_BsnMobileStationPortNumber_Type = Unsigned32
_BsnMobileStationPortNumber_Object = MibTableColumn
bsnMobileStationPortNumber = _BsnMobileStationPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 21),
    _BsnMobileStationPortNumber_Type()
)
bsnMobileStationPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationPortNumber.setStatus("current")


class _BsnMobileStationDeleteAction_Type(Integer32):
    """Custom type bsnMobileStationDeleteAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("delete", 1))
    )


_BsnMobileStationDeleteAction_Type.__name__ = "Integer32"
_BsnMobileStationDeleteAction_Object = MibTableColumn
bsnMobileStationDeleteAction = _BsnMobileStationDeleteAction_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 22),
    _BsnMobileStationDeleteAction_Type()
)
bsnMobileStationDeleteAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnMobileStationDeleteAction.setStatus("current")
_BsnMobileStationPolicyManagerState_Type = DisplayString
_BsnMobileStationPolicyManagerState_Object = MibTableColumn
bsnMobileStationPolicyManagerState = _BsnMobileStationPolicyManagerState_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 23),
    _BsnMobileStationPolicyManagerState_Type()
)
bsnMobileStationPolicyManagerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationPolicyManagerState.setStatus("current")


class _BsnMobileStationSecurityPolicyStatus_Type(Integer32):
    """Custom type bsnMobileStationSecurityPolicyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("completed", 0),
          ("notcompleted", 1))
    )


_BsnMobileStationSecurityPolicyStatus_Type.__name__ = "Integer32"
_BsnMobileStationSecurityPolicyStatus_Object = MibTableColumn
bsnMobileStationSecurityPolicyStatus = _BsnMobileStationSecurityPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 24),
    _BsnMobileStationSecurityPolicyStatus_Type()
)
bsnMobileStationSecurityPolicyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationSecurityPolicyStatus.setStatus("current")


class _BsnMobileStationProtocol_Type(Integer32):
    """Custom type bsnMobileStationProtocol based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 1),
          ("dot11b", 2),
          ("dot11g", 3),
          ("dot11n24", 6),
          ("dot11n5", 7),
          ("dot3", 9),
          ("ethernet", 8),
          ("mobile", 5),
          ("unknown", 4))
    )


_BsnMobileStationProtocol_Type.__name__ = "Integer32"
_BsnMobileStationProtocol_Object = MibTableColumn
bsnMobileStationProtocol = _BsnMobileStationProtocol_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 25),
    _BsnMobileStationProtocol_Type()
)
bsnMobileStationProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationProtocol.setStatus("current")


class _BsnMobileStationMirrorMode_Type(Integer32):
    """Custom type bsnMobileStationMirrorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnMobileStationMirrorMode_Type.__name__ = "Integer32"
_BsnMobileStationMirrorMode_Object = MibTableColumn
bsnMobileStationMirrorMode = _BsnMobileStationMirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 26),
    _BsnMobileStationMirrorMode_Type()
)
bsnMobileStationMirrorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnMobileStationMirrorMode.setStatus("current")


class _BsnMobileStationInterface_Type(DisplayString):
    """Custom type bsnMobileStationInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BsnMobileStationInterface_Type.__name__ = "DisplayString"
_BsnMobileStationInterface_Object = MibTableColumn
bsnMobileStationInterface = _BsnMobileStationInterface_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 27),
    _BsnMobileStationInterface_Type()
)
bsnMobileStationInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationInterface.setStatus("current")


class _BsnMobileStationApMode_Type(Integer32):
    """Custom type bsnMobileStationApMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("monitor", 1),
          ("remote", 2),
          ("roguedetector", 3))
    )


_BsnMobileStationApMode_Type.__name__ = "Integer32"
_BsnMobileStationApMode_Object = MibTableColumn
bsnMobileStationApMode = _BsnMobileStationApMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 28),
    _BsnMobileStationApMode_Type()
)
bsnMobileStationApMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationApMode.setStatus("current")


class _BsnMobileStationVlanId_Type(Integer32):
    """Custom type bsnMobileStationVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_BsnMobileStationVlanId_Type.__name__ = "Integer32"
_BsnMobileStationVlanId_Object = MibTableColumn
bsnMobileStationVlanId = _BsnMobileStationVlanId_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 29),
    _BsnMobileStationVlanId_Type()
)
bsnMobileStationVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationVlanId.setStatus("current")


class _BsnMobileStationPolicyType_Type(Integer32):
    """Custom type bsnMobileStationPolicyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dot1x", 0),
          ("notavailable", 4),
          ("unknown", 5),
          ("wapi", 6),
          ("wpa1", 1),
          ("wpa2", 2),
          ("wpa2vff", 3))
    )


_BsnMobileStationPolicyType_Type.__name__ = "Integer32"
_BsnMobileStationPolicyType_Object = MibTableColumn
bsnMobileStationPolicyType = _BsnMobileStationPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 30),
    _BsnMobileStationPolicyType_Type()
)
bsnMobileStationPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationPolicyType.setStatus("current")


class _BsnMobileStationEncryptionCypher_Type(Integer32):
    """Custom type bsnMobileStationEncryptionCypher based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("ccmpAes", 0),
          ("none", 5),
          ("notavailable", 6),
          ("tkipMic", 1),
          ("unknown", 7),
          ("wapiSMS4", 8),
          ("wep104", 3),
          ("wep128", 4),
          ("wep40", 2))
    )


_BsnMobileStationEncryptionCypher_Type.__name__ = "Integer32"
_BsnMobileStationEncryptionCypher_Object = MibTableColumn
bsnMobileStationEncryptionCypher = _BsnMobileStationEncryptionCypher_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 31),
    _BsnMobileStationEncryptionCypher_Type()
)
bsnMobileStationEncryptionCypher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationEncryptionCypher.setStatus("current")


class _BsnMobileStationEapType_Type(Integer32):
    """Custom type bsnMobileStationEapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("eapFast", 5),
          ("eapTls", 0),
          ("leap", 3),
          ("notavailable", 6),
          ("peap", 2),
          ("speke", 4),
          ("ttls", 1),
          ("unknown", 7))
    )


_BsnMobileStationEapType_Type.__name__ = "Integer32"
_BsnMobileStationEapType_Object = MibTableColumn
bsnMobileStationEapType = _BsnMobileStationEapType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 32),
    _BsnMobileStationEapType_Type()
)
bsnMobileStationEapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationEapType.setStatus("current")


class _BsnMobileStationCcxVersion_Type(Integer32):
    """Custom type bsnMobileStationCcxVersion based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ccxv1", 1),
          ("ccxv2", 2),
          ("ccxv3", 3),
          ("ccxv4", 4),
          ("ccxv5", 5),
          ("ccxv6", 6),
          ("notSupported", 0))
    )


_BsnMobileStationCcxVersion_Type.__name__ = "Integer32"
_BsnMobileStationCcxVersion_Object = MibTableColumn
bsnMobileStationCcxVersion = _BsnMobileStationCcxVersion_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 33),
    _BsnMobileStationCcxVersion_Type()
)
bsnMobileStationCcxVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationCcxVersion.setStatus("current")


class _BsnMobileStationE2eVersion_Type(Integer32):
    """Custom type bsnMobileStationE2eVersion based on Integer32"""
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
        *(("e2ev1", 1),
          ("e2ev2", 2),
          ("notSupported", 0))
    )


_BsnMobileStationE2eVersion_Type.__name__ = "Integer32"
_BsnMobileStationE2eVersion_Object = MibTableColumn
bsnMobileStationE2eVersion = _BsnMobileStationE2eVersion_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 34),
    _BsnMobileStationE2eVersion_Type()
)
bsnMobileStationE2eVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationE2eVersion.setStatus("current")


class _BsnMobileStationStatusCode_Type(Integer32):
    """Custom type bsnMobileStationStatusCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BsnMobileStationStatusCode_Type.__name__ = "Integer32"
_BsnMobileStationStatusCode_Object = MibTableColumn
bsnMobileStationStatusCode = _BsnMobileStationStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 4, 1, 42),
    _BsnMobileStationStatusCode_Type()
)
bsnMobileStationStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationStatusCode.setStatus("current")
_BsnMobileStationPerRadioPerVapTable_Object = MibTable
bsnMobileStationPerRadioPerVapTable = _BsnMobileStationPerRadioPerVapTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 5)
)
if mibBuilder.loadTexts:
    bsnMobileStationPerRadioPerVapTable.setStatus("current")
_BsnMobileStationPerRadioPerVapEntry_Object = MibTableRow
bsnMobileStationPerRadioPerVapEntry = _BsnMobileStationPerRadioPerVapEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 5, 1)
)
bsnMobileStationPerRadioPerVapEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnDot11EssIndex"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnMobileStationPerRadioPerVapIndex"),
)
if mibBuilder.loadTexts:
    bsnMobileStationPerRadioPerVapEntry.setStatus("current")
_BsnMobileStationPerRadioPerVapIndex_Type = Integer32
_BsnMobileStationPerRadioPerVapIndex_Object = MibTableColumn
bsnMobileStationPerRadioPerVapIndex = _BsnMobileStationPerRadioPerVapIndex_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 5, 1, 1),
    _BsnMobileStationPerRadioPerVapIndex_Type()
)
bsnMobileStationPerRadioPerVapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationPerRadioPerVapIndex.setStatus("current")
_BsnMobileStationMacAddr_Type = MacAddress
_BsnMobileStationMacAddr_Object = MibTableColumn
bsnMobileStationMacAddr = _BsnMobileStationMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 5, 1, 20),
    _BsnMobileStationMacAddr_Type()
)
bsnMobileStationMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationMacAddr.setStatus("current")
_BsnMobileStationStatsTable_Object = MibTable
bsnMobileStationStatsTable = _BsnMobileStationStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 6)
)
if mibBuilder.loadTexts:
    bsnMobileStationStatsTable.setStatus("current")
_BsnMobileStationStatsEntry_Object = MibTableRow
bsnMobileStationStatsEntry = _BsnMobileStationStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 6, 1)
)
bsnMobileStationStatsEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnMobileStationMacAddress"),
)
if mibBuilder.loadTexts:
    bsnMobileStationStatsEntry.setStatus("current")
_BsnMobileStationRSSI_Type = Integer32
_BsnMobileStationRSSI_Object = MibTableColumn
bsnMobileStationRSSI = _BsnMobileStationRSSI_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 6, 1, 1),
    _BsnMobileStationRSSI_Type()
)
bsnMobileStationRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationRSSI.setStatus("current")
_BsnMobileStationBytesReceived_Type = Counter64
_BsnMobileStationBytesReceived_Object = MibTableColumn
bsnMobileStationBytesReceived = _BsnMobileStationBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 6, 1, 2),
    _BsnMobileStationBytesReceived_Type()
)
bsnMobileStationBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationBytesReceived.setStatus("current")
_BsnMobileStationBytesSent_Type = Counter64
_BsnMobileStationBytesSent_Object = MibTableColumn
bsnMobileStationBytesSent = _BsnMobileStationBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 6, 1, 3),
    _BsnMobileStationBytesSent_Type()
)
bsnMobileStationBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationBytesSent.setStatus("current")
_BsnMobileStationPolicyErrors_Type = Counter64
_BsnMobileStationPolicyErrors_Object = MibTableColumn
bsnMobileStationPolicyErrors = _BsnMobileStationPolicyErrors_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 6, 1, 4),
    _BsnMobileStationPolicyErrors_Type()
)
bsnMobileStationPolicyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationPolicyErrors.setStatus("current")
_BsnMobileStationPacketsReceived_Type = Counter64
_BsnMobileStationPacketsReceived_Object = MibTableColumn
bsnMobileStationPacketsReceived = _BsnMobileStationPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 6, 1, 5),
    _BsnMobileStationPacketsReceived_Type()
)
bsnMobileStationPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationPacketsReceived.setStatus("current")
_BsnMobileStationPacketsSent_Type = Counter64
_BsnMobileStationPacketsSent_Object = MibTableColumn
bsnMobileStationPacketsSent = _BsnMobileStationPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 6, 1, 6),
    _BsnMobileStationPacketsSent_Type()
)
bsnMobileStationPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationPacketsSent.setStatus("current")
_BsnMobileStationSnr_Type = Integer32
_BsnMobileStationSnr_Object = MibTableColumn
bsnMobileStationSnr = _BsnMobileStationSnr_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 6, 1, 26),
    _BsnMobileStationSnr_Type()
)
bsnMobileStationSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationSnr.setStatus("current")
_BsnRogueAPTable_Object = MibTable
bsnRogueAPTable = _BsnRogueAPTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 7)
)
if mibBuilder.loadTexts:
    bsnRogueAPTable.setStatus("current")
_BsnRogueAPEntry_Object = MibTableRow
bsnRogueAPEntry = _BsnRogueAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 7, 1)
)
bsnRogueAPEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnRogueAPDot11MacAddress"),
)
if mibBuilder.loadTexts:
    bsnRogueAPEntry.setStatus("current")
_BsnRogueAPDot11MacAddress_Type = MacAddress
_BsnRogueAPDot11MacAddress_Object = MibTableColumn
bsnRogueAPDot11MacAddress = _BsnRogueAPDot11MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 7, 1, 1),
    _BsnRogueAPDot11MacAddress_Type()
)
bsnRogueAPDot11MacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRogueAPDot11MacAddress.setStatus("current")
_BsnRogueAPTotalDetectingAPs_Type = Integer32
_BsnRogueAPTotalDetectingAPs_Object = MibTableColumn
bsnRogueAPTotalDetectingAPs = _BsnRogueAPTotalDetectingAPs_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 7, 1, 2),
    _BsnRogueAPTotalDetectingAPs_Type()
)
bsnRogueAPTotalDetectingAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPTotalDetectingAPs.setStatus("current")
_BsnRogueAPFirstReported_Type = DisplayString
_BsnRogueAPFirstReported_Object = MibTableColumn
bsnRogueAPFirstReported = _BsnRogueAPFirstReported_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 7, 1, 3),
    _BsnRogueAPFirstReported_Type()
)
bsnRogueAPFirstReported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPFirstReported.setStatus("current")
_BsnRogueAPLastReported_Type = DisplayString
_BsnRogueAPLastReported_Object = MibTableColumn
bsnRogueAPLastReported = _BsnRogueAPLastReported_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 7, 1, 4),
    _BsnRogueAPLastReported_Type()
)
bsnRogueAPLastReported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPLastReported.setStatus("current")


class _BsnRogueAPContainmentLevel_Type(Integer32):
    """Custom type bsnRogueAPContainmentLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4),
          ("unassigned", 0))
    )


_BsnRogueAPContainmentLevel_Type.__name__ = "Integer32"
_BsnRogueAPContainmentLevel_Object = MibTableColumn
bsnRogueAPContainmentLevel = _BsnRogueAPContainmentLevel_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 7, 1, 5),
    _BsnRogueAPContainmentLevel_Type()
)
bsnRogueAPContainmentLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRogueAPContainmentLevel.setStatus("current")


class _BsnRogueAPType_Type(Integer32):
    """Custom type bsnRogueAPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("adhoc", 1),
          ("ap", 0))
    )


_BsnRogueAPType_Type.__name__ = "Integer32"
_BsnRogueAPType_Object = MibTableColumn
bsnRogueAPType = _BsnRogueAPType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 7, 1, 6),
    _BsnRogueAPType_Type()
)
bsnRogueAPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPType.setStatus("current")


class _BsnRogueAPOnNetwork_Type(Integer32):
    """Custom type bsnRogueAPOnNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_BsnRogueAPOnNetwork_Type.__name__ = "Integer32"
_BsnRogueAPOnNetwork_Object = MibTableColumn
bsnRogueAPOnNetwork = _BsnRogueAPOnNetwork_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 7, 1, 7),
    _BsnRogueAPOnNetwork_Type()
)
bsnRogueAPOnNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPOnNetwork.setStatus("current")
_BsnRogueAPTotalClients_Type = Integer32
_BsnRogueAPTotalClients_Object = MibTableColumn
bsnRogueAPTotalClients = _BsnRogueAPTotalClients_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 7, 1, 8),
    _BsnRogueAPTotalClients_Type()
)
bsnRogueAPTotalClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPTotalClients.setStatus("current")
_BsnRogueAPRowStatus_Type = RowStatus
_BsnRogueAPRowStatus_Object = MibTableColumn
bsnRogueAPRowStatus = _BsnRogueAPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 7, 1, 9),
    _BsnRogueAPRowStatus_Type()
)
bsnRogueAPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRogueAPRowStatus.setStatus("current")
_BsnRogueAPMaxDetectedRSSI_Type = Integer32
_BsnRogueAPMaxDetectedRSSI_Object = MibTableColumn
bsnRogueAPMaxDetectedRSSI = _BsnRogueAPMaxDetectedRSSI_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 7, 1, 10),
    _BsnRogueAPMaxDetectedRSSI_Type()
)
bsnRogueAPMaxDetectedRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPMaxDetectedRSSI.setStatus("current")


class _BsnRogueAPSSID_Type(DisplayString):
    """Custom type bsnRogueAPSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BsnRogueAPSSID_Type.__name__ = "DisplayString"
_BsnRogueAPSSID_Object = MibTableColumn
bsnRogueAPSSID = _BsnRogueAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 7, 1, 11),
    _BsnRogueAPSSID_Type()
)
bsnRogueAPSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPSSID.setStatus("current")


class _BsnRogueAPDetectingAPRadioType_Type(Bits):
    """Custom type bsnRogueAPDetectingAPRadioType based on Bits"""
    namedValues = NamedValues(
        *(("dot11a", 1),
          ("dot11abgn", 5),
          ("dot11ac", 6),
          ("dot11b", 0),
          ("dot11g", 2),
          ("dot11n24", 3),
          ("dot11n5", 4))
    )

_BsnRogueAPDetectingAPRadioType_Type.__name__ = "Bits"
_BsnRogueAPDetectingAPRadioType_Object = MibTableColumn
bsnRogueAPDetectingAPRadioType = _BsnRogueAPDetectingAPRadioType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 7, 1, 12),
    _BsnRogueAPDetectingAPRadioType_Type()
)
bsnRogueAPDetectingAPRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPDetectingAPRadioType.setStatus("current")
_BsnRogueAPDetectingAPMacAddress_Type = MacAddress
_BsnRogueAPDetectingAPMacAddress_Object = MibTableColumn
bsnRogueAPDetectingAPMacAddress = _BsnRogueAPDetectingAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 7, 1, 13),
    _BsnRogueAPDetectingAPMacAddress_Type()
)
bsnRogueAPDetectingAPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPDetectingAPMacAddress.setStatus("current")


class _BsnRogueAPMaxRssiRadioType_Type(Integer32):
    """Custom type bsnRogueAPMaxRssiRadioType based on Integer32"""
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
        *(("dot11a", 2),
          ("dot11abgn", 3),
          ("dot11ac", 8),
          ("dot11b", 1),
          ("dot11g", 5),
          ("dot11n24", 6),
          ("dot11n5", 7),
          ("uwb", 4))
    )


_BsnRogueAPMaxRssiRadioType_Type.__name__ = "Integer32"
_BsnRogueAPMaxRssiRadioType_Object = MibTableColumn
bsnRogueAPMaxRssiRadioType = _BsnRogueAPMaxRssiRadioType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 7, 1, 14),
    _BsnRogueAPMaxRssiRadioType_Type()
)
bsnRogueAPMaxRssiRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPMaxRssiRadioType.setStatus("current")


class _BsnRogueAPState_Type(Integer32):
    """Custom type bsnRogueAPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("acknowledge", 5),
          ("alert", 2),
          ("contained", 6),
          ("containedPending", 8),
          ("detectedLrad", 3),
          ("initializing", 0),
          ("known", 4),
          ("knownContained", 9),
          ("pending", 1),
          ("threat", 7),
          ("trustedMissing", 10))
    )


_BsnRogueAPState_Type.__name__ = "Integer32"
_BsnRogueAPState_Object = MibTableColumn
bsnRogueAPState = _BsnRogueAPState_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 7, 1, 24),
    _BsnRogueAPState_Type()
)
bsnRogueAPState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRogueAPState.setStatus("current")


class _BsnRogueAPClassType_Type(Integer32):
    """Custom type bsnRogueAPClassType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("custom", 4),
          ("friendly", 1),
          ("malicious", 2),
          ("pending", 0),
          ("unclassified", 3))
    )


_BsnRogueAPClassType_Type.__name__ = "Integer32"
_BsnRogueAPClassType_Object = MibTableColumn
bsnRogueAPClassType = _BsnRogueAPClassType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 7, 1, 25),
    _BsnRogueAPClassType_Type()
)
bsnRogueAPClassType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRogueAPClassType.setStatus("current")
_BsnRogueAPChannel_Type = Integer32
_BsnRogueAPChannel_Object = MibTableColumn
bsnRogueAPChannel = _BsnRogueAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 7, 1, 26),
    _BsnRogueAPChannel_Type()
)
bsnRogueAPChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPChannel.setStatus("current")


class _BsnRogueAPDetectingAPName_Type(OctetString):
    """Custom type bsnRogueAPDetectingAPName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BsnRogueAPDetectingAPName_Type.__name__ = "OctetString"
_BsnRogueAPDetectingAPName_Object = MibTableColumn
bsnRogueAPDetectingAPName = _BsnRogueAPDetectingAPName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 7, 1, 27),
    _BsnRogueAPDetectingAPName_Type()
)
bsnRogueAPDetectingAPName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRogueAPDetectingAPName.setStatus("current")
_BsnRogueAPAirespaceAPTable_Object = MibTable
bsnRogueAPAirespaceAPTable = _BsnRogueAPAirespaceAPTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 8)
)
if mibBuilder.loadTexts:
    bsnRogueAPAirespaceAPTable.setStatus("current")
_BsnRogueAPAirespaceAPEntry_Object = MibTableRow
bsnRogueAPAirespaceAPEntry = _BsnRogueAPAirespaceAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 8, 1)
)
bsnRogueAPAirespaceAPEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnRogueAPDot11MacAddress"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnRogueAPAirespaceAPMacAddress"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnRogueAPAirespaceAPSlotId"),
)
if mibBuilder.loadTexts:
    bsnRogueAPAirespaceAPEntry.setStatus("current")
_BsnRogueAPAirespaceAPMacAddress_Type = MacAddress
_BsnRogueAPAirespaceAPMacAddress_Object = MibTableColumn
bsnRogueAPAirespaceAPMacAddress = _BsnRogueAPAirespaceAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 8, 1, 1),
    _BsnRogueAPAirespaceAPMacAddress_Type()
)
bsnRogueAPAirespaceAPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPAirespaceAPMacAddress.setStatus("current")


class _BsnRogueAPAirespaceAPSlotId_Type(Unsigned32):
    """Custom type bsnRogueAPAirespaceAPSlotId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BsnRogueAPAirespaceAPSlotId_Type.__name__ = "Unsigned32"
_BsnRogueAPAirespaceAPSlotId_Object = MibTableColumn
bsnRogueAPAirespaceAPSlotId = _BsnRogueAPAirespaceAPSlotId_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 8, 1, 2),
    _BsnRogueAPAirespaceAPSlotId_Type()
)
bsnRogueAPAirespaceAPSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPAirespaceAPSlotId.setStatus("current")


class _BsnRogueAPRadioType_Type(Integer32):
    """Custom type bsnRogueAPRadioType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 2),
          ("dot11abgn", 3),
          ("dot11ac", 9),
          ("dot11b", 1),
          ("dot11g", 5),
          ("dot11n24", 6),
          ("dot11n5", 7),
          ("unknown", 8),
          ("uwb", 4))
    )


_BsnRogueAPRadioType_Type.__name__ = "Integer32"
_BsnRogueAPRadioType_Object = MibTableColumn
bsnRogueAPRadioType = _BsnRogueAPRadioType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 8, 1, 3),
    _BsnRogueAPRadioType_Type()
)
bsnRogueAPRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPRadioType.setStatus("current")
_BsnRogueAPAirespaceAPName_Type = DisplayString
_BsnRogueAPAirespaceAPName_Object = MibTableColumn
bsnRogueAPAirespaceAPName = _BsnRogueAPAirespaceAPName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 8, 1, 4),
    _BsnRogueAPAirespaceAPName_Type()
)
bsnRogueAPAirespaceAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPAirespaceAPName.setStatus("current")
_BsnRogueAPChannelNumber_Type = Integer32
_BsnRogueAPChannelNumber_Object = MibTableColumn
bsnRogueAPChannelNumber = _BsnRogueAPChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 8, 1, 5),
    _BsnRogueAPChannelNumber_Type()
)
bsnRogueAPChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPChannelNumber.setStatus("current")
_BsnRogueAPSsid_Type = DisplayString
_BsnRogueAPSsid_Object = MibTableColumn
bsnRogueAPSsid = _BsnRogueAPSsid_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 8, 1, 6),
    _BsnRogueAPSsid_Type()
)
bsnRogueAPSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPSsid.setStatus("current")
_BsnRogueAPAirespaceAPRSSI_Type = Integer32
_BsnRogueAPAirespaceAPRSSI_Object = MibTableColumn
bsnRogueAPAirespaceAPRSSI = _BsnRogueAPAirespaceAPRSSI_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 8, 1, 7),
    _BsnRogueAPAirespaceAPRSSI_Type()
)
bsnRogueAPAirespaceAPRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPAirespaceAPRSSI.setStatus("current")


class _BsnRogueAPContainmentMode_Type(Integer32):
    """Custom type bsnRogueAPContainmentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("cfp", 2),
          ("deauthBroadcast", 1),
          ("invalid", 0),
          ("max", 3),
          ("unknown", 99))
    )


_BsnRogueAPContainmentMode_Type.__name__ = "Integer32"
_BsnRogueAPContainmentMode_Object = MibTableColumn
bsnRogueAPContainmentMode = _BsnRogueAPContainmentMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 8, 1, 8),
    _BsnRogueAPContainmentMode_Type()
)
bsnRogueAPContainmentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPContainmentMode.setStatus("current")
_BsnRogueAPContainmentChannelCount_Type = Unsigned32
_BsnRogueAPContainmentChannelCount_Object = MibTableColumn
bsnRogueAPContainmentChannelCount = _BsnRogueAPContainmentChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 8, 1, 9),
    _BsnRogueAPContainmentChannelCount_Type()
)
bsnRogueAPContainmentChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPContainmentChannelCount.setStatus("current")
_BsnRogueAPContainmentChannels_Type = DisplayString
_BsnRogueAPContainmentChannels_Object = MibTableColumn
bsnRogueAPContainmentChannels = _BsnRogueAPContainmentChannels_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 8, 1, 10),
    _BsnRogueAPContainmentChannels_Type()
)
bsnRogueAPContainmentChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPContainmentChannels.setStatus("current")
_BsnRogueAPAirespaceAPLastHeard_Type = Counter32
_BsnRogueAPAirespaceAPLastHeard_Object = MibTableColumn
bsnRogueAPAirespaceAPLastHeard = _BsnRogueAPAirespaceAPLastHeard_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 8, 1, 11),
    _BsnRogueAPAirespaceAPLastHeard_Type()
)
bsnRogueAPAirespaceAPLastHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPAirespaceAPLastHeard.setStatus("current")


class _BsnRogueAPAirespaceAPWepMode_Type(Integer32):
    """Custom type bsnRogueAPAirespaceAPWepMode based on Integer32"""
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


_BsnRogueAPAirespaceAPWepMode_Type.__name__ = "Integer32"
_BsnRogueAPAirespaceAPWepMode_Object = MibTableColumn
bsnRogueAPAirespaceAPWepMode = _BsnRogueAPAirespaceAPWepMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 8, 1, 12),
    _BsnRogueAPAirespaceAPWepMode_Type()
)
bsnRogueAPAirespaceAPWepMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPAirespaceAPWepMode.setStatus("current")


class _BsnRogueAPAirespaceAPPreamble_Type(Integer32):
    """Custom type bsnRogueAPAirespaceAPPreamble based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 0),
          ("notSupported", 2),
          ("short", 1))
    )


_BsnRogueAPAirespaceAPPreamble_Type.__name__ = "Integer32"
_BsnRogueAPAirespaceAPPreamble_Object = MibTableColumn
bsnRogueAPAirespaceAPPreamble = _BsnRogueAPAirespaceAPPreamble_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 8, 1, 13),
    _BsnRogueAPAirespaceAPPreamble_Type()
)
bsnRogueAPAirespaceAPPreamble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPAirespaceAPPreamble.setStatus("current")


class _BsnRogueAPAirespaceAPWpaMode_Type(Integer32):
    """Custom type bsnRogueAPAirespaceAPWpaMode based on Integer32"""
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


_BsnRogueAPAirespaceAPWpaMode_Type.__name__ = "Integer32"
_BsnRogueAPAirespaceAPWpaMode_Object = MibTableColumn
bsnRogueAPAirespaceAPWpaMode = _BsnRogueAPAirespaceAPWpaMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 8, 1, 14),
    _BsnRogueAPAirespaceAPWpaMode_Type()
)
bsnRogueAPAirespaceAPWpaMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPAirespaceAPWpaMode.setStatus("current")
_BsnRogueAPAirespaceAPSNR_Type = Integer32
_BsnRogueAPAirespaceAPSNR_Object = MibTableColumn
bsnRogueAPAirespaceAPSNR = _BsnRogueAPAirespaceAPSNR_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 8, 1, 27),
    _BsnRogueAPAirespaceAPSNR_Type()
)
bsnRogueAPAirespaceAPSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPAirespaceAPSNR.setStatus("current")


class _BsnRogueAPChannelWidth_Type(Integer32):
    """Custom type bsnRogueAPChannelWidth based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("aboveEightyBelowforty", 8),
          ("aboveforty", 4),
          ("abovefortyAndEighty", 6),
          ("abovefortyBelowEighty", 7),
          ("belowforty", 5),
          ("belowfortyBelowEighty", 9),
          ("five", 1),
          ("ten", 2),
          ("twenty", 3))
    )


_BsnRogueAPChannelWidth_Type.__name__ = "Integer32"
_BsnRogueAPChannelWidth_Object = MibTableColumn
bsnRogueAPChannelWidth = _BsnRogueAPChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 8, 1, 28),
    _BsnRogueAPChannelWidth_Type()
)
bsnRogueAPChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPChannelWidth.setStatus("current")
_BsnThirdPartyAPTable_Object = MibTable
bsnThirdPartyAPTable = _BsnThirdPartyAPTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 9)
)
if mibBuilder.loadTexts:
    bsnThirdPartyAPTable.setStatus("obsolete")
_BsnThirdPartyAPEntry_Object = MibTableRow
bsnThirdPartyAPEntry = _BsnThirdPartyAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 9, 1)
)
bsnThirdPartyAPEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnThirdPartyAPMacAddress"),
)
if mibBuilder.loadTexts:
    bsnThirdPartyAPEntry.setStatus("obsolete")
_BsnThirdPartyAPMacAddress_Type = MacAddress
_BsnThirdPartyAPMacAddress_Object = MibTableColumn
bsnThirdPartyAPMacAddress = _BsnThirdPartyAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 9, 1, 1),
    _BsnThirdPartyAPMacAddress_Type()
)
bsnThirdPartyAPMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnThirdPartyAPMacAddress.setStatus("obsolete")
_BsnThirdPartyAPInterface_Type = Integer32
_BsnThirdPartyAPInterface_Object = MibTableColumn
bsnThirdPartyAPInterface = _BsnThirdPartyAPInterface_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 9, 1, 2),
    _BsnThirdPartyAPInterface_Type()
)
bsnThirdPartyAPInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnThirdPartyAPInterface.setStatus("obsolete")


class _BsnThirdPartyAPIpAddress_Type(IpAddress):
    """Custom type bsnThirdPartyAPIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_BsnThirdPartyAPIpAddress_Object = MibTableColumn
bsnThirdPartyAPIpAddress = _BsnThirdPartyAPIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 9, 1, 3),
    _BsnThirdPartyAPIpAddress_Type()
)
bsnThirdPartyAPIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnThirdPartyAPIpAddress.setStatus("obsolete")


class _BsnThirdPartyAP802Dot1XRequired_Type(Integer32):
    """Custom type bsnThirdPartyAP802Dot1XRequired based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnThirdPartyAP802Dot1XRequired_Type.__name__ = "Integer32"
_BsnThirdPartyAP802Dot1XRequired_Object = MibTableColumn
bsnThirdPartyAP802Dot1XRequired = _BsnThirdPartyAP802Dot1XRequired_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 9, 1, 4),
    _BsnThirdPartyAP802Dot1XRequired_Type()
)
bsnThirdPartyAP802Dot1XRequired.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnThirdPartyAP802Dot1XRequired.setStatus("obsolete")


class _BsnThirdPartyAPMirrorMode_Type(Integer32):
    """Custom type bsnThirdPartyAPMirrorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnThirdPartyAPMirrorMode_Type.__name__ = "Integer32"
_BsnThirdPartyAPMirrorMode_Object = MibTableColumn
bsnThirdPartyAPMirrorMode = _BsnThirdPartyAPMirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 9, 1, 5),
    _BsnThirdPartyAPMirrorMode_Type()
)
bsnThirdPartyAPMirrorMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnThirdPartyAPMirrorMode.setStatus("obsolete")
_BsnThirdPartyAPRowStatus_Type = RowStatus
_BsnThirdPartyAPRowStatus_Object = MibTableColumn
bsnThirdPartyAPRowStatus = _BsnThirdPartyAPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 9, 1, 24),
    _BsnThirdPartyAPRowStatus_Type()
)
bsnThirdPartyAPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnThirdPartyAPRowStatus.setStatus("obsolete")
_BsnMobileStationByIpTable_Object = MibTable
bsnMobileStationByIpTable = _BsnMobileStationByIpTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 10)
)
if mibBuilder.loadTexts:
    bsnMobileStationByIpTable.setStatus("current")
_BsnMobileStationByIpEntry_Object = MibTableRow
bsnMobileStationByIpEntry = _BsnMobileStationByIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 10, 1)
)
bsnMobileStationByIpEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnMobileStationByIpAddress"),
)
if mibBuilder.loadTexts:
    bsnMobileStationByIpEntry.setStatus("current")
_BsnMobileStationByIpAddress_Type = IpAddress
_BsnMobileStationByIpAddress_Object = MibTableColumn
bsnMobileStationByIpAddress = _BsnMobileStationByIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 10, 1, 1),
    _BsnMobileStationByIpAddress_Type()
)
bsnMobileStationByIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationByIpAddress.setStatus("current")
_BsnMobileStationByIpMacAddress_Type = MacAddress
_BsnMobileStationByIpMacAddress_Object = MibTableColumn
bsnMobileStationByIpMacAddress = _BsnMobileStationByIpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 10, 1, 2),
    _BsnMobileStationByIpMacAddress_Type()
)
bsnMobileStationByIpMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationByIpMacAddress.setStatus("current")
_BsnMobileStationRssiDataTable_Object = MibTable
bsnMobileStationRssiDataTable = _BsnMobileStationRssiDataTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 11)
)
if mibBuilder.loadTexts:
    bsnMobileStationRssiDataTable.setStatus("current")
_BsnMobileStationRssiDataEntry_Object = MibTableRow
bsnMobileStationRssiDataEntry = _BsnMobileStationRssiDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 11, 1)
)
bsnMobileStationRssiDataEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnMobileStationMacAddress"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnMobileStationRssiDataApMacAddress"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnMobileStationRssiDataApIfSlotId"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPIfPhyAntennaIndex"),
)
if mibBuilder.loadTexts:
    bsnMobileStationRssiDataEntry.setStatus("current")
_BsnMobileStationRssiDataApMacAddress_Type = MacAddress
_BsnMobileStationRssiDataApMacAddress_Object = MibTableColumn
bsnMobileStationRssiDataApMacAddress = _BsnMobileStationRssiDataApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 11, 1, 1),
    _BsnMobileStationRssiDataApMacAddress_Type()
)
bsnMobileStationRssiDataApMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationRssiDataApMacAddress.setStatus("current")


class _BsnMobileStationRssiDataApIfSlotId_Type(Unsigned32):
    """Custom type bsnMobileStationRssiDataApIfSlotId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_BsnMobileStationRssiDataApIfSlotId_Type.__name__ = "Unsigned32"
_BsnMobileStationRssiDataApIfSlotId_Object = MibTableColumn
bsnMobileStationRssiDataApIfSlotId = _BsnMobileStationRssiDataApIfSlotId_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 11, 1, 2),
    _BsnMobileStationRssiDataApIfSlotId_Type()
)
bsnMobileStationRssiDataApIfSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationRssiDataApIfSlotId.setStatus("current")


class _BsnMobileStationRssiDataApIfType_Type(Integer32):
    """Custom type bsnMobileStationRssiDataApIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 2),
          ("dot11bg", 1),
          ("unknown", 3))
    )


_BsnMobileStationRssiDataApIfType_Type.__name__ = "Integer32"
_BsnMobileStationRssiDataApIfType_Object = MibTableColumn
bsnMobileStationRssiDataApIfType = _BsnMobileStationRssiDataApIfType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 11, 1, 3),
    _BsnMobileStationRssiDataApIfType_Type()
)
bsnMobileStationRssiDataApIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationRssiDataApIfType.setStatus("current")
_BsnMobileStationRssiDataApName_Type = DisplayString
_BsnMobileStationRssiDataApName_Object = MibTableColumn
bsnMobileStationRssiDataApName = _BsnMobileStationRssiDataApName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 11, 1, 4),
    _BsnMobileStationRssiDataApName_Type()
)
bsnMobileStationRssiDataApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationRssiDataApName.setStatus("current")
_BsnMobileStationRssiData_Type = Integer32
_BsnMobileStationRssiData_Object = MibTableColumn
bsnMobileStationRssiData = _BsnMobileStationRssiData_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 11, 1, 5),
    _BsnMobileStationRssiData_Type()
)
bsnMobileStationRssiData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationRssiData.setStatus("current")
_BsnAPIfPhyAntennaIndex_Type = Unsigned32
_BsnAPIfPhyAntennaIndex_Object = MibTableColumn
bsnAPIfPhyAntennaIndex = _BsnAPIfPhyAntennaIndex_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 11, 1, 6),
    _BsnAPIfPhyAntennaIndex_Type()
)
bsnAPIfPhyAntennaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfPhyAntennaIndex.setStatus("current")
_BsnMobileStationRssiDataLastHeard_Type = Counter32
_BsnMobileStationRssiDataLastHeard_Object = MibTableColumn
bsnMobileStationRssiDataLastHeard = _BsnMobileStationRssiDataLastHeard_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 11, 1, 25),
    _BsnMobileStationRssiDataLastHeard_Type()
)
bsnMobileStationRssiDataLastHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationRssiDataLastHeard.setStatus("current")
_BsnWatchListClientTable_Object = MibTable
bsnWatchListClientTable = _BsnWatchListClientTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 12)
)
if mibBuilder.loadTexts:
    bsnWatchListClientTable.setStatus("obsolete")
_BsnWatchListClientEntry_Object = MibTableRow
bsnWatchListClientEntry = _BsnWatchListClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 12, 1)
)
bsnWatchListClientEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnWatchListClientKey"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnWatchListClientType"),
)
if mibBuilder.loadTexts:
    bsnWatchListClientEntry.setStatus("obsolete")


class _BsnWatchListClientKey_Type(OctetString):
    """Custom type bsnWatchListClientKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_BsnWatchListClientKey_Type.__name__ = "OctetString"
_BsnWatchListClientKey_Object = MibTableColumn
bsnWatchListClientKey = _BsnWatchListClientKey_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 12, 1, 1),
    _BsnWatchListClientKey_Type()
)
bsnWatchListClientKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnWatchListClientKey.setStatus("obsolete")


class _BsnWatchListClientType_Type(Integer32):
    """Custom type bsnWatchListClientType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("byMac", 1),
          ("byUserName", 2))
    )


_BsnWatchListClientType_Type.__name__ = "Integer32"
_BsnWatchListClientType_Object = MibTableColumn
bsnWatchListClientType = _BsnWatchListClientType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 12, 1, 2),
    _BsnWatchListClientType_Type()
)
bsnWatchListClientType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnWatchListClientType.setStatus("obsolete")
_BsnWatchListClientRowStatus_Type = RowStatus
_BsnWatchListClientRowStatus_Object = MibTableColumn
bsnWatchListClientRowStatus = _BsnWatchListClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 12, 1, 20),
    _BsnWatchListClientRowStatus_Type()
)
bsnWatchListClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnWatchListClientRowStatus.setStatus("obsolete")
_BsnMobileStationByUsernameTable_Object = MibTable
bsnMobileStationByUsernameTable = _BsnMobileStationByUsernameTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 13)
)
if mibBuilder.loadTexts:
    bsnMobileStationByUsernameTable.setStatus("current")
_BsnMobileStationByUsernameEntry_Object = MibTableRow
bsnMobileStationByUsernameEntry = _BsnMobileStationByUsernameEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 13, 1)
)
bsnMobileStationByUsernameEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnMobileStationByUserName"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnMobileStationByUserMacAddress"),
)
if mibBuilder.loadTexts:
    bsnMobileStationByUsernameEntry.setStatus("current")


class _BsnMobileStationByUserName_Type(OctetString):
    """Custom type bsnMobileStationByUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_BsnMobileStationByUserName_Type.__name__ = "OctetString"
_BsnMobileStationByUserName_Object = MibTableColumn
bsnMobileStationByUserName = _BsnMobileStationByUserName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 13, 1, 1),
    _BsnMobileStationByUserName_Type()
)
bsnMobileStationByUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationByUserName.setStatus("current")
_BsnMobileStationByUserMacAddress_Type = MacAddress
_BsnMobileStationByUserMacAddress_Object = MibTableColumn
bsnMobileStationByUserMacAddress = _BsnMobileStationByUserMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 13, 1, 2),
    _BsnMobileStationByUserMacAddress_Type()
)
bsnMobileStationByUserMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationByUserMacAddress.setStatus("current")
_BsnRogueClientTable_Object = MibTable
bsnRogueClientTable = _BsnRogueClientTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 14)
)
if mibBuilder.loadTexts:
    bsnRogueClientTable.setStatus("current")
_BsnRogueClientEntry_Object = MibTableRow
bsnRogueClientEntry = _BsnRogueClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 14, 1)
)
bsnRogueClientEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnRogueClientDot11MacAddress"),
)
if mibBuilder.loadTexts:
    bsnRogueClientEntry.setStatus("current")
_BsnRogueClientDot11MacAddress_Type = MacAddress
_BsnRogueClientDot11MacAddress_Object = MibTableColumn
bsnRogueClientDot11MacAddress = _BsnRogueClientDot11MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 14, 1, 1),
    _BsnRogueClientDot11MacAddress_Type()
)
bsnRogueClientDot11MacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsnRogueClientDot11MacAddress.setStatus("current")
_BsnRogueClientTotalDetectingAPs_Type = Integer32
_BsnRogueClientTotalDetectingAPs_Object = MibTableColumn
bsnRogueClientTotalDetectingAPs = _BsnRogueClientTotalDetectingAPs_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 14, 1, 2),
    _BsnRogueClientTotalDetectingAPs_Type()
)
bsnRogueClientTotalDetectingAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueClientTotalDetectingAPs.setStatus("current")
_BsnRogueClientFirstReported_Type = DisplayString
_BsnRogueClientFirstReported_Object = MibTableColumn
bsnRogueClientFirstReported = _BsnRogueClientFirstReported_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 14, 1, 3),
    _BsnRogueClientFirstReported_Type()
)
bsnRogueClientFirstReported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueClientFirstReported.setStatus("current")
_BsnRogueClientLastReported_Type = DisplayString
_BsnRogueClientLastReported_Object = MibTableColumn
bsnRogueClientLastReported = _BsnRogueClientLastReported_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 14, 1, 4),
    _BsnRogueClientLastReported_Type()
)
bsnRogueClientLastReported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueClientLastReported.setStatus("current")
_BsnRogueClientBSSID_Type = MacAddress
_BsnRogueClientBSSID_Object = MibTableColumn
bsnRogueClientBSSID = _BsnRogueClientBSSID_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 14, 1, 5),
    _BsnRogueClientBSSID_Type()
)
bsnRogueClientBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueClientBSSID.setStatus("current")


class _BsnRogueClientContainmentLevel_Type(Integer32):
    """Custom type bsnRogueClientContainmentLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4),
          ("unassigned", 0))
    )


_BsnRogueClientContainmentLevel_Type.__name__ = "Integer32"
_BsnRogueClientContainmentLevel_Object = MibTableColumn
bsnRogueClientContainmentLevel = _BsnRogueClientContainmentLevel_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 14, 1, 6),
    _BsnRogueClientContainmentLevel_Type()
)
bsnRogueClientContainmentLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRogueClientContainmentLevel.setStatus("current")
_BsnRogueClientLastHeard_Type = Integer32
_BsnRogueClientLastHeard_Object = MibTableColumn
bsnRogueClientLastHeard = _BsnRogueClientLastHeard_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 14, 1, 7),
    _BsnRogueClientLastHeard_Type()
)
bsnRogueClientLastHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueClientLastHeard.setStatus("current")


class _BsnRogueClientState_Type(Integer32):
    """Custom type bsnRogueClientState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("alert", 2),
          ("contained", 6),
          ("containedpending", 8),
          ("initializing", 0),
          ("pending", 1),
          ("threat", 7))
    )


_BsnRogueClientState_Type.__name__ = "Integer32"
_BsnRogueClientState_Object = MibTableColumn
bsnRogueClientState = _BsnRogueClientState_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 14, 1, 24),
    _BsnRogueClientState_Type()
)
bsnRogueClientState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRogueClientState.setStatus("current")
_BsnRogueClientAirespaceAPTable_Object = MibTable
bsnRogueClientAirespaceAPTable = _BsnRogueClientAirespaceAPTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 15)
)
if mibBuilder.loadTexts:
    bsnRogueClientAirespaceAPTable.setStatus("current")
_BsnRogueClientAirespaceAPEntry_Object = MibTableRow
bsnRogueClientAirespaceAPEntry = _BsnRogueClientAirespaceAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 15, 1)
)
bsnRogueClientAirespaceAPEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnRogueClientDot11MacAddress"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnRogueClientAirespaceAPMacAddress"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnRogueClientAirespaceAPSlotId"),
)
if mibBuilder.loadTexts:
    bsnRogueClientAirespaceAPEntry.setStatus("current")
_BsnRogueClientAirespaceAPMacAddress_Type = MacAddress
_BsnRogueClientAirespaceAPMacAddress_Object = MibTableColumn
bsnRogueClientAirespaceAPMacAddress = _BsnRogueClientAirespaceAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 15, 1, 1),
    _BsnRogueClientAirespaceAPMacAddress_Type()
)
bsnRogueClientAirespaceAPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueClientAirespaceAPMacAddress.setStatus("current")


class _BsnRogueClientAirespaceAPSlotId_Type(Unsigned32):
    """Custom type bsnRogueClientAirespaceAPSlotId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BsnRogueClientAirespaceAPSlotId_Type.__name__ = "Unsigned32"
_BsnRogueClientAirespaceAPSlotId_Object = MibTableColumn
bsnRogueClientAirespaceAPSlotId = _BsnRogueClientAirespaceAPSlotId_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 15, 1, 2),
    _BsnRogueClientAirespaceAPSlotId_Type()
)
bsnRogueClientAirespaceAPSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueClientAirespaceAPSlotId.setStatus("current")


class _BsnRogueClientRadioType_Type(Integer32):
    """Custom type bsnRogueClientRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 2),
          ("dot11b", 1),
          ("unknown", 3))
    )


_BsnRogueClientRadioType_Type.__name__ = "Integer32"
_BsnRogueClientRadioType_Object = MibTableColumn
bsnRogueClientRadioType = _BsnRogueClientRadioType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 15, 1, 3),
    _BsnRogueClientRadioType_Type()
)
bsnRogueClientRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueClientRadioType.setStatus("current")
_BsnRogueClientAirespaceAPName_Type = DisplayString
_BsnRogueClientAirespaceAPName_Object = MibTableColumn
bsnRogueClientAirespaceAPName = _BsnRogueClientAirespaceAPName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 15, 1, 4),
    _BsnRogueClientAirespaceAPName_Type()
)
bsnRogueClientAirespaceAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueClientAirespaceAPName.setStatus("current")
_BsnRogueClientChannelNumber_Type = Integer32
_BsnRogueClientChannelNumber_Object = MibTableColumn
bsnRogueClientChannelNumber = _BsnRogueClientChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 15, 1, 5),
    _BsnRogueClientChannelNumber_Type()
)
bsnRogueClientChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueClientChannelNumber.setStatus("current")
_BsnRogueClientAirespaceAPRSSI_Type = Integer32
_BsnRogueClientAirespaceAPRSSI_Object = MibTableColumn
bsnRogueClientAirespaceAPRSSI = _BsnRogueClientAirespaceAPRSSI_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 15, 1, 7),
    _BsnRogueClientAirespaceAPRSSI_Type()
)
bsnRogueClientAirespaceAPRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueClientAirespaceAPRSSI.setStatus("current")
_BsnRogueClientAirespaceAPLastHeard_Type = DisplayString
_BsnRogueClientAirespaceAPLastHeard_Object = MibTableColumn
bsnRogueClientAirespaceAPLastHeard = _BsnRogueClientAirespaceAPLastHeard_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 15, 1, 11),
    _BsnRogueClientAirespaceAPLastHeard_Type()
)
bsnRogueClientAirespaceAPLastHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueClientAirespaceAPLastHeard.setStatus("current")
_BsnRogueClientAirespaceAPSNR_Type = Integer32
_BsnRogueClientAirespaceAPSNR_Object = MibTableColumn
bsnRogueClientAirespaceAPSNR = _BsnRogueClientAirespaceAPSNR_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 15, 1, 27),
    _BsnRogueClientAirespaceAPSNR_Type()
)
bsnRogueClientAirespaceAPSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueClientAirespaceAPSNR.setStatus("current")
_BsnRogueClientPerRogueAPTable_Object = MibTable
bsnRogueClientPerRogueAPTable = _BsnRogueClientPerRogueAPTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 16)
)
if mibBuilder.loadTexts:
    bsnRogueClientPerRogueAPTable.setStatus("current")
_BsnRogueClientPerRogueAPEntry_Object = MibTableRow
bsnRogueClientPerRogueAPEntry = _BsnRogueClientPerRogueAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 16, 1)
)
bsnRogueClientPerRogueAPEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnRogueAPDot11MacAddr"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnRogueClientDot11MacAddr"),
)
if mibBuilder.loadTexts:
    bsnRogueClientPerRogueAPEntry.setStatus("current")
_BsnRogueAPDot11MacAddr_Type = MacAddress
_BsnRogueAPDot11MacAddr_Object = MibTableColumn
bsnRogueAPDot11MacAddr = _BsnRogueAPDot11MacAddr_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 16, 1, 1),
    _BsnRogueAPDot11MacAddr_Type()
)
bsnRogueAPDot11MacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueAPDot11MacAddr.setStatus("current")
_BsnRogueClientDot11MacAddr_Type = MacAddress
_BsnRogueClientDot11MacAddr_Object = MibTableColumn
bsnRogueClientDot11MacAddr = _BsnRogueClientDot11MacAddr_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 16, 1, 20),
    _BsnRogueClientDot11MacAddr_Type()
)
bsnRogueClientDot11MacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRogueClientDot11MacAddr.setStatus("current")
_BsnDot11QosProfileTable_Object = MibTable
bsnDot11QosProfileTable = _BsnDot11QosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 17)
)
if mibBuilder.loadTexts:
    bsnDot11QosProfileTable.setStatus("current")
_BsnDot11QosProfileEntry_Object = MibTableRow
bsnDot11QosProfileEntry = _BsnDot11QosProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 17, 1)
)
bsnDot11QosProfileEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnDot11QosProfileName"),
)
if mibBuilder.loadTexts:
    bsnDot11QosProfileEntry.setStatus("current")


class _BsnDot11QosProfileName_Type(OctetString):
    """Custom type bsnDot11QosProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BsnDot11QosProfileName_Type.__name__ = "OctetString"
_BsnDot11QosProfileName_Object = MibTableColumn
bsnDot11QosProfileName = _BsnDot11QosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 17, 1, 1),
    _BsnDot11QosProfileName_Type()
)
bsnDot11QosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnDot11QosProfileName.setStatus("current")


class _BsnDot11QosProfileDesc_Type(OctetString):
    """Custom type bsnDot11QosProfileDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_BsnDot11QosProfileDesc_Type.__name__ = "OctetString"
_BsnDot11QosProfileDesc_Object = MibTableColumn
bsnDot11QosProfileDesc = _BsnDot11QosProfileDesc_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 17, 1, 2),
    _BsnDot11QosProfileDesc_Type()
)
bsnDot11QosProfileDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnDot11QosProfileDesc.setStatus("current")


class _BsnDot11QosAverageDataRate_Type(Integer32):
    """Custom type bsnDot11QosAverageDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_BsnDot11QosAverageDataRate_Type.__name__ = "Integer32"
_BsnDot11QosAverageDataRate_Object = MibTableColumn
bsnDot11QosAverageDataRate = _BsnDot11QosAverageDataRate_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 17, 1, 3),
    _BsnDot11QosAverageDataRate_Type()
)
bsnDot11QosAverageDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnDot11QosAverageDataRate.setStatus("current")


class _BsnDot11QosBurstDataRate_Type(Integer32):
    """Custom type bsnDot11QosBurstDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_BsnDot11QosBurstDataRate_Type.__name__ = "Integer32"
_BsnDot11QosBurstDataRate_Object = MibTableColumn
bsnDot11QosBurstDataRate = _BsnDot11QosBurstDataRate_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 17, 1, 4),
    _BsnDot11QosBurstDataRate_Type()
)
bsnDot11QosBurstDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnDot11QosBurstDataRate.setStatus("current")


class _BsnDot11QosAvgRealTimeDataRate_Type(Integer32):
    """Custom type bsnDot11QosAvgRealTimeDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_BsnDot11QosAvgRealTimeDataRate_Type.__name__ = "Integer32"
_BsnDot11QosAvgRealTimeDataRate_Object = MibTableColumn
bsnDot11QosAvgRealTimeDataRate = _BsnDot11QosAvgRealTimeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 17, 1, 5),
    _BsnDot11QosAvgRealTimeDataRate_Type()
)
bsnDot11QosAvgRealTimeDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnDot11QosAvgRealTimeDataRate.setStatus("current")


class _BsnDot11QosBurstRealTimeDataRate_Type(Integer32):
    """Custom type bsnDot11QosBurstRealTimeDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_BsnDot11QosBurstRealTimeDataRate_Type.__name__ = "Integer32"
_BsnDot11QosBurstRealTimeDataRate_Object = MibTableColumn
bsnDot11QosBurstRealTimeDataRate = _BsnDot11QosBurstRealTimeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 17, 1, 6),
    _BsnDot11QosBurstRealTimeDataRate_Type()
)
bsnDot11QosBurstRealTimeDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnDot11QosBurstRealTimeDataRate.setStatus("current")


class _BsnDot11QosMaxRFUsagePerAP_Type(Integer32):
    """Custom type bsnDot11QosMaxRFUsagePerAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_BsnDot11QosMaxRFUsagePerAP_Type.__name__ = "Integer32"
_BsnDot11QosMaxRFUsagePerAP_Object = MibTableColumn
bsnDot11QosMaxRFUsagePerAP = _BsnDot11QosMaxRFUsagePerAP_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 17, 1, 7),
    _BsnDot11QosMaxRFUsagePerAP_Type()
)
bsnDot11QosMaxRFUsagePerAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnDot11QosMaxRFUsagePerAP.setStatus("current")


class _BsnDot11QosProfileQueueDepth_Type(Integer32):
    """Custom type bsnDot11QosProfileQueueDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_BsnDot11QosProfileQueueDepth_Type.__name__ = "Integer32"
_BsnDot11QosProfileQueueDepth_Object = MibTableColumn
bsnDot11QosProfileQueueDepth = _BsnDot11QosProfileQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 17, 1, 8),
    _BsnDot11QosProfileQueueDepth_Type()
)
bsnDot11QosProfileQueueDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnDot11QosProfileQueueDepth.setStatus("current")


class _BsnDot11WiredQosProtocol_Type(Integer32):
    """Custom type bsnDot11WiredQosProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dot1p", 1),
          ("none", 0))
    )


_BsnDot11WiredQosProtocol_Type.__name__ = "Integer32"
_BsnDot11WiredQosProtocol_Object = MibTableColumn
bsnDot11WiredQosProtocol = _BsnDot11WiredQosProtocol_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 17, 1, 9),
    _BsnDot11WiredQosProtocol_Type()
)
bsnDot11WiredQosProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnDot11WiredQosProtocol.setStatus("current")


class _BsnDot11802Dot1PTag_Type(Integer32):
    """Custom type bsnDot11802Dot1PTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BsnDot11802Dot1PTag_Type.__name__ = "Integer32"
_BsnDot11802Dot1PTag_Object = MibTableColumn
bsnDot11802Dot1PTag = _BsnDot11802Dot1PTag_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 17, 1, 10),
    _BsnDot11802Dot1PTag_Type()
)
bsnDot11802Dot1PTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnDot11802Dot1PTag.setStatus("current")


class _BsnDot11ResetProfileToDefault_Type(Integer32):
    """Custom type bsnDot11ResetProfileToDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_BsnDot11ResetProfileToDefault_Type.__name__ = "Integer32"
_BsnDot11ResetProfileToDefault_Object = MibTableColumn
bsnDot11ResetProfileToDefault = _BsnDot11ResetProfileToDefault_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 17, 1, 40),
    _BsnDot11ResetProfileToDefault_Type()
)
bsnDot11ResetProfileToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnDot11ResetProfileToDefault.setStatus("current")
_BsnTagTable_Object = MibTable
bsnTagTable = _BsnTagTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 18)
)
if mibBuilder.loadTexts:
    bsnTagTable.setStatus("current")
_BsnTagEntry_Object = MibTableRow
bsnTagEntry = _BsnTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 18, 1)
)
bsnTagEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnTagDot11MacAddress"),
)
if mibBuilder.loadTexts:
    bsnTagEntry.setStatus("current")
_BsnTagDot11MacAddress_Type = MacAddress
_BsnTagDot11MacAddress_Object = MibTableColumn
bsnTagDot11MacAddress = _BsnTagDot11MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 18, 1, 1),
    _BsnTagDot11MacAddress_Type()
)
bsnTagDot11MacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTagDot11MacAddress.setStatus("current")


class _BsnTagType_Type(Integer32):
    """Custom type bsnTagType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type1", 2),
          ("unknown", 0))
    )


_BsnTagType_Type.__name__ = "Integer32"
_BsnTagType_Object = MibTableColumn
bsnTagType = _BsnTagType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 18, 1, 2),
    _BsnTagType_Type()
)
bsnTagType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTagType.setStatus("current")
_BsnTagTimeInterval_Type = Unsigned32
_BsnTagTimeInterval_Object = MibTableColumn
bsnTagTimeInterval = _BsnTagTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 18, 1, 3),
    _BsnTagTimeInterval_Type()
)
bsnTagTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTagTimeInterval.setStatus("current")


class _BsnTagBatteryStatus_Type(Integer32):
    """Custom type bsnTagBatteryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("medium", 3),
          ("normal", 2),
          ("unknown", 0))
    )


_BsnTagBatteryStatus_Type.__name__ = "Integer32"
_BsnTagBatteryStatus_Object = MibTableColumn
bsnTagBatteryStatus = _BsnTagBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 18, 1, 4),
    _BsnTagBatteryStatus_Type()
)
bsnTagBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTagBatteryStatus.setStatus("current")
_BsnTagLastReported_Type = Unsigned32
_BsnTagLastReported_Object = MibTableColumn
bsnTagLastReported = _BsnTagLastReported_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 18, 1, 23),
    _BsnTagLastReported_Type()
)
bsnTagLastReported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTagLastReported.setStatus("current")
_BsnTagRssiDataTable_Object = MibTable
bsnTagRssiDataTable = _BsnTagRssiDataTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 19)
)
if mibBuilder.loadTexts:
    bsnTagRssiDataTable.setStatus("current")
_BsnTagRssiDataEntry_Object = MibTableRow
bsnTagRssiDataEntry = _BsnTagRssiDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 19, 1)
)
bsnTagRssiDataEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnTagDot11MacAddress"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnTagRssiDataApMacAddress"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnTagRssiDataApIfSlotId"),
)
if mibBuilder.loadTexts:
    bsnTagRssiDataEntry.setStatus("current")
_BsnTagRssiDataApMacAddress_Type = MacAddress
_BsnTagRssiDataApMacAddress_Object = MibTableColumn
bsnTagRssiDataApMacAddress = _BsnTagRssiDataApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 19, 1, 1),
    _BsnTagRssiDataApMacAddress_Type()
)
bsnTagRssiDataApMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTagRssiDataApMacAddress.setStatus("current")


class _BsnTagRssiDataApIfSlotId_Type(Unsigned32):
    """Custom type bsnTagRssiDataApIfSlotId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_BsnTagRssiDataApIfSlotId_Type.__name__ = "Unsigned32"
_BsnTagRssiDataApIfSlotId_Object = MibTableColumn
bsnTagRssiDataApIfSlotId = _BsnTagRssiDataApIfSlotId_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 19, 1, 2),
    _BsnTagRssiDataApIfSlotId_Type()
)
bsnTagRssiDataApIfSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTagRssiDataApIfSlotId.setStatus("current")


class _BsnTagRssiDataApIfType_Type(Integer32):
    """Custom type bsnTagRssiDataApIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 2),
          ("dot11b", 1),
          ("uwb", 4))
    )


_BsnTagRssiDataApIfType_Type.__name__ = "Integer32"
_BsnTagRssiDataApIfType_Object = MibTableColumn
bsnTagRssiDataApIfType = _BsnTagRssiDataApIfType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 19, 1, 3),
    _BsnTagRssiDataApIfType_Type()
)
bsnTagRssiDataApIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTagRssiDataApIfType.setStatus("current")


class _BsnTagRssiDataApName_Type(DisplayString):
    """Custom type bsnTagRssiDataApName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BsnTagRssiDataApName_Type.__name__ = "DisplayString"
_BsnTagRssiDataApName_Object = MibTableColumn
bsnTagRssiDataApName = _BsnTagRssiDataApName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 19, 1, 4),
    _BsnTagRssiDataApName_Type()
)
bsnTagRssiDataApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTagRssiDataApName.setStatus("current")
_BsnTagRssiDataLastHeard_Type = Counter32
_BsnTagRssiDataLastHeard_Object = MibTableColumn
bsnTagRssiDataLastHeard = _BsnTagRssiDataLastHeard_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 19, 1, 5),
    _BsnTagRssiDataLastHeard_Type()
)
bsnTagRssiDataLastHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTagRssiDataLastHeard.setStatus("current")
_BsnTagRssiData_Type = Integer32
_BsnTagRssiData_Object = MibTableColumn
bsnTagRssiData = _BsnTagRssiData_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 19, 1, 6),
    _BsnTagRssiData_Type()
)
bsnTagRssiData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTagRssiData.setStatus("current")
_BsnTagRssiDataSnr_Type = Integer32
_BsnTagRssiDataSnr_Object = MibTableColumn
bsnTagRssiDataSnr = _BsnTagRssiDataSnr_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 19, 1, 26),
    _BsnTagRssiDataSnr_Type()
)
bsnTagRssiDataSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTagRssiDataSnr.setStatus("current")
_BsnTagStatsTable_Object = MibTable
bsnTagStatsTable = _BsnTagStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 20)
)
if mibBuilder.loadTexts:
    bsnTagStatsTable.setStatus("current")
_BsnTagStatsEntry_Object = MibTableRow
bsnTagStatsEntry = _BsnTagStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 20, 1)
)
bsnTagStatsEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnTagDot11MacAddress"),
)
if mibBuilder.loadTexts:
    bsnTagStatsEntry.setStatus("current")
_BsnTagBytesReceived_Type = Unsigned32
_BsnTagBytesReceived_Object = MibTableColumn
bsnTagBytesReceived = _BsnTagBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 20, 1, 1),
    _BsnTagBytesReceived_Type()
)
bsnTagBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTagBytesReceived.setStatus("current")
_BsnTagPacketsReceived_Type = Unsigned32
_BsnTagPacketsReceived_Object = MibTableColumn
bsnTagPacketsReceived = _BsnTagPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 20, 1, 20),
    _BsnTagPacketsReceived_Type()
)
bsnTagPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTagPacketsReceived.setStatus("current")
_BsnMobileStationExtStatsTable_Object = MibTable
bsnMobileStationExtStatsTable = _BsnMobileStationExtStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 21)
)
if mibBuilder.loadTexts:
    bsnMobileStationExtStatsTable.setStatus("obsolete")
_BsnMobileStationExtStatsEntry_Object = MibTableRow
bsnMobileStationExtStatsEntry = _BsnMobileStationExtStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 21, 1)
)
bsnMobileStationExtStatsEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnMobileStationMacAddress"),
)
if mibBuilder.loadTexts:
    bsnMobileStationExtStatsEntry.setStatus("obsolete")
_BsnMobileStationSampleTime_Type = Integer32
_BsnMobileStationSampleTime_Object = MibTableColumn
bsnMobileStationSampleTime = _BsnMobileStationSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 21, 1, 1),
    _BsnMobileStationSampleTime_Type()
)
bsnMobileStationSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationSampleTime.setStatus("obsolete")
_BsnMobileStationTxExcessiveRetries_Type = Counter64
_BsnMobileStationTxExcessiveRetries_Object = MibTableColumn
bsnMobileStationTxExcessiveRetries = _BsnMobileStationTxExcessiveRetries_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 21, 1, 2),
    _BsnMobileStationTxExcessiveRetries_Type()
)
bsnMobileStationTxExcessiveRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationTxExcessiveRetries.setStatus("obsolete")
_BsnMobileStationTxRetries_Type = Counter64
_BsnMobileStationTxRetries_Object = MibTableColumn
bsnMobileStationTxRetries = _BsnMobileStationTxRetries_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 21, 1, 3),
    _BsnMobileStationTxRetries_Type()
)
bsnMobileStationTxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationTxRetries.setStatus("obsolete")
_BsnMobileStationTxFiltered_Type = Counter64
_BsnMobileStationTxFiltered_Object = MibTableColumn
bsnMobileStationTxFiltered = _BsnMobileStationTxFiltered_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 1, 21, 1, 20),
    _BsnMobileStationTxFiltered_Type()
)
bsnMobileStationTxFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMobileStationTxFiltered.setStatus("obsolete")
_BsnAP_ObjectIdentity = ObjectIdentity
bsnAP = _BsnAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2)
)
_BsnAPTable_Object = MibTable
bsnAPTable = _BsnAPTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1)
)
if mibBuilder.loadTexts:
    bsnAPTable.setStatus("current")
_BsnAPEntry_Object = MibTableRow
bsnAPEntry = _BsnAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1)
)
bsnAPEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
)
if mibBuilder.loadTexts:
    bsnAPEntry.setStatus("current")
_BsnAPDot3MacAddress_Type = MacAddress
_BsnAPDot3MacAddress_Object = MibTableColumn
bsnAPDot3MacAddress = _BsnAPDot3MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 1),
    _BsnAPDot3MacAddress_Type()
)
bsnAPDot3MacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPDot3MacAddress.setStatus("current")


class _BsnAPNumOfSlots_Type(Integer32):
    """Custom type bsnAPNumOfSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_BsnAPNumOfSlots_Type.__name__ = "Integer32"
_BsnAPNumOfSlots_Object = MibTableColumn
bsnAPNumOfSlots = _BsnAPNumOfSlots_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 2),
    _BsnAPNumOfSlots_Type()
)
bsnAPNumOfSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPNumOfSlots.setStatus("current")


class _BsnAPName_Type(OctetString):
    """Custom type bsnAPName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BsnAPName_Type.__name__ = "OctetString"
_BsnAPName_Object = MibTableColumn
bsnAPName = _BsnAPName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 3),
    _BsnAPName_Type()
)
bsnAPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPName.setStatus("current")


class _BsnAPLocation_Type(OctetString):
    """Custom type bsnAPLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_BsnAPLocation_Type.__name__ = "OctetString"
_BsnAPLocation_Object = MibTableColumn
bsnAPLocation = _BsnAPLocation_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 4),
    _BsnAPLocation_Type()
)
bsnAPLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPLocation.setStatus("current")


class _BsnAPMonitorOnlyMode_Type(Integer32):
    """Custom type bsnAPMonitorOnlyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 5),
          ("local", 0),
          ("monitor", 1),
          ("remote", 2),
          ("remoteBridge", 7),
          ("roguedetector", 3),
          ("seConnect", 6),
          ("sniffer", 4))
    )


_BsnAPMonitorOnlyMode_Type.__name__ = "Integer32"
_BsnAPMonitorOnlyMode_Object = MibTableColumn
bsnAPMonitorOnlyMode = _BsnAPMonitorOnlyMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 5),
    _BsnAPMonitorOnlyMode_Type()
)
bsnAPMonitorOnlyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPMonitorOnlyMode.setStatus("current")


class _BsnAPOperationStatus_Type(Integer32):
    """Custom type bsnAPOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("associated", 1),
          ("disassociating", 2),
          ("downloading", 3))
    )


_BsnAPOperationStatus_Type.__name__ = "Integer32"
_BsnAPOperationStatus_Object = MibTableColumn
bsnAPOperationStatus = _BsnAPOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 6),
    _BsnAPOperationStatus_Type()
)
bsnAPOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPOperationStatus.setStatus("current")
_BsnAPSoftwareVersion_Type = DisplayString
_BsnAPSoftwareVersion_Object = MibTableColumn
bsnAPSoftwareVersion = _BsnAPSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 8),
    _BsnAPSoftwareVersion_Type()
)
bsnAPSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPSoftwareVersion.setStatus("current")
_BsnAPBootVersion_Type = DisplayString
_BsnAPBootVersion_Object = MibTableColumn
bsnAPBootVersion = _BsnAPBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 9),
    _BsnAPBootVersion_Type()
)
bsnAPBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPBootVersion.setStatus("current")


class _BsnAPPrimaryMwarName_Type(OctetString):
    """Custom type bsnAPPrimaryMwarName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_BsnAPPrimaryMwarName_Type.__name__ = "OctetString"
_BsnAPPrimaryMwarName_Object = MibTableColumn
bsnAPPrimaryMwarName = _BsnAPPrimaryMwarName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 10),
    _BsnAPPrimaryMwarName_Type()
)
bsnAPPrimaryMwarName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPPrimaryMwarName.setStatus("current")


class _BsnAPReset_Type(Integer32):
    """Custom type bsnAPReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_BsnAPReset_Type.__name__ = "Integer32"
_BsnAPReset_Object = MibTableColumn
bsnAPReset = _BsnAPReset_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 11),
    _BsnAPReset_Type()
)
bsnAPReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPReset.setStatus("current")


class _BsnAPStatsTimer_Type(Integer32):
    """Custom type bsnAPStatsTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BsnAPStatsTimer_Type.__name__ = "Integer32"
_BsnAPStatsTimer_Object = MibTableColumn
bsnAPStatsTimer = _BsnAPStatsTimer_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 12),
    _BsnAPStatsTimer_Type()
)
bsnAPStatsTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPStatsTimer.setStatus("current")


class _BsnAPPortNumber_Type(Integer32):
    """Custom type bsnAPPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BsnAPPortNumber_Type.__name__ = "Integer32"
_BsnAPPortNumber_Object = MibTableColumn
bsnAPPortNumber = _BsnAPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 13),
    _BsnAPPortNumber_Type()
)
bsnAPPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPPortNumber.setStatus("deprecated")
_BsnAPModel_Type = DisplayString
_BsnAPModel_Object = MibTableColumn
bsnAPModel = _BsnAPModel_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 16),
    _BsnAPModel_Type()
)
bsnAPModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPModel.setStatus("current")
_BsnAPSerialNumber_Type = DisplayString
_BsnAPSerialNumber_Object = MibTableColumn
bsnAPSerialNumber = _BsnAPSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 17),
    _BsnAPSerialNumber_Type()
)
bsnAPSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPSerialNumber.setStatus("current")


class _BsnAPClearConfig_Type(Integer32):
    """Custom type bsnAPClearConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("clearAll", 2),
          ("default", 0))
    )


_BsnAPClearConfig_Type.__name__ = "Integer32"
_BsnAPClearConfig_Object = MibTableColumn
bsnAPClearConfig = _BsnAPClearConfig_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 18),
    _BsnAPClearConfig_Type()
)
bsnAPClearConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPClearConfig.setStatus("current")
_BsnApIpAddress_Type = IpAddress
_BsnApIpAddress_Object = MibTableColumn
bsnApIpAddress = _BsnApIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 19),
    _BsnApIpAddress_Type()
)
bsnApIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnApIpAddress.setStatus("current")


class _BsnAPMirrorMode_Type(Integer32):
    """Custom type bsnAPMirrorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnAPMirrorMode_Type.__name__ = "Integer32"
_BsnAPMirrorMode_Object = MibTableColumn
bsnAPMirrorMode = _BsnAPMirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 20),
    _BsnAPMirrorMode_Type()
)
bsnAPMirrorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPMirrorMode.setStatus("current")


class _BsnAPRemoteModeSupport_Type(Integer32):
    """Custom type bsnAPRemoteModeSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnAPRemoteModeSupport_Type.__name__ = "Integer32"
_BsnAPRemoteModeSupport_Object = MibTableColumn
bsnAPRemoteModeSupport = _BsnAPRemoteModeSupport_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 21),
    _BsnAPRemoteModeSupport_Type()
)
bsnAPRemoteModeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPRemoteModeSupport.setStatus("current")


class _BsnAPType_Type(Integer32):
    """Custom type bsnAPType based on Integer32"""
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
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54)
        )
    )
    namedValues = NamedValues(
        *(("ap1000", 1),
          ("ap1030", 2),
          ("ap1040", 21),
          ("ap1100", 5),
          ("ap1130", 6),
          ("ap1140", 16),
          ("ap1200", 8),
          ("ap1240", 7),
          ("ap1250", 11),
          ("ap1260", 20),
          ("ap1310", 9),
          ("ap1500", 10),
          ("ap1505", 12),
          ("ap1520", 14),
          ("ap1530e", 38),
          ("ap1530i", 37),
          ("ap1550", 22),
          ("ap1570e", 53),
          ("ap1570i", 54),
          ("ap1600e", 33),
          ("ap1600i", 32),
          ("ap1700e", 52),
          ("ap1700i", 51),
          ("ap2600e", 30),
          ("ap2600i", 29),
          ("ap2700e", 42),
          ("ap2700i", 43),
          ("ap3201", 13),
          ("ap3500e", 19),
          ("ap3500i", 18),
          ("ap3500p", 24),
          ("ap3600e", 28),
          ("ap3600i", 27),
          ("ap3600p", 36),
          ("ap3700e", 39),
          ("ap3700i", 40),
          ("ap3700p", 41),
          ("ap602i", 23),
          ("ap702e", 34),
          ("ap702i", 35),
          ("ap702w", 44),
          ("ap800", 15),
          ("ap800agn", 17),
          ("ap802agn", 26),
          ("ap802gn", 25),
          ("ap802hagn", 31),
          ("mimo", 3),
          ("unknown", 4),
          ("wap1600e", 48),
          ("wap1600i", 47),
          ("wap2600e", 46),
          ("wap2600i", 45),
          ("wap702e", 50),
          ("wap702i", 49))
    )


_BsnAPType_Type.__name__ = "Integer32"
_BsnAPType_Object = MibTableColumn
bsnAPType = _BsnAPType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 22),
    _BsnAPType_Type()
)
bsnAPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPType.setStatus("current")


class _BsnAPSecondaryMwarName_Type(OctetString):
    """Custom type bsnAPSecondaryMwarName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_BsnAPSecondaryMwarName_Type.__name__ = "OctetString"
_BsnAPSecondaryMwarName_Object = MibTableColumn
bsnAPSecondaryMwarName = _BsnAPSecondaryMwarName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 23),
    _BsnAPSecondaryMwarName_Type()
)
bsnAPSecondaryMwarName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPSecondaryMwarName.setStatus("current")


class _BsnAPTertiaryMwarName_Type(OctetString):
    """Custom type bsnAPTertiaryMwarName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_BsnAPTertiaryMwarName_Type.__name__ = "OctetString"
_BsnAPTertiaryMwarName_Object = MibTableColumn
bsnAPTertiaryMwarName = _BsnAPTertiaryMwarName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 24),
    _BsnAPTertiaryMwarName_Type()
)
bsnAPTertiaryMwarName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPTertiaryMwarName.setStatus("current")


class _BsnAPIsStaticIP_Type(Integer32):
    """Custom type bsnAPIsStaticIP based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnAPIsStaticIP_Type.__name__ = "Integer32"
_BsnAPIsStaticIP_Object = MibTableColumn
bsnAPIsStaticIP = _BsnAPIsStaticIP_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 25),
    _BsnAPIsStaticIP_Type()
)
bsnAPIsStaticIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPIsStaticIP.setStatus("current")
_BsnAPNetmask_Type = IpAddress
_BsnAPNetmask_Object = MibTableColumn
bsnAPNetmask = _BsnAPNetmask_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 26),
    _BsnAPNetmask_Type()
)
bsnAPNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPNetmask.setStatus("current")
_BsnAPGateway_Type = IpAddress
_BsnAPGateway_Object = MibTableColumn
bsnAPGateway = _BsnAPGateway_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 27),
    _BsnAPGateway_Type()
)
bsnAPGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPGateway.setStatus("current")
_BsnAPStaticIPAddress_Type = IpAddress
_BsnAPStaticIPAddress_Object = MibTableColumn
bsnAPStaticIPAddress = _BsnAPStaticIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 28),
    _BsnAPStaticIPAddress_Type()
)
bsnAPStaticIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPStaticIPAddress.setStatus("current")


class _BsnAPBridgingSupport_Type(Integer32):
    """Custom type bsnAPBridgingSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnAPBridgingSupport_Type.__name__ = "Integer32"
_BsnAPBridgingSupport_Object = MibTableColumn
bsnAPBridgingSupport = _BsnAPBridgingSupport_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 29),
    _BsnAPBridgingSupport_Type()
)
bsnAPBridgingSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPBridgingSupport.setStatus("current")


class _BsnAPGroupVlanName_Type(OctetString):
    """Custom type bsnAPGroupVlanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BsnAPGroupVlanName_Type.__name__ = "OctetString"
_BsnAPGroupVlanName_Object = MibTableColumn
bsnAPGroupVlanName = _BsnAPGroupVlanName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 30),
    _BsnAPGroupVlanName_Type()
)
bsnAPGroupVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPGroupVlanName.setStatus("current")
_BsnAPIOSVersion_Type = DisplayString
_BsnAPIOSVersion_Object = MibTableColumn
bsnAPIOSVersion = _BsnAPIOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 31),
    _BsnAPIOSVersion_Type()
)
bsnAPIOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIOSVersion.setStatus("current")


class _BsnAPCertificateType_Type(Integer32):
    """Custom type bsnAPCertificateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localsignificance", 3),
          ("manufactureinstalled", 1),
          ("selfsigned", 2),
          ("unknown", 0))
    )


_BsnAPCertificateType_Type.__name__ = "Integer32"
_BsnAPCertificateType_Object = MibTableColumn
bsnAPCertificateType = _BsnAPCertificateType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 32),
    _BsnAPCertificateType_Type()
)
bsnAPCertificateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPCertificateType.setStatus("current")
_BsnAPEthernetMacAddress_Type = MacAddress
_BsnAPEthernetMacAddress_Object = MibTableColumn
bsnAPEthernetMacAddress = _BsnAPEthernetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 33),
    _BsnAPEthernetMacAddress_Type()
)
bsnAPEthernetMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPEthernetMacAddress.setStatus("current")


class _BsnAPAdminStatus_Type(Integer32):
    """Custom type bsnAPAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_BsnAPAdminStatus_Type.__name__ = "Integer32"
_BsnAPAdminStatus_Object = MibTableColumn
bsnAPAdminStatus = _BsnAPAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 1, 1, 37),
    _BsnAPAdminStatus_Type()
)
bsnAPAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPAdminStatus.setStatus("deprecated")
_BsnAPIfTable_Object = MibTable
bsnAPIfTable = _BsnAPIfTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 2)
)
if mibBuilder.loadTexts:
    bsnAPIfTable.setStatus("current")
_BsnAPIfEntry_Object = MibTableRow
bsnAPIfEntry = _BsnAPIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 2, 1)
)
bsnAPIfEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
)
if mibBuilder.loadTexts:
    bsnAPIfEntry.setStatus("current")


class _BsnAPIfSlotId_Type(Unsigned32):
    """Custom type bsnAPIfSlotId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BsnAPIfSlotId_Type.__name__ = "Unsigned32"
_BsnAPIfSlotId_Object = MibTableColumn
bsnAPIfSlotId = _BsnAPIfSlotId_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 2, 1, 1),
    _BsnAPIfSlotId_Type()
)
bsnAPIfSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfSlotId.setStatus("current")


class _BsnAPIfType_Type(Integer32):
    """Custom type bsnAPIfType based on Integer32"""
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
        *(("dot11a", 2),
          ("dot11abgn", 3),
          ("dot11b", 1),
          ("uwb", 4))
    )


_BsnAPIfType_Type.__name__ = "Integer32"
_BsnAPIfType_Object = MibTableColumn
bsnAPIfType = _BsnAPIfType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 2, 1, 2),
    _BsnAPIfType_Type()
)
bsnAPIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfType.setStatus("current")


class _BsnAPIfPhyChannelAssignment_Type(Integer32):
    """Custom type bsnAPIfPhyChannelAssignment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("customized", 2))
    )


_BsnAPIfPhyChannelAssignment_Type.__name__ = "Integer32"
_BsnAPIfPhyChannelAssignment_Object = MibTableColumn
bsnAPIfPhyChannelAssignment = _BsnAPIfPhyChannelAssignment_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 2, 1, 3),
    _BsnAPIfPhyChannelAssignment_Type()
)
bsnAPIfPhyChannelAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPIfPhyChannelAssignment.setStatus("current")


class _BsnAPIfPhyChannelNumber_Type(Integer32):
    """Custom type bsnAPIfPhyChannelNumber based on Integer32"""
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
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              34,
              36,
              38,
              40,
              42,
              44,
              46,
              48,
              52,
              56,
              60,
              64,
              100,
              104,
              108,
              112,
              116,
              120,
              124,
              128,
              132,
              136,
              140,
              149,
              153,
              157,
              161,
              165,
              169,
              173)
        )
    )
    namedValues = NamedValues(
        *(("ch1", 1),
          ("ch10", 10),
          ("ch100", 100),
          ("ch104", 104),
          ("ch108", 108),
          ("ch11", 11),
          ("ch112", 112),
          ("ch116", 116),
          ("ch12", 12),
          ("ch120", 120),
          ("ch124", 124),
          ("ch128", 128),
          ("ch13", 13),
          ("ch132", 132),
          ("ch136", 136),
          ("ch14", 14),
          ("ch140", 140),
          ("ch149", 149),
          ("ch153", 153),
          ("ch157", 157),
          ("ch161", 161),
          ("ch165", 165),
          ("ch169", 169),
          ("ch173", 173),
          ("ch2", 2),
          ("ch20", 20),
          ("ch21", 21),
          ("ch22", 22),
          ("ch23", 23),
          ("ch24", 24),
          ("ch25", 25),
          ("ch26", 26),
          ("ch3", 3),
          ("ch34", 34),
          ("ch36", 36),
          ("ch38", 38),
          ("ch4", 4),
          ("ch40", 40),
          ("ch42", 42),
          ("ch44", 44),
          ("ch46", 46),
          ("ch48", 48),
          ("ch5", 5),
          ("ch52", 52),
          ("ch56", 56),
          ("ch6", 6),
          ("ch60", 60),
          ("ch64", 64),
          ("ch7", 7),
          ("ch8", 8),
          ("ch9", 9))
    )


_BsnAPIfPhyChannelNumber_Type.__name__ = "Integer32"
_BsnAPIfPhyChannelNumber_Object = MibTableColumn
bsnAPIfPhyChannelNumber = _BsnAPIfPhyChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 2, 1, 4),
    _BsnAPIfPhyChannelNumber_Type()
)
bsnAPIfPhyChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPIfPhyChannelNumber.setStatus("current")


class _BsnAPIfPhyTxPowerControl_Type(Integer32):
    """Custom type bsnAPIfPhyTxPowerControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("customized", 2))
    )


_BsnAPIfPhyTxPowerControl_Type.__name__ = "Integer32"
_BsnAPIfPhyTxPowerControl_Object = MibTableColumn
bsnAPIfPhyTxPowerControl = _BsnAPIfPhyTxPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 2, 1, 5),
    _BsnAPIfPhyTxPowerControl_Type()
)
bsnAPIfPhyTxPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPIfPhyTxPowerControl.setStatus("current")


class _BsnAPIfPhyTxPowerLevel_Type(Integer32):
    """Custom type bsnAPIfPhyTxPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BsnAPIfPhyTxPowerLevel_Type.__name__ = "Integer32"
_BsnAPIfPhyTxPowerLevel_Object = MibTableColumn
bsnAPIfPhyTxPowerLevel = _BsnAPIfPhyTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 2, 1, 6),
    _BsnAPIfPhyTxPowerLevel_Type()
)
bsnAPIfPhyTxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPIfPhyTxPowerLevel.setStatus("current")


class _BsnAPIfPhyAntennaMode_Type(Integer32):
    """Custom type bsnAPIfPhyAntennaMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("notapplicable", 99),
          ("omni", 3),
          ("sectorA", 1),
          ("sectorB", 2))
    )


_BsnAPIfPhyAntennaMode_Type.__name__ = "Integer32"
_BsnAPIfPhyAntennaMode_Object = MibTableColumn
bsnAPIfPhyAntennaMode = _BsnAPIfPhyAntennaMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 2, 1, 7),
    _BsnAPIfPhyAntennaMode_Type()
)
bsnAPIfPhyAntennaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPIfPhyAntennaMode.setStatus("current")


class _BsnAPIfPhyAntennaType_Type(Integer32):
    """Custom type bsnAPIfPhyAntennaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_BsnAPIfPhyAntennaType_Type.__name__ = "Integer32"
_BsnAPIfPhyAntennaType_Object = MibTableColumn
bsnAPIfPhyAntennaType = _BsnAPIfPhyAntennaType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 2, 1, 8),
    _BsnAPIfPhyAntennaType_Type()
)
bsnAPIfPhyAntennaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPIfPhyAntennaType.setStatus("current")


class _BsnAPIfPhyAntennaDiversity_Type(Integer32):
    """Custom type bsnAPIfPhyAntennaDiversity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("connectorA", 0),
          ("connectorB", 1),
          ("enabled", 255))
    )


_BsnAPIfPhyAntennaDiversity_Type.__name__ = "Integer32"
_BsnAPIfPhyAntennaDiversity_Object = MibTableColumn
bsnAPIfPhyAntennaDiversity = _BsnAPIfPhyAntennaDiversity_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 2, 1, 9),
    _BsnAPIfPhyAntennaDiversity_Type()
)
bsnAPIfPhyAntennaDiversity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPIfPhyAntennaDiversity.setStatus("current")
_BsnAPIfCellSiteConfigId_Type = Unsigned32
_BsnAPIfCellSiteConfigId_Object = MibTableColumn
bsnAPIfCellSiteConfigId = _BsnAPIfCellSiteConfigId_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 2, 1, 10),
    _BsnAPIfCellSiteConfigId_Type()
)
bsnAPIfCellSiteConfigId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPIfCellSiteConfigId.setStatus("current")


class _BsnAPIfNumberOfVaps_Type(Integer32):
    """Custom type bsnAPIfNumberOfVaps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BsnAPIfNumberOfVaps_Type.__name__ = "Integer32"
_BsnAPIfNumberOfVaps_Object = MibTableColumn
bsnAPIfNumberOfVaps = _BsnAPIfNumberOfVaps_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 2, 1, 11),
    _BsnAPIfNumberOfVaps_Type()
)
bsnAPIfNumberOfVaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfNumberOfVaps.setStatus("current")


class _BsnAPIfOperStatus_Type(Integer32):
    """Custom type bsnAPIfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_BsnAPIfOperStatus_Type.__name__ = "Integer32"
_BsnAPIfOperStatus_Object = MibTableColumn
bsnAPIfOperStatus = _BsnAPIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 2, 1, 12),
    _BsnAPIfOperStatus_Type()
)
bsnAPIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfOperStatus.setStatus("current")


class _BsnAPIfPortNumber_Type(Integer32):
    """Custom type bsnAPIfPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BsnAPIfPortNumber_Type.__name__ = "Integer32"
_BsnAPIfPortNumber_Object = MibTableColumn
bsnAPIfPortNumber = _BsnAPIfPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 2, 1, 13),
    _BsnAPIfPortNumber_Type()
)
bsnAPIfPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfPortNumber.setStatus("current")


class _BsnAPIfPhyAntennaOptions_Type(Integer32):
    """Custom type bsnAPIfPhyAntennaOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ext11bInt11a", 4),
          ("external", 3),
          ("internal", 1),
          ("internalAndExternal", 0),
          ("siacAp", 2))
    )


_BsnAPIfPhyAntennaOptions_Type.__name__ = "Integer32"
_BsnAPIfPhyAntennaOptions_Object = MibTableColumn
bsnAPIfPhyAntennaOptions = _BsnAPIfPhyAntennaOptions_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 2, 1, 14),
    _BsnAPIfPhyAntennaOptions_Type()
)
bsnAPIfPhyAntennaOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfPhyAntennaOptions.setStatus("current")
_BsnApIfNoOfUsers_Type = Counter32
_BsnApIfNoOfUsers_Object = MibTableColumn
bsnApIfNoOfUsers = _BsnApIfNoOfUsers_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 2, 1, 15),
    _BsnApIfNoOfUsers_Type()
)
bsnApIfNoOfUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnApIfNoOfUsers.setStatus("current")


class _BsnAPIfWlanOverride_Type(Integer32):
    """Custom type bsnAPIfWlanOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnAPIfWlanOverride_Type.__name__ = "Integer32"
_BsnAPIfWlanOverride_Object = MibTableColumn
bsnAPIfWlanOverride = _BsnAPIfWlanOverride_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 2, 1, 16),
    _BsnAPIfWlanOverride_Type()
)
bsnAPIfWlanOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPIfWlanOverride.setStatus("current")


class _BsnAPIfPacketsSniffingFeature_Type(Integer32):
    """Custom type bsnAPIfPacketsSniffingFeature based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnAPIfPacketsSniffingFeature_Type.__name__ = "Integer32"
_BsnAPIfPacketsSniffingFeature_Object = MibTableColumn
bsnAPIfPacketsSniffingFeature = _BsnAPIfPacketsSniffingFeature_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 2, 1, 17),
    _BsnAPIfPacketsSniffingFeature_Type()
)
bsnAPIfPacketsSniffingFeature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPIfPacketsSniffingFeature.setStatus("current")


class _BsnAPIfSniffChannel_Type(Integer32):
    """Custom type bsnAPIfSniffChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              34,
              36,
              38,
              40,
              42,
              44,
              46,
              48,
              52,
              56,
              60,
              64,
              100,
              104,
              108,
              112,
              116,
              120,
              124,
              128,
              132,
              136,
              140,
              149,
              153,
              157,
              161,
              165,
              169,
              173)
        )
    )
    namedValues = NamedValues(
        *(("ch0", 0),
          ("ch1", 1),
          ("ch10", 10),
          ("ch100", 100),
          ("ch104", 104),
          ("ch108", 108),
          ("ch11", 11),
          ("ch112", 112),
          ("ch116", 116),
          ("ch12", 12),
          ("ch120", 120),
          ("ch124", 124),
          ("ch128", 128),
          ("ch13", 13),
          ("ch132", 132),
          ("ch136", 136),
          ("ch14", 14),
          ("ch140", 140),
          ("ch149", 149),
          ("ch153", 153),
          ("ch157", 157),
          ("ch161", 161),
          ("ch165", 165),
          ("ch169", 169),
          ("ch173", 173),
          ("ch2", 2),
          ("ch20", 20),
          ("ch21", 21),
          ("ch22", 22),
          ("ch23", 23),
          ("ch24", 24),
          ("ch25", 25),
          ("ch26", 26),
          ("ch3", 3),
          ("ch34", 34),
          ("ch36", 36),
          ("ch38", 38),
          ("ch4", 4),
          ("ch40", 40),
          ("ch42", 42),
          ("ch44", 44),
          ("ch46", 46),
          ("ch48", 48),
          ("ch5", 5),
          ("ch52", 52),
          ("ch56", 56),
          ("ch6", 6),
          ("ch60", 60),
          ("ch64", 64),
          ("ch7", 7),
          ("ch8", 8),
          ("ch9", 9))
    )


_BsnAPIfSniffChannel_Type.__name__ = "Integer32"
_BsnAPIfSniffChannel_Object = MibTableColumn
bsnAPIfSniffChannel = _BsnAPIfSniffChannel_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 2, 1, 18),
    _BsnAPIfSniffChannel_Type()
)
bsnAPIfSniffChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPIfSniffChannel.setStatus("current")
_BsnAPIfSniffServerIPAddress_Type = IpAddress
_BsnAPIfSniffServerIPAddress_Object = MibTableColumn
bsnAPIfSniffServerIPAddress = _BsnAPIfSniffServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 2, 1, 19),
    _BsnAPIfSniffServerIPAddress_Type()
)
bsnAPIfSniffServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPIfSniffServerIPAddress.setStatus("current")


class _BsnAPIfAntennaGain_Type(Integer32):
    """Custom type bsnAPIfAntennaGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_BsnAPIfAntennaGain_Type.__name__ = "Integer32"
_BsnAPIfAntennaGain_Object = MibTableColumn
bsnAPIfAntennaGain = _BsnAPIfAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 2, 1, 20),
    _BsnAPIfAntennaGain_Type()
)
bsnAPIfAntennaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPIfAntennaGain.setStatus("current")
_BsnAPIfChannelList_Type = DisplayString
_BsnAPIfChannelList_Object = MibTableColumn
bsnAPIfChannelList = _BsnAPIfChannelList_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 2, 1, 21),
    _BsnAPIfChannelList_Type()
)
bsnAPIfChannelList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPIfChannelList.setStatus("current")
_BsnAPIfAbsolutePowerList_Type = DisplayString
_BsnAPIfAbsolutePowerList_Object = MibTableColumn
bsnAPIfAbsolutePowerList = _BsnAPIfAbsolutePowerList_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 2, 1, 22),
    _BsnAPIfAbsolutePowerList_Type()
)
bsnAPIfAbsolutePowerList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPIfAbsolutePowerList.setStatus("current")


class _BsnAPIfRegulatoryDomainSupport_Type(Integer32):
    """Custom type bsnAPIfRegulatoryDomainSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("supported", 1))
    )


_BsnAPIfRegulatoryDomainSupport_Type.__name__ = "Integer32"
_BsnAPIfRegulatoryDomainSupport_Object = MibTableColumn
bsnAPIfRegulatoryDomainSupport = _BsnAPIfRegulatoryDomainSupport_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 2, 1, 23),
    _BsnAPIfRegulatoryDomainSupport_Type()
)
bsnAPIfRegulatoryDomainSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfRegulatoryDomainSupport.setStatus("current")


class _BsnAPIfAdminStatus_Type(Integer32):
    """Custom type bsnAPIfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_BsnAPIfAdminStatus_Type.__name__ = "Integer32"
_BsnAPIfAdminStatus_Object = MibTableColumn
bsnAPIfAdminStatus = _BsnAPIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 2, 1, 34),
    _BsnAPIfAdminStatus_Type()
)
bsnAPIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPIfAdminStatus.setStatus("deprecated")
_BsnAPIfSmtParamTable_Object = MibTable
bsnAPIfSmtParamTable = _BsnAPIfSmtParamTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 3)
)
if mibBuilder.loadTexts:
    bsnAPIfSmtParamTable.setStatus("current")
_BsnAPIfSmtParamEntry_Object = MibTableRow
bsnAPIfSmtParamEntry = _BsnAPIfSmtParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 3, 1)
)
bsnAPIfSmtParamEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
)
if mibBuilder.loadTexts:
    bsnAPIfSmtParamEntry.setStatus("current")


class _BsnAPIfDot11BeaconPeriod_Type(Integer32):
    """Custom type bsnAPIfDot11BeaconPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 1000),
    )


_BsnAPIfDot11BeaconPeriod_Type.__name__ = "Integer32"
_BsnAPIfDot11BeaconPeriod_Object = MibTableColumn
bsnAPIfDot11BeaconPeriod = _BsnAPIfDot11BeaconPeriod_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 3, 1, 1),
    _BsnAPIfDot11BeaconPeriod_Type()
)
bsnAPIfDot11BeaconPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11BeaconPeriod.setStatus("current")


class _BsnAPIfDot11MediumOccupancyLimit_Type(Integer32):
    """Custom type bsnAPIfDot11MediumOccupancyLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_BsnAPIfDot11MediumOccupancyLimit_Type.__name__ = "Integer32"
_BsnAPIfDot11MediumOccupancyLimit_Object = MibTableColumn
bsnAPIfDot11MediumOccupancyLimit = _BsnAPIfDot11MediumOccupancyLimit_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 3, 1, 2),
    _BsnAPIfDot11MediumOccupancyLimit_Type()
)
bsnAPIfDot11MediumOccupancyLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11MediumOccupancyLimit.setStatus("current")


class _BsnAPIfDot11CFPPeriod_Type(Integer32):
    """Custom type bsnAPIfDot11CFPPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BsnAPIfDot11CFPPeriod_Type.__name__ = "Integer32"
_BsnAPIfDot11CFPPeriod_Object = MibTableColumn
bsnAPIfDot11CFPPeriod = _BsnAPIfDot11CFPPeriod_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 3, 1, 3),
    _BsnAPIfDot11CFPPeriod_Type()
)
bsnAPIfDot11CFPPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11CFPPeriod.setStatus("current")


class _BsnAPIfDot11CFPMaxDuration_Type(Integer32):
    """Custom type bsnAPIfDot11CFPMaxDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BsnAPIfDot11CFPMaxDuration_Type.__name__ = "Integer32"
_BsnAPIfDot11CFPMaxDuration_Object = MibTableColumn
bsnAPIfDot11CFPMaxDuration = _BsnAPIfDot11CFPMaxDuration_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 3, 1, 4),
    _BsnAPIfDot11CFPMaxDuration_Type()
)
bsnAPIfDot11CFPMaxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11CFPMaxDuration.setStatus("current")


class _BsnAPIfDot11OperationalRateSet_Type(OctetString):
    """Custom type bsnAPIfDot11OperationalRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 126),
    )


_BsnAPIfDot11OperationalRateSet_Type.__name__ = "OctetString"
_BsnAPIfDot11OperationalRateSet_Object = MibTableColumn
bsnAPIfDot11OperationalRateSet = _BsnAPIfDot11OperationalRateSet_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 3, 1, 5),
    _BsnAPIfDot11OperationalRateSet_Type()
)
bsnAPIfDot11OperationalRateSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11OperationalRateSet.setStatus("current")


class _BsnAPIfDot11DTIMPeriod_Type(Integer32):
    """Custom type bsnAPIfDot11DTIMPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BsnAPIfDot11DTIMPeriod_Type.__name__ = "Integer32"
_BsnAPIfDot11DTIMPeriod_Object = MibTableColumn
bsnAPIfDot11DTIMPeriod = _BsnAPIfDot11DTIMPeriod_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 3, 1, 6),
    _BsnAPIfDot11DTIMPeriod_Type()
)
bsnAPIfDot11DTIMPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11DTIMPeriod.setStatus("current")


class _BsnAPIfDot11MultiDomainCapabilityImplemented_Type(Integer32):
    """Custom type bsnAPIfDot11MultiDomainCapabilityImplemented based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("implemented", 1),
          ("notimplemented", 0))
    )


_BsnAPIfDot11MultiDomainCapabilityImplemented_Type.__name__ = "Integer32"
_BsnAPIfDot11MultiDomainCapabilityImplemented_Object = MibTableColumn
bsnAPIfDot11MultiDomainCapabilityImplemented = _BsnAPIfDot11MultiDomainCapabilityImplemented_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 3, 1, 7),
    _BsnAPIfDot11MultiDomainCapabilityImplemented_Type()
)
bsnAPIfDot11MultiDomainCapabilityImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11MultiDomainCapabilityImplemented.setStatus("current")


class _BsnAPIfDot11MultiDomainCapabilityEnabled_Type(Integer32):
    """Custom type bsnAPIfDot11MultiDomainCapabilityEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_BsnAPIfDot11MultiDomainCapabilityEnabled_Type.__name__ = "Integer32"
_BsnAPIfDot11MultiDomainCapabilityEnabled_Object = MibTableColumn
bsnAPIfDot11MultiDomainCapabilityEnabled = _BsnAPIfDot11MultiDomainCapabilityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 3, 1, 8),
    _BsnAPIfDot11MultiDomainCapabilityEnabled_Type()
)
bsnAPIfDot11MultiDomainCapabilityEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11MultiDomainCapabilityEnabled.setStatus("current")


class _BsnAPIfDot11CountryString_Type(OctetString):
    """Custom type bsnAPIfDot11CountryString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_BsnAPIfDot11CountryString_Type.__name__ = "OctetString"
_BsnAPIfDot11CountryString_Object = MibTableColumn
bsnAPIfDot11CountryString = _BsnAPIfDot11CountryString_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 3, 1, 9),
    _BsnAPIfDot11CountryString_Type()
)
bsnAPIfDot11CountryString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11CountryString.setStatus("current")


class _BsnAPIfDot11SmtParamsConfigType_Type(Integer32):
    """Custom type bsnAPIfDot11SmtParamsConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 0),
          ("customized", 1))
    )


_BsnAPIfDot11SmtParamsConfigType_Type.__name__ = "Integer32"
_BsnAPIfDot11SmtParamsConfigType_Object = MibTableColumn
bsnAPIfDot11SmtParamsConfigType = _BsnAPIfDot11SmtParamsConfigType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 3, 1, 10),
    _BsnAPIfDot11SmtParamsConfigType_Type()
)
bsnAPIfDot11SmtParamsConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11SmtParamsConfigType.setStatus("current")
_BsnAPIfDot11BSSID_Type = MacAddress
_BsnAPIfDot11BSSID_Object = MibTableColumn
bsnAPIfDot11BSSID = _BsnAPIfDot11BSSID_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 3, 1, 30),
    _BsnAPIfDot11BSSID_Type()
)
bsnAPIfDot11BSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11BSSID.setStatus("current")
_BsnAPIfMultiDomainCapabilityTable_Object = MibTable
bsnAPIfMultiDomainCapabilityTable = _BsnAPIfMultiDomainCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 4)
)
if mibBuilder.loadTexts:
    bsnAPIfMultiDomainCapabilityTable.setStatus("current")
_BsnAPIfMultiDomainCapabilityEntry_Object = MibTableRow
bsnAPIfMultiDomainCapabilityEntry = _BsnAPIfMultiDomainCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 4, 1)
)
bsnAPIfMultiDomainCapabilityEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
)
if mibBuilder.loadTexts:
    bsnAPIfMultiDomainCapabilityEntry.setStatus("current")
_BsnAPIfDot11MaximumTransmitPowerLevel_Type = Integer32
_BsnAPIfDot11MaximumTransmitPowerLevel_Object = MibTableColumn
bsnAPIfDot11MaximumTransmitPowerLevel = _BsnAPIfDot11MaximumTransmitPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 4, 1, 1),
    _BsnAPIfDot11MaximumTransmitPowerLevel_Type()
)
bsnAPIfDot11MaximumTransmitPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11MaximumTransmitPowerLevel.setStatus("current")
_BsnAPIfDot11FirstChannelNumber_Type = Integer32
_BsnAPIfDot11FirstChannelNumber_Object = MibTableColumn
bsnAPIfDot11FirstChannelNumber = _BsnAPIfDot11FirstChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 4, 1, 2),
    _BsnAPIfDot11FirstChannelNumber_Type()
)
bsnAPIfDot11FirstChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11FirstChannelNumber.setStatus("current")
_BsnAPIfDot11NumberofChannels_Type = Integer32
_BsnAPIfDot11NumberofChannels_Object = MibTableColumn
bsnAPIfDot11NumberofChannels = _BsnAPIfDot11NumberofChannels_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 4, 1, 20),
    _BsnAPIfDot11NumberofChannels_Type()
)
bsnAPIfDot11NumberofChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11NumberofChannels.setStatus("current")
_BsnAPIfMacOperationParamTable_Object = MibTable
bsnAPIfMacOperationParamTable = _BsnAPIfMacOperationParamTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 5)
)
if mibBuilder.loadTexts:
    bsnAPIfMacOperationParamTable.setStatus("current")
_BsnAPIfMacOperationParamEntry_Object = MibTableRow
bsnAPIfMacOperationParamEntry = _BsnAPIfMacOperationParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 5, 1)
)
bsnAPIfMacOperationParamEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
)
if mibBuilder.loadTexts:
    bsnAPIfMacOperationParamEntry.setStatus("current")


class _BsnAPIfDot11MacRTSThreshold_Type(Integer32):
    """Custom type bsnAPIfDot11MacRTSThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2347),
    )


_BsnAPIfDot11MacRTSThreshold_Type.__name__ = "Integer32"
_BsnAPIfDot11MacRTSThreshold_Object = MibTableColumn
bsnAPIfDot11MacRTSThreshold = _BsnAPIfDot11MacRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 5, 1, 1),
    _BsnAPIfDot11MacRTSThreshold_Type()
)
bsnAPIfDot11MacRTSThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11MacRTSThreshold.setStatus("current")


class _BsnAPIfDot11MacShortRetryLimit_Type(Integer32):
    """Custom type bsnAPIfDot11MacShortRetryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BsnAPIfDot11MacShortRetryLimit_Type.__name__ = "Integer32"
_BsnAPIfDot11MacShortRetryLimit_Object = MibTableColumn
bsnAPIfDot11MacShortRetryLimit = _BsnAPIfDot11MacShortRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 5, 1, 2),
    _BsnAPIfDot11MacShortRetryLimit_Type()
)
bsnAPIfDot11MacShortRetryLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11MacShortRetryLimit.setStatus("current")


class _BsnAPIfDot11MacLongRetryLimit_Type(Integer32):
    """Custom type bsnAPIfDot11MacLongRetryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BsnAPIfDot11MacLongRetryLimit_Type.__name__ = "Integer32"
_BsnAPIfDot11MacLongRetryLimit_Object = MibTableColumn
bsnAPIfDot11MacLongRetryLimit = _BsnAPIfDot11MacLongRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 5, 1, 3),
    _BsnAPIfDot11MacLongRetryLimit_Type()
)
bsnAPIfDot11MacLongRetryLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11MacLongRetryLimit.setStatus("current")


class _BsnAPIfDot11MacFragmentationThreshold_Type(Integer32):
    """Custom type bsnAPIfDot11MacFragmentationThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_BsnAPIfDot11MacFragmentationThreshold_Type.__name__ = "Integer32"
_BsnAPIfDot11MacFragmentationThreshold_Object = MibTableColumn
bsnAPIfDot11MacFragmentationThreshold = _BsnAPIfDot11MacFragmentationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 5, 1, 4),
    _BsnAPIfDot11MacFragmentationThreshold_Type()
)
bsnAPIfDot11MacFragmentationThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11MacFragmentationThreshold.setStatus("current")


class _BsnAPIfDot11MacMaxTransmitMSDULifetime_Type(Unsigned32):
    """Custom type bsnAPIfDot11MacMaxTransmitMSDULifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_BsnAPIfDot11MacMaxTransmitMSDULifetime_Type.__name__ = "Unsigned32"
_BsnAPIfDot11MacMaxTransmitMSDULifetime_Object = MibTableColumn
bsnAPIfDot11MacMaxTransmitMSDULifetime = _BsnAPIfDot11MacMaxTransmitMSDULifetime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 5, 1, 5),
    _BsnAPIfDot11MacMaxTransmitMSDULifetime_Type()
)
bsnAPIfDot11MacMaxTransmitMSDULifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11MacMaxTransmitMSDULifetime.setStatus("current")


class _BsnAPIfDot11MacParamsConfigType_Type(Integer32):
    """Custom type bsnAPIfDot11MacParamsConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 0),
          ("customized", 1))
    )


_BsnAPIfDot11MacParamsConfigType_Type.__name__ = "Integer32"
_BsnAPIfDot11MacParamsConfigType_Object = MibTableColumn
bsnAPIfDot11MacParamsConfigType = _BsnAPIfDot11MacParamsConfigType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 5, 1, 6),
    _BsnAPIfDot11MacParamsConfigType_Type()
)
bsnAPIfDot11MacParamsConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11MacParamsConfigType.setStatus("current")


class _BsnAPIfDot11MacMaxReceiveLifetime_Type(Unsigned32):
    """Custom type bsnAPIfDot11MacMaxReceiveLifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_BsnAPIfDot11MacMaxReceiveLifetime_Type.__name__ = "Unsigned32"
_BsnAPIfDot11MacMaxReceiveLifetime_Object = MibTableColumn
bsnAPIfDot11MacMaxReceiveLifetime = _BsnAPIfDot11MacMaxReceiveLifetime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 5, 1, 25),
    _BsnAPIfDot11MacMaxReceiveLifetime_Type()
)
bsnAPIfDot11MacMaxReceiveLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11MacMaxReceiveLifetime.setStatus("current")
_BsnAPIfDot11CountersTable_Object = MibTable
bsnAPIfDot11CountersTable = _BsnAPIfDot11CountersTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 6)
)
if mibBuilder.loadTexts:
    bsnAPIfDot11CountersTable.setStatus("current")
_BsnAPIfDot11CountersEntry_Object = MibTableRow
bsnAPIfDot11CountersEntry = _BsnAPIfDot11CountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 6, 1)
)
bsnAPIfDot11CountersEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
)
if mibBuilder.loadTexts:
    bsnAPIfDot11CountersEntry.setStatus("current")
_BsnAPIfDot11TransmittedFragmentCount_Type = Counter32
_BsnAPIfDot11TransmittedFragmentCount_Object = MibTableColumn
bsnAPIfDot11TransmittedFragmentCount = _BsnAPIfDot11TransmittedFragmentCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 6, 1, 1),
    _BsnAPIfDot11TransmittedFragmentCount_Type()
)
bsnAPIfDot11TransmittedFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11TransmittedFragmentCount.setStatus("current")
_BsnAPIfDot11MulticastTransmittedFrameCount_Type = Counter32
_BsnAPIfDot11MulticastTransmittedFrameCount_Object = MibTableColumn
bsnAPIfDot11MulticastTransmittedFrameCount = _BsnAPIfDot11MulticastTransmittedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 6, 1, 2),
    _BsnAPIfDot11MulticastTransmittedFrameCount_Type()
)
bsnAPIfDot11MulticastTransmittedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11MulticastTransmittedFrameCount.setStatus("current")
_BsnAPIfDot11RetryCount_Type = Counter32
_BsnAPIfDot11RetryCount_Object = MibTableColumn
bsnAPIfDot11RetryCount = _BsnAPIfDot11RetryCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 6, 1, 3),
    _BsnAPIfDot11RetryCount_Type()
)
bsnAPIfDot11RetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11RetryCount.setStatus("current")
_BsnAPIfDot11MultipleRetryCount_Type = Counter32
_BsnAPIfDot11MultipleRetryCount_Object = MibTableColumn
bsnAPIfDot11MultipleRetryCount = _BsnAPIfDot11MultipleRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 6, 1, 4),
    _BsnAPIfDot11MultipleRetryCount_Type()
)
bsnAPIfDot11MultipleRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11MultipleRetryCount.setStatus("current")
_BsnAPIfDot11FrameDuplicateCount_Type = Counter32
_BsnAPIfDot11FrameDuplicateCount_Object = MibTableColumn
bsnAPIfDot11FrameDuplicateCount = _BsnAPIfDot11FrameDuplicateCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 6, 1, 5),
    _BsnAPIfDot11FrameDuplicateCount_Type()
)
bsnAPIfDot11FrameDuplicateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11FrameDuplicateCount.setStatus("current")
_BsnAPIfDot11RTSSuccessCount_Type = Counter32
_BsnAPIfDot11RTSSuccessCount_Object = MibTableColumn
bsnAPIfDot11RTSSuccessCount = _BsnAPIfDot11RTSSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 6, 1, 6),
    _BsnAPIfDot11RTSSuccessCount_Type()
)
bsnAPIfDot11RTSSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11RTSSuccessCount.setStatus("current")
_BsnAPIfDot11RTSFailureCount_Type = Counter32
_BsnAPIfDot11RTSFailureCount_Object = MibTableColumn
bsnAPIfDot11RTSFailureCount = _BsnAPIfDot11RTSFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 6, 1, 7),
    _BsnAPIfDot11RTSFailureCount_Type()
)
bsnAPIfDot11RTSFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11RTSFailureCount.setStatus("current")
_BsnAPIfDot11ACKFailureCount_Type = Counter32
_BsnAPIfDot11ACKFailureCount_Object = MibTableColumn
bsnAPIfDot11ACKFailureCount = _BsnAPIfDot11ACKFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 6, 1, 8),
    _BsnAPIfDot11ACKFailureCount_Type()
)
bsnAPIfDot11ACKFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11ACKFailureCount.setStatus("current")
_BsnAPIfDot11ReceivedFragmentCount_Type = Counter32
_BsnAPIfDot11ReceivedFragmentCount_Object = MibTableColumn
bsnAPIfDot11ReceivedFragmentCount = _BsnAPIfDot11ReceivedFragmentCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 6, 1, 9),
    _BsnAPIfDot11ReceivedFragmentCount_Type()
)
bsnAPIfDot11ReceivedFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11ReceivedFragmentCount.setStatus("current")
_BsnAPIfDot11MulticastReceivedFrameCount_Type = Counter32
_BsnAPIfDot11MulticastReceivedFrameCount_Object = MibTableColumn
bsnAPIfDot11MulticastReceivedFrameCount = _BsnAPIfDot11MulticastReceivedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 6, 1, 10),
    _BsnAPIfDot11MulticastReceivedFrameCount_Type()
)
bsnAPIfDot11MulticastReceivedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11MulticastReceivedFrameCount.setStatus("current")
_BsnAPIfDot11FCSErrorCount_Type = Counter32
_BsnAPIfDot11FCSErrorCount_Object = MibTableColumn
bsnAPIfDot11FCSErrorCount = _BsnAPIfDot11FCSErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 6, 1, 11),
    _BsnAPIfDot11FCSErrorCount_Type()
)
bsnAPIfDot11FCSErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11FCSErrorCount.setStatus("current")
_BsnAPIfDot11TransmittedFrameCount_Type = Counter32
_BsnAPIfDot11TransmittedFrameCount_Object = MibTableColumn
bsnAPIfDot11TransmittedFrameCount = _BsnAPIfDot11TransmittedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 6, 1, 12),
    _BsnAPIfDot11TransmittedFrameCount_Type()
)
bsnAPIfDot11TransmittedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11TransmittedFrameCount.setStatus("current")
_BsnAPIfDot11WEPUndecryptableCount_Type = Counter32
_BsnAPIfDot11WEPUndecryptableCount_Object = MibTableColumn
bsnAPIfDot11WEPUndecryptableCount = _BsnAPIfDot11WEPUndecryptableCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 6, 1, 13),
    _BsnAPIfDot11WEPUndecryptableCount_Type()
)
bsnAPIfDot11WEPUndecryptableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11WEPUndecryptableCount.setStatus("current")
_BsnAPIfDot11FailedCount_Type = Counter32
_BsnAPIfDot11FailedCount_Object = MibTableColumn
bsnAPIfDot11FailedCount = _BsnAPIfDot11FailedCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 6, 1, 33),
    _BsnAPIfDot11FailedCount_Type()
)
bsnAPIfDot11FailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11FailedCount.setStatus("current")
_BsnAPIfDot11PhyTxPowerTable_Object = MibTable
bsnAPIfDot11PhyTxPowerTable = _BsnAPIfDot11PhyTxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 8)
)
if mibBuilder.loadTexts:
    bsnAPIfDot11PhyTxPowerTable.setStatus("deprecated")
_BsnAPIfDot11PhyTxPowerEntry_Object = MibTableRow
bsnAPIfDot11PhyTxPowerEntry = _BsnAPIfDot11PhyTxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 8, 1)
)
bsnAPIfDot11PhyTxPowerEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
)
if mibBuilder.loadTexts:
    bsnAPIfDot11PhyTxPowerEntry.setStatus("deprecated")


class _BsnAPIfDot11NumberSupportedPowerLevels_Type(Integer32):
    """Custom type bsnAPIfDot11NumberSupportedPowerLevels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BsnAPIfDot11NumberSupportedPowerLevels_Type.__name__ = "Integer32"
_BsnAPIfDot11NumberSupportedPowerLevels_Object = MibTableColumn
bsnAPIfDot11NumberSupportedPowerLevels = _BsnAPIfDot11NumberSupportedPowerLevels_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 8, 1, 1),
    _BsnAPIfDot11NumberSupportedPowerLevels_Type()
)
bsnAPIfDot11NumberSupportedPowerLevels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11NumberSupportedPowerLevels.setStatus("deprecated")


class _BsnAPIfDot11TxPowerLevel1_Type(Integer32):
    """Custom type bsnAPIfDot11TxPowerLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_BsnAPIfDot11TxPowerLevel1_Type.__name__ = "Integer32"
_BsnAPIfDot11TxPowerLevel1_Object = MibTableColumn
bsnAPIfDot11TxPowerLevel1 = _BsnAPIfDot11TxPowerLevel1_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 8, 1, 2),
    _BsnAPIfDot11TxPowerLevel1_Type()
)
bsnAPIfDot11TxPowerLevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11TxPowerLevel1.setStatus("deprecated")


class _BsnAPIfDot11TxPowerLevel2_Type(Integer32):
    """Custom type bsnAPIfDot11TxPowerLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_BsnAPIfDot11TxPowerLevel2_Type.__name__ = "Integer32"
_BsnAPIfDot11TxPowerLevel2_Object = MibTableColumn
bsnAPIfDot11TxPowerLevel2 = _BsnAPIfDot11TxPowerLevel2_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 8, 1, 3),
    _BsnAPIfDot11TxPowerLevel2_Type()
)
bsnAPIfDot11TxPowerLevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11TxPowerLevel2.setStatus("deprecated")


class _BsnAPIfDot11TxPowerLevel3_Type(Integer32):
    """Custom type bsnAPIfDot11TxPowerLevel3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_BsnAPIfDot11TxPowerLevel3_Type.__name__ = "Integer32"
_BsnAPIfDot11TxPowerLevel3_Object = MibTableColumn
bsnAPIfDot11TxPowerLevel3 = _BsnAPIfDot11TxPowerLevel3_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 8, 1, 4),
    _BsnAPIfDot11TxPowerLevel3_Type()
)
bsnAPIfDot11TxPowerLevel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11TxPowerLevel3.setStatus("deprecated")


class _BsnAPIfDot11TxPowerLevel4_Type(Integer32):
    """Custom type bsnAPIfDot11TxPowerLevel4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_BsnAPIfDot11TxPowerLevel4_Type.__name__ = "Integer32"
_BsnAPIfDot11TxPowerLevel4_Object = MibTableColumn
bsnAPIfDot11TxPowerLevel4 = _BsnAPIfDot11TxPowerLevel4_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 8, 1, 5),
    _BsnAPIfDot11TxPowerLevel4_Type()
)
bsnAPIfDot11TxPowerLevel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11TxPowerLevel4.setStatus("deprecated")


class _BsnAPIfDot11TxPowerLevel5_Type(Integer32):
    """Custom type bsnAPIfDot11TxPowerLevel5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_BsnAPIfDot11TxPowerLevel5_Type.__name__ = "Integer32"
_BsnAPIfDot11TxPowerLevel5_Object = MibTableColumn
bsnAPIfDot11TxPowerLevel5 = _BsnAPIfDot11TxPowerLevel5_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 8, 1, 6),
    _BsnAPIfDot11TxPowerLevel5_Type()
)
bsnAPIfDot11TxPowerLevel5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11TxPowerLevel5.setStatus("deprecated")


class _BsnAPIfDot11TxPowerLevel6_Type(Integer32):
    """Custom type bsnAPIfDot11TxPowerLevel6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_BsnAPIfDot11TxPowerLevel6_Type.__name__ = "Integer32"
_BsnAPIfDot11TxPowerLevel6_Object = MibTableColumn
bsnAPIfDot11TxPowerLevel6 = _BsnAPIfDot11TxPowerLevel6_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 8, 1, 7),
    _BsnAPIfDot11TxPowerLevel6_Type()
)
bsnAPIfDot11TxPowerLevel6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11TxPowerLevel6.setStatus("deprecated")


class _BsnAPIfDot11TxPowerLevel7_Type(Integer32):
    """Custom type bsnAPIfDot11TxPowerLevel7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_BsnAPIfDot11TxPowerLevel7_Type.__name__ = "Integer32"
_BsnAPIfDot11TxPowerLevel7_Object = MibTableColumn
bsnAPIfDot11TxPowerLevel7 = _BsnAPIfDot11TxPowerLevel7_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 8, 1, 8),
    _BsnAPIfDot11TxPowerLevel7_Type()
)
bsnAPIfDot11TxPowerLevel7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11TxPowerLevel7.setStatus("deprecated")


class _BsnAPIfDot11TxPowerLevel8_Type(Integer32):
    """Custom type bsnAPIfDot11TxPowerLevel8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_BsnAPIfDot11TxPowerLevel8_Type.__name__ = "Integer32"
_BsnAPIfDot11TxPowerLevel8_Object = MibTableColumn
bsnAPIfDot11TxPowerLevel8 = _BsnAPIfDot11TxPowerLevel8_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 8, 1, 28),
    _BsnAPIfDot11TxPowerLevel8_Type()
)
bsnAPIfDot11TxPowerLevel8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11TxPowerLevel8.setStatus("deprecated")
_BsnAPIfDot11PhyChannelTable_Object = MibTable
bsnAPIfDot11PhyChannelTable = _BsnAPIfDot11PhyChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 9)
)
if mibBuilder.loadTexts:
    bsnAPIfDot11PhyChannelTable.setStatus("current")
_BsnAPIfDot11PhyChannelEntry_Object = MibTableRow
bsnAPIfDot11PhyChannelEntry = _BsnAPIfDot11PhyChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 9, 1)
)
bsnAPIfDot11PhyChannelEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
)
if mibBuilder.loadTexts:
    bsnAPIfDot11PhyChannelEntry.setStatus("current")


class _BsnAPIfDot11CurrentCCAMode_Type(Integer32):
    """Custom type bsnAPIfDot11CurrentCCAMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("csonly", 2),
          ("cswithtimer", 8),
          ("edandcs", 4),
          ("edonly", 1),
          ("hrcsanded", 16))
    )


_BsnAPIfDot11CurrentCCAMode_Type.__name__ = "Integer32"
_BsnAPIfDot11CurrentCCAMode_Object = MibTableColumn
bsnAPIfDot11CurrentCCAMode = _BsnAPIfDot11CurrentCCAMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 9, 1, 1),
    _BsnAPIfDot11CurrentCCAMode_Type()
)
bsnAPIfDot11CurrentCCAMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11CurrentCCAMode.setStatus("current")
_BsnAPIfDot11EDThreshold_Type = Integer32
_BsnAPIfDot11EDThreshold_Object = MibTableColumn
bsnAPIfDot11EDThreshold = _BsnAPIfDot11EDThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 9, 1, 2),
    _BsnAPIfDot11EDThreshold_Type()
)
bsnAPIfDot11EDThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11EDThreshold.setStatus("current")
_BsnAPIfDot11TIThreshold_Type = Integer32
_BsnAPIfDot11TIThreshold_Object = MibTableColumn
bsnAPIfDot11TIThreshold = _BsnAPIfDot11TIThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 9, 1, 23),
    _BsnAPIfDot11TIThreshold_Type()
)
bsnAPIfDot11TIThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDot11TIThreshold.setStatus("current")
_BsnAPIfProfileThresholdConfigTable_Object = MibTable
bsnAPIfProfileThresholdConfigTable = _BsnAPIfProfileThresholdConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 12)
)
if mibBuilder.loadTexts:
    bsnAPIfProfileThresholdConfigTable.setStatus("current")
_BsnAPIfProfileThresholdConfigEntry_Object = MibTableRow
bsnAPIfProfileThresholdConfigEntry = _BsnAPIfProfileThresholdConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 12, 1)
)
bsnAPIfProfileThresholdConfigEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
)
if mibBuilder.loadTexts:
    bsnAPIfProfileThresholdConfigEntry.setStatus("current")


class _BsnAPIfProfileParamAssignment_Type(Integer32):
    """Custom type bsnAPIfProfileParamAssignment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("customized", 2))
    )


_BsnAPIfProfileParamAssignment_Type.__name__ = "Integer32"
_BsnAPIfProfileParamAssignment_Object = MibTableColumn
bsnAPIfProfileParamAssignment = _BsnAPIfProfileParamAssignment_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 12, 1, 1),
    _BsnAPIfProfileParamAssignment_Type()
)
bsnAPIfProfileParamAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPIfProfileParamAssignment.setStatus("current")


class _BsnAPIfForeignInterferenceThreshold_Type(Integer32):
    """Custom type bsnAPIfForeignInterferenceThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BsnAPIfForeignInterferenceThreshold_Type.__name__ = "Integer32"
_BsnAPIfForeignInterferenceThreshold_Object = MibTableColumn
bsnAPIfForeignInterferenceThreshold = _BsnAPIfForeignInterferenceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 12, 1, 2),
    _BsnAPIfForeignInterferenceThreshold_Type()
)
bsnAPIfForeignInterferenceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPIfForeignInterferenceThreshold.setStatus("current")


class _BsnAPIfForeignNoiseThreshold_Type(Integer32):
    """Custom type bsnAPIfForeignNoiseThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 0),
    )


_BsnAPIfForeignNoiseThreshold_Type.__name__ = "Integer32"
_BsnAPIfForeignNoiseThreshold_Object = MibTableColumn
bsnAPIfForeignNoiseThreshold = _BsnAPIfForeignNoiseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 12, 1, 3),
    _BsnAPIfForeignNoiseThreshold_Type()
)
bsnAPIfForeignNoiseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPIfForeignNoiseThreshold.setStatus("current")


class _BsnAPIfRFUtilizationThreshold_Type(Integer32):
    """Custom type bsnAPIfRFUtilizationThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BsnAPIfRFUtilizationThreshold_Type.__name__ = "Integer32"
_BsnAPIfRFUtilizationThreshold_Object = MibTableColumn
bsnAPIfRFUtilizationThreshold = _BsnAPIfRFUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 12, 1, 4),
    _BsnAPIfRFUtilizationThreshold_Type()
)
bsnAPIfRFUtilizationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPIfRFUtilizationThreshold.setStatus("current")


class _BsnAPIfThroughputThreshold_Type(Unsigned32):
    """Custom type bsnAPIfThroughputThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 1000000),
    )


_BsnAPIfThroughputThreshold_Type.__name__ = "Unsigned32"
_BsnAPIfThroughputThreshold_Object = MibTableColumn
bsnAPIfThroughputThreshold = _BsnAPIfThroughputThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 12, 1, 5),
    _BsnAPIfThroughputThreshold_Type()
)
bsnAPIfThroughputThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPIfThroughputThreshold.setStatus("current")


class _BsnAPIfMobilesThreshold_Type(Integer32):
    """Custom type bsnAPIfMobilesThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 75),
    )


_BsnAPIfMobilesThreshold_Type.__name__ = "Integer32"
_BsnAPIfMobilesThreshold_Object = MibTableColumn
bsnAPIfMobilesThreshold = _BsnAPIfMobilesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 12, 1, 6),
    _BsnAPIfMobilesThreshold_Type()
)
bsnAPIfMobilesThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPIfMobilesThreshold.setStatus("current")


class _BsnAPIfCoverageThreshold_Type(Integer32):
    """Custom type bsnAPIfCoverageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 50),
    )


_BsnAPIfCoverageThreshold_Type.__name__ = "Integer32"
_BsnAPIfCoverageThreshold_Object = MibTableColumn
bsnAPIfCoverageThreshold = _BsnAPIfCoverageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 12, 1, 7),
    _BsnAPIfCoverageThreshold_Type()
)
bsnAPIfCoverageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPIfCoverageThreshold.setStatus("current")


class _BsnAPIfMobileMinExceptionLevel_Type(Integer32):
    """Custom type bsnAPIfMobileMinExceptionLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 75),
    )


_BsnAPIfMobileMinExceptionLevel_Type.__name__ = "Integer32"
_BsnAPIfMobileMinExceptionLevel_Object = MibTableColumn
bsnAPIfMobileMinExceptionLevel = _BsnAPIfMobileMinExceptionLevel_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 12, 1, 8),
    _BsnAPIfMobileMinExceptionLevel_Type()
)
bsnAPIfMobileMinExceptionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPIfMobileMinExceptionLevel.setStatus("current")


class _BsnAPIfCoverageExceptionLevel_Type(Integer32):
    """Custom type bsnAPIfCoverageExceptionLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BsnAPIfCoverageExceptionLevel_Type.__name__ = "Integer32"
_BsnAPIfCoverageExceptionLevel_Object = MibTableColumn
bsnAPIfCoverageExceptionLevel = _BsnAPIfCoverageExceptionLevel_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 12, 1, 28),
    _BsnAPIfCoverageExceptionLevel_Type()
)
bsnAPIfCoverageExceptionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPIfCoverageExceptionLevel.setStatus("current")
_BsnAPIfLoadParametersTable_Object = MibTable
bsnAPIfLoadParametersTable = _BsnAPIfLoadParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 13)
)
if mibBuilder.loadTexts:
    bsnAPIfLoadParametersTable.setStatus("current")
_BsnAPIfLoadParametersEntry_Object = MibTableRow
bsnAPIfLoadParametersEntry = _BsnAPIfLoadParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 13, 1)
)
bsnAPIfLoadParametersEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
)
if mibBuilder.loadTexts:
    bsnAPIfLoadParametersEntry.setStatus("current")


class _BsnAPIfLoadRxUtilization_Type(Integer32):
    """Custom type bsnAPIfLoadRxUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BsnAPIfLoadRxUtilization_Type.__name__ = "Integer32"
_BsnAPIfLoadRxUtilization_Object = MibTableColumn
bsnAPIfLoadRxUtilization = _BsnAPIfLoadRxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 13, 1, 1),
    _BsnAPIfLoadRxUtilization_Type()
)
bsnAPIfLoadRxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfLoadRxUtilization.setStatus("current")


class _BsnAPIfLoadTxUtilization_Type(Integer32):
    """Custom type bsnAPIfLoadTxUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BsnAPIfLoadTxUtilization_Type.__name__ = "Integer32"
_BsnAPIfLoadTxUtilization_Object = MibTableColumn
bsnAPIfLoadTxUtilization = _BsnAPIfLoadTxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 13, 1, 2),
    _BsnAPIfLoadTxUtilization_Type()
)
bsnAPIfLoadTxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfLoadTxUtilization.setStatus("current")


class _BsnAPIfLoadChannelUtilization_Type(Integer32):
    """Custom type bsnAPIfLoadChannelUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BsnAPIfLoadChannelUtilization_Type.__name__ = "Integer32"
_BsnAPIfLoadChannelUtilization_Object = MibTableColumn
bsnAPIfLoadChannelUtilization = _BsnAPIfLoadChannelUtilization_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 13, 1, 3),
    _BsnAPIfLoadChannelUtilization_Type()
)
bsnAPIfLoadChannelUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfLoadChannelUtilization.setStatus("current")
_BsnAPIfLoadNumOfClients_Type = Integer32
_BsnAPIfLoadNumOfClients_Object = MibTableColumn
bsnAPIfLoadNumOfClients = _BsnAPIfLoadNumOfClients_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 13, 1, 4),
    _BsnAPIfLoadNumOfClients_Type()
)
bsnAPIfLoadNumOfClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfLoadNumOfClients.setStatus("current")
_BsnAPIfPoorSNRClients_Type = Integer32
_BsnAPIfPoorSNRClients_Object = MibTableColumn
bsnAPIfPoorSNRClients = _BsnAPIfPoorSNRClients_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 13, 1, 24),
    _BsnAPIfPoorSNRClients_Type()
)
bsnAPIfPoorSNRClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfPoorSNRClients.setStatus("current")
_BsnAPIfChannelInterferenceInfoTable_Object = MibTable
bsnAPIfChannelInterferenceInfoTable = _BsnAPIfChannelInterferenceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 14)
)
if mibBuilder.loadTexts:
    bsnAPIfChannelInterferenceInfoTable.setStatus("current")
_BsnAPIfChannelInterferenceInfoEntry_Object = MibTableRow
bsnAPIfChannelInterferenceInfoEntry = _BsnAPIfChannelInterferenceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 14, 1)
)
bsnAPIfChannelInterferenceInfoEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPIfInterferenceChannelNo"),
)
if mibBuilder.loadTexts:
    bsnAPIfChannelInterferenceInfoEntry.setStatus("current")
_BsnAPIfInterferenceChannelNo_Type = Integer32
_BsnAPIfInterferenceChannelNo_Object = MibTableColumn
bsnAPIfInterferenceChannelNo = _BsnAPIfInterferenceChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 14, 1, 1),
    _BsnAPIfInterferenceChannelNo_Type()
)
bsnAPIfInterferenceChannelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfInterferenceChannelNo.setStatus("current")
_BsnAPIfInterferencePower_Type = Integer32
_BsnAPIfInterferencePower_Object = MibTableColumn
bsnAPIfInterferencePower = _BsnAPIfInterferencePower_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 14, 1, 2),
    _BsnAPIfInterferencePower_Type()
)
bsnAPIfInterferencePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfInterferencePower.setStatus("current")


class _BsnAPIfInterferenceUtilization_Type(Integer32):
    """Custom type bsnAPIfInterferenceUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BsnAPIfInterferenceUtilization_Type.__name__ = "Integer32"
_BsnAPIfInterferenceUtilization_Object = MibTableColumn
bsnAPIfInterferenceUtilization = _BsnAPIfInterferenceUtilization_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 14, 1, 22),
    _BsnAPIfInterferenceUtilization_Type()
)
bsnAPIfInterferenceUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfInterferenceUtilization.setStatus("current")
_BsnAPIfChannelNoiseInfoTable_Object = MibTable
bsnAPIfChannelNoiseInfoTable = _BsnAPIfChannelNoiseInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 15)
)
if mibBuilder.loadTexts:
    bsnAPIfChannelNoiseInfoTable.setStatus("current")
_BsnAPIfChannelNoiseInfoEntry_Object = MibTableRow
bsnAPIfChannelNoiseInfoEntry = _BsnAPIfChannelNoiseInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 15, 1)
)
bsnAPIfChannelNoiseInfoEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPIfNoiseChannelNo"),
)
if mibBuilder.loadTexts:
    bsnAPIfChannelNoiseInfoEntry.setStatus("current")
_BsnAPIfNoiseChannelNo_Type = Integer32
_BsnAPIfNoiseChannelNo_Object = MibTableColumn
bsnAPIfNoiseChannelNo = _BsnAPIfNoiseChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 15, 1, 1),
    _BsnAPIfNoiseChannelNo_Type()
)
bsnAPIfNoiseChannelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfNoiseChannelNo.setStatus("current")
_BsnAPIfDBNoisePower_Type = Integer32
_BsnAPIfDBNoisePower_Object = MibTableColumn
bsnAPIfDBNoisePower = _BsnAPIfDBNoisePower_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 15, 1, 21),
    _BsnAPIfDBNoisePower_Type()
)
bsnAPIfDBNoisePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfDBNoisePower.setStatus("current")
_BsnAPIfProfileStateTable_Object = MibTable
bsnAPIfProfileStateTable = _BsnAPIfProfileStateTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 16)
)
if mibBuilder.loadTexts:
    bsnAPIfProfileStateTable.setStatus("current")
_BsnAPIfProfileStateEntry_Object = MibTableRow
bsnAPIfProfileStateEntry = _BsnAPIfProfileStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 16, 1)
)
bsnAPIfProfileStateEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
)
if mibBuilder.loadTexts:
    bsnAPIfProfileStateEntry.setStatus("current")
_BsnAPIfLoadProfileState_Type = ProfileState
_BsnAPIfLoadProfileState_Object = MibTableColumn
bsnAPIfLoadProfileState = _BsnAPIfLoadProfileState_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 16, 1, 1),
    _BsnAPIfLoadProfileState_Type()
)
bsnAPIfLoadProfileState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfLoadProfileState.setStatus("current")
_BsnAPIfInterferenceProfileState_Type = ProfileState
_BsnAPIfInterferenceProfileState_Object = MibTableColumn
bsnAPIfInterferenceProfileState = _BsnAPIfInterferenceProfileState_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 16, 1, 2),
    _BsnAPIfInterferenceProfileState_Type()
)
bsnAPIfInterferenceProfileState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfInterferenceProfileState.setStatus("current")
_BsnAPIfNoiseProfileState_Type = ProfileState
_BsnAPIfNoiseProfileState_Object = MibTableColumn
bsnAPIfNoiseProfileState = _BsnAPIfNoiseProfileState_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 16, 1, 3),
    _BsnAPIfNoiseProfileState_Type()
)
bsnAPIfNoiseProfileState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfNoiseProfileState.setStatus("current")
_BsnAPIfCoverageProfileState_Type = ProfileState
_BsnAPIfCoverageProfileState_Object = MibTableColumn
bsnAPIfCoverageProfileState = _BsnAPIfCoverageProfileState_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 16, 1, 24),
    _BsnAPIfCoverageProfileState_Type()
)
bsnAPIfCoverageProfileState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfCoverageProfileState.setStatus("current")
_BsnAPIfRxNeighborsTable_Object = MibTable
bsnAPIfRxNeighborsTable = _BsnAPIfRxNeighborsTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 17)
)
if mibBuilder.loadTexts:
    bsnAPIfRxNeighborsTable.setStatus("current")
_BsnAPIfRxNeighborsEntry_Object = MibTableRow
bsnAPIfRxNeighborsEntry = _BsnAPIfRxNeighborsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 17, 1)
)
bsnAPIfRxNeighborsEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPIfRxNeighborMacAddress"),
)
if mibBuilder.loadTexts:
    bsnAPIfRxNeighborsEntry.setStatus("current")
_BsnAPIfRxNeighborMacAddress_Type = MacAddress
_BsnAPIfRxNeighborMacAddress_Object = MibTableColumn
bsnAPIfRxNeighborMacAddress = _BsnAPIfRxNeighborMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 17, 1, 1),
    _BsnAPIfRxNeighborMacAddress_Type()
)
bsnAPIfRxNeighborMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfRxNeighborMacAddress.setStatus("current")
_BsnAPIfRxNeighborIpAddress_Type = IpAddress
_BsnAPIfRxNeighborIpAddress_Object = MibTableColumn
bsnAPIfRxNeighborIpAddress = _BsnAPIfRxNeighborIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 17, 1, 2),
    _BsnAPIfRxNeighborIpAddress_Type()
)
bsnAPIfRxNeighborIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfRxNeighborIpAddress.setStatus("current")
_BsnAPIfRxNeighborRSSI_Type = Integer32
_BsnAPIfRxNeighborRSSI_Object = MibTableColumn
bsnAPIfRxNeighborRSSI = _BsnAPIfRxNeighborRSSI_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 17, 1, 3),
    _BsnAPIfRxNeighborRSSI_Type()
)
bsnAPIfRxNeighborRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfRxNeighborRSSI.setStatus("current")
_BsnAPIfRxNeighborSlot_Type = Integer32
_BsnAPIfRxNeighborSlot_Object = MibTableColumn
bsnAPIfRxNeighborSlot = _BsnAPIfRxNeighborSlot_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 17, 1, 24),
    _BsnAPIfRxNeighborSlot_Type()
)
bsnAPIfRxNeighborSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfRxNeighborSlot.setStatus("current")
_BsnAPIfRxNeighborChannel_Type = Integer32
_BsnAPIfRxNeighborChannel_Object = MibTableColumn
bsnAPIfRxNeighborChannel = _BsnAPIfRxNeighborChannel_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 17, 1, 26),
    _BsnAPIfRxNeighborChannel_Type()
)
bsnAPIfRxNeighborChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfRxNeighborChannel.setStatus("current")


class _BsnAPIfRxNeighborChannelWidth_Type(Integer32):
    """Custom type bsnAPIfRxNeighborChannelWidth based on Integer32"""
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
        *(("aboveforty", 4),
          ("belowforty", 5),
          ("five", 1),
          ("ten", 2),
          ("twenty", 3))
    )


_BsnAPIfRxNeighborChannelWidth_Type.__name__ = "Integer32"
_BsnAPIfRxNeighborChannelWidth_Object = MibTableColumn
bsnAPIfRxNeighborChannelWidth = _BsnAPIfRxNeighborChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 17, 1, 27),
    _BsnAPIfRxNeighborChannelWidth_Type()
)
bsnAPIfRxNeighborChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfRxNeighborChannelWidth.setStatus("current")
_BsnAPIfStationRSSICoverageInfoTable_Object = MibTable
bsnAPIfStationRSSICoverageInfoTable = _BsnAPIfStationRSSICoverageInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 18)
)
if mibBuilder.loadTexts:
    bsnAPIfStationRSSICoverageInfoTable.setStatus("current")
_BsnAPIfStationRSSICoverageInfoEntry_Object = MibTableRow
bsnAPIfStationRSSICoverageInfoEntry = _BsnAPIfStationRSSICoverageInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 18, 1)
)
bsnAPIfStationRSSICoverageInfoEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPIfStationRSSICoverageIndex"),
)
if mibBuilder.loadTexts:
    bsnAPIfStationRSSICoverageInfoEntry.setStatus("current")
_BsnAPIfStationRSSICoverageIndex_Type = Integer32
_BsnAPIfStationRSSICoverageIndex_Object = MibTableColumn
bsnAPIfStationRSSICoverageIndex = _BsnAPIfStationRSSICoverageIndex_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 18, 1, 1),
    _BsnAPIfStationRSSICoverageIndex_Type()
)
bsnAPIfStationRSSICoverageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfStationRSSICoverageIndex.setStatus("current")
_BsnAPIfRSSILevel_Type = Integer32
_BsnAPIfRSSILevel_Object = MibTableColumn
bsnAPIfRSSILevel = _BsnAPIfRSSILevel_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 18, 1, 2),
    _BsnAPIfRSSILevel_Type()
)
bsnAPIfRSSILevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfRSSILevel.setStatus("current")
_BsnAPIfStationCountOnRSSI_Type = Integer32
_BsnAPIfStationCountOnRSSI_Object = MibTableColumn
bsnAPIfStationCountOnRSSI = _BsnAPIfStationCountOnRSSI_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 18, 1, 23),
    _BsnAPIfStationCountOnRSSI_Type()
)
bsnAPIfStationCountOnRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfStationCountOnRSSI.setStatus("current")
_BsnAPIfStationSNRCoverageInfoTable_Object = MibTable
bsnAPIfStationSNRCoverageInfoTable = _BsnAPIfStationSNRCoverageInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 19)
)
if mibBuilder.loadTexts:
    bsnAPIfStationSNRCoverageInfoTable.setStatus("current")
_BsnAPIfStationSNRCoverageInfoEntry_Object = MibTableRow
bsnAPIfStationSNRCoverageInfoEntry = _BsnAPIfStationSNRCoverageInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 19, 1)
)
bsnAPIfStationSNRCoverageInfoEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPIfStationSNRCoverageIndex"),
)
if mibBuilder.loadTexts:
    bsnAPIfStationSNRCoverageInfoEntry.setStatus("current")
_BsnAPIfStationSNRCoverageIndex_Type = Integer32
_BsnAPIfStationSNRCoverageIndex_Object = MibTableColumn
bsnAPIfStationSNRCoverageIndex = _BsnAPIfStationSNRCoverageIndex_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 19, 1, 1),
    _BsnAPIfStationSNRCoverageIndex_Type()
)
bsnAPIfStationSNRCoverageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfStationSNRCoverageIndex.setStatus("current")
_BsnAPIfSNRLevel_Type = Integer32
_BsnAPIfSNRLevel_Object = MibTableColumn
bsnAPIfSNRLevel = _BsnAPIfSNRLevel_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 19, 1, 2),
    _BsnAPIfSNRLevel_Type()
)
bsnAPIfSNRLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfSNRLevel.setStatus("current")
_BsnAPIfStationCountOnSNR_Type = Integer32
_BsnAPIfStationCountOnSNR_Object = MibTableColumn
bsnAPIfStationCountOnSNR = _BsnAPIfStationCountOnSNR_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 19, 1, 23),
    _BsnAPIfStationCountOnSNR_Type()
)
bsnAPIfStationCountOnSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfStationCountOnSNR.setStatus("current")
_BsnAPIfRecommendedRFParametersTable_Object = MibTable
bsnAPIfRecommendedRFParametersTable = _BsnAPIfRecommendedRFParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 20)
)
if mibBuilder.loadTexts:
    bsnAPIfRecommendedRFParametersTable.setStatus("current")
_BsnAPIfRecommendedRFParametersEntry_Object = MibTableRow
bsnAPIfRecommendedRFParametersEntry = _BsnAPIfRecommendedRFParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 20, 1)
)
bsnAPIfRecommendedRFParametersEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
)
if mibBuilder.loadTexts:
    bsnAPIfRecommendedRFParametersEntry.setStatus("current")
_BsnAPIfRecommendedChannelNumber_Type = Integer32
_BsnAPIfRecommendedChannelNumber_Object = MibTableColumn
bsnAPIfRecommendedChannelNumber = _BsnAPIfRecommendedChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 20, 1, 1),
    _BsnAPIfRecommendedChannelNumber_Type()
)
bsnAPIfRecommendedChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfRecommendedChannelNumber.setStatus("current")
_BsnAPIfRecommendedTxPowerLevel_Type = Integer32
_BsnAPIfRecommendedTxPowerLevel_Object = MibTableColumn
bsnAPIfRecommendedTxPowerLevel = _BsnAPIfRecommendedTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 20, 1, 2),
    _BsnAPIfRecommendedTxPowerLevel_Type()
)
bsnAPIfRecommendedTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfRecommendedTxPowerLevel.setStatus("current")
_BsnAPIfRecommendedRTSThreshold_Type = Integer32
_BsnAPIfRecommendedRTSThreshold_Object = MibTableColumn
bsnAPIfRecommendedRTSThreshold = _BsnAPIfRecommendedRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 20, 1, 3),
    _BsnAPIfRecommendedRTSThreshold_Type()
)
bsnAPIfRecommendedRTSThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfRecommendedRTSThreshold.setStatus("current")
_BsnAPIfRecommendedFragmentationThreshold_Type = Integer32
_BsnAPIfRecommendedFragmentationThreshold_Object = MibTableColumn
bsnAPIfRecommendedFragmentationThreshold = _BsnAPIfRecommendedFragmentationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 20, 1, 24),
    _BsnAPIfRecommendedFragmentationThreshold_Type()
)
bsnAPIfRecommendedFragmentationThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfRecommendedFragmentationThreshold.setStatus("current")
_BsnAPIfWlanOverrideTable_Object = MibTable
bsnAPIfWlanOverrideTable = _BsnAPIfWlanOverrideTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 21)
)
if mibBuilder.loadTexts:
    bsnAPIfWlanOverrideTable.setStatus("current")
_BsnAPIfWlanOverrideEntry_Object = MibTableRow
bsnAPIfWlanOverrideEntry = _BsnAPIfWlanOverrideEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 21, 1)
)
bsnAPIfWlanOverrideEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPIfWlanOverrideId"),
)
if mibBuilder.loadTexts:
    bsnAPIfWlanOverrideEntry.setStatus("current")


class _BsnAPIfWlanOverrideId_Type(Unsigned32):
    """Custom type bsnAPIfWlanOverrideId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BsnAPIfWlanOverrideId_Type.__name__ = "Unsigned32"
_BsnAPIfWlanOverrideId_Object = MibTableColumn
bsnAPIfWlanOverrideId = _BsnAPIfWlanOverrideId_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 21, 1, 1),
    _BsnAPIfWlanOverrideId_Type()
)
bsnAPIfWlanOverrideId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAPIfWlanOverrideId.setStatus("current")


class _BsnAPIfWlanOverrideSsid_Type(DisplayString):
    """Custom type bsnAPIfWlanOverrideSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BsnAPIfWlanOverrideSsid_Type.__name__ = "DisplayString"
_BsnAPIfWlanOverrideSsid_Object = MibTableColumn
bsnAPIfWlanOverrideSsid = _BsnAPIfWlanOverrideSsid_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 21, 1, 2),
    _BsnAPIfWlanOverrideSsid_Type()
)
bsnAPIfWlanOverrideSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfWlanOverrideSsid.setStatus("current")
_BsnAPIfWlanOverrideRowStatus_Type = RowStatus
_BsnAPIfWlanOverrideRowStatus_Object = MibTableColumn
bsnAPIfWlanOverrideRowStatus = _BsnAPIfWlanOverrideRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 21, 1, 15),
    _BsnAPIfWlanOverrideRowStatus_Type()
)
bsnAPIfWlanOverrideRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAPIfWlanOverrideRowStatus.setStatus("current")
_BsnMeshNodeTable_Object = MibTable
bsnMeshNodeTable = _BsnMeshNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 22)
)
if mibBuilder.loadTexts:
    bsnMeshNodeTable.setStatus("current")
_BsnMeshNodeEntry_Object = MibTableRow
bsnMeshNodeEntry = _BsnMeshNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 22, 1)
)
bsnMeshNodeEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
)
if mibBuilder.loadTexts:
    bsnMeshNodeEntry.setStatus("current")


class _BsnMeshNodeRole_Type(Integer32):
    """Custom type bsnMeshNodeRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pap", 0),
          ("rap", 1))
    )


_BsnMeshNodeRole_Type.__name__ = "Integer32"
_BsnMeshNodeRole_Object = MibTableColumn
bsnMeshNodeRole = _BsnMeshNodeRole_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 22, 1, 1),
    _BsnMeshNodeRole_Type()
)
bsnMeshNodeRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNodeRole.setStatus("current")


class _BsnMeshNodeGroup_Type(OctetString):
    """Custom type bsnMeshNodeGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_BsnMeshNodeGroup_Type.__name__ = "OctetString"
_BsnMeshNodeGroup_Object = MibTableColumn
bsnMeshNodeGroup = _BsnMeshNodeGroup_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 22, 1, 2),
    _BsnMeshNodeGroup_Type()
)
bsnMeshNodeGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNodeGroup.setStatus("current")


class _BsnMeshNodeBackhaul_Type(Integer32):
    """Custom type bsnMeshNodeBackhaul based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 0),
          ("dot11b", 1),
          ("dot11g", 2))
    )


_BsnMeshNodeBackhaul_Type.__name__ = "Integer32"
_BsnMeshNodeBackhaul_Object = MibTableColumn
bsnMeshNodeBackhaul = _BsnMeshNodeBackhaul_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 22, 1, 3),
    _BsnMeshNodeBackhaul_Type()
)
bsnMeshNodeBackhaul.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNodeBackhaul.setStatus("current")


class _BsnMeshNodeBackhaulPAP_Type(Integer32):
    """Custom type bsnMeshNodeBackhaulPAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("dot11a", 1),
          ("dot11b", 2),
          ("dot11g", 3))
    )


_BsnMeshNodeBackhaulPAP_Type.__name__ = "Integer32"
_BsnMeshNodeBackhaulPAP_Object = MibTableColumn
bsnMeshNodeBackhaulPAP = _BsnMeshNodeBackhaulPAP_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 22, 1, 4),
    _BsnMeshNodeBackhaulPAP_Type()
)
bsnMeshNodeBackhaulPAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNodeBackhaulPAP.setStatus("current")


class _BsnMeshNodeBackhaulRAP_Type(Integer32):
    """Custom type bsnMeshNodeBackhaulRAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 0),
          ("dot11b", 1),
          ("dot11g", 2))
    )


_BsnMeshNodeBackhaulRAP_Type.__name__ = "Integer32"
_BsnMeshNodeBackhaulRAP_Object = MibTableColumn
bsnMeshNodeBackhaulRAP = _BsnMeshNodeBackhaulRAP_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 22, 1, 5),
    _BsnMeshNodeBackhaulRAP_Type()
)
bsnMeshNodeBackhaulRAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnMeshNodeBackhaulRAP.setStatus("current")
_BsnMeshNodeDataRate_Type = Integer32
_BsnMeshNodeDataRate_Object = MibTableColumn
bsnMeshNodeDataRate = _BsnMeshNodeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 22, 1, 6),
    _BsnMeshNodeDataRate_Type()
)
bsnMeshNodeDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnMeshNodeDataRate.setStatus("current")
_BsnMeshNodeChannel_Type = Integer32
_BsnMeshNodeChannel_Object = MibTableColumn
bsnMeshNodeChannel = _BsnMeshNodeChannel_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 22, 1, 7),
    _BsnMeshNodeChannel_Type()
)
bsnMeshNodeChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNodeChannel.setStatus("current")


class _BsnMeshNodeRoutingState_Type(Integer32):
    """Custom type bsnMeshNodeRoutingState based on Integer32"""
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
        *(("auth", 4),
          ("maint", 5),
          ("seek", 2),
          ("start", 1),
          ("sync", 3))
    )


_BsnMeshNodeRoutingState_Type.__name__ = "Integer32"
_BsnMeshNodeRoutingState_Object = MibTableColumn
bsnMeshNodeRoutingState = _BsnMeshNodeRoutingState_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 22, 1, 8),
    _BsnMeshNodeRoutingState_Type()
)
bsnMeshNodeRoutingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNodeRoutingState.setStatus("current")
_BsnMeshNodeMalformedNeighPackets_Type = Counter32
_BsnMeshNodeMalformedNeighPackets_Object = MibTableColumn
bsnMeshNodeMalformedNeighPackets = _BsnMeshNodeMalformedNeighPackets_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 22, 1, 9),
    _BsnMeshNodeMalformedNeighPackets_Type()
)
bsnMeshNodeMalformedNeighPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNodeMalformedNeighPackets.setStatus("current")
_BsnMeshNodePoorNeighSnr_Type = Counter32
_BsnMeshNodePoorNeighSnr_Object = MibTableColumn
bsnMeshNodePoorNeighSnr = _BsnMeshNodePoorNeighSnr_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 22, 1, 10),
    _BsnMeshNodePoorNeighSnr_Type()
)
bsnMeshNodePoorNeighSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNodePoorNeighSnr.setStatus("current")
_BsnMeshNodeBlacklistPackets_Type = Counter32
_BsnMeshNodeBlacklistPackets_Object = MibTableColumn
bsnMeshNodeBlacklistPackets = _BsnMeshNodeBlacklistPackets_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 22, 1, 11),
    _BsnMeshNodeBlacklistPackets_Type()
)
bsnMeshNodeBlacklistPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNodeBlacklistPackets.setStatus("current")
_BsnMeshNodeInsufficientMemory_Type = Counter32
_BsnMeshNodeInsufficientMemory_Object = MibTableColumn
bsnMeshNodeInsufficientMemory = _BsnMeshNodeInsufficientMemory_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 22, 1, 12),
    _BsnMeshNodeInsufficientMemory_Type()
)
bsnMeshNodeInsufficientMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNodeInsufficientMemory.setStatus("current")
_BsnMeshNodeRxNeighReq_Type = Counter32
_BsnMeshNodeRxNeighReq_Object = MibTableColumn
bsnMeshNodeRxNeighReq = _BsnMeshNodeRxNeighReq_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 22, 1, 13),
    _BsnMeshNodeRxNeighReq_Type()
)
bsnMeshNodeRxNeighReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNodeRxNeighReq.setStatus("current")
_BsnMeshNodeRxNeighRsp_Type = Counter32
_BsnMeshNodeRxNeighRsp_Object = MibTableColumn
bsnMeshNodeRxNeighRsp = _BsnMeshNodeRxNeighRsp_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 22, 1, 14),
    _BsnMeshNodeRxNeighRsp_Type()
)
bsnMeshNodeRxNeighRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNodeRxNeighRsp.setStatus("current")
_BsnMeshNodeTxNeighReq_Type = Counter32
_BsnMeshNodeTxNeighReq_Object = MibTableColumn
bsnMeshNodeTxNeighReq = _BsnMeshNodeTxNeighReq_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 22, 1, 15),
    _BsnMeshNodeTxNeighReq_Type()
)
bsnMeshNodeTxNeighReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNodeTxNeighReq.setStatus("current")
_BsnMeshNodeTxNeighRsp_Type = Counter32
_BsnMeshNodeTxNeighRsp_Object = MibTableColumn
bsnMeshNodeTxNeighRsp = _BsnMeshNodeTxNeighRsp_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 22, 1, 16),
    _BsnMeshNodeTxNeighRsp_Type()
)
bsnMeshNodeTxNeighRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNodeTxNeighRsp.setStatus("current")
_BsnMeshNodeParentChanges_Type = Counter32
_BsnMeshNodeParentChanges_Object = MibTableColumn
bsnMeshNodeParentChanges = _BsnMeshNodeParentChanges_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 22, 1, 17),
    _BsnMeshNodeParentChanges_Type()
)
bsnMeshNodeParentChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNodeParentChanges.setStatus("current")
_BsnMeshNodeNeighTimeout_Type = Counter32
_BsnMeshNodeNeighTimeout_Object = MibTableColumn
bsnMeshNodeNeighTimeout = _BsnMeshNodeNeighTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 22, 1, 18),
    _BsnMeshNodeNeighTimeout_Type()
)
bsnMeshNodeNeighTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNodeNeighTimeout.setStatus("current")
_BsnMeshNodeParentMacAddress_Type = MacAddress
_BsnMeshNodeParentMacAddress_Object = MibTableColumn
bsnMeshNodeParentMacAddress = _BsnMeshNodeParentMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 22, 1, 19),
    _BsnMeshNodeParentMacAddress_Type()
)
bsnMeshNodeParentMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNodeParentMacAddress.setStatus("current")


class _BsnMeshNodeAPType_Type(Integer32):
    """Custom type bsnMeshNodeAPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("indoorBridge", 5),
          ("outdoorBridge", 6))
    )


_BsnMeshNodeAPType_Type.__name__ = "Integer32"
_BsnMeshNodeAPType_Object = MibTableColumn
bsnMeshNodeAPType = _BsnMeshNodeAPType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 22, 1, 20),
    _BsnMeshNodeAPType_Type()
)
bsnMeshNodeAPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNodeAPType.setStatus("current")


class _BsnMeshNodeEthernetBridge_Type(Integer32):
    """Custom type bsnMeshNodeEthernetBridge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnMeshNodeEthernetBridge_Type.__name__ = "Integer32"
_BsnMeshNodeEthernetBridge_Object = MibTableColumn
bsnMeshNodeEthernetBridge = _BsnMeshNodeEthernetBridge_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 22, 1, 21),
    _BsnMeshNodeEthernetBridge_Type()
)
bsnMeshNodeEthernetBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnMeshNodeEthernetBridge.setStatus("current")
_BsnMeshNodeHops_Type = Integer32
_BsnMeshNodeHops_Object = MibTableColumn
bsnMeshNodeHops = _BsnMeshNodeHops_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 22, 1, 30),
    _BsnMeshNodeHops_Type()
)
bsnMeshNodeHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNodeHops.setStatus("current")
_BsnMeshNeighsTable_Object = MibTable
bsnMeshNeighsTable = _BsnMeshNeighsTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 23)
)
if mibBuilder.loadTexts:
    bsnMeshNeighsTable.setStatus("current")
_BsnMeshNeighsEntry_Object = MibTableRow
bsnMeshNeighsEntry = _BsnMeshNeighsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 23, 1)
)
bsnMeshNeighsEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnMeshNeighMacAddress"),
)
if mibBuilder.loadTexts:
    bsnMeshNeighsEntry.setStatus("current")
_BsnMeshNeighMacAddress_Type = MacAddress
_BsnMeshNeighMacAddress_Object = MibTableColumn
bsnMeshNeighMacAddress = _BsnMeshNeighMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 23, 1, 1),
    _BsnMeshNeighMacAddress_Type()
)
bsnMeshNeighMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNeighMacAddress.setStatus("current")


class _BsnMeshNeighType_Type(Integer32):
    """Custom type bsnMeshNeighType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("blacklisted", 3),
          ("child", 4),
          ("neigh", 2),
          ("parent", 0),
          ("tentparent", 1))
    )


_BsnMeshNeighType_Type.__name__ = "Integer32"
_BsnMeshNeighType_Object = MibTableColumn
bsnMeshNeighType = _BsnMeshNeighType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 23, 1, 2),
    _BsnMeshNeighType_Type()
)
bsnMeshNeighType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNeighType.setStatus("current")


class _BsnMeshNeighState_Type(Integer32):
    """Custom type bsnMeshNeighState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("needupdate", 1),
          ("updated", 0))
    )


_BsnMeshNeighState_Type.__name__ = "Integer32"
_BsnMeshNeighState_Object = MibTableColumn
bsnMeshNeighState = _BsnMeshNeighState_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 23, 1, 3),
    _BsnMeshNeighState_Type()
)
bsnMeshNeighState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNeighState.setStatus("current")
_BsnMeshNeighSnr_Type = Integer32
_BsnMeshNeighSnr_Object = MibTableColumn
bsnMeshNeighSnr = _BsnMeshNeighSnr_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 23, 1, 4),
    _BsnMeshNeighSnr_Type()
)
bsnMeshNeighSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNeighSnr.setStatus("current")
_BsnMeshNeighSnrUp_Type = Integer32
_BsnMeshNeighSnrUp_Object = MibTableColumn
bsnMeshNeighSnrUp = _BsnMeshNeighSnrUp_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 23, 1, 5),
    _BsnMeshNeighSnrUp_Type()
)
bsnMeshNeighSnrUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNeighSnrUp.setStatus("current")
_BsnMeshNeighSnrDown_Type = Integer32
_BsnMeshNeighSnrDown_Object = MibTableColumn
bsnMeshNeighSnrDown = _BsnMeshNeighSnrDown_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 23, 1, 6),
    _BsnMeshNeighSnrDown_Type()
)
bsnMeshNeighSnrDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNeighSnrDown.setStatus("current")
_BsnMeshNeighLinkSnr_Type = Integer32
_BsnMeshNeighLinkSnr_Object = MibTableColumn
bsnMeshNeighLinkSnr = _BsnMeshNeighLinkSnr_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 23, 1, 7),
    _BsnMeshNeighLinkSnr_Type()
)
bsnMeshNeighLinkSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNeighLinkSnr.setStatus("current")
_BsnMeshNeighAdjustedEase_Type = Integer32
_BsnMeshNeighAdjustedEase_Object = MibTableColumn
bsnMeshNeighAdjustedEase = _BsnMeshNeighAdjustedEase_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 23, 1, 8),
    _BsnMeshNeighAdjustedEase_Type()
)
bsnMeshNeighAdjustedEase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNeighAdjustedEase.setStatus("current")
_BsnMeshNeighUnadjustedEase_Type = Integer32
_BsnMeshNeighUnadjustedEase_Object = MibTableColumn
bsnMeshNeighUnadjustedEase = _BsnMeshNeighUnadjustedEase_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 23, 1, 9),
    _BsnMeshNeighUnadjustedEase_Type()
)
bsnMeshNeighUnadjustedEase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNeighUnadjustedEase.setStatus("current")
_BsnMeshNeighRapEase_Type = Integer32
_BsnMeshNeighRapEase_Object = MibTableColumn
bsnMeshNeighRapEase = _BsnMeshNeighRapEase_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 23, 1, 10),
    _BsnMeshNeighRapEase_Type()
)
bsnMeshNeighRapEase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNeighRapEase.setStatus("current")
_BsnMeshNeighTxParent_Type = Counter32
_BsnMeshNeighTxParent_Object = MibTableColumn
bsnMeshNeighTxParent = _BsnMeshNeighTxParent_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 23, 1, 11),
    _BsnMeshNeighTxParent_Type()
)
bsnMeshNeighTxParent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNeighTxParent.setStatus("current")
_BsnMeshNeighRxParent_Type = Counter32
_BsnMeshNeighRxParent_Object = MibTableColumn
bsnMeshNeighRxParent = _BsnMeshNeighRxParent_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 23, 1, 12),
    _BsnMeshNeighRxParent_Type()
)
bsnMeshNeighRxParent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNeighRxParent.setStatus("current")
_BsnMeshNeighPoorSnr_Type = Counter32
_BsnMeshNeighPoorSnr_Object = MibTableColumn
bsnMeshNeighPoorSnr = _BsnMeshNeighPoorSnr_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 23, 1, 13),
    _BsnMeshNeighPoorSnr_Type()
)
bsnMeshNeighPoorSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNeighPoorSnr.setStatus("current")
_BsnMeshNeighLastUpdate_Type = Integer32
_BsnMeshNeighLastUpdate_Object = MibTableColumn
bsnMeshNeighLastUpdate = _BsnMeshNeighLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 23, 1, 14),
    _BsnMeshNeighLastUpdate_Type()
)
bsnMeshNeighLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNeighLastUpdate.setStatus("current")
_BsnMeshNeighParentChange_Type = Integer32
_BsnMeshNeighParentChange_Object = MibTableColumn
bsnMeshNeighParentChange = _BsnMeshNeighParentChange_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 23, 1, 20),
    _BsnMeshNeighParentChange_Type()
)
bsnMeshNeighParentChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMeshNeighParentChange.setStatus("current")
_BsnAPIfRadarChannelStatisticsTable_Object = MibTable
bsnAPIfRadarChannelStatisticsTable = _BsnAPIfRadarChannelStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 24)
)
if mibBuilder.loadTexts:
    bsnAPIfRadarChannelStatisticsTable.setStatus("current")
_BsnAPIfRadarChannelStatisticsEntry_Object = MibTableRow
bsnAPIfRadarChannelStatisticsEntry = _BsnAPIfRadarChannelStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 24, 1)
)
bsnAPIfRadarChannelStatisticsEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPIfRadarDetectedChannelNumber"),
)
if mibBuilder.loadTexts:
    bsnAPIfRadarChannelStatisticsEntry.setStatus("current")
_BsnAPIfRadarDetectedChannelNumber_Type = Integer32
_BsnAPIfRadarDetectedChannelNumber_Object = MibTableColumn
bsnAPIfRadarDetectedChannelNumber = _BsnAPIfRadarDetectedChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 24, 1, 1),
    _BsnAPIfRadarDetectedChannelNumber_Type()
)
bsnAPIfRadarDetectedChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfRadarDetectedChannelNumber.setStatus("current")
_BsnAPIfRadarSignalLastHeard_Type = Integer32
_BsnAPIfRadarSignalLastHeard_Object = MibTableColumn
bsnAPIfRadarSignalLastHeard = _BsnAPIfRadarSignalLastHeard_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 2, 24, 1, 2),
    _BsnAPIfRadarSignalLastHeard_Type()
)
bsnAPIfRadarSignalLastHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAPIfRadarSignalLastHeard.setStatus("current")
if mibBuilder.loadTexts:
    bsnAPIfRadarSignalLastHeard.setUnits("seconds")
_BsnGlobalDot11_ObjectIdentity = ObjectIdentity
bsnGlobalDot11 = _BsnGlobalDot11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3)
)
_BsnGlobalDot11Config_ObjectIdentity = ObjectIdentity
bsnGlobalDot11Config = _BsnGlobalDot11Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1)
)


class _BsnGlobalDot11PrivacyOptionImplemented_Type(Integer32):
    """Custom type bsnGlobalDot11PrivacyOptionImplemented based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("implemented", 1),
          ("notimplemented", 0))
    )


_BsnGlobalDot11PrivacyOptionImplemented_Type.__name__ = "Integer32"
_BsnGlobalDot11PrivacyOptionImplemented_Object = MibScalar
bsnGlobalDot11PrivacyOptionImplemented = _BsnGlobalDot11PrivacyOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 1),
    _BsnGlobalDot11PrivacyOptionImplemented_Type()
)
bsnGlobalDot11PrivacyOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11PrivacyOptionImplemented.setStatus("current")


class _BsnGlobalDot11AuthenticationResponseTimeOut_Type(Unsigned32):
    """Custom type bsnGlobalDot11AuthenticationResponseTimeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_BsnGlobalDot11AuthenticationResponseTimeOut_Type.__name__ = "Unsigned32"
_BsnGlobalDot11AuthenticationResponseTimeOut_Object = MibScalar
bsnGlobalDot11AuthenticationResponseTimeOut = _BsnGlobalDot11AuthenticationResponseTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 2),
    _BsnGlobalDot11AuthenticationResponseTimeOut_Type()
)
bsnGlobalDot11AuthenticationResponseTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11AuthenticationResponseTimeOut.setStatus("current")


class _BsnGlobalDot11MultiDomainCapabilityImplemented_Type(Integer32):
    """Custom type bsnGlobalDot11MultiDomainCapabilityImplemented based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_BsnGlobalDot11MultiDomainCapabilityImplemented_Type.__name__ = "Integer32"
_BsnGlobalDot11MultiDomainCapabilityImplemented_Object = MibScalar
bsnGlobalDot11MultiDomainCapabilityImplemented = _BsnGlobalDot11MultiDomainCapabilityImplemented_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 3),
    _BsnGlobalDot11MultiDomainCapabilityImplemented_Type()
)
bsnGlobalDot11MultiDomainCapabilityImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11MultiDomainCapabilityImplemented.setStatus("current")


class _BsnGlobalDot11MultiDomainCapabilityEnabled_Type(Integer32):
    """Custom type bsnGlobalDot11MultiDomainCapabilityEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_BsnGlobalDot11MultiDomainCapabilityEnabled_Type.__name__ = "Integer32"
_BsnGlobalDot11MultiDomainCapabilityEnabled_Object = MibScalar
bsnGlobalDot11MultiDomainCapabilityEnabled = _BsnGlobalDot11MultiDomainCapabilityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 4),
    _BsnGlobalDot11MultiDomainCapabilityEnabled_Type()
)
bsnGlobalDot11MultiDomainCapabilityEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11MultiDomainCapabilityEnabled.setStatus("current")


class _BsnGlobalDot11CountryIndex_Type(Integer32):
    """Custom type bsnGlobalDot11CountryIndex based on Integer32"""
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
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68)
        )
    )
    namedValues = NamedValues(
        *(("argentina", 48),
          ("australia", 9),
          ("austria", 10),
          ("belgium", 11),
          ("brazil", 49),
          ("canada", 2),
          ("chile", 63),
          ("china", 54),
          ("colombia", 64),
          ("cyprus", 33),
          ("czechrepublic", 34),
          ("denmark", 12),
          ("estonia", 35),
          ("finland", 13),
          ("france", 3),
          ("germany", 14),
          ("gibraltar", 57),
          ("greece", 15),
          ("hongkong", 25),
          ("hungary", 36),
          ("iceland", 27),
          ("india", 24),
          ("indonesia", 53),
          ("ireland", 16),
          ("israel", 46),
          ("israelOutdoor", 47),
          ("italy", 17),
          ("japan", 4),
          ("japan2", 56),
          ("koreaExtended", 55),
          ("korearepublic", 8),
          ("latvia", 38),
          ("liechtenstein", 58),
          ("lithuania", 37),
          ("luxembourg", 18),
          ("malaysia", 39),
          ("malta", 59),
          ("mexico", 5),
          ("monaco", 60),
          ("netherlands", 19),
          ("newzealand", 40),
          ("none", 23),
          ("norway", 28),
          ("panama", 65),
          ("peru", 66),
          ("philippines", 68),
          ("poland", 41),
          ("portugal", 20),
          ("romania", 61),
          ("russianfederation", 62),
          ("saudiArabia", 51),
          ("singapore", 29),
          ("slovakrepublic", 43),
          ("slovenia", 42),
          ("southafrica", 44),
          ("spain", 6),
          ("sweden", 21),
          ("switzerland", 26),
          ("taiwan", 31),
          ("thailand", 30),
          ("turkey", 52),
          ("unitedkingdom", 22),
          ("usa", 1),
          ("usachan165", 45),
          ("usalegacy", 7),
          ("venezuela", 67))
    )


_BsnGlobalDot11CountryIndex_Type.__name__ = "Integer32"
_BsnGlobalDot11CountryIndex_Object = MibScalar
bsnGlobalDot11CountryIndex = _BsnGlobalDot11CountryIndex_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 5),
    _BsnGlobalDot11CountryIndex_Type()
)
bsnGlobalDot11CountryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11CountryIndex.setStatus("deprecated")


class _BsnGlobalDot11LoadBalancing_Type(Integer32):
    """Custom type bsnGlobalDot11LoadBalancing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnGlobalDot11LoadBalancing_Type.__name__ = "Integer32"
_BsnGlobalDot11LoadBalancing_Object = MibScalar
bsnGlobalDot11LoadBalancing = _BsnGlobalDot11LoadBalancing_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 6),
    _BsnGlobalDot11LoadBalancing_Type()
)
bsnGlobalDot11LoadBalancing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11LoadBalancing.setStatus("deprecated")


class _BsnGlobalDot11RogueTimer_Type(Integer32):
    """Custom type bsnGlobalDot11RogueTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 3600),
    )


_BsnGlobalDot11RogueTimer_Type.__name__ = "Integer32"
_BsnGlobalDot11RogueTimer_Object = MibScalar
bsnGlobalDot11RogueTimer = _BsnGlobalDot11RogueTimer_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 7),
    _BsnGlobalDot11RogueTimer_Type()
)
bsnGlobalDot11RogueTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11RogueTimer.setStatus("current")


class _BsnPrimaryMwarForAPs_Type(Integer32):
    """Custom type bsnPrimaryMwarForAPs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnPrimaryMwarForAPs_Type.__name__ = "Integer32"
_BsnPrimaryMwarForAPs_Object = MibScalar
bsnPrimaryMwarForAPs = _BsnPrimaryMwarForAPs_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 8),
    _BsnPrimaryMwarForAPs_Type()
)
bsnPrimaryMwarForAPs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnPrimaryMwarForAPs.setStatus("current")


class _BsnRtpProtocolPriority_Type(Integer32):
    """Custom type bsnRtpProtocolPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("highpriority", 1),
          ("nopriority", 0))
    )


_BsnRtpProtocolPriority_Type.__name__ = "Integer32"
_BsnRtpProtocolPriority_Object = MibScalar
bsnRtpProtocolPriority = _BsnRtpProtocolPriority_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 9),
    _BsnRtpProtocolPriority_Type()
)
bsnRtpProtocolPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRtpProtocolPriority.setStatus("current")
_BsnSystemCurrentTime_Type = DisplayString
_BsnSystemCurrentTime_Object = MibScalar
bsnSystemCurrentTime = _BsnSystemCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 10),
    _BsnSystemCurrentTime_Type()
)
bsnSystemCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnSystemCurrentTime.setStatus("current")


class _BsnUpdateSystemTime_Type(DisplayString):
    """Custom type bsnUpdateSystemTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BsnUpdateSystemTime_Type.__name__ = "DisplayString"
_BsnUpdateSystemTime_Object = MibScalar
bsnUpdateSystemTime = _BsnUpdateSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 11),
    _BsnUpdateSystemTime_Type()
)
bsnUpdateSystemTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnUpdateSystemTime.setStatus("current")


class _BsnOperatingTemperatureEnvironment_Type(Integer32):
    """Custom type bsnOperatingTemperatureEnvironment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("commercial", 1),
          ("industrial", 2),
          ("unknown", 0))
    )


_BsnOperatingTemperatureEnvironment_Type.__name__ = "Integer32"
_BsnOperatingTemperatureEnvironment_Object = MibScalar
bsnOperatingTemperatureEnvironment = _BsnOperatingTemperatureEnvironment_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 12),
    _BsnOperatingTemperatureEnvironment_Type()
)
bsnOperatingTemperatureEnvironment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnOperatingTemperatureEnvironment.setStatus("current")
_BsnSensorTemperature_Type = Integer32
_BsnSensorTemperature_Object = MibScalar
bsnSensorTemperature = _BsnSensorTemperature_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 13),
    _BsnSensorTemperature_Type()
)
bsnSensorTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnSensorTemperature.setStatus("current")
_BsnTemperatureAlarmLowLimit_Type = Integer32
_BsnTemperatureAlarmLowLimit_Object = MibScalar
bsnTemperatureAlarmLowLimit = _BsnTemperatureAlarmLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 14),
    _BsnTemperatureAlarmLowLimit_Type()
)
bsnTemperatureAlarmLowLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTemperatureAlarmLowLimit.setStatus("current")
_BsnTemperatureAlarmHighLimit_Type = Integer32
_BsnTemperatureAlarmHighLimit_Object = MibScalar
bsnTemperatureAlarmHighLimit = _BsnTemperatureAlarmHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 15),
    _BsnTemperatureAlarmHighLimit_Type()
)
bsnTemperatureAlarmHighLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTemperatureAlarmHighLimit.setStatus("current")
_BsnVirtualGatewayAddress_Type = IpAddress
_BsnVirtualGatewayAddress_Object = MibScalar
bsnVirtualGatewayAddress = _BsnVirtualGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 16),
    _BsnVirtualGatewayAddress_Type()
)
bsnVirtualGatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnVirtualGatewayAddress.setStatus("current")


class _BsnRFMobilityDomainName_Type(OctetString):
    """Custom type bsnRFMobilityDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BsnRFMobilityDomainName_Type.__name__ = "OctetString"
_BsnRFMobilityDomainName_Object = MibScalar
bsnRFMobilityDomainName = _BsnRFMobilityDomainName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 17),
    _BsnRFMobilityDomainName_Type()
)
bsnRFMobilityDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRFMobilityDomainName.setStatus("current")


class _BsnClientWatchListFeature_Type(Integer32):
    """Custom type bsnClientWatchListFeature based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnClientWatchListFeature_Type.__name__ = "Integer32"
_BsnClientWatchListFeature_Object = MibScalar
bsnClientWatchListFeature = _BsnClientWatchListFeature_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 18),
    _BsnClientWatchListFeature_Type()
)
bsnClientWatchListFeature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnClientWatchListFeature.setStatus("current")


class _BsnRogueLocationDiscoveryProtocol_Type(Integer32):
    """Custom type bsnRogueLocationDiscoveryProtocol based on Integer32"""
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
        *(("allAPs", 1),
          ("disable", 0),
          ("monitorAPOnly", 2))
    )


_BsnRogueLocationDiscoveryProtocol_Type.__name__ = "Integer32"
_BsnRogueLocationDiscoveryProtocol_Object = MibScalar
bsnRogueLocationDiscoveryProtocol = _BsnRogueLocationDiscoveryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 19),
    _BsnRogueLocationDiscoveryProtocol_Type()
)
bsnRogueLocationDiscoveryProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRogueLocationDiscoveryProtocol.setStatus("current")


class _BsnRogueAutoContainFeature_Type(Integer32):
    """Custom type bsnRogueAutoContainFeature based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnRogueAutoContainFeature_Type.__name__ = "Integer32"
_BsnRogueAutoContainFeature_Object = MibScalar
bsnRogueAutoContainFeature = _BsnRogueAutoContainFeature_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 20),
    _BsnRogueAutoContainFeature_Type()
)
bsnRogueAutoContainFeature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRogueAutoContainFeature.setStatus("current")


class _BsnOverAirProvisionApMode_Type(Integer32):
    """Custom type bsnOverAirProvisionApMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnOverAirProvisionApMode_Type.__name__ = "Integer32"
_BsnOverAirProvisionApMode_Object = MibScalar
bsnOverAirProvisionApMode = _BsnOverAirProvisionApMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 21),
    _BsnOverAirProvisionApMode_Type()
)
bsnOverAirProvisionApMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnOverAirProvisionApMode.setStatus("current")


class _BsnMaximumNumberOfConcurrentLogins_Type(Integer32):
    """Custom type bsnMaximumNumberOfConcurrentLogins based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_BsnMaximumNumberOfConcurrentLogins_Type.__name__ = "Integer32"
_BsnMaximumNumberOfConcurrentLogins_Object = MibScalar
bsnMaximumNumberOfConcurrentLogins = _BsnMaximumNumberOfConcurrentLogins_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 22),
    _BsnMaximumNumberOfConcurrentLogins_Type()
)
bsnMaximumNumberOfConcurrentLogins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnMaximumNumberOfConcurrentLogins.setStatus("current")


class _BsnAutoContainRoguesAdvertisingSsid_Type(Integer32):
    """Custom type bsnAutoContainRoguesAdvertisingSsid based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarmOnly", 0),
          ("contain", 1))
    )


_BsnAutoContainRoguesAdvertisingSsid_Type.__name__ = "Integer32"
_BsnAutoContainRoguesAdvertisingSsid_Object = MibScalar
bsnAutoContainRoguesAdvertisingSsid = _BsnAutoContainRoguesAdvertisingSsid_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 23),
    _BsnAutoContainRoguesAdvertisingSsid_Type()
)
bsnAutoContainRoguesAdvertisingSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAutoContainRoguesAdvertisingSsid.setStatus("current")


class _BsnAutoContainAdhocNetworks_Type(Integer32):
    """Custom type bsnAutoContainAdhocNetworks based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarmOnly", 0),
          ("contain", 1))
    )


_BsnAutoContainAdhocNetworks_Type.__name__ = "Integer32"
_BsnAutoContainAdhocNetworks_Object = MibScalar
bsnAutoContainAdhocNetworks = _BsnAutoContainAdhocNetworks_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 24),
    _BsnAutoContainAdhocNetworks_Type()
)
bsnAutoContainAdhocNetworks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAutoContainAdhocNetworks.setStatus("current")


class _BsnAutoContainTrustedClientsOnRogueAps_Type(Integer32):
    """Custom type bsnAutoContainTrustedClientsOnRogueAps based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarmOnly", 0),
          ("contain", 1))
    )


_BsnAutoContainTrustedClientsOnRogueAps_Type.__name__ = "Integer32"
_BsnAutoContainTrustedClientsOnRogueAps_Object = MibScalar
bsnAutoContainTrustedClientsOnRogueAps = _BsnAutoContainTrustedClientsOnRogueAps_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 25),
    _BsnAutoContainTrustedClientsOnRogueAps_Type()
)
bsnAutoContainTrustedClientsOnRogueAps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAutoContainTrustedClientsOnRogueAps.setStatus("current")


class _BsnValidateRogueClientsAgainstAAA_Type(Integer32):
    """Custom type bsnValidateRogueClientsAgainstAAA based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnValidateRogueClientsAgainstAAA_Type.__name__ = "Integer32"
_BsnValidateRogueClientsAgainstAAA_Object = MibScalar
bsnValidateRogueClientsAgainstAAA = _BsnValidateRogueClientsAgainstAAA_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 26),
    _BsnValidateRogueClientsAgainstAAA_Type()
)
bsnValidateRogueClientsAgainstAAA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnValidateRogueClientsAgainstAAA.setStatus("current")
_BsnSystemTimezoneDelta_Type = Integer32
_BsnSystemTimezoneDelta_Object = MibScalar
bsnSystemTimezoneDelta = _BsnSystemTimezoneDelta_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 27),
    _BsnSystemTimezoneDelta_Type()
)
bsnSystemTimezoneDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnSystemTimezoneDelta.setStatus("current")


class _BsnSystemTimezoneDaylightSavings_Type(Integer32):
    """Custom type bsnSystemTimezoneDaylightSavings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnSystemTimezoneDaylightSavings_Type.__name__ = "Integer32"
_BsnSystemTimezoneDaylightSavings_Object = MibScalar
bsnSystemTimezoneDaylightSavings = _BsnSystemTimezoneDaylightSavings_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 28),
    _BsnSystemTimezoneDaylightSavings_Type()
)
bsnSystemTimezoneDaylightSavings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnSystemTimezoneDaylightSavings.setStatus("obsolete")


class _BsnAllowAuthorizeApAgainstAAA_Type(Integer32):
    """Custom type bsnAllowAuthorizeApAgainstAAA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnAllowAuthorizeApAgainstAAA_Type.__name__ = "Integer32"
_BsnAllowAuthorizeApAgainstAAA_Object = MibScalar
bsnAllowAuthorizeApAgainstAAA = _BsnAllowAuthorizeApAgainstAAA_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 29),
    _BsnAllowAuthorizeApAgainstAAA_Type()
)
bsnAllowAuthorizeApAgainstAAA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAllowAuthorizeApAgainstAAA.setStatus("current")
_BsnSystemTimezoneDeltaMinutes_Type = Integer32
_BsnSystemTimezoneDeltaMinutes_Object = MibScalar
bsnSystemTimezoneDeltaMinutes = _BsnSystemTimezoneDeltaMinutes_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 30),
    _BsnSystemTimezoneDeltaMinutes_Type()
)
bsnSystemTimezoneDeltaMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnSystemTimezoneDeltaMinutes.setStatus("current")


class _BsnApFallbackEnabled_Type(Integer32):
    """Custom type bsnApFallbackEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnApFallbackEnabled_Type.__name__ = "Integer32"
_BsnApFallbackEnabled_Object = MibScalar
bsnApFallbackEnabled = _BsnApFallbackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 31),
    _BsnApFallbackEnabled_Type()
)
bsnApFallbackEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnApFallbackEnabled.setStatus("current")


class _BsnAppleTalkEnabled_Type(Integer32):
    """Custom type bsnAppleTalkEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnAppleTalkEnabled_Type.__name__ = "Integer32"
_BsnAppleTalkEnabled_Object = MibScalar
bsnAppleTalkEnabled = _BsnAppleTalkEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 32),
    _BsnAppleTalkEnabled_Type()
)
bsnAppleTalkEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAppleTalkEnabled.setStatus("current")
_BsnTrustedApPolicyConfig_ObjectIdentity = ObjectIdentity
bsnTrustedApPolicyConfig = _BsnTrustedApPolicyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 40)
)


class _BsnPolicyForMisconfiguredAps_Type(Integer32):
    """Custom type bsnPolicyForMisconfiguredAps based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarmOnly", 0),
          ("contain", 1))
    )


_BsnPolicyForMisconfiguredAps_Type.__name__ = "Integer32"
_BsnPolicyForMisconfiguredAps_Object = MibScalar
bsnPolicyForMisconfiguredAps = _BsnPolicyForMisconfiguredAps_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 40, 1),
    _BsnPolicyForMisconfiguredAps_Type()
)
bsnPolicyForMisconfiguredAps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnPolicyForMisconfiguredAps.setStatus("current")


class _BsnEncryptionPolicyEnforced_Type(Integer32):
    """Custom type bsnEncryptionPolicyEnforced based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("open", 1),
          ("wep", 2),
          ("wpa", 3))
    )


_BsnEncryptionPolicyEnforced_Type.__name__ = "Integer32"
_BsnEncryptionPolicyEnforced_Object = MibScalar
bsnEncryptionPolicyEnforced = _BsnEncryptionPolicyEnforced_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 40, 2),
    _BsnEncryptionPolicyEnforced_Type()
)
bsnEncryptionPolicyEnforced.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnEncryptionPolicyEnforced.setStatus("current")


class _BsnPreamblePolicyEnforced_Type(Integer32):
    """Custom type bsnPreamblePolicyEnforced based on Integer32"""
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
        *(("long", 2),
          ("none", 0),
          ("short", 1))
    )


_BsnPreamblePolicyEnforced_Type.__name__ = "Integer32"
_BsnPreamblePolicyEnforced_Object = MibScalar
bsnPreamblePolicyEnforced = _BsnPreamblePolicyEnforced_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 40, 3),
    _BsnPreamblePolicyEnforced_Type()
)
bsnPreamblePolicyEnforced.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnPreamblePolicyEnforced.setStatus("current")


class _BsnDot11ModePolicyEnforced_Type(Integer32):
    """Custom type bsnDot11ModePolicyEnforced based on Integer32"""
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
        *(("dcfOnly", 1),
          ("none", 0),
          ("pcfOnly", 2))
    )


_BsnDot11ModePolicyEnforced_Type.__name__ = "Integer32"
_BsnDot11ModePolicyEnforced_Object = MibScalar
bsnDot11ModePolicyEnforced = _BsnDot11ModePolicyEnforced_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 40, 4),
    _BsnDot11ModePolicyEnforced_Type()
)
bsnDot11ModePolicyEnforced.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnDot11ModePolicyEnforced.setStatus("current")


class _BsnRadioTypePolicyEnforced_Type(Integer32):
    """Custom type bsnRadioTypePolicyEnforced based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aOnly", 1),
          ("bOnly", 2),
          ("bgOnly", 3),
          ("none", 0))
    )


_BsnRadioTypePolicyEnforced_Type.__name__ = "Integer32"
_BsnRadioTypePolicyEnforced_Object = MibScalar
bsnRadioTypePolicyEnforced = _BsnRadioTypePolicyEnforced_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 40, 5),
    _BsnRadioTypePolicyEnforced_Type()
)
bsnRadioTypePolicyEnforced.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRadioTypePolicyEnforced.setStatus("current")


class _BsnValidateSsidForTrustedAp_Type(Integer32):
    """Custom type bsnValidateSsidForTrustedAp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnValidateSsidForTrustedAp_Type.__name__ = "Integer32"
_BsnValidateSsidForTrustedAp_Object = MibScalar
bsnValidateSsidForTrustedAp = _BsnValidateSsidForTrustedAp_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 40, 6),
    _BsnValidateSsidForTrustedAp_Type()
)
bsnValidateSsidForTrustedAp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnValidateSsidForTrustedAp.setStatus("current")


class _BsnAlertIfTrustedApMissing_Type(Integer32):
    """Custom type bsnAlertIfTrustedApMissing based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnAlertIfTrustedApMissing_Type.__name__ = "Integer32"
_BsnAlertIfTrustedApMissing_Object = MibScalar
bsnAlertIfTrustedApMissing = _BsnAlertIfTrustedApMissing_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 40, 7),
    _BsnAlertIfTrustedApMissing_Type()
)
bsnAlertIfTrustedApMissing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAlertIfTrustedApMissing.setStatus("current")


class _BsnTrustedApEntryExpirationTimeout_Type(Integer32):
    """Custom type bsnTrustedApEntryExpirationTimeout based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 3600),
    )


_BsnTrustedApEntryExpirationTimeout_Type.__name__ = "Integer32"
_BsnTrustedApEntryExpirationTimeout_Object = MibScalar
bsnTrustedApEntryExpirationTimeout = _BsnTrustedApEntryExpirationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 40, 8),
    _BsnTrustedApEntryExpirationTimeout_Type()
)
bsnTrustedApEntryExpirationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnTrustedApEntryExpirationTimeout.setStatus("current")
_BsnClientExclusionPolicyConfig_ObjectIdentity = ObjectIdentity
bsnClientExclusionPolicyConfig = _BsnClientExclusionPolicyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 41)
)


class _BsnExcessive80211AssocFailures_Type(Integer32):
    """Custom type bsnExcessive80211AssocFailures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnExcessive80211AssocFailures_Type.__name__ = "Integer32"
_BsnExcessive80211AssocFailures_Object = MibScalar
bsnExcessive80211AssocFailures = _BsnExcessive80211AssocFailures_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 41, 1),
    _BsnExcessive80211AssocFailures_Type()
)
bsnExcessive80211AssocFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnExcessive80211AssocFailures.setStatus("current")


class _BsnExcessive80211AuthFailures_Type(Integer32):
    """Custom type bsnExcessive80211AuthFailures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnExcessive80211AuthFailures_Type.__name__ = "Integer32"
_BsnExcessive80211AuthFailures_Object = MibScalar
bsnExcessive80211AuthFailures = _BsnExcessive80211AuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 41, 2),
    _BsnExcessive80211AuthFailures_Type()
)
bsnExcessive80211AuthFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnExcessive80211AuthFailures.setStatus("current")


class _BsnExcessive8021xAuthFailures_Type(Integer32):
    """Custom type bsnExcessive8021xAuthFailures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnExcessive8021xAuthFailures_Type.__name__ = "Integer32"
_BsnExcessive8021xAuthFailures_Object = MibScalar
bsnExcessive8021xAuthFailures = _BsnExcessive8021xAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 41, 3),
    _BsnExcessive8021xAuthFailures_Type()
)
bsnExcessive8021xAuthFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnExcessive8021xAuthFailures.setStatus("current")


class _BsnExternalPolicyServerFailures_Type(Integer32):
    """Custom type bsnExternalPolicyServerFailures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnExternalPolicyServerFailures_Type.__name__ = "Integer32"
_BsnExternalPolicyServerFailures_Object = MibScalar
bsnExternalPolicyServerFailures = _BsnExternalPolicyServerFailures_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 41, 4),
    _BsnExternalPolicyServerFailures_Type()
)
bsnExternalPolicyServerFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnExternalPolicyServerFailures.setStatus("current")


class _BsnExcessiveWebAuthFailures_Type(Integer32):
    """Custom type bsnExcessiveWebAuthFailures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnExcessiveWebAuthFailures_Type.__name__ = "Integer32"
_BsnExcessiveWebAuthFailures_Object = MibScalar
bsnExcessiveWebAuthFailures = _BsnExcessiveWebAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 41, 5),
    _BsnExcessiveWebAuthFailures_Type()
)
bsnExcessiveWebAuthFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnExcessiveWebAuthFailures.setStatus("current")


class _BsnIPTheftORReuse_Type(Integer32):
    """Custom type bsnIPTheftORReuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnIPTheftORReuse_Type.__name__ = "Integer32"
_BsnIPTheftORReuse_Object = MibScalar
bsnIPTheftORReuse = _BsnIPTheftORReuse_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 41, 6),
    _BsnIPTheftORReuse_Type()
)
bsnIPTheftORReuse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnIPTheftORReuse.setStatus("current")
_BsnSignatureConfig_ObjectIdentity = ObjectIdentity
bsnSignatureConfig = _BsnSignatureConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42)
)
_BsnStandardSignatureTable_Object = MibTable
bsnStandardSignatureTable = _BsnStandardSignatureTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 1)
)
if mibBuilder.loadTexts:
    bsnStandardSignatureTable.setStatus("current")
_BsnStandardSignatureEntry_Object = MibTableRow
bsnStandardSignatureEntry = _BsnStandardSignatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 1, 1)
)
bsnStandardSignatureEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnStandardSignaturePrecedence"),
)
if mibBuilder.loadTexts:
    bsnStandardSignatureEntry.setStatus("current")


class _BsnStandardSignaturePrecedence_Type(Unsigned32):
    """Custom type bsnStandardSignaturePrecedence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_BsnStandardSignaturePrecedence_Type.__name__ = "Unsigned32"
_BsnStandardSignaturePrecedence_Object = MibTableColumn
bsnStandardSignaturePrecedence = _BsnStandardSignaturePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 1, 1, 1),
    _BsnStandardSignaturePrecedence_Type()
)
bsnStandardSignaturePrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnStandardSignaturePrecedence.setStatus("current")


class _BsnStandardSignatureName_Type(DisplayString):
    """Custom type bsnStandardSignatureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BsnStandardSignatureName_Type.__name__ = "DisplayString"
_BsnStandardSignatureName_Object = MibTableColumn
bsnStandardSignatureName = _BsnStandardSignatureName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 1, 1, 2),
    _BsnStandardSignatureName_Type()
)
bsnStandardSignatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnStandardSignatureName.setStatus("current")


class _BsnStandardSignatureDescription_Type(DisplayString):
    """Custom type bsnStandardSignatureDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_BsnStandardSignatureDescription_Type.__name__ = "DisplayString"
_BsnStandardSignatureDescription_Object = MibTableColumn
bsnStandardSignatureDescription = _BsnStandardSignatureDescription_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 1, 1, 3),
    _BsnStandardSignatureDescription_Type()
)
bsnStandardSignatureDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnStandardSignatureDescription.setStatus("current")


class _BsnStandardSignatureFrameType_Type(Integer32):
    """Custom type bsnStandardSignatureFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("management", 0))
    )


_BsnStandardSignatureFrameType_Type.__name__ = "Integer32"
_BsnStandardSignatureFrameType_Object = MibTableColumn
bsnStandardSignatureFrameType = _BsnStandardSignatureFrameType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 1, 1, 4),
    _BsnStandardSignatureFrameType_Type()
)
bsnStandardSignatureFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnStandardSignatureFrameType.setStatus("current")


class _BsnStandardSignatureAction_Type(Integer32):
    """Custom type bsnStandardSignatureAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("contain", 2),
          ("exclude", 3),
          ("none", 0),
          ("report", 1))
    )


_BsnStandardSignatureAction_Type.__name__ = "Integer32"
_BsnStandardSignatureAction_Object = MibTableColumn
bsnStandardSignatureAction = _BsnStandardSignatureAction_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 1, 1, 5),
    _BsnStandardSignatureAction_Type()
)
bsnStandardSignatureAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnStandardSignatureAction.setStatus("current")


class _BsnStandardSignatureState_Type(Integer32):
    """Custom type bsnStandardSignatureState based on Integer32"""
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


_BsnStandardSignatureState_Type.__name__ = "Integer32"
_BsnStandardSignatureState_Object = MibTableColumn
bsnStandardSignatureState = _BsnStandardSignatureState_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 1, 1, 6),
    _BsnStandardSignatureState_Type()
)
bsnStandardSignatureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnStandardSignatureState.setStatus("current")


class _BsnStandardSignatureFrequency_Type(Unsigned32):
    """Custom type bsnStandardSignatureFrequency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BsnStandardSignatureFrequency_Type.__name__ = "Unsigned32"
_BsnStandardSignatureFrequency_Object = MibTableColumn
bsnStandardSignatureFrequency = _BsnStandardSignatureFrequency_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 1, 1, 7),
    _BsnStandardSignatureFrequency_Type()
)
bsnStandardSignatureFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnStandardSignatureFrequency.setStatus("current")


class _BsnStandardSignatureQuietTime_Type(Unsigned32):
    """Custom type bsnStandardSignatureQuietTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BsnStandardSignatureQuietTime_Type.__name__ = "Unsigned32"
_BsnStandardSignatureQuietTime_Object = MibTableColumn
bsnStandardSignatureQuietTime = _BsnStandardSignatureQuietTime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 1, 1, 8),
    _BsnStandardSignatureQuietTime_Type()
)
bsnStandardSignatureQuietTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnStandardSignatureQuietTime.setStatus("current")


class _BsnStandardSignatureVersion_Type(Unsigned32):
    """Custom type bsnStandardSignatureVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_BsnStandardSignatureVersion_Type.__name__ = "Unsigned32"
_BsnStandardSignatureVersion_Object = MibTableColumn
bsnStandardSignatureVersion = _BsnStandardSignatureVersion_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 1, 1, 9),
    _BsnStandardSignatureVersion_Type()
)
bsnStandardSignatureVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnStandardSignatureVersion.setStatus("current")


class _BsnStandardSignatureConfigType_Type(Integer32):
    """Custom type bsnStandardSignatureConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pattern", 0),
          ("protocol", 1))
    )


_BsnStandardSignatureConfigType_Type.__name__ = "Integer32"
_BsnStandardSignatureConfigType_Object = MibTableColumn
bsnStandardSignatureConfigType = _BsnStandardSignatureConfigType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 1, 1, 10),
    _BsnStandardSignatureConfigType_Type()
)
bsnStandardSignatureConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnStandardSignatureConfigType.setStatus("current")


class _BsnStandardSignatureEnable_Type(TruthValue):
    """Custom type bsnStandardSignatureEnable based on TruthValue"""


_BsnStandardSignatureEnable_Object = MibTableColumn
bsnStandardSignatureEnable = _BsnStandardSignatureEnable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 1, 1, 11),
    _BsnStandardSignatureEnable_Type()
)
bsnStandardSignatureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnStandardSignatureEnable.setStatus("current")
_BsnStandardSignatureMacInfo_Type = BsnTxtSignatureMacInfo
_BsnStandardSignatureMacInfo_Object = MibTableColumn
bsnStandardSignatureMacInfo = _BsnStandardSignatureMacInfo_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 1, 1, 12),
    _BsnStandardSignatureMacInfo_Type()
)
bsnStandardSignatureMacInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnStandardSignatureMacInfo.setStatus("current")


class _BsnStandardSignatureMacFreq_Type(Unsigned32):
    """Custom type bsnStandardSignatureMacFreq based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BsnStandardSignatureMacFreq_Type.__name__ = "Unsigned32"
_BsnStandardSignatureMacFreq_Object = MibTableColumn
bsnStandardSignatureMacFreq = _BsnStandardSignatureMacFreq_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 1, 1, 13),
    _BsnStandardSignatureMacFreq_Type()
)
bsnStandardSignatureMacFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnStandardSignatureMacFreq.setStatus("current")
_BsnStandardSignatureRowStatus_Type = RowStatus
_BsnStandardSignatureRowStatus_Object = MibTableColumn
bsnStandardSignatureRowStatus = _BsnStandardSignatureRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 1, 1, 20),
    _BsnStandardSignatureRowStatus_Type()
)
bsnStandardSignatureRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnStandardSignatureRowStatus.setStatus("current")


class _BsnStandardSignatureInterval_Type(Unsigned32):
    """Custom type bsnStandardSignatureInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_BsnStandardSignatureInterval_Type.__name__ = "Unsigned32"
_BsnStandardSignatureInterval_Object = MibTableColumn
bsnStandardSignatureInterval = _BsnStandardSignatureInterval_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 1, 1, 21),
    _BsnStandardSignatureInterval_Type()
)
bsnStandardSignatureInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnStandardSignatureInterval.setStatus("current")
_BsnStandardSignaturePatternTable_Object = MibTable
bsnStandardSignaturePatternTable = _BsnStandardSignaturePatternTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 2)
)
if mibBuilder.loadTexts:
    bsnStandardSignaturePatternTable.setStatus("current")
_BsnStandardSignaturePatternEntry_Object = MibTableRow
bsnStandardSignaturePatternEntry = _BsnStandardSignaturePatternEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 2, 1)
)
bsnStandardSignaturePatternEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnStandardSignaturePrecedence"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnStandardSignaturePatternIndex"),
)
if mibBuilder.loadTexts:
    bsnStandardSignaturePatternEntry.setStatus("current")


class _BsnStandardSignaturePatternIndex_Type(Unsigned32):
    """Custom type bsnStandardSignaturePatternIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_BsnStandardSignaturePatternIndex_Type.__name__ = "Unsigned32"
_BsnStandardSignaturePatternIndex_Object = MibTableColumn
bsnStandardSignaturePatternIndex = _BsnStandardSignaturePatternIndex_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 2, 1, 1),
    _BsnStandardSignaturePatternIndex_Type()
)
bsnStandardSignaturePatternIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnStandardSignaturePatternIndex.setStatus("current")


class _BsnStandardSignaturePatternOffset_Type(Unsigned32):
    """Custom type bsnStandardSignaturePatternOffset based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_BsnStandardSignaturePatternOffset_Type.__name__ = "Unsigned32"
_BsnStandardSignaturePatternOffset_Object = MibTableColumn
bsnStandardSignaturePatternOffset = _BsnStandardSignaturePatternOffset_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 2, 1, 2),
    _BsnStandardSignaturePatternOffset_Type()
)
bsnStandardSignaturePatternOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnStandardSignaturePatternOffset.setStatus("current")


class _BsnStandardSignaturePatternString_Type(DisplayString):
    """Custom type bsnStandardSignaturePatternString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_BsnStandardSignaturePatternString_Type.__name__ = "DisplayString"
_BsnStandardSignaturePatternString_Object = MibTableColumn
bsnStandardSignaturePatternString = _BsnStandardSignaturePatternString_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 2, 1, 3),
    _BsnStandardSignaturePatternString_Type()
)
bsnStandardSignaturePatternString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnStandardSignaturePatternString.setStatus("current")


class _BsnStandardSignaturePatternMask_Type(DisplayString):
    """Custom type bsnStandardSignaturePatternMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_BsnStandardSignaturePatternMask_Type.__name__ = "DisplayString"
_BsnStandardSignaturePatternMask_Object = MibTableColumn
bsnStandardSignaturePatternMask = _BsnStandardSignaturePatternMask_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 2, 1, 4),
    _BsnStandardSignaturePatternMask_Type()
)
bsnStandardSignaturePatternMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnStandardSignaturePatternMask.setStatus("current")
_BsnStandardSignaturePatternOffSetStart_Type = BsnSignaturePatternOffSetStart
_BsnStandardSignaturePatternOffSetStart_Object = MibTableColumn
bsnStandardSignaturePatternOffSetStart = _BsnStandardSignaturePatternOffSetStart_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 2, 1, 5),
    _BsnStandardSignaturePatternOffSetStart_Type()
)
bsnStandardSignaturePatternOffSetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnStandardSignaturePatternOffSetStart.setStatus("current")
_BsnStandardSignaturePatternRowStatus_Type = RowStatus
_BsnStandardSignaturePatternRowStatus_Object = MibTableColumn
bsnStandardSignaturePatternRowStatus = _BsnStandardSignaturePatternRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 2, 1, 15),
    _BsnStandardSignaturePatternRowStatus_Type()
)
bsnStandardSignaturePatternRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnStandardSignaturePatternRowStatus.setStatus("current")
_BsnCustomSignatureTable_Object = MibTable
bsnCustomSignatureTable = _BsnCustomSignatureTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 3)
)
if mibBuilder.loadTexts:
    bsnCustomSignatureTable.setStatus("current")
_BsnCustomSignatureEntry_Object = MibTableRow
bsnCustomSignatureEntry = _BsnCustomSignatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 3, 1)
)
bsnCustomSignatureEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnCustomSignaturePrecedence"),
)
if mibBuilder.loadTexts:
    bsnCustomSignatureEntry.setStatus("current")


class _BsnCustomSignaturePrecedence_Type(Unsigned32):
    """Custom type bsnCustomSignaturePrecedence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_BsnCustomSignaturePrecedence_Type.__name__ = "Unsigned32"
_BsnCustomSignaturePrecedence_Object = MibTableColumn
bsnCustomSignaturePrecedence = _BsnCustomSignaturePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 3, 1, 1),
    _BsnCustomSignaturePrecedence_Type()
)
bsnCustomSignaturePrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnCustomSignaturePrecedence.setStatus("current")


class _BsnCustomSignatureName_Type(DisplayString):
    """Custom type bsnCustomSignatureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BsnCustomSignatureName_Type.__name__ = "DisplayString"
_BsnCustomSignatureName_Object = MibTableColumn
bsnCustomSignatureName = _BsnCustomSignatureName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 3, 1, 2),
    _BsnCustomSignatureName_Type()
)
bsnCustomSignatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnCustomSignatureName.setStatus("current")


class _BsnCustomSignatureDescription_Type(DisplayString):
    """Custom type bsnCustomSignatureDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_BsnCustomSignatureDescription_Type.__name__ = "DisplayString"
_BsnCustomSignatureDescription_Object = MibTableColumn
bsnCustomSignatureDescription = _BsnCustomSignatureDescription_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 3, 1, 3),
    _BsnCustomSignatureDescription_Type()
)
bsnCustomSignatureDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnCustomSignatureDescription.setStatus("current")


class _BsnCustomSignatureFrameType_Type(Integer32):
    """Custom type bsnCustomSignatureFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("management", 0))
    )


_BsnCustomSignatureFrameType_Type.__name__ = "Integer32"
_BsnCustomSignatureFrameType_Object = MibTableColumn
bsnCustomSignatureFrameType = _BsnCustomSignatureFrameType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 3, 1, 4),
    _BsnCustomSignatureFrameType_Type()
)
bsnCustomSignatureFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnCustomSignatureFrameType.setStatus("current")


class _BsnCustomSignatureAction_Type(Integer32):
    """Custom type bsnCustomSignatureAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("contain", 2),
          ("exclude", 3),
          ("none", 0),
          ("report", 1))
    )


_BsnCustomSignatureAction_Type.__name__ = "Integer32"
_BsnCustomSignatureAction_Object = MibTableColumn
bsnCustomSignatureAction = _BsnCustomSignatureAction_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 3, 1, 5),
    _BsnCustomSignatureAction_Type()
)
bsnCustomSignatureAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnCustomSignatureAction.setStatus("current")


class _BsnCustomSignatureState_Type(Integer32):
    """Custom type bsnCustomSignatureState based on Integer32"""
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


_BsnCustomSignatureState_Type.__name__ = "Integer32"
_BsnCustomSignatureState_Object = MibTableColumn
bsnCustomSignatureState = _BsnCustomSignatureState_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 3, 1, 6),
    _BsnCustomSignatureState_Type()
)
bsnCustomSignatureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnCustomSignatureState.setStatus("current")


class _BsnCustomSignatureFrequency_Type(Unsigned32):
    """Custom type bsnCustomSignatureFrequency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BsnCustomSignatureFrequency_Type.__name__ = "Unsigned32"
_BsnCustomSignatureFrequency_Object = MibTableColumn
bsnCustomSignatureFrequency = _BsnCustomSignatureFrequency_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 3, 1, 7),
    _BsnCustomSignatureFrequency_Type()
)
bsnCustomSignatureFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnCustomSignatureFrequency.setStatus("current")


class _BsnCustomSignatureQuietTime_Type(Unsigned32):
    """Custom type bsnCustomSignatureQuietTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BsnCustomSignatureQuietTime_Type.__name__ = "Unsigned32"
_BsnCustomSignatureQuietTime_Object = MibTableColumn
bsnCustomSignatureQuietTime = _BsnCustomSignatureQuietTime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 3, 1, 8),
    _BsnCustomSignatureQuietTime_Type()
)
bsnCustomSignatureQuietTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnCustomSignatureQuietTime.setStatus("current")


class _BsnCustomSignatureVersion_Type(Unsigned32):
    """Custom type bsnCustomSignatureVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_BsnCustomSignatureVersion_Type.__name__ = "Unsigned32"
_BsnCustomSignatureVersion_Object = MibTableColumn
bsnCustomSignatureVersion = _BsnCustomSignatureVersion_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 3, 1, 9),
    _BsnCustomSignatureVersion_Type()
)
bsnCustomSignatureVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnCustomSignatureVersion.setStatus("current")


class _BsnCustomSignatureConfigType_Type(Integer32):
    """Custom type bsnCustomSignatureConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pattern", 0),
          ("protocol", 1))
    )


_BsnCustomSignatureConfigType_Type.__name__ = "Integer32"
_BsnCustomSignatureConfigType_Object = MibTableColumn
bsnCustomSignatureConfigType = _BsnCustomSignatureConfigType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 3, 1, 10),
    _BsnCustomSignatureConfigType_Type()
)
bsnCustomSignatureConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnCustomSignatureConfigType.setStatus("current")


class _BsnCustomSignatureEnable_Type(TruthValue):
    """Custom type bsnCustomSignatureEnable based on TruthValue"""


_BsnCustomSignatureEnable_Object = MibTableColumn
bsnCustomSignatureEnable = _BsnCustomSignatureEnable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 3, 1, 11),
    _BsnCustomSignatureEnable_Type()
)
bsnCustomSignatureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnCustomSignatureEnable.setStatus("current")
_BsnCustomSignatureMacInfo_Type = BsnTxtSignatureMacInfo
_BsnCustomSignatureMacInfo_Object = MibTableColumn
bsnCustomSignatureMacInfo = _BsnCustomSignatureMacInfo_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 3, 1, 12),
    _BsnCustomSignatureMacInfo_Type()
)
bsnCustomSignatureMacInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnCustomSignatureMacInfo.setStatus("current")


class _BsnCustomSignatureMacFreq_Type(Unsigned32):
    """Custom type bsnCustomSignatureMacFreq based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BsnCustomSignatureMacFreq_Type.__name__ = "Unsigned32"
_BsnCustomSignatureMacFreq_Object = MibTableColumn
bsnCustomSignatureMacFreq = _BsnCustomSignatureMacFreq_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 3, 1, 13),
    _BsnCustomSignatureMacFreq_Type()
)
bsnCustomSignatureMacFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnCustomSignatureMacFreq.setStatus("current")
_BsnCustomSignatureRowStatus_Type = RowStatus
_BsnCustomSignatureRowStatus_Object = MibTableColumn
bsnCustomSignatureRowStatus = _BsnCustomSignatureRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 3, 1, 20),
    _BsnCustomSignatureRowStatus_Type()
)
bsnCustomSignatureRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnCustomSignatureRowStatus.setStatus("current")


class _BsnCustomSignatureInterval_Type(Unsigned32):
    """Custom type bsnCustomSignatureInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_BsnCustomSignatureInterval_Type.__name__ = "Unsigned32"
_BsnCustomSignatureInterval_Object = MibTableColumn
bsnCustomSignatureInterval = _BsnCustomSignatureInterval_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 3, 1, 21),
    _BsnCustomSignatureInterval_Type()
)
bsnCustomSignatureInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnCustomSignatureInterval.setStatus("current")
_BsnCustomSignaturePatternTable_Object = MibTable
bsnCustomSignaturePatternTable = _BsnCustomSignaturePatternTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 4)
)
if mibBuilder.loadTexts:
    bsnCustomSignaturePatternTable.setStatus("current")
_BsnCustomSignaturePatternEntry_Object = MibTableRow
bsnCustomSignaturePatternEntry = _BsnCustomSignaturePatternEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 4, 1)
)
bsnCustomSignaturePatternEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnCustomSignaturePrecedence"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnCustomSignaturePatternIndex"),
)
if mibBuilder.loadTexts:
    bsnCustomSignaturePatternEntry.setStatus("current")


class _BsnCustomSignaturePatternIndex_Type(Unsigned32):
    """Custom type bsnCustomSignaturePatternIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_BsnCustomSignaturePatternIndex_Type.__name__ = "Unsigned32"
_BsnCustomSignaturePatternIndex_Object = MibTableColumn
bsnCustomSignaturePatternIndex = _BsnCustomSignaturePatternIndex_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 4, 1, 1),
    _BsnCustomSignaturePatternIndex_Type()
)
bsnCustomSignaturePatternIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnCustomSignaturePatternIndex.setStatus("current")


class _BsnCustomSignaturePatternOffset_Type(Unsigned32):
    """Custom type bsnCustomSignaturePatternOffset based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_BsnCustomSignaturePatternOffset_Type.__name__ = "Unsigned32"
_BsnCustomSignaturePatternOffset_Object = MibTableColumn
bsnCustomSignaturePatternOffset = _BsnCustomSignaturePatternOffset_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 4, 1, 2),
    _BsnCustomSignaturePatternOffset_Type()
)
bsnCustomSignaturePatternOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnCustomSignaturePatternOffset.setStatus("current")


class _BsnCustomSignaturePatternString_Type(DisplayString):
    """Custom type bsnCustomSignaturePatternString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_BsnCustomSignaturePatternString_Type.__name__ = "DisplayString"
_BsnCustomSignaturePatternString_Object = MibTableColumn
bsnCustomSignaturePatternString = _BsnCustomSignaturePatternString_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 4, 1, 3),
    _BsnCustomSignaturePatternString_Type()
)
bsnCustomSignaturePatternString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnCustomSignaturePatternString.setStatus("current")


class _BsnCustomSignaturePatternMask_Type(DisplayString):
    """Custom type bsnCustomSignaturePatternMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_BsnCustomSignaturePatternMask_Type.__name__ = "DisplayString"
_BsnCustomSignaturePatternMask_Object = MibTableColumn
bsnCustomSignaturePatternMask = _BsnCustomSignaturePatternMask_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 4, 1, 4),
    _BsnCustomSignaturePatternMask_Type()
)
bsnCustomSignaturePatternMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnCustomSignaturePatternMask.setStatus("current")
_BsnCustomSignaturePatternOffSetStart_Type = BsnSignaturePatternOffSetStart
_BsnCustomSignaturePatternOffSetStart_Object = MibTableColumn
bsnCustomSignaturePatternOffSetStart = _BsnCustomSignaturePatternOffSetStart_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 4, 1, 5),
    _BsnCustomSignaturePatternOffSetStart_Type()
)
bsnCustomSignaturePatternOffSetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnCustomSignaturePatternOffSetStart.setStatus("current")
_BsnCustomSignaturePatternRowStatus_Type = RowStatus
_BsnCustomSignaturePatternRowStatus_Object = MibTableColumn
bsnCustomSignaturePatternRowStatus = _BsnCustomSignaturePatternRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 4, 1, 15),
    _BsnCustomSignaturePatternRowStatus_Type()
)
bsnCustomSignaturePatternRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnCustomSignaturePatternRowStatus.setStatus("current")


class _BsnSignatureCheckState_Type(Integer32):
    """Custom type bsnSignatureCheckState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnSignatureCheckState_Type.__name__ = "Integer32"
_BsnSignatureCheckState_Object = MibScalar
bsnSignatureCheckState = _BsnSignatureCheckState_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 42, 5),
    _BsnSignatureCheckState_Type()
)
bsnSignatureCheckState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnSignatureCheckState.setStatus("current")
_BsnRfIdTagConfig_ObjectIdentity = ObjectIdentity
bsnRfIdTagConfig = _BsnRfIdTagConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 43)
)


class _BsnRfIdTagStatus_Type(Integer32):
    """Custom type bsnRfIdTagStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnRfIdTagStatus_Type.__name__ = "Integer32"
_BsnRfIdTagStatus_Object = MibScalar
bsnRfIdTagStatus = _BsnRfIdTagStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 43, 1),
    _BsnRfIdTagStatus_Type()
)
bsnRfIdTagStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRfIdTagStatus.setStatus("current")


class _BsnRfIdTagDataTimeout_Type(Unsigned32):
    """Custom type bsnRfIdTagDataTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 7200),
    )


_BsnRfIdTagDataTimeout_Type.__name__ = "Unsigned32"
_BsnRfIdTagDataTimeout_Object = MibScalar
bsnRfIdTagDataTimeout = _BsnRfIdTagDataTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 43, 2),
    _BsnRfIdTagDataTimeout_Type()
)
bsnRfIdTagDataTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRfIdTagDataTimeout.setStatus("current")


class _BsnRfIdTagAutoTimeoutStatus_Type(Integer32):
    """Custom type bsnRfIdTagAutoTimeoutStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnRfIdTagAutoTimeoutStatus_Type.__name__ = "Integer32"
_BsnRfIdTagAutoTimeoutStatus_Object = MibScalar
bsnRfIdTagAutoTimeoutStatus = _BsnRfIdTagAutoTimeoutStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 43, 3),
    _BsnRfIdTagAutoTimeoutStatus_Type()
)
bsnRfIdTagAutoTimeoutStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRfIdTagAutoTimeoutStatus.setStatus("current")
_BsnAPNeighborAuthConfig_ObjectIdentity = ObjectIdentity
bsnAPNeighborAuthConfig = _BsnAPNeighborAuthConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 44)
)


class _BsnAPNeighborAuthStatus_Type(Integer32):
    """Custom type bsnAPNeighborAuthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnAPNeighborAuthStatus_Type.__name__ = "Integer32"
_BsnAPNeighborAuthStatus_Object = MibScalar
bsnAPNeighborAuthStatus = _BsnAPNeighborAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 44, 1),
    _BsnAPNeighborAuthStatus_Type()
)
bsnAPNeighborAuthStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPNeighborAuthStatus.setStatus("current")


class _BsnAPNeighborAuthAlarmThreshold_Type(Integer32):
    """Custom type bsnAPNeighborAuthAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BsnAPNeighborAuthAlarmThreshold_Type.__name__ = "Integer32"
_BsnAPNeighborAuthAlarmThreshold_Object = MibScalar
bsnAPNeighborAuthAlarmThreshold = _BsnAPNeighborAuthAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 44, 2),
    _BsnAPNeighborAuthAlarmThreshold_Type()
)
bsnAPNeighborAuthAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPNeighborAuthAlarmThreshold.setStatus("current")


class _BsnRFNetworkName_Type(OctetString):
    """Custom type bsnRFNetworkName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_BsnRFNetworkName_Type.__name__ = "OctetString"
_BsnRFNetworkName_Object = MibScalar
bsnRFNetworkName = _BsnRFNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 45),
    _BsnRFNetworkName_Type()
)
bsnRFNetworkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRFNetworkName.setStatus("current")


class _BsnFastSSIDChangeFeature_Type(Integer32):
    """Custom type bsnFastSSIDChangeFeature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnFastSSIDChangeFeature_Type.__name__ = "Integer32"
_BsnFastSSIDChangeFeature_Object = MibScalar
bsnFastSSIDChangeFeature = _BsnFastSSIDChangeFeature_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 46),
    _BsnFastSSIDChangeFeature_Type()
)
bsnFastSSIDChangeFeature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnFastSSIDChangeFeature.setStatus("current")
_BsnBridgingPolicyConfig_ObjectIdentity = ObjectIdentity
bsnBridgingPolicyConfig = _BsnBridgingPolicyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 47)
)


class _BsnBridgingZeroTouchConfig_Type(Integer32):
    """Custom type bsnBridgingZeroTouchConfig based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnBridgingZeroTouchConfig_Type.__name__ = "Integer32"
_BsnBridgingZeroTouchConfig_Object = MibScalar
bsnBridgingZeroTouchConfig = _BsnBridgingZeroTouchConfig_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 47, 1),
    _BsnBridgingZeroTouchConfig_Type()
)
bsnBridgingZeroTouchConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnBridgingZeroTouchConfig.setStatus("current")


class _BsnBridgingSharedSecretKey_Type(OctetString):
    """Custom type bsnBridgingSharedSecretKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BsnBridgingSharedSecretKey_Type.__name__ = "OctetString"
_BsnBridgingSharedSecretKey_Object = MibScalar
bsnBridgingSharedSecretKey = _BsnBridgingSharedSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 47, 2),
    _BsnBridgingSharedSecretKey_Type()
)
bsnBridgingSharedSecretKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnBridgingSharedSecretKey.setStatus("current")


class _BsnAcceptSelfSignedCertificate_Type(Integer32):
    """Custom type bsnAcceptSelfSignedCertificate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnAcceptSelfSignedCertificate_Type.__name__ = "Integer32"
_BsnAcceptSelfSignedCertificate_Object = MibScalar
bsnAcceptSelfSignedCertificate = _BsnAcceptSelfSignedCertificate_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 48),
    _BsnAcceptSelfSignedCertificate_Type()
)
bsnAcceptSelfSignedCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAcceptSelfSignedCertificate.setStatus("current")
_BsnSystemClockTime_Type = Unsigned32
_BsnSystemClockTime_Object = MibScalar
bsnSystemClockTime = _BsnSystemClockTime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 1, 49),
    _BsnSystemClockTime_Type()
)
bsnSystemClockTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnSystemClockTime.setStatus("current")
if mibBuilder.loadTexts:
    bsnSystemClockTime.setUnits("seconds")
_BsnGlobalDot11b_ObjectIdentity = ObjectIdentity
bsnGlobalDot11b = _BsnGlobalDot11b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2)
)
_BsnGlobalDot11bConfig_ObjectIdentity = ObjectIdentity
bsnGlobalDot11bConfig = _BsnGlobalDot11bConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1)
)


class _BsnGlobalDot11bNetworkStatus_Type(Integer32):
    """Custom type bsnGlobalDot11bNetworkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnGlobalDot11bNetworkStatus_Type.__name__ = "Integer32"
_BsnGlobalDot11bNetworkStatus_Object = MibScalar
bsnGlobalDot11bNetworkStatus = _BsnGlobalDot11bNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 1),
    _BsnGlobalDot11bNetworkStatus_Type()
)
bsnGlobalDot11bNetworkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bNetworkStatus.setStatus("current")


class _BsnGlobalDot11bBeaconPeriod_Type(Integer32):
    """Custom type bsnGlobalDot11bBeaconPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 1000),
    )


_BsnGlobalDot11bBeaconPeriod_Type.__name__ = "Integer32"
_BsnGlobalDot11bBeaconPeriod_Object = MibScalar
bsnGlobalDot11bBeaconPeriod = _BsnGlobalDot11bBeaconPeriod_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 2),
    _BsnGlobalDot11bBeaconPeriod_Type()
)
bsnGlobalDot11bBeaconPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bBeaconPeriod.setStatus("current")


class _BsnGlobalDot11bDynamicChannelAssignment_Type(Integer32):
    """Custom type bsnGlobalDot11bDynamicChannelAssignment based on Integer32"""
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
        *(("automatic", 1),
          ("runOnce", 2),
          ("static", 3))
    )


_BsnGlobalDot11bDynamicChannelAssignment_Type.__name__ = "Integer32"
_BsnGlobalDot11bDynamicChannelAssignment_Object = MibScalar
bsnGlobalDot11bDynamicChannelAssignment = _BsnGlobalDot11bDynamicChannelAssignment_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 3),
    _BsnGlobalDot11bDynamicChannelAssignment_Type()
)
bsnGlobalDot11bDynamicChannelAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bDynamicChannelAssignment.setStatus("current")


class _BsnGlobalDot11bCurrentChannel_Type(Integer32):
    """Custom type bsnGlobalDot11bCurrentChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_BsnGlobalDot11bCurrentChannel_Type.__name__ = "Integer32"
_BsnGlobalDot11bCurrentChannel_Object = MibScalar
bsnGlobalDot11bCurrentChannel = _BsnGlobalDot11bCurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 4),
    _BsnGlobalDot11bCurrentChannel_Type()
)
bsnGlobalDot11bCurrentChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bCurrentChannel.setStatus("current")


class _BsnGlobalDot11bDynamicChannelUpdateInterval_Type(Unsigned32):
    """Custom type bsnGlobalDot11bDynamicChannelUpdateInterval based on Unsigned32"""
    defaultValue = 600


_BsnGlobalDot11bDynamicChannelUpdateInterval_Object = MibScalar
bsnGlobalDot11bDynamicChannelUpdateInterval = _BsnGlobalDot11bDynamicChannelUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 5),
    _BsnGlobalDot11bDynamicChannelUpdateInterval_Type()
)
bsnGlobalDot11bDynamicChannelUpdateInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11bDynamicChannelUpdateInterval.setStatus("current")


class _BsnGlobalDot11bInputsForDCA_Type(Unsigned32):
    """Custom type bsnGlobalDot11bInputsForDCA based on Unsigned32"""
    defaultValue = 63


_BsnGlobalDot11bInputsForDCA_Object = MibScalar
bsnGlobalDot11bInputsForDCA = _BsnGlobalDot11bInputsForDCA_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 6),
    _BsnGlobalDot11bInputsForDCA_Type()
)
bsnGlobalDot11bInputsForDCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bInputsForDCA.setStatus("current")


class _BsnGlobalDot11bChannelUpdateCmdInvoke_Type(Integer32):
    """Custom type bsnGlobalDot11bChannelUpdateCmdInvoke based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("default", 0))
    )


_BsnGlobalDot11bChannelUpdateCmdInvoke_Type.__name__ = "Integer32"
_BsnGlobalDot11bChannelUpdateCmdInvoke_Object = MibScalar
bsnGlobalDot11bChannelUpdateCmdInvoke = _BsnGlobalDot11bChannelUpdateCmdInvoke_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 7),
    _BsnGlobalDot11bChannelUpdateCmdInvoke_Type()
)
bsnGlobalDot11bChannelUpdateCmdInvoke.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bChannelUpdateCmdInvoke.setStatus("current")
_BsnGlobalDot11bChannelUpdateCmdStatus_Type = Integer32
_BsnGlobalDot11bChannelUpdateCmdStatus_Object = MibScalar
bsnGlobalDot11bChannelUpdateCmdStatus = _BsnGlobalDot11bChannelUpdateCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 8),
    _BsnGlobalDot11bChannelUpdateCmdStatus_Type()
)
bsnGlobalDot11bChannelUpdateCmdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11bChannelUpdateCmdStatus.setStatus("current")


class _BsnGlobalDot11bDynamicTransmitPowerControl_Type(Integer32):
    """Custom type bsnGlobalDot11bDynamicTransmitPowerControl based on Integer32"""
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
        *(("automatic", 1),
          ("runOnce", 2),
          ("static", 3))
    )


_BsnGlobalDot11bDynamicTransmitPowerControl_Type.__name__ = "Integer32"
_BsnGlobalDot11bDynamicTransmitPowerControl_Object = MibScalar
bsnGlobalDot11bDynamicTransmitPowerControl = _BsnGlobalDot11bDynamicTransmitPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 9),
    _BsnGlobalDot11bDynamicTransmitPowerControl_Type()
)
bsnGlobalDot11bDynamicTransmitPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bDynamicTransmitPowerControl.setStatus("current")


class _BsnGlobalDot11bDynamicTxPowerControlInterval_Type(Unsigned32):
    """Custom type bsnGlobalDot11bDynamicTxPowerControlInterval based on Unsigned32"""
    defaultValue = 600


_BsnGlobalDot11bDynamicTxPowerControlInterval_Object = MibScalar
bsnGlobalDot11bDynamicTxPowerControlInterval = _BsnGlobalDot11bDynamicTxPowerControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 10),
    _BsnGlobalDot11bDynamicTxPowerControlInterval_Type()
)
bsnGlobalDot11bDynamicTxPowerControlInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11bDynamicTxPowerControlInterval.setStatus("current")


class _BsnGlobalDot11bCurrentTxPowerLevel_Type(Integer32):
    """Custom type bsnGlobalDot11bCurrentTxPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_BsnGlobalDot11bCurrentTxPowerLevel_Type.__name__ = "Integer32"
_BsnGlobalDot11bCurrentTxPowerLevel_Object = MibScalar
bsnGlobalDot11bCurrentTxPowerLevel = _BsnGlobalDot11bCurrentTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 11),
    _BsnGlobalDot11bCurrentTxPowerLevel_Type()
)
bsnGlobalDot11bCurrentTxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bCurrentTxPowerLevel.setStatus("current")


class _BsnGlobalDot11bInputsForDTP_Type(Unsigned32):
    """Custom type bsnGlobalDot11bInputsForDTP based on Unsigned32"""
    defaultValue = 15


_BsnGlobalDot11bInputsForDTP_Object = MibScalar
bsnGlobalDot11bInputsForDTP = _BsnGlobalDot11bInputsForDTP_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 12),
    _BsnGlobalDot11bInputsForDTP_Type()
)
bsnGlobalDot11bInputsForDTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bInputsForDTP.setStatus("current")


class _BsnGlobalDot11bPowerUpdateCmdInvoke_Type(Integer32):
    """Custom type bsnGlobalDot11bPowerUpdateCmdInvoke based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("default", 0))
    )


_BsnGlobalDot11bPowerUpdateCmdInvoke_Type.__name__ = "Integer32"
_BsnGlobalDot11bPowerUpdateCmdInvoke_Object = MibScalar
bsnGlobalDot11bPowerUpdateCmdInvoke = _BsnGlobalDot11bPowerUpdateCmdInvoke_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 13),
    _BsnGlobalDot11bPowerUpdateCmdInvoke_Type()
)
bsnGlobalDot11bPowerUpdateCmdInvoke.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bPowerUpdateCmdInvoke.setStatus("current")
_BsnGlobalDot11bPowerUpdateCmdStatus_Type = Integer32
_BsnGlobalDot11bPowerUpdateCmdStatus_Object = MibScalar
bsnGlobalDot11bPowerUpdateCmdStatus = _BsnGlobalDot11bPowerUpdateCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 14),
    _BsnGlobalDot11bPowerUpdateCmdStatus_Type()
)
bsnGlobalDot11bPowerUpdateCmdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11bPowerUpdateCmdStatus.setStatus("current")


class _BsnGlobalDot11bDataRate1Mhz_Type(Integer32):
    """Custom type bsnGlobalDot11bDataRate1Mhz based on Integer32"""
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
          ("mandatory", 2),
          ("supported", 1))
    )


_BsnGlobalDot11bDataRate1Mhz_Type.__name__ = "Integer32"
_BsnGlobalDot11bDataRate1Mhz_Object = MibScalar
bsnGlobalDot11bDataRate1Mhz = _BsnGlobalDot11bDataRate1Mhz_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 15),
    _BsnGlobalDot11bDataRate1Mhz_Type()
)
bsnGlobalDot11bDataRate1Mhz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bDataRate1Mhz.setStatus("current")


class _BsnGlobalDot11bDataRate2Mhz_Type(Integer32):
    """Custom type bsnGlobalDot11bDataRate2Mhz based on Integer32"""
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
          ("mandatory", 2),
          ("supported", 1))
    )


_BsnGlobalDot11bDataRate2Mhz_Type.__name__ = "Integer32"
_BsnGlobalDot11bDataRate2Mhz_Object = MibScalar
bsnGlobalDot11bDataRate2Mhz = _BsnGlobalDot11bDataRate2Mhz_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 16),
    _BsnGlobalDot11bDataRate2Mhz_Type()
)
bsnGlobalDot11bDataRate2Mhz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bDataRate2Mhz.setStatus("current")


class _BsnGlobalDot11bDataRate5AndHalfMhz_Type(Integer32):
    """Custom type bsnGlobalDot11bDataRate5AndHalfMhz based on Integer32"""
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
          ("mandatory", 2),
          ("supported", 1))
    )


_BsnGlobalDot11bDataRate5AndHalfMhz_Type.__name__ = "Integer32"
_BsnGlobalDot11bDataRate5AndHalfMhz_Object = MibScalar
bsnGlobalDot11bDataRate5AndHalfMhz = _BsnGlobalDot11bDataRate5AndHalfMhz_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 17),
    _BsnGlobalDot11bDataRate5AndHalfMhz_Type()
)
bsnGlobalDot11bDataRate5AndHalfMhz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bDataRate5AndHalfMhz.setStatus("current")


class _BsnGlobalDot11bDataRate11Mhz_Type(Integer32):
    """Custom type bsnGlobalDot11bDataRate11Mhz based on Integer32"""
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
          ("mandatory", 2),
          ("supported", 1))
    )


_BsnGlobalDot11bDataRate11Mhz_Type.__name__ = "Integer32"
_BsnGlobalDot11bDataRate11Mhz_Object = MibScalar
bsnGlobalDot11bDataRate11Mhz = _BsnGlobalDot11bDataRate11Mhz_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 18),
    _BsnGlobalDot11bDataRate11Mhz_Type()
)
bsnGlobalDot11bDataRate11Mhz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bDataRate11Mhz.setStatus("current")


class _BsnGlobalDot11bShortPreamble_Type(Integer32):
    """Custom type bsnGlobalDot11bShortPreamble based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnGlobalDot11bShortPreamble_Type.__name__ = "Integer32"
_BsnGlobalDot11bShortPreamble_Object = MibScalar
bsnGlobalDot11bShortPreamble = _BsnGlobalDot11bShortPreamble_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 19),
    _BsnGlobalDot11bShortPreamble_Type()
)
bsnGlobalDot11bShortPreamble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bShortPreamble.setStatus("current")


class _BsnGlobalDot11bDot11gSupport_Type(Integer32):
    """Custom type bsnGlobalDot11bDot11gSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnGlobalDot11bDot11gSupport_Type.__name__ = "Integer32"
_BsnGlobalDot11bDot11gSupport_Object = MibScalar
bsnGlobalDot11bDot11gSupport = _BsnGlobalDot11bDot11gSupport_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 20),
    _BsnGlobalDot11bDot11gSupport_Type()
)
bsnGlobalDot11bDot11gSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bDot11gSupport.setStatus("current")


class _BsnGlobalDot11bDataRate6Mhz_Type(Integer32):
    """Custom type bsnGlobalDot11bDataRate6Mhz based on Integer32"""
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
          ("mandatory", 2),
          ("supported", 1))
    )


_BsnGlobalDot11bDataRate6Mhz_Type.__name__ = "Integer32"
_BsnGlobalDot11bDataRate6Mhz_Object = MibScalar
bsnGlobalDot11bDataRate6Mhz = _BsnGlobalDot11bDataRate6Mhz_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 21),
    _BsnGlobalDot11bDataRate6Mhz_Type()
)
bsnGlobalDot11bDataRate6Mhz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bDataRate6Mhz.setStatus("current")


class _BsnGlobalDot11bDataRate9Mhz_Type(Integer32):
    """Custom type bsnGlobalDot11bDataRate9Mhz based on Integer32"""
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
          ("mandatory", 2),
          ("supported", 1))
    )


_BsnGlobalDot11bDataRate9Mhz_Type.__name__ = "Integer32"
_BsnGlobalDot11bDataRate9Mhz_Object = MibScalar
bsnGlobalDot11bDataRate9Mhz = _BsnGlobalDot11bDataRate9Mhz_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 22),
    _BsnGlobalDot11bDataRate9Mhz_Type()
)
bsnGlobalDot11bDataRate9Mhz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bDataRate9Mhz.setStatus("current")


class _BsnGlobalDot11bDataRate12Mhz_Type(Integer32):
    """Custom type bsnGlobalDot11bDataRate12Mhz based on Integer32"""
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
          ("mandatory", 2),
          ("supported", 1))
    )


_BsnGlobalDot11bDataRate12Mhz_Type.__name__ = "Integer32"
_BsnGlobalDot11bDataRate12Mhz_Object = MibScalar
bsnGlobalDot11bDataRate12Mhz = _BsnGlobalDot11bDataRate12Mhz_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 23),
    _BsnGlobalDot11bDataRate12Mhz_Type()
)
bsnGlobalDot11bDataRate12Mhz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bDataRate12Mhz.setStatus("current")


class _BsnGlobalDot11bDataRate18Mhz_Type(Integer32):
    """Custom type bsnGlobalDot11bDataRate18Mhz based on Integer32"""
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
          ("mandatory", 2),
          ("supported", 1))
    )


_BsnGlobalDot11bDataRate18Mhz_Type.__name__ = "Integer32"
_BsnGlobalDot11bDataRate18Mhz_Object = MibScalar
bsnGlobalDot11bDataRate18Mhz = _BsnGlobalDot11bDataRate18Mhz_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 24),
    _BsnGlobalDot11bDataRate18Mhz_Type()
)
bsnGlobalDot11bDataRate18Mhz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bDataRate18Mhz.setStatus("current")


class _BsnGlobalDot11bDataRate24Mhz_Type(Integer32):
    """Custom type bsnGlobalDot11bDataRate24Mhz based on Integer32"""
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
          ("mandatory", 2),
          ("supported", 1))
    )


_BsnGlobalDot11bDataRate24Mhz_Type.__name__ = "Integer32"
_BsnGlobalDot11bDataRate24Mhz_Object = MibScalar
bsnGlobalDot11bDataRate24Mhz = _BsnGlobalDot11bDataRate24Mhz_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 25),
    _BsnGlobalDot11bDataRate24Mhz_Type()
)
bsnGlobalDot11bDataRate24Mhz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bDataRate24Mhz.setStatus("current")


class _BsnGlobalDot11bDataRate36Mhz_Type(Integer32):
    """Custom type bsnGlobalDot11bDataRate36Mhz based on Integer32"""
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
          ("mandatory", 2),
          ("supported", 1))
    )


_BsnGlobalDot11bDataRate36Mhz_Type.__name__ = "Integer32"
_BsnGlobalDot11bDataRate36Mhz_Object = MibScalar
bsnGlobalDot11bDataRate36Mhz = _BsnGlobalDot11bDataRate36Mhz_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 26),
    _BsnGlobalDot11bDataRate36Mhz_Type()
)
bsnGlobalDot11bDataRate36Mhz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bDataRate36Mhz.setStatus("current")


class _BsnGlobalDot11bDataRate48Mhz_Type(Integer32):
    """Custom type bsnGlobalDot11bDataRate48Mhz based on Integer32"""
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
          ("mandatory", 2),
          ("supported", 1))
    )


_BsnGlobalDot11bDataRate48Mhz_Type.__name__ = "Integer32"
_BsnGlobalDot11bDataRate48Mhz_Object = MibScalar
bsnGlobalDot11bDataRate48Mhz = _BsnGlobalDot11bDataRate48Mhz_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 27),
    _BsnGlobalDot11bDataRate48Mhz_Type()
)
bsnGlobalDot11bDataRate48Mhz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bDataRate48Mhz.setStatus("current")


class _BsnGlobalDot11bDataRate54Mhz_Type(Integer32):
    """Custom type bsnGlobalDot11bDataRate54Mhz based on Integer32"""
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
          ("mandatory", 2),
          ("supported", 1))
    )


_BsnGlobalDot11bDataRate54Mhz_Type.__name__ = "Integer32"
_BsnGlobalDot11bDataRate54Mhz_Object = MibScalar
bsnGlobalDot11bDataRate54Mhz = _BsnGlobalDot11bDataRate54Mhz_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 28),
    _BsnGlobalDot11bDataRate54Mhz_Type()
)
bsnGlobalDot11bDataRate54Mhz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bDataRate54Mhz.setStatus("current")


class _BsnGlobalDot11bPicoCellMode_Type(Integer32):
    """Custom type bsnGlobalDot11bPicoCellMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnGlobalDot11bPicoCellMode_Type.__name__ = "Integer32"
_BsnGlobalDot11bPicoCellMode_Object = MibScalar
bsnGlobalDot11bPicoCellMode = _BsnGlobalDot11bPicoCellMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 29),
    _BsnGlobalDot11bPicoCellMode_Type()
)
bsnGlobalDot11bPicoCellMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bPicoCellMode.setStatus("current")


class _BsnGlobalDot11bFastRoamingMode_Type(Integer32):
    """Custom type bsnGlobalDot11bFastRoamingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnGlobalDot11bFastRoamingMode_Type.__name__ = "Integer32"
_BsnGlobalDot11bFastRoamingMode_Object = MibScalar
bsnGlobalDot11bFastRoamingMode = _BsnGlobalDot11bFastRoamingMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 30),
    _BsnGlobalDot11bFastRoamingMode_Type()
)
bsnGlobalDot11bFastRoamingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bFastRoamingMode.setStatus("current")


class _BsnGlobalDot11bFastRoamingVoipMinRate_Type(Integer32):
    """Custom type bsnGlobalDot11bFastRoamingVoipMinRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("rate11Mbps", 4),
          ("rate1Mbps", 1),
          ("rate2Mbps", 2),
          ("rate5andHalfMbps", 3),
          ("undefined", 0))
    )


_BsnGlobalDot11bFastRoamingVoipMinRate_Type.__name__ = "Integer32"
_BsnGlobalDot11bFastRoamingVoipMinRate_Object = MibScalar
bsnGlobalDot11bFastRoamingVoipMinRate = _BsnGlobalDot11bFastRoamingVoipMinRate_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 31),
    _BsnGlobalDot11bFastRoamingVoipMinRate_Type()
)
bsnGlobalDot11bFastRoamingVoipMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bFastRoamingVoipMinRate.setStatus("current")


class _BsnGlobalDot11bFastRoamingVoipPercentage_Type(Integer32):
    """Custom type bsnGlobalDot11bFastRoamingVoipPercentage based on Integer32"""
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
        *(("fifty", 3),
          ("hundred", 5),
          ("seventyfive", 4),
          ("twentyfive", 2),
          ("zero", 1))
    )


_BsnGlobalDot11bFastRoamingVoipPercentage_Type.__name__ = "Integer32"
_BsnGlobalDot11bFastRoamingVoipPercentage_Object = MibScalar
bsnGlobalDot11bFastRoamingVoipPercentage = _BsnGlobalDot11bFastRoamingVoipPercentage_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 32),
    _BsnGlobalDot11bFastRoamingVoipPercentage_Type()
)
bsnGlobalDot11bFastRoamingVoipPercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bFastRoamingVoipPercentage.setStatus("current")


class _BsnGlobalDot11b80211eMaxBandwidth_Type(Integer32):
    """Custom type bsnGlobalDot11b80211eMaxBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BsnGlobalDot11b80211eMaxBandwidth_Type.__name__ = "Integer32"
_BsnGlobalDot11b80211eMaxBandwidth_Object = MibScalar
bsnGlobalDot11b80211eMaxBandwidth = _BsnGlobalDot11b80211eMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 33),
    _BsnGlobalDot11b80211eMaxBandwidth_Type()
)
bsnGlobalDot11b80211eMaxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11b80211eMaxBandwidth.setStatus("current")


class _BsnGlobalDot11bDTPCSupport_Type(Integer32):
    """Custom type bsnGlobalDot11bDTPCSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnGlobalDot11bDTPCSupport_Type.__name__ = "Integer32"
_BsnGlobalDot11bDTPCSupport_Object = MibScalar
bsnGlobalDot11bDTPCSupport = _BsnGlobalDot11bDTPCSupport_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 34),
    _BsnGlobalDot11bDTPCSupport_Type()
)
bsnGlobalDot11bDTPCSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bDTPCSupport.setStatus("current")


class _BsnGlobalDot11bRxSopThreshold_Type(Integer32):
    """Custom type bsnGlobalDot11bRxSopThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("high", 3),
          ("low", 1),
          ("medium", 2))
    )


_BsnGlobalDot11bRxSopThreshold_Type.__name__ = "Integer32"
_BsnGlobalDot11bRxSopThreshold_Object = MibScalar
bsnGlobalDot11bRxSopThreshold = _BsnGlobalDot11bRxSopThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 1, 35),
    _BsnGlobalDot11bRxSopThreshold_Type()
)
bsnGlobalDot11bRxSopThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bRxSopThreshold.setStatus("current")
_BsnGlobalDot11bPhy_ObjectIdentity = ObjectIdentity
bsnGlobalDot11bPhy = _BsnGlobalDot11bPhy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 2)
)


class _BsnGlobalDot11bMediumOccupancyLimit_Type(Integer32):
    """Custom type bsnGlobalDot11bMediumOccupancyLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_BsnGlobalDot11bMediumOccupancyLimit_Type.__name__ = "Integer32"
_BsnGlobalDot11bMediumOccupancyLimit_Object = MibScalar
bsnGlobalDot11bMediumOccupancyLimit = _BsnGlobalDot11bMediumOccupancyLimit_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 2, 1),
    _BsnGlobalDot11bMediumOccupancyLimit_Type()
)
bsnGlobalDot11bMediumOccupancyLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11bMediumOccupancyLimit.setStatus("current")


class _BsnGlobalDot11bCFPPeriod_Type(Integer32):
    """Custom type bsnGlobalDot11bCFPPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BsnGlobalDot11bCFPPeriod_Type.__name__ = "Integer32"
_BsnGlobalDot11bCFPPeriod_Object = MibScalar
bsnGlobalDot11bCFPPeriod = _BsnGlobalDot11bCFPPeriod_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 2, 2),
    _BsnGlobalDot11bCFPPeriod_Type()
)
bsnGlobalDot11bCFPPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11bCFPPeriod.setStatus("current")


class _BsnGlobalDot11bCFPMaxDuration_Type(Integer32):
    """Custom type bsnGlobalDot11bCFPMaxDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BsnGlobalDot11bCFPMaxDuration_Type.__name__ = "Integer32"
_BsnGlobalDot11bCFPMaxDuration_Object = MibScalar
bsnGlobalDot11bCFPMaxDuration = _BsnGlobalDot11bCFPMaxDuration_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 2, 3),
    _BsnGlobalDot11bCFPMaxDuration_Type()
)
bsnGlobalDot11bCFPMaxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11bCFPMaxDuration.setStatus("current")


class _BsnGlobalDot11bCFPollable_Type(Integer32):
    """Custom type bsnGlobalDot11bCFPollable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_BsnGlobalDot11bCFPollable_Type.__name__ = "Integer32"
_BsnGlobalDot11bCFPollable_Object = MibScalar
bsnGlobalDot11bCFPollable = _BsnGlobalDot11bCFPollable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 2, 5),
    _BsnGlobalDot11bCFPollable_Type()
)
bsnGlobalDot11bCFPollable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11bCFPollable.setStatus("current")


class _BsnGlobalDot11bCFPollRequest_Type(Integer32):
    """Custom type bsnGlobalDot11bCFPollRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_BsnGlobalDot11bCFPollRequest_Type.__name__ = "Integer32"
_BsnGlobalDot11bCFPollRequest_Object = MibScalar
bsnGlobalDot11bCFPollRequest = _BsnGlobalDot11bCFPollRequest_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 2, 6),
    _BsnGlobalDot11bCFPollRequest_Type()
)
bsnGlobalDot11bCFPollRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11bCFPollRequest.setStatus("current")


class _BsnGlobalDot11bDTIMPeriod_Type(Integer32):
    """Custom type bsnGlobalDot11bDTIMPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BsnGlobalDot11bDTIMPeriod_Type.__name__ = "Integer32"
_BsnGlobalDot11bDTIMPeriod_Object = MibScalar
bsnGlobalDot11bDTIMPeriod = _BsnGlobalDot11bDTIMPeriod_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 2, 7),
    _BsnGlobalDot11bDTIMPeriod_Type()
)
bsnGlobalDot11bDTIMPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bDTIMPeriod.setStatus("current")
_BsnGlobalDot11bMaximumTransmitPowerLevel_Type = Integer32
_BsnGlobalDot11bMaximumTransmitPowerLevel_Object = MibScalar
bsnGlobalDot11bMaximumTransmitPowerLevel = _BsnGlobalDot11bMaximumTransmitPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 2, 8),
    _BsnGlobalDot11bMaximumTransmitPowerLevel_Type()
)
bsnGlobalDot11bMaximumTransmitPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11bMaximumTransmitPowerLevel.setStatus("deprecated")
_BsnGlobalDot11bFirstChannelNumber_Type = Integer32
_BsnGlobalDot11bFirstChannelNumber_Object = MibScalar
bsnGlobalDot11bFirstChannelNumber = _BsnGlobalDot11bFirstChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 2, 9),
    _BsnGlobalDot11bFirstChannelNumber_Type()
)
bsnGlobalDot11bFirstChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11bFirstChannelNumber.setStatus("deprecated")
_BsnGlobalDot11bNumberofChannels_Type = Integer32
_BsnGlobalDot11bNumberofChannels_Object = MibScalar
bsnGlobalDot11bNumberofChannels = _BsnGlobalDot11bNumberofChannels_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 2, 10),
    _BsnGlobalDot11bNumberofChannels_Type()
)
bsnGlobalDot11bNumberofChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11bNumberofChannels.setStatus("deprecated")


class _BsnGlobalDot11bRTSThreshold_Type(Integer32):
    """Custom type bsnGlobalDot11bRTSThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2347),
    )


_BsnGlobalDot11bRTSThreshold_Type.__name__ = "Integer32"
_BsnGlobalDot11bRTSThreshold_Object = MibScalar
bsnGlobalDot11bRTSThreshold = _BsnGlobalDot11bRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 2, 11),
    _BsnGlobalDot11bRTSThreshold_Type()
)
bsnGlobalDot11bRTSThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11bRTSThreshold.setStatus("current")


class _BsnGlobalDot11bShortRetryLimit_Type(Integer32):
    """Custom type bsnGlobalDot11bShortRetryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BsnGlobalDot11bShortRetryLimit_Type.__name__ = "Integer32"
_BsnGlobalDot11bShortRetryLimit_Object = MibScalar
bsnGlobalDot11bShortRetryLimit = _BsnGlobalDot11bShortRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 2, 12),
    _BsnGlobalDot11bShortRetryLimit_Type()
)
bsnGlobalDot11bShortRetryLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11bShortRetryLimit.setStatus("current")


class _BsnGlobalDot11bLongRetryLimit_Type(Integer32):
    """Custom type bsnGlobalDot11bLongRetryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BsnGlobalDot11bLongRetryLimit_Type.__name__ = "Integer32"
_BsnGlobalDot11bLongRetryLimit_Object = MibScalar
bsnGlobalDot11bLongRetryLimit = _BsnGlobalDot11bLongRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 2, 13),
    _BsnGlobalDot11bLongRetryLimit_Type()
)
bsnGlobalDot11bLongRetryLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11bLongRetryLimit.setStatus("current")


class _BsnGlobalDot11bFragmentationThreshold_Type(Integer32):
    """Custom type bsnGlobalDot11bFragmentationThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_BsnGlobalDot11bFragmentationThreshold_Type.__name__ = "Integer32"
_BsnGlobalDot11bFragmentationThreshold_Object = MibScalar
bsnGlobalDot11bFragmentationThreshold = _BsnGlobalDot11bFragmentationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 2, 14),
    _BsnGlobalDot11bFragmentationThreshold_Type()
)
bsnGlobalDot11bFragmentationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11bFragmentationThreshold.setStatus("current")


class _BsnGlobalDot11bMaxTransmitMSDULifetime_Type(Unsigned32):
    """Custom type bsnGlobalDot11bMaxTransmitMSDULifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_BsnGlobalDot11bMaxTransmitMSDULifetime_Type.__name__ = "Unsigned32"
_BsnGlobalDot11bMaxTransmitMSDULifetime_Object = MibScalar
bsnGlobalDot11bMaxTransmitMSDULifetime = _BsnGlobalDot11bMaxTransmitMSDULifetime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 2, 15),
    _BsnGlobalDot11bMaxTransmitMSDULifetime_Type()
)
bsnGlobalDot11bMaxTransmitMSDULifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11bMaxTransmitMSDULifetime.setStatus("current")


class _BsnGlobalDot11bMaxReceiveLifetime_Type(Unsigned32):
    """Custom type bsnGlobalDot11bMaxReceiveLifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_BsnGlobalDot11bMaxReceiveLifetime_Type.__name__ = "Unsigned32"
_BsnGlobalDot11bMaxReceiveLifetime_Object = MibScalar
bsnGlobalDot11bMaxReceiveLifetime = _BsnGlobalDot11bMaxReceiveLifetime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 2, 16),
    _BsnGlobalDot11bMaxReceiveLifetime_Type()
)
bsnGlobalDot11bMaxReceiveLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11bMaxReceiveLifetime.setStatus("current")
_BsnGlobalDot11bEDThreshold_Type = Integer32
_BsnGlobalDot11bEDThreshold_Object = MibScalar
bsnGlobalDot11bEDThreshold = _BsnGlobalDot11bEDThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 2, 17),
    _BsnGlobalDot11bEDThreshold_Type()
)
bsnGlobalDot11bEDThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11bEDThreshold.setStatus("current")


class _BsnGlobalDot11bChannelAgilityEnabled_Type(Integer32):
    """Custom type bsnGlobalDot11bChannelAgilityEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_BsnGlobalDot11bChannelAgilityEnabled_Type.__name__ = "Integer32"
_BsnGlobalDot11bChannelAgilityEnabled_Object = MibScalar
bsnGlobalDot11bChannelAgilityEnabled = _BsnGlobalDot11bChannelAgilityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 2, 18),
    _BsnGlobalDot11bChannelAgilityEnabled_Type()
)
bsnGlobalDot11bChannelAgilityEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11bChannelAgilityEnabled.setStatus("current")


class _BsnGlobalDot11bPBCCOptionImplemented_Type(Integer32):
    """Custom type bsnGlobalDot11bPBCCOptionImplemented based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_BsnGlobalDot11bPBCCOptionImplemented_Type.__name__ = "Integer32"
_BsnGlobalDot11bPBCCOptionImplemented_Object = MibScalar
bsnGlobalDot11bPBCCOptionImplemented = _BsnGlobalDot11bPBCCOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 2, 19),
    _BsnGlobalDot11bPBCCOptionImplemented_Type()
)
bsnGlobalDot11bPBCCOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11bPBCCOptionImplemented.setStatus("current")


class _BsnGlobalDot11bShortPreambleOptionImplemented_Type(Integer32):
    """Custom type bsnGlobalDot11bShortPreambleOptionImplemented based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_BsnGlobalDot11bShortPreambleOptionImplemented_Type.__name__ = "Integer32"
_BsnGlobalDot11bShortPreambleOptionImplemented_Object = MibScalar
bsnGlobalDot11bShortPreambleOptionImplemented = _BsnGlobalDot11bShortPreambleOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 2, 2, 20),
    _BsnGlobalDot11bShortPreambleOptionImplemented_Type()
)
bsnGlobalDot11bShortPreambleOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11bShortPreambleOptionImplemented.setStatus("current")
_BsnGlobalDot11a_ObjectIdentity = ObjectIdentity
bsnGlobalDot11a = _BsnGlobalDot11a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3)
)
_BsnGlobalDot11aConfig_ObjectIdentity = ObjectIdentity
bsnGlobalDot11aConfig = _BsnGlobalDot11aConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1)
)


class _BsnGlobalDot11aNetworkStatus_Type(Integer32):
    """Custom type bsnGlobalDot11aNetworkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnGlobalDot11aNetworkStatus_Type.__name__ = "Integer32"
_BsnGlobalDot11aNetworkStatus_Object = MibScalar
bsnGlobalDot11aNetworkStatus = _BsnGlobalDot11aNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 1),
    _BsnGlobalDot11aNetworkStatus_Type()
)
bsnGlobalDot11aNetworkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11aNetworkStatus.setStatus("current")


class _BsnGlobalDot11aLowBandNetwork_Type(Integer32):
    """Custom type bsnGlobalDot11aLowBandNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnGlobalDot11aLowBandNetwork_Type.__name__ = "Integer32"
_BsnGlobalDot11aLowBandNetwork_Object = MibScalar
bsnGlobalDot11aLowBandNetwork = _BsnGlobalDot11aLowBandNetwork_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 2),
    _BsnGlobalDot11aLowBandNetwork_Type()
)
bsnGlobalDot11aLowBandNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11aLowBandNetwork.setStatus("current")


class _BsnGlobalDot11aMediumBandNetwork_Type(Integer32):
    """Custom type bsnGlobalDot11aMediumBandNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnGlobalDot11aMediumBandNetwork_Type.__name__ = "Integer32"
_BsnGlobalDot11aMediumBandNetwork_Object = MibScalar
bsnGlobalDot11aMediumBandNetwork = _BsnGlobalDot11aMediumBandNetwork_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 3),
    _BsnGlobalDot11aMediumBandNetwork_Type()
)
bsnGlobalDot11aMediumBandNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11aMediumBandNetwork.setStatus("current")


class _BsnGlobalDot11aHighBandNetwork_Type(Integer32):
    """Custom type bsnGlobalDot11aHighBandNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnGlobalDot11aHighBandNetwork_Type.__name__ = "Integer32"
_BsnGlobalDot11aHighBandNetwork_Object = MibScalar
bsnGlobalDot11aHighBandNetwork = _BsnGlobalDot11aHighBandNetwork_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 4),
    _BsnGlobalDot11aHighBandNetwork_Type()
)
bsnGlobalDot11aHighBandNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11aHighBandNetwork.setStatus("current")


class _BsnGlobalDot11aBeaconPeriod_Type(Integer32):
    """Custom type bsnGlobalDot11aBeaconPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 1000),
    )


_BsnGlobalDot11aBeaconPeriod_Type.__name__ = "Integer32"
_BsnGlobalDot11aBeaconPeriod_Object = MibScalar
bsnGlobalDot11aBeaconPeriod = _BsnGlobalDot11aBeaconPeriod_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 5),
    _BsnGlobalDot11aBeaconPeriod_Type()
)
bsnGlobalDot11aBeaconPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11aBeaconPeriod.setStatus("current")


class _BsnGlobalDot11aDynamicChannelAssignment_Type(Integer32):
    """Custom type bsnGlobalDot11aDynamicChannelAssignment based on Integer32"""
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
        *(("automatic", 1),
          ("runOnce", 2),
          ("static", 3))
    )


_BsnGlobalDot11aDynamicChannelAssignment_Type.__name__ = "Integer32"
_BsnGlobalDot11aDynamicChannelAssignment_Object = MibScalar
bsnGlobalDot11aDynamicChannelAssignment = _BsnGlobalDot11aDynamicChannelAssignment_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 6),
    _BsnGlobalDot11aDynamicChannelAssignment_Type()
)
bsnGlobalDot11aDynamicChannelAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11aDynamicChannelAssignment.setStatus("current")


class _BsnGlobalDot11aCurrentChannel_Type(Integer32):
    """Custom type bsnGlobalDot11aCurrentChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_BsnGlobalDot11aCurrentChannel_Type.__name__ = "Integer32"
_BsnGlobalDot11aCurrentChannel_Object = MibScalar
bsnGlobalDot11aCurrentChannel = _BsnGlobalDot11aCurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 7),
    _BsnGlobalDot11aCurrentChannel_Type()
)
bsnGlobalDot11aCurrentChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11aCurrentChannel.setStatus("current")


class _BsnGlobalDot11aDynamicChannelUpdateInterval_Type(Unsigned32):
    """Custom type bsnGlobalDot11aDynamicChannelUpdateInterval based on Unsigned32"""
    defaultValue = 600


_BsnGlobalDot11aDynamicChannelUpdateInterval_Object = MibScalar
bsnGlobalDot11aDynamicChannelUpdateInterval = _BsnGlobalDot11aDynamicChannelUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 8),
    _BsnGlobalDot11aDynamicChannelUpdateInterval_Type()
)
bsnGlobalDot11aDynamicChannelUpdateInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11aDynamicChannelUpdateInterval.setStatus("current")


class _BsnGlobalDot11aInputsForDCA_Type(Unsigned32):
    """Custom type bsnGlobalDot11aInputsForDCA based on Unsigned32"""
    defaultValue = 63


_BsnGlobalDot11aInputsForDCA_Object = MibScalar
bsnGlobalDot11aInputsForDCA = _BsnGlobalDot11aInputsForDCA_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 9),
    _BsnGlobalDot11aInputsForDCA_Type()
)
bsnGlobalDot11aInputsForDCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11aInputsForDCA.setStatus("current")


class _BsnGlobalDot11aChannelUpdateCmdInvoke_Type(Integer32):
    """Custom type bsnGlobalDot11aChannelUpdateCmdInvoke based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("default", 0))
    )


_BsnGlobalDot11aChannelUpdateCmdInvoke_Type.__name__ = "Integer32"
_BsnGlobalDot11aChannelUpdateCmdInvoke_Object = MibScalar
bsnGlobalDot11aChannelUpdateCmdInvoke = _BsnGlobalDot11aChannelUpdateCmdInvoke_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 10),
    _BsnGlobalDot11aChannelUpdateCmdInvoke_Type()
)
bsnGlobalDot11aChannelUpdateCmdInvoke.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11aChannelUpdateCmdInvoke.setStatus("current")
_BsnGlobalDot11aChannelUpdateCmdStatus_Type = Integer32
_BsnGlobalDot11aChannelUpdateCmdStatus_Object = MibScalar
bsnGlobalDot11aChannelUpdateCmdStatus = _BsnGlobalDot11aChannelUpdateCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 11),
    _BsnGlobalDot11aChannelUpdateCmdStatus_Type()
)
bsnGlobalDot11aChannelUpdateCmdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11aChannelUpdateCmdStatus.setStatus("current")


class _BsnGlobalDot11aDynamicTransmitPowerControl_Type(Integer32):
    """Custom type bsnGlobalDot11aDynamicTransmitPowerControl based on Integer32"""
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
        *(("automatic", 1),
          ("runOnce", 2),
          ("static", 3))
    )


_BsnGlobalDot11aDynamicTransmitPowerControl_Type.__name__ = "Integer32"
_BsnGlobalDot11aDynamicTransmitPowerControl_Object = MibScalar
bsnGlobalDot11aDynamicTransmitPowerControl = _BsnGlobalDot11aDynamicTransmitPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 12),
    _BsnGlobalDot11aDynamicTransmitPowerControl_Type()
)
bsnGlobalDot11aDynamicTransmitPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11aDynamicTransmitPowerControl.setStatus("current")


class _BsnGlobalDot11aCurrentTxPowerLevel_Type(Integer32):
    """Custom type bsnGlobalDot11aCurrentTxPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_BsnGlobalDot11aCurrentTxPowerLevel_Type.__name__ = "Integer32"
_BsnGlobalDot11aCurrentTxPowerLevel_Object = MibScalar
bsnGlobalDot11aCurrentTxPowerLevel = _BsnGlobalDot11aCurrentTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 13),
    _BsnGlobalDot11aCurrentTxPowerLevel_Type()
)
bsnGlobalDot11aCurrentTxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11aCurrentTxPowerLevel.setStatus("current")


class _BsnGlobalDot11aDynamicTxPowerControlInterval_Type(Unsigned32):
    """Custom type bsnGlobalDot11aDynamicTxPowerControlInterval based on Unsigned32"""
    defaultValue = 600


_BsnGlobalDot11aDynamicTxPowerControlInterval_Object = MibScalar
bsnGlobalDot11aDynamicTxPowerControlInterval = _BsnGlobalDot11aDynamicTxPowerControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 14),
    _BsnGlobalDot11aDynamicTxPowerControlInterval_Type()
)
bsnGlobalDot11aDynamicTxPowerControlInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11aDynamicTxPowerControlInterval.setStatus("current")


class _BsnGlobalDot11aInputsForDTP_Type(Unsigned32):
    """Custom type bsnGlobalDot11aInputsForDTP based on Unsigned32"""
    defaultValue = 15


_BsnGlobalDot11aInputsForDTP_Object = MibScalar
bsnGlobalDot11aInputsForDTP = _BsnGlobalDot11aInputsForDTP_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 15),
    _BsnGlobalDot11aInputsForDTP_Type()
)
bsnGlobalDot11aInputsForDTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11aInputsForDTP.setStatus("current")


class _BsnGlobalDot11aPowerUpdateCmdInvoke_Type(Integer32):
    """Custom type bsnGlobalDot11aPowerUpdateCmdInvoke based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("default", 0))
    )


_BsnGlobalDot11aPowerUpdateCmdInvoke_Type.__name__ = "Integer32"
_BsnGlobalDot11aPowerUpdateCmdInvoke_Object = MibScalar
bsnGlobalDot11aPowerUpdateCmdInvoke = _BsnGlobalDot11aPowerUpdateCmdInvoke_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 16),
    _BsnGlobalDot11aPowerUpdateCmdInvoke_Type()
)
bsnGlobalDot11aPowerUpdateCmdInvoke.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11aPowerUpdateCmdInvoke.setStatus("current")
_BsnGlobalDot11aPowerUpdateCmdStatus_Type = Integer32
_BsnGlobalDot11aPowerUpdateCmdStatus_Object = MibScalar
bsnGlobalDot11aPowerUpdateCmdStatus = _BsnGlobalDot11aPowerUpdateCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 17),
    _BsnGlobalDot11aPowerUpdateCmdStatus_Type()
)
bsnGlobalDot11aPowerUpdateCmdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11aPowerUpdateCmdStatus.setStatus("current")


class _BsnGlobalDot11aDataRate6Mhz_Type(Integer32):
    """Custom type bsnGlobalDot11aDataRate6Mhz based on Integer32"""
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
          ("mandatory", 2),
          ("supported", 1))
    )


_BsnGlobalDot11aDataRate6Mhz_Type.__name__ = "Integer32"
_BsnGlobalDot11aDataRate6Mhz_Object = MibScalar
bsnGlobalDot11aDataRate6Mhz = _BsnGlobalDot11aDataRate6Mhz_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 19),
    _BsnGlobalDot11aDataRate6Mhz_Type()
)
bsnGlobalDot11aDataRate6Mhz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11aDataRate6Mhz.setStatus("current")


class _BsnGlobalDot11aDataRate9Mhz_Type(Integer32):
    """Custom type bsnGlobalDot11aDataRate9Mhz based on Integer32"""
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
          ("mandatory", 2),
          ("supported", 1))
    )


_BsnGlobalDot11aDataRate9Mhz_Type.__name__ = "Integer32"
_BsnGlobalDot11aDataRate9Mhz_Object = MibScalar
bsnGlobalDot11aDataRate9Mhz = _BsnGlobalDot11aDataRate9Mhz_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 20),
    _BsnGlobalDot11aDataRate9Mhz_Type()
)
bsnGlobalDot11aDataRate9Mhz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11aDataRate9Mhz.setStatus("current")


class _BsnGlobalDot11aDataRate12Mhz_Type(Integer32):
    """Custom type bsnGlobalDot11aDataRate12Mhz based on Integer32"""
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
          ("mandatory", 2),
          ("supported", 1))
    )


_BsnGlobalDot11aDataRate12Mhz_Type.__name__ = "Integer32"
_BsnGlobalDot11aDataRate12Mhz_Object = MibScalar
bsnGlobalDot11aDataRate12Mhz = _BsnGlobalDot11aDataRate12Mhz_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 21),
    _BsnGlobalDot11aDataRate12Mhz_Type()
)
bsnGlobalDot11aDataRate12Mhz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11aDataRate12Mhz.setStatus("current")


class _BsnGlobalDot11aDataRate18Mhz_Type(Integer32):
    """Custom type bsnGlobalDot11aDataRate18Mhz based on Integer32"""
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
          ("mandatory", 2),
          ("supported", 1))
    )


_BsnGlobalDot11aDataRate18Mhz_Type.__name__ = "Integer32"
_BsnGlobalDot11aDataRate18Mhz_Object = MibScalar
bsnGlobalDot11aDataRate18Mhz = _BsnGlobalDot11aDataRate18Mhz_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 22),
    _BsnGlobalDot11aDataRate18Mhz_Type()
)
bsnGlobalDot11aDataRate18Mhz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11aDataRate18Mhz.setStatus("current")


class _BsnGlobalDot11aDataRate24Mhz_Type(Integer32):
    """Custom type bsnGlobalDot11aDataRate24Mhz based on Integer32"""
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
          ("mandatory", 2),
          ("supported", 1))
    )


_BsnGlobalDot11aDataRate24Mhz_Type.__name__ = "Integer32"
_BsnGlobalDot11aDataRate24Mhz_Object = MibScalar
bsnGlobalDot11aDataRate24Mhz = _BsnGlobalDot11aDataRate24Mhz_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 23),
    _BsnGlobalDot11aDataRate24Mhz_Type()
)
bsnGlobalDot11aDataRate24Mhz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11aDataRate24Mhz.setStatus("current")


class _BsnGlobalDot11aDataRate36Mhz_Type(Integer32):
    """Custom type bsnGlobalDot11aDataRate36Mhz based on Integer32"""
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
          ("mandatory", 2),
          ("supported", 1))
    )


_BsnGlobalDot11aDataRate36Mhz_Type.__name__ = "Integer32"
_BsnGlobalDot11aDataRate36Mhz_Object = MibScalar
bsnGlobalDot11aDataRate36Mhz = _BsnGlobalDot11aDataRate36Mhz_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 24),
    _BsnGlobalDot11aDataRate36Mhz_Type()
)
bsnGlobalDot11aDataRate36Mhz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11aDataRate36Mhz.setStatus("current")


class _BsnGlobalDot11aDataRate48Mhz_Type(Integer32):
    """Custom type bsnGlobalDot11aDataRate48Mhz based on Integer32"""
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
          ("mandatory", 2),
          ("supported", 1))
    )


_BsnGlobalDot11aDataRate48Mhz_Type.__name__ = "Integer32"
_BsnGlobalDot11aDataRate48Mhz_Object = MibScalar
bsnGlobalDot11aDataRate48Mhz = _BsnGlobalDot11aDataRate48Mhz_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 25),
    _BsnGlobalDot11aDataRate48Mhz_Type()
)
bsnGlobalDot11aDataRate48Mhz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11aDataRate48Mhz.setStatus("current")


class _BsnGlobalDot11aDataRate54Mhz_Type(Integer32):
    """Custom type bsnGlobalDot11aDataRate54Mhz based on Integer32"""
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
          ("mandatory", 2),
          ("supported", 1))
    )


_BsnGlobalDot11aDataRate54Mhz_Type.__name__ = "Integer32"
_BsnGlobalDot11aDataRate54Mhz_Object = MibScalar
bsnGlobalDot11aDataRate54Mhz = _BsnGlobalDot11aDataRate54Mhz_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 26),
    _BsnGlobalDot11aDataRate54Mhz_Type()
)
bsnGlobalDot11aDataRate54Mhz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11aDataRate54Mhz.setStatus("current")


class _BsnGlobalDot11aPicoCellMode_Type(Integer32):
    """Custom type bsnGlobalDot11aPicoCellMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnGlobalDot11aPicoCellMode_Type.__name__ = "Integer32"
_BsnGlobalDot11aPicoCellMode_Object = MibScalar
bsnGlobalDot11aPicoCellMode = _BsnGlobalDot11aPicoCellMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 27),
    _BsnGlobalDot11aPicoCellMode_Type()
)
bsnGlobalDot11aPicoCellMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11aPicoCellMode.setStatus("current")


class _BsnGlobalDot11aFastRoamingMode_Type(Integer32):
    """Custom type bsnGlobalDot11aFastRoamingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnGlobalDot11aFastRoamingMode_Type.__name__ = "Integer32"
_BsnGlobalDot11aFastRoamingMode_Object = MibScalar
bsnGlobalDot11aFastRoamingMode = _BsnGlobalDot11aFastRoamingMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 28),
    _BsnGlobalDot11aFastRoamingMode_Type()
)
bsnGlobalDot11aFastRoamingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11aFastRoamingMode.setStatus("current")


class _BsnGlobalDot11aFastRoamingVoipMinRate_Type(Integer32):
    """Custom type bsnGlobalDot11aFastRoamingVoipMinRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("rate11Mbps", 4),
          ("rate1Mbps", 1),
          ("rate2Mbps", 2),
          ("rate5andHalfMbps", 3),
          ("undefined", 0))
    )


_BsnGlobalDot11aFastRoamingVoipMinRate_Type.__name__ = "Integer32"
_BsnGlobalDot11aFastRoamingVoipMinRate_Object = MibScalar
bsnGlobalDot11aFastRoamingVoipMinRate = _BsnGlobalDot11aFastRoamingVoipMinRate_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 29),
    _BsnGlobalDot11aFastRoamingVoipMinRate_Type()
)
bsnGlobalDot11aFastRoamingVoipMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11aFastRoamingVoipMinRate.setStatus("current")


class _BsnGlobalDot11aFastRoamingVoipPercentage_Type(Integer32):
    """Custom type bsnGlobalDot11aFastRoamingVoipPercentage based on Integer32"""
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
        *(("fifty", 3),
          ("hundred", 5),
          ("seventyfive", 4),
          ("twentyfive", 2),
          ("zero", 1))
    )


_BsnGlobalDot11aFastRoamingVoipPercentage_Type.__name__ = "Integer32"
_BsnGlobalDot11aFastRoamingVoipPercentage_Object = MibScalar
bsnGlobalDot11aFastRoamingVoipPercentage = _BsnGlobalDot11aFastRoamingVoipPercentage_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 30),
    _BsnGlobalDot11aFastRoamingVoipPercentage_Type()
)
bsnGlobalDot11aFastRoamingVoipPercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11aFastRoamingVoipPercentage.setStatus("current")


class _BsnGlobalDot11a80211eMaxBandwidth_Type(Integer32):
    """Custom type bsnGlobalDot11a80211eMaxBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BsnGlobalDot11a80211eMaxBandwidth_Type.__name__ = "Integer32"
_BsnGlobalDot11a80211eMaxBandwidth_Object = MibScalar
bsnGlobalDot11a80211eMaxBandwidth = _BsnGlobalDot11a80211eMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 31),
    _BsnGlobalDot11a80211eMaxBandwidth_Type()
)
bsnGlobalDot11a80211eMaxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11a80211eMaxBandwidth.setStatus("current")


class _BsnGlobalDot11aDTPCSupport_Type(Integer32):
    """Custom type bsnGlobalDot11aDTPCSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnGlobalDot11aDTPCSupport_Type.__name__ = "Integer32"
_BsnGlobalDot11aDTPCSupport_Object = MibScalar
bsnGlobalDot11aDTPCSupport = _BsnGlobalDot11aDTPCSupport_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 32),
    _BsnGlobalDot11aDTPCSupport_Type()
)
bsnGlobalDot11aDTPCSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11aDTPCSupport.setStatus("current")


class _BsnGlobalDot11aRxSopThreshold_Type(Integer32):
    """Custom type bsnGlobalDot11aRxSopThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("high", 3),
          ("low", 1),
          ("medium", 2))
    )


_BsnGlobalDot11aRxSopThreshold_Type.__name__ = "Integer32"
_BsnGlobalDot11aRxSopThreshold_Object = MibScalar
bsnGlobalDot11aRxSopThreshold = _BsnGlobalDot11aRxSopThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 1, 33),
    _BsnGlobalDot11aRxSopThreshold_Type()
)
bsnGlobalDot11aRxSopThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11aRxSopThreshold.setStatus("current")
_BsnGlobalDot11aPhy_ObjectIdentity = ObjectIdentity
bsnGlobalDot11aPhy = _BsnGlobalDot11aPhy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 2)
)


class _BsnGlobalDot11aMediumOccupancyLimit_Type(Integer32):
    """Custom type bsnGlobalDot11aMediumOccupancyLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_BsnGlobalDot11aMediumOccupancyLimit_Type.__name__ = "Integer32"
_BsnGlobalDot11aMediumOccupancyLimit_Object = MibScalar
bsnGlobalDot11aMediumOccupancyLimit = _BsnGlobalDot11aMediumOccupancyLimit_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 2, 1),
    _BsnGlobalDot11aMediumOccupancyLimit_Type()
)
bsnGlobalDot11aMediumOccupancyLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11aMediumOccupancyLimit.setStatus("current")


class _BsnGlobalDot11aCFPPeriod_Type(Integer32):
    """Custom type bsnGlobalDot11aCFPPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BsnGlobalDot11aCFPPeriod_Type.__name__ = "Integer32"
_BsnGlobalDot11aCFPPeriod_Object = MibScalar
bsnGlobalDot11aCFPPeriod = _BsnGlobalDot11aCFPPeriod_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 2, 2),
    _BsnGlobalDot11aCFPPeriod_Type()
)
bsnGlobalDot11aCFPPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11aCFPPeriod.setStatus("current")


class _BsnGlobalDot11aCFPMaxDuration_Type(Integer32):
    """Custom type bsnGlobalDot11aCFPMaxDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BsnGlobalDot11aCFPMaxDuration_Type.__name__ = "Integer32"
_BsnGlobalDot11aCFPMaxDuration_Object = MibScalar
bsnGlobalDot11aCFPMaxDuration = _BsnGlobalDot11aCFPMaxDuration_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 2, 3),
    _BsnGlobalDot11aCFPMaxDuration_Type()
)
bsnGlobalDot11aCFPMaxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11aCFPMaxDuration.setStatus("current")


class _BsnGlobalDot11aCFPollable_Type(Integer32):
    """Custom type bsnGlobalDot11aCFPollable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_BsnGlobalDot11aCFPollable_Type.__name__ = "Integer32"
_BsnGlobalDot11aCFPollable_Object = MibScalar
bsnGlobalDot11aCFPollable = _BsnGlobalDot11aCFPollable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 2, 5),
    _BsnGlobalDot11aCFPollable_Type()
)
bsnGlobalDot11aCFPollable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11aCFPollable.setStatus("current")


class _BsnGlobalDot11aCFPollRequest_Type(Integer32):
    """Custom type bsnGlobalDot11aCFPollRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_BsnGlobalDot11aCFPollRequest_Type.__name__ = "Integer32"
_BsnGlobalDot11aCFPollRequest_Object = MibScalar
bsnGlobalDot11aCFPollRequest = _BsnGlobalDot11aCFPollRequest_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 2, 6),
    _BsnGlobalDot11aCFPollRequest_Type()
)
bsnGlobalDot11aCFPollRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11aCFPollRequest.setStatus("current")


class _BsnGlobalDot11aDTIMPeriod_Type(Integer32):
    """Custom type bsnGlobalDot11aDTIMPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BsnGlobalDot11aDTIMPeriod_Type.__name__ = "Integer32"
_BsnGlobalDot11aDTIMPeriod_Object = MibScalar
bsnGlobalDot11aDTIMPeriod = _BsnGlobalDot11aDTIMPeriod_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 2, 7),
    _BsnGlobalDot11aDTIMPeriod_Type()
)
bsnGlobalDot11aDTIMPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11aDTIMPeriod.setStatus("current")
_BsnGlobalDot11aMaximumTransmitPowerLevel_Type = Integer32
_BsnGlobalDot11aMaximumTransmitPowerLevel_Object = MibScalar
bsnGlobalDot11aMaximumTransmitPowerLevel = _BsnGlobalDot11aMaximumTransmitPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 2, 8),
    _BsnGlobalDot11aMaximumTransmitPowerLevel_Type()
)
bsnGlobalDot11aMaximumTransmitPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11aMaximumTransmitPowerLevel.setStatus("deprecated")
_BsnGlobalDot11aFirstChannelNumber_Type = Integer32
_BsnGlobalDot11aFirstChannelNumber_Object = MibScalar
bsnGlobalDot11aFirstChannelNumber = _BsnGlobalDot11aFirstChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 2, 9),
    _BsnGlobalDot11aFirstChannelNumber_Type()
)
bsnGlobalDot11aFirstChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11aFirstChannelNumber.setStatus("deprecated")
_BsnGlobalDot11aNumberofChannels_Type = Integer32
_BsnGlobalDot11aNumberofChannels_Object = MibScalar
bsnGlobalDot11aNumberofChannels = _BsnGlobalDot11aNumberofChannels_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 2, 10),
    _BsnGlobalDot11aNumberofChannels_Type()
)
bsnGlobalDot11aNumberofChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11aNumberofChannels.setStatus("deprecated")


class _BsnGlobalDot11aRTSThreshold_Type(Integer32):
    """Custom type bsnGlobalDot11aRTSThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2347),
    )


_BsnGlobalDot11aRTSThreshold_Type.__name__ = "Integer32"
_BsnGlobalDot11aRTSThreshold_Object = MibScalar
bsnGlobalDot11aRTSThreshold = _BsnGlobalDot11aRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 2, 11),
    _BsnGlobalDot11aRTSThreshold_Type()
)
bsnGlobalDot11aRTSThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11aRTSThreshold.setStatus("current")


class _BsnGlobalDot11aShortRetryLimit_Type(Integer32):
    """Custom type bsnGlobalDot11aShortRetryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BsnGlobalDot11aShortRetryLimit_Type.__name__ = "Integer32"
_BsnGlobalDot11aShortRetryLimit_Object = MibScalar
bsnGlobalDot11aShortRetryLimit = _BsnGlobalDot11aShortRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 2, 12),
    _BsnGlobalDot11aShortRetryLimit_Type()
)
bsnGlobalDot11aShortRetryLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11aShortRetryLimit.setStatus("current")


class _BsnGlobalDot11aLongRetryLimit_Type(Integer32):
    """Custom type bsnGlobalDot11aLongRetryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BsnGlobalDot11aLongRetryLimit_Type.__name__ = "Integer32"
_BsnGlobalDot11aLongRetryLimit_Object = MibScalar
bsnGlobalDot11aLongRetryLimit = _BsnGlobalDot11aLongRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 2, 13),
    _BsnGlobalDot11aLongRetryLimit_Type()
)
bsnGlobalDot11aLongRetryLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11aLongRetryLimit.setStatus("current")


class _BsnGlobalDot11aFragmentationThreshold_Type(Integer32):
    """Custom type bsnGlobalDot11aFragmentationThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_BsnGlobalDot11aFragmentationThreshold_Type.__name__ = "Integer32"
_BsnGlobalDot11aFragmentationThreshold_Object = MibScalar
bsnGlobalDot11aFragmentationThreshold = _BsnGlobalDot11aFragmentationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 2, 14),
    _BsnGlobalDot11aFragmentationThreshold_Type()
)
bsnGlobalDot11aFragmentationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11aFragmentationThreshold.setStatus("current")


class _BsnGlobalDot11aMaxTransmitMSDULifetime_Type(Unsigned32):
    """Custom type bsnGlobalDot11aMaxTransmitMSDULifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_BsnGlobalDot11aMaxTransmitMSDULifetime_Type.__name__ = "Unsigned32"
_BsnGlobalDot11aMaxTransmitMSDULifetime_Object = MibScalar
bsnGlobalDot11aMaxTransmitMSDULifetime = _BsnGlobalDot11aMaxTransmitMSDULifetime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 2, 15),
    _BsnGlobalDot11aMaxTransmitMSDULifetime_Type()
)
bsnGlobalDot11aMaxTransmitMSDULifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11aMaxTransmitMSDULifetime.setStatus("current")


class _BsnGlobalDot11aMaxReceiveLifetime_Type(Unsigned32):
    """Custom type bsnGlobalDot11aMaxReceiveLifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_BsnGlobalDot11aMaxReceiveLifetime_Type.__name__ = "Unsigned32"
_BsnGlobalDot11aMaxReceiveLifetime_Object = MibScalar
bsnGlobalDot11aMaxReceiveLifetime = _BsnGlobalDot11aMaxReceiveLifetime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 2, 16),
    _BsnGlobalDot11aMaxReceiveLifetime_Type()
)
bsnGlobalDot11aMaxReceiveLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11aMaxReceiveLifetime.setStatus("current")
_BsnGlobalDot11aTIThreshold_Type = Integer32
_BsnGlobalDot11aTIThreshold_Object = MibScalar
bsnGlobalDot11aTIThreshold = _BsnGlobalDot11aTIThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 2, 17),
    _BsnGlobalDot11aTIThreshold_Type()
)
bsnGlobalDot11aTIThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11aTIThreshold.setStatus("current")


class _BsnGlobalDot11aChannelAgilityEnabled_Type(Integer32):
    """Custom type bsnGlobalDot11aChannelAgilityEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_BsnGlobalDot11aChannelAgilityEnabled_Type.__name__ = "Integer32"
_BsnGlobalDot11aChannelAgilityEnabled_Object = MibScalar
bsnGlobalDot11aChannelAgilityEnabled = _BsnGlobalDot11aChannelAgilityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 3, 2, 18),
    _BsnGlobalDot11aChannelAgilityEnabled_Type()
)
bsnGlobalDot11aChannelAgilityEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGlobalDot11aChannelAgilityEnabled.setStatus("current")
_BsnGlobalDot11h_ObjectIdentity = ObjectIdentity
bsnGlobalDot11h = _BsnGlobalDot11h_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 4)
)
_BsnGlobalDot11hConfig_ObjectIdentity = ObjectIdentity
bsnGlobalDot11hConfig = _BsnGlobalDot11hConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 4, 1)
)


class _BsnGlobalDot11hPowerConstraint_Type(Integer32):
    """Custom type bsnGlobalDot11hPowerConstraint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_BsnGlobalDot11hPowerConstraint_Type.__name__ = "Integer32"
_BsnGlobalDot11hPowerConstraint_Object = MibScalar
bsnGlobalDot11hPowerConstraint = _BsnGlobalDot11hPowerConstraint_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 4, 1, 1),
    _BsnGlobalDot11hPowerConstraint_Type()
)
bsnGlobalDot11hPowerConstraint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11hPowerConstraint.setStatus("current")
if mibBuilder.loadTexts:
    bsnGlobalDot11hPowerConstraint.setUnits("decibels")


class _BsnGlobalDot11hChannelSwitchEnable_Type(Integer32):
    """Custom type bsnGlobalDot11hChannelSwitchEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnGlobalDot11hChannelSwitchEnable_Type.__name__ = "Integer32"
_BsnGlobalDot11hChannelSwitchEnable_Object = MibScalar
bsnGlobalDot11hChannelSwitchEnable = _BsnGlobalDot11hChannelSwitchEnable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 4, 1, 2),
    _BsnGlobalDot11hChannelSwitchEnable_Type()
)
bsnGlobalDot11hChannelSwitchEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11hChannelSwitchEnable.setStatus("current")


class _BsnGlobalDot11hChannelSwitchMode_Type(Integer32):
    """Custom type bsnGlobalDot11hChannelSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loud", 0),
          ("quiet", 1))
    )


_BsnGlobalDot11hChannelSwitchMode_Type.__name__ = "Integer32"
_BsnGlobalDot11hChannelSwitchMode_Object = MibScalar
bsnGlobalDot11hChannelSwitchMode = _BsnGlobalDot11hChannelSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 3, 4, 1, 3),
    _BsnGlobalDot11hChannelSwitchMode_Type()
)
bsnGlobalDot11hChannelSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnGlobalDot11hChannelSwitchMode.setStatus("current")
_BsnRrm_ObjectIdentity = ObjectIdentity
bsnRrm = _BsnRrm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4)
)
_BsnRrmDot11a_ObjectIdentity = ObjectIdentity
bsnRrmDot11a = _BsnRrmDot11a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 1)
)
_BsnRrmDot11aGroup_ObjectIdentity = ObjectIdentity
bsnRrmDot11aGroup = _BsnRrmDot11aGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 1, 1)
)


class _BsnRrmDot11aGlobalAutomaticGrouping_Type(Integer32):
    """Custom type bsnRrmDot11aGlobalAutomaticGrouping based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("off", 2))
    )


_BsnRrmDot11aGlobalAutomaticGrouping_Type.__name__ = "Integer32"
_BsnRrmDot11aGlobalAutomaticGrouping_Object = MibScalar
bsnRrmDot11aGlobalAutomaticGrouping = _BsnRrmDot11aGlobalAutomaticGrouping_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 1, 1, 1),
    _BsnRrmDot11aGlobalAutomaticGrouping_Type()
)
bsnRrmDot11aGlobalAutomaticGrouping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11aGlobalAutomaticGrouping.setStatus("deprecated")
_BsnRrmDot11aGroupLeaderMacAddr_Type = MacAddress
_BsnRrmDot11aGroupLeaderMacAddr_Object = MibScalar
bsnRrmDot11aGroupLeaderMacAddr = _BsnRrmDot11aGroupLeaderMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 1, 1, 2),
    _BsnRrmDot11aGroupLeaderMacAddr_Type()
)
bsnRrmDot11aGroupLeaderMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRrmDot11aGroupLeaderMacAddr.setStatus("deprecated")


class _BsnRrmIsDot11aGroupLeader_Type(Integer32):
    """Custom type bsnRrmIsDot11aGroupLeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_BsnRrmIsDot11aGroupLeader_Type.__name__ = "Integer32"
_BsnRrmIsDot11aGroupLeader_Object = MibScalar
bsnRrmIsDot11aGroupLeader = _BsnRrmIsDot11aGroupLeader_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 1, 1, 3),
    _BsnRrmIsDot11aGroupLeader_Type()
)
bsnRrmIsDot11aGroupLeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRrmIsDot11aGroupLeader.setStatus("deprecated")
_BsnRrmDot11aGroupLastUpdateTime_Type = Unsigned32
_BsnRrmDot11aGroupLastUpdateTime_Object = MibScalar
bsnRrmDot11aGroupLastUpdateTime = _BsnRrmDot11aGroupLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 1, 1, 4),
    _BsnRrmDot11aGroupLastUpdateTime_Type()
)
bsnRrmDot11aGroupLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRrmDot11aGroupLastUpdateTime.setStatus("deprecated")


class _BsnRrmDot11aGlobalGroupInterval_Type(Unsigned32):
    """Custom type bsnRrmDot11aGlobalGroupInterval based on Unsigned32"""
    defaultValue = 3600


_BsnRrmDot11aGlobalGroupInterval_Object = MibScalar
bsnRrmDot11aGlobalGroupInterval = _BsnRrmDot11aGlobalGroupInterval_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 1, 1, 5),
    _BsnRrmDot11aGlobalGroupInterval_Type()
)
bsnRrmDot11aGlobalGroupInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRrmDot11aGlobalGroupInterval.setStatus("deprecated")
_BsnWrasDot11aGroupTable_Object = MibTable
bsnWrasDot11aGroupTable = _BsnWrasDot11aGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 1, 1, 9)
)
if mibBuilder.loadTexts:
    bsnWrasDot11aGroupTable.setStatus("deprecated")
_BsnWrasDot11aGroupEntry_Object = MibTableRow
bsnWrasDot11aGroupEntry = _BsnWrasDot11aGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 1, 1, 9, 1)
)
bsnWrasDot11aGroupEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnWrasDot11aPeerMacAddress"),
)
if mibBuilder.loadTexts:
    bsnWrasDot11aGroupEntry.setStatus("deprecated")
_BsnWrasDot11aPeerMacAddress_Type = MacAddress
_BsnWrasDot11aPeerMacAddress_Object = MibTableColumn
bsnWrasDot11aPeerMacAddress = _BsnWrasDot11aPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 1, 1, 9, 1, 1),
    _BsnWrasDot11aPeerMacAddress_Type()
)
bsnWrasDot11aPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnWrasDot11aPeerMacAddress.setStatus("deprecated")
_BsnWrasDot11aPeerIpAddress_Type = IpAddress
_BsnWrasDot11aPeerIpAddress_Object = MibTableColumn
bsnWrasDot11aPeerIpAddress = _BsnWrasDot11aPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 1, 1, 9, 1, 21),
    _BsnWrasDot11aPeerIpAddress_Type()
)
bsnWrasDot11aPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnWrasDot11aPeerIpAddress.setStatus("deprecated")
_BsnRrmDot11aAPDefault_ObjectIdentity = ObjectIdentity
bsnRrmDot11aAPDefault = _BsnRrmDot11aAPDefault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 1, 6)
)


class _BsnRrmDot11aForeignInterferenceThreshold_Type(Integer32):
    """Custom type bsnRrmDot11aForeignInterferenceThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BsnRrmDot11aForeignInterferenceThreshold_Type.__name__ = "Integer32"
_BsnRrmDot11aForeignInterferenceThreshold_Object = MibScalar
bsnRrmDot11aForeignInterferenceThreshold = _BsnRrmDot11aForeignInterferenceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 1, 6, 1),
    _BsnRrmDot11aForeignInterferenceThreshold_Type()
)
bsnRrmDot11aForeignInterferenceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11aForeignInterferenceThreshold.setStatus("current")


class _BsnRrmDot11aForeignNoiseThreshold_Type(Integer32):
    """Custom type bsnRrmDot11aForeignNoiseThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 0),
    )


_BsnRrmDot11aForeignNoiseThreshold_Type.__name__ = "Integer32"
_BsnRrmDot11aForeignNoiseThreshold_Object = MibScalar
bsnRrmDot11aForeignNoiseThreshold = _BsnRrmDot11aForeignNoiseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 1, 6, 2),
    _BsnRrmDot11aForeignNoiseThreshold_Type()
)
bsnRrmDot11aForeignNoiseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11aForeignNoiseThreshold.setStatus("current")


class _BsnRrmDot11aRFUtilizationThreshold_Type(Integer32):
    """Custom type bsnRrmDot11aRFUtilizationThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BsnRrmDot11aRFUtilizationThreshold_Type.__name__ = "Integer32"
_BsnRrmDot11aRFUtilizationThreshold_Object = MibScalar
bsnRrmDot11aRFUtilizationThreshold = _BsnRrmDot11aRFUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 1, 6, 3),
    _BsnRrmDot11aRFUtilizationThreshold_Type()
)
bsnRrmDot11aRFUtilizationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11aRFUtilizationThreshold.setStatus("current")


class _BsnRrmDot11aThroughputThreshold_Type(Unsigned32):
    """Custom type bsnRrmDot11aThroughputThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 1000000),
    )


_BsnRrmDot11aThroughputThreshold_Type.__name__ = "Unsigned32"
_BsnRrmDot11aThroughputThreshold_Object = MibScalar
bsnRrmDot11aThroughputThreshold = _BsnRrmDot11aThroughputThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 1, 6, 4),
    _BsnRrmDot11aThroughputThreshold_Type()
)
bsnRrmDot11aThroughputThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11aThroughputThreshold.setStatus("current")


class _BsnRrmDot11aMobilesThreshold_Type(Integer32):
    """Custom type bsnRrmDot11aMobilesThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 75),
    )


_BsnRrmDot11aMobilesThreshold_Type.__name__ = "Integer32"
_BsnRrmDot11aMobilesThreshold_Object = MibScalar
bsnRrmDot11aMobilesThreshold = _BsnRrmDot11aMobilesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 1, 6, 5),
    _BsnRrmDot11aMobilesThreshold_Type()
)
bsnRrmDot11aMobilesThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11aMobilesThreshold.setStatus("current")


class _BsnRrmDot11aCoverageThreshold_Type(Integer32):
    """Custom type bsnRrmDot11aCoverageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 50),
    )


_BsnRrmDot11aCoverageThreshold_Type.__name__ = "Integer32"
_BsnRrmDot11aCoverageThreshold_Object = MibScalar
bsnRrmDot11aCoverageThreshold = _BsnRrmDot11aCoverageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 1, 6, 6),
    _BsnRrmDot11aCoverageThreshold_Type()
)
bsnRrmDot11aCoverageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11aCoverageThreshold.setStatus("current")


class _BsnRrmDot11aMobileMinExceptionLevel_Type(Integer32):
    """Custom type bsnRrmDot11aMobileMinExceptionLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 75),
    )


_BsnRrmDot11aMobileMinExceptionLevel_Type.__name__ = "Integer32"
_BsnRrmDot11aMobileMinExceptionLevel_Object = MibScalar
bsnRrmDot11aMobileMinExceptionLevel = _BsnRrmDot11aMobileMinExceptionLevel_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 1, 6, 7),
    _BsnRrmDot11aMobileMinExceptionLevel_Type()
)
bsnRrmDot11aMobileMinExceptionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11aMobileMinExceptionLevel.setStatus("current")


class _BsnRrmDot11aCoverageExceptionLevel_Type(Integer32):
    """Custom type bsnRrmDot11aCoverageExceptionLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BsnRrmDot11aCoverageExceptionLevel_Type.__name__ = "Integer32"
_BsnRrmDot11aCoverageExceptionLevel_Object = MibScalar
bsnRrmDot11aCoverageExceptionLevel = _BsnRrmDot11aCoverageExceptionLevel_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 1, 6, 8),
    _BsnRrmDot11aCoverageExceptionLevel_Type()
)
bsnRrmDot11aCoverageExceptionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11aCoverageExceptionLevel.setStatus("current")


class _BsnRrmDot11aSignalMeasurementInterval_Type(Unsigned32):
    """Custom type bsnRrmDot11aSignalMeasurementInterval based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_BsnRrmDot11aSignalMeasurementInterval_Type.__name__ = "Unsigned32"
_BsnRrmDot11aSignalMeasurementInterval_Object = MibScalar
bsnRrmDot11aSignalMeasurementInterval = _BsnRrmDot11aSignalMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 1, 6, 9),
    _BsnRrmDot11aSignalMeasurementInterval_Type()
)
bsnRrmDot11aSignalMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11aSignalMeasurementInterval.setStatus("current")


class _BsnRrmDot11aNoiseMeasurementInterval_Type(Unsigned32):
    """Custom type bsnRrmDot11aNoiseMeasurementInterval based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_BsnRrmDot11aNoiseMeasurementInterval_Type.__name__ = "Unsigned32"
_BsnRrmDot11aNoiseMeasurementInterval_Object = MibScalar
bsnRrmDot11aNoiseMeasurementInterval = _BsnRrmDot11aNoiseMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 1, 6, 10),
    _BsnRrmDot11aNoiseMeasurementInterval_Type()
)
bsnRrmDot11aNoiseMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11aNoiseMeasurementInterval.setStatus("current")


class _BsnRrmDot11aLoadMeasurementInterval_Type(Unsigned32):
    """Custom type bsnRrmDot11aLoadMeasurementInterval based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_BsnRrmDot11aLoadMeasurementInterval_Type.__name__ = "Unsigned32"
_BsnRrmDot11aLoadMeasurementInterval_Object = MibScalar
bsnRrmDot11aLoadMeasurementInterval = _BsnRrmDot11aLoadMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 1, 6, 11),
    _BsnRrmDot11aLoadMeasurementInterval_Type()
)
bsnRrmDot11aLoadMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11aLoadMeasurementInterval.setStatus("current")


class _BsnRrmDot11aCoverageMeasurementInterval_Type(Unsigned32):
    """Custom type bsnRrmDot11aCoverageMeasurementInterval based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_BsnRrmDot11aCoverageMeasurementInterval_Type.__name__ = "Unsigned32"
_BsnRrmDot11aCoverageMeasurementInterval_Object = MibScalar
bsnRrmDot11aCoverageMeasurementInterval = _BsnRrmDot11aCoverageMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 1, 6, 12),
    _BsnRrmDot11aCoverageMeasurementInterval_Type()
)
bsnRrmDot11aCoverageMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11aCoverageMeasurementInterval.setStatus("current")


class _BsnRrmDot11aChannelMonitorList_Type(Integer32):
    """Custom type bsnRrmDot11aChannelMonitorList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("country", 2),
          ("dca", 3))
    )


_BsnRrmDot11aChannelMonitorList_Type.__name__ = "Integer32"
_BsnRrmDot11aChannelMonitorList_Object = MibScalar
bsnRrmDot11aChannelMonitorList = _BsnRrmDot11aChannelMonitorList_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 1, 6, 13),
    _BsnRrmDot11aChannelMonitorList_Type()
)
bsnRrmDot11aChannelMonitorList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11aChannelMonitorList.setStatus("current")


class _BsnRrmDot11aSetFactoryDefault_Type(Integer32):
    """Custom type bsnRrmDot11aSetFactoryDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("default", 0))
    )


_BsnRrmDot11aSetFactoryDefault_Type.__name__ = "Integer32"
_BsnRrmDot11aSetFactoryDefault_Object = MibScalar
bsnRrmDot11aSetFactoryDefault = _BsnRrmDot11aSetFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 1, 7),
    _BsnRrmDot11aSetFactoryDefault_Type()
)
bsnRrmDot11aSetFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11aSetFactoryDefault.setStatus("current")
_BsnRrmDot11b_ObjectIdentity = ObjectIdentity
bsnRrmDot11b = _BsnRrmDot11b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 2)
)
_BsnRrmDot11bGroup_ObjectIdentity = ObjectIdentity
bsnRrmDot11bGroup = _BsnRrmDot11bGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 2, 1)
)


class _BsnRrmDot11bGlobalAutomaticGrouping_Type(Integer32):
    """Custom type bsnRrmDot11bGlobalAutomaticGrouping based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("off", 2))
    )


_BsnRrmDot11bGlobalAutomaticGrouping_Type.__name__ = "Integer32"
_BsnRrmDot11bGlobalAutomaticGrouping_Object = MibScalar
bsnRrmDot11bGlobalAutomaticGrouping = _BsnRrmDot11bGlobalAutomaticGrouping_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 2, 1, 1),
    _BsnRrmDot11bGlobalAutomaticGrouping_Type()
)
bsnRrmDot11bGlobalAutomaticGrouping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11bGlobalAutomaticGrouping.setStatus("deprecated")
_BsnRrmDot11bGroupLeaderMacAddr_Type = MacAddress
_BsnRrmDot11bGroupLeaderMacAddr_Object = MibScalar
bsnRrmDot11bGroupLeaderMacAddr = _BsnRrmDot11bGroupLeaderMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 2, 1, 2),
    _BsnRrmDot11bGroupLeaderMacAddr_Type()
)
bsnRrmDot11bGroupLeaderMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRrmDot11bGroupLeaderMacAddr.setStatus("deprecated")


class _BsnRrmIsDot11bGroupLeader_Type(Integer32):
    """Custom type bsnRrmIsDot11bGroupLeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_BsnRrmIsDot11bGroupLeader_Type.__name__ = "Integer32"
_BsnRrmIsDot11bGroupLeader_Object = MibScalar
bsnRrmIsDot11bGroupLeader = _BsnRrmIsDot11bGroupLeader_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 2, 1, 3),
    _BsnRrmIsDot11bGroupLeader_Type()
)
bsnRrmIsDot11bGroupLeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRrmIsDot11bGroupLeader.setStatus("deprecated")
_BsnRrmDot11bGroupLastUpdateTime_Type = Unsigned32
_BsnRrmDot11bGroupLastUpdateTime_Object = MibScalar
bsnRrmDot11bGroupLastUpdateTime = _BsnRrmDot11bGroupLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 2, 1, 4),
    _BsnRrmDot11bGroupLastUpdateTime_Type()
)
bsnRrmDot11bGroupLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRrmDot11bGroupLastUpdateTime.setStatus("deprecated")


class _BsnRrmDot11bGlobalGroupInterval_Type(Unsigned32):
    """Custom type bsnRrmDot11bGlobalGroupInterval based on Unsigned32"""
    defaultValue = 3600


_BsnRrmDot11bGlobalGroupInterval_Object = MibScalar
bsnRrmDot11bGlobalGroupInterval = _BsnRrmDot11bGlobalGroupInterval_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 2, 1, 5),
    _BsnRrmDot11bGlobalGroupInterval_Type()
)
bsnRrmDot11bGlobalGroupInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRrmDot11bGlobalGroupInterval.setStatus("deprecated")
_BsnWrasDot11bGroupTable_Object = MibTable
bsnWrasDot11bGroupTable = _BsnWrasDot11bGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 2, 1, 9)
)
if mibBuilder.loadTexts:
    bsnWrasDot11bGroupTable.setStatus("deprecated")
_BsnWrasDot11bGroupEntry_Object = MibTableRow
bsnWrasDot11bGroupEntry = _BsnWrasDot11bGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 2, 1, 9, 1)
)
bsnWrasDot11bGroupEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnWrasDot11bPeerMacAddress"),
)
if mibBuilder.loadTexts:
    bsnWrasDot11bGroupEntry.setStatus("deprecated")
_BsnWrasDot11bPeerMacAddress_Type = MacAddress
_BsnWrasDot11bPeerMacAddress_Object = MibTableColumn
bsnWrasDot11bPeerMacAddress = _BsnWrasDot11bPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 2, 1, 9, 1, 1),
    _BsnWrasDot11bPeerMacAddress_Type()
)
bsnWrasDot11bPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnWrasDot11bPeerMacAddress.setStatus("deprecated")
_BsnWrasDot11bPeerIpAddress_Type = IpAddress
_BsnWrasDot11bPeerIpAddress_Object = MibTableColumn
bsnWrasDot11bPeerIpAddress = _BsnWrasDot11bPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 2, 1, 9, 1, 21),
    _BsnWrasDot11bPeerIpAddress_Type()
)
bsnWrasDot11bPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnWrasDot11bPeerIpAddress.setStatus("deprecated")
_BsnRrmDot11bAPDefault_ObjectIdentity = ObjectIdentity
bsnRrmDot11bAPDefault = _BsnRrmDot11bAPDefault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 2, 6)
)


class _BsnRrmDot11bForeignInterferenceThreshold_Type(Integer32):
    """Custom type bsnRrmDot11bForeignInterferenceThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BsnRrmDot11bForeignInterferenceThreshold_Type.__name__ = "Integer32"
_BsnRrmDot11bForeignInterferenceThreshold_Object = MibScalar
bsnRrmDot11bForeignInterferenceThreshold = _BsnRrmDot11bForeignInterferenceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 2, 6, 1),
    _BsnRrmDot11bForeignInterferenceThreshold_Type()
)
bsnRrmDot11bForeignInterferenceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11bForeignInterferenceThreshold.setStatus("current")


class _BsnRrmDot11bForeignNoiseThreshold_Type(Integer32):
    """Custom type bsnRrmDot11bForeignNoiseThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 0),
    )


_BsnRrmDot11bForeignNoiseThreshold_Type.__name__ = "Integer32"
_BsnRrmDot11bForeignNoiseThreshold_Object = MibScalar
bsnRrmDot11bForeignNoiseThreshold = _BsnRrmDot11bForeignNoiseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 2, 6, 2),
    _BsnRrmDot11bForeignNoiseThreshold_Type()
)
bsnRrmDot11bForeignNoiseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11bForeignNoiseThreshold.setStatus("current")


class _BsnRrmDot11bRFUtilizationThreshold_Type(Integer32):
    """Custom type bsnRrmDot11bRFUtilizationThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BsnRrmDot11bRFUtilizationThreshold_Type.__name__ = "Integer32"
_BsnRrmDot11bRFUtilizationThreshold_Object = MibScalar
bsnRrmDot11bRFUtilizationThreshold = _BsnRrmDot11bRFUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 2, 6, 3),
    _BsnRrmDot11bRFUtilizationThreshold_Type()
)
bsnRrmDot11bRFUtilizationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11bRFUtilizationThreshold.setStatus("current")


class _BsnRrmDot11bThroughputThreshold_Type(Unsigned32):
    """Custom type bsnRrmDot11bThroughputThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 1000000),
    )


_BsnRrmDot11bThroughputThreshold_Type.__name__ = "Unsigned32"
_BsnRrmDot11bThroughputThreshold_Object = MibScalar
bsnRrmDot11bThroughputThreshold = _BsnRrmDot11bThroughputThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 2, 6, 4),
    _BsnRrmDot11bThroughputThreshold_Type()
)
bsnRrmDot11bThroughputThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11bThroughputThreshold.setStatus("current")


class _BsnRrmDot11bMobilesThreshold_Type(Integer32):
    """Custom type bsnRrmDot11bMobilesThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 75),
    )


_BsnRrmDot11bMobilesThreshold_Type.__name__ = "Integer32"
_BsnRrmDot11bMobilesThreshold_Object = MibScalar
bsnRrmDot11bMobilesThreshold = _BsnRrmDot11bMobilesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 2, 6, 5),
    _BsnRrmDot11bMobilesThreshold_Type()
)
bsnRrmDot11bMobilesThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11bMobilesThreshold.setStatus("current")


class _BsnRrmDot11bCoverageThreshold_Type(Integer32):
    """Custom type bsnRrmDot11bCoverageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 50),
    )


_BsnRrmDot11bCoverageThreshold_Type.__name__ = "Integer32"
_BsnRrmDot11bCoverageThreshold_Object = MibScalar
bsnRrmDot11bCoverageThreshold = _BsnRrmDot11bCoverageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 2, 6, 6),
    _BsnRrmDot11bCoverageThreshold_Type()
)
bsnRrmDot11bCoverageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11bCoverageThreshold.setStatus("current")


class _BsnRrmDot11bMobileMinExceptionLevel_Type(Integer32):
    """Custom type bsnRrmDot11bMobileMinExceptionLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 75),
    )


_BsnRrmDot11bMobileMinExceptionLevel_Type.__name__ = "Integer32"
_BsnRrmDot11bMobileMinExceptionLevel_Object = MibScalar
bsnRrmDot11bMobileMinExceptionLevel = _BsnRrmDot11bMobileMinExceptionLevel_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 2, 6, 7),
    _BsnRrmDot11bMobileMinExceptionLevel_Type()
)
bsnRrmDot11bMobileMinExceptionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11bMobileMinExceptionLevel.setStatus("current")


class _BsnRrmDot11bCoverageExceptionLevel_Type(Integer32):
    """Custom type bsnRrmDot11bCoverageExceptionLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BsnRrmDot11bCoverageExceptionLevel_Type.__name__ = "Integer32"
_BsnRrmDot11bCoverageExceptionLevel_Object = MibScalar
bsnRrmDot11bCoverageExceptionLevel = _BsnRrmDot11bCoverageExceptionLevel_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 2, 6, 8),
    _BsnRrmDot11bCoverageExceptionLevel_Type()
)
bsnRrmDot11bCoverageExceptionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11bCoverageExceptionLevel.setStatus("current")


class _BsnRrmDot11bSignalMeasurementInterval_Type(Unsigned32):
    """Custom type bsnRrmDot11bSignalMeasurementInterval based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_BsnRrmDot11bSignalMeasurementInterval_Type.__name__ = "Unsigned32"
_BsnRrmDot11bSignalMeasurementInterval_Object = MibScalar
bsnRrmDot11bSignalMeasurementInterval = _BsnRrmDot11bSignalMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 2, 6, 9),
    _BsnRrmDot11bSignalMeasurementInterval_Type()
)
bsnRrmDot11bSignalMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11bSignalMeasurementInterval.setStatus("current")


class _BsnRrmDot11bNoiseMeasurementInterval_Type(Unsigned32):
    """Custom type bsnRrmDot11bNoiseMeasurementInterval based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_BsnRrmDot11bNoiseMeasurementInterval_Type.__name__ = "Unsigned32"
_BsnRrmDot11bNoiseMeasurementInterval_Object = MibScalar
bsnRrmDot11bNoiseMeasurementInterval = _BsnRrmDot11bNoiseMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 2, 6, 10),
    _BsnRrmDot11bNoiseMeasurementInterval_Type()
)
bsnRrmDot11bNoiseMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11bNoiseMeasurementInterval.setStatus("current")


class _BsnRrmDot11bLoadMeasurementInterval_Type(Unsigned32):
    """Custom type bsnRrmDot11bLoadMeasurementInterval based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_BsnRrmDot11bLoadMeasurementInterval_Type.__name__ = "Unsigned32"
_BsnRrmDot11bLoadMeasurementInterval_Object = MibScalar
bsnRrmDot11bLoadMeasurementInterval = _BsnRrmDot11bLoadMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 2, 6, 11),
    _BsnRrmDot11bLoadMeasurementInterval_Type()
)
bsnRrmDot11bLoadMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11bLoadMeasurementInterval.setStatus("current")


class _BsnRrmDot11bCoverageMeasurementInterval_Type(Unsigned32):
    """Custom type bsnRrmDot11bCoverageMeasurementInterval based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_BsnRrmDot11bCoverageMeasurementInterval_Type.__name__ = "Unsigned32"
_BsnRrmDot11bCoverageMeasurementInterval_Object = MibScalar
bsnRrmDot11bCoverageMeasurementInterval = _BsnRrmDot11bCoverageMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 2, 6, 12),
    _BsnRrmDot11bCoverageMeasurementInterval_Type()
)
bsnRrmDot11bCoverageMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11bCoverageMeasurementInterval.setStatus("current")


class _BsnRrmDot11bChannelMonitorList_Type(Integer32):
    """Custom type bsnRrmDot11bChannelMonitorList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("country", 2),
          ("dca", 3))
    )


_BsnRrmDot11bChannelMonitorList_Type.__name__ = "Integer32"
_BsnRrmDot11bChannelMonitorList_Object = MibScalar
bsnRrmDot11bChannelMonitorList = _BsnRrmDot11bChannelMonitorList_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 2, 6, 13),
    _BsnRrmDot11bChannelMonitorList_Type()
)
bsnRrmDot11bChannelMonitorList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11bChannelMonitorList.setStatus("current")


class _BsnRrmDot11bSetFactoryDefault_Type(Integer32):
    """Custom type bsnRrmDot11bSetFactoryDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("default", 0))
    )


_BsnRrmDot11bSetFactoryDefault_Type.__name__ = "Integer32"
_BsnRrmDot11bSetFactoryDefault_Object = MibScalar
bsnRrmDot11bSetFactoryDefault = _BsnRrmDot11bSetFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 4, 2, 7),
    _BsnRrmDot11bSetFactoryDefault_Type()
)
bsnRrmDot11bSetFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRrmDot11bSetFactoryDefault.setStatus("current")
_BsnAAA_ObjectIdentity = ObjectIdentity
bsnAAA = _BsnAAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5)
)
_BsnRadiusAuthServerTable_Object = MibTable
bsnRadiusAuthServerTable = _BsnRadiusAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 1)
)
if mibBuilder.loadTexts:
    bsnRadiusAuthServerTable.setStatus("current")
_BsnRadiusAuthServerEntry_Object = MibTableRow
bsnRadiusAuthServerEntry = _BsnRadiusAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 1, 1)
)
bsnRadiusAuthServerEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerIndex"),
)
if mibBuilder.loadTexts:
    bsnRadiusAuthServerEntry.setStatus("current")


class _BsnRadiusAuthServerIndex_Type(Integer32):
    """Custom type bsnRadiusAuthServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 17),
    )


_BsnRadiusAuthServerIndex_Type.__name__ = "Integer32"
_BsnRadiusAuthServerIndex_Object = MibTableColumn
bsnRadiusAuthServerIndex = _BsnRadiusAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 1, 1, 1),
    _BsnRadiusAuthServerIndex_Type()
)
bsnRadiusAuthServerIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAuthServerIndex.setStatus("current")
_BsnRadiusAuthServerAddress_Type = IpAddress
_BsnRadiusAuthServerAddress_Object = MibTableColumn
bsnRadiusAuthServerAddress = _BsnRadiusAuthServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 1, 1, 2),
    _BsnRadiusAuthServerAddress_Type()
)
bsnRadiusAuthServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAuthServerAddress.setStatus("deprecated")


class _BsnRadiusAuthClientServerPortNumber_Type(Integer32):
    """Custom type bsnRadiusAuthClientServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BsnRadiusAuthClientServerPortNumber_Type.__name__ = "Integer32"
_BsnRadiusAuthClientServerPortNumber_Object = MibTableColumn
bsnRadiusAuthClientServerPortNumber = _BsnRadiusAuthClientServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 1, 1, 3),
    _BsnRadiusAuthClientServerPortNumber_Type()
)
bsnRadiusAuthClientServerPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAuthClientServerPortNumber.setStatus("current")


class _BsnRadiusAuthServerKey_Type(OctetString):
    """Custom type bsnRadiusAuthServerKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BsnRadiusAuthServerKey_Type.__name__ = "OctetString"
_BsnRadiusAuthServerKey_Object = MibTableColumn
bsnRadiusAuthServerKey = _BsnRadiusAuthServerKey_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 1, 1, 4),
    _BsnRadiusAuthServerKey_Type()
)
bsnRadiusAuthServerKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAuthServerKey.setStatus("current")


class _BsnRadiusAuthServerStatus_Type(Integer32):
    """Custom type bsnRadiusAuthServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnRadiusAuthServerStatus_Type.__name__ = "Integer32"
_BsnRadiusAuthServerStatus_Object = MibTableColumn
bsnRadiusAuthServerStatus = _BsnRadiusAuthServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 1, 1, 5),
    _BsnRadiusAuthServerStatus_Type()
)
bsnRadiusAuthServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAuthServerStatus.setStatus("current")


class _BsnRadiusAuthServerKeyFormat_Type(Integer32):
    """Custom type bsnRadiusAuthServerKeyFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 2),
          ("hex", 1))
    )


_BsnRadiusAuthServerKeyFormat_Type.__name__ = "Integer32"
_BsnRadiusAuthServerKeyFormat_Object = MibTableColumn
bsnRadiusAuthServerKeyFormat = _BsnRadiusAuthServerKeyFormat_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 1, 1, 6),
    _BsnRadiusAuthServerKeyFormat_Type()
)
bsnRadiusAuthServerKeyFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAuthServerKeyFormat.setStatus("current")


class _BsnRadiusAuthServerRFC3576_Type(Integer32):
    """Custom type bsnRadiusAuthServerRFC3576 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnRadiusAuthServerRFC3576_Type.__name__ = "Integer32"
_BsnRadiusAuthServerRFC3576_Object = MibTableColumn
bsnRadiusAuthServerRFC3576 = _BsnRadiusAuthServerRFC3576_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 1, 1, 7),
    _BsnRadiusAuthServerRFC3576_Type()
)
bsnRadiusAuthServerRFC3576.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAuthServerRFC3576.setStatus("current")


class _BsnRadiusAuthServerIPSec_Type(Integer32):
    """Custom type bsnRadiusAuthServerIPSec based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnRadiusAuthServerIPSec_Type.__name__ = "Integer32"
_BsnRadiusAuthServerIPSec_Object = MibTableColumn
bsnRadiusAuthServerIPSec = _BsnRadiusAuthServerIPSec_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 1, 1, 8),
    _BsnRadiusAuthServerIPSec_Type()
)
bsnRadiusAuthServerIPSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAuthServerIPSec.setStatus("current")


class _BsnRadiusAuthServerIPSecAuth_Type(Integer32):
    """Custom type bsnRadiusAuthServerIPSecAuth based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hmacMd5", 1),
          ("hmacSha1", 2),
          ("none", 0))
    )


_BsnRadiusAuthServerIPSecAuth_Type.__name__ = "Integer32"
_BsnRadiusAuthServerIPSecAuth_Object = MibTableColumn
bsnRadiusAuthServerIPSecAuth = _BsnRadiusAuthServerIPSecAuth_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 1, 1, 9),
    _BsnRadiusAuthServerIPSecAuth_Type()
)
bsnRadiusAuthServerIPSecAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAuthServerIPSecAuth.setStatus("current")


class _BsnRadiusAuthServerIPSecEncryption_Type(Integer32):
    """Custom type bsnRadiusAuthServerIPSecEncryption based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("aes256Cbc", 4),
          ("aesCbc", 3),
          ("des", 1),
          ("none", 0),
          ("tripleDes", 2))
    )


_BsnRadiusAuthServerIPSecEncryption_Type.__name__ = "Integer32"
_BsnRadiusAuthServerIPSecEncryption_Object = MibTableColumn
bsnRadiusAuthServerIPSecEncryption = _BsnRadiusAuthServerIPSecEncryption_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 1, 1, 10),
    _BsnRadiusAuthServerIPSecEncryption_Type()
)
bsnRadiusAuthServerIPSecEncryption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAuthServerIPSecEncryption.setStatus("current")


class _BsnRadiusAuthServerIPSecIKEPhase1_Type(Integer32):
    """Custom type bsnRadiusAuthServerIPSecIKEPhase1 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("agressive", 2),
          ("main", 1))
    )


_BsnRadiusAuthServerIPSecIKEPhase1_Type.__name__ = "Integer32"
_BsnRadiusAuthServerIPSecIKEPhase1_Object = MibTableColumn
bsnRadiusAuthServerIPSecIKEPhase1 = _BsnRadiusAuthServerIPSecIKEPhase1_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 1, 1, 11),
    _BsnRadiusAuthServerIPSecIKEPhase1_Type()
)
bsnRadiusAuthServerIPSecIKEPhase1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAuthServerIPSecIKEPhase1.setStatus("current")


class _BsnRadiusAuthServerIPSecIKELifetime_Type(Integer32):
    """Custom type bsnRadiusAuthServerIPSecIKELifetime based on Integer32"""
    defaultValue = 28800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1800, 345600),
    )


_BsnRadiusAuthServerIPSecIKELifetime_Type.__name__ = "Integer32"
_BsnRadiusAuthServerIPSecIKELifetime_Object = MibTableColumn
bsnRadiusAuthServerIPSecIKELifetime = _BsnRadiusAuthServerIPSecIKELifetime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 1, 1, 12),
    _BsnRadiusAuthServerIPSecIKELifetime_Type()
)
bsnRadiusAuthServerIPSecIKELifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAuthServerIPSecIKELifetime.setStatus("current")


class _BsnRadiusAuthServerIPSecDHGroup_Type(Integer32):
    """Custom type bsnRadiusAuthServerIPSecDHGroup based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              14)
        )
    )
    namedValues = NamedValues(
        *(("group1", 1),
          ("group14", 14),
          ("group2", 2),
          ("group5", 5))
    )


_BsnRadiusAuthServerIPSecDHGroup_Type.__name__ = "Integer32"
_BsnRadiusAuthServerIPSecDHGroup_Object = MibTableColumn
bsnRadiusAuthServerIPSecDHGroup = _BsnRadiusAuthServerIPSecDHGroup_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 1, 1, 13),
    _BsnRadiusAuthServerIPSecDHGroup_Type()
)
bsnRadiusAuthServerIPSecDHGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAuthServerIPSecDHGroup.setStatus("current")


class _BsnRadiusAuthServerNetworkUserConfig_Type(Integer32):
    """Custom type bsnRadiusAuthServerNetworkUserConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnRadiusAuthServerNetworkUserConfig_Type.__name__ = "Integer32"
_BsnRadiusAuthServerNetworkUserConfig_Object = MibTableColumn
bsnRadiusAuthServerNetworkUserConfig = _BsnRadiusAuthServerNetworkUserConfig_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 1, 1, 14),
    _BsnRadiusAuthServerNetworkUserConfig_Type()
)
bsnRadiusAuthServerNetworkUserConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAuthServerNetworkUserConfig.setStatus("current")


class _BsnRadiusAuthServerMgmtUserConfig_Type(Integer32):
    """Custom type bsnRadiusAuthServerMgmtUserConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnRadiusAuthServerMgmtUserConfig_Type.__name__ = "Integer32"
_BsnRadiusAuthServerMgmtUserConfig_Object = MibTableColumn
bsnRadiusAuthServerMgmtUserConfig = _BsnRadiusAuthServerMgmtUserConfig_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 1, 1, 15),
    _BsnRadiusAuthServerMgmtUserConfig_Type()
)
bsnRadiusAuthServerMgmtUserConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAuthServerMgmtUserConfig.setStatus("current")


class _BsnRadiusAuthServerRetransmitTimeout_Type(Integer32):
    """Custom type bsnRadiusAuthServerRetransmitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_BsnRadiusAuthServerRetransmitTimeout_Type.__name__ = "Integer32"
_BsnRadiusAuthServerRetransmitTimeout_Object = MibTableColumn
bsnRadiusAuthServerRetransmitTimeout = _BsnRadiusAuthServerRetransmitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 1, 1, 17),
    _BsnRadiusAuthServerRetransmitTimeout_Type()
)
bsnRadiusAuthServerRetransmitTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAuthServerRetransmitTimeout.setStatus("current")
_BsnRadiusAuthServerKeyWrapKEKkey_Type = OctetString
_BsnRadiusAuthServerKeyWrapKEKkey_Object = MibTableColumn
bsnRadiusAuthServerKeyWrapKEKkey = _BsnRadiusAuthServerKeyWrapKEKkey_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 1, 1, 18),
    _BsnRadiusAuthServerKeyWrapKEKkey_Type()
)
bsnRadiusAuthServerKeyWrapKEKkey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAuthServerKeyWrapKEKkey.setStatus("current")
_BsnRadiusAuthServerKeyWrapMACKkey_Type = OctetString
_BsnRadiusAuthServerKeyWrapMACKkey_Object = MibTableColumn
bsnRadiusAuthServerKeyWrapMACKkey = _BsnRadiusAuthServerKeyWrapMACKkey_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 1, 1, 19),
    _BsnRadiusAuthServerKeyWrapMACKkey_Type()
)
bsnRadiusAuthServerKeyWrapMACKkey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAuthServerKeyWrapMACKkey.setStatus("current")


class _BsnRadiusAuthServerKeyWrapFormat_Type(Integer32):
    """Custom type bsnRadiusAuthServerKeyWrapFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 2),
          ("hex", 1))
    )


_BsnRadiusAuthServerKeyWrapFormat_Type.__name__ = "Integer32"
_BsnRadiusAuthServerKeyWrapFormat_Object = MibTableColumn
bsnRadiusAuthServerKeyWrapFormat = _BsnRadiusAuthServerKeyWrapFormat_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 1, 1, 20),
    _BsnRadiusAuthServerKeyWrapFormat_Type()
)
bsnRadiusAuthServerKeyWrapFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAuthServerKeyWrapFormat.setStatus("current")
_BsnRadiusAuthServerRowStatus_Type = RowStatus
_BsnRadiusAuthServerRowStatus_Object = MibTableColumn
bsnRadiusAuthServerRowStatus = _BsnRadiusAuthServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 1, 1, 26),
    _BsnRadiusAuthServerRowStatus_Type()
)
bsnRadiusAuthServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAuthServerRowStatus.setStatus("current")
_BsnRadiusAuthServerInetAddressType_Type = InetAddressType
_BsnRadiusAuthServerInetAddressType_Object = MibTableColumn
bsnRadiusAuthServerInetAddressType = _BsnRadiusAuthServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 1, 1, 27),
    _BsnRadiusAuthServerInetAddressType_Type()
)
bsnRadiusAuthServerInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAuthServerInetAddressType.setStatus("current")
_BsnRadiusAuthServerInetAddress_Type = InetAddress
_BsnRadiusAuthServerInetAddress_Object = MibTableColumn
bsnRadiusAuthServerInetAddress = _BsnRadiusAuthServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 1, 1, 28),
    _BsnRadiusAuthServerInetAddress_Type()
)
bsnRadiusAuthServerInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAuthServerInetAddress.setStatus("current")
_BsnRadiusAccServerTable_Object = MibTable
bsnRadiusAccServerTable = _BsnRadiusAccServerTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 2)
)
if mibBuilder.loadTexts:
    bsnRadiusAccServerTable.setStatus("current")
_BsnRadiusAccServerEntry_Object = MibTableRow
bsnRadiusAccServerEntry = _BsnRadiusAccServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 2, 1)
)
bsnRadiusAccServerEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerIndex"),
)
if mibBuilder.loadTexts:
    bsnRadiusAccServerEntry.setStatus("current")


class _BsnRadiusAccServerIndex_Type(Integer32):
    """Custom type bsnRadiusAccServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 17),
    )


_BsnRadiusAccServerIndex_Type.__name__ = "Integer32"
_BsnRadiusAccServerIndex_Object = MibTableColumn
bsnRadiusAccServerIndex = _BsnRadiusAccServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 2, 1, 1),
    _BsnRadiusAccServerIndex_Type()
)
bsnRadiusAccServerIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAccServerIndex.setStatus("current")
_BsnRadiusAccServerAddress_Type = IpAddress
_BsnRadiusAccServerAddress_Object = MibTableColumn
bsnRadiusAccServerAddress = _BsnRadiusAccServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 2, 1, 2),
    _BsnRadiusAccServerAddress_Type()
)
bsnRadiusAccServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAccServerAddress.setStatus("current")


class _BsnRadiusAccClientServerPortNumber_Type(Integer32):
    """Custom type bsnRadiusAccClientServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BsnRadiusAccClientServerPortNumber_Type.__name__ = "Integer32"
_BsnRadiusAccClientServerPortNumber_Object = MibTableColumn
bsnRadiusAccClientServerPortNumber = _BsnRadiusAccClientServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 2, 1, 3),
    _BsnRadiusAccClientServerPortNumber_Type()
)
bsnRadiusAccClientServerPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAccClientServerPortNumber.setStatus("current")


class _BsnRadiusAccServerKey_Type(OctetString):
    """Custom type bsnRadiusAccServerKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BsnRadiusAccServerKey_Type.__name__ = "OctetString"
_BsnRadiusAccServerKey_Object = MibTableColumn
bsnRadiusAccServerKey = _BsnRadiusAccServerKey_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 2, 1, 4),
    _BsnRadiusAccServerKey_Type()
)
bsnRadiusAccServerKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAccServerKey.setStatus("current")


class _BsnRadiusAccServerStatus_Type(Integer32):
    """Custom type bsnRadiusAccServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnRadiusAccServerStatus_Type.__name__ = "Integer32"
_BsnRadiusAccServerStatus_Object = MibTableColumn
bsnRadiusAccServerStatus = _BsnRadiusAccServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 2, 1, 5),
    _BsnRadiusAccServerStatus_Type()
)
bsnRadiusAccServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAccServerStatus.setStatus("current")


class _BsnRadiusAccServerKeyFormat_Type(Integer32):
    """Custom type bsnRadiusAccServerKeyFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 2),
          ("hex", 1))
    )


_BsnRadiusAccServerKeyFormat_Type.__name__ = "Integer32"
_BsnRadiusAccServerKeyFormat_Object = MibTableColumn
bsnRadiusAccServerKeyFormat = _BsnRadiusAccServerKeyFormat_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 2, 1, 6),
    _BsnRadiusAccServerKeyFormat_Type()
)
bsnRadiusAccServerKeyFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAccServerKeyFormat.setStatus("current")


class _BsnRadiusAccServerIPSec_Type(Integer32):
    """Custom type bsnRadiusAccServerIPSec based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnRadiusAccServerIPSec_Type.__name__ = "Integer32"
_BsnRadiusAccServerIPSec_Object = MibTableColumn
bsnRadiusAccServerIPSec = _BsnRadiusAccServerIPSec_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 2, 1, 7),
    _BsnRadiusAccServerIPSec_Type()
)
bsnRadiusAccServerIPSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAccServerIPSec.setStatus("current")


class _BsnRadiusAccServerIPSecAuth_Type(Integer32):
    """Custom type bsnRadiusAccServerIPSecAuth based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hmacMd5", 1),
          ("hmacSha1", 2),
          ("none", 0))
    )


_BsnRadiusAccServerIPSecAuth_Type.__name__ = "Integer32"
_BsnRadiusAccServerIPSecAuth_Object = MibTableColumn
bsnRadiusAccServerIPSecAuth = _BsnRadiusAccServerIPSecAuth_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 2, 1, 8),
    _BsnRadiusAccServerIPSecAuth_Type()
)
bsnRadiusAccServerIPSecAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAccServerIPSecAuth.setStatus("current")


class _BsnRadiusAccServerIPSecEncryption_Type(Integer32):
    """Custom type bsnRadiusAccServerIPSecEncryption based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("aes256Cbc", 4),
          ("aesCbc", 3),
          ("des", 1),
          ("none", 0),
          ("tripleDes", 2))
    )


_BsnRadiusAccServerIPSecEncryption_Type.__name__ = "Integer32"
_BsnRadiusAccServerIPSecEncryption_Object = MibTableColumn
bsnRadiusAccServerIPSecEncryption = _BsnRadiusAccServerIPSecEncryption_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 2, 1, 9),
    _BsnRadiusAccServerIPSecEncryption_Type()
)
bsnRadiusAccServerIPSecEncryption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAccServerIPSecEncryption.setStatus("current")


class _BsnRadiusAccServerIPSecIKEPhase1_Type(Integer32):
    """Custom type bsnRadiusAccServerIPSecIKEPhase1 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("agressive", 2),
          ("main", 1))
    )


_BsnRadiusAccServerIPSecIKEPhase1_Type.__name__ = "Integer32"
_BsnRadiusAccServerIPSecIKEPhase1_Object = MibTableColumn
bsnRadiusAccServerIPSecIKEPhase1 = _BsnRadiusAccServerIPSecIKEPhase1_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 2, 1, 10),
    _BsnRadiusAccServerIPSecIKEPhase1_Type()
)
bsnRadiusAccServerIPSecIKEPhase1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAccServerIPSecIKEPhase1.setStatus("current")


class _BsnRadiusAccServerIPSecIKELifetime_Type(Integer32):
    """Custom type bsnRadiusAccServerIPSecIKELifetime based on Integer32"""
    defaultValue = 28800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1800, 345600),
    )


_BsnRadiusAccServerIPSecIKELifetime_Type.__name__ = "Integer32"
_BsnRadiusAccServerIPSecIKELifetime_Object = MibTableColumn
bsnRadiusAccServerIPSecIKELifetime = _BsnRadiusAccServerIPSecIKELifetime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 2, 1, 11),
    _BsnRadiusAccServerIPSecIKELifetime_Type()
)
bsnRadiusAccServerIPSecIKELifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAccServerIPSecIKELifetime.setStatus("current")


class _BsnRadiusAccServerIPSecDHGroup_Type(Integer32):
    """Custom type bsnRadiusAccServerIPSecDHGroup based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              14)
        )
    )
    namedValues = NamedValues(
        *(("group1", 1),
          ("group14", 14),
          ("group2", 2),
          ("group5", 5))
    )


_BsnRadiusAccServerIPSecDHGroup_Type.__name__ = "Integer32"
_BsnRadiusAccServerIPSecDHGroup_Object = MibTableColumn
bsnRadiusAccServerIPSecDHGroup = _BsnRadiusAccServerIPSecDHGroup_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 2, 1, 12),
    _BsnRadiusAccServerIPSecDHGroup_Type()
)
bsnRadiusAccServerIPSecDHGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAccServerIPSecDHGroup.setStatus("current")


class _BsnRadiusAccServerNetworkUserConfig_Type(Integer32):
    """Custom type bsnRadiusAccServerNetworkUserConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnRadiusAccServerNetworkUserConfig_Type.__name__ = "Integer32"
_BsnRadiusAccServerNetworkUserConfig_Object = MibTableColumn
bsnRadiusAccServerNetworkUserConfig = _BsnRadiusAccServerNetworkUserConfig_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 2, 1, 13),
    _BsnRadiusAccServerNetworkUserConfig_Type()
)
bsnRadiusAccServerNetworkUserConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAccServerNetworkUserConfig.setStatus("current")


class _BsnRadiusAccServerRetransmitTimeout_Type(Integer32):
    """Custom type bsnRadiusAccServerRetransmitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_BsnRadiusAccServerRetransmitTimeout_Type.__name__ = "Integer32"
_BsnRadiusAccServerRetransmitTimeout_Object = MibTableColumn
bsnRadiusAccServerRetransmitTimeout = _BsnRadiusAccServerRetransmitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 2, 1, 14),
    _BsnRadiusAccServerRetransmitTimeout_Type()
)
bsnRadiusAccServerRetransmitTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAccServerRetransmitTimeout.setStatus("current")
_BsnRadiusAccServerRowStatus_Type = RowStatus
_BsnRadiusAccServerRowStatus_Object = MibTableColumn
bsnRadiusAccServerRowStatus = _BsnRadiusAccServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 2, 1, 26),
    _BsnRadiusAccServerRowStatus_Type()
)
bsnRadiusAccServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAccServerRowStatus.setStatus("current")
_BsnRadiusAccServerInetAddressType_Type = InetAddressType
_BsnRadiusAccServerInetAddressType_Object = MibTableColumn
bsnRadiusAccServerInetAddressType = _BsnRadiusAccServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 2, 1, 27),
    _BsnRadiusAccServerInetAddressType_Type()
)
bsnRadiusAccServerInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAccServerInetAddressType.setStatus("current")
_BsnRadiusAccServerInetAddress_Type = InetAddress
_BsnRadiusAccServerInetAddress_Object = MibTableColumn
bsnRadiusAccServerInetAddress = _BsnRadiusAccServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 2, 1, 28),
    _BsnRadiusAccServerInetAddress_Type()
)
bsnRadiusAccServerInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnRadiusAccServerInetAddress.setStatus("current")
_BsnRadiusAuthServerStatsTable_Object = MibTable
bsnRadiusAuthServerStatsTable = _BsnRadiusAuthServerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 3)
)
if mibBuilder.loadTexts:
    bsnRadiusAuthServerStatsTable.setStatus("current")
_BsnRadiusAuthServerStatsEntry_Object = MibTableRow
bsnRadiusAuthServerStatsEntry = _BsnRadiusAuthServerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 3, 1)
)
bsnRadiusAuthServerStatsEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerIndex"),
)
if mibBuilder.loadTexts:
    bsnRadiusAuthServerStatsEntry.setStatus("current")
_BsnRadiusAuthClientRoundTripTime_Type = TimeTicks
_BsnRadiusAuthClientRoundTripTime_Object = MibTableColumn
bsnRadiusAuthClientRoundTripTime = _BsnRadiusAuthClientRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 3, 1, 6),
    _BsnRadiusAuthClientRoundTripTime_Type()
)
bsnRadiusAuthClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRadiusAuthClientRoundTripTime.setStatus("current")
_BsnRadiusAuthClientAccessRequests_Type = Counter32
_BsnRadiusAuthClientAccessRequests_Object = MibTableColumn
bsnRadiusAuthClientAccessRequests = _BsnRadiusAuthClientAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 3, 1, 7),
    _BsnRadiusAuthClientAccessRequests_Type()
)
bsnRadiusAuthClientAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRadiusAuthClientAccessRequests.setStatus("current")
_BsnRadiusAuthClientAccessRetransmissions_Type = Counter32
_BsnRadiusAuthClientAccessRetransmissions_Object = MibTableColumn
bsnRadiusAuthClientAccessRetransmissions = _BsnRadiusAuthClientAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 3, 1, 8),
    _BsnRadiusAuthClientAccessRetransmissions_Type()
)
bsnRadiusAuthClientAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRadiusAuthClientAccessRetransmissions.setStatus("current")
_BsnRadiusAuthClientAccessAccepts_Type = Counter32
_BsnRadiusAuthClientAccessAccepts_Object = MibTableColumn
bsnRadiusAuthClientAccessAccepts = _BsnRadiusAuthClientAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 3, 1, 9),
    _BsnRadiusAuthClientAccessAccepts_Type()
)
bsnRadiusAuthClientAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRadiusAuthClientAccessAccepts.setStatus("current")
_BsnRadiusAuthClientAccessRejects_Type = Counter32
_BsnRadiusAuthClientAccessRejects_Object = MibTableColumn
bsnRadiusAuthClientAccessRejects = _BsnRadiusAuthClientAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 3, 1, 10),
    _BsnRadiusAuthClientAccessRejects_Type()
)
bsnRadiusAuthClientAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRadiusAuthClientAccessRejects.setStatus("current")
_BsnRadiusAuthClientAccessChallenges_Type = Counter32
_BsnRadiusAuthClientAccessChallenges_Object = MibTableColumn
bsnRadiusAuthClientAccessChallenges = _BsnRadiusAuthClientAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 3, 1, 11),
    _BsnRadiusAuthClientAccessChallenges_Type()
)
bsnRadiusAuthClientAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRadiusAuthClientAccessChallenges.setStatus("current")
_BsnRadiusAuthClientMalformedAccessResponses_Type = Counter32
_BsnRadiusAuthClientMalformedAccessResponses_Object = MibTableColumn
bsnRadiusAuthClientMalformedAccessResponses = _BsnRadiusAuthClientMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 3, 1, 12),
    _BsnRadiusAuthClientMalformedAccessResponses_Type()
)
bsnRadiusAuthClientMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRadiusAuthClientMalformedAccessResponses.setStatus("current")
_BsnRadiusAuthClientBadAuthenticators_Type = Counter32
_BsnRadiusAuthClientBadAuthenticators_Object = MibTableColumn
bsnRadiusAuthClientBadAuthenticators = _BsnRadiusAuthClientBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 3, 1, 13),
    _BsnRadiusAuthClientBadAuthenticators_Type()
)
bsnRadiusAuthClientBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRadiusAuthClientBadAuthenticators.setStatus("current")
_BsnRadiusAuthClientPendingRequests_Type = Gauge32
_BsnRadiusAuthClientPendingRequests_Object = MibTableColumn
bsnRadiusAuthClientPendingRequests = _BsnRadiusAuthClientPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 3, 1, 14),
    _BsnRadiusAuthClientPendingRequests_Type()
)
bsnRadiusAuthClientPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRadiusAuthClientPendingRequests.setStatus("current")
_BsnRadiusAuthClientTimeouts_Type = Counter32
_BsnRadiusAuthClientTimeouts_Object = MibTableColumn
bsnRadiusAuthClientTimeouts = _BsnRadiusAuthClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 3, 1, 15),
    _BsnRadiusAuthClientTimeouts_Type()
)
bsnRadiusAuthClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRadiusAuthClientTimeouts.setStatus("current")
_BsnRadiusAuthClientUnknownTypes_Type = Counter32
_BsnRadiusAuthClientUnknownTypes_Object = MibTableColumn
bsnRadiusAuthClientUnknownTypes = _BsnRadiusAuthClientUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 3, 1, 16),
    _BsnRadiusAuthClientUnknownTypes_Type()
)
bsnRadiusAuthClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRadiusAuthClientUnknownTypes.setStatus("current")
_BsnRadiusAuthClientPacketsDropped_Type = Counter32
_BsnRadiusAuthClientPacketsDropped_Object = MibTableColumn
bsnRadiusAuthClientPacketsDropped = _BsnRadiusAuthClientPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 3, 1, 36),
    _BsnRadiusAuthClientPacketsDropped_Type()
)
bsnRadiusAuthClientPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRadiusAuthClientPacketsDropped.setStatus("current")
_BsnRadiusAccServerStatsTable_Object = MibTable
bsnRadiusAccServerStatsTable = _BsnRadiusAccServerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 4)
)
if mibBuilder.loadTexts:
    bsnRadiusAccServerStatsTable.setStatus("current")
_BsnRadiusAccServerStatsEntry_Object = MibTableRow
bsnRadiusAccServerStatsEntry = _BsnRadiusAccServerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 4, 1)
)
bsnRadiusAccServerStatsEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerIndex"),
)
if mibBuilder.loadTexts:
    bsnRadiusAccServerStatsEntry.setStatus("current")
_BsnRadiusAccClientRoundTripTime_Type = TimeTicks
_BsnRadiusAccClientRoundTripTime_Object = MibTableColumn
bsnRadiusAccClientRoundTripTime = _BsnRadiusAccClientRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 4, 1, 6),
    _BsnRadiusAccClientRoundTripTime_Type()
)
bsnRadiusAccClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRadiusAccClientRoundTripTime.setStatus("current")
_BsnRadiusAccClientRequests_Type = Counter32
_BsnRadiusAccClientRequests_Object = MibTableColumn
bsnRadiusAccClientRequests = _BsnRadiusAccClientRequests_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 4, 1, 7),
    _BsnRadiusAccClientRequests_Type()
)
bsnRadiusAccClientRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRadiusAccClientRequests.setStatus("current")
_BsnRadiusAccClientRetransmissions_Type = Counter32
_BsnRadiusAccClientRetransmissions_Object = MibTableColumn
bsnRadiusAccClientRetransmissions = _BsnRadiusAccClientRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 4, 1, 8),
    _BsnRadiusAccClientRetransmissions_Type()
)
bsnRadiusAccClientRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRadiusAccClientRetransmissions.setStatus("current")
_BsnRadiusAccClientResponses_Type = Counter32
_BsnRadiusAccClientResponses_Object = MibTableColumn
bsnRadiusAccClientResponses = _BsnRadiusAccClientResponses_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 4, 1, 9),
    _BsnRadiusAccClientResponses_Type()
)
bsnRadiusAccClientResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRadiusAccClientResponses.setStatus("current")
_BsnRadiusAccClientMalformedResponses_Type = Counter32
_BsnRadiusAccClientMalformedResponses_Object = MibTableColumn
bsnRadiusAccClientMalformedResponses = _BsnRadiusAccClientMalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 4, 1, 10),
    _BsnRadiusAccClientMalformedResponses_Type()
)
bsnRadiusAccClientMalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRadiusAccClientMalformedResponses.setStatus("current")
_BsnRadiusAccClientBadAuthenticators_Type = Counter32
_BsnRadiusAccClientBadAuthenticators_Object = MibTableColumn
bsnRadiusAccClientBadAuthenticators = _BsnRadiusAccClientBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 4, 1, 11),
    _BsnRadiusAccClientBadAuthenticators_Type()
)
bsnRadiusAccClientBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRadiusAccClientBadAuthenticators.setStatus("current")
_BsnRadiusAccClientPendingRequests_Type = Gauge32
_BsnRadiusAccClientPendingRequests_Object = MibTableColumn
bsnRadiusAccClientPendingRequests = _BsnRadiusAccClientPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 4, 1, 12),
    _BsnRadiusAccClientPendingRequests_Type()
)
bsnRadiusAccClientPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRadiusAccClientPendingRequests.setStatus("current")
_BsnRadiusAccClientTimeouts_Type = Counter32
_BsnRadiusAccClientTimeouts_Object = MibTableColumn
bsnRadiusAccClientTimeouts = _BsnRadiusAccClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 4, 1, 13),
    _BsnRadiusAccClientTimeouts_Type()
)
bsnRadiusAccClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRadiusAccClientTimeouts.setStatus("current")
_BsnRadiusAccClientUnknownTypes_Type = Counter32
_BsnRadiusAccClientUnknownTypes_Object = MibTableColumn
bsnRadiusAccClientUnknownTypes = _BsnRadiusAccClientUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 4, 1, 14),
    _BsnRadiusAccClientUnknownTypes_Type()
)
bsnRadiusAccClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRadiusAccClientUnknownTypes.setStatus("current")
_BsnRadiusAccClientPacketsDropped_Type = Counter32
_BsnRadiusAccClientPacketsDropped_Object = MibTableColumn
bsnRadiusAccClientPacketsDropped = _BsnRadiusAccClientPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 4, 1, 34),
    _BsnRadiusAccClientPacketsDropped_Type()
)
bsnRadiusAccClientPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnRadiusAccClientPacketsDropped.setStatus("current")
_BsnUsersTable_Object = MibTable
bsnUsersTable = _BsnUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 5)
)
if mibBuilder.loadTexts:
    bsnUsersTable.setStatus("obsolete")
_BsnUsersEntry_Object = MibTableRow
bsnUsersEntry = _BsnUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 5, 1)
)
bsnUsersEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnUserName"),
)
if mibBuilder.loadTexts:
    bsnUsersEntry.setStatus("obsolete")


class _BsnUserName_Type(OctetString):
    """Custom type bsnUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_BsnUserName_Type.__name__ = "OctetString"
_BsnUserName_Object = MibTableColumn
bsnUserName = _BsnUserName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 5, 1, 2),
    _BsnUserName_Type()
)
bsnUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnUserName.setStatus("obsolete")


class _BsnUserPassword_Type(OctetString):
    """Custom type bsnUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_BsnUserPassword_Type.__name__ = "OctetString"
_BsnUserPassword_Object = MibTableColumn
bsnUserPassword = _BsnUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 5, 1, 3),
    _BsnUserPassword_Type()
)
bsnUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnUserPassword.setStatus("obsolete")


class _BsnUserEssIndex_Type(Integer32):
    """Custom type bsnUserEssIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 517),
    )


_BsnUserEssIndex_Type.__name__ = "Integer32"
_BsnUserEssIndex_Object = MibTableColumn
bsnUserEssIndex = _BsnUserEssIndex_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 5, 1, 4),
    _BsnUserEssIndex_Type()
)
bsnUserEssIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnUserEssIndex.setStatus("obsolete")


class _BsnUserAccessMode_Type(Integer32):
    """Custom type bsnUserAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_BsnUserAccessMode_Type.__name__ = "Integer32"
_BsnUserAccessMode_Object = MibTableColumn
bsnUserAccessMode = _BsnUserAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 5, 1, 5),
    _BsnUserAccessMode_Type()
)
bsnUserAccessMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnUserAccessMode.setStatus("obsolete")


class _BsnUserType_Type(Integer32):
    """Custom type bsnUserType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("macFilter", 3),
          ("management", 1),
          ("wlan", 2))
    )


_BsnUserType_Type.__name__ = "Integer32"
_BsnUserType_Object = MibTableColumn
bsnUserType = _BsnUserType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 5, 1, 6),
    _BsnUserType_Type()
)
bsnUserType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnUserType.setStatus("obsolete")


class _BsnUserInterfaceName_Type(OctetString):
    """Custom type bsnUserInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BsnUserInterfaceName_Type.__name__ = "OctetString"
_BsnUserInterfaceName_Object = MibTableColumn
bsnUserInterfaceName = _BsnUserInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 5, 1, 7),
    _BsnUserInterfaceName_Type()
)
bsnUserInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnUserInterfaceName.setStatus("obsolete")
_BsnUserRowStatus_Type = RowStatus
_BsnUserRowStatus_Object = MibTableColumn
bsnUserRowStatus = _BsnUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 5, 1, 26),
    _BsnUserRowStatus_Type()
)
bsnUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnUserRowStatus.setStatus("obsolete")
_BsnBlackListClientTable_Object = MibTable
bsnBlackListClientTable = _BsnBlackListClientTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 6)
)
if mibBuilder.loadTexts:
    bsnBlackListClientTable.setStatus("current")
_BsnBlackListClientEntry_Object = MibTableRow
bsnBlackListClientEntry = _BsnBlackListClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 6, 1)
)
bsnBlackListClientEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnBlackListClientMacAddress"),
)
if mibBuilder.loadTexts:
    bsnBlackListClientEntry.setStatus("current")


class _BsnBlackListClientMacAddress_Type(OctetString):
    """Custom type bsnBlackListClientMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_BsnBlackListClientMacAddress_Type.__name__ = "OctetString"
_BsnBlackListClientMacAddress_Object = MibTableColumn
bsnBlackListClientMacAddress = _BsnBlackListClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 6, 1, 1),
    _BsnBlackListClientMacAddress_Type()
)
bsnBlackListClientMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnBlackListClientMacAddress.setStatus("current")


class _BsnBlackListClientDescription_Type(OctetString):
    """Custom type bsnBlackListClientDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BsnBlackListClientDescription_Type.__name__ = "OctetString"
_BsnBlackListClientDescription_Object = MibTableColumn
bsnBlackListClientDescription = _BsnBlackListClientDescription_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 6, 1, 2),
    _BsnBlackListClientDescription_Type()
)
bsnBlackListClientDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnBlackListClientDescription.setStatus("current")
_BsnBlackListClientRowStatus_Type = RowStatus
_BsnBlackListClientRowStatus_Object = MibTableColumn
bsnBlackListClientRowStatus = _BsnBlackListClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 6, 1, 22),
    _BsnBlackListClientRowStatus_Type()
)
bsnBlackListClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnBlackListClientRowStatus.setStatus("current")
_BsnAclTable_Object = MibTable
bsnAclTable = _BsnAclTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 7)
)
if mibBuilder.loadTexts:
    bsnAclTable.setStatus("current")
_BsnAclEntry_Object = MibTableRow
bsnAclEntry = _BsnAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 7, 1)
)
bsnAclEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAclName"),
)
if mibBuilder.loadTexts:
    bsnAclEntry.setStatus("current")


class _BsnAclName_Type(OctetString):
    """Custom type bsnAclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BsnAclName_Type.__name__ = "OctetString"
_BsnAclName_Object = MibTableColumn
bsnAclName = _BsnAclName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 7, 1, 1),
    _BsnAclName_Type()
)
bsnAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAclName.setStatus("current")


class _BsnAclApplyMode_Type(Integer32):
    """Custom type bsnAclApplyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("applied", 1),
          ("notapplied", 0))
    )


_BsnAclApplyMode_Type.__name__ = "Integer32"
_BsnAclApplyMode_Object = MibTableColumn
bsnAclApplyMode = _BsnAclApplyMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 7, 1, 2),
    _BsnAclApplyMode_Type()
)
bsnAclApplyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAclApplyMode.setStatus("current")
_BsnAclRowStatus_Type = RowStatus
_BsnAclRowStatus_Object = MibTableColumn
bsnAclRowStatus = _BsnAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 7, 1, 20),
    _BsnAclRowStatus_Type()
)
bsnAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAclRowStatus.setStatus("current")
_BsnAclRuleTable_Object = MibTable
bsnAclRuleTable = _BsnAclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 8)
)
if mibBuilder.loadTexts:
    bsnAclRuleTable.setStatus("current")
_BsnAclRuleEntry_Object = MibTableRow
bsnAclRuleEntry = _BsnAclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 8, 1)
)
bsnAclRuleEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAclName"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAclRuleIndex"),
)
if mibBuilder.loadTexts:
    bsnAclRuleEntry.setStatus("current")


class _BsnAclRuleIndex_Type(Unsigned32):
    """Custom type bsnAclRuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_BsnAclRuleIndex_Type.__name__ = "Unsigned32"
_BsnAclRuleIndex_Object = MibTableColumn
bsnAclRuleIndex = _BsnAclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 8, 1, 2),
    _BsnAclRuleIndex_Type()
)
bsnAclRuleIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAclRuleIndex.setStatus("current")


class _BsnAclRuleAction_Type(Integer32):
    """Custom type bsnAclRuleAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_BsnAclRuleAction_Type.__name__ = "Integer32"
_BsnAclRuleAction_Object = MibTableColumn
bsnAclRuleAction = _BsnAclRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 8, 1, 3),
    _BsnAclRuleAction_Type()
)
bsnAclRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAclRuleAction.setStatus("current")


class _BsnAclRuleDirection_Type(Integer32):
    """Custom type bsnAclRuleDirection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 2),
          ("inbound", 0),
          ("outbound", 1))
    )


_BsnAclRuleDirection_Type.__name__ = "Integer32"
_BsnAclRuleDirection_Object = MibTableColumn
bsnAclRuleDirection = _BsnAclRuleDirection_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 8, 1, 4),
    _BsnAclRuleDirection_Type()
)
bsnAclRuleDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAclRuleDirection.setStatus("current")


class _BsnAclRuleSourceIpAddress_Type(IpAddress):
    """Custom type bsnAclRuleSourceIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_BsnAclRuleSourceIpAddress_Object = MibTableColumn
bsnAclRuleSourceIpAddress = _BsnAclRuleSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 8, 1, 5),
    _BsnAclRuleSourceIpAddress_Type()
)
bsnAclRuleSourceIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAclRuleSourceIpAddress.setStatus("current")


class _BsnAclRuleSourceIpNetmask_Type(IpAddress):
    """Custom type bsnAclRuleSourceIpNetmask based on IpAddress"""
    defaultHexValue = "00000000"


_BsnAclRuleSourceIpNetmask_Object = MibTableColumn
bsnAclRuleSourceIpNetmask = _BsnAclRuleSourceIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 8, 1, 6),
    _BsnAclRuleSourceIpNetmask_Type()
)
bsnAclRuleSourceIpNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAclRuleSourceIpNetmask.setStatus("current")


class _BsnAclRuleDestinationIpAddress_Type(IpAddress):
    """Custom type bsnAclRuleDestinationIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_BsnAclRuleDestinationIpAddress_Object = MibTableColumn
bsnAclRuleDestinationIpAddress = _BsnAclRuleDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 8, 1, 7),
    _BsnAclRuleDestinationIpAddress_Type()
)
bsnAclRuleDestinationIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAclRuleDestinationIpAddress.setStatus("current")


class _BsnAclRuleDestinationIpNetmask_Type(IpAddress):
    """Custom type bsnAclRuleDestinationIpNetmask based on IpAddress"""
    defaultHexValue = "00000000"


_BsnAclRuleDestinationIpNetmask_Object = MibTableColumn
bsnAclRuleDestinationIpNetmask = _BsnAclRuleDestinationIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 8, 1, 8),
    _BsnAclRuleDestinationIpNetmask_Type()
)
bsnAclRuleDestinationIpNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAclRuleDestinationIpNetmask.setStatus("current")


class _BsnAclRuleProtocol_Type(Unsigned32):
    """Custom type bsnAclRuleProtocol based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_BsnAclRuleProtocol_Type.__name__ = "Unsigned32"
_BsnAclRuleProtocol_Object = MibTableColumn
bsnAclRuleProtocol = _BsnAclRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 8, 1, 9),
    _BsnAclRuleProtocol_Type()
)
bsnAclRuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAclRuleProtocol.setStatus("current")


class _BsnAclRuleStartSourcePort_Type(Unsigned32):
    """Custom type bsnAclRuleStartSourcePort based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BsnAclRuleStartSourcePort_Type.__name__ = "Unsigned32"
_BsnAclRuleStartSourcePort_Object = MibTableColumn
bsnAclRuleStartSourcePort = _BsnAclRuleStartSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 8, 1, 10),
    _BsnAclRuleStartSourcePort_Type()
)
bsnAclRuleStartSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAclRuleStartSourcePort.setStatus("current")


class _BsnAclRuleEndSourcePort_Type(Unsigned32):
    """Custom type bsnAclRuleEndSourcePort based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BsnAclRuleEndSourcePort_Type.__name__ = "Unsigned32"
_BsnAclRuleEndSourcePort_Object = MibTableColumn
bsnAclRuleEndSourcePort = _BsnAclRuleEndSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 8, 1, 11),
    _BsnAclRuleEndSourcePort_Type()
)
bsnAclRuleEndSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAclRuleEndSourcePort.setStatus("current")


class _BsnAclRuleStartDestinationPort_Type(Unsigned32):
    """Custom type bsnAclRuleStartDestinationPort based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BsnAclRuleStartDestinationPort_Type.__name__ = "Unsigned32"
_BsnAclRuleStartDestinationPort_Object = MibTableColumn
bsnAclRuleStartDestinationPort = _BsnAclRuleStartDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 8, 1, 12),
    _BsnAclRuleStartDestinationPort_Type()
)
bsnAclRuleStartDestinationPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAclRuleStartDestinationPort.setStatus("current")


class _BsnAclRuleEndDestinationPort_Type(Unsigned32):
    """Custom type bsnAclRuleEndDestinationPort based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BsnAclRuleEndDestinationPort_Type.__name__ = "Unsigned32"
_BsnAclRuleEndDestinationPort_Object = MibTableColumn
bsnAclRuleEndDestinationPort = _BsnAclRuleEndDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 8, 1, 13),
    _BsnAclRuleEndDestinationPort_Type()
)
bsnAclRuleEndDestinationPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAclRuleEndDestinationPort.setStatus("current")


class _BsnAclRuleDscp_Type(Unsigned32):
    """Custom type bsnAclRuleDscp based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_BsnAclRuleDscp_Type.__name__ = "Unsigned32"
_BsnAclRuleDscp_Object = MibTableColumn
bsnAclRuleDscp = _BsnAclRuleDscp_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 8, 1, 14),
    _BsnAclRuleDscp_Type()
)
bsnAclRuleDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAclRuleDscp.setStatus("current")


class _BsnAclNewRuleIndex_Type(Unsigned32):
    """Custom type bsnAclNewRuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_BsnAclNewRuleIndex_Type.__name__ = "Unsigned32"
_BsnAclNewRuleIndex_Object = MibTableColumn
bsnAclNewRuleIndex = _BsnAclNewRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 8, 1, 15),
    _BsnAclNewRuleIndex_Type()
)
bsnAclNewRuleIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAclNewRuleIndex.setStatus("current")
_BsnAclRuleRowStatus_Type = RowStatus
_BsnAclRuleRowStatus_Object = MibTableColumn
bsnAclRuleRowStatus = _BsnAclRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 8, 1, 40),
    _BsnAclRuleRowStatus_Type()
)
bsnAclRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAclRuleRowStatus.setStatus("current")
_BsnMacFilterTable_Object = MibTable
bsnMacFilterTable = _BsnMacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 9)
)
if mibBuilder.loadTexts:
    bsnMacFilterTable.setStatus("current")
_BsnMacFilterEntry_Object = MibTableRow
bsnMacFilterEntry = _BsnMacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 9, 1)
)
bsnMacFilterEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnMacFilterAddress"),
)
if mibBuilder.loadTexts:
    bsnMacFilterEntry.setStatus("current")


class _BsnMacFilterAddress_Type(OctetString):
    """Custom type bsnMacFilterAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_BsnMacFilterAddress_Type.__name__ = "OctetString"
_BsnMacFilterAddress_Object = MibTableColumn
bsnMacFilterAddress = _BsnMacFilterAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 9, 1, 1),
    _BsnMacFilterAddress_Type()
)
bsnMacFilterAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnMacFilterAddress.setStatus("current")


class _BsnMacFilterWlanId_Type(Integer32):
    """Custom type bsnMacFilterWlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 517),
    )


_BsnMacFilterWlanId_Type.__name__ = "Integer32"
_BsnMacFilterWlanId_Object = MibTableColumn
bsnMacFilterWlanId = _BsnMacFilterWlanId_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 9, 1, 2),
    _BsnMacFilterWlanId_Type()
)
bsnMacFilterWlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnMacFilterWlanId.setStatus("current")


class _BsnMacFilterInterfaceName_Type(OctetString):
    """Custom type bsnMacFilterInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BsnMacFilterInterfaceName_Type.__name__ = "OctetString"
_BsnMacFilterInterfaceName_Object = MibTableColumn
bsnMacFilterInterfaceName = _BsnMacFilterInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 9, 1, 3),
    _BsnMacFilterInterfaceName_Type()
)
bsnMacFilterInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnMacFilterInterfaceName.setStatus("current")


class _BsnMacFilterDescription_Type(OctetString):
    """Custom type bsnMacFilterDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BsnMacFilterDescription_Type.__name__ = "OctetString"
_BsnMacFilterDescription_Object = MibTableColumn
bsnMacFilterDescription = _BsnMacFilterDescription_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 9, 1, 4),
    _BsnMacFilterDescription_Type()
)
bsnMacFilterDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnMacFilterDescription.setStatus("current")
_BsnMacFilterRowStatus_Type = RowStatus
_BsnMacFilterRowStatus_Object = MibTableColumn
bsnMacFilterRowStatus = _BsnMacFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 9, 1, 24),
    _BsnMacFilterRowStatus_Type()
)
bsnMacFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnMacFilterRowStatus.setStatus("current")
_BsnLocalNetUserTable_Object = MibTable
bsnLocalNetUserTable = _BsnLocalNetUserTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 10)
)
if mibBuilder.loadTexts:
    bsnLocalNetUserTable.setStatus("current")
_BsnLocalNetUserEntry_Object = MibTableRow
bsnLocalNetUserEntry = _BsnLocalNetUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 10, 1)
)
bsnLocalNetUserEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnLocalNetUserName"),
)
if mibBuilder.loadTexts:
    bsnLocalNetUserEntry.setStatus("current")


class _BsnLocalNetUserName_Type(OctetString):
    """Custom type bsnLocalNetUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_BsnLocalNetUserName_Type.__name__ = "OctetString"
_BsnLocalNetUserName_Object = MibTableColumn
bsnLocalNetUserName = _BsnLocalNetUserName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 10, 1, 1),
    _BsnLocalNetUserName_Type()
)
bsnLocalNetUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnLocalNetUserName.setStatus("current")


class _BsnLocalNetUserWlanId_Type(Integer32):
    """Custom type bsnLocalNetUserWlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 517),
    )


_BsnLocalNetUserWlanId_Type.__name__ = "Integer32"
_BsnLocalNetUserWlanId_Object = MibTableColumn
bsnLocalNetUserWlanId = _BsnLocalNetUserWlanId_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 10, 1, 2),
    _BsnLocalNetUserWlanId_Type()
)
bsnLocalNetUserWlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnLocalNetUserWlanId.setStatus("current")


class _BsnLocalNetUserPassword_Type(OctetString):
    """Custom type bsnLocalNetUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_BsnLocalNetUserPassword_Type.__name__ = "OctetString"
_BsnLocalNetUserPassword_Object = MibTableColumn
bsnLocalNetUserPassword = _BsnLocalNetUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 10, 1, 3),
    _BsnLocalNetUserPassword_Type()
)
bsnLocalNetUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnLocalNetUserPassword.setStatus("current")


class _BsnLocalNetUserDescription_Type(OctetString):
    """Custom type bsnLocalNetUserDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BsnLocalNetUserDescription_Type.__name__ = "OctetString"
_BsnLocalNetUserDescription_Object = MibTableColumn
bsnLocalNetUserDescription = _BsnLocalNetUserDescription_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 10, 1, 4),
    _BsnLocalNetUserDescription_Type()
)
bsnLocalNetUserDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnLocalNetUserDescription.setStatus("current")


class _BsnLocalNetUserLifetime_Type(TimeInterval):
    """Custom type bsnLocalNetUserLifetime based on TimeInterval"""
    defaultValue = 8640000

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(6000, 259200000),
    )


_BsnLocalNetUserLifetime_Type.__name__ = "TimeInterval"
_BsnLocalNetUserLifetime_Object = MibTableColumn
bsnLocalNetUserLifetime = _BsnLocalNetUserLifetime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 10, 1, 5),
    _BsnLocalNetUserLifetime_Type()
)
bsnLocalNetUserLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnLocalNetUserLifetime.setStatus("current")
_BsnLocalNetUserStartTime_Type = TimeTicks
_BsnLocalNetUserStartTime_Object = MibTableColumn
bsnLocalNetUserStartTime = _BsnLocalNetUserStartTime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 10, 1, 6),
    _BsnLocalNetUserStartTime_Type()
)
bsnLocalNetUserStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnLocalNetUserStartTime.setStatus("current")
_BsnLocalNetUserRemainingTime_Type = TimeInterval
_BsnLocalNetUserRemainingTime_Object = MibTableColumn
bsnLocalNetUserRemainingTime = _BsnLocalNetUserRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 10, 1, 7),
    _BsnLocalNetUserRemainingTime_Type()
)
bsnLocalNetUserRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnLocalNetUserRemainingTime.setStatus("current")
_BsnLocalNetUserRowStatus_Type = RowStatus
_BsnLocalNetUserRowStatus_Object = MibTableColumn
bsnLocalNetUserRowStatus = _BsnLocalNetUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 10, 1, 24),
    _BsnLocalNetUserRowStatus_Type()
)
bsnLocalNetUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnLocalNetUserRowStatus.setStatus("current")
_BsnLocalManagementUserTable_Object = MibTable
bsnLocalManagementUserTable = _BsnLocalManagementUserTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 11)
)
if mibBuilder.loadTexts:
    bsnLocalManagementUserTable.setStatus("current")
_BsnLocalManagementUserEntry_Object = MibTableRow
bsnLocalManagementUserEntry = _BsnLocalManagementUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 11, 1)
)
bsnLocalManagementUserEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnLocalManagementUserName"),
)
if mibBuilder.loadTexts:
    bsnLocalManagementUserEntry.setStatus("current")


class _BsnLocalManagementUserName_Type(OctetString):
    """Custom type bsnLocalManagementUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_BsnLocalManagementUserName_Type.__name__ = "OctetString"
_BsnLocalManagementUserName_Object = MibTableColumn
bsnLocalManagementUserName = _BsnLocalManagementUserName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 11, 1, 1),
    _BsnLocalManagementUserName_Type()
)
bsnLocalManagementUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnLocalManagementUserName.setStatus("current")


class _BsnLocalManagementUserPassword_Type(OctetString):
    """Custom type bsnLocalManagementUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_BsnLocalManagementUserPassword_Type.__name__ = "OctetString"
_BsnLocalManagementUserPassword_Object = MibTableColumn
bsnLocalManagementUserPassword = _BsnLocalManagementUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 11, 1, 2),
    _BsnLocalManagementUserPassword_Type()
)
bsnLocalManagementUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnLocalManagementUserPassword.setStatus("current")


class _BsnLocalManagementUserAccessMode_Type(Integer32):
    """Custom type bsnLocalManagementUserAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_BsnLocalManagementUserAccessMode_Type.__name__ = "Integer32"
_BsnLocalManagementUserAccessMode_Object = MibTableColumn
bsnLocalManagementUserAccessMode = _BsnLocalManagementUserAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 11, 1, 3),
    _BsnLocalManagementUserAccessMode_Type()
)
bsnLocalManagementUserAccessMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnLocalManagementUserAccessMode.setStatus("current")
_BsnLocalManagementUserRowStatus_Type = RowStatus
_BsnLocalManagementUserRowStatus_Object = MibTableColumn
bsnLocalManagementUserRowStatus = _BsnLocalManagementUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 11, 1, 23),
    _BsnLocalManagementUserRowStatus_Type()
)
bsnLocalManagementUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnLocalManagementUserRowStatus.setStatus("current")


class _BsnRadiusAuthKeyWrapEnable_Type(TruthValue):
    """Custom type bsnRadiusAuthKeyWrapEnable based on TruthValue"""


_BsnRadiusAuthKeyWrapEnable_Object = MibScalar
bsnRadiusAuthKeyWrapEnable = _BsnRadiusAuthKeyWrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 12),
    _BsnRadiusAuthKeyWrapEnable_Type()
)
bsnRadiusAuthKeyWrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRadiusAuthKeyWrapEnable.setStatus("current")


class _BsnRadiusAuthCacheCredentialsLocally_Type(Integer32):
    """Custom type bsnRadiusAuthCacheCredentialsLocally based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnRadiusAuthCacheCredentialsLocally_Type.__name__ = "Integer32"
_BsnRadiusAuthCacheCredentialsLocally_Object = MibScalar
bsnRadiusAuthCacheCredentialsLocally = _BsnRadiusAuthCacheCredentialsLocally_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 14),
    _BsnRadiusAuthCacheCredentialsLocally_Type()
)
bsnRadiusAuthCacheCredentialsLocally.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRadiusAuthCacheCredentialsLocally.setStatus("deprecated")


class _BsnAAAMacDelimiter_Type(Integer32):
    """Custom type bsnAAAMacDelimiter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("colon", 1),
          ("hyphen", 2),
          ("noDelimiter", 0),
          ("singleHyphen", 3))
    )


_BsnAAAMacDelimiter_Type.__name__ = "Integer32"
_BsnAAAMacDelimiter_Object = MibScalar
bsnAAAMacDelimiter = _BsnAAAMacDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 15),
    _BsnAAAMacDelimiter_Type()
)
bsnAAAMacDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAAAMacDelimiter.setStatus("current")


class _BsnAAARadiusCompatibilityMode_Type(Integer32):
    """Custom type bsnAAARadiusCompatibilityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ciscoACS", 0),
          ("orinocoRadius", 1),
          ("other", 2))
    )


_BsnAAARadiusCompatibilityMode_Type.__name__ = "Integer32"
_BsnAAARadiusCompatibilityMode_Object = MibScalar
bsnAAARadiusCompatibilityMode = _BsnAAARadiusCompatibilityMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 16),
    _BsnAAARadiusCompatibilityMode_Type()
)
bsnAAARadiusCompatibilityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAAARadiusCompatibilityMode.setStatus("current")


class _BsnAAARadiusCallStationIdType_Type(Integer32):
    """Custom type bsnAAARadiusCallStationIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("apGroupName", 6),
          ("apLabelAddress", 12),
          ("apLabelAddressSsid", 13),
          ("apLocation", 8),
          ("apMacAddress", 2),
          ("apMacAddressSsid", 3),
          ("apMacEthAddress", 10),
          ("apMacEthAddressSsid", 11),
          ("apName", 5),
          ("apNameSsid", 4),
          ("apVlanId", 9),
          ("flexGroupName", 7),
          ("ipAddr", 0),
          ("macAddr", 1))
    )


_BsnAAARadiusCallStationIdType_Type.__name__ = "Integer32"
_BsnAAARadiusCallStationIdType_Object = MibScalar
bsnAAARadiusCallStationIdType = _BsnAAARadiusCallStationIdType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 17),
    _BsnAAARadiusCallStationIdType_Type()
)
bsnAAARadiusCallStationIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAAARadiusCallStationIdType.setStatus("current")


class _BsnExternalPolicyServerAclName_Type(DisplayString):
    """Custom type bsnExternalPolicyServerAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BsnExternalPolicyServerAclName_Type.__name__ = "DisplayString"
_BsnExternalPolicyServerAclName_Object = MibScalar
bsnExternalPolicyServerAclName = _BsnExternalPolicyServerAclName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 18),
    _BsnExternalPolicyServerAclName_Type()
)
bsnExternalPolicyServerAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnExternalPolicyServerAclName.setStatus("current")
_BsnExternalPolicyServerTable_Object = MibTable
bsnExternalPolicyServerTable = _BsnExternalPolicyServerTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 19)
)
if mibBuilder.loadTexts:
    bsnExternalPolicyServerTable.setStatus("obsolete")
_BsnExternalPolicyServerEntry_Object = MibTableRow
bsnExternalPolicyServerEntry = _BsnExternalPolicyServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 19, 1)
)
bsnExternalPolicyServerEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnExternalPolicyServerIndex"),
)
if mibBuilder.loadTexts:
    bsnExternalPolicyServerEntry.setStatus("obsolete")


class _BsnExternalPolicyServerIndex_Type(Integer32):
    """Custom type bsnExternalPolicyServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BsnExternalPolicyServerIndex_Type.__name__ = "Integer32"
_BsnExternalPolicyServerIndex_Object = MibTableColumn
bsnExternalPolicyServerIndex = _BsnExternalPolicyServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 19, 1, 1),
    _BsnExternalPolicyServerIndex_Type()
)
bsnExternalPolicyServerIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnExternalPolicyServerIndex.setStatus("obsolete")
_BsnExternalPolicyServerAddress_Type = IpAddress
_BsnExternalPolicyServerAddress_Object = MibTableColumn
bsnExternalPolicyServerAddress = _BsnExternalPolicyServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 19, 1, 2),
    _BsnExternalPolicyServerAddress_Type()
)
bsnExternalPolicyServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnExternalPolicyServerAddress.setStatus("obsolete")


class _BsnExternalPolicyServerPortNumber_Type(Integer32):
    """Custom type bsnExternalPolicyServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BsnExternalPolicyServerPortNumber_Type.__name__ = "Integer32"
_BsnExternalPolicyServerPortNumber_Object = MibTableColumn
bsnExternalPolicyServerPortNumber = _BsnExternalPolicyServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 19, 1, 3),
    _BsnExternalPolicyServerPortNumber_Type()
)
bsnExternalPolicyServerPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnExternalPolicyServerPortNumber.setStatus("obsolete")


class _BsnExternalPolicyServerKey_Type(OctetString):
    """Custom type bsnExternalPolicyServerKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BsnExternalPolicyServerKey_Type.__name__ = "OctetString"
_BsnExternalPolicyServerKey_Object = MibTableColumn
bsnExternalPolicyServerKey = _BsnExternalPolicyServerKey_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 19, 1, 4),
    _BsnExternalPolicyServerKey_Type()
)
bsnExternalPolicyServerKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnExternalPolicyServerKey.setStatus("obsolete")


class _BsnExternalPolicyServerAdminStatus_Type(Integer32):
    """Custom type bsnExternalPolicyServerAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnExternalPolicyServerAdminStatus_Type.__name__ = "Integer32"
_BsnExternalPolicyServerAdminStatus_Object = MibTableColumn
bsnExternalPolicyServerAdminStatus = _BsnExternalPolicyServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 19, 1, 5),
    _BsnExternalPolicyServerAdminStatus_Type()
)
bsnExternalPolicyServerAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnExternalPolicyServerAdminStatus.setStatus("obsolete")


class _BsnExternalPolicyServerConnectionStatus_Type(Integer32):
    """Custom type bsnExternalPolicyServerConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 0))
    )


_BsnExternalPolicyServerConnectionStatus_Type.__name__ = "Integer32"
_BsnExternalPolicyServerConnectionStatus_Object = MibTableColumn
bsnExternalPolicyServerConnectionStatus = _BsnExternalPolicyServerConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 19, 1, 6),
    _BsnExternalPolicyServerConnectionStatus_Type()
)
bsnExternalPolicyServerConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnExternalPolicyServerConnectionStatus.setStatus("obsolete")
_BsnExternalPolicyServerRowStatus_Type = RowStatus
_BsnExternalPolicyServerRowStatus_Object = MibTableColumn
bsnExternalPolicyServerRowStatus = _BsnExternalPolicyServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 19, 1, 26),
    _BsnExternalPolicyServerRowStatus_Type()
)
bsnExternalPolicyServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnExternalPolicyServerRowStatus.setStatus("obsolete")


class _BsnAAALocalDatabaseSize_Type(Integer32):
    """Custom type bsnAAALocalDatabaseSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 2048),
    )


_BsnAAALocalDatabaseSize_Type.__name__ = "Integer32"
_BsnAAALocalDatabaseSize_Object = MibScalar
bsnAAALocalDatabaseSize = _BsnAAALocalDatabaseSize_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 20),
    _BsnAAALocalDatabaseSize_Type()
)
bsnAAALocalDatabaseSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAAALocalDatabaseSize.setStatus("current")


class _BsnAAACurrentLocalDatabaseSize_Type(Integer32):
    """Custom type bsnAAACurrentLocalDatabaseSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 2048),
    )


_BsnAAACurrentLocalDatabaseSize_Type.__name__ = "Integer32"
_BsnAAACurrentLocalDatabaseSize_Object = MibScalar
bsnAAACurrentLocalDatabaseSize = _BsnAAACurrentLocalDatabaseSize_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 21),
    _BsnAAACurrentLocalDatabaseSize_Type()
)
bsnAAACurrentLocalDatabaseSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnAAACurrentLocalDatabaseSize.setStatus("current")
_BsnAPAuthorizationTable_Object = MibTable
bsnAPAuthorizationTable = _BsnAPAuthorizationTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 22)
)
if mibBuilder.loadTexts:
    bsnAPAuthorizationTable.setStatus("current")
_BsnAPAuthorizationEntry_Object = MibTableRow
bsnAPAuthorizationEntry = _BsnAPAuthorizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 22, 1)
)
bsnAPAuthorizationEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPAuthMacAddress"),
)
if mibBuilder.loadTexts:
    bsnAPAuthorizationEntry.setStatus("current")


class _BsnAPAuthMacAddress_Type(OctetString):
    """Custom type bsnAPAuthMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_BsnAPAuthMacAddress_Type.__name__ = "OctetString"
_BsnAPAuthMacAddress_Object = MibTableColumn
bsnAPAuthMacAddress = _BsnAPAuthMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 22, 1, 1),
    _BsnAPAuthMacAddress_Type()
)
bsnAPAuthMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAPAuthMacAddress.setStatus("current")


class _BsnAPAuthCertificateType_Type(Integer32):
    """Custom type bsnAPAuthCertificateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("locMic", 3),
          ("locSsc", 4),
          ("locSsc256", 6),
          ("mic", 1),
          ("none", 5),
          ("ssc", 2),
          ("unknown", 0))
    )


_BsnAPAuthCertificateType_Type.__name__ = "Integer32"
_BsnAPAuthCertificateType_Object = MibTableColumn
bsnAPAuthCertificateType = _BsnAPAuthCertificateType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 22, 1, 2),
    _BsnAPAuthCertificateType_Type()
)
bsnAPAuthCertificateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAPAuthCertificateType.setStatus("current")
_BsnAPAuthHashKey_Type = OctetString
_BsnAPAuthHashKey_Object = MibTableColumn
bsnAPAuthHashKey = _BsnAPAuthHashKey_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 22, 1, 3),
    _BsnAPAuthHashKey_Type()
)
bsnAPAuthHashKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAPAuthHashKey.setStatus("current")
_BsnAPAuthRowStatus_Type = RowStatus
_BsnAPAuthRowStatus_Object = MibTableColumn
bsnAPAuthRowStatus = _BsnAPAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 5, 22, 1, 20),
    _BsnAPAuthRowStatus_Type()
)
bsnAPAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAPAuthRowStatus.setStatus("current")
_BsnTrap_ObjectIdentity = ObjectIdentity
bsnTrap = _BsnTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6)
)
_BsnTrapControl_ObjectIdentity = ObjectIdentity
bsnTrapControl = _BsnTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 1)
)


class _BsnDot11StationTrapControlMask_Type(Unsigned32):
    """Custom type bsnDot11StationTrapControlMask based on Unsigned32"""
    defaultValue = 0


_BsnDot11StationTrapControlMask_Object = MibScalar
bsnDot11StationTrapControlMask = _BsnDot11StationTrapControlMask_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 1, 1),
    _BsnDot11StationTrapControlMask_Type()
)
bsnDot11StationTrapControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnDot11StationTrapControlMask.setStatus("current")


class _BsnAPTrapControlMask_Type(Unsigned32):
    """Custom type bsnAPTrapControlMask based on Unsigned32"""
    defaultValue = 63


_BsnAPTrapControlMask_Object = MibScalar
bsnAPTrapControlMask = _BsnAPTrapControlMask_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 1, 2),
    _BsnAPTrapControlMask_Type()
)
bsnAPTrapControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPTrapControlMask.setStatus("current")
_BsnAPProfileTrapControlMask_Type = Unsigned32
_BsnAPProfileTrapControlMask_Object = MibScalar
bsnAPProfileTrapControlMask = _BsnAPProfileTrapControlMask_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 1, 3),
    _BsnAPProfileTrapControlMask_Type()
)
bsnAPProfileTrapControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPProfileTrapControlMask.setStatus("current")
_BsnAPParamUpdateTrapControlMask_Type = Unsigned32
_BsnAPParamUpdateTrapControlMask_Object = MibScalar
bsnAPParamUpdateTrapControlMask = _BsnAPParamUpdateTrapControlMask_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 1, 4),
    _BsnAPParamUpdateTrapControlMask_Type()
)
bsnAPParamUpdateTrapControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPParamUpdateTrapControlMask.setStatus("current")
_BsnIpsecTrapsMask_Type = Unsigned32
_BsnIpsecTrapsMask_Object = MibScalar
bsnIpsecTrapsMask = _BsnIpsecTrapsMask_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 1, 5),
    _BsnIpsecTrapsMask_Type()
)
bsnIpsecTrapsMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnIpsecTrapsMask.setStatus("current")


class _BsnRogueAPTrapEnable_Type(Integer32):
    """Custom type bsnRogueAPTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnRogueAPTrapEnable_Type.__name__ = "Integer32"
_BsnRogueAPTrapEnable_Object = MibScalar
bsnRogueAPTrapEnable = _BsnRogueAPTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 1, 6),
    _BsnRogueAPTrapEnable_Type()
)
bsnRogueAPTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRogueAPTrapEnable.setStatus("current")


class _BsnRADIUSServerTrapEnable_Type(Integer32):
    """Custom type bsnRADIUSServerTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnRADIUSServerTrapEnable_Type.__name__ = "Integer32"
_BsnRADIUSServerTrapEnable_Object = MibScalar
bsnRADIUSServerTrapEnable = _BsnRADIUSServerTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 1, 7),
    _BsnRADIUSServerTrapEnable_Type()
)
bsnRADIUSServerTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnRADIUSServerTrapEnable.setStatus("current")


class _BsnAuthenticationFailureTrapEnable_Type(Integer32):
    """Custom type bsnAuthenticationFailureTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnAuthenticationFailureTrapEnable_Type.__name__ = "Integer32"
_BsnAuthenticationFailureTrapEnable_Object = MibScalar
bsnAuthenticationFailureTrapEnable = _BsnAuthenticationFailureTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 1, 8),
    _BsnAuthenticationFailureTrapEnable_Type()
)
bsnAuthenticationFailureTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAuthenticationFailureTrapEnable.setStatus("current")


class _BsnConfigSaveTrapEnable_Type(Integer32):
    """Custom type bsnConfigSaveTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnConfigSaveTrapEnable_Type.__name__ = "Integer32"
_BsnConfigSaveTrapEnable_Object = MibScalar
bsnConfigSaveTrapEnable = _BsnConfigSaveTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 1, 9),
    _BsnConfigSaveTrapEnable_Type()
)
bsnConfigSaveTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnConfigSaveTrapEnable.setStatus("current")


class _Bsn80211SecurityTrapControlMask_Type(Unsigned32):
    """Custom type bsn80211SecurityTrapControlMask based on Unsigned32"""
    defaultValue = 0


_Bsn80211SecurityTrapControlMask_Object = MibScalar
bsn80211SecurityTrapControlMask = _Bsn80211SecurityTrapControlMask_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 1, 10),
    _Bsn80211SecurityTrapControlMask_Type()
)
bsn80211SecurityTrapControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsn80211SecurityTrapControlMask.setStatus("current")


class _BsnWpsTrapControlEnable_Type(Integer32):
    """Custom type bsnWpsTrapControlEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnWpsTrapControlEnable_Type.__name__ = "Integer32"
_BsnWpsTrapControlEnable_Object = MibScalar
bsnWpsTrapControlEnable = _BsnWpsTrapControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 1, 11),
    _BsnWpsTrapControlEnable_Type()
)
bsnWpsTrapControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnWpsTrapControlEnable.setStatus("current")
_BsnTrapVariable_ObjectIdentity = ObjectIdentity
bsnTrapVariable = _BsnTrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2)
)


class _BsnAuthFailureUserName_Type(OctetString):
    """Custom type bsnAuthFailureUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BsnAuthFailureUserName_Type.__name__ = "OctetString"
_BsnAuthFailureUserName_Object = MibScalar
bsnAuthFailureUserName = _BsnAuthFailureUserName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 1),
    _BsnAuthFailureUserName_Type()
)
bsnAuthFailureUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnAuthFailureUserName.setStatus("current")


class _BsnAuthFailureUserType_Type(Integer32):
    """Custom type bsnAuthFailureUserType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("macFilter", 3),
          ("mgmtUser", 1),
          ("wlanUser", 2))
    )


_BsnAuthFailureUserType_Type.__name__ = "Integer32"
_BsnAuthFailureUserType_Object = MibScalar
bsnAuthFailureUserType = _BsnAuthFailureUserType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 2),
    _BsnAuthFailureUserType_Type()
)
bsnAuthFailureUserType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnAuthFailureUserType.setStatus("current")
_BsnRemoteIPv4Address_Type = IpAddress
_BsnRemoteIPv4Address_Object = MibScalar
bsnRemoteIPv4Address = _BsnRemoteIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 3),
    _BsnRemoteIPv4Address_Type()
)
bsnRemoteIPv4Address.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnRemoteIPv4Address.setStatus("current")
_BsnIpsecErrorCount_Type = Integer32
_BsnIpsecErrorCount_Object = MibScalar
bsnIpsecErrorCount = _BsnIpsecErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 4),
    _BsnIpsecErrorCount_Type()
)
bsnIpsecErrorCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnIpsecErrorCount.setStatus("current")
_BsnIpsecSPI_Type = Integer32
_BsnIpsecSPI_Object = MibScalar
bsnIpsecSPI = _BsnIpsecSPI_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 5),
    _BsnIpsecSPI_Type()
)
bsnIpsecSPI.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnIpsecSPI.setStatus("current")


class _BsnRemoteUdpPort_Type(Integer32):
    """Custom type bsnRemoteUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BsnRemoteUdpPort_Type.__name__ = "Integer32"
_BsnRemoteUdpPort_Object = MibScalar
bsnRemoteUdpPort = _BsnRemoteUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 6),
    _BsnRemoteUdpPort_Type()
)
bsnRemoteUdpPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnRemoteUdpPort.setStatus("current")
_BsnIkeAuthMethod_Type = Integer32
_BsnIkeAuthMethod_Object = MibScalar
bsnIkeAuthMethod = _BsnIkeAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 7),
    _BsnIkeAuthMethod_Type()
)
bsnIkeAuthMethod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnIkeAuthMethod.setStatus("current")
_BsnIkeTotalInitFailures_Type = Integer32
_BsnIkeTotalInitFailures_Object = MibScalar
bsnIkeTotalInitFailures = _BsnIkeTotalInitFailures_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 8),
    _BsnIkeTotalInitFailures_Type()
)
bsnIkeTotalInitFailures.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnIkeTotalInitFailures.setStatus("current")
_BsnIkeTotalInitNoResponses_Type = Integer32
_BsnIkeTotalInitNoResponses_Object = MibScalar
bsnIkeTotalInitNoResponses = _BsnIkeTotalInitNoResponses_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 9),
    _BsnIkeTotalInitNoResponses_Type()
)
bsnIkeTotalInitNoResponses.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnIkeTotalInitNoResponses.setStatus("current")
_BsnIkeTotalRespFailures_Type = Integer32
_BsnIkeTotalRespFailures_Object = MibScalar
bsnIkeTotalRespFailures = _BsnIkeTotalRespFailures_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 10),
    _BsnIkeTotalRespFailures_Type()
)
bsnIkeTotalRespFailures.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnIkeTotalRespFailures.setStatus("current")
_BsnNotifiesSent_Type = Integer32
_BsnNotifiesSent_Object = MibScalar
bsnNotifiesSent = _BsnNotifiesSent_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 11),
    _BsnNotifiesSent_Type()
)
bsnNotifiesSent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnNotifiesSent.setStatus("current")
_BsnNotifiesReceived_Type = Integer32
_BsnNotifiesReceived_Object = MibScalar
bsnNotifiesReceived = _BsnNotifiesReceived_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 12),
    _BsnNotifiesReceived_Type()
)
bsnNotifiesReceived.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnNotifiesReceived.setStatus("current")
_BsnSuiteInitFailures_Type = Integer32
_BsnSuiteInitFailures_Object = MibScalar
bsnSuiteInitFailures = _BsnSuiteInitFailures_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 13),
    _BsnSuiteInitFailures_Type()
)
bsnSuiteInitFailures.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnSuiteInitFailures.setStatus("current")
_BsnSuiteRespondFailures_Type = Integer32
_BsnSuiteRespondFailures_Object = MibScalar
bsnSuiteRespondFailures = _BsnSuiteRespondFailures_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 14),
    _BsnSuiteRespondFailures_Type()
)
bsnSuiteRespondFailures.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnSuiteRespondFailures.setStatus("current")


class _BsnInitiatorCookie_Type(OctetString):
    """Custom type bsnInitiatorCookie based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_BsnInitiatorCookie_Type.__name__ = "OctetString"
_BsnInitiatorCookie_Object = MibScalar
bsnInitiatorCookie = _BsnInitiatorCookie_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 15),
    _BsnInitiatorCookie_Type()
)
bsnInitiatorCookie.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnInitiatorCookie.setStatus("current")


class _BsnResponderCookie_Type(OctetString):
    """Custom type bsnResponderCookie based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_BsnResponderCookie_Type.__name__ = "OctetString"
_BsnResponderCookie_Object = MibScalar
bsnResponderCookie = _BsnResponderCookie_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 16),
    _BsnResponderCookie_Type()
)
bsnResponderCookie.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnResponderCookie.setStatus("current")
_BsnIsakmpInvalidCookies_Type = Integer32
_BsnIsakmpInvalidCookies_Object = MibScalar
bsnIsakmpInvalidCookies = _BsnIsakmpInvalidCookies_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 17),
    _BsnIsakmpInvalidCookies_Type()
)
bsnIsakmpInvalidCookies.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnIsakmpInvalidCookies.setStatus("current")
_BsnCurrentRadiosCount_Type = Integer32
_BsnCurrentRadiosCount_Object = MibScalar
bsnCurrentRadiosCount = _BsnCurrentRadiosCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 18),
    _BsnCurrentRadiosCount_Type()
)
bsnCurrentRadiosCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnCurrentRadiosCount.setStatus("current")
_BsnLicenseRadioCount_Type = Integer32
_BsnLicenseRadioCount_Object = MibScalar
bsnLicenseRadioCount = _BsnLicenseRadioCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 19),
    _BsnLicenseRadioCount_Type()
)
bsnLicenseRadioCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnLicenseRadioCount.setStatus("current")
_BsnAPMacAddrTrapVariable_Type = MacAddress
_BsnAPMacAddrTrapVariable_Object = MibScalar
bsnAPMacAddrTrapVariable = _BsnAPMacAddrTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 20),
    _BsnAPMacAddrTrapVariable_Type()
)
bsnAPMacAddrTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnAPMacAddrTrapVariable.setStatus("current")
_BsnAPNameTrapVariable_Type = DisplayString
_BsnAPNameTrapVariable_Object = MibScalar
bsnAPNameTrapVariable = _BsnAPNameTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 21),
    _BsnAPNameTrapVariable_Type()
)
bsnAPNameTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnAPNameTrapVariable.setStatus("current")
_BsnAPSlotIdTrapVariable_Type = Integer32
_BsnAPSlotIdTrapVariable_Object = MibScalar
bsnAPSlotIdTrapVariable = _BsnAPSlotIdTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 22),
    _BsnAPSlotIdTrapVariable_Type()
)
bsnAPSlotIdTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnAPSlotIdTrapVariable.setStatus("current")
_BsnAPChannelNumberTrapVariable_Type = Integer32
_BsnAPChannelNumberTrapVariable_Object = MibScalar
bsnAPChannelNumberTrapVariable = _BsnAPChannelNumberTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 23),
    _BsnAPChannelNumberTrapVariable_Type()
)
bsnAPChannelNumberTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnAPChannelNumberTrapVariable.setStatus("current")
_BsnAPCoverageThresholdTrapVariable_Type = Integer32
_BsnAPCoverageThresholdTrapVariable_Object = MibScalar
bsnAPCoverageThresholdTrapVariable = _BsnAPCoverageThresholdTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 24),
    _BsnAPCoverageThresholdTrapVariable_Type()
)
bsnAPCoverageThresholdTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnAPCoverageThresholdTrapVariable.setStatus("current")
_BsnAPCoverageFailedClients_Type = Integer32
_BsnAPCoverageFailedClients_Object = MibScalar
bsnAPCoverageFailedClients = _BsnAPCoverageFailedClients_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 25),
    _BsnAPCoverageFailedClients_Type()
)
bsnAPCoverageFailedClients.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnAPCoverageFailedClients.setStatus("current")
_BsnAPCoverageTotalClients_Type = Integer32
_BsnAPCoverageTotalClients_Object = MibScalar
bsnAPCoverageTotalClients = _BsnAPCoverageTotalClients_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 26),
    _BsnAPCoverageTotalClients_Type()
)
bsnAPCoverageTotalClients.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnAPCoverageTotalClients.setStatus("current")
_BsnClientMacAddr_Type = MacAddress
_BsnClientMacAddr_Object = MibScalar
bsnClientMacAddr = _BsnClientMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 27),
    _BsnClientMacAddr_Type()
)
bsnClientMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnClientMacAddr.setStatus("current")
_BsnClientRssi_Type = Integer32
_BsnClientRssi_Object = MibScalar
bsnClientRssi = _BsnClientRssi_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 28),
    _BsnClientRssi_Type()
)
bsnClientRssi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnClientRssi.setStatus("current")
_BsnClientSnr_Type = Integer32
_BsnClientSnr_Object = MibScalar
bsnClientSnr = _BsnClientSnr_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 29),
    _BsnClientSnr_Type()
)
bsnClientSnr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnClientSnr.setStatus("current")
_BsnInterferenceEnergyBeforeChannelUpdate_Type = Integer32
_BsnInterferenceEnergyBeforeChannelUpdate_Object = MibScalar
bsnInterferenceEnergyBeforeChannelUpdate = _BsnInterferenceEnergyBeforeChannelUpdate_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 30),
    _BsnInterferenceEnergyBeforeChannelUpdate_Type()
)
bsnInterferenceEnergyBeforeChannelUpdate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnInterferenceEnergyBeforeChannelUpdate.setStatus("current")
_BsnInterferenceEnergyAfterChannelUpdate_Type = Integer32
_BsnInterferenceEnergyAfterChannelUpdate_Object = MibScalar
bsnInterferenceEnergyAfterChannelUpdate = _BsnInterferenceEnergyAfterChannelUpdate_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 31),
    _BsnInterferenceEnergyAfterChannelUpdate_Type()
)
bsnInterferenceEnergyAfterChannelUpdate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnInterferenceEnergyAfterChannelUpdate.setStatus("current")
_BsnAPPortNumberTrapVariable_Type = Integer32
_BsnAPPortNumberTrapVariable_Object = MibScalar
bsnAPPortNumberTrapVariable = _BsnAPPortNumberTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 32),
    _BsnAPPortNumberTrapVariable_Type()
)
bsnAPPortNumberTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnAPPortNumberTrapVariable.setStatus("current")
_BsnMaxRogueCount_Type = Integer32
_BsnMaxRogueCount_Object = MibScalar
bsnMaxRogueCount = _BsnMaxRogueCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 33),
    _BsnMaxRogueCount_Type()
)
bsnMaxRogueCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnMaxRogueCount.setStatus("current")
_BsnStationMacAddress_Type = MacAddress
_BsnStationMacAddress_Object = MibScalar
bsnStationMacAddress = _BsnStationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 34),
    _BsnStationMacAddress_Type()
)
bsnStationMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnStationMacAddress.setStatus("current")
_BsnStationAPMacAddr_Type = MacAddress
_BsnStationAPMacAddr_Object = MibScalar
bsnStationAPMacAddr = _BsnStationAPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 35),
    _BsnStationAPMacAddr_Type()
)
bsnStationAPMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnStationAPMacAddr.setStatus("current")


class _BsnStationAPIfSlotId_Type(Integer32):
    """Custom type bsnStationAPIfSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_BsnStationAPIfSlotId_Type.__name__ = "Integer32"
_BsnStationAPIfSlotId_Object = MibScalar
bsnStationAPIfSlotId = _BsnStationAPIfSlotId_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 36),
    _BsnStationAPIfSlotId_Type()
)
bsnStationAPIfSlotId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnStationAPIfSlotId.setStatus("current")


class _BsnStationReasonCode_Type(Integer32):
    """Custom type bsnStationReasonCode based on Integer32"""
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
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              99,
              101,
              105,
              106,
              200,
              201,
              202,
              203)
        )
    )
    namedValues = NamedValues(
        *(("akmpInvalid", 43),
          ("cipherSuiteRejected", 46),
          ("class2FrameFromNonAssStation", 7),
          ("class2FrameFromNonAuthStation", 6),
          ("deauthenticationLeaving", 3),
          ("disassociationAPBusy", 5),
          ("disassociationDueToInactivity", 4),
          ("disassociationStaHasLeft", 8),
          ("groupCipherInvalid", 41),
          ("inSufficientBandwidth", 202),
          ("inValidQosParams", 203),
          ("invalidInformationElement", 40),
          ("invalidRsnIeCapabilities", 45),
          ("maxAssociatedClientsReached", 101),
          ("maxAssociatedClientsReachedOnRadio", 105),
          ("maxAssociatedClientsReachedOnWlan", 106),
          ("missingReasonCode", 99),
          ("previousAuthNotValid", 2),
          ("qosPolicyMismatch", 201),
          ("staReqAssociationWithoutAuth", 9),
          ("unSpecifiedQosFailure", 200),
          ("unicastCipherInvalid", 42),
          ("unspecified", 1),
          ("unsupportedRsnVersion", 44))
    )


_BsnStationReasonCode_Type.__name__ = "Integer32"
_BsnStationReasonCode_Object = MibScalar
bsnStationReasonCode = _BsnStationReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 37),
    _BsnStationReasonCode_Type()
)
bsnStationReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnStationReasonCode.setStatus("current")


class _BsnStationBlacklistingReasonCode_Type(Integer32):
    """Custom type bsnStationBlacklistingReasonCode based on Integer32"""
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
        *(("failed80211Auth", 1),
          ("failed8021xAuth", 4),
          ("failedAssociation", 2),
          ("failedWebAuth", 5),
          ("ipTheft", 3))
    )


_BsnStationBlacklistingReasonCode_Type.__name__ = "Integer32"
_BsnStationBlacklistingReasonCode_Object = MibScalar
bsnStationBlacklistingReasonCode = _BsnStationBlacklistingReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 38),
    _BsnStationBlacklistingReasonCode_Type()
)
bsnStationBlacklistingReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnStationBlacklistingReasonCode.setStatus("current")
_BsnStationUserName_Type = DisplayString
_BsnStationUserName_Object = MibScalar
bsnStationUserName = _BsnStationUserName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 39),
    _BsnStationUserName_Type()
)
bsnStationUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnStationUserName.setStatus("current")


class _BsnRogueAPOnWiredNetwork_Type(Integer32):
    """Custom type bsnRogueAPOnWiredNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_BsnRogueAPOnWiredNetwork_Type.__name__ = "Integer32"
_BsnRogueAPOnWiredNetwork_Object = MibScalar
bsnRogueAPOnWiredNetwork = _BsnRogueAPOnWiredNetwork_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 40),
    _BsnRogueAPOnWiredNetwork_Type()
)
bsnRogueAPOnWiredNetwork.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnRogueAPOnWiredNetwork.setStatus("current")
_BsnNavDosAttackSourceMacAddr_Type = MacAddress
_BsnNavDosAttackSourceMacAddr_Object = MibScalar
bsnNavDosAttackSourceMacAddr = _BsnNavDosAttackSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 41),
    _BsnNavDosAttackSourceMacAddr_Type()
)
bsnNavDosAttackSourceMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnNavDosAttackSourceMacAddr.setStatus("current")


class _BsnWlanIdTrapVariable_Type(Integer32):
    """Custom type bsnWlanIdTrapVariable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 517),
    )


_BsnWlanIdTrapVariable_Type.__name__ = "Integer32"
_BsnWlanIdTrapVariable_Object = MibScalar
bsnWlanIdTrapVariable = _BsnWlanIdTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 42),
    _BsnWlanIdTrapVariable_Type()
)
bsnWlanIdTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnWlanIdTrapVariable.setStatus("current")
_BsnUserIpAddress_Type = IpAddress
_BsnUserIpAddress_Object = MibScalar
bsnUserIpAddress = _BsnUserIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 43),
    _BsnUserIpAddress_Type()
)
bsnUserIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnUserIpAddress.setStatus("current")


class _BsnRogueAdhocMode_Type(Integer32):
    """Custom type bsnRogueAdhocMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_BsnRogueAdhocMode_Type.__name__ = "Integer32"
_BsnRogueAdhocMode_Object = MibScalar
bsnRogueAdhocMode = _BsnRogueAdhocMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 44),
    _BsnRogueAdhocMode_Type()
)
bsnRogueAdhocMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnRogueAdhocMode.setStatus("current")


class _BsnClearTrapVariable_Type(Integer32):
    """Custom type bsnClearTrapVariable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_BsnClearTrapVariable_Type.__name__ = "Integer32"
_BsnClearTrapVariable_Object = MibScalar
bsnClearTrapVariable = _BsnClearTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 45),
    _BsnClearTrapVariable_Type()
)
bsnClearTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnClearTrapVariable.setStatus("current")
_BsnDuplicateIpTrapVariable_Type = IpAddress
_BsnDuplicateIpTrapVariable_Object = MibScalar
bsnDuplicateIpTrapVariable = _BsnDuplicateIpTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 46),
    _BsnDuplicateIpTrapVariable_Type()
)
bsnDuplicateIpTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnDuplicateIpTrapVariable.setStatus("current")


class _BsnDuplicateIpTrapClear_Type(Integer32):
    """Custom type bsnDuplicateIpTrapClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_BsnDuplicateIpTrapClear_Type.__name__ = "Integer32"
_BsnDuplicateIpTrapClear_Object = MibScalar
bsnDuplicateIpTrapClear = _BsnDuplicateIpTrapClear_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 47),
    _BsnDuplicateIpTrapClear_Type()
)
bsnDuplicateIpTrapClear.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnDuplicateIpTrapClear.setStatus("current")


class _BsnDuplicateIpReportedByAP_Type(Integer32):
    """Custom type bsnDuplicateIpReportedByAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_BsnDuplicateIpReportedByAP_Type.__name__ = "Integer32"
_BsnDuplicateIpReportedByAP_Object = MibScalar
bsnDuplicateIpReportedByAP = _BsnDuplicateIpReportedByAP_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 48),
    _BsnDuplicateIpReportedByAP_Type()
)
bsnDuplicateIpReportedByAP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnDuplicateIpReportedByAP.setStatus("current")


class _BsnTrustedApRadioPolicyRequired_Type(Integer32):
    """Custom type bsnTrustedApRadioPolicyRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 2),
          ("dot11b", 1),
          ("dot11bg", 3),
          ("none", 0))
    )


_BsnTrustedApRadioPolicyRequired_Type.__name__ = "Integer32"
_BsnTrustedApRadioPolicyRequired_Object = MibScalar
bsnTrustedApRadioPolicyRequired = _BsnTrustedApRadioPolicyRequired_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 49),
    _BsnTrustedApRadioPolicyRequired_Type()
)
bsnTrustedApRadioPolicyRequired.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnTrustedApRadioPolicyRequired.setStatus("current")


class _BsnTrustedApEncryptionUsed_Type(Integer32):
    """Custom type bsnTrustedApEncryptionUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("open", 1),
          ("wep", 2),
          ("wpa", 3))
    )


_BsnTrustedApEncryptionUsed_Type.__name__ = "Integer32"
_BsnTrustedApEncryptionUsed_Object = MibScalar
bsnTrustedApEncryptionUsed = _BsnTrustedApEncryptionUsed_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 50),
    _BsnTrustedApEncryptionUsed_Type()
)
bsnTrustedApEncryptionUsed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnTrustedApEncryptionUsed.setStatus("current")


class _BsnTrustedApEncryptionRequired_Type(Integer32):
    """Custom type bsnTrustedApEncryptionRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("open", 1),
          ("wep", 2),
          ("wpa", 3))
    )


_BsnTrustedApEncryptionRequired_Type.__name__ = "Integer32"
_BsnTrustedApEncryptionRequired_Object = MibScalar
bsnTrustedApEncryptionRequired = _BsnTrustedApEncryptionRequired_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 51),
    _BsnTrustedApEncryptionRequired_Type()
)
bsnTrustedApEncryptionRequired.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnTrustedApEncryptionRequired.setStatus("current")


class _BsnTrustedApRadioPolicyUsed_Type(Integer32):
    """Custom type bsnTrustedApRadioPolicyUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 2),
          ("dot11b", 1),
          ("dot11bg", 3),
          ("none", 0))
    )


_BsnTrustedApRadioPolicyUsed_Type.__name__ = "Integer32"
_BsnTrustedApRadioPolicyUsed_Object = MibScalar
bsnTrustedApRadioPolicyUsed = _BsnTrustedApRadioPolicyUsed_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 52),
    _BsnTrustedApRadioPolicyUsed_Type()
)
bsnTrustedApRadioPolicyUsed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnTrustedApRadioPolicyUsed.setStatus("current")


class _BsnNetworkType_Type(Integer32):
    """Custom type bsnNetworkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 2),
          ("dot11b", 1))
    )


_BsnNetworkType_Type.__name__ = "Integer32"
_BsnNetworkType_Object = MibScalar
bsnNetworkType = _BsnNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 53),
    _BsnNetworkType_Type()
)
bsnNetworkType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnNetworkType.setStatus("current")


class _BsnNetworkState_Type(Integer32):
    """Custom type bsnNetworkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnNetworkState_Type.__name__ = "Integer32"
_BsnNetworkState_Object = MibScalar
bsnNetworkState = _BsnNetworkState_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 54),
    _BsnNetworkState_Type()
)
bsnNetworkState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnNetworkState.setStatus("current")


class _BsnSignatureType_Type(Integer32):
    """Custom type bsnSignatureType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("custom", 1),
          ("standard", 0))
    )


_BsnSignatureType_Type.__name__ = "Integer32"
_BsnSignatureType_Object = MibScalar
bsnSignatureType = _BsnSignatureType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 55),
    _BsnSignatureType_Type()
)
bsnSignatureType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnSignatureType.setStatus("current")


class _BsnSignatureName_Type(DisplayString):
    """Custom type bsnSignatureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BsnSignatureName_Type.__name__ = "DisplayString"
_BsnSignatureName_Object = MibScalar
bsnSignatureName = _BsnSignatureName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 56),
    _BsnSignatureName_Type()
)
bsnSignatureName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnSignatureName.setStatus("current")


class _BsnSignatureDescription_Type(DisplayString):
    """Custom type bsnSignatureDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_BsnSignatureDescription_Type.__name__ = "DisplayString"
_BsnSignatureDescription_Object = MibScalar
bsnSignatureDescription = _BsnSignatureDescription_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 57),
    _BsnSignatureDescription_Type()
)
bsnSignatureDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnSignatureDescription.setStatus("current")
_BsnImpersonatedAPMacAddr_Type = MacAddress
_BsnImpersonatedAPMacAddr_Object = MibScalar
bsnImpersonatedAPMacAddr = _BsnImpersonatedAPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 58),
    _BsnImpersonatedAPMacAddr_Type()
)
bsnImpersonatedAPMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnImpersonatedAPMacAddr.setStatus("current")


class _BsnTrustedApPreambleUsed_Type(Integer32):
    """Custom type bsnTrustedApPreambleUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 2),
          ("none", 0),
          ("short", 1))
    )


_BsnTrustedApPreambleUsed_Type.__name__ = "Integer32"
_BsnTrustedApPreambleUsed_Object = MibScalar
bsnTrustedApPreambleUsed = _BsnTrustedApPreambleUsed_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 59),
    _BsnTrustedApPreambleUsed_Type()
)
bsnTrustedApPreambleUsed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnTrustedApPreambleUsed.setStatus("current")


class _BsnTrustedApPreambleRequired_Type(Integer32):
    """Custom type bsnTrustedApPreambleRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 2),
          ("none", 0),
          ("short", 1))
    )


_BsnTrustedApPreambleRequired_Type.__name__ = "Integer32"
_BsnTrustedApPreambleRequired_Object = MibScalar
bsnTrustedApPreambleRequired = _BsnTrustedApPreambleRequired_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 60),
    _BsnTrustedApPreambleRequired_Type()
)
bsnTrustedApPreambleRequired.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnTrustedApPreambleRequired.setStatus("current")


class _BsnSignatureAttackPreced_Type(Integer32):
    """Custom type bsnSignatureAttackPreced based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BsnSignatureAttackPreced_Type.__name__ = "Integer32"
_BsnSignatureAttackPreced_Object = MibScalar
bsnSignatureAttackPreced = _BsnSignatureAttackPreced_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 61),
    _BsnSignatureAttackPreced_Type()
)
bsnSignatureAttackPreced.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnSignatureAttackPreced.setStatus("current")


class _BsnSignatureAttackFrequency_Type(Integer32):
    """Custom type bsnSignatureAttackFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BsnSignatureAttackFrequency_Type.__name__ = "Integer32"
_BsnSignatureAttackFrequency_Object = MibScalar
bsnSignatureAttackFrequency = _BsnSignatureAttackFrequency_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 62),
    _BsnSignatureAttackFrequency_Type()
)
bsnSignatureAttackFrequency.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnSignatureAttackFrequency.setStatus("current")


class _BsnSignatureAttackChannel_Type(Integer32):
    """Custom type bsnSignatureAttackChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BsnSignatureAttackChannel_Type.__name__ = "Integer32"
_BsnSignatureAttackChannel_Object = MibScalar
bsnSignatureAttackChannel = _BsnSignatureAttackChannel_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 63),
    _BsnSignatureAttackChannel_Type()
)
bsnSignatureAttackChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnSignatureAttackChannel.setStatus("current")
_BsnSignatureAttackerMacAddress_Type = MacAddress
_BsnSignatureAttackerMacAddress_Object = MibScalar
bsnSignatureAttackerMacAddress = _BsnSignatureAttackerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 64),
    _BsnSignatureAttackerMacAddress_Type()
)
bsnSignatureAttackerMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnSignatureAttackerMacAddress.setStatus("current")


class _BsnLicenseKeyTrapVariable_Type(OctetString):
    """Custom type bsnLicenseKeyTrapVariable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BsnLicenseKeyTrapVariable_Type.__name__ = "OctetString"
_BsnLicenseKeyTrapVariable_Object = MibScalar
bsnLicenseKeyTrapVariable = _BsnLicenseKeyTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 65),
    _BsnLicenseKeyTrapVariable_Type()
)
bsnLicenseKeyTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnLicenseKeyTrapVariable.setStatus("current")


class _BsnApFunctionalityDisableReasonCode_Type(Integer32):
    """Custom type bsnApFunctionalityDisableReasonCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("licenseKeyDeleted", 2),
          ("licenseKeyExpired", 1),
          ("licenseKeyFeatureMismatch", 3),
          ("unknown", 0))
    )


_BsnApFunctionalityDisableReasonCode_Type.__name__ = "Integer32"
_BsnApFunctionalityDisableReasonCode_Object = MibScalar
bsnApFunctionalityDisableReasonCode = _BsnApFunctionalityDisableReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 66),
    _BsnApFunctionalityDisableReasonCode_Type()
)
bsnApFunctionalityDisableReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnApFunctionalityDisableReasonCode.setStatus("current")


class _BsnLicenseKeyFeatureSetTrapVariable_Type(Integer32):
    """Custom type bsnLicenseKeyFeatureSetTrapVariable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("wps", 1))
    )


_BsnLicenseKeyFeatureSetTrapVariable_Type.__name__ = "Integer32"
_BsnLicenseKeyFeatureSetTrapVariable_Object = MibScalar
bsnLicenseKeyFeatureSetTrapVariable = _BsnLicenseKeyFeatureSetTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 67),
    _BsnLicenseKeyFeatureSetTrapVariable_Type()
)
bsnLicenseKeyFeatureSetTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnLicenseKeyFeatureSetTrapVariable.setStatus("current")


class _BsnApRegulatoryDomain_Type(Integer32):
    """Custom type bsnApRegulatoryDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              6,
              9,
              16,
              21,
              32,
              33,
              34,
              35,
              48,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("a", 0),
          ("c", 16),
          ("e", 1),
          ("i", 6),
          ("j", 9),
          ("k", 32),
          ("n", 21),
          ("notavailable", 65535),
          ("p", 33),
          ("r", 48),
          ("s", 34),
          ("t", 35))
    )


_BsnApRegulatoryDomain_Type.__name__ = "Integer32"
_BsnApRegulatoryDomain_Object = MibScalar
bsnApRegulatoryDomain = _BsnApRegulatoryDomain_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 68),
    _BsnApRegulatoryDomain_Type()
)
bsnApRegulatoryDomain.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnApRegulatoryDomain.setStatus("current")


class _BsnAPAuthorizationFailureCause_Type(Integer32):
    """Custom type bsnAPAuthorizationFailureCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("aaaEntryDoesNotExist", 5),
          ("entryIsMIC", 4),
          ("entrydoesnotexist", 2),
          ("invalidCertifcate", 3),
          ("keymismatch", 1),
          ("unknown", 0))
    )


_BsnAPAuthorizationFailureCause_Type.__name__ = "Integer32"
_BsnAPAuthorizationFailureCause_Object = MibScalar
bsnAPAuthorizationFailureCause = _BsnAPAuthorizationFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 69),
    _BsnAPAuthorizationFailureCause_Type()
)
bsnAPAuthorizationFailureCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnAPAuthorizationFailureCause.setStatus("current")


class _BsnAPIfUpDownCause_Type(Integer32):
    """Custom type bsnAPIfUpDownCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("adminConfigured", 8),
          ("configAP", 5),
          ("configNetwork", 7),
          ("configRadio", 6),
          ("detectingInLinePower", 10),
          ("echoTimeout", 4),
          ("maxRetransmission", 3),
          ("missedRekey", 9),
          ("newDiscovery", 11),
          ("radioFailure", 1),
          ("radioLowPower", 2),
          ("unknown", 0))
    )


_BsnAPIfUpDownCause_Type.__name__ = "Integer32"
_BsnAPIfUpDownCause_Object = MibScalar
bsnAPIfUpDownCause = _BsnAPIfUpDownCause_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 70),
    _BsnAPIfUpDownCause_Type()
)
bsnAPIfUpDownCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnAPIfUpDownCause.setStatus("current")


class _BsnAPInvalidRadioType_Type(Integer32):
    """Custom type bsnAPInvalidRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("unsupportedRadio", 0)
    )


_BsnAPInvalidRadioType_Type.__name__ = "Integer32"
_BsnAPInvalidRadioType_Object = MibScalar
bsnAPInvalidRadioType = _BsnAPInvalidRadioType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 71),
    _BsnAPInvalidRadioType_Type()
)
bsnAPInvalidRadioType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnAPInvalidRadioType.setStatus("current")


class _LocationNotifyContent_Type(OctetString):
    """Custom type locationNotifyContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_LocationNotifyContent_Type.__name__ = "OctetString"
_LocationNotifyContent_Object = MibScalar
locationNotifyContent = _LocationNotifyContent_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 72),
    _LocationNotifyContent_Type()
)
locationNotifyContent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    locationNotifyContent.setStatus("current")
_BsnSignatureMacInfo_Type = BsnTxtSignatureMacInfo
_BsnSignatureMacInfo_Object = MibScalar
bsnSignatureMacInfo = _BsnSignatureMacInfo_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 73),
    _BsnSignatureMacInfo_Type()
)
bsnSignatureMacInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnSignatureMacInfo.setStatus("current")
_BsnImpersonatingSourceMacAddr_Type = MacAddress
_BsnImpersonatingSourceMacAddr_Object = MibScalar
bsnImpersonatingSourceMacAddr = _BsnImpersonatingSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 74),
    _BsnImpersonatingSourceMacAddr_Type()
)
bsnImpersonatingSourceMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnImpersonatingSourceMacAddr.setStatus("current")
_BsnAPPreviousChannelNumberTrapVariable_Type = Integer32
_BsnAPPreviousChannelNumberTrapVariable_Object = MibScalar
bsnAPPreviousChannelNumberTrapVariable = _BsnAPPreviousChannelNumberTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 83),
    _BsnAPPreviousChannelNumberTrapVariable_Type()
)
bsnAPPreviousChannelNumberTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnAPPreviousChannelNumberTrapVariable.setStatus("current")


class _BsnAPReasonCodeTrapVariable_Type(Bits):
    """Custom type bsnAPReasonCodeTrapVariable based on Bits"""
    namedValues = NamedValues(
        *(("deviceAware", 6),
          ("interference", 3),
          ("load", 4),
          ("majorSIAQEvent", 7),
          ("noReason", 0),
          ("noise", 2),
          ("radar", 5),
          ("radarClear", 8),
          ("signal", 1),
          ("userInput", 9))
    )

_BsnAPReasonCodeTrapVariable_Type.__name__ = "Bits"
_BsnAPReasonCodeTrapVariable_Object = MibScalar
bsnAPReasonCodeTrapVariable = _BsnAPReasonCodeTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 84),
    _BsnAPReasonCodeTrapVariable_Type()
)
bsnAPReasonCodeTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnAPReasonCodeTrapVariable.setStatus("current")
_BsnNoiseBeforeChannelUpdate_Type = Integer32
_BsnNoiseBeforeChannelUpdate_Object = MibScalar
bsnNoiseBeforeChannelUpdate = _BsnNoiseBeforeChannelUpdate_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 85),
    _BsnNoiseBeforeChannelUpdate_Type()
)
bsnNoiseBeforeChannelUpdate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnNoiseBeforeChannelUpdate.setStatus("current")
_BsnNoiseAfterChannelUpdate_Type = Integer32
_BsnNoiseAfterChannelUpdate_Object = MibScalar
bsnNoiseAfterChannelUpdate = _BsnNoiseAfterChannelUpdate_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 86),
    _BsnNoiseAfterChannelUpdate_Type()
)
bsnNoiseAfterChannelUpdate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnNoiseAfterChannelUpdate.setStatus("current")
_BsnInterferenceBeforeChannelUpdate_Type = Integer32
_BsnInterferenceBeforeChannelUpdate_Object = MibScalar
bsnInterferenceBeforeChannelUpdate = _BsnInterferenceBeforeChannelUpdate_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 87),
    _BsnInterferenceBeforeChannelUpdate_Type()
)
bsnInterferenceBeforeChannelUpdate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnInterferenceBeforeChannelUpdate.setStatus("current")
_BsnInterferenceAfterChannelUpdate_Type = Integer32
_BsnInterferenceAfterChannelUpdate_Object = MibScalar
bsnInterferenceAfterChannelUpdate = _BsnInterferenceAfterChannelUpdate_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 2, 88),
    _BsnInterferenceAfterChannelUpdate_Type()
)
bsnInterferenceAfterChannelUpdate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsnInterferenceAfterChannelUpdate.setStatus("current")
_BsnTraps_ObjectIdentity = ObjectIdentity
bsnTraps = _BsnTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3)
)
_BsnUtility_ObjectIdentity = ObjectIdentity
bsnUtility = _BsnUtility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7)
)
_BsnSyslog_ObjectIdentity = ObjectIdentity
bsnSyslog = _BsnSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7, 1)
)


class _BsnSyslogEnable_Type(Integer32):
    """Custom type bsnSyslogEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_BsnSyslogEnable_Type.__name__ = "Integer32"
_BsnSyslogEnable_Object = MibScalar
bsnSyslogEnable = _BsnSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7, 1, 1),
    _BsnSyslogEnable_Type()
)
bsnSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnSyslogEnable.setStatus("current")
_BsnSyslogRemoteAddress_Type = DisplayString
_BsnSyslogRemoteAddress_Object = MibScalar
bsnSyslogRemoteAddress = _BsnSyslogRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7, 1, 2),
    _BsnSyslogRemoteAddress_Type()
)
bsnSyslogRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnSyslogRemoteAddress.setStatus("current")
_BsnPing_ObjectIdentity = ObjectIdentity
bsnPing = _BsnPing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7, 2)
)
_BsnPingTestTable_Object = MibTable
bsnPingTestTable = _BsnPingTestTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7, 2, 1)
)
if mibBuilder.loadTexts:
    bsnPingTestTable.setStatus("current")
_BsnPingTestEntry_Object = MibTableRow
bsnPingTestEntry = _BsnPingTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7, 2, 1, 1)
)
bsnPingTestEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnPingTestId"),
)
if mibBuilder.loadTexts:
    bsnPingTestEntry.setStatus("current")


class _BsnPingTestId_Type(Integer32):
    """Custom type bsnPingTestId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_BsnPingTestId_Type.__name__ = "Integer32"
_BsnPingTestId_Object = MibTableColumn
bsnPingTestId = _BsnPingTestId_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7, 2, 1, 1, 1),
    _BsnPingTestId_Type()
)
bsnPingTestId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnPingTestId.setStatus("current")
_BsnPingTestIPAddress_Type = IpAddress
_BsnPingTestIPAddress_Object = MibTableColumn
bsnPingTestIPAddress = _BsnPingTestIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7, 2, 1, 1, 2),
    _BsnPingTestIPAddress_Type()
)
bsnPingTestIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnPingTestIPAddress.setStatus("current")


class _BsnPingTestSendCount_Type(Integer32):
    """Custom type bsnPingTestSendCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_BsnPingTestSendCount_Type.__name__ = "Integer32"
_BsnPingTestSendCount_Object = MibTableColumn
bsnPingTestSendCount = _BsnPingTestSendCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7, 2, 1, 1, 3),
    _BsnPingTestSendCount_Type()
)
bsnPingTestSendCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnPingTestSendCount.setStatus("current")


class _BsnPingTestReceivedCount_Type(Integer32):
    """Custom type bsnPingTestReceivedCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_BsnPingTestReceivedCount_Type.__name__ = "Integer32"
_BsnPingTestReceivedCount_Object = MibTableColumn
bsnPingTestReceivedCount = _BsnPingTestReceivedCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7, 2, 1, 1, 4),
    _BsnPingTestReceivedCount_Type()
)
bsnPingTestReceivedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnPingTestReceivedCount.setStatus("current")


class _BsnPingTestStatus_Type(Integer32):
    """Custom type bsnPingTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("complete", 2),
          ("inprogress", 1))
    )


_BsnPingTestStatus_Type.__name__ = "Integer32"
_BsnPingTestStatus_Object = MibTableColumn
bsnPingTestStatus = _BsnPingTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7, 2, 1, 1, 5),
    _BsnPingTestStatus_Type()
)
bsnPingTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnPingTestStatus.setStatus("current")
_BsnPingTestMaxTimeInterval_Type = Unsigned32
_BsnPingTestMaxTimeInterval_Object = MibTableColumn
bsnPingTestMaxTimeInterval = _BsnPingTestMaxTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7, 2, 1, 1, 6),
    _BsnPingTestMaxTimeInterval_Type()
)
bsnPingTestMaxTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnPingTestMaxTimeInterval.setStatus("current")
if mibBuilder.loadTexts:
    bsnPingTestMaxTimeInterval.setUnits("mSec")
_BsnPingTestMinTimeInterval_Type = Unsigned32
_BsnPingTestMinTimeInterval_Object = MibTableColumn
bsnPingTestMinTimeInterval = _BsnPingTestMinTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7, 2, 1, 1, 7),
    _BsnPingTestMinTimeInterval_Type()
)
bsnPingTestMinTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnPingTestMinTimeInterval.setStatus("current")
if mibBuilder.loadTexts:
    bsnPingTestMinTimeInterval.setUnits("mSec")
_BsnPingTestAvgTimeInterval_Type = Unsigned32
_BsnPingTestAvgTimeInterval_Object = MibTableColumn
bsnPingTestAvgTimeInterval = _BsnPingTestAvgTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7, 2, 1, 1, 8),
    _BsnPingTestAvgTimeInterval_Type()
)
bsnPingTestAvgTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnPingTestAvgTimeInterval.setStatus("current")
if mibBuilder.loadTexts:
    bsnPingTestAvgTimeInterval.setUnits("mSec")
_BsnPingTestRowStatus_Type = RowStatus
_BsnPingTestRowStatus_Object = MibTableColumn
bsnPingTestRowStatus = _BsnPingTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7, 2, 1, 1, 25),
    _BsnPingTestRowStatus_Type()
)
bsnPingTestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnPingTestRowStatus.setStatus("current")
_BsnLinkTest_ObjectIdentity = ObjectIdentity
bsnLinkTest = _BsnLinkTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7, 3)
)
_BsnLinkTestTable_Object = MibTable
bsnLinkTestTable = _BsnLinkTestTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7, 3, 1)
)
if mibBuilder.loadTexts:
    bsnLinkTestTable.setStatus("deprecated")
_BsnLinkTestEntry_Object = MibTableRow
bsnLinkTestEntry = _BsnLinkTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7, 3, 1, 1)
)
bsnLinkTestEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnLinkTestId"),
)
if mibBuilder.loadTexts:
    bsnLinkTestEntry.setStatus("deprecated")


class _BsnLinkTestId_Type(Integer32):
    """Custom type bsnLinkTestId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_BsnLinkTestId_Type.__name__ = "Integer32"
_BsnLinkTestId_Object = MibTableColumn
bsnLinkTestId = _BsnLinkTestId_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7, 3, 1, 1, 1),
    _BsnLinkTestId_Type()
)
bsnLinkTestId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnLinkTestId.setStatus("deprecated")
_BsnLinkTestMacAddress_Type = MacAddress
_BsnLinkTestMacAddress_Object = MibTableColumn
bsnLinkTestMacAddress = _BsnLinkTestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7, 3, 1, 1, 2),
    _BsnLinkTestMacAddress_Type()
)
bsnLinkTestMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnLinkTestMacAddress.setStatus("deprecated")


class _BsnLinkTestSendPktCount_Type(Integer32):
    """Custom type bsnLinkTestSendPktCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_BsnLinkTestSendPktCount_Type.__name__ = "Integer32"
_BsnLinkTestSendPktCount_Object = MibTableColumn
bsnLinkTestSendPktCount = _BsnLinkTestSendPktCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7, 3, 1, 1, 3),
    _BsnLinkTestSendPktCount_Type()
)
bsnLinkTestSendPktCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnLinkTestSendPktCount.setStatus("deprecated")


class _BsnLinkTestSendPktLength_Type(Integer32):
    """Custom type bsnLinkTestSendPktLength based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_BsnLinkTestSendPktLength_Type.__name__ = "Integer32"
_BsnLinkTestSendPktLength_Object = MibTableColumn
bsnLinkTestSendPktLength = _BsnLinkTestSendPktLength_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7, 3, 1, 1, 4),
    _BsnLinkTestSendPktLength_Type()
)
bsnLinkTestSendPktLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnLinkTestSendPktLength.setStatus("deprecated")
_BsnLinkTestReceivedPktCount_Type = Integer32
_BsnLinkTestReceivedPktCount_Object = MibTableColumn
bsnLinkTestReceivedPktCount = _BsnLinkTestReceivedPktCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7, 3, 1, 1, 5),
    _BsnLinkTestReceivedPktCount_Type()
)
bsnLinkTestReceivedPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnLinkTestReceivedPktCount.setStatus("deprecated")
_BsnLinkTestClientRSSI_Type = Integer32
_BsnLinkTestClientRSSI_Object = MibTableColumn
bsnLinkTestClientRSSI = _BsnLinkTestClientRSSI_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7, 3, 1, 1, 6),
    _BsnLinkTestClientRSSI_Type()
)
bsnLinkTestClientRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnLinkTestClientRSSI.setStatus("deprecated")
_BsnLinkTestLocalSNR_Type = Integer32
_BsnLinkTestLocalSNR_Object = MibTableColumn
bsnLinkTestLocalSNR = _BsnLinkTestLocalSNR_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7, 3, 1, 1, 7),
    _BsnLinkTestLocalSNR_Type()
)
bsnLinkTestLocalSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnLinkTestLocalSNR.setStatus("deprecated")
_BsnLinkTestLocalRSSI_Type = Integer32
_BsnLinkTestLocalRSSI_Object = MibTableColumn
bsnLinkTestLocalRSSI = _BsnLinkTestLocalRSSI_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7, 3, 1, 1, 8),
    _BsnLinkTestLocalRSSI_Type()
)
bsnLinkTestLocalRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnLinkTestLocalRSSI.setStatus("deprecated")


class _BsnLinkTestStatus_Type(Integer32):
    """Custom type bsnLinkTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("complete", 2),
          ("inprogress", 1))
    )


_BsnLinkTestStatus_Type.__name__ = "Integer32"
_BsnLinkTestStatus_Object = MibTableColumn
bsnLinkTestStatus = _BsnLinkTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7, 3, 1, 1, 9),
    _BsnLinkTestStatus_Type()
)
bsnLinkTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnLinkTestStatus.setStatus("deprecated")
_BsnLinkTestRowStatus_Type = RowStatus
_BsnLinkTestRowStatus_Object = MibTableColumn
bsnLinkTestRowStatus = _BsnLinkTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 7, 3, 1, 1, 30),
    _BsnLinkTestRowStatus_Type()
)
bsnLinkTestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnLinkTestRowStatus.setStatus("deprecated")
_BsnMobility_ObjectIdentity = ObjectIdentity
bsnMobility = _BsnMobility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8)
)
_BsnMobilityConfig_ObjectIdentity = ObjectIdentity
bsnMobilityConfig = _BsnMobilityConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 1)
)


class _BsnMobilityProtocolPortNum_Type(Integer32):
    """Custom type bsnMobilityProtocolPortNum based on Integer32"""
    defaultValue = 0


_BsnMobilityProtocolPortNum_Object = MibScalar
bsnMobilityProtocolPortNum = _BsnMobilityProtocolPortNum_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 1, 1),
    _BsnMobilityProtocolPortNum_Type()
)
bsnMobilityProtocolPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnMobilityProtocolPortNum.setStatus("current")


class _BsnMobilityDynamicDiscovery_Type(Integer32):
    """Custom type bsnMobilityDynamicDiscovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnMobilityDynamicDiscovery_Type.__name__ = "Integer32"
_BsnMobilityDynamicDiscovery_Object = MibScalar
bsnMobilityDynamicDiscovery = _BsnMobilityDynamicDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 1, 3),
    _BsnMobilityDynamicDiscovery_Type()
)
bsnMobilityDynamicDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnMobilityDynamicDiscovery.setStatus("current")


class _BsnMobilityStatsReset_Type(Integer32):
    """Custom type bsnMobilityStatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("resetNow", 1))
    )


_BsnMobilityStatsReset_Type.__name__ = "Integer32"
_BsnMobilityStatsReset_Object = MibScalar
bsnMobilityStatsReset = _BsnMobilityStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 1, 4),
    _BsnMobilityStatsReset_Type()
)
bsnMobilityStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnMobilityStatsReset.setStatus("current")
_BsnMobilityGroupMembersTable_Object = MibTable
bsnMobilityGroupMembersTable = _BsnMobilityGroupMembersTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 1, 10)
)
if mibBuilder.loadTexts:
    bsnMobilityGroupMembersTable.setStatus("current")
_BsnMobilityGroupMembersEntry_Object = MibTableRow
bsnMobilityGroupMembersEntry = _BsnMobilityGroupMembersEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 1, 10, 1)
)
bsnMobilityGroupMembersEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnMobilityGroupMemberMacAddress"),
)
if mibBuilder.loadTexts:
    bsnMobilityGroupMembersEntry.setStatus("current")
_BsnMobilityGroupMemberMacAddress_Type = MacAddress
_BsnMobilityGroupMemberMacAddress_Object = MibTableColumn
bsnMobilityGroupMemberMacAddress = _BsnMobilityGroupMemberMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 1, 10, 1, 1),
    _BsnMobilityGroupMemberMacAddress_Type()
)
bsnMobilityGroupMemberMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnMobilityGroupMemberMacAddress.setStatus("current")
_BsnMobilityGroupMemberIPAddress_Type = IpAddress
_BsnMobilityGroupMemberIPAddress_Object = MibTableColumn
bsnMobilityGroupMemberIPAddress = _BsnMobilityGroupMemberIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 1, 10, 1, 2),
    _BsnMobilityGroupMemberIPAddress_Type()
)
bsnMobilityGroupMemberIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnMobilityGroupMemberIPAddress.setStatus("current")


class _BsnMobilityGroupMemberGroupName_Type(DisplayString):
    """Custom type bsnMobilityGroupMemberGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_BsnMobilityGroupMemberGroupName_Type.__name__ = "DisplayString"
_BsnMobilityGroupMemberGroupName_Object = MibTableColumn
bsnMobilityGroupMemberGroupName = _BsnMobilityGroupMemberGroupName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 1, 10, 1, 3),
    _BsnMobilityGroupMemberGroupName_Type()
)
bsnMobilityGroupMemberGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnMobilityGroupMemberGroupName.setStatus("current")
_BsnMobilityGroupMemberRowStatus_Type = RowStatus
_BsnMobilityGroupMemberRowStatus_Object = MibTableColumn
bsnMobilityGroupMemberRowStatus = _BsnMobilityGroupMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 1, 10, 1, 22),
    _BsnMobilityGroupMemberRowStatus_Type()
)
bsnMobilityGroupMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnMobilityGroupMemberRowStatus.setStatus("current")
_BsnMobilityAnchorsTable_Object = MibTable
bsnMobilityAnchorsTable = _BsnMobilityAnchorsTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 1, 11)
)
if mibBuilder.loadTexts:
    bsnMobilityAnchorsTable.setStatus("deprecated")
_BsnMobilityAnchorsEntry_Object = MibTableRow
bsnMobilityAnchorsEntry = _BsnMobilityAnchorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 1, 11, 1)
)
bsnMobilityAnchorsEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnMobilityAnchorWlanSsid"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnMobilityAnchorSwitchIPAddress"),
)
if mibBuilder.loadTexts:
    bsnMobilityAnchorsEntry.setStatus("deprecated")


class _BsnMobilityAnchorWlanSsid_Type(DisplayString):
    """Custom type bsnMobilityAnchorWlanSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BsnMobilityAnchorWlanSsid_Type.__name__ = "DisplayString"
_BsnMobilityAnchorWlanSsid_Object = MibTableColumn
bsnMobilityAnchorWlanSsid = _BsnMobilityAnchorWlanSsid_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 1, 11, 1, 1),
    _BsnMobilityAnchorWlanSsid_Type()
)
bsnMobilityAnchorWlanSsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnMobilityAnchorWlanSsid.setStatus("deprecated")
_BsnMobilityAnchorSwitchIPAddress_Type = IpAddress
_BsnMobilityAnchorSwitchIPAddress_Object = MibTableColumn
bsnMobilityAnchorSwitchIPAddress = _BsnMobilityAnchorSwitchIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 1, 11, 1, 2),
    _BsnMobilityAnchorSwitchIPAddress_Type()
)
bsnMobilityAnchorSwitchIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnMobilityAnchorSwitchIPAddress.setStatus("deprecated")
_BsnMobilityAnchorRowStatus_Type = RowStatus
_BsnMobilityAnchorRowStatus_Object = MibTableColumn
bsnMobilityAnchorRowStatus = _BsnMobilityAnchorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 1, 11, 1, 20),
    _BsnMobilityAnchorRowStatus_Type()
)
bsnMobilityAnchorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnMobilityAnchorRowStatus.setStatus("deprecated")
_BsnMobilityStats_ObjectIdentity = ObjectIdentity
bsnMobilityStats = _BsnMobilityStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2)
)
_BsnTotalHandoffRequests_Type = Counter32
_BsnTotalHandoffRequests_Object = MibScalar
bsnTotalHandoffRequests = _BsnTotalHandoffRequests_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 1),
    _BsnTotalHandoffRequests_Type()
)
bsnTotalHandoffRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalHandoffRequests.setStatus("current")
_BsnTotalHandoffs_Type = Counter32
_BsnTotalHandoffs_Object = MibScalar
bsnTotalHandoffs = _BsnTotalHandoffs_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 2),
    _BsnTotalHandoffs_Type()
)
bsnTotalHandoffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalHandoffs.setStatus("current")
_BsnCurrentExportedClients_Type = Counter32
_BsnCurrentExportedClients_Object = MibScalar
bsnCurrentExportedClients = _BsnCurrentExportedClients_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 3),
    _BsnCurrentExportedClients_Type()
)
bsnCurrentExportedClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnCurrentExportedClients.setStatus("current")
_BsnTotalExportedClients_Type = Counter32
_BsnTotalExportedClients_Object = MibScalar
bsnTotalExportedClients = _BsnTotalExportedClients_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 4),
    _BsnTotalExportedClients_Type()
)
bsnTotalExportedClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalExportedClients.setStatus("current")
_BsnCurrentImportedClients_Type = Counter32
_BsnCurrentImportedClients_Object = MibScalar
bsnCurrentImportedClients = _BsnCurrentImportedClients_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 5),
    _BsnCurrentImportedClients_Type()
)
bsnCurrentImportedClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnCurrentImportedClients.setStatus("current")
_BsnTotalImportedClients_Type = Counter32
_BsnTotalImportedClients_Object = MibScalar
bsnTotalImportedClients = _BsnTotalImportedClients_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 6),
    _BsnTotalImportedClients_Type()
)
bsnTotalImportedClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalImportedClients.setStatus("current")
_BsnTotalHandoffErrors_Type = Counter32
_BsnTotalHandoffErrors_Object = MibScalar
bsnTotalHandoffErrors = _BsnTotalHandoffErrors_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 7),
    _BsnTotalHandoffErrors_Type()
)
bsnTotalHandoffErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalHandoffErrors.setStatus("current")
_BsnTotalCommunicationErrors_Type = Counter32
_BsnTotalCommunicationErrors_Object = MibScalar
bsnTotalCommunicationErrors = _BsnTotalCommunicationErrors_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 8),
    _BsnTotalCommunicationErrors_Type()
)
bsnTotalCommunicationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalCommunicationErrors.setStatus("current")
_BsnMobilityGroupDirectoryTable_Object = MibTable
bsnMobilityGroupDirectoryTable = _BsnMobilityGroupDirectoryTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 9)
)
if mibBuilder.loadTexts:
    bsnMobilityGroupDirectoryTable.setStatus("current")
_BsnMobilityGroupDirectoryEntry_Object = MibTableRow
bsnMobilityGroupDirectoryEntry = _BsnMobilityGroupDirectoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 9, 1)
)
bsnMobilityGroupDirectoryEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnGroupDirectoryMemberMacAddress"),
)
if mibBuilder.loadTexts:
    bsnMobilityGroupDirectoryEntry.setStatus("current")
_BsnGroupDirectoryMemberIPAddress_Type = IpAddress
_BsnGroupDirectoryMemberIPAddress_Object = MibTableColumn
bsnGroupDirectoryMemberIPAddress = _BsnGroupDirectoryMemberIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 9, 1, 1),
    _BsnGroupDirectoryMemberIPAddress_Type()
)
bsnGroupDirectoryMemberIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGroupDirectoryMemberIPAddress.setStatus("current")
_BsnGroupDirectoryMemberMacAddress_Type = MacAddress
_BsnGroupDirectoryMemberMacAddress_Object = MibTableColumn
bsnGroupDirectoryMemberMacAddress = _BsnGroupDirectoryMemberMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 9, 1, 2),
    _BsnGroupDirectoryMemberMacAddress_Type()
)
bsnGroupDirectoryMemberMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGroupDirectoryMemberMacAddress.setStatus("current")


class _BsnGroupDirectoryDicoveryType_Type(Integer32):
    """Custom type bsnGroupDirectoryDicoveryType based on Integer32"""
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
        *(("broadcast", 3),
          ("learned", 4),
          ("rrm", 2),
          ("static", 1))
    )


_BsnGroupDirectoryDicoveryType_Type.__name__ = "Integer32"
_BsnGroupDirectoryDicoveryType_Object = MibTableColumn
bsnGroupDirectoryDicoveryType = _BsnGroupDirectoryDicoveryType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 9, 1, 3),
    _BsnGroupDirectoryDicoveryType_Type()
)
bsnGroupDirectoryDicoveryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnGroupDirectoryDicoveryType.setStatus("current")
_BsnMemberCurrentAnchoredClients_Type = Counter32
_BsnMemberCurrentAnchoredClients_Object = MibTableColumn
bsnMemberCurrentAnchoredClients = _BsnMemberCurrentAnchoredClients_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 9, 1, 4),
    _BsnMemberCurrentAnchoredClients_Type()
)
bsnMemberCurrentAnchoredClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMemberCurrentAnchoredClients.setStatus("current")
_BsnMemberTotalAnchoredClients_Type = Counter32
_BsnMemberTotalAnchoredClients_Object = MibTableColumn
bsnMemberTotalAnchoredClients = _BsnMemberTotalAnchoredClients_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 9, 1, 5),
    _BsnMemberTotalAnchoredClients_Type()
)
bsnMemberTotalAnchoredClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMemberTotalAnchoredClients.setStatus("current")
_BsnMemberCurrentExportedClients_Type = Counter32
_BsnMemberCurrentExportedClients_Object = MibTableColumn
bsnMemberCurrentExportedClients = _BsnMemberCurrentExportedClients_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 9, 1, 6),
    _BsnMemberCurrentExportedClients_Type()
)
bsnMemberCurrentExportedClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMemberCurrentExportedClients.setStatus("current")
_BsnMemberTotalExportedClients_Type = Counter32
_BsnMemberTotalExportedClients_Object = MibTableColumn
bsnMemberTotalExportedClients = _BsnMemberTotalExportedClients_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 9, 1, 7),
    _BsnMemberTotalExportedClients_Type()
)
bsnMemberTotalExportedClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMemberTotalExportedClients.setStatus("current")
_BsnMemberCurrentImportedClients_Type = Counter32
_BsnMemberCurrentImportedClients_Object = MibTableColumn
bsnMemberCurrentImportedClients = _BsnMemberCurrentImportedClients_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 9, 1, 8),
    _BsnMemberCurrentImportedClients_Type()
)
bsnMemberCurrentImportedClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMemberCurrentImportedClients.setStatus("current")
_BsnMemberTotalImportedClients_Type = Counter32
_BsnMemberTotalImportedClients_Object = MibTableColumn
bsnMemberTotalImportedClients = _BsnMemberTotalImportedClients_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 9, 1, 9),
    _BsnMemberTotalImportedClients_Type()
)
bsnMemberTotalImportedClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMemberTotalImportedClients.setStatus("current")
_BsnMemberTotalHandoffErrors_Type = Counter32
_BsnMemberTotalHandoffErrors_Object = MibTableColumn
bsnMemberTotalHandoffErrors = _BsnMemberTotalHandoffErrors_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 9, 1, 10),
    _BsnMemberTotalHandoffErrors_Type()
)
bsnMemberTotalHandoffErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMemberTotalHandoffErrors.setStatus("current")
_BsnMemberTotalCommunicationErrors_Type = Counter32
_BsnMemberTotalCommunicationErrors_Object = MibTableColumn
bsnMemberTotalCommunicationErrors = _BsnMemberTotalCommunicationErrors_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 9, 1, 30),
    _BsnMemberTotalCommunicationErrors_Type()
)
bsnMemberTotalCommunicationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnMemberTotalCommunicationErrors.setStatus("current")
_BsnTotalReceiveErrors_Type = Counter32
_BsnTotalReceiveErrors_Object = MibScalar
bsnTotalReceiveErrors = _BsnTotalReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 10),
    _BsnTotalReceiveErrors_Type()
)
bsnTotalReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalReceiveErrors.setStatus("current")
_BsnTotalTransmitErrors_Type = Counter32
_BsnTotalTransmitErrors_Object = MibScalar
bsnTotalTransmitErrors = _BsnTotalTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 11),
    _BsnTotalTransmitErrors_Type()
)
bsnTotalTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalTransmitErrors.setStatus("current")
_BsnTotalResponsesRetransmitted_Type = Counter32
_BsnTotalResponsesRetransmitted_Object = MibScalar
bsnTotalResponsesRetransmitted = _BsnTotalResponsesRetransmitted_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 12),
    _BsnTotalResponsesRetransmitted_Type()
)
bsnTotalResponsesRetransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalResponsesRetransmitted.setStatus("current")
_BsnTotalHandoffEndRequestsReceived_Type = Counter32
_BsnTotalHandoffEndRequestsReceived_Object = MibScalar
bsnTotalHandoffEndRequestsReceived = _BsnTotalHandoffEndRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 13),
    _BsnTotalHandoffEndRequestsReceived_Type()
)
bsnTotalHandoffEndRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalHandoffEndRequestsReceived.setStatus("current")
_BsnTotalStateTransitionsDisallowed_Type = Counter32
_BsnTotalStateTransitionsDisallowed_Object = MibScalar
bsnTotalStateTransitionsDisallowed = _BsnTotalStateTransitionsDisallowed_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 14),
    _BsnTotalStateTransitionsDisallowed_Type()
)
bsnTotalStateTransitionsDisallowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalStateTransitionsDisallowed.setStatus("current")
_BsnTotalResourceErrors_Type = Counter32
_BsnTotalResourceErrors_Object = MibScalar
bsnTotalResourceErrors = _BsnTotalResourceErrors_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 15),
    _BsnTotalResourceErrors_Type()
)
bsnTotalResourceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalResourceErrors.setStatus("current")
_BsnTotalHandoffRequestsSent_Type = Counter32
_BsnTotalHandoffRequestsSent_Object = MibScalar
bsnTotalHandoffRequestsSent = _BsnTotalHandoffRequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 16),
    _BsnTotalHandoffRequestsSent_Type()
)
bsnTotalHandoffRequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalHandoffRequestsSent.setStatus("current")
_BsnTotalHandoffRepliesReceived_Type = Counter32
_BsnTotalHandoffRepliesReceived_Object = MibScalar
bsnTotalHandoffRepliesReceived = _BsnTotalHandoffRepliesReceived_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 17),
    _BsnTotalHandoffRepliesReceived_Type()
)
bsnTotalHandoffRepliesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalHandoffRepliesReceived.setStatus("current")
_BsnTotalHandoffAsLocalReceived_Type = Counter32
_BsnTotalHandoffAsLocalReceived_Object = MibScalar
bsnTotalHandoffAsLocalReceived = _BsnTotalHandoffAsLocalReceived_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 18),
    _BsnTotalHandoffAsLocalReceived_Type()
)
bsnTotalHandoffAsLocalReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalHandoffAsLocalReceived.setStatus("current")
_BsnTotalHandoffAsForeignReceived_Type = Counter32
_BsnTotalHandoffAsForeignReceived_Object = MibScalar
bsnTotalHandoffAsForeignReceived = _BsnTotalHandoffAsForeignReceived_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 19),
    _BsnTotalHandoffAsForeignReceived_Type()
)
bsnTotalHandoffAsForeignReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalHandoffAsForeignReceived.setStatus("current")
_BsnTotalHandoffDeniesReceived_Type = Counter32
_BsnTotalHandoffDeniesReceived_Object = MibScalar
bsnTotalHandoffDeniesReceived = _BsnTotalHandoffDeniesReceived_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 20),
    _BsnTotalHandoffDeniesReceived_Type()
)
bsnTotalHandoffDeniesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalHandoffDeniesReceived.setStatus("current")
_BsnTotalAnchorRequestsSent_Type = Counter32
_BsnTotalAnchorRequestsSent_Object = MibScalar
bsnTotalAnchorRequestsSent = _BsnTotalAnchorRequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 21),
    _BsnTotalAnchorRequestsSent_Type()
)
bsnTotalAnchorRequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalAnchorRequestsSent.setStatus("current")
_BsnTotalAnchorDenyReceived_Type = Counter32
_BsnTotalAnchorDenyReceived_Object = MibScalar
bsnTotalAnchorDenyReceived = _BsnTotalAnchorDenyReceived_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 22),
    _BsnTotalAnchorDenyReceived_Type()
)
bsnTotalAnchorDenyReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalAnchorDenyReceived.setStatus("current")
_BsnTotalAnchorGrantReceived_Type = Counter32
_BsnTotalAnchorGrantReceived_Object = MibScalar
bsnTotalAnchorGrantReceived = _BsnTotalAnchorGrantReceived_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 23),
    _BsnTotalAnchorGrantReceived_Type()
)
bsnTotalAnchorGrantReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalAnchorGrantReceived.setStatus("current")
_BsnTotalAnchorTransferReceived_Type = Counter32
_BsnTotalAnchorTransferReceived_Object = MibScalar
bsnTotalAnchorTransferReceived = _BsnTotalAnchorTransferReceived_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 24),
    _BsnTotalAnchorTransferReceived_Type()
)
bsnTotalAnchorTransferReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalAnchorTransferReceived.setStatus("current")
_BsnTotalHandoffRequestsIgnored_Type = Counter32
_BsnTotalHandoffRequestsIgnored_Object = MibScalar
bsnTotalHandoffRequestsIgnored = _BsnTotalHandoffRequestsIgnored_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 25),
    _BsnTotalHandoffRequestsIgnored_Type()
)
bsnTotalHandoffRequestsIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalHandoffRequestsIgnored.setStatus("current")
_BsnTotalPingPongHandoffRequestsDropped_Type = Counter32
_BsnTotalPingPongHandoffRequestsDropped_Object = MibScalar
bsnTotalPingPongHandoffRequestsDropped = _BsnTotalPingPongHandoffRequestsDropped_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 26),
    _BsnTotalPingPongHandoffRequestsDropped_Type()
)
bsnTotalPingPongHandoffRequestsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalPingPongHandoffRequestsDropped.setStatus("current")
_BsnTotalHandoffRequestsDropped_Type = Counter32
_BsnTotalHandoffRequestsDropped_Object = MibScalar
bsnTotalHandoffRequestsDropped = _BsnTotalHandoffRequestsDropped_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 27),
    _BsnTotalHandoffRequestsDropped_Type()
)
bsnTotalHandoffRequestsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalHandoffRequestsDropped.setStatus("current")
_BsnTotalHandoffRequestsDenied_Type = Counter32
_BsnTotalHandoffRequestsDenied_Object = MibScalar
bsnTotalHandoffRequestsDenied = _BsnTotalHandoffRequestsDenied_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 28),
    _BsnTotalHandoffRequestsDenied_Type()
)
bsnTotalHandoffRequestsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalHandoffRequestsDenied.setStatus("current")
_BsnTotalClientHandoffAsLocal_Type = Counter32
_BsnTotalClientHandoffAsLocal_Object = MibScalar
bsnTotalClientHandoffAsLocal = _BsnTotalClientHandoffAsLocal_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 29),
    _BsnTotalClientHandoffAsLocal_Type()
)
bsnTotalClientHandoffAsLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalClientHandoffAsLocal.setStatus("current")
_BsnTotalClientHandoffAsForeign_Type = Counter32
_BsnTotalClientHandoffAsForeign_Object = MibScalar
bsnTotalClientHandoffAsForeign = _BsnTotalClientHandoffAsForeign_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 30),
    _BsnTotalClientHandoffAsForeign_Type()
)
bsnTotalClientHandoffAsForeign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalClientHandoffAsForeign.setStatus("current")
_BsnTotalAnchorRequestsReceived_Type = Counter32
_BsnTotalAnchorRequestsReceived_Object = MibScalar
bsnTotalAnchorRequestsReceived = _BsnTotalAnchorRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 31),
    _BsnTotalAnchorRequestsReceived_Type()
)
bsnTotalAnchorRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalAnchorRequestsReceived.setStatus("current")
_BsnTotalAnchorRequestsDenied_Type = Counter32
_BsnTotalAnchorRequestsDenied_Object = MibScalar
bsnTotalAnchorRequestsDenied = _BsnTotalAnchorRequestsDenied_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 32),
    _BsnTotalAnchorRequestsDenied_Type()
)
bsnTotalAnchorRequestsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalAnchorRequestsDenied.setStatus("current")
_BsnTotalAnchorRequestsGranted_Type = Counter32
_BsnTotalAnchorRequestsGranted_Object = MibScalar
bsnTotalAnchorRequestsGranted = _BsnTotalAnchorRequestsGranted_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 33),
    _BsnTotalAnchorRequestsGranted_Type()
)
bsnTotalAnchorRequestsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalAnchorRequestsGranted.setStatus("current")
_BsnTotalAnchorTransferred_Type = Counter32
_BsnTotalAnchorTransferred_Object = MibScalar
bsnTotalAnchorTransferred = _BsnTotalAnchorTransferred_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 34),
    _BsnTotalAnchorTransferred_Type()
)
bsnTotalAnchorTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalAnchorTransferred.setStatus("current")
_BsnTotalHandoffRequestsReceived_Type = Counter32
_BsnTotalHandoffRequestsReceived_Object = MibScalar
bsnTotalHandoffRequestsReceived = _BsnTotalHandoffRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 8, 2, 35),
    _BsnTotalHandoffRequestsReceived_Type()
)
bsnTotalHandoffRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnTotalHandoffRequestsReceived.setStatus("current")
_BsnIpsec_ObjectIdentity = ObjectIdentity
bsnIpsec = _BsnIpsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 9)
)


class _BsnWrasIpsecCACertificate_Type(OctetString):
    """Custom type bsnWrasIpsecCACertificate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4096),
    )


_BsnWrasIpsecCACertificate_Type.__name__ = "OctetString"
_BsnWrasIpsecCACertificate_Object = MibScalar
bsnWrasIpsecCACertificate = _BsnWrasIpsecCACertificate_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 9, 1),
    _BsnWrasIpsecCACertificate_Type()
)
bsnWrasIpsecCACertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnWrasIpsecCACertificate.setStatus("current")


class _BsnWrasIpsecCACertificateUpdate_Type(OctetString):
    """Custom type bsnWrasIpsecCACertificateUpdate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4096),
    )


_BsnWrasIpsecCACertificateUpdate_Type.__name__ = "OctetString"
_BsnWrasIpsecCACertificateUpdate_Object = MibScalar
bsnWrasIpsecCACertificateUpdate = _BsnWrasIpsecCACertificateUpdate_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 9, 2),
    _BsnWrasIpsecCACertificateUpdate_Type()
)
bsnWrasIpsecCACertificateUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnWrasIpsecCACertificateUpdate.setStatus("current")
_BsnWrasIpsecCertTable_Object = MibTable
bsnWrasIpsecCertTable = _BsnWrasIpsecCertTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 9, 3)
)
if mibBuilder.loadTexts:
    bsnWrasIpsecCertTable.setStatus("current")
_BsnWrasIpsecCertEntry_Object = MibTableRow
bsnWrasIpsecCertEntry = _BsnWrasIpsecCertEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 9, 3, 1)
)
bsnWrasIpsecCertEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnWrasIpsecCertName"),
)
if mibBuilder.loadTexts:
    bsnWrasIpsecCertEntry.setStatus("current")


class _BsnWrasIpsecCertName_Type(DisplayString):
    """Custom type bsnWrasIpsecCertName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_BsnWrasIpsecCertName_Type.__name__ = "DisplayString"
_BsnWrasIpsecCertName_Object = MibTableColumn
bsnWrasIpsecCertName = _BsnWrasIpsecCertName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 9, 3, 1, 1),
    _BsnWrasIpsecCertName_Type()
)
bsnWrasIpsecCertName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnWrasIpsecCertName.setStatus("current")


class _BsnWrasIpsecCertificateUpdate_Type(OctetString):
    """Custom type bsnWrasIpsecCertificateUpdate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4096),
    )


_BsnWrasIpsecCertificateUpdate_Type.__name__ = "OctetString"
_BsnWrasIpsecCertificateUpdate_Object = MibTableColumn
bsnWrasIpsecCertificateUpdate = _BsnWrasIpsecCertificateUpdate_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 9, 3, 1, 2),
    _BsnWrasIpsecCertificateUpdate_Type()
)
bsnWrasIpsecCertificateUpdate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnWrasIpsecCertificateUpdate.setStatus("current")


class _BsnWrasIpsecCertificate_Type(OctetString):
    """Custom type bsnWrasIpsecCertificate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4096),
    )


_BsnWrasIpsecCertificate_Type.__name__ = "OctetString"
_BsnWrasIpsecCertificate_Object = MibTableColumn
bsnWrasIpsecCertificate = _BsnWrasIpsecCertificate_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 9, 3, 1, 3),
    _BsnWrasIpsecCertificate_Type()
)
bsnWrasIpsecCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnWrasIpsecCertificate.setStatus("current")


class _BsnWrasIpsecCertPassword_Type(OctetString):
    """Custom type bsnWrasIpsecCertPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1500),
    )


_BsnWrasIpsecCertPassword_Type.__name__ = "OctetString"
_BsnWrasIpsecCertPassword_Object = MibTableColumn
bsnWrasIpsecCertPassword = _BsnWrasIpsecCertPassword_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 9, 3, 1, 4),
    _BsnWrasIpsecCertPassword_Type()
)
bsnWrasIpsecCertPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnWrasIpsecCertPassword.setStatus("current")
_BsnWrasIpsecCertStatus_Type = RowStatus
_BsnWrasIpsecCertStatus_Object = MibTableColumn
bsnWrasIpsecCertStatus = _BsnWrasIpsecCertStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 9, 3, 1, 24),
    _BsnWrasIpsecCertStatus_Type()
)
bsnWrasIpsecCertStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnWrasIpsecCertStatus.setStatus("current")
_BsnAPGroupsVlanConfig_ObjectIdentity = ObjectIdentity
bsnAPGroupsVlanConfig = _BsnAPGroupsVlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 10)
)


class _BsnAPGroupsVlanFeature_Type(Integer32):
    """Custom type bsnAPGroupsVlanFeature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BsnAPGroupsVlanFeature_Type.__name__ = "Integer32"
_BsnAPGroupsVlanFeature_Object = MibScalar
bsnAPGroupsVlanFeature = _BsnAPGroupsVlanFeature_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 10, 1),
    _BsnAPGroupsVlanFeature_Type()
)
bsnAPGroupsVlanFeature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnAPGroupsVlanFeature.setStatus("current")
_BsnAPGroupsVlanTable_Object = MibTable
bsnAPGroupsVlanTable = _BsnAPGroupsVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 10, 2)
)
if mibBuilder.loadTexts:
    bsnAPGroupsVlanTable.setStatus("current")
_BsnAPGroupsVlanEntry_Object = MibTableRow
bsnAPGroupsVlanEntry = _BsnAPGroupsVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 10, 2, 1)
)
bsnAPGroupsVlanEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPGroupsVlanName"),
)
if mibBuilder.loadTexts:
    bsnAPGroupsVlanEntry.setStatus("current")


class _BsnAPGroupsVlanName_Type(OctetString):
    """Custom type bsnAPGroupsVlanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BsnAPGroupsVlanName_Type.__name__ = "OctetString"
_BsnAPGroupsVlanName_Object = MibTableColumn
bsnAPGroupsVlanName = _BsnAPGroupsVlanName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 10, 2, 1, 1),
    _BsnAPGroupsVlanName_Type()
)
bsnAPGroupsVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAPGroupsVlanName.setStatus("current")


class _BsnAPGroupsVlanDescription_Type(OctetString):
    """Custom type bsnAPGroupsVlanDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BsnAPGroupsVlanDescription_Type.__name__ = "OctetString"
_BsnAPGroupsVlanDescription_Object = MibTableColumn
bsnAPGroupsVlanDescription = _BsnAPGroupsVlanDescription_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 10, 2, 1, 2),
    _BsnAPGroupsVlanDescription_Type()
)
bsnAPGroupsVlanDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAPGroupsVlanDescription.setStatus("current")
_BsnAPGroupsVlanRowStatus_Type = RowStatus
_BsnAPGroupsVlanRowStatus_Object = MibTableColumn
bsnAPGroupsVlanRowStatus = _BsnAPGroupsVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 10, 2, 1, 20),
    _BsnAPGroupsVlanRowStatus_Type()
)
bsnAPGroupsVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAPGroupsVlanRowStatus.setStatus("current")
_BsnAPGroupsVlanMappingTable_Object = MibTable
bsnAPGroupsVlanMappingTable = _BsnAPGroupsVlanMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 10, 3)
)
if mibBuilder.loadTexts:
    bsnAPGroupsVlanMappingTable.setStatus("deprecated")
_BsnAPGroupsVlanMappingEntry_Object = MibTableRow
bsnAPGroupsVlanMappingEntry = _BsnAPGroupsVlanMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 10, 3, 1)
)
bsnAPGroupsVlanMappingEntry.setIndexNames(
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPGroupsVlanName"),
    (0, "AIRESPACE-WIRELESS-MIB", "bsnAPGroupsVlanMappingSsid"),
)
if mibBuilder.loadTexts:
    bsnAPGroupsVlanMappingEntry.setStatus("deprecated")


class _BsnAPGroupsVlanMappingSsid_Type(DisplayString):
    """Custom type bsnAPGroupsVlanMappingSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BsnAPGroupsVlanMappingSsid_Type.__name__ = "DisplayString"
_BsnAPGroupsVlanMappingSsid_Object = MibTableColumn
bsnAPGroupsVlanMappingSsid = _BsnAPGroupsVlanMappingSsid_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 10, 3, 1, 1),
    _BsnAPGroupsVlanMappingSsid_Type()
)
bsnAPGroupsVlanMappingSsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAPGroupsVlanMappingSsid.setStatus("deprecated")


class _BsnAPGroupsVlanMappingInterfaceName_Type(OctetString):
    """Custom type bsnAPGroupsVlanMappingInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BsnAPGroupsVlanMappingInterfaceName_Type.__name__ = "OctetString"
_BsnAPGroupsVlanMappingInterfaceName_Object = MibTableColumn
bsnAPGroupsVlanMappingInterfaceName = _BsnAPGroupsVlanMappingInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 10, 3, 1, 2),
    _BsnAPGroupsVlanMappingInterfaceName_Type()
)
bsnAPGroupsVlanMappingInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAPGroupsVlanMappingInterfaceName.setStatus("deprecated")
_BsnAPGroupsVlanMappingRowStatus_Type = RowStatus
_BsnAPGroupsVlanMappingRowStatus_Object = MibTableColumn
bsnAPGroupsVlanMappingRowStatus = _BsnAPGroupsVlanMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 10, 3, 1, 20),
    _BsnAPGroupsVlanMappingRowStatus_Type()
)
bsnAPGroupsVlanMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnAPGroupsVlanMappingRowStatus.setStatus("deprecated")
_BsnWrasGroups_ObjectIdentity = ObjectIdentity
bsnWrasGroups = _BsnWrasGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 50)
)
_BsnWrasCompliances_ObjectIdentity = ObjectIdentity
bsnWrasCompliances = _BsnWrasCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 51)
)

# Managed Objects groups

bsnEssGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14179, 2, 50, 1)
)
bsnEssGroup.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnDot11EssIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssSsid"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssSessionTimeout"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssMacFiltering"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssAdminStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssSecurityAuthType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssStaticWEPSecurity"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssStaticWEPEncryptionType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssStaticWEPDefaultKey"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssStaticWEPKeyIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssStaticWEPKeyFormat"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11Ess8021xSecurity"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11Ess8021xEncryptionType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssIpsecSecurity"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssVpnEncrTransform"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssVpnAuthTransform"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssVpnIkeAuthMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssVpnSharedKey"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssVpnSharedKeySize"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssVpnIkePhase1Mode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssVpnIkeLifetime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssVpnIkeDHGroup"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssIpsecPassthruSecurity"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssVpnPassthruGateway"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssWebSecurity"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssRadioPolicy"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssQualityOfService"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssDhcpRequired"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssDhcpServerIpAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssVpnContivityMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssVpnQotdServerAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssBlacklistTimeout"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssNumberOfMobileStations"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssWebPassthru"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssCraniteSecurity"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssBlacklistingCapability"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssInterfaceName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssAclName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssAAAOverride"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssWepAllowSharedKeyAuth"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssFortressSecurity"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssL2tpSecurity"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssBroadcastSsid"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssExternalPolicyValidation"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssWmePolicySetting"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11Ess80211ePolicySetting"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssWebPassthroughEmail"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11Ess7920PhoneSupport"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssRadiusAuthPrimaryServer"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssRadiusAuthSecondaryServer"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssRadiusAuthTertiaryServer"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssRadiusAcctPrimaryServer"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssRadiusAcctSecondaryServer"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssRadiusAcctTertiaryServer"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationIpAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationUserName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationAPMacAddr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationEssIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationSsid"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationReasonCode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationMobilityStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationAID"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationAnchorAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationCFPollable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationCFPollRequest"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationChannelAgilityEnabled"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationPBCCOptionImplemented"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationShortPreambleOptionImplemented"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationSessionTimeout"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationAuthenticationAlgorithm"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationWepState"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationPortNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationDeleteAction"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationPolicyManagerState"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationSecurityPolicyStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationProtocol"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationMirrorMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationInterface"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationApMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationVlanId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationPolicyType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationEncryptionCypher"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationEapType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationCcxVersion"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationE2eVersion"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationStatusCode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationPerRadioPerVapIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationMacAddr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationRSSI"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationBytesReceived"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationBytesSent"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationPolicyErrors"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationPacketsReceived"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationPacketsSent"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationSnr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPDot11MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPTotalDetectingAPs"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPFirstReported"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPLastReported"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPContainmentLevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPOnNetwork"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPTotalClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPMaxDetectedRSSI"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPSSID"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPState"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPAirespaceAPMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPAirespaceAPSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPRadioType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPAirespaceAPName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPChannelNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPSsid"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPAirespaceAPRSSI"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPContainmentMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPContainmentChannelCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPContainmentChannels"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPAirespaceAPLastHeard"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPAirespaceAPWepMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPAirespaceAPPreamble"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPAirespaceAPWpaMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPAirespaceAPSNR"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationByIpAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationByIpMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationRssiDataApMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationRssiDataApIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationRssiDataApIfType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationRssiDataApName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationRssiData"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfPhyAntennaIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationRssiDataLastHeard"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationByUserName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationByUserMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientAirespaceAPMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientAirespaceAPSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientRadioType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientAirespaceAPName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientChannelNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientAirespaceAPRSSI"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientAirespaceAPLastHeard"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientAirespaceAPSNR"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientTotalDetectingAPs"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientFirstReported"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientLastReported"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientBSSID"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientContainmentLevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientLastHeard"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientState"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPDot11MacAddr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientDot11MacAddr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11QosProfileName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11QosProfileDesc"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11QosAverageDataRate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11QosBurstDataRate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11QosAvgRealTimeDataRate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11QosBurstRealTimeDataRate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11QosMaxRFUsagePerAP"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11QosProfileQueueDepth"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11WiredQosProtocol"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11802Dot1PTag"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11ResetProfileToDefault"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTagDot11MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTagType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTagTimeInterval"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTagBatteryStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTagLastReported"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTagRssiDataApMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTagRssiDataApIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTagRssiDataApIfType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTagRssiDataApName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTagRssiDataLastHeard"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTagRssiData"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTagRssiDataSnr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTagBytesReceived"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTagPacketsReceived"))
)
if mibBuilder.loadTexts:
    bsnEssGroup.setStatus("deprecated")

bsnApGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14179, 2, 50, 2)
)
bsnApGroup.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPNumOfSlots"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPLocation"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPMonitorOnlyMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPOperationStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPSoftwareVersion"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPBootVersion"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPPrimaryMwarName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPReset"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPStatsTimer"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPPortNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPModel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPSerialNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPClearConfig"),
        ("AIRESPACE-WIRELESS-MIB", "bsnApIpAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPMirrorMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPRemoteModeSupport"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPSecondaryMwarName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPTertiaryMwarName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIsStaticIP"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPNetmask"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPGateway"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPStaticIPAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPBridgingSupport"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPGroupVlanName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIOSVersion"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPCertificateType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPEthernetMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPAdminStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfPhyChannelAssignment"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfPhyChannelNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfPhyTxPowerControl"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfPhyTxPowerLevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfPhyAntennaMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfPhyAntennaType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfPhyAntennaDiversity"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfCellSiteConfigId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfNumberOfVaps"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfOperStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfPortNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfPhyAntennaOptions"),
        ("AIRESPACE-WIRELESS-MIB", "bsnApIfNoOfUsers"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfWlanOverride"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfPacketsSniffingFeature"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSniffChannel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSniffServerIPAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfAntennaGain"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfChannelList"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfAbsolutePowerList"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfRegulatoryDomainSupport"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfAdminStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11BeaconPeriod"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11MediumOccupancyLimit"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11CFPPeriod"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11CFPMaxDuration"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11OperationalRateSet"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11DTIMPeriod"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11MultiDomainCapabilityImplemented"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11MultiDomainCapabilityEnabled"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11CountryString"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11SmtParamsConfigType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11BSSID"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11MaximumTransmitPowerLevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11FirstChannelNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11NumberofChannels"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11MacRTSThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11MacShortRetryLimit"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11MacLongRetryLimit"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11MacFragmentationThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11MacMaxTransmitMSDULifetime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11MacParamsConfigType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11MacMaxReceiveLifetime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11TransmittedFragmentCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11MulticastTransmittedFrameCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11RetryCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11MultipleRetryCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11FrameDuplicateCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11RTSSuccessCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11RTSFailureCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11ACKFailureCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11ReceivedFragmentCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11MulticastReceivedFrameCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11FCSErrorCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11TransmittedFrameCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11WEPUndecryptableCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11FailedCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11EDThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11TIThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfProfileParamAssignment"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfForeignInterferenceThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfForeignNoiseThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfRFUtilizationThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfThroughputThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfMobilesThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfCoverageThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfMobileMinExceptionLevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfCoverageExceptionLevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfLoadRxUtilization"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfLoadTxUtilization"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfLoadChannelUtilization"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfLoadNumOfClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfPoorSNRClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfInterferenceChannelNo"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfInterferencePower"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfInterferenceUtilization"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfNoiseChannelNo"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDBNoisePower"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfLoadProfileState"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfInterferenceProfileState"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfNoiseProfileState"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfCoverageProfileState"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfRxNeighborMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfRxNeighborIpAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfRxNeighborRSSI"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfRxNeighborSlot"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfStationRSSICoverageIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfRSSILevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfStationCountOnRSSI"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfStationSNRCoverageIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSNRLevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfStationCountOnSNR"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfRecommendedChannelNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfRecommendedTxPowerLevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfRecommendedRTSThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfRecommendedFragmentationThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfWlanOverrideId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfWlanOverrideSsid"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfWlanOverrideRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeRole"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeGroup"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeBackhaul"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeBackhaulPAP"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeBackhaulRAP"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeDataRate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeChannel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeRoutingState"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeMalformedNeighPackets"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodePoorNeighSnr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeBlacklistPackets"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeInsufficientMemory"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeRxNeighReq"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeRxNeighRsp"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeTxNeighReq"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeTxNeighRsp"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeParentChanges"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeNeighTimeout"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeParentMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeAPType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeEthernetBridge"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeHops"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighState"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighSnr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighSnrUp"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighSnrDown"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighLinkSnr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighAdjustedEase"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighUnadjustedEase"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighRapEase"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighTxParent"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighRxParent"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighPoorSnr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighLastUpdate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighParentChange"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfRadarDetectedChannelNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfRadarSignalLastHeard"))
)
if mibBuilder.loadTexts:
    bsnApGroup.setStatus("deprecated")

bsnGlobalDot11Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14179, 2, 50, 3)
)
bsnGlobalDot11Group.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11PrivacyOptionImplemented"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11AuthenticationResponseTimeOut"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11MultiDomainCapabilityImplemented"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11MultiDomainCapabilityEnabled"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11CountryIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11LoadBalancing"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11RogueTimer"),
        ("AIRESPACE-WIRELESS-MIB", "bsnPrimaryMwarForAPs"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRtpProtocolPriority"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSystemCurrentTime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnUpdateSystemTime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnOperatingTemperatureEnvironment"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSensorTemperature"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTemperatureAlarmLowLimit"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTemperatureAlarmHighLimit"),
        ("AIRESPACE-WIRELESS-MIB", "bsnVirtualGatewayAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRFMobilityDomainName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnClientWatchListFeature"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueLocationDiscoveryProtocol"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAutoContainFeature"),
        ("AIRESPACE-WIRELESS-MIB", "bsnOverAirProvisionApMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMaximumNumberOfConcurrentLogins"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAutoContainRoguesAdvertisingSsid"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAutoContainAdhocNetworks"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAutoContainTrustedClientsOnRogueAps"),
        ("AIRESPACE-WIRELESS-MIB", "bsnValidateRogueClientsAgainstAAA"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSystemTimezoneDelta"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSystemTimezoneDeltaMinutes"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAllowAuthorizeApAgainstAAA"),
        ("AIRESPACE-WIRELESS-MIB", "bsnApFallbackEnabled"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAppleTalkEnabled"),
        ("AIRESPACE-WIRELESS-MIB", "bsnPolicyForMisconfiguredAps"),
        ("AIRESPACE-WIRELESS-MIB", "bsnEncryptionPolicyEnforced"),
        ("AIRESPACE-WIRELESS-MIB", "bsnPreamblePolicyEnforced"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11ModePolicyEnforced"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadioTypePolicyEnforced"),
        ("AIRESPACE-WIRELESS-MIB", "bsnValidateSsidForTrustedAp"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAlertIfTrustedApMissing"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApEntryExpirationTimeout"),
        ("AIRESPACE-WIRELESS-MIB", "bsnExcessive80211AssocFailures"),
        ("AIRESPACE-WIRELESS-MIB", "bsnExcessive80211AuthFailures"),
        ("AIRESPACE-WIRELESS-MIB", "bsnExcessive8021xAuthFailures"),
        ("AIRESPACE-WIRELESS-MIB", "bsnExternalPolicyServerFailures"),
        ("AIRESPACE-WIRELESS-MIB", "bsnExcessiveWebAuthFailures"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIPTheftORReuse"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignaturePrecedence"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignatureName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignatureDescription"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignatureFrameType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignatureAction"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignatureState"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignatureFrequency"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignatureQuietTime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignatureVersion"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignatureConfigType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignatureEnable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignatureMacInfo"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignatureMacFreq"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignatureRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignaturePatternIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignaturePatternOffset"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignaturePatternString"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignaturePatternMask"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignaturePatternOffSetStart"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignaturePatternRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignaturePrecedence"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignatureName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignatureDescription"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignatureFrameType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignatureAction"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignatureState"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignatureFrequency"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignatureQuietTime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignatureVersion"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignatureConfigType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignatureEnable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignatureMacInfo"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignatureMacFreq"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignatureRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignaturePatternIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignaturePatternOffset"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignaturePatternString"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignaturePatternMask"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignaturePatternOffSetStart"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignaturePatternRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSignatureCheckState"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRfIdTagStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRfIdTagDataTimeout"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRfIdTagAutoTimeoutStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPNeighborAuthStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPNeighborAuthAlarmThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRFNetworkName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnFastSSIDChangeFeature"),
        ("AIRESPACE-WIRELESS-MIB", "bsnBridgingZeroTouchConfig"),
        ("AIRESPACE-WIRELESS-MIB", "bsnBridgingSharedSecretKey"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bNetworkStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bBeaconPeriod"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDynamicChannelAssignment"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bCurrentChannel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDynamicChannelUpdateInterval"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bInputsForDCA"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bChannelUpdateCmdInvoke"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bChannelUpdateCmdStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDynamicTransmitPowerControl"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDynamicTxPowerControlInterval"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bCurrentTxPowerLevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bInputsForDTP"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bPowerUpdateCmdInvoke"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bPowerUpdateCmdStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDataRate1Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDataRate2Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDataRate5AndHalfMhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDataRate11Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bShortPreamble"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDot11gSupport"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDataRate6Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDataRate9Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDataRate12Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDataRate18Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDataRate24Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDataRate36Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDataRate48Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDataRate54Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bPicoCellMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bFastRoamingMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bFastRoamingVoipMinRate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bFastRoamingVoipPercentage"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11b80211eMaxBandwidth"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDTPCSupport"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bRxSopThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bMediumOccupancyLimit"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bCFPPeriod"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bCFPMaxDuration"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bCFPollable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bCFPollRequest"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDTIMPeriod"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bMaximumTransmitPowerLevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bFirstChannelNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bNumberofChannels"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bRTSThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bShortRetryLimit"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bLongRetryLimit"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bFragmentationThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bMaxTransmitMSDULifetime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bMaxReceiveLifetime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bEDThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bChannelAgilityEnabled"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bPBCCOptionImplemented"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bShortPreambleOptionImplemented"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aNetworkStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aLowBandNetwork"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aMediumBandNetwork"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aHighBandNetwork"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aBeaconPeriod"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aDynamicChannelAssignment"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aCurrentChannel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aDynamicChannelUpdateInterval"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aInputsForDCA"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aChannelUpdateCmdInvoke"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aChannelUpdateCmdStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aDynamicTransmitPowerControl"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aCurrentTxPowerLevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aDynamicTxPowerControlInterval"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aInputsForDTP"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aPowerUpdateCmdInvoke"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aPowerUpdateCmdStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aDataRate6Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aDataRate9Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aDataRate12Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aDataRate18Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aDataRate24Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aDataRate36Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aDataRate48Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aDataRate54Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aPicoCellMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aFastRoamingMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aFastRoamingVoipMinRate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aFastRoamingVoipPercentage"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11a80211eMaxBandwidth"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aDTPCSupport"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aRxSopThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aMediumOccupancyLimit"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aCFPPeriod"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aCFPMaxDuration"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aCFPollable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aCFPollRequest"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aDTIMPeriod"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aMaximumTransmitPowerLevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aFirstChannelNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aNumberofChannels"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aRTSThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aShortRetryLimit"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aLongRetryLimit"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aFragmentationThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aMaxTransmitMSDULifetime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aMaxReceiveLifetime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aTIThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aChannelAgilityEnabled"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11hPowerConstraint"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11hChannelSwitchEnable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11hChannelSwitchMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11aGlobalAutomaticGrouping"))
)
if mibBuilder.loadTexts:
    bsnGlobalDot11Group.setStatus("deprecated")

bsnRrmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14179, 2, 50, 4)
)
bsnRrmGroup.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11aForeignInterferenceThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11aForeignNoiseThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11aRFUtilizationThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11aThroughputThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11aMobilesThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11aCoverageThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11aMobileMinExceptionLevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11aCoverageExceptionLevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11aSignalMeasurementInterval"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11aNoiseMeasurementInterval"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11aLoadMeasurementInterval"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11aCoverageMeasurementInterval"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11aChannelMonitorList"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11aSetFactoryDefault"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11bForeignInterferenceThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11bForeignNoiseThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11bRFUtilizationThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11bThroughputThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11bMobilesThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11bCoverageThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11bMobileMinExceptionLevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11bCoverageExceptionLevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11bSignalMeasurementInterval"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11bNoiseMeasurementInterval"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11bLoadMeasurementInterval"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11bCoverageMeasurementInterval"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11bChannelMonitorList"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11bSetFactoryDefault"))
)
if mibBuilder.loadTexts:
    bsnRrmGroup.setStatus("current")

bsnAAAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14179, 2, 50, 5)
)
bsnAAAGroup.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthClientServerPortNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerKey"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerKeyFormat"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerRFC3576"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerIPSec"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerIPSecAuth"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerIPSecEncryption"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerIPSecIKEPhase1"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerIPSecIKELifetime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerIPSecDHGroup"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerNetworkUserConfig"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerMgmtUserConfig"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerRetransmitTimeout"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerKeyWrapKEKkey"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerKeyWrapMACKkey"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerKeyWrapFormat"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccClientServerPortNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerKey"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerKeyFormat"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerIPSec"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerIPSecAuth"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerIPSecEncryption"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerIPSecIKEPhase1"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerIPSecIKELifetime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerIPSecDHGroup"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerNetworkUserConfig"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerRetransmitTimeout"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthClientRoundTripTime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthClientAccessRequests"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthClientAccessRetransmissions"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthClientAccessAccepts"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthClientAccessRejects"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthClientAccessChallenges"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthClientMalformedAccessResponses"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthClientBadAuthenticators"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthClientPendingRequests"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthClientTimeouts"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthClientUnknownTypes"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthClientPacketsDropped"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccClientRoundTripTime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccClientRequests"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccClientRetransmissions"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccClientResponses"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccClientMalformedResponses"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccClientBadAuthenticators"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccClientPendingRequests"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccClientTimeouts"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccClientUnknownTypes"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccClientPacketsDropped"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclApplyMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRuleIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRuleAction"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRuleDirection"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRuleSourceIpAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRuleSourceIpNetmask"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRuleDestinationIpAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRuleDestinationIpNetmask"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRuleProtocol"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRuleStartSourcePort"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRuleEndSourcePort"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRuleStartDestinationPort"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRuleEndDestinationPort"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRuleDscp"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclNewRuleIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRuleRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMacFilterAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMacFilterWlanId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMacFilterInterfaceName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMacFilterDescription"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMacFilterRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLocalNetUserName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLocalNetUserWlanId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLocalNetUserPassword"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLocalNetUserDescription"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLocalNetUserLifetime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLocalNetUserStartTime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLocalNetUserRemainingTime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLocalNetUserRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLocalManagementUserName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLocalManagementUserPassword"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLocalManagementUserAccessMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLocalManagementUserRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnBlackListClientMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnBlackListClientDescription"),
        ("AIRESPACE-WIRELESS-MIB", "bsnBlackListClientRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthKeyWrapEnable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthCacheCredentialsLocally"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAAAMacDelimiter"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAAARadiusCompatibilityMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAAARadiusCallStationIdType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAAALocalDatabaseSize"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAAACurrentLocalDatabaseSize"),
        ("AIRESPACE-WIRELESS-MIB", "bsnExternalPolicyServerAclName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAcceptSelfSignedCertificate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSystemClockTime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPAuthMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPAuthCertificateType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPAuthHashKey"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPAuthRowStatus"))
)
if mibBuilder.loadTexts:
    bsnAAAGroup.setStatus("deprecated")

bsnTrapsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14179, 2, 50, 6)
)
bsnTrapsGroup.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnDot11StationTrapControlMask"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPTrapControlMask"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPProfileTrapControlMask"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPMacAddrTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPNameTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPSlotIdTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPChannelNumberTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPCoverageThresholdTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPCoverageFailedClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPCoverageTotalClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnClientMacAddr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnClientRssi"),
        ("AIRESPACE-WIRELESS-MIB", "bsnClientSnr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnInterferenceEnergyBeforeChannelUpdate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnInterferenceEnergyAfterChannelUpdate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPPortNumberTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPParamUpdateTrapControlMask"),
        ("AIRESPACE-WIRELESS-MIB", "bsnConfigSaveTrapEnable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRADIUSServerTrapEnable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAuthenticationFailureTrapEnable"),
        ("AIRESPACE-WIRELESS-MIB", "bsn80211SecurityTrapControlMask"),
        ("AIRESPACE-WIRELESS-MIB", "bsnWpsTrapControlEnable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAuthFailureUserName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAuthFailureUserType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRemoteIPv4Address"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIpsecErrorCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIpsecSPI"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRemoteUdpPort"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIkeAuthMethod"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIkeTotalInitFailures"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIkeTotalInitNoResponses"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIkeTotalRespFailures"),
        ("AIRESPACE-WIRELESS-MIB", "bsnNotifiesSent"),
        ("AIRESPACE-WIRELESS-MIB", "bsnNotifiesReceived"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSuiteInitFailures"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSuiteRespondFailures"),
        ("AIRESPACE-WIRELESS-MIB", "bsnInitiatorCookie"),
        ("AIRESPACE-WIRELESS-MIB", "bsnResponderCookie"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIsakmpInvalidCookies"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIpsecTrapsMask"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPTrapEnable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCurrentRadiosCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLicenseRadioCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMaxRogueCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationAPMacAddr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnUserIpAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationReasonCode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationBlacklistingReasonCode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationUserName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPOnWiredNetwork"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAdhocMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDuplicateIpReportedByAP"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDuplicateIpTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDuplicateIpTrapClear"),
        ("AIRESPACE-WIRELESS-MIB", "bsnNavDosAttackSourceMacAddr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnWlanIdTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnClearTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApEncryptionUsed"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApEncryptionRequired"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApRadioPolicyUsed"),
        ("AIRESPACE-WIRELESS-MIB", "bsnNetworkType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnNetworkState"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSignatureType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSignatureName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSignatureDescription"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSignatureAttackPreced"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSignatureAttackFrequency"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSignatureAttackChannel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSignatureAttackerMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnApRegulatoryDomain"),
        ("AIRESPACE-WIRELESS-MIB", "bsnImpersonatedAPMacAddr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApPreambleUsed"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApPreambleRequired"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApRadioPolicyRequired"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGroupDirectoryMemberIPAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGroupDirectoryMemberMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGroupDirectoryDicoveryType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMemberCurrentAnchoredClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMemberTotalAnchoredClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMemberCurrentExportedClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMemberTotalExportedClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMemberCurrentImportedClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMemberTotalImportedClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMemberTotalHandoffErrors"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMemberTotalCommunicationErrors"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPGroupsVlanFeature"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPGroupsVlanName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPGroupsVlanDescription"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPGroupsVlanRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPGroupsVlanMappingSsid"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPGroupsVlanMappingInterfaceName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPGroupsVlanMappingRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLicenseKeyTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnApFunctionalityDisableReasonCode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLicenseKeyFeatureSetTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPAuthorizationFailureCause"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfUpDownCause"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPInvalidRadioType"),
        ("AIRESPACE-WIRELESS-MIB", "locationNotifyContent"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSignatureMacInfo"))
)
if mibBuilder.loadTexts:
    bsnTrapsGroup.setStatus("deprecated")

bsnUtilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14179, 2, 50, 7)
)
bsnUtilityGroup.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnSyslogEnable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSyslogRemoteAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnPingTestId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnPingTestIPAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnPingTestSendCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnPingTestReceivedCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnPingTestStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnPingTestRowStatus"))
)
if mibBuilder.loadTexts:
    bsnUtilityGroup.setStatus("deprecated")

bsnMobilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14179, 2, 50, 8)
)
bsnMobilityGroup.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnMobilityProtocolPortNum"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobilityDynamicDiscovery"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobilityStatsReset"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobilityGroupMemberMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobilityGroupMemberIPAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobilityGroupMemberGroupName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobilityGroupMemberRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobilityAnchorWlanSsid"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobilityAnchorSwitchIPAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobilityAnchorRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalHandoffRequests"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalHandoffs"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCurrentExportedClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalExportedClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCurrentImportedClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalImportedClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalHandoffErrors"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalCommunicationErrors"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalReceiveErrors"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalTransmitErrors"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalResponsesRetransmitted"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalHandoffEndRequestsReceived"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalStateTransitionsDisallowed"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalResourceErrors"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalHandoffRequestsSent"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalHandoffRepliesReceived"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalHandoffAsLocalReceived"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalHandoffAsForeignReceived"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalHandoffDeniesReceived"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalAnchorRequestsSent"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalAnchorDenyReceived"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalAnchorGrantReceived"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalAnchorTransferReceived"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalHandoffRequestsIgnored"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalPingPongHandoffRequestsDropped"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalHandoffRequestsDropped"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalHandoffRequestsDenied"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalClientHandoffAsLocal"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalClientHandoffAsForeign"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalAnchorRequestsReceived"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalAnchorRequestsDenied"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalAnchorRequestsGranted"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalAnchorTransferred"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTotalHandoffRequestsReceived"))
)
if mibBuilder.loadTexts:
    bsnMobilityGroup.setStatus("current")

bsnIpsecGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14179, 2, 50, 9)
)
bsnIpsecGroup.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnWrasIpsecCACertificate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnWrasIpsecCACertificateUpdate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnWrasIpsecCertName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnWrasIpsecCertificateUpdate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnWrasIpsecCertificate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnWrasIpsecCertPassword"),
        ("AIRESPACE-WIRELESS-MIB", "bsnWrasIpsecCertStatus"))
)
if mibBuilder.loadTexts:
    bsnIpsecGroup.setStatus("current")

bsnWrasDepGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14179, 2, 50, 10)
)
bsnWrasDepGroup.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnDot11EssWPASecurity"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssWPAEncryptionType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssWPAAuthKeyMgmtMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssWPAAuthPresharedKey"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssWPAAuthPresharedKeyHex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssRSNSecurity"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssRSNWPACompatibilityMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssRSNAllowTKIPClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssRSNAuthKeyMgmtMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssRSNAuthPresharedKey"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssRSNAuthPresharedKeyHex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11NumberSupportedPowerLevels"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11TxPowerLevel1"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11TxPowerLevel2"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11TxPowerLevel3"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11TxPowerLevel4"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11TxPowerLevel5"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11TxPowerLevel6"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11TxPowerLevel7"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11TxPowerLevel8"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11CurrentCCAMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLinkTestId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLinkTestMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLinkTestSendPktCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLinkTestSendPktLength"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLinkTestReceivedPktCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLinkTestClientRSSI"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLinkTestLocalSNR"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLinkTestLocalRSSI"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLinkTestStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLinkTestRowStatus"))
)
if mibBuilder.loadTexts:
    bsnWrasDepGroup.setStatus("deprecated")

bsnWrasObsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14179, 2, 50, 11)
)
bsnWrasObsGroup.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnUserName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnUserPassword"),
        ("AIRESPACE-WIRELESS-MIB", "bsnUserEssIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnUserAccessMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnUserType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnUserInterfaceName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnUserRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnExternalPolicyServerIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnExternalPolicyServerAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnExternalPolicyServerPortNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnExternalPolicyServerKey"),
        ("AIRESPACE-WIRELESS-MIB", "bsnExternalPolicyServerAdminStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnExternalPolicyServerConnectionStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnExternalPolicyServerRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnThirdPartyAPMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnThirdPartyAPInterface"),
        ("AIRESPACE-WIRELESS-MIB", "bsnThirdPartyAPIpAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnThirdPartyAP802Dot1XRequired"),
        ("AIRESPACE-WIRELESS-MIB", "bsnThirdPartyAPMirrorMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnThirdPartyAPRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnWatchListClientKey"),
        ("AIRESPACE-WIRELESS-MIB", "bsnWatchListClientType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnWatchListClientRowStatus"))
)
if mibBuilder.loadTexts:
    bsnWrasObsGroup.setStatus("obsolete")

bsnEssGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14179, 2, 50, 13)
)
bsnEssGroupRev1.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnDot11EssIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssSsid"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssSessionTimeout"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssMacFiltering"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssAdminStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssSecurityAuthType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssStaticWEPSecurity"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssStaticWEPEncryptionType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssStaticWEPDefaultKey"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssStaticWEPKeyIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssStaticWEPKeyFormat"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11Ess8021xSecurity"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11Ess8021xEncryptionType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssIpsecSecurity"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssVpnEncrTransform"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssVpnAuthTransform"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssVpnIkeAuthMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssVpnSharedKey"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssVpnSharedKeySize"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssVpnIkePhase1Mode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssVpnIkeLifetime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssVpnIkeDHGroup"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssIpsecPassthruSecurity"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssVpnPassthruGateway"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssWebSecurity"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssRadioPolicy"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssQualityOfService"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssDhcpRequired"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssDhcpServerIpAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssVpnContivityMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssVpnQotdServerAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssBlacklistTimeout"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssNumberOfMobileStations"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssWebPassthru"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssCraniteSecurity"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssBlacklistingCapability"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssInterfaceName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssAclName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssAAAOverride"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssWepAllowSharedKeyAuth"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssFortressSecurity"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssL2tpSecurity"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssBroadcastSsid"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssExternalPolicyValidation"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssWmePolicySetting"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11Ess80211ePolicySetting"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssWebPassthroughEmail"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11Ess7920PhoneSupport"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssRadiusAuthPrimaryServer"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssRadiusAuthSecondaryServer"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssRadiusAuthTertiaryServer"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssRadiusAcctPrimaryServer"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssRadiusAcctSecondaryServer"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssRadiusAcctTertiaryServer"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationIpAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationUserName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationAPMacAddr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationEssIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationSsid"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationReasonCode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationMobilityStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationAID"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationAnchorAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationCFPollable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationCFPollRequest"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationChannelAgilityEnabled"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationPBCCOptionImplemented"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationShortPreambleOptionImplemented"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationSessionTimeout"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationAuthenticationAlgorithm"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationWepState"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationPortNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationDeleteAction"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationPolicyManagerState"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationSecurityPolicyStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationProtocol"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationMirrorMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationInterface"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationApMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationVlanId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationPolicyType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationEncryptionCypher"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationEapType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationCcxVersion"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationE2eVersion"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationStatusCode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationPerRadioPerVapIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationMacAddr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationRSSI"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationBytesReceived"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationBytesSent"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationPolicyErrors"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationPacketsReceived"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationPacketsSent"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationSnr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPDot11MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPTotalDetectingAPs"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPFirstReported"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPLastReported"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPContainmentLevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPOnNetwork"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPTotalClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPMaxDetectedRSSI"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPSSID"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPState"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPDetectingAPRadioType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPDetectingAPMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPMaxRssiRadioType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPClassType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPChannel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPDetectingAPName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPChannelWidth"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPAirespaceAPMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPAirespaceAPSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPRadioType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPAirespaceAPName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPChannelNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPSsid"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPAirespaceAPRSSI"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPContainmentMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPContainmentChannelCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPContainmentChannels"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPAirespaceAPLastHeard"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPAirespaceAPWepMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPAirespaceAPPreamble"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPAirespaceAPWpaMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPAirespaceAPSNR"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationByIpAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationByIpMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationRssiDataApMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationRssiDataApIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationRssiDataApIfType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationRssiDataApName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationRssiData"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfPhyAntennaIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationRssiDataLastHeard"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationByUserName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationByUserMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientAirespaceAPMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientAirespaceAPSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientRadioType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientAirespaceAPName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientChannelNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientAirespaceAPRSSI"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientAirespaceAPLastHeard"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientAirespaceAPSNR"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientTotalDetectingAPs"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientFirstReported"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientLastReported"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientBSSID"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientContainmentLevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientLastHeard"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientState"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPDot11MacAddr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueClientDot11MacAddr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11QosProfileName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11QosProfileDesc"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11QosAverageDataRate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11QosBurstDataRate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11QosAvgRealTimeDataRate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11QosBurstRealTimeDataRate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11QosMaxRFUsagePerAP"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11QosProfileQueueDepth"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11WiredQosProtocol"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11802Dot1PTag"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11ResetProfileToDefault"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTagDot11MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTagType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTagTimeInterval"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTagBatteryStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTagLastReported"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTagRssiDataApMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTagRssiDataApIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTagRssiDataApIfType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTagRssiDataApName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTagRssiDataLastHeard"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTagRssiData"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTagRssiDataSnr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTagBytesReceived"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTagPacketsReceived"))
)
if mibBuilder.loadTexts:
    bsnEssGroupRev1.setStatus("current")

bsnGlobalDot11GroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14179, 2, 50, 14)
)
bsnGlobalDot11GroupRev1.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11PrivacyOptionImplemented"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11AuthenticationResponseTimeOut"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11MultiDomainCapabilityImplemented"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11MultiDomainCapabilityEnabled"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11RogueTimer"),
        ("AIRESPACE-WIRELESS-MIB", "bsnPrimaryMwarForAPs"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRtpProtocolPriority"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSystemCurrentTime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnUpdateSystemTime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnOperatingTemperatureEnvironment"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSensorTemperature"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTemperatureAlarmLowLimit"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTemperatureAlarmHighLimit"),
        ("AIRESPACE-WIRELESS-MIB", "bsnVirtualGatewayAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRFMobilityDomainName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnClientWatchListFeature"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueLocationDiscoveryProtocol"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAutoContainFeature"),
        ("AIRESPACE-WIRELESS-MIB", "bsnOverAirProvisionApMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMaximumNumberOfConcurrentLogins"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAutoContainRoguesAdvertisingSsid"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAutoContainAdhocNetworks"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAutoContainTrustedClientsOnRogueAps"),
        ("AIRESPACE-WIRELESS-MIB", "bsnValidateRogueClientsAgainstAAA"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSystemTimezoneDelta"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSystemTimezoneDeltaMinutes"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAllowAuthorizeApAgainstAAA"),
        ("AIRESPACE-WIRELESS-MIB", "bsnApFallbackEnabled"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAppleTalkEnabled"),
        ("AIRESPACE-WIRELESS-MIB", "bsnPolicyForMisconfiguredAps"),
        ("AIRESPACE-WIRELESS-MIB", "bsnEncryptionPolicyEnforced"),
        ("AIRESPACE-WIRELESS-MIB", "bsnPreamblePolicyEnforced"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11ModePolicyEnforced"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadioTypePolicyEnforced"),
        ("AIRESPACE-WIRELESS-MIB", "bsnValidateSsidForTrustedAp"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAlertIfTrustedApMissing"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApEntryExpirationTimeout"),
        ("AIRESPACE-WIRELESS-MIB", "bsnExcessive80211AssocFailures"),
        ("AIRESPACE-WIRELESS-MIB", "bsnExcessive80211AuthFailures"),
        ("AIRESPACE-WIRELESS-MIB", "bsnExcessive8021xAuthFailures"),
        ("AIRESPACE-WIRELESS-MIB", "bsnExternalPolicyServerFailures"),
        ("AIRESPACE-WIRELESS-MIB", "bsnExcessiveWebAuthFailures"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIPTheftORReuse"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignaturePrecedence"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignatureName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignatureDescription"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignatureFrameType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignatureAction"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignatureState"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignatureFrequency"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignatureQuietTime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignatureVersion"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignatureConfigType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignatureEnable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignatureMacInfo"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignatureMacFreq"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignatureRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignaturePatternIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignaturePatternOffset"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignaturePatternString"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignaturePatternMask"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignaturePatternOffSetStart"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignaturePatternRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignaturePrecedence"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignatureName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignatureDescription"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignatureFrameType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignatureAction"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignatureState"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignatureFrequency"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignatureQuietTime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignatureVersion"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignatureConfigType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignatureEnable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignatureMacInfo"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignatureMacFreq"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignatureRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignaturePatternIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignaturePatternOffset"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignaturePatternString"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignaturePatternMask"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignaturePatternOffSetStart"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignaturePatternRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSignatureCheckState"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRfIdTagStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRfIdTagDataTimeout"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRfIdTagAutoTimeoutStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPNeighborAuthStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPNeighborAuthAlarmThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRFNetworkName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnFastSSIDChangeFeature"),
        ("AIRESPACE-WIRELESS-MIB", "bsnBridgingZeroTouchConfig"),
        ("AIRESPACE-WIRELESS-MIB", "bsnBridgingSharedSecretKey"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bNetworkStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bBeaconPeriod"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDynamicChannelAssignment"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bCurrentChannel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDynamicChannelUpdateInterval"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bInputsForDCA"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bChannelUpdateCmdInvoke"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bChannelUpdateCmdStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDynamicTransmitPowerControl"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDynamicTxPowerControlInterval"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bCurrentTxPowerLevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bInputsForDTP"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bPowerUpdateCmdInvoke"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bPowerUpdateCmdStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDataRate1Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDataRate2Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDataRate5AndHalfMhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDataRate11Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bShortPreamble"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDot11gSupport"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDataRate6Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDataRate9Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDataRate12Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDataRate18Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDataRate24Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDataRate36Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDataRate48Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDataRate54Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bPicoCellMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bFastRoamingMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bFastRoamingVoipMinRate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bFastRoamingVoipPercentage"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11b80211eMaxBandwidth"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDTPCSupport"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bRxSopThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bMediumOccupancyLimit"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bCFPPeriod"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bCFPMaxDuration"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bCFPollable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bCFPollRequest"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bDTIMPeriod"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bRTSThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bShortRetryLimit"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bLongRetryLimit"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bFragmentationThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bMaxTransmitMSDULifetime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bMaxReceiveLifetime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bEDThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bChannelAgilityEnabled"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bPBCCOptionImplemented"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11bShortPreambleOptionImplemented"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aNetworkStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aLowBandNetwork"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aMediumBandNetwork"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aHighBandNetwork"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aBeaconPeriod"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aDynamicChannelAssignment"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aCurrentChannel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aDynamicChannelUpdateInterval"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aInputsForDCA"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aChannelUpdateCmdInvoke"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aChannelUpdateCmdStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aDynamicTransmitPowerControl"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aCurrentTxPowerLevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aDynamicTxPowerControlInterval"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aInputsForDTP"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aPowerUpdateCmdInvoke"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aPowerUpdateCmdStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aDataRate6Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aDataRate9Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aDataRate12Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aDataRate18Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aDataRate24Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aDataRate36Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aDataRate48Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aDataRate54Mhz"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aPicoCellMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aFastRoamingMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aFastRoamingVoipMinRate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aFastRoamingVoipPercentage"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11a80211eMaxBandwidth"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aDTPCSupport"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aRxSopThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aMediumOccupancyLimit"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aCFPPeriod"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aCFPMaxDuration"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aCFPollable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aCFPollRequest"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aDTIMPeriod"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aRTSThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aShortRetryLimit"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aLongRetryLimit"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aFragmentationThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aMaxTransmitMSDULifetime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aMaxReceiveLifetime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aTIThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11aChannelAgilityEnabled"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11hPowerConstraint"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11hChannelSwitchEnable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11hChannelSwitchMode"))
)
if mibBuilder.loadTexts:
    bsnGlobalDot11GroupRev1.setStatus("current")

bsnAAAGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14179, 2, 50, 15)
)
bsnAAAGroupRev1.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthClientServerPortNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerKey"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerKeyFormat"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerRFC3576"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerIPSec"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerIPSecAuth"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerIPSecEncryption"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerIPSecIKEPhase1"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerIPSecIKELifetime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerIPSecDHGroup"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerNetworkUserConfig"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerMgmtUserConfig"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerRetransmitTimeout"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerKeyWrapKEKkey"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerKeyWrapMACKkey"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerKeyWrapFormat"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthServerRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccClientServerPortNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerKey"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerKeyFormat"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerIPSec"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerIPSecAuth"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerIPSecEncryption"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerIPSecIKEPhase1"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerIPSecIKELifetime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerIPSecDHGroup"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerNetworkUserConfig"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerRetransmitTimeout"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccServerRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthClientRoundTripTime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthClientAccessRequests"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthClientAccessRetransmissions"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthClientAccessAccepts"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthClientAccessRejects"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthClientAccessChallenges"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthClientMalformedAccessResponses"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthClientBadAuthenticators"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthClientPendingRequests"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthClientTimeouts"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthClientUnknownTypes"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthClientPacketsDropped"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccClientRoundTripTime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccClientRequests"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccClientRetransmissions"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccClientResponses"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccClientMalformedResponses"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccClientBadAuthenticators"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccClientPendingRequests"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccClientTimeouts"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccClientUnknownTypes"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAccClientPacketsDropped"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclApplyMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRuleIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRuleAction"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRuleDirection"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRuleSourceIpAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRuleSourceIpNetmask"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRuleDestinationIpAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRuleDestinationIpNetmask"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRuleProtocol"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRuleStartSourcePort"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRuleEndSourcePort"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRuleStartDestinationPort"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRuleEndDestinationPort"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRuleDscp"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclNewRuleIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAclRuleRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMacFilterAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMacFilterWlanId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMacFilterInterfaceName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMacFilterDescription"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMacFilterRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLocalNetUserName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLocalNetUserWlanId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLocalNetUserPassword"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLocalNetUserDescription"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLocalNetUserLifetime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLocalNetUserStartTime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLocalNetUserRemainingTime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLocalNetUserRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLocalManagementUserName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLocalManagementUserPassword"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLocalManagementUserAccessMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLocalManagementUserRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnBlackListClientMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnBlackListClientDescription"),
        ("AIRESPACE-WIRELESS-MIB", "bsnBlackListClientRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiusAuthKeyWrapEnable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAAAMacDelimiter"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAAARadiusCompatibilityMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAAARadiusCallStationIdType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAAALocalDatabaseSize"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAAACurrentLocalDatabaseSize"),
        ("AIRESPACE-WIRELESS-MIB", "bsnExternalPolicyServerAclName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAcceptSelfSignedCertificate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSystemClockTime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPAuthMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPAuthCertificateType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPAuthHashKey"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPAuthRowStatus"))
)
if mibBuilder.loadTexts:
    bsnAAAGroupRev1.setStatus("current")

bsnTrapsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14179, 2, 50, 16)
)
bsnTrapsGroupRev1.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnDot11StationTrapControlMask"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPTrapControlMask"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPProfileTrapControlMask"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPMacAddrTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPNameTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPSlotIdTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPChannelNumberTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPCoverageThresholdTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPCoverageFailedClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPCoverageTotalClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnClientMacAddr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnClientRssi"),
        ("AIRESPACE-WIRELESS-MIB", "bsnClientSnr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnInterferenceEnergyBeforeChannelUpdate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnInterferenceEnergyAfterChannelUpdate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPPortNumberTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPParamUpdateTrapControlMask"),
        ("AIRESPACE-WIRELESS-MIB", "bsnConfigSaveTrapEnable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRADIUSServerTrapEnable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAuthenticationFailureTrapEnable"),
        ("AIRESPACE-WIRELESS-MIB", "bsn80211SecurityTrapControlMask"),
        ("AIRESPACE-WIRELESS-MIB", "bsnWpsTrapControlEnable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAuthFailureUserName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAuthFailureUserType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRemoteIPv4Address"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIpsecErrorCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIpsecSPI"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRemoteUdpPort"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIkeAuthMethod"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIkeTotalInitFailures"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIkeTotalInitNoResponses"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIkeTotalRespFailures"),
        ("AIRESPACE-WIRELESS-MIB", "bsnNotifiesSent"),
        ("AIRESPACE-WIRELESS-MIB", "bsnNotifiesReceived"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSuiteInitFailures"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSuiteRespondFailures"),
        ("AIRESPACE-WIRELESS-MIB", "bsnInitiatorCookie"),
        ("AIRESPACE-WIRELESS-MIB", "bsnResponderCookie"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIsakmpInvalidCookies"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIpsecTrapsMask"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPTrapEnable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCurrentRadiosCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLicenseRadioCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMaxRogueCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationAPMacAddr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnUserIpAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationReasonCode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationBlacklistingReasonCode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationUserName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPOnWiredNetwork"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAdhocMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDuplicateIpReportedByAP"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDuplicateIpTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDuplicateIpTrapClear"),
        ("AIRESPACE-WIRELESS-MIB", "bsnNavDosAttackSourceMacAddr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnWlanIdTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnClearTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApEncryptionUsed"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApEncryptionRequired"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApRadioPolicyUsed"),
        ("AIRESPACE-WIRELESS-MIB", "bsnNetworkType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnNetworkState"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSignatureType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSignatureName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSignatureDescription"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSignatureAttackPreced"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSignatureAttackFrequency"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSignatureAttackChannel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSignatureAttackerMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnApRegulatoryDomain"),
        ("AIRESPACE-WIRELESS-MIB", "bsnImpersonatedAPMacAddr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApPreambleUsed"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApPreambleRequired"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApRadioPolicyRequired"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGroupDirectoryMemberIPAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGroupDirectoryMemberMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGroupDirectoryDicoveryType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMemberCurrentAnchoredClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMemberTotalAnchoredClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMemberCurrentExportedClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMemberTotalExportedClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMemberCurrentImportedClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMemberTotalImportedClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMemberTotalHandoffErrors"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMemberTotalCommunicationErrors"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPGroupsVlanFeature"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPGroupsVlanName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPGroupsVlanDescription"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPGroupsVlanRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLicenseKeyTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnApFunctionalityDisableReasonCode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLicenseKeyFeatureSetTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPAuthorizationFailureCause"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfUpDownCause"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPInvalidRadioType"),
        ("AIRESPACE-WIRELESS-MIB", "locationNotifyContent"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSignatureMacInfo"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPPreviousChannelNumberTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPReasonCodeTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnNoiseBeforeChannelUpdate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnNoiseAfterChannelUpdate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnInterferenceBeforeChannelUpdate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnInterferenceAfterChannelUpdate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnImpersonatingSourceMacAddr"))
)
if mibBuilder.loadTexts:
    bsnTrapsGroupRev1.setStatus("current")

bsnApGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14179, 2, 50, 18)
)
bsnApGroupRev1.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPNumOfSlots"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPLocation"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPMonitorOnlyMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPOperationStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPSoftwareVersion"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPBootVersion"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPPrimaryMwarName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPReset"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPStatsTimer"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPModel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPSerialNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPClearConfig"),
        ("AIRESPACE-WIRELESS-MIB", "bsnApIpAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPMirrorMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPRemoteModeSupport"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPSecondaryMwarName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPTertiaryMwarName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIsStaticIP"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPNetmask"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPGateway"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPStaticIPAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPBridgingSupport"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPGroupVlanName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIOSVersion"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPCertificateType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPEthernetMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfPhyChannelAssignment"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfPhyChannelNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfPhyTxPowerControl"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfPhyTxPowerLevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfPhyAntennaMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfPhyAntennaType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfPhyAntennaDiversity"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfCellSiteConfigId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfNumberOfVaps"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfOperStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfPortNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfPhyAntennaOptions"),
        ("AIRESPACE-WIRELESS-MIB", "bsnApIfNoOfUsers"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfWlanOverride"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfPacketsSniffingFeature"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSniffChannel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSniffServerIPAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfAntennaGain"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfChannelList"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfAbsolutePowerList"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfRegulatoryDomainSupport"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11BeaconPeriod"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11MediumOccupancyLimit"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11CFPPeriod"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11CFPMaxDuration"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11OperationalRateSet"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11DTIMPeriod"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11MultiDomainCapabilityImplemented"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11MultiDomainCapabilityEnabled"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11CountryString"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11SmtParamsConfigType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11BSSID"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11MaximumTransmitPowerLevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11FirstChannelNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11NumberofChannels"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11MacRTSThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11MacShortRetryLimit"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11MacLongRetryLimit"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11MacFragmentationThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11MacMaxTransmitMSDULifetime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11MacParamsConfigType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11MacMaxReceiveLifetime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11TransmittedFragmentCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11MulticastTransmittedFrameCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11RetryCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11MultipleRetryCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11FrameDuplicateCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11RTSSuccessCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11RTSFailureCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11ACKFailureCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11ReceivedFragmentCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11MulticastReceivedFrameCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11FCSErrorCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11TransmittedFrameCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11WEPUndecryptableCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11FailedCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11EDThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDot11TIThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfProfileParamAssignment"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfForeignInterferenceThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfForeignNoiseThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfRFUtilizationThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfThroughputThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfMobilesThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfCoverageThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfMobileMinExceptionLevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfCoverageExceptionLevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfLoadRxUtilization"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfLoadTxUtilization"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfLoadChannelUtilization"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfLoadNumOfClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfPoorSNRClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfInterferenceChannelNo"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfInterferencePower"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfInterferenceUtilization"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfNoiseChannelNo"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDBNoisePower"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfLoadProfileState"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfInterferenceProfileState"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfNoiseProfileState"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfCoverageProfileState"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfRxNeighborMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfRxNeighborIpAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfRxNeighborRSSI"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfRxNeighborSlot"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfStationRSSICoverageIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfRSSILevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfStationCountOnRSSI"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfStationSNRCoverageIndex"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSNRLevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfStationCountOnSNR"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfRecommendedChannelNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfRecommendedTxPowerLevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfRecommendedRTSThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfRecommendedFragmentationThreshold"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfWlanOverrideId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfWlanOverrideSsid"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfWlanOverrideRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeRole"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeGroup"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeBackhaul"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeBackhaulPAP"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeBackhaulRAP"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeDataRate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeChannel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeRoutingState"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeMalformedNeighPackets"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodePoorNeighSnr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeBlacklistPackets"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeInsufficientMemory"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeRxNeighReq"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeRxNeighRsp"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeTxNeighReq"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeTxNeighRsp"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeParentChanges"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeNeighTimeout"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeParentMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeAPType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeEthernetBridge"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNodeHops"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighState"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighSnr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighSnrUp"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighSnrDown"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighLinkSnr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighAdjustedEase"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighUnadjustedEase"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighRapEase"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighTxParent"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighRxParent"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighPoorSnr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighLastUpdate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMeshNeighParentChange"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfRadarDetectedChannelNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfRadarSignalLastHeard"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfRxNeighborChannel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfRxNeighborChannelWidth"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStandardSignatureInterval"),
        ("AIRESPACE-WIRELESS-MIB", "bsnCustomSignatureInterval"))
)
if mibBuilder.loadTexts:
    bsnApGroupRev1.setStatus("current")

bsnUtilityGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14179, 2, 50, 19)
)
bsnUtilityGroupRev1.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnSyslogEnable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSyslogRemoteAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnPingTestId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnPingTestIPAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnPingTestSendCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnPingTestReceivedCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnPingTestStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnPingTestRowStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnPingTestMaxTimeInterval"),
        ("AIRESPACE-WIRELESS-MIB", "bsnPingTestMinTimeInterval"),
        ("AIRESPACE-WIRELESS-MIB", "bsnPingTestAvgTimeInterval"))
)
if mibBuilder.loadTexts:
    bsnUtilityGroupRev1.setStatus("current")

bsnWrasObsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14179, 2, 50, 20)
)
bsnWrasObsGroupRev1.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnMobileStationSampleTime"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationTxExcessiveRetries"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationTxRetries"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMobileStationTxFiltered"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSystemTimezoneDaylightSavings"))
)
if mibBuilder.loadTexts:
    bsnWrasObsGroupRev1.setStatus("obsolete")


# Notification objects

bsnDot11StationDisassociate = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 1)
)
bsnDot11StationDisassociate.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnStationAPMacAddr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationReasonCode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnUserIpAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationUserName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnDot11StationDisassociate.setStatus(
        "current"
    )

bsnDot11StationDeauthenticate = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 2)
)
bsnDot11StationDeauthenticate.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnStationAPMacAddr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationReasonCode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnUserIpAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationUserName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnDot11StationDeauthenticate.setStatus(
        "current"
    )

bsnDot11StationAuthenticateFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 3)
)
bsnDot11StationAuthenticateFail.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnStationAPMacAddr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationReasonCode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnUserIpAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationUserName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnDot11StationAuthenticateFail.setStatus(
        "current"
    )

bsnDot11StationAssociateFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 4)
)
bsnDot11StationAssociateFail.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnStationAPMacAddr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationReasonCode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnUserIpAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationUserName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnDot11StationAssociateFail.setStatus(
        "current"
    )

bsnAPUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 5)
)
bsnAPUp.setObjects(
    ("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress")
)
if mibBuilder.loadTexts:
    bsnAPUp.setStatus(
        "obsolete"
    )

bsnAPDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 6)
)
bsnAPDown.setObjects(
    ("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress")
)
if mibBuilder.loadTexts:
    bsnAPDown.setStatus(
        "obsolete"
    )

bsnAPAssociated = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 7)
)
bsnAPAssociated.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPMacAddrTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPPortNumberTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnAPAssociated.setStatus(
        "deprecated"
    )

bsnAPDisassociated = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 8)
)
bsnAPDisassociated.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPMacAddrTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnAPDisassociated.setStatus(
        "current"
    )

bsnAPIfUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 9)
)
bsnAPIfUp.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPPortNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfUpDownCause"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnAPIfUp.setStatus(
        "deprecated"
    )

bsnAPIfDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 10)
)
bsnAPIfDown.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPAdminStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfAdminStatus"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfUpDownCause"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnAPIfDown.setStatus(
        "deprecated"
    )

bsnAPLoadProfileFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 11)
)
bsnAPLoadProfileFailed.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnAPLoadProfileFailed.setStatus(
        "current"
    )

bsnAPNoiseProfileFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 12)
)
bsnAPNoiseProfileFailed.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnAPNoiseProfileFailed.setStatus(
        "current"
    )

bsnAPInterferenceProfileFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 13)
)
bsnAPInterferenceProfileFailed.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnAPInterferenceProfileFailed.setStatus(
        "current"
    )

bsnAPCoverageProfileFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 14)
)
bsnAPCoverageProfileFailed.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPMacAddrTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPNameTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPSlotIdTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPCoverageThresholdTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPCoverageFailedClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPCoverageTotalClients"),
        ("AIRESPACE-WIRELESS-MIB", "bsnClientMacAddr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnClientRssi"),
        ("AIRESPACE-WIRELESS-MIB", "bsnClientSnr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnAPCoverageProfileFailed.setStatus(
        "current"
    )

bsnAPCurrentTxPowerChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 15)
)
bsnAPCurrentTxPowerChanged.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfPhyTxPowerLevel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnAPCurrentTxPowerChanged.setStatus(
        "current"
    )

bsnAPCurrentChannelChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 16)
)
bsnAPCurrentChannelChanged.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPMacAddrTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPSlotIdTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPChannelNumberTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnInterferenceEnergyBeforeChannelUpdate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnInterferenceEnergyAfterChannelUpdate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPPreviousChannelNumberTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPReasonCodeTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnNoiseBeforeChannelUpdate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnNoiseAfterChannelUpdate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnInterferenceBeforeChannelUpdate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnInterferenceAfterChannelUpdate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnAPCurrentChannelChanged.setStatus(
        "current"
    )

bsnRrmDot11aGroupingDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 21)
)
bsnRrmDot11aGroupingDone.setObjects(
    ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11aGroupLeaderMacAddr")
)
if mibBuilder.loadTexts:
    bsnRrmDot11aGroupingDone.setStatus(
        "current"
    )

bsnRrmDot11bGroupingDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 22)
)
bsnRrmDot11bGroupingDone.setObjects(
    ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11bGroupLeaderMacAddr")
)
if mibBuilder.loadTexts:
    bsnRrmDot11bGroupingDone.setStatus(
        "current"
    )

bsnConfigSaved = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 23)
)
if mibBuilder.loadTexts:
    bsnConfigSaved.setStatus(
        "current"
    )

bsnDot11EssCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 24)
)
bsnDot11EssCreated.setObjects(
    ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssIndex")
)
if mibBuilder.loadTexts:
    bsnDot11EssCreated.setStatus(
        "current"
    )

bsnDot11EssDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 25)
)
bsnDot11EssDeleted.setObjects(
    ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssIndex")
)
if mibBuilder.loadTexts:
    bsnDot11EssDeleted.setStatus(
        "current"
    )

bsnRADIUSServerNotResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 26)
)
if mibBuilder.loadTexts:
    bsnRADIUSServerNotResponding.setStatus(
        "current"
    )

bsnAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 27)
)
bsnAuthenticationFailure.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAuthFailureUserType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAuthFailureUserName"))
)
if mibBuilder.loadTexts:
    bsnAuthenticationFailure.setStatus(
        "current"
    )

bsnIpsecEspAuthFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 28)
)
bsnIpsecEspAuthFailureTrap.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnRemoteIPv4Address"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIpsecErrorCount"))
)
if mibBuilder.loadTexts:
    bsnIpsecEspAuthFailureTrap.setStatus(
        "current"
    )

bsnIpsecEspReplayFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 29)
)
bsnIpsecEspReplayFailureTrap.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnRemoteIPv4Address"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIpsecErrorCount"))
)
if mibBuilder.loadTexts:
    bsnIpsecEspReplayFailureTrap.setStatus(
        "current"
    )

bsnIpsecEspInvalidSpiTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 31)
)
bsnIpsecEspInvalidSpiTrap.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnRemoteIPv4Address"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIpsecSPI"))
)
if mibBuilder.loadTexts:
    bsnIpsecEspInvalidSpiTrap.setStatus(
        "current"
    )

bsnIpsecIkeNegFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 33)
)
bsnIpsecIkeNegFailure.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnRemoteIPv4Address"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRemoteUdpPort"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIkeAuthMethod"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIkeTotalInitFailures"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIkeTotalInitNoResponses"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIkeTotalRespFailures"),
        ("AIRESPACE-WIRELESS-MIB", "bsnNotifiesSent"),
        ("AIRESPACE-WIRELESS-MIB", "bsnNotifiesReceived"))
)
if mibBuilder.loadTexts:
    bsnIpsecIkeNegFailure.setStatus(
        "current"
    )

bsnIpsecSuiteNegFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 34)
)
bsnIpsecSuiteNegFailure.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnRemoteIPv4Address"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSuiteInitFailures"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSuiteRespondFailures"),
        ("AIRESPACE-WIRELESS-MIB", "bsnNotifiesSent"),
        ("AIRESPACE-WIRELESS-MIB", "bsnNotifiesReceived"))
)
if mibBuilder.loadTexts:
    bsnIpsecSuiteNegFailure.setStatus(
        "current"
    )

bsnIpsecInvalidCookieTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 35)
)
bsnIpsecInvalidCookieTrap.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnRemoteIPv4Address"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRemoteUdpPort"),
        ("AIRESPACE-WIRELESS-MIB", "bsnInitiatorCookie"),
        ("AIRESPACE-WIRELESS-MIB", "bsnResponderCookie"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIsakmpInvalidCookies"))
)
if mibBuilder.loadTexts:
    bsnIpsecInvalidCookieTrap.setStatus(
        "current"
    )

bsnRogueAPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 36)
)
bsnRogueAPDetected.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnRogueAPDot11MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPAirespaceAPMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPAirespaceAPSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPSsid"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPChannelNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPAirespaceAPRSSI"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPAirespaceAPSNR"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPOnWiredNetwork"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAdhocMode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPRadioType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPAirespaceAPName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPClassType"))
)
if mibBuilder.loadTexts:
    bsnRogueAPDetected.setStatus(
        "deprecated"
    )

bsnAPLoadProfileUpdatedToPass = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 37)
)
bsnAPLoadProfileUpdatedToPass.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnAPLoadProfileUpdatedToPass.setStatus(
        "current"
    )

bsnAPNoiseProfileUpdatedToPass = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 38)
)
bsnAPNoiseProfileUpdatedToPass.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnAPNoiseProfileUpdatedToPass.setStatus(
        "current"
    )

bsnAPInterferenceProfileUpdatedToPass = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 39)
)
bsnAPInterferenceProfileUpdatedToPass.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnAPInterferenceProfileUpdatedToPass.setStatus(
        "current"
    )

bsnAPCoverageProfileUpdatedToPass = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 40)
)
bsnAPCoverageProfileUpdatedToPass.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnAPCoverageProfileUpdatedToPass.setStatus(
        "current"
    )

bsnRogueAPRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 41)
)
bsnRogueAPRemoved.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnRogueAPDot11MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPAirespaceAPMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPAirespaceAPSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPRadioType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPAirespaceAPName"))
)
if mibBuilder.loadTexts:
    bsnRogueAPRemoved.setStatus(
        "current"
    )

bsnRadiosExceedLicenseCount = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 42)
)
bsnRadiosExceedLicenseCount.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnCurrentRadiosCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLicenseRadioCount"))
)
if mibBuilder.loadTexts:
    bsnRadiosExceedLicenseCount.setStatus(
        "current"
    )

bsnSensedTemperatureTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 43)
)
bsnSensedTemperatureTooHigh.setObjects(
    ("AIRESPACE-WIRELESS-MIB", "bsnSensorTemperature")
)
if mibBuilder.loadTexts:
    bsnSensedTemperatureTooHigh.setStatus(
        "current"
    )

bsnSensedTemperatureTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 44)
)
bsnSensedTemperatureTooLow.setObjects(
    ("AIRESPACE-WIRELESS-MIB", "bsnSensorTemperature")
)
if mibBuilder.loadTexts:
    bsnSensedTemperatureTooLow.setStatus(
        "current"
    )

bsnTemperatureSensorFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 45)
)
if mibBuilder.loadTexts:
    bsnTemperatureSensorFailure.setStatus(
        "current"
    )

bsnTemperatureSensorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 46)
)
bsnTemperatureSensorClear.setObjects(
    ("AIRESPACE-WIRELESS-MIB", "bsnSensorTemperature")
)
if mibBuilder.loadTexts:
    bsnTemperatureSensorClear.setStatus(
        "current"
    )

bsnPOEControllerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 47)
)
if mibBuilder.loadTexts:
    bsnPOEControllerFailure.setStatus(
        "current"
    )

bsnMaxRogueCountExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 48)
)
bsnMaxRogueCountExceeded.setObjects(
    ("AIRESPACE-WIRELESS-MIB", "bsnMaxRogueCount")
)
if mibBuilder.loadTexts:
    bsnMaxRogueCountExceeded.setStatus(
        "current"
    )

bsnMaxRogueCountClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 49)
)
bsnMaxRogueCountClear.setObjects(
    ("AIRESPACE-WIRELESS-MIB", "bsnMaxRogueCount")
)
if mibBuilder.loadTexts:
    bsnMaxRogueCountClear.setStatus(
        "current"
    )

bsnApMaxRogueCountExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 50)
)
bsnApMaxRogueCountExceeded.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPMacAddrTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMaxRogueCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnApMaxRogueCountExceeded.setStatus(
        "current"
    )

bsnApMaxRogueCountClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 51)
)
bsnApMaxRogueCountClear.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPMacAddrTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMaxRogueCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnApMaxRogueCountClear.setStatus(
        "current"
    )

bsnDot11StationBlacklisted = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 52)
)
bsnDot11StationBlacklisted.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnStationAPMacAddr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationBlacklistingReasonCode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnUserIpAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationUserName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnDot11StationBlacklisted.setStatus(
        "current"
    )

bsnDot11StationAssociate = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 53)
)
bsnDot11StationAssociate.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnStationAPMacAddr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnUserIpAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationUserName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnDot11StationAssociate.setStatus(
        "current"
    )

bsnApBigNavDosAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 55)
)
bsnApBigNavDosAttack.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPMacAddrTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPSlotIdTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnNavDosAttackSourceMacAddr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnApBigNavDosAttack.setStatus(
        "current"
    )

bsnTooManyUnsuccessLoginAttempts = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 56)
)
bsnTooManyUnsuccessLoginAttempts.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnUserIpAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationUserName"))
)
if mibBuilder.loadTexts:
    bsnTooManyUnsuccessLoginAttempts.setStatus(
        "current"
    )

bsnWepKeyDecryptError = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 57)
)
bsnWepKeyDecryptError.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnStationMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationAPMacAddr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationAPIfSlotId"))
)
if mibBuilder.loadTexts:
    bsnWepKeyDecryptError.setStatus(
        "current"
    )

bsnWpaMicErrorCounterActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 58)
)
bsnWpaMicErrorCounterActivated.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnStationMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationAPMacAddr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnStationAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnWlanIdTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnWpaMicErrorCounterActivated.setStatus(
        "current"
    )

bsnRogueAPDetectedOnWiredNetwork = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 59)
)
bsnRogueAPDetectedOnWiredNetwork.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnRogueAPDot11MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPOnWiredNetwork"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnRogueAPDetectedOnWiredNetwork.setStatus(
        "current"
    )

bsnApHasNoRadioCards = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 60)
)
bsnApHasNoRadioCards.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPMacAddrTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnApHasNoRadioCards.setStatus(
        "current"
    )

bsnDuplicateIpAddressReported = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 61)
)
bsnDuplicateIpAddressReported.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnDuplicateIpReportedByAP"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPMacAddrTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDuplicateIpTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPDot11MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDuplicateIpTrapClear"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnDuplicateIpAddressReported.setStatus(
        "current"
    )

bsnAPContainedAsARogue = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 62)
)
bsnAPContainedAsARogue.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnClearTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnAPContainedAsARogue.setStatus(
        "current"
    )

bsnTrustedApHasInvalidSsid = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 63)
)
bsnTrustedApHasInvalidSsid.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnRogueAPDot11MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnClearTrapVariable"))
)
if mibBuilder.loadTexts:
    bsnTrustedApHasInvalidSsid.setStatus(
        "current"
    )

bsnTrustedApIsMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 64)
)
bsnTrustedApIsMissing.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnRogueAPDot11MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnClearTrapVariable"))
)
if mibBuilder.loadTexts:
    bsnTrustedApIsMissing.setStatus(
        "current"
    )

bsnAdhocRogueAutoContained = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 65)
)
bsnAdhocRogueAutoContained.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnRogueAPDot11MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnClearTrapVariable"))
)
if mibBuilder.loadTexts:
    bsnAdhocRogueAutoContained.setStatus(
        "current"
    )

bsnRogueApAutoContained = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 66)
)
bsnRogueApAutoContained.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnRogueAPDot11MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnClearTrapVariable"))
)
if mibBuilder.loadTexts:
    bsnRogueApAutoContained.setStatus(
        "current"
    )

bsnTrustedApHasInvalidEncryption = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 67)
)
bsnTrustedApHasInvalidEncryption.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnRogueAPDot11MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApEncryptionUsed"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApEncryptionRequired"),
        ("AIRESPACE-WIRELESS-MIB", "bsnClearTrapVariable"))
)
if mibBuilder.loadTexts:
    bsnTrustedApHasInvalidEncryption.setStatus(
        "current"
    )

bsnTrustedApHasInvalidRadioPolicy = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 68)
)
bsnTrustedApHasInvalidRadioPolicy.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnRogueAPDot11MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApRadioPolicyUsed"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApRadioPolicyRequired"),
        ("AIRESPACE-WIRELESS-MIB", "bsnClearTrapVariable"))
)
if mibBuilder.loadTexts:
    bsnTrustedApHasInvalidRadioPolicy.setStatus(
        "current"
    )

bsnNetworkStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 69)
)
bsnNetworkStateChanged.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnNetworkType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnNetworkState"))
)
if mibBuilder.loadTexts:
    bsnNetworkStateChanged.setStatus(
        "current"
    )

bsnSignatureAttackDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 70)
)
bsnSignatureAttackDetected.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSignatureType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSignatureName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSignatureDescription"),
        ("AIRESPACE-WIRELESS-MIB", "bsnClearTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSignatureAttackPreced"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSignatureAttackFrequency"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSignatureAttackChannel"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSignatureAttackerMacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSignatureMacInfo"))
)
if mibBuilder.loadTexts:
    bsnSignatureAttackDetected.setStatus(
        "current"
    )

bsnAPRadioCardTxFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 71)
)
bsnAPRadioCardTxFailure.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnAPRadioCardTxFailure.setStatus(
        "current"
    )

bsnAPRadioCardTxFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 72)
)
bsnAPRadioCardTxFailureClear.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnAPRadioCardTxFailureClear.setStatus(
        "current"
    )

bsnAPRadioCardRxFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 73)
)
bsnAPRadioCardRxFailure.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnAPRadioCardRxFailure.setStatus(
        "current"
    )

bsnAPRadioCardRxFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 74)
)
bsnAPRadioCardRxFailureClear.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnAPRadioCardRxFailureClear.setStatus(
        "current"
    )

bsnAPImpersonationDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 75)
)
bsnAPImpersonationDetected.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnImpersonatedAPMacAddr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnImpersonatingSourceMacAddr"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnAPImpersonationDetected.setStatus(
        "current"
    )

bsnTrustedApHasInvalidPreamble = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 76)
)
bsnTrustedApHasInvalidPreamble.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnRogueAPDot11MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApPreambleUsed"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApPreambleRequired"),
        ("AIRESPACE-WIRELESS-MIB", "bsnClearTrapVariable"))
)
if mibBuilder.loadTexts:
    bsnTrustedApHasInvalidPreamble.setStatus(
        "current"
    )

bsnAPIPAddressFallback = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 77)
)
bsnAPIPAddressFallback.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnApIpAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPStaticIPAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnAPIPAddressFallback.setStatus(
        "current"
    )

bsnAPFunctionalityDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 78)
)
bsnAPFunctionalityDisabled.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnApFunctionalityDisableReasonCode"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLicenseKeyTrapVariable"),
        ("AIRESPACE-WIRELESS-MIB", "bsnLicenseKeyFeatureSetTrapVariable"))
)
if mibBuilder.loadTexts:
    bsnAPFunctionalityDisabled.setStatus(
        "current"
    )

bsnAPRegulatoryDomainMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 79)
)
bsnAPRegulatoryDomainMismatch.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnApRegulatoryDomain"),
        ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11CountryIndex"))
)
if mibBuilder.loadTexts:
    bsnAPRegulatoryDomainMismatch.setStatus(
        "deprecated"
    )

bsnRxMulticastQueueFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 80)
)
if mibBuilder.loadTexts:
    bsnRxMulticastQueueFull.setStatus(
        "current"
    )

bsnRadarChannelDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 81)
)
bsnRadarChannelDetected.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfPhyChannelNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnRadarChannelDetected.setStatus(
        "current"
    )

bsnRadarChannelCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 82)
)
bsnRadarChannelCleared.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfPhyChannelNumber"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    bsnRadarChannelCleared.setStatus(
        "current"
    )

bsnAPAuthorizationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 83)
)
bsnAPAuthorizationFailure.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPAuthCertificateType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPAuthorizationFailureCause"))
)
if mibBuilder.loadTexts:
    bsnAPAuthorizationFailure.setStatus(
        "current"
    )

radioCoreDumpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 84)
)
radioCoreDumpTrap.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    radioCoreDumpTrap.setStatus(
        "current"
    )

invalidRadioTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 85)
)
invalidRadioTrap.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfSlotId"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPInvalidRadioType"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    invalidRadioTrap.setStatus(
        "current"
    )

countryChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 86)
)
countryChangeTrap.setObjects(
    ("AIRESPACE-WIRELESS-MIB", "bsnGlobalDot11CountryIndex")
)
if mibBuilder.loadTexts:
    countryChangeTrap.setStatus(
        "deprecated"
    )

unsupportedAPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 87)
)
unsupportedAPTrap.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPDot3MacAddress"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPName"))
)
if mibBuilder.loadTexts:
    unsupportedAPTrap.setStatus(
        "current"
    )

heartbeatLossTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 88)
)
if mibBuilder.loadTexts:
    heartbeatLossTrap.setStatus(
        "current"
    )

locationNotifyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 2, 6, 3, 89)
)
locationNotifyTrap.setObjects(
    ("AIRESPACE-WIRELESS-MIB", "locationNotifyContent")
)
if mibBuilder.loadTexts:
    locationNotifyTrap.setStatus(
        "current"
    )


# Notifications groups

bsnWrasTrap = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 14179, 2, 50, 12)
)
bsnWrasTrap.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnDot11StationDisassociate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11StationDeauthenticate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11StationAuthenticateFail"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11StationAssociateFail"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11StationBlacklisted"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11StationAssociate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPUp"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPDown"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPAssociated"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPDisassociated"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfUp"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIfDown"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPLoadProfileFailed"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPNoiseProfileFailed"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPInterferenceProfileFailed"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPCoverageProfileFailed"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPLoadProfileUpdatedToPass"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPNoiseProfileUpdatedToPass"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPInterferenceProfileUpdatedToPass"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPCoverageProfileUpdatedToPass"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPCurrentTxPowerChanged"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPCurrentChannelChanged"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11aGroupingDone"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11bGroupingDone"),
        ("AIRESPACE-WIRELESS-MIB", "bsnConfigSaved"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssCreated"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssDeleted"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRADIUSServerNotResponding"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAuthenticationFailure"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIpsecEspAuthFailureTrap"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIpsecEspReplayFailureTrap"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIpsecEspInvalidSpiTrap"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIpsecIkeNegFailure"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIpsecSuiteNegFailure"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIpsecInvalidCookieTrap"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPDetected"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPRemoved"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPDetectedOnWiredNetwork"),
        ("AIRESPACE-WIRELESS-MIB", "bsnApHasNoRadioCards"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDuplicateIpAddressReported"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPContainedAsARogue"),
        ("AIRESPACE-WIRELESS-MIB", "bsnNetworkStateChanged"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSignatureAttackDetected"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPRadioCardTxFailure"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPRadioCardTxFailureClear"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPRadioCardRxFailure"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPRadioCardRxFailureClear"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPImpersonationDetected"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPRegulatoryDomainMismatch"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApHasInvalidPreamble"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiosExceedLicenseCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSensedTemperatureTooHigh"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSensedTemperatureTooLow"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTemperatureSensorFailure"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTemperatureSensorClear"),
        ("AIRESPACE-WIRELESS-MIB", "bsnPOEControllerFailure"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMaxRogueCountExceeded"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMaxRogueCountClear"),
        ("AIRESPACE-WIRELESS-MIB", "bsnApMaxRogueCountExceeded"),
        ("AIRESPACE-WIRELESS-MIB", "bsnApMaxRogueCountClear"),
        ("AIRESPACE-WIRELESS-MIB", "bsnApBigNavDosAttack"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTooManyUnsuccessLoginAttempts"),
        ("AIRESPACE-WIRELESS-MIB", "bsnWepKeyDecryptError"),
        ("AIRESPACE-WIRELESS-MIB", "bsnWpaMicErrorCounterActivated"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAdhocRogueAutoContained"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueApAutoContained"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApHasInvalidEncryption"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApHasInvalidRadioPolicy"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApHasInvalidSsid"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApIsMissing"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIPAddressFallback"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPFunctionalityDisabled"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRxMulticastQueueFull"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadarChannelDetected"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadarChannelCleared"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPAuthorizationFailure"),
        ("AIRESPACE-WIRELESS-MIB", "radioCoreDumpTrap"),
        ("AIRESPACE-WIRELESS-MIB", "invalidRadioTrap"),
        ("AIRESPACE-WIRELESS-MIB", "countryChangeTrap"),
        ("AIRESPACE-WIRELESS-MIB", "unsupportedAPTrap"),
        ("AIRESPACE-WIRELESS-MIB", "heartbeatLossTrap"),
        ("AIRESPACE-WIRELESS-MIB", "locationNotifyTrap"))
)
if mibBuilder.loadTexts:
    bsnWrasTrap.setStatus(
        "obsolete"
    )

bsnWrasTrapRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 14179, 2, 50, 17)
)
bsnWrasTrapRev1.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnDot11StationDisassociate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11StationDeauthenticate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11StationAuthenticateFail"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11StationAssociateFail"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11StationBlacklisted"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11StationAssociate"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPDisassociated"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPLoadProfileFailed"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPNoiseProfileFailed"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPInterferenceProfileFailed"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPCoverageProfileFailed"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPLoadProfileUpdatedToPass"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPNoiseProfileUpdatedToPass"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPInterferenceProfileUpdatedToPass"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPCoverageProfileUpdatedToPass"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPCurrentTxPowerChanged"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPCurrentChannelChanged"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11aGroupingDone"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRrmDot11bGroupingDone"),
        ("AIRESPACE-WIRELESS-MIB", "bsnConfigSaved"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssCreated"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDot11EssDeleted"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRADIUSServerNotResponding"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAuthenticationFailure"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIpsecEspAuthFailureTrap"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIpsecEspReplayFailureTrap"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIpsecEspInvalidSpiTrap"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIpsecIkeNegFailure"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIpsecSuiteNegFailure"),
        ("AIRESPACE-WIRELESS-MIB", "bsnIpsecInvalidCookieTrap"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPDetected"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPRemoved"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueAPDetectedOnWiredNetwork"),
        ("AIRESPACE-WIRELESS-MIB", "bsnApHasNoRadioCards"),
        ("AIRESPACE-WIRELESS-MIB", "bsnDuplicateIpAddressReported"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPContainedAsARogue"),
        ("AIRESPACE-WIRELESS-MIB", "bsnNetworkStateChanged"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSignatureAttackDetected"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPRadioCardTxFailure"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPRadioCardTxFailureClear"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPRadioCardRxFailure"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPRadioCardRxFailureClear"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPImpersonationDetected"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApHasInvalidPreamble"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadiosExceedLicenseCount"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSensedTemperatureTooHigh"),
        ("AIRESPACE-WIRELESS-MIB", "bsnSensedTemperatureTooLow"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTemperatureSensorFailure"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTemperatureSensorClear"),
        ("AIRESPACE-WIRELESS-MIB", "bsnPOEControllerFailure"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMaxRogueCountExceeded"),
        ("AIRESPACE-WIRELESS-MIB", "bsnMaxRogueCountClear"),
        ("AIRESPACE-WIRELESS-MIB", "bsnApMaxRogueCountExceeded"),
        ("AIRESPACE-WIRELESS-MIB", "bsnApMaxRogueCountClear"),
        ("AIRESPACE-WIRELESS-MIB", "bsnApBigNavDosAttack"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTooManyUnsuccessLoginAttempts"),
        ("AIRESPACE-WIRELESS-MIB", "bsnWepKeyDecryptError"),
        ("AIRESPACE-WIRELESS-MIB", "bsnWpaMicErrorCounterActivated"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAdhocRogueAutoContained"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRogueApAutoContained"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApHasInvalidEncryption"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApHasInvalidRadioPolicy"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApHasInvalidSsid"),
        ("AIRESPACE-WIRELESS-MIB", "bsnTrustedApIsMissing"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPIPAddressFallback"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPFunctionalityDisabled"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRxMulticastQueueFull"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadarChannelDetected"),
        ("AIRESPACE-WIRELESS-MIB", "bsnRadarChannelCleared"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPAuthorizationFailure"),
        ("AIRESPACE-WIRELESS-MIB", "radioCoreDumpTrap"),
        ("AIRESPACE-WIRELESS-MIB", "invalidRadioTrap"),
        ("AIRESPACE-WIRELESS-MIB", "unsupportedAPTrap"),
        ("AIRESPACE-WIRELESS-MIB", "heartbeatLossTrap"),
        ("AIRESPACE-WIRELESS-MIB", "locationNotifyTrap"))
)
if mibBuilder.loadTexts:
    bsnWrasTrapRev1.setStatus(
        "current"
    )

bsnWrasObsTrap = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 14179, 2, 50, 21)
)
bsnWrasObsTrap.setObjects(
      *(("AIRESPACE-WIRELESS-MIB", "bsnAPUp"),
        ("AIRESPACE-WIRELESS-MIB", "bsnAPDown"))
)
if mibBuilder.loadTexts:
    bsnWrasObsTrap.setStatus(
        "obsolete"
    )


# Agent capabilities


# Module compliance

bsnWrasCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14179, 2, 51, 1)
)
if mibBuilder.loadTexts:
    bsnWrasCompliance.setStatus(
        "deprecated"
    )

bsnWrasComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14179, 2, 51, 2)
)
if mibBuilder.loadTexts:
    bsnWrasComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AIRESPACE-WIRELESS-MIB",
    **{"WEPKeytype": WEPKeytype,
       "ProfileState": ProfileState,
       "BsnTxtSignatureMacInfo": BsnTxtSignatureMacInfo,
       "BsnSignaturePatternOffSetStart": BsnSignaturePatternOffSetStart,
       "bsnWireless": bsnWireless,
       "bsnEss": bsnEss,
       "bsnDot11EssTable": bsnDot11EssTable,
       "bsnDot11EssEntry": bsnDot11EssEntry,
       "bsnDot11EssIndex": bsnDot11EssIndex,
       "bsnDot11EssSsid": bsnDot11EssSsid,
       "bsnDot11EssSessionTimeout": bsnDot11EssSessionTimeout,
       "bsnDot11EssMacFiltering": bsnDot11EssMacFiltering,
       "bsnDot11EssAdminStatus": bsnDot11EssAdminStatus,
       "bsnDot11EssSecurityAuthType": bsnDot11EssSecurityAuthType,
       "bsnDot11EssStaticWEPSecurity": bsnDot11EssStaticWEPSecurity,
       "bsnDot11EssStaticWEPEncryptionType": bsnDot11EssStaticWEPEncryptionType,
       "bsnDot11EssStaticWEPDefaultKey": bsnDot11EssStaticWEPDefaultKey,
       "bsnDot11EssStaticWEPKeyIndex": bsnDot11EssStaticWEPKeyIndex,
       "bsnDot11EssStaticWEPKeyFormat": bsnDot11EssStaticWEPKeyFormat,
       "bsnDot11Ess8021xSecurity": bsnDot11Ess8021xSecurity,
       "bsnDot11Ess8021xEncryptionType": bsnDot11Ess8021xEncryptionType,
       "bsnDot11EssWPASecurity": bsnDot11EssWPASecurity,
       "bsnDot11EssWPAEncryptionType": bsnDot11EssWPAEncryptionType,
       "bsnDot11EssIpsecSecurity": bsnDot11EssIpsecSecurity,
       "bsnDot11EssVpnEncrTransform": bsnDot11EssVpnEncrTransform,
       "bsnDot11EssVpnAuthTransform": bsnDot11EssVpnAuthTransform,
       "bsnDot11EssVpnIkeAuthMode": bsnDot11EssVpnIkeAuthMode,
       "bsnDot11EssVpnSharedKey": bsnDot11EssVpnSharedKey,
       "bsnDot11EssVpnSharedKeySize": bsnDot11EssVpnSharedKeySize,
       "bsnDot11EssVpnIkePhase1Mode": bsnDot11EssVpnIkePhase1Mode,
       "bsnDot11EssVpnIkeLifetime": bsnDot11EssVpnIkeLifetime,
       "bsnDot11EssVpnIkeDHGroup": bsnDot11EssVpnIkeDHGroup,
       "bsnDot11EssIpsecPassthruSecurity": bsnDot11EssIpsecPassthruSecurity,
       "bsnDot11EssVpnPassthruGateway": bsnDot11EssVpnPassthruGateway,
       "bsnDot11EssWebSecurity": bsnDot11EssWebSecurity,
       "bsnDot11EssRadioPolicy": bsnDot11EssRadioPolicy,
       "bsnDot11EssQualityOfService": bsnDot11EssQualityOfService,
       "bsnDot11EssDhcpRequired": bsnDot11EssDhcpRequired,
       "bsnDot11EssDhcpServerIpAddress": bsnDot11EssDhcpServerIpAddress,
       "bsnDot11EssVpnContivityMode": bsnDot11EssVpnContivityMode,
       "bsnDot11EssVpnQotdServerAddress": bsnDot11EssVpnQotdServerAddress,
       "bsnDot11EssBlacklistTimeout": bsnDot11EssBlacklistTimeout,
       "bsnDot11EssNumberOfMobileStations": bsnDot11EssNumberOfMobileStations,
       "bsnDot11EssWebPassthru": bsnDot11EssWebPassthru,
       "bsnDot11EssCraniteSecurity": bsnDot11EssCraniteSecurity,
       "bsnDot11EssBlacklistingCapability": bsnDot11EssBlacklistingCapability,
       "bsnDot11EssInterfaceName": bsnDot11EssInterfaceName,
       "bsnDot11EssAclName": bsnDot11EssAclName,
       "bsnDot11EssAAAOverride": bsnDot11EssAAAOverride,
       "bsnDot11EssWPAAuthKeyMgmtMode": bsnDot11EssWPAAuthKeyMgmtMode,
       "bsnDot11EssWPAAuthPresharedKey": bsnDot11EssWPAAuthPresharedKey,
       "bsnDot11EssFortressSecurity": bsnDot11EssFortressSecurity,
       "bsnDot11EssWepAllowSharedKeyAuth": bsnDot11EssWepAllowSharedKeyAuth,
       "bsnDot11EssL2tpSecurity": bsnDot11EssL2tpSecurity,
       "bsnDot11EssWPAAuthPresharedKeyHex": bsnDot11EssWPAAuthPresharedKeyHex,
       "bsnDot11EssBroadcastSsid": bsnDot11EssBroadcastSsid,
       "bsnDot11EssExternalPolicyValidation": bsnDot11EssExternalPolicyValidation,
       "bsnDot11EssRSNSecurity": bsnDot11EssRSNSecurity,
       "bsnDot11EssRSNWPACompatibilityMode": bsnDot11EssRSNWPACompatibilityMode,
       "bsnDot11EssRSNAllowTKIPClients": bsnDot11EssRSNAllowTKIPClients,
       "bsnDot11EssRSNAuthKeyMgmtMode": bsnDot11EssRSNAuthKeyMgmtMode,
       "bsnDot11EssRSNAuthPresharedKey": bsnDot11EssRSNAuthPresharedKey,
       "bsnDot11EssRSNAuthPresharedKeyHex": bsnDot11EssRSNAuthPresharedKeyHex,
       "bsnDot11EssIPv6Bridging": bsnDot11EssIPv6Bridging,
       "bsnDot11EssRowStatus": bsnDot11EssRowStatus,
       "bsnDot11EssWmePolicySetting": bsnDot11EssWmePolicySetting,
       "bsnDot11Ess80211ePolicySetting": bsnDot11Ess80211ePolicySetting,
       "bsnDot11EssWebPassthroughEmail": bsnDot11EssWebPassthroughEmail,
       "bsnDot11Ess7920PhoneSupport": bsnDot11Ess7920PhoneSupport,
       "bsnDot11EssRadiusAuthPrimaryServer": bsnDot11EssRadiusAuthPrimaryServer,
       "bsnDot11EssRadiusAuthSecondaryServer": bsnDot11EssRadiusAuthSecondaryServer,
       "bsnDot11EssRadiusAuthTertiaryServer": bsnDot11EssRadiusAuthTertiaryServer,
       "bsnDot11EssRadiusAcctPrimaryServer": bsnDot11EssRadiusAcctPrimaryServer,
       "bsnDot11EssRadiusAcctSecondaryServer": bsnDot11EssRadiusAcctSecondaryServer,
       "bsnDot11EssRadiusAcctTertiaryServer": bsnDot11EssRadiusAcctTertiaryServer,
       "bsnMobileStationTable": bsnMobileStationTable,
       "bsnMobileStationEntry": bsnMobileStationEntry,
       "bsnMobileStationMacAddress": bsnMobileStationMacAddress,
       "bsnMobileStationIpAddress": bsnMobileStationIpAddress,
       "bsnMobileStationUserName": bsnMobileStationUserName,
       "bsnMobileStationAPMacAddr": bsnMobileStationAPMacAddr,
       "bsnMobileStationAPIfSlotId": bsnMobileStationAPIfSlotId,
       "bsnMobileStationEssIndex": bsnMobileStationEssIndex,
       "bsnMobileStationSsid": bsnMobileStationSsid,
       "bsnMobileStationAID": bsnMobileStationAID,
       "bsnMobileStationStatus": bsnMobileStationStatus,
       "bsnMobileStationReasonCode": bsnMobileStationReasonCode,
       "bsnMobileStationMobilityStatus": bsnMobileStationMobilityStatus,
       "bsnMobileStationAnchorAddress": bsnMobileStationAnchorAddress,
       "bsnMobileStationCFPollable": bsnMobileStationCFPollable,
       "bsnMobileStationCFPollRequest": bsnMobileStationCFPollRequest,
       "bsnMobileStationChannelAgilityEnabled": bsnMobileStationChannelAgilityEnabled,
       "bsnMobileStationPBCCOptionImplemented": bsnMobileStationPBCCOptionImplemented,
       "bsnMobileStationShortPreambleOptionImplemented": bsnMobileStationShortPreambleOptionImplemented,
       "bsnMobileStationSessionTimeout": bsnMobileStationSessionTimeout,
       "bsnMobileStationAuthenticationAlgorithm": bsnMobileStationAuthenticationAlgorithm,
       "bsnMobileStationWepState": bsnMobileStationWepState,
       "bsnMobileStationPortNumber": bsnMobileStationPortNumber,
       "bsnMobileStationDeleteAction": bsnMobileStationDeleteAction,
       "bsnMobileStationPolicyManagerState": bsnMobileStationPolicyManagerState,
       "bsnMobileStationSecurityPolicyStatus": bsnMobileStationSecurityPolicyStatus,
       "bsnMobileStationProtocol": bsnMobileStationProtocol,
       "bsnMobileStationMirrorMode": bsnMobileStationMirrorMode,
       "bsnMobileStationInterface": bsnMobileStationInterface,
       "bsnMobileStationApMode": bsnMobileStationApMode,
       "bsnMobileStationVlanId": bsnMobileStationVlanId,
       "bsnMobileStationPolicyType": bsnMobileStationPolicyType,
       "bsnMobileStationEncryptionCypher": bsnMobileStationEncryptionCypher,
       "bsnMobileStationEapType": bsnMobileStationEapType,
       "bsnMobileStationCcxVersion": bsnMobileStationCcxVersion,
       "bsnMobileStationE2eVersion": bsnMobileStationE2eVersion,
       "bsnMobileStationStatusCode": bsnMobileStationStatusCode,
       "bsnMobileStationPerRadioPerVapTable": bsnMobileStationPerRadioPerVapTable,
       "bsnMobileStationPerRadioPerVapEntry": bsnMobileStationPerRadioPerVapEntry,
       "bsnMobileStationPerRadioPerVapIndex": bsnMobileStationPerRadioPerVapIndex,
       "bsnMobileStationMacAddr": bsnMobileStationMacAddr,
       "bsnMobileStationStatsTable": bsnMobileStationStatsTable,
       "bsnMobileStationStatsEntry": bsnMobileStationStatsEntry,
       "bsnMobileStationRSSI": bsnMobileStationRSSI,
       "bsnMobileStationBytesReceived": bsnMobileStationBytesReceived,
       "bsnMobileStationBytesSent": bsnMobileStationBytesSent,
       "bsnMobileStationPolicyErrors": bsnMobileStationPolicyErrors,
       "bsnMobileStationPacketsReceived": bsnMobileStationPacketsReceived,
       "bsnMobileStationPacketsSent": bsnMobileStationPacketsSent,
       "bsnMobileStationSnr": bsnMobileStationSnr,
       "bsnRogueAPTable": bsnRogueAPTable,
       "bsnRogueAPEntry": bsnRogueAPEntry,
       "bsnRogueAPDot11MacAddress": bsnRogueAPDot11MacAddress,
       "bsnRogueAPTotalDetectingAPs": bsnRogueAPTotalDetectingAPs,
       "bsnRogueAPFirstReported": bsnRogueAPFirstReported,
       "bsnRogueAPLastReported": bsnRogueAPLastReported,
       "bsnRogueAPContainmentLevel": bsnRogueAPContainmentLevel,
       "bsnRogueAPType": bsnRogueAPType,
       "bsnRogueAPOnNetwork": bsnRogueAPOnNetwork,
       "bsnRogueAPTotalClients": bsnRogueAPTotalClients,
       "bsnRogueAPRowStatus": bsnRogueAPRowStatus,
       "bsnRogueAPMaxDetectedRSSI": bsnRogueAPMaxDetectedRSSI,
       "bsnRogueAPSSID": bsnRogueAPSSID,
       "bsnRogueAPDetectingAPRadioType": bsnRogueAPDetectingAPRadioType,
       "bsnRogueAPDetectingAPMacAddress": bsnRogueAPDetectingAPMacAddress,
       "bsnRogueAPMaxRssiRadioType": bsnRogueAPMaxRssiRadioType,
       "bsnRogueAPState": bsnRogueAPState,
       "bsnRogueAPClassType": bsnRogueAPClassType,
       "bsnRogueAPChannel": bsnRogueAPChannel,
       "bsnRogueAPDetectingAPName": bsnRogueAPDetectingAPName,
       "bsnRogueAPAirespaceAPTable": bsnRogueAPAirespaceAPTable,
       "bsnRogueAPAirespaceAPEntry": bsnRogueAPAirespaceAPEntry,
       "bsnRogueAPAirespaceAPMacAddress": bsnRogueAPAirespaceAPMacAddress,
       "bsnRogueAPAirespaceAPSlotId": bsnRogueAPAirespaceAPSlotId,
       "bsnRogueAPRadioType": bsnRogueAPRadioType,
       "bsnRogueAPAirespaceAPName": bsnRogueAPAirespaceAPName,
       "bsnRogueAPChannelNumber": bsnRogueAPChannelNumber,
       "bsnRogueAPSsid": bsnRogueAPSsid,
       "bsnRogueAPAirespaceAPRSSI": bsnRogueAPAirespaceAPRSSI,
       "bsnRogueAPContainmentMode": bsnRogueAPContainmentMode,
       "bsnRogueAPContainmentChannelCount": bsnRogueAPContainmentChannelCount,
       "bsnRogueAPContainmentChannels": bsnRogueAPContainmentChannels,
       "bsnRogueAPAirespaceAPLastHeard": bsnRogueAPAirespaceAPLastHeard,
       "bsnRogueAPAirespaceAPWepMode": bsnRogueAPAirespaceAPWepMode,
       "bsnRogueAPAirespaceAPPreamble": bsnRogueAPAirespaceAPPreamble,
       "bsnRogueAPAirespaceAPWpaMode": bsnRogueAPAirespaceAPWpaMode,
       "bsnRogueAPAirespaceAPSNR": bsnRogueAPAirespaceAPSNR,
       "bsnRogueAPChannelWidth": bsnRogueAPChannelWidth,
       "bsnThirdPartyAPTable": bsnThirdPartyAPTable,
       "bsnThirdPartyAPEntry": bsnThirdPartyAPEntry,
       "bsnThirdPartyAPMacAddress": bsnThirdPartyAPMacAddress,
       "bsnThirdPartyAPInterface": bsnThirdPartyAPInterface,
       "bsnThirdPartyAPIpAddress": bsnThirdPartyAPIpAddress,
       "bsnThirdPartyAP802Dot1XRequired": bsnThirdPartyAP802Dot1XRequired,
       "bsnThirdPartyAPMirrorMode": bsnThirdPartyAPMirrorMode,
       "bsnThirdPartyAPRowStatus": bsnThirdPartyAPRowStatus,
       "bsnMobileStationByIpTable": bsnMobileStationByIpTable,
       "bsnMobileStationByIpEntry": bsnMobileStationByIpEntry,
       "bsnMobileStationByIpAddress": bsnMobileStationByIpAddress,
       "bsnMobileStationByIpMacAddress": bsnMobileStationByIpMacAddress,
       "bsnMobileStationRssiDataTable": bsnMobileStationRssiDataTable,
       "bsnMobileStationRssiDataEntry": bsnMobileStationRssiDataEntry,
       "bsnMobileStationRssiDataApMacAddress": bsnMobileStationRssiDataApMacAddress,
       "bsnMobileStationRssiDataApIfSlotId": bsnMobileStationRssiDataApIfSlotId,
       "bsnMobileStationRssiDataApIfType": bsnMobileStationRssiDataApIfType,
       "bsnMobileStationRssiDataApName": bsnMobileStationRssiDataApName,
       "bsnMobileStationRssiData": bsnMobileStationRssiData,
       "bsnAPIfPhyAntennaIndex": bsnAPIfPhyAntennaIndex,
       "bsnMobileStationRssiDataLastHeard": bsnMobileStationRssiDataLastHeard,
       "bsnWatchListClientTable": bsnWatchListClientTable,
       "bsnWatchListClientEntry": bsnWatchListClientEntry,
       "bsnWatchListClientKey": bsnWatchListClientKey,
       "bsnWatchListClientType": bsnWatchListClientType,
       "bsnWatchListClientRowStatus": bsnWatchListClientRowStatus,
       "bsnMobileStationByUsernameTable": bsnMobileStationByUsernameTable,
       "bsnMobileStationByUsernameEntry": bsnMobileStationByUsernameEntry,
       "bsnMobileStationByUserName": bsnMobileStationByUserName,
       "bsnMobileStationByUserMacAddress": bsnMobileStationByUserMacAddress,
       "bsnRogueClientTable": bsnRogueClientTable,
       "bsnRogueClientEntry": bsnRogueClientEntry,
       "bsnRogueClientDot11MacAddress": bsnRogueClientDot11MacAddress,
       "bsnRogueClientTotalDetectingAPs": bsnRogueClientTotalDetectingAPs,
       "bsnRogueClientFirstReported": bsnRogueClientFirstReported,
       "bsnRogueClientLastReported": bsnRogueClientLastReported,
       "bsnRogueClientBSSID": bsnRogueClientBSSID,
       "bsnRogueClientContainmentLevel": bsnRogueClientContainmentLevel,
       "bsnRogueClientLastHeard": bsnRogueClientLastHeard,
       "bsnRogueClientState": bsnRogueClientState,
       "bsnRogueClientAirespaceAPTable": bsnRogueClientAirespaceAPTable,
       "bsnRogueClientAirespaceAPEntry": bsnRogueClientAirespaceAPEntry,
       "bsnRogueClientAirespaceAPMacAddress": bsnRogueClientAirespaceAPMacAddress,
       "bsnRogueClientAirespaceAPSlotId": bsnRogueClientAirespaceAPSlotId,
       "bsnRogueClientRadioType": bsnRogueClientRadioType,
       "bsnRogueClientAirespaceAPName": bsnRogueClientAirespaceAPName,
       "bsnRogueClientChannelNumber": bsnRogueClientChannelNumber,
       "bsnRogueClientAirespaceAPRSSI": bsnRogueClientAirespaceAPRSSI,
       "bsnRogueClientAirespaceAPLastHeard": bsnRogueClientAirespaceAPLastHeard,
       "bsnRogueClientAirespaceAPSNR": bsnRogueClientAirespaceAPSNR,
       "bsnRogueClientPerRogueAPTable": bsnRogueClientPerRogueAPTable,
       "bsnRogueClientPerRogueAPEntry": bsnRogueClientPerRogueAPEntry,
       "bsnRogueAPDot11MacAddr": bsnRogueAPDot11MacAddr,
       "bsnRogueClientDot11MacAddr": bsnRogueClientDot11MacAddr,
       "bsnDot11QosProfileTable": bsnDot11QosProfileTable,
       "bsnDot11QosProfileEntry": bsnDot11QosProfileEntry,
       "bsnDot11QosProfileName": bsnDot11QosProfileName,
       "bsnDot11QosProfileDesc": bsnDot11QosProfileDesc,
       "bsnDot11QosAverageDataRate": bsnDot11QosAverageDataRate,
       "bsnDot11QosBurstDataRate": bsnDot11QosBurstDataRate,
       "bsnDot11QosAvgRealTimeDataRate": bsnDot11QosAvgRealTimeDataRate,
       "bsnDot11QosBurstRealTimeDataRate": bsnDot11QosBurstRealTimeDataRate,
       "bsnDot11QosMaxRFUsagePerAP": bsnDot11QosMaxRFUsagePerAP,
       "bsnDot11QosProfileQueueDepth": bsnDot11QosProfileQueueDepth,
       "bsnDot11WiredQosProtocol": bsnDot11WiredQosProtocol,
       "bsnDot11802Dot1PTag": bsnDot11802Dot1PTag,
       "bsnDot11ResetProfileToDefault": bsnDot11ResetProfileToDefault,
       "bsnTagTable": bsnTagTable,
       "bsnTagEntry": bsnTagEntry,
       "bsnTagDot11MacAddress": bsnTagDot11MacAddress,
       "bsnTagType": bsnTagType,
       "bsnTagTimeInterval": bsnTagTimeInterval,
       "bsnTagBatteryStatus": bsnTagBatteryStatus,
       "bsnTagLastReported": bsnTagLastReported,
       "bsnTagRssiDataTable": bsnTagRssiDataTable,
       "bsnTagRssiDataEntry": bsnTagRssiDataEntry,
       "bsnTagRssiDataApMacAddress": bsnTagRssiDataApMacAddress,
       "bsnTagRssiDataApIfSlotId": bsnTagRssiDataApIfSlotId,
       "bsnTagRssiDataApIfType": bsnTagRssiDataApIfType,
       "bsnTagRssiDataApName": bsnTagRssiDataApName,
       "bsnTagRssiDataLastHeard": bsnTagRssiDataLastHeard,
       "bsnTagRssiData": bsnTagRssiData,
       "bsnTagRssiDataSnr": bsnTagRssiDataSnr,
       "bsnTagStatsTable": bsnTagStatsTable,
       "bsnTagStatsEntry": bsnTagStatsEntry,
       "bsnTagBytesReceived": bsnTagBytesReceived,
       "bsnTagPacketsReceived": bsnTagPacketsReceived,
       "bsnMobileStationExtStatsTable": bsnMobileStationExtStatsTable,
       "bsnMobileStationExtStatsEntry": bsnMobileStationExtStatsEntry,
       "bsnMobileStationSampleTime": bsnMobileStationSampleTime,
       "bsnMobileStationTxExcessiveRetries": bsnMobileStationTxExcessiveRetries,
       "bsnMobileStationTxRetries": bsnMobileStationTxRetries,
       "bsnMobileStationTxFiltered": bsnMobileStationTxFiltered,
       "bsnAP": bsnAP,
       "bsnAPTable": bsnAPTable,
       "bsnAPEntry": bsnAPEntry,
       "bsnAPDot3MacAddress": bsnAPDot3MacAddress,
       "bsnAPNumOfSlots": bsnAPNumOfSlots,
       "bsnAPName": bsnAPName,
       "bsnAPLocation": bsnAPLocation,
       "bsnAPMonitorOnlyMode": bsnAPMonitorOnlyMode,
       "bsnAPOperationStatus": bsnAPOperationStatus,
       "bsnAPSoftwareVersion": bsnAPSoftwareVersion,
       "bsnAPBootVersion": bsnAPBootVersion,
       "bsnAPPrimaryMwarName": bsnAPPrimaryMwarName,
       "bsnAPReset": bsnAPReset,
       "bsnAPStatsTimer": bsnAPStatsTimer,
       "bsnAPPortNumber": bsnAPPortNumber,
       "bsnAPModel": bsnAPModel,
       "bsnAPSerialNumber": bsnAPSerialNumber,
       "bsnAPClearConfig": bsnAPClearConfig,
       "bsnApIpAddress": bsnApIpAddress,
       "bsnAPMirrorMode": bsnAPMirrorMode,
       "bsnAPRemoteModeSupport": bsnAPRemoteModeSupport,
       "bsnAPType": bsnAPType,
       "bsnAPSecondaryMwarName": bsnAPSecondaryMwarName,
       "bsnAPTertiaryMwarName": bsnAPTertiaryMwarName,
       "bsnAPIsStaticIP": bsnAPIsStaticIP,
       "bsnAPNetmask": bsnAPNetmask,
       "bsnAPGateway": bsnAPGateway,
       "bsnAPStaticIPAddress": bsnAPStaticIPAddress,
       "bsnAPBridgingSupport": bsnAPBridgingSupport,
       "bsnAPGroupVlanName": bsnAPGroupVlanName,
       "bsnAPIOSVersion": bsnAPIOSVersion,
       "bsnAPCertificateType": bsnAPCertificateType,
       "bsnAPEthernetMacAddress": bsnAPEthernetMacAddress,
       "bsnAPAdminStatus": bsnAPAdminStatus,
       "bsnAPIfTable": bsnAPIfTable,
       "bsnAPIfEntry": bsnAPIfEntry,
       "bsnAPIfSlotId": bsnAPIfSlotId,
       "bsnAPIfType": bsnAPIfType,
       "bsnAPIfPhyChannelAssignment": bsnAPIfPhyChannelAssignment,
       "bsnAPIfPhyChannelNumber": bsnAPIfPhyChannelNumber,
       "bsnAPIfPhyTxPowerControl": bsnAPIfPhyTxPowerControl,
       "bsnAPIfPhyTxPowerLevel": bsnAPIfPhyTxPowerLevel,
       "bsnAPIfPhyAntennaMode": bsnAPIfPhyAntennaMode,
       "bsnAPIfPhyAntennaType": bsnAPIfPhyAntennaType,
       "bsnAPIfPhyAntennaDiversity": bsnAPIfPhyAntennaDiversity,
       "bsnAPIfCellSiteConfigId": bsnAPIfCellSiteConfigId,
       "bsnAPIfNumberOfVaps": bsnAPIfNumberOfVaps,
       "bsnAPIfOperStatus": bsnAPIfOperStatus,
       "bsnAPIfPortNumber": bsnAPIfPortNumber,
       "bsnAPIfPhyAntennaOptions": bsnAPIfPhyAntennaOptions,
       "bsnApIfNoOfUsers": bsnApIfNoOfUsers,
       "bsnAPIfWlanOverride": bsnAPIfWlanOverride,
       "bsnAPIfPacketsSniffingFeature": bsnAPIfPacketsSniffingFeature,
       "bsnAPIfSniffChannel": bsnAPIfSniffChannel,
       "bsnAPIfSniffServerIPAddress": bsnAPIfSniffServerIPAddress,
       "bsnAPIfAntennaGain": bsnAPIfAntennaGain,
       "bsnAPIfChannelList": bsnAPIfChannelList,
       "bsnAPIfAbsolutePowerList": bsnAPIfAbsolutePowerList,
       "bsnAPIfRegulatoryDomainSupport": bsnAPIfRegulatoryDomainSupport,
       "bsnAPIfAdminStatus": bsnAPIfAdminStatus,
       "bsnAPIfSmtParamTable": bsnAPIfSmtParamTable,
       "bsnAPIfSmtParamEntry": bsnAPIfSmtParamEntry,
       "bsnAPIfDot11BeaconPeriod": bsnAPIfDot11BeaconPeriod,
       "bsnAPIfDot11MediumOccupancyLimit": bsnAPIfDot11MediumOccupancyLimit,
       "bsnAPIfDot11CFPPeriod": bsnAPIfDot11CFPPeriod,
       "bsnAPIfDot11CFPMaxDuration": bsnAPIfDot11CFPMaxDuration,
       "bsnAPIfDot11OperationalRateSet": bsnAPIfDot11OperationalRateSet,
       "bsnAPIfDot11DTIMPeriod": bsnAPIfDot11DTIMPeriod,
       "bsnAPIfDot11MultiDomainCapabilityImplemented": bsnAPIfDot11MultiDomainCapabilityImplemented,
       "bsnAPIfDot11MultiDomainCapabilityEnabled": bsnAPIfDot11MultiDomainCapabilityEnabled,
       "bsnAPIfDot11CountryString": bsnAPIfDot11CountryString,
       "bsnAPIfDot11SmtParamsConfigType": bsnAPIfDot11SmtParamsConfigType,
       "bsnAPIfDot11BSSID": bsnAPIfDot11BSSID,
       "bsnAPIfMultiDomainCapabilityTable": bsnAPIfMultiDomainCapabilityTable,
       "bsnAPIfMultiDomainCapabilityEntry": bsnAPIfMultiDomainCapabilityEntry,
       "bsnAPIfDot11MaximumTransmitPowerLevel": bsnAPIfDot11MaximumTransmitPowerLevel,
       "bsnAPIfDot11FirstChannelNumber": bsnAPIfDot11FirstChannelNumber,
       "bsnAPIfDot11NumberofChannels": bsnAPIfDot11NumberofChannels,
       "bsnAPIfMacOperationParamTable": bsnAPIfMacOperationParamTable,
       "bsnAPIfMacOperationParamEntry": bsnAPIfMacOperationParamEntry,
       "bsnAPIfDot11MacRTSThreshold": bsnAPIfDot11MacRTSThreshold,
       "bsnAPIfDot11MacShortRetryLimit": bsnAPIfDot11MacShortRetryLimit,
       "bsnAPIfDot11MacLongRetryLimit": bsnAPIfDot11MacLongRetryLimit,
       "bsnAPIfDot11MacFragmentationThreshold": bsnAPIfDot11MacFragmentationThreshold,
       "bsnAPIfDot11MacMaxTransmitMSDULifetime": bsnAPIfDot11MacMaxTransmitMSDULifetime,
       "bsnAPIfDot11MacParamsConfigType": bsnAPIfDot11MacParamsConfigType,
       "bsnAPIfDot11MacMaxReceiveLifetime": bsnAPIfDot11MacMaxReceiveLifetime,
       "bsnAPIfDot11CountersTable": bsnAPIfDot11CountersTable,
       "bsnAPIfDot11CountersEntry": bsnAPIfDot11CountersEntry,
       "bsnAPIfDot11TransmittedFragmentCount": bsnAPIfDot11TransmittedFragmentCount,
       "bsnAPIfDot11MulticastTransmittedFrameCount": bsnAPIfDot11MulticastTransmittedFrameCount,
       "bsnAPIfDot11RetryCount": bsnAPIfDot11RetryCount,
       "bsnAPIfDot11MultipleRetryCount": bsnAPIfDot11MultipleRetryCount,
       "bsnAPIfDot11FrameDuplicateCount": bsnAPIfDot11FrameDuplicateCount,
       "bsnAPIfDot11RTSSuccessCount": bsnAPIfDot11RTSSuccessCount,
       "bsnAPIfDot11RTSFailureCount": bsnAPIfDot11RTSFailureCount,
       "bsnAPIfDot11ACKFailureCount": bsnAPIfDot11ACKFailureCount,
       "bsnAPIfDot11ReceivedFragmentCount": bsnAPIfDot11ReceivedFragmentCount,
       "bsnAPIfDot11MulticastReceivedFrameCount": bsnAPIfDot11MulticastReceivedFrameCount,
       "bsnAPIfDot11FCSErrorCount": bsnAPIfDot11FCSErrorCount,
       "bsnAPIfDot11TransmittedFrameCount": bsnAPIfDot11TransmittedFrameCount,
       "bsnAPIfDot11WEPUndecryptableCount": bsnAPIfDot11WEPUndecryptableCount,
       "bsnAPIfDot11FailedCount": bsnAPIfDot11FailedCount,
       "bsnAPIfDot11PhyTxPowerTable": bsnAPIfDot11PhyTxPowerTable,
       "bsnAPIfDot11PhyTxPowerEntry": bsnAPIfDot11PhyTxPowerEntry,
       "bsnAPIfDot11NumberSupportedPowerLevels": bsnAPIfDot11NumberSupportedPowerLevels,
       "bsnAPIfDot11TxPowerLevel1": bsnAPIfDot11TxPowerLevel1,
       "bsnAPIfDot11TxPowerLevel2": bsnAPIfDot11TxPowerLevel2,
       "bsnAPIfDot11TxPowerLevel3": bsnAPIfDot11TxPowerLevel3,
       "bsnAPIfDot11TxPowerLevel4": bsnAPIfDot11TxPowerLevel4,
       "bsnAPIfDot11TxPowerLevel5": bsnAPIfDot11TxPowerLevel5,
       "bsnAPIfDot11TxPowerLevel6": bsnAPIfDot11TxPowerLevel6,
       "bsnAPIfDot11TxPowerLevel7": bsnAPIfDot11TxPowerLevel7,
       "bsnAPIfDot11TxPowerLevel8": bsnAPIfDot11TxPowerLevel8,
       "bsnAPIfDot11PhyChannelTable": bsnAPIfDot11PhyChannelTable,
       "bsnAPIfDot11PhyChannelEntry": bsnAPIfDot11PhyChannelEntry,
       "bsnAPIfDot11CurrentCCAMode": bsnAPIfDot11CurrentCCAMode,
       "bsnAPIfDot11EDThreshold": bsnAPIfDot11EDThreshold,
       "bsnAPIfDot11TIThreshold": bsnAPIfDot11TIThreshold,
       "bsnAPIfProfileThresholdConfigTable": bsnAPIfProfileThresholdConfigTable,
       "bsnAPIfProfileThresholdConfigEntry": bsnAPIfProfileThresholdConfigEntry,
       "bsnAPIfProfileParamAssignment": bsnAPIfProfileParamAssignment,
       "bsnAPIfForeignInterferenceThreshold": bsnAPIfForeignInterferenceThreshold,
       "bsnAPIfForeignNoiseThreshold": bsnAPIfForeignNoiseThreshold,
       "bsnAPIfRFUtilizationThreshold": bsnAPIfRFUtilizationThreshold,
       "bsnAPIfThroughputThreshold": bsnAPIfThroughputThreshold,
       "bsnAPIfMobilesThreshold": bsnAPIfMobilesThreshold,
       "bsnAPIfCoverageThreshold": bsnAPIfCoverageThreshold,
       "bsnAPIfMobileMinExceptionLevel": bsnAPIfMobileMinExceptionLevel,
       "bsnAPIfCoverageExceptionLevel": bsnAPIfCoverageExceptionLevel,
       "bsnAPIfLoadParametersTable": bsnAPIfLoadParametersTable,
       "bsnAPIfLoadParametersEntry": bsnAPIfLoadParametersEntry,
       "bsnAPIfLoadRxUtilization": bsnAPIfLoadRxUtilization,
       "bsnAPIfLoadTxUtilization": bsnAPIfLoadTxUtilization,
       "bsnAPIfLoadChannelUtilization": bsnAPIfLoadChannelUtilization,
       "bsnAPIfLoadNumOfClients": bsnAPIfLoadNumOfClients,
       "bsnAPIfPoorSNRClients": bsnAPIfPoorSNRClients,
       "bsnAPIfChannelInterferenceInfoTable": bsnAPIfChannelInterferenceInfoTable,
       "bsnAPIfChannelInterferenceInfoEntry": bsnAPIfChannelInterferenceInfoEntry,
       "bsnAPIfInterferenceChannelNo": bsnAPIfInterferenceChannelNo,
       "bsnAPIfInterferencePower": bsnAPIfInterferencePower,
       "bsnAPIfInterferenceUtilization": bsnAPIfInterferenceUtilization,
       "bsnAPIfChannelNoiseInfoTable": bsnAPIfChannelNoiseInfoTable,
       "bsnAPIfChannelNoiseInfoEntry": bsnAPIfChannelNoiseInfoEntry,
       "bsnAPIfNoiseChannelNo": bsnAPIfNoiseChannelNo,
       "bsnAPIfDBNoisePower": bsnAPIfDBNoisePower,
       "bsnAPIfProfileStateTable": bsnAPIfProfileStateTable,
       "bsnAPIfProfileStateEntry": bsnAPIfProfileStateEntry,
       "bsnAPIfLoadProfileState": bsnAPIfLoadProfileState,
       "bsnAPIfInterferenceProfileState": bsnAPIfInterferenceProfileState,
       "bsnAPIfNoiseProfileState": bsnAPIfNoiseProfileState,
       "bsnAPIfCoverageProfileState": bsnAPIfCoverageProfileState,
       "bsnAPIfRxNeighborsTable": bsnAPIfRxNeighborsTable,
       "bsnAPIfRxNeighborsEntry": bsnAPIfRxNeighborsEntry,
       "bsnAPIfRxNeighborMacAddress": bsnAPIfRxNeighborMacAddress,
       "bsnAPIfRxNeighborIpAddress": bsnAPIfRxNeighborIpAddress,
       "bsnAPIfRxNeighborRSSI": bsnAPIfRxNeighborRSSI,
       "bsnAPIfRxNeighborSlot": bsnAPIfRxNeighborSlot,
       "bsnAPIfRxNeighborChannel": bsnAPIfRxNeighborChannel,
       "bsnAPIfRxNeighborChannelWidth": bsnAPIfRxNeighborChannelWidth,
       "bsnAPIfStationRSSICoverageInfoTable": bsnAPIfStationRSSICoverageInfoTable,
       "bsnAPIfStationRSSICoverageInfoEntry": bsnAPIfStationRSSICoverageInfoEntry,
       "bsnAPIfStationRSSICoverageIndex": bsnAPIfStationRSSICoverageIndex,
       "bsnAPIfRSSILevel": bsnAPIfRSSILevel,
       "bsnAPIfStationCountOnRSSI": bsnAPIfStationCountOnRSSI,
       "bsnAPIfStationSNRCoverageInfoTable": bsnAPIfStationSNRCoverageInfoTable,
       "bsnAPIfStationSNRCoverageInfoEntry": bsnAPIfStationSNRCoverageInfoEntry,
       "bsnAPIfStationSNRCoverageIndex": bsnAPIfStationSNRCoverageIndex,
       "bsnAPIfSNRLevel": bsnAPIfSNRLevel,
       "bsnAPIfStationCountOnSNR": bsnAPIfStationCountOnSNR,
       "bsnAPIfRecommendedRFParametersTable": bsnAPIfRecommendedRFParametersTable,
       "bsnAPIfRecommendedRFParametersEntry": bsnAPIfRecommendedRFParametersEntry,
       "bsnAPIfRecommendedChannelNumber": bsnAPIfRecommendedChannelNumber,
       "bsnAPIfRecommendedTxPowerLevel": bsnAPIfRecommendedTxPowerLevel,
       "bsnAPIfRecommendedRTSThreshold": bsnAPIfRecommendedRTSThreshold,
       "bsnAPIfRecommendedFragmentationThreshold": bsnAPIfRecommendedFragmentationThreshold,
       "bsnAPIfWlanOverrideTable": bsnAPIfWlanOverrideTable,
       "bsnAPIfWlanOverrideEntry": bsnAPIfWlanOverrideEntry,
       "bsnAPIfWlanOverrideId": bsnAPIfWlanOverrideId,
       "bsnAPIfWlanOverrideSsid": bsnAPIfWlanOverrideSsid,
       "bsnAPIfWlanOverrideRowStatus": bsnAPIfWlanOverrideRowStatus,
       "bsnMeshNodeTable": bsnMeshNodeTable,
       "bsnMeshNodeEntry": bsnMeshNodeEntry,
       "bsnMeshNodeRole": bsnMeshNodeRole,
       "bsnMeshNodeGroup": bsnMeshNodeGroup,
       "bsnMeshNodeBackhaul": bsnMeshNodeBackhaul,
       "bsnMeshNodeBackhaulPAP": bsnMeshNodeBackhaulPAP,
       "bsnMeshNodeBackhaulRAP": bsnMeshNodeBackhaulRAP,
       "bsnMeshNodeDataRate": bsnMeshNodeDataRate,
       "bsnMeshNodeChannel": bsnMeshNodeChannel,
       "bsnMeshNodeRoutingState": bsnMeshNodeRoutingState,
       "bsnMeshNodeMalformedNeighPackets": bsnMeshNodeMalformedNeighPackets,
       "bsnMeshNodePoorNeighSnr": bsnMeshNodePoorNeighSnr,
       "bsnMeshNodeBlacklistPackets": bsnMeshNodeBlacklistPackets,
       "bsnMeshNodeInsufficientMemory": bsnMeshNodeInsufficientMemory,
       "bsnMeshNodeRxNeighReq": bsnMeshNodeRxNeighReq,
       "bsnMeshNodeRxNeighRsp": bsnMeshNodeRxNeighRsp,
       "bsnMeshNodeTxNeighReq": bsnMeshNodeTxNeighReq,
       "bsnMeshNodeTxNeighRsp": bsnMeshNodeTxNeighRsp,
       "bsnMeshNodeParentChanges": bsnMeshNodeParentChanges,
       "bsnMeshNodeNeighTimeout": bsnMeshNodeNeighTimeout,
       "bsnMeshNodeParentMacAddress": bsnMeshNodeParentMacAddress,
       "bsnMeshNodeAPType": bsnMeshNodeAPType,
       "bsnMeshNodeEthernetBridge": bsnMeshNodeEthernetBridge,
       "bsnMeshNodeHops": bsnMeshNodeHops,
       "bsnMeshNeighsTable": bsnMeshNeighsTable,
       "bsnMeshNeighsEntry": bsnMeshNeighsEntry,
       "bsnMeshNeighMacAddress": bsnMeshNeighMacAddress,
       "bsnMeshNeighType": bsnMeshNeighType,
       "bsnMeshNeighState": bsnMeshNeighState,
       "bsnMeshNeighSnr": bsnMeshNeighSnr,
       "bsnMeshNeighSnrUp": bsnMeshNeighSnrUp,
       "bsnMeshNeighSnrDown": bsnMeshNeighSnrDown,
       "bsnMeshNeighLinkSnr": bsnMeshNeighLinkSnr,
       "bsnMeshNeighAdjustedEase": bsnMeshNeighAdjustedEase,
       "bsnMeshNeighUnadjustedEase": bsnMeshNeighUnadjustedEase,
       "bsnMeshNeighRapEase": bsnMeshNeighRapEase,
       "bsnMeshNeighTxParent": bsnMeshNeighTxParent,
       "bsnMeshNeighRxParent": bsnMeshNeighRxParent,
       "bsnMeshNeighPoorSnr": bsnMeshNeighPoorSnr,
       "bsnMeshNeighLastUpdate": bsnMeshNeighLastUpdate,
       "bsnMeshNeighParentChange": bsnMeshNeighParentChange,
       "bsnAPIfRadarChannelStatisticsTable": bsnAPIfRadarChannelStatisticsTable,
       "bsnAPIfRadarChannelStatisticsEntry": bsnAPIfRadarChannelStatisticsEntry,
       "bsnAPIfRadarDetectedChannelNumber": bsnAPIfRadarDetectedChannelNumber,
       "bsnAPIfRadarSignalLastHeard": bsnAPIfRadarSignalLastHeard,
       "bsnGlobalDot11": bsnGlobalDot11,
       "bsnGlobalDot11Config": bsnGlobalDot11Config,
       "bsnGlobalDot11PrivacyOptionImplemented": bsnGlobalDot11PrivacyOptionImplemented,
       "bsnGlobalDot11AuthenticationResponseTimeOut": bsnGlobalDot11AuthenticationResponseTimeOut,
       "bsnGlobalDot11MultiDomainCapabilityImplemented": bsnGlobalDot11MultiDomainCapabilityImplemented,
       "bsnGlobalDot11MultiDomainCapabilityEnabled": bsnGlobalDot11MultiDomainCapabilityEnabled,
       "bsnGlobalDot11CountryIndex": bsnGlobalDot11CountryIndex,
       "bsnGlobalDot11LoadBalancing": bsnGlobalDot11LoadBalancing,
       "bsnGlobalDot11RogueTimer": bsnGlobalDot11RogueTimer,
       "bsnPrimaryMwarForAPs": bsnPrimaryMwarForAPs,
       "bsnRtpProtocolPriority": bsnRtpProtocolPriority,
       "bsnSystemCurrentTime": bsnSystemCurrentTime,
       "bsnUpdateSystemTime": bsnUpdateSystemTime,
       "bsnOperatingTemperatureEnvironment": bsnOperatingTemperatureEnvironment,
       "bsnSensorTemperature": bsnSensorTemperature,
       "bsnTemperatureAlarmLowLimit": bsnTemperatureAlarmLowLimit,
       "bsnTemperatureAlarmHighLimit": bsnTemperatureAlarmHighLimit,
       "bsnVirtualGatewayAddress": bsnVirtualGatewayAddress,
       "bsnRFMobilityDomainName": bsnRFMobilityDomainName,
       "bsnClientWatchListFeature": bsnClientWatchListFeature,
       "bsnRogueLocationDiscoveryProtocol": bsnRogueLocationDiscoveryProtocol,
       "bsnRogueAutoContainFeature": bsnRogueAutoContainFeature,
       "bsnOverAirProvisionApMode": bsnOverAirProvisionApMode,
       "bsnMaximumNumberOfConcurrentLogins": bsnMaximumNumberOfConcurrentLogins,
       "bsnAutoContainRoguesAdvertisingSsid": bsnAutoContainRoguesAdvertisingSsid,
       "bsnAutoContainAdhocNetworks": bsnAutoContainAdhocNetworks,
       "bsnAutoContainTrustedClientsOnRogueAps": bsnAutoContainTrustedClientsOnRogueAps,
       "bsnValidateRogueClientsAgainstAAA": bsnValidateRogueClientsAgainstAAA,
       "bsnSystemTimezoneDelta": bsnSystemTimezoneDelta,
       "bsnSystemTimezoneDaylightSavings": bsnSystemTimezoneDaylightSavings,
       "bsnAllowAuthorizeApAgainstAAA": bsnAllowAuthorizeApAgainstAAA,
       "bsnSystemTimezoneDeltaMinutes": bsnSystemTimezoneDeltaMinutes,
       "bsnApFallbackEnabled": bsnApFallbackEnabled,
       "bsnAppleTalkEnabled": bsnAppleTalkEnabled,
       "bsnTrustedApPolicyConfig": bsnTrustedApPolicyConfig,
       "bsnPolicyForMisconfiguredAps": bsnPolicyForMisconfiguredAps,
       "bsnEncryptionPolicyEnforced": bsnEncryptionPolicyEnforced,
       "bsnPreamblePolicyEnforced": bsnPreamblePolicyEnforced,
       "bsnDot11ModePolicyEnforced": bsnDot11ModePolicyEnforced,
       "bsnRadioTypePolicyEnforced": bsnRadioTypePolicyEnforced,
       "bsnValidateSsidForTrustedAp": bsnValidateSsidForTrustedAp,
       "bsnAlertIfTrustedApMissing": bsnAlertIfTrustedApMissing,
       "bsnTrustedApEntryExpirationTimeout": bsnTrustedApEntryExpirationTimeout,
       "bsnClientExclusionPolicyConfig": bsnClientExclusionPolicyConfig,
       "bsnExcessive80211AssocFailures": bsnExcessive80211AssocFailures,
       "bsnExcessive80211AuthFailures": bsnExcessive80211AuthFailures,
       "bsnExcessive8021xAuthFailures": bsnExcessive8021xAuthFailures,
       "bsnExternalPolicyServerFailures": bsnExternalPolicyServerFailures,
       "bsnExcessiveWebAuthFailures": bsnExcessiveWebAuthFailures,
       "bsnIPTheftORReuse": bsnIPTheftORReuse,
       "bsnSignatureConfig": bsnSignatureConfig,
       "bsnStandardSignatureTable": bsnStandardSignatureTable,
       "bsnStandardSignatureEntry": bsnStandardSignatureEntry,
       "bsnStandardSignaturePrecedence": bsnStandardSignaturePrecedence,
       "bsnStandardSignatureName": bsnStandardSignatureName,
       "bsnStandardSignatureDescription": bsnStandardSignatureDescription,
       "bsnStandardSignatureFrameType": bsnStandardSignatureFrameType,
       "bsnStandardSignatureAction": bsnStandardSignatureAction,
       "bsnStandardSignatureState": bsnStandardSignatureState,
       "bsnStandardSignatureFrequency": bsnStandardSignatureFrequency,
       "bsnStandardSignatureQuietTime": bsnStandardSignatureQuietTime,
       "bsnStandardSignatureVersion": bsnStandardSignatureVersion,
       "bsnStandardSignatureConfigType": bsnStandardSignatureConfigType,
       "bsnStandardSignatureEnable": bsnStandardSignatureEnable,
       "bsnStandardSignatureMacInfo": bsnStandardSignatureMacInfo,
       "bsnStandardSignatureMacFreq": bsnStandardSignatureMacFreq,
       "bsnStandardSignatureRowStatus": bsnStandardSignatureRowStatus,
       "bsnStandardSignatureInterval": bsnStandardSignatureInterval,
       "bsnStandardSignaturePatternTable": bsnStandardSignaturePatternTable,
       "bsnStandardSignaturePatternEntry": bsnStandardSignaturePatternEntry,
       "bsnStandardSignaturePatternIndex": bsnStandardSignaturePatternIndex,
       "bsnStandardSignaturePatternOffset": bsnStandardSignaturePatternOffset,
       "bsnStandardSignaturePatternString": bsnStandardSignaturePatternString,
       "bsnStandardSignaturePatternMask": bsnStandardSignaturePatternMask,
       "bsnStandardSignaturePatternOffSetStart": bsnStandardSignaturePatternOffSetStart,
       "bsnStandardSignaturePatternRowStatus": bsnStandardSignaturePatternRowStatus,
       "bsnCustomSignatureTable": bsnCustomSignatureTable,
       "bsnCustomSignatureEntry": bsnCustomSignatureEntry,
       "bsnCustomSignaturePrecedence": bsnCustomSignaturePrecedence,
       "bsnCustomSignatureName": bsnCustomSignatureName,
       "bsnCustomSignatureDescription": bsnCustomSignatureDescription,
       "bsnCustomSignatureFrameType": bsnCustomSignatureFrameType,
       "bsnCustomSignatureAction": bsnCustomSignatureAction,
       "bsnCustomSignatureState": bsnCustomSignatureState,
       "bsnCustomSignatureFrequency": bsnCustomSignatureFrequency,
       "bsnCustomSignatureQuietTime": bsnCustomSignatureQuietTime,
       "bsnCustomSignatureVersion": bsnCustomSignatureVersion,
       "bsnCustomSignatureConfigType": bsnCustomSignatureConfigType,
       "bsnCustomSignatureEnable": bsnCustomSignatureEnable,
       "bsnCustomSignatureMacInfo": bsnCustomSignatureMacInfo,
       "bsnCustomSignatureMacFreq": bsnCustomSignatureMacFreq,
       "bsnCustomSignatureRowStatus": bsnCustomSignatureRowStatus,
       "bsnCustomSignatureInterval": bsnCustomSignatureInterval,
       "bsnCustomSignaturePatternTable": bsnCustomSignaturePatternTable,
       "bsnCustomSignaturePatternEntry": bsnCustomSignaturePatternEntry,
       "bsnCustomSignaturePatternIndex": bsnCustomSignaturePatternIndex,
       "bsnCustomSignaturePatternOffset": bsnCustomSignaturePatternOffset,
       "bsnCustomSignaturePatternString": bsnCustomSignaturePatternString,
       "bsnCustomSignaturePatternMask": bsnCustomSignaturePatternMask,
       "bsnCustomSignaturePatternOffSetStart": bsnCustomSignaturePatternOffSetStart,
       "bsnCustomSignaturePatternRowStatus": bsnCustomSignaturePatternRowStatus,
       "bsnSignatureCheckState": bsnSignatureCheckState,
       "bsnRfIdTagConfig": bsnRfIdTagConfig,
       "bsnRfIdTagStatus": bsnRfIdTagStatus,
       "bsnRfIdTagDataTimeout": bsnRfIdTagDataTimeout,
       "bsnRfIdTagAutoTimeoutStatus": bsnRfIdTagAutoTimeoutStatus,
       "bsnAPNeighborAuthConfig": bsnAPNeighborAuthConfig,
       "bsnAPNeighborAuthStatus": bsnAPNeighborAuthStatus,
       "bsnAPNeighborAuthAlarmThreshold": bsnAPNeighborAuthAlarmThreshold,
       "bsnRFNetworkName": bsnRFNetworkName,
       "bsnFastSSIDChangeFeature": bsnFastSSIDChangeFeature,
       "bsnBridgingPolicyConfig": bsnBridgingPolicyConfig,
       "bsnBridgingZeroTouchConfig": bsnBridgingZeroTouchConfig,
       "bsnBridgingSharedSecretKey": bsnBridgingSharedSecretKey,
       "bsnAcceptSelfSignedCertificate": bsnAcceptSelfSignedCertificate,
       "bsnSystemClockTime": bsnSystemClockTime,
       "bsnGlobalDot11b": bsnGlobalDot11b,
       "bsnGlobalDot11bConfig": bsnGlobalDot11bConfig,
       "bsnGlobalDot11bNetworkStatus": bsnGlobalDot11bNetworkStatus,
       "bsnGlobalDot11bBeaconPeriod": bsnGlobalDot11bBeaconPeriod,
       "bsnGlobalDot11bDynamicChannelAssignment": bsnGlobalDot11bDynamicChannelAssignment,
       "bsnGlobalDot11bCurrentChannel": bsnGlobalDot11bCurrentChannel,
       "bsnGlobalDot11bDynamicChannelUpdateInterval": bsnGlobalDot11bDynamicChannelUpdateInterval,
       "bsnGlobalDot11bInputsForDCA": bsnGlobalDot11bInputsForDCA,
       "bsnGlobalDot11bChannelUpdateCmdInvoke": bsnGlobalDot11bChannelUpdateCmdInvoke,
       "bsnGlobalDot11bChannelUpdateCmdStatus": bsnGlobalDot11bChannelUpdateCmdStatus,
       "bsnGlobalDot11bDynamicTransmitPowerControl": bsnGlobalDot11bDynamicTransmitPowerControl,
       "bsnGlobalDot11bDynamicTxPowerControlInterval": bsnGlobalDot11bDynamicTxPowerControlInterval,
       "bsnGlobalDot11bCurrentTxPowerLevel": bsnGlobalDot11bCurrentTxPowerLevel,
       "bsnGlobalDot11bInputsForDTP": bsnGlobalDot11bInputsForDTP,
       "bsnGlobalDot11bPowerUpdateCmdInvoke": bsnGlobalDot11bPowerUpdateCmdInvoke,
       "bsnGlobalDot11bPowerUpdateCmdStatus": bsnGlobalDot11bPowerUpdateCmdStatus,
       "bsnGlobalDot11bDataRate1Mhz": bsnGlobalDot11bDataRate1Mhz,
       "bsnGlobalDot11bDataRate2Mhz": bsnGlobalDot11bDataRate2Mhz,
       "bsnGlobalDot11bDataRate5AndHalfMhz": bsnGlobalDot11bDataRate5AndHalfMhz,
       "bsnGlobalDot11bDataRate11Mhz": bsnGlobalDot11bDataRate11Mhz,
       "bsnGlobalDot11bShortPreamble": bsnGlobalDot11bShortPreamble,
       "bsnGlobalDot11bDot11gSupport": bsnGlobalDot11bDot11gSupport,
       "bsnGlobalDot11bDataRate6Mhz": bsnGlobalDot11bDataRate6Mhz,
       "bsnGlobalDot11bDataRate9Mhz": bsnGlobalDot11bDataRate9Mhz,
       "bsnGlobalDot11bDataRate12Mhz": bsnGlobalDot11bDataRate12Mhz,
       "bsnGlobalDot11bDataRate18Mhz": bsnGlobalDot11bDataRate18Mhz,
       "bsnGlobalDot11bDataRate24Mhz": bsnGlobalDot11bDataRate24Mhz,
       "bsnGlobalDot11bDataRate36Mhz": bsnGlobalDot11bDataRate36Mhz,
       "bsnGlobalDot11bDataRate48Mhz": bsnGlobalDot11bDataRate48Mhz,
       "bsnGlobalDot11bDataRate54Mhz": bsnGlobalDot11bDataRate54Mhz,
       "bsnGlobalDot11bPicoCellMode": bsnGlobalDot11bPicoCellMode,
       "bsnGlobalDot11bFastRoamingMode": bsnGlobalDot11bFastRoamingMode,
       "bsnGlobalDot11bFastRoamingVoipMinRate": bsnGlobalDot11bFastRoamingVoipMinRate,
       "bsnGlobalDot11bFastRoamingVoipPercentage": bsnGlobalDot11bFastRoamingVoipPercentage,
       "bsnGlobalDot11b80211eMaxBandwidth": bsnGlobalDot11b80211eMaxBandwidth,
       "bsnGlobalDot11bDTPCSupport": bsnGlobalDot11bDTPCSupport,
       "bsnGlobalDot11bRxSopThreshold": bsnGlobalDot11bRxSopThreshold,
       "bsnGlobalDot11bPhy": bsnGlobalDot11bPhy,
       "bsnGlobalDot11bMediumOccupancyLimit": bsnGlobalDot11bMediumOccupancyLimit,
       "bsnGlobalDot11bCFPPeriod": bsnGlobalDot11bCFPPeriod,
       "bsnGlobalDot11bCFPMaxDuration": bsnGlobalDot11bCFPMaxDuration,
       "bsnGlobalDot11bCFPollable": bsnGlobalDot11bCFPollable,
       "bsnGlobalDot11bCFPollRequest": bsnGlobalDot11bCFPollRequest,
       "bsnGlobalDot11bDTIMPeriod": bsnGlobalDot11bDTIMPeriod,
       "bsnGlobalDot11bMaximumTransmitPowerLevel": bsnGlobalDot11bMaximumTransmitPowerLevel,
       "bsnGlobalDot11bFirstChannelNumber": bsnGlobalDot11bFirstChannelNumber,
       "bsnGlobalDot11bNumberofChannels": bsnGlobalDot11bNumberofChannels,
       "bsnGlobalDot11bRTSThreshold": bsnGlobalDot11bRTSThreshold,
       "bsnGlobalDot11bShortRetryLimit": bsnGlobalDot11bShortRetryLimit,
       "bsnGlobalDot11bLongRetryLimit": bsnGlobalDot11bLongRetryLimit,
       "bsnGlobalDot11bFragmentationThreshold": bsnGlobalDot11bFragmentationThreshold,
       "bsnGlobalDot11bMaxTransmitMSDULifetime": bsnGlobalDot11bMaxTransmitMSDULifetime,
       "bsnGlobalDot11bMaxReceiveLifetime": bsnGlobalDot11bMaxReceiveLifetime,
       "bsnGlobalDot11bEDThreshold": bsnGlobalDot11bEDThreshold,
       "bsnGlobalDot11bChannelAgilityEnabled": bsnGlobalDot11bChannelAgilityEnabled,
       "bsnGlobalDot11bPBCCOptionImplemented": bsnGlobalDot11bPBCCOptionImplemented,
       "bsnGlobalDot11bShortPreambleOptionImplemented": bsnGlobalDot11bShortPreambleOptionImplemented,
       "bsnGlobalDot11a": bsnGlobalDot11a,
       "bsnGlobalDot11aConfig": bsnGlobalDot11aConfig,
       "bsnGlobalDot11aNetworkStatus": bsnGlobalDot11aNetworkStatus,
       "bsnGlobalDot11aLowBandNetwork": bsnGlobalDot11aLowBandNetwork,
       "bsnGlobalDot11aMediumBandNetwork": bsnGlobalDot11aMediumBandNetwork,
       "bsnGlobalDot11aHighBandNetwork": bsnGlobalDot11aHighBandNetwork,
       "bsnGlobalDot11aBeaconPeriod": bsnGlobalDot11aBeaconPeriod,
       "bsnGlobalDot11aDynamicChannelAssignment": bsnGlobalDot11aDynamicChannelAssignment,
       "bsnGlobalDot11aCurrentChannel": bsnGlobalDot11aCurrentChannel,
       "bsnGlobalDot11aDynamicChannelUpdateInterval": bsnGlobalDot11aDynamicChannelUpdateInterval,
       "bsnGlobalDot11aInputsForDCA": bsnGlobalDot11aInputsForDCA,
       "bsnGlobalDot11aChannelUpdateCmdInvoke": bsnGlobalDot11aChannelUpdateCmdInvoke,
       "bsnGlobalDot11aChannelUpdateCmdStatus": bsnGlobalDot11aChannelUpdateCmdStatus,
       "bsnGlobalDot11aDynamicTransmitPowerControl": bsnGlobalDot11aDynamicTransmitPowerControl,
       "bsnGlobalDot11aCurrentTxPowerLevel": bsnGlobalDot11aCurrentTxPowerLevel,
       "bsnGlobalDot11aDynamicTxPowerControlInterval": bsnGlobalDot11aDynamicTxPowerControlInterval,
       "bsnGlobalDot11aInputsForDTP": bsnGlobalDot11aInputsForDTP,
       "bsnGlobalDot11aPowerUpdateCmdInvoke": bsnGlobalDot11aPowerUpdateCmdInvoke,
       "bsnGlobalDot11aPowerUpdateCmdStatus": bsnGlobalDot11aPowerUpdateCmdStatus,
       "bsnGlobalDot11aDataRate6Mhz": bsnGlobalDot11aDataRate6Mhz,
       "bsnGlobalDot11aDataRate9Mhz": bsnGlobalDot11aDataRate9Mhz,
       "bsnGlobalDot11aDataRate12Mhz": bsnGlobalDot11aDataRate12Mhz,
       "bsnGlobalDot11aDataRate18Mhz": bsnGlobalDot11aDataRate18Mhz,
       "bsnGlobalDot11aDataRate24Mhz": bsnGlobalDot11aDataRate24Mhz,
       "bsnGlobalDot11aDataRate36Mhz": bsnGlobalDot11aDataRate36Mhz,
       "bsnGlobalDot11aDataRate48Mhz": bsnGlobalDot11aDataRate48Mhz,
       "bsnGlobalDot11aDataRate54Mhz": bsnGlobalDot11aDataRate54Mhz,
       "bsnGlobalDot11aPicoCellMode": bsnGlobalDot11aPicoCellMode,
       "bsnGlobalDot11aFastRoamingMode": bsnGlobalDot11aFastRoamingMode,
       "bsnGlobalDot11aFastRoamingVoipMinRate": bsnGlobalDot11aFastRoamingVoipMinRate,
       "bsnGlobalDot11aFastRoamingVoipPercentage": bsnGlobalDot11aFastRoamingVoipPercentage,
       "bsnGlobalDot11a80211eMaxBandwidth": bsnGlobalDot11a80211eMaxBandwidth,
       "bsnGlobalDot11aDTPCSupport": bsnGlobalDot11aDTPCSupport,
       "bsnGlobalDot11aRxSopThreshold": bsnGlobalDot11aRxSopThreshold,
       "bsnGlobalDot11aPhy": bsnGlobalDot11aPhy,
       "bsnGlobalDot11aMediumOccupancyLimit": bsnGlobalDot11aMediumOccupancyLimit,
       "bsnGlobalDot11aCFPPeriod": bsnGlobalDot11aCFPPeriod,
       "bsnGlobalDot11aCFPMaxDuration": bsnGlobalDot11aCFPMaxDuration,
       "bsnGlobalDot11aCFPollable": bsnGlobalDot11aCFPollable,
       "bsnGlobalDot11aCFPollRequest": bsnGlobalDot11aCFPollRequest,
       "bsnGlobalDot11aDTIMPeriod": bsnGlobalDot11aDTIMPeriod,
       "bsnGlobalDot11aMaximumTransmitPowerLevel": bsnGlobalDot11aMaximumTransmitPowerLevel,
       "bsnGlobalDot11aFirstChannelNumber": bsnGlobalDot11aFirstChannelNumber,
       "bsnGlobalDot11aNumberofChannels": bsnGlobalDot11aNumberofChannels,
       "bsnGlobalDot11aRTSThreshold": bsnGlobalDot11aRTSThreshold,
       "bsnGlobalDot11aShortRetryLimit": bsnGlobalDot11aShortRetryLimit,
       "bsnGlobalDot11aLongRetryLimit": bsnGlobalDot11aLongRetryLimit,
       "bsnGlobalDot11aFragmentationThreshold": bsnGlobalDot11aFragmentationThreshold,
       "bsnGlobalDot11aMaxTransmitMSDULifetime": bsnGlobalDot11aMaxTransmitMSDULifetime,
       "bsnGlobalDot11aMaxReceiveLifetime": bsnGlobalDot11aMaxReceiveLifetime,
       "bsnGlobalDot11aTIThreshold": bsnGlobalDot11aTIThreshold,
       "bsnGlobalDot11aChannelAgilityEnabled": bsnGlobalDot11aChannelAgilityEnabled,
       "bsnGlobalDot11h": bsnGlobalDot11h,
       "bsnGlobalDot11hConfig": bsnGlobalDot11hConfig,
       "bsnGlobalDot11hPowerConstraint": bsnGlobalDot11hPowerConstraint,
       "bsnGlobalDot11hChannelSwitchEnable": bsnGlobalDot11hChannelSwitchEnable,
       "bsnGlobalDot11hChannelSwitchMode": bsnGlobalDot11hChannelSwitchMode,
       "bsnRrm": bsnRrm,
       "bsnRrmDot11a": bsnRrmDot11a,
       "bsnRrmDot11aGroup": bsnRrmDot11aGroup,
       "bsnRrmDot11aGlobalAutomaticGrouping": bsnRrmDot11aGlobalAutomaticGrouping,
       "bsnRrmDot11aGroupLeaderMacAddr": bsnRrmDot11aGroupLeaderMacAddr,
       "bsnRrmIsDot11aGroupLeader": bsnRrmIsDot11aGroupLeader,
       "bsnRrmDot11aGroupLastUpdateTime": bsnRrmDot11aGroupLastUpdateTime,
       "bsnRrmDot11aGlobalGroupInterval": bsnRrmDot11aGlobalGroupInterval,
       "bsnWrasDot11aGroupTable": bsnWrasDot11aGroupTable,
       "bsnWrasDot11aGroupEntry": bsnWrasDot11aGroupEntry,
       "bsnWrasDot11aPeerMacAddress": bsnWrasDot11aPeerMacAddress,
       "bsnWrasDot11aPeerIpAddress": bsnWrasDot11aPeerIpAddress,
       "bsnRrmDot11aAPDefault": bsnRrmDot11aAPDefault,
       "bsnRrmDot11aForeignInterferenceThreshold": bsnRrmDot11aForeignInterferenceThreshold,
       "bsnRrmDot11aForeignNoiseThreshold": bsnRrmDot11aForeignNoiseThreshold,
       "bsnRrmDot11aRFUtilizationThreshold": bsnRrmDot11aRFUtilizationThreshold,
       "bsnRrmDot11aThroughputThreshold": bsnRrmDot11aThroughputThreshold,
       "bsnRrmDot11aMobilesThreshold": bsnRrmDot11aMobilesThreshold,
       "bsnRrmDot11aCoverageThreshold": bsnRrmDot11aCoverageThreshold,
       "bsnRrmDot11aMobileMinExceptionLevel": bsnRrmDot11aMobileMinExceptionLevel,
       "bsnRrmDot11aCoverageExceptionLevel": bsnRrmDot11aCoverageExceptionLevel,
       "bsnRrmDot11aSignalMeasurementInterval": bsnRrmDot11aSignalMeasurementInterval,
       "bsnRrmDot11aNoiseMeasurementInterval": bsnRrmDot11aNoiseMeasurementInterval,
       "bsnRrmDot11aLoadMeasurementInterval": bsnRrmDot11aLoadMeasurementInterval,
       "bsnRrmDot11aCoverageMeasurementInterval": bsnRrmDot11aCoverageMeasurementInterval,
       "bsnRrmDot11aChannelMonitorList": bsnRrmDot11aChannelMonitorList,
       "bsnRrmDot11aSetFactoryDefault": bsnRrmDot11aSetFactoryDefault,
       "bsnRrmDot11b": bsnRrmDot11b,
       "bsnRrmDot11bGroup": bsnRrmDot11bGroup,
       "bsnRrmDot11bGlobalAutomaticGrouping": bsnRrmDot11bGlobalAutomaticGrouping,
       "bsnRrmDot11bGroupLeaderMacAddr": bsnRrmDot11bGroupLeaderMacAddr,
       "bsnRrmIsDot11bGroupLeader": bsnRrmIsDot11bGroupLeader,
       "bsnRrmDot11bGroupLastUpdateTime": bsnRrmDot11bGroupLastUpdateTime,
       "bsnRrmDot11bGlobalGroupInterval": bsnRrmDot11bGlobalGroupInterval,
       "bsnWrasDot11bGroupTable": bsnWrasDot11bGroupTable,
       "bsnWrasDot11bGroupEntry": bsnWrasDot11bGroupEntry,
       "bsnWrasDot11bPeerMacAddress": bsnWrasDot11bPeerMacAddress,
       "bsnWrasDot11bPeerIpAddress": bsnWrasDot11bPeerIpAddress,
       "bsnRrmDot11bAPDefault": bsnRrmDot11bAPDefault,
       "bsnRrmDot11bForeignInterferenceThreshold": bsnRrmDot11bForeignInterferenceThreshold,
       "bsnRrmDot11bForeignNoiseThreshold": bsnRrmDot11bForeignNoiseThreshold,
       "bsnRrmDot11bRFUtilizationThreshold": bsnRrmDot11bRFUtilizationThreshold,
       "bsnRrmDot11bThroughputThreshold": bsnRrmDot11bThroughputThreshold,
       "bsnRrmDot11bMobilesThreshold": bsnRrmDot11bMobilesThreshold,
       "bsnRrmDot11bCoverageThreshold": bsnRrmDot11bCoverageThreshold,
       "bsnRrmDot11bMobileMinExceptionLevel": bsnRrmDot11bMobileMinExceptionLevel,
       "bsnRrmDot11bCoverageExceptionLevel": bsnRrmDot11bCoverageExceptionLevel,
       "bsnRrmDot11bSignalMeasurementInterval": bsnRrmDot11bSignalMeasurementInterval,
       "bsnRrmDot11bNoiseMeasurementInterval": bsnRrmDot11bNoiseMeasurementInterval,
       "bsnRrmDot11bLoadMeasurementInterval": bsnRrmDot11bLoadMeasurementInterval,
       "bsnRrmDot11bCoverageMeasurementInterval": bsnRrmDot11bCoverageMeasurementInterval,
       "bsnRrmDot11bChannelMonitorList": bsnRrmDot11bChannelMonitorList,
       "bsnRrmDot11bSetFactoryDefault": bsnRrmDot11bSetFactoryDefault,
       "bsnAAA": bsnAAA,
       "bsnRadiusAuthServerTable": bsnRadiusAuthServerTable,
       "bsnRadiusAuthServerEntry": bsnRadiusAuthServerEntry,
       "bsnRadiusAuthServerIndex": bsnRadiusAuthServerIndex,
       "bsnRadiusAuthServerAddress": bsnRadiusAuthServerAddress,
       "bsnRadiusAuthClientServerPortNumber": bsnRadiusAuthClientServerPortNumber,
       "bsnRadiusAuthServerKey": bsnRadiusAuthServerKey,
       "bsnRadiusAuthServerStatus": bsnRadiusAuthServerStatus,
       "bsnRadiusAuthServerKeyFormat": bsnRadiusAuthServerKeyFormat,
       "bsnRadiusAuthServerRFC3576": bsnRadiusAuthServerRFC3576,
       "bsnRadiusAuthServerIPSec": bsnRadiusAuthServerIPSec,
       "bsnRadiusAuthServerIPSecAuth": bsnRadiusAuthServerIPSecAuth,
       "bsnRadiusAuthServerIPSecEncryption": bsnRadiusAuthServerIPSecEncryption,
       "bsnRadiusAuthServerIPSecIKEPhase1": bsnRadiusAuthServerIPSecIKEPhase1,
       "bsnRadiusAuthServerIPSecIKELifetime": bsnRadiusAuthServerIPSecIKELifetime,
       "bsnRadiusAuthServerIPSecDHGroup": bsnRadiusAuthServerIPSecDHGroup,
       "bsnRadiusAuthServerNetworkUserConfig": bsnRadiusAuthServerNetworkUserConfig,
       "bsnRadiusAuthServerMgmtUserConfig": bsnRadiusAuthServerMgmtUserConfig,
       "bsnRadiusAuthServerRetransmitTimeout": bsnRadiusAuthServerRetransmitTimeout,
       "bsnRadiusAuthServerKeyWrapKEKkey": bsnRadiusAuthServerKeyWrapKEKkey,
       "bsnRadiusAuthServerKeyWrapMACKkey": bsnRadiusAuthServerKeyWrapMACKkey,
       "bsnRadiusAuthServerKeyWrapFormat": bsnRadiusAuthServerKeyWrapFormat,
       "bsnRadiusAuthServerRowStatus": bsnRadiusAuthServerRowStatus,
       "bsnRadiusAuthServerInetAddressType": bsnRadiusAuthServerInetAddressType,
       "bsnRadiusAuthServerInetAddress": bsnRadiusAuthServerInetAddress,
       "bsnRadiusAccServerTable": bsnRadiusAccServerTable,
       "bsnRadiusAccServerEntry": bsnRadiusAccServerEntry,
       "bsnRadiusAccServerIndex": bsnRadiusAccServerIndex,
       "bsnRadiusAccServerAddress": bsnRadiusAccServerAddress,
       "bsnRadiusAccClientServerPortNumber": bsnRadiusAccClientServerPortNumber,
       "bsnRadiusAccServerKey": bsnRadiusAccServerKey,
       "bsnRadiusAccServerStatus": bsnRadiusAccServerStatus,
       "bsnRadiusAccServerKeyFormat": bsnRadiusAccServerKeyFormat,
       "bsnRadiusAccServerIPSec": bsnRadiusAccServerIPSec,
       "bsnRadiusAccServerIPSecAuth": bsnRadiusAccServerIPSecAuth,
       "bsnRadiusAccServerIPSecEncryption": bsnRadiusAccServerIPSecEncryption,
       "bsnRadiusAccServerIPSecIKEPhase1": bsnRadiusAccServerIPSecIKEPhase1,
       "bsnRadiusAccServerIPSecIKELifetime": bsnRadiusAccServerIPSecIKELifetime,
       "bsnRadiusAccServerIPSecDHGroup": bsnRadiusAccServerIPSecDHGroup,
       "bsnRadiusAccServerNetworkUserConfig": bsnRadiusAccServerNetworkUserConfig,
       "bsnRadiusAccServerRetransmitTimeout": bsnRadiusAccServerRetransmitTimeout,
       "bsnRadiusAccServerRowStatus": bsnRadiusAccServerRowStatus,
       "bsnRadiusAccServerInetAddressType": bsnRadiusAccServerInetAddressType,
       "bsnRadiusAccServerInetAddress": bsnRadiusAccServerInetAddress,
       "bsnRadiusAuthServerStatsTable": bsnRadiusAuthServerStatsTable,
       "bsnRadiusAuthServerStatsEntry": bsnRadiusAuthServerStatsEntry,
       "bsnRadiusAuthClientRoundTripTime": bsnRadiusAuthClientRoundTripTime,
       "bsnRadiusAuthClientAccessRequests": bsnRadiusAuthClientAccessRequests,
       "bsnRadiusAuthClientAccessRetransmissions": bsnRadiusAuthClientAccessRetransmissions,
       "bsnRadiusAuthClientAccessAccepts": bsnRadiusAuthClientAccessAccepts,
       "bsnRadiusAuthClientAccessRejects": bsnRadiusAuthClientAccessRejects,
       "bsnRadiusAuthClientAccessChallenges": bsnRadiusAuthClientAccessChallenges,
       "bsnRadiusAuthClientMalformedAccessResponses": bsnRadiusAuthClientMalformedAccessResponses,
       "bsnRadiusAuthClientBadAuthenticators": bsnRadiusAuthClientBadAuthenticators,
       "bsnRadiusAuthClientPendingRequests": bsnRadiusAuthClientPendingRequests,
       "bsnRadiusAuthClientTimeouts": bsnRadiusAuthClientTimeouts,
       "bsnRadiusAuthClientUnknownTypes": bsnRadiusAuthClientUnknownTypes,
       "bsnRadiusAuthClientPacketsDropped": bsnRadiusAuthClientPacketsDropped,
       "bsnRadiusAccServerStatsTable": bsnRadiusAccServerStatsTable,
       "bsnRadiusAccServerStatsEntry": bsnRadiusAccServerStatsEntry,
       "bsnRadiusAccClientRoundTripTime": bsnRadiusAccClientRoundTripTime,
       "bsnRadiusAccClientRequests": bsnRadiusAccClientRequests,
       "bsnRadiusAccClientRetransmissions": bsnRadiusAccClientRetransmissions,
       "bsnRadiusAccClientResponses": bsnRadiusAccClientResponses,
       "bsnRadiusAccClientMalformedResponses": bsnRadiusAccClientMalformedResponses,
       "bsnRadiusAccClientBadAuthenticators": bsnRadiusAccClientBadAuthenticators,
       "bsnRadiusAccClientPendingRequests": bsnRadiusAccClientPendingRequests,
       "bsnRadiusAccClientTimeouts": bsnRadiusAccClientTimeouts,
       "bsnRadiusAccClientUnknownTypes": bsnRadiusAccClientUnknownTypes,
       "bsnRadiusAccClientPacketsDropped": bsnRadiusAccClientPacketsDropped,
       "bsnUsersTable": bsnUsersTable,
       "bsnUsersEntry": bsnUsersEntry,
       "bsnUserName": bsnUserName,
       "bsnUserPassword": bsnUserPassword,
       "bsnUserEssIndex": bsnUserEssIndex,
       "bsnUserAccessMode": bsnUserAccessMode,
       "bsnUserType": bsnUserType,
       "bsnUserInterfaceName": bsnUserInterfaceName,
       "bsnUserRowStatus": bsnUserRowStatus,
       "bsnBlackListClientTable": bsnBlackListClientTable,
       "bsnBlackListClientEntry": bsnBlackListClientEntry,
       "bsnBlackListClientMacAddress": bsnBlackListClientMacAddress,
       "bsnBlackListClientDescription": bsnBlackListClientDescription,
       "bsnBlackListClientRowStatus": bsnBlackListClientRowStatus,
       "bsnAclTable": bsnAclTable,
       "bsnAclEntry": bsnAclEntry,
       "bsnAclName": bsnAclName,
       "bsnAclApplyMode": bsnAclApplyMode,
       "bsnAclRowStatus": bsnAclRowStatus,
       "bsnAclRuleTable": bsnAclRuleTable,
       "bsnAclRuleEntry": bsnAclRuleEntry,
       "bsnAclRuleIndex": bsnAclRuleIndex,
       "bsnAclRuleAction": bsnAclRuleAction,
       "bsnAclRuleDirection": bsnAclRuleDirection,
       "bsnAclRuleSourceIpAddress": bsnAclRuleSourceIpAddress,
       "bsnAclRuleSourceIpNetmask": bsnAclRuleSourceIpNetmask,
       "bsnAclRuleDestinationIpAddress": bsnAclRuleDestinationIpAddress,
       "bsnAclRuleDestinationIpNetmask": bsnAclRuleDestinationIpNetmask,
       "bsnAclRuleProtocol": bsnAclRuleProtocol,
       "bsnAclRuleStartSourcePort": bsnAclRuleStartSourcePort,
       "bsnAclRuleEndSourcePort": bsnAclRuleEndSourcePort,
       "bsnAclRuleStartDestinationPort": bsnAclRuleStartDestinationPort,
       "bsnAclRuleEndDestinationPort": bsnAclRuleEndDestinationPort,
       "bsnAclRuleDscp": bsnAclRuleDscp,
       "bsnAclNewRuleIndex": bsnAclNewRuleIndex,
       "bsnAclRuleRowStatus": bsnAclRuleRowStatus,
       "bsnMacFilterTable": bsnMacFilterTable,
       "bsnMacFilterEntry": bsnMacFilterEntry,
       "bsnMacFilterAddress": bsnMacFilterAddress,
       "bsnMacFilterWlanId": bsnMacFilterWlanId,
       "bsnMacFilterInterfaceName": bsnMacFilterInterfaceName,
       "bsnMacFilterDescription": bsnMacFilterDescription,
       "bsnMacFilterRowStatus": bsnMacFilterRowStatus,
       "bsnLocalNetUserTable": bsnLocalNetUserTable,
       "bsnLocalNetUserEntry": bsnLocalNetUserEntry,
       "bsnLocalNetUserName": bsnLocalNetUserName,
       "bsnLocalNetUserWlanId": bsnLocalNetUserWlanId,
       "bsnLocalNetUserPassword": bsnLocalNetUserPassword,
       "bsnLocalNetUserDescription": bsnLocalNetUserDescription,
       "bsnLocalNetUserLifetime": bsnLocalNetUserLifetime,
       "bsnLocalNetUserStartTime": bsnLocalNetUserStartTime,
       "bsnLocalNetUserRemainingTime": bsnLocalNetUserRemainingTime,
       "bsnLocalNetUserRowStatus": bsnLocalNetUserRowStatus,
       "bsnLocalManagementUserTable": bsnLocalManagementUserTable,
       "bsnLocalManagementUserEntry": bsnLocalManagementUserEntry,
       "bsnLocalManagementUserName": bsnLocalManagementUserName,
       "bsnLocalManagementUserPassword": bsnLocalManagementUserPassword,
       "bsnLocalManagementUserAccessMode": bsnLocalManagementUserAccessMode,
       "bsnLocalManagementUserRowStatus": bsnLocalManagementUserRowStatus,
       "bsnRadiusAuthKeyWrapEnable": bsnRadiusAuthKeyWrapEnable,
       "bsnRadiusAuthCacheCredentialsLocally": bsnRadiusAuthCacheCredentialsLocally,
       "bsnAAAMacDelimiter": bsnAAAMacDelimiter,
       "bsnAAARadiusCompatibilityMode": bsnAAARadiusCompatibilityMode,
       "bsnAAARadiusCallStationIdType": bsnAAARadiusCallStationIdType,
       "bsnExternalPolicyServerAclName": bsnExternalPolicyServerAclName,
       "bsnExternalPolicyServerTable": bsnExternalPolicyServerTable,
       "bsnExternalPolicyServerEntry": bsnExternalPolicyServerEntry,
       "bsnExternalPolicyServerIndex": bsnExternalPolicyServerIndex,
       "bsnExternalPolicyServerAddress": bsnExternalPolicyServerAddress,
       "bsnExternalPolicyServerPortNumber": bsnExternalPolicyServerPortNumber,
       "bsnExternalPolicyServerKey": bsnExternalPolicyServerKey,
       "bsnExternalPolicyServerAdminStatus": bsnExternalPolicyServerAdminStatus,
       "bsnExternalPolicyServerConnectionStatus": bsnExternalPolicyServerConnectionStatus,
       "bsnExternalPolicyServerRowStatus": bsnExternalPolicyServerRowStatus,
       "bsnAAALocalDatabaseSize": bsnAAALocalDatabaseSize,
       "bsnAAACurrentLocalDatabaseSize": bsnAAACurrentLocalDatabaseSize,
       "bsnAPAuthorizationTable": bsnAPAuthorizationTable,
       "bsnAPAuthorizationEntry": bsnAPAuthorizationEntry,
       "bsnAPAuthMacAddress": bsnAPAuthMacAddress,
       "bsnAPAuthCertificateType": bsnAPAuthCertificateType,
       "bsnAPAuthHashKey": bsnAPAuthHashKey,
       "bsnAPAuthRowStatus": bsnAPAuthRowStatus,
       "bsnTrap": bsnTrap,
       "bsnTrapControl": bsnTrapControl,
       "bsnDot11StationTrapControlMask": bsnDot11StationTrapControlMask,
       "bsnAPTrapControlMask": bsnAPTrapControlMask,
       "bsnAPProfileTrapControlMask": bsnAPProfileTrapControlMask,
       "bsnAPParamUpdateTrapControlMask": bsnAPParamUpdateTrapControlMask,
       "bsnIpsecTrapsMask": bsnIpsecTrapsMask,
       "bsnRogueAPTrapEnable": bsnRogueAPTrapEnable,
       "bsnRADIUSServerTrapEnable": bsnRADIUSServerTrapEnable,
       "bsnAuthenticationFailureTrapEnable": bsnAuthenticationFailureTrapEnable,
       "bsnConfigSaveTrapEnable": bsnConfigSaveTrapEnable,
       "bsn80211SecurityTrapControlMask": bsn80211SecurityTrapControlMask,
       "bsnWpsTrapControlEnable": bsnWpsTrapControlEnable,
       "bsnTrapVariable": bsnTrapVariable,
       "bsnAuthFailureUserName": bsnAuthFailureUserName,
       "bsnAuthFailureUserType": bsnAuthFailureUserType,
       "bsnRemoteIPv4Address": bsnRemoteIPv4Address,
       "bsnIpsecErrorCount": bsnIpsecErrorCount,
       "bsnIpsecSPI": bsnIpsecSPI,
       "bsnRemoteUdpPort": bsnRemoteUdpPort,
       "bsnIkeAuthMethod": bsnIkeAuthMethod,
       "bsnIkeTotalInitFailures": bsnIkeTotalInitFailures,
       "bsnIkeTotalInitNoResponses": bsnIkeTotalInitNoResponses,
       "bsnIkeTotalRespFailures": bsnIkeTotalRespFailures,
       "bsnNotifiesSent": bsnNotifiesSent,
       "bsnNotifiesReceived": bsnNotifiesReceived,
       "bsnSuiteInitFailures": bsnSuiteInitFailures,
       "bsnSuiteRespondFailures": bsnSuiteRespondFailures,
       "bsnInitiatorCookie": bsnInitiatorCookie,
       "bsnResponderCookie": bsnResponderCookie,
       "bsnIsakmpInvalidCookies": bsnIsakmpInvalidCookies,
       "bsnCurrentRadiosCount": bsnCurrentRadiosCount,
       "bsnLicenseRadioCount": bsnLicenseRadioCount,
       "bsnAPMacAddrTrapVariable": bsnAPMacAddrTrapVariable,
       "bsnAPNameTrapVariable": bsnAPNameTrapVariable,
       "bsnAPSlotIdTrapVariable": bsnAPSlotIdTrapVariable,
       "bsnAPChannelNumberTrapVariable": bsnAPChannelNumberTrapVariable,
       "bsnAPCoverageThresholdTrapVariable": bsnAPCoverageThresholdTrapVariable,
       "bsnAPCoverageFailedClients": bsnAPCoverageFailedClients,
       "bsnAPCoverageTotalClients": bsnAPCoverageTotalClients,
       "bsnClientMacAddr": bsnClientMacAddr,
       "bsnClientRssi": bsnClientRssi,
       "bsnClientSnr": bsnClientSnr,
       "bsnInterferenceEnergyBeforeChannelUpdate": bsnInterferenceEnergyBeforeChannelUpdate,
       "bsnInterferenceEnergyAfterChannelUpdate": bsnInterferenceEnergyAfterChannelUpdate,
       "bsnAPPortNumberTrapVariable": bsnAPPortNumberTrapVariable,
       "bsnMaxRogueCount": bsnMaxRogueCount,
       "bsnStationMacAddress": bsnStationMacAddress,
       "bsnStationAPMacAddr": bsnStationAPMacAddr,
       "bsnStationAPIfSlotId": bsnStationAPIfSlotId,
       "bsnStationReasonCode": bsnStationReasonCode,
       "bsnStationBlacklistingReasonCode": bsnStationBlacklistingReasonCode,
       "bsnStationUserName": bsnStationUserName,
       "bsnRogueAPOnWiredNetwork": bsnRogueAPOnWiredNetwork,
       "bsnNavDosAttackSourceMacAddr": bsnNavDosAttackSourceMacAddr,
       "bsnWlanIdTrapVariable": bsnWlanIdTrapVariable,
       "bsnUserIpAddress": bsnUserIpAddress,
       "bsnRogueAdhocMode": bsnRogueAdhocMode,
       "bsnClearTrapVariable": bsnClearTrapVariable,
       "bsnDuplicateIpTrapVariable": bsnDuplicateIpTrapVariable,
       "bsnDuplicateIpTrapClear": bsnDuplicateIpTrapClear,
       "bsnDuplicateIpReportedByAP": bsnDuplicateIpReportedByAP,
       "bsnTrustedApRadioPolicyRequired": bsnTrustedApRadioPolicyRequired,
       "bsnTrustedApEncryptionUsed": bsnTrustedApEncryptionUsed,
       "bsnTrustedApEncryptionRequired": bsnTrustedApEncryptionRequired,
       "bsnTrustedApRadioPolicyUsed": bsnTrustedApRadioPolicyUsed,
       "bsnNetworkType": bsnNetworkType,
       "bsnNetworkState": bsnNetworkState,
       "bsnSignatureType": bsnSignatureType,
       "bsnSignatureName": bsnSignatureName,
       "bsnSignatureDescription": bsnSignatureDescription,
       "bsnImpersonatedAPMacAddr": bsnImpersonatedAPMacAddr,
       "bsnTrustedApPreambleUsed": bsnTrustedApPreambleUsed,
       "bsnTrustedApPreambleRequired": bsnTrustedApPreambleRequired,
       "bsnSignatureAttackPreced": bsnSignatureAttackPreced,
       "bsnSignatureAttackFrequency": bsnSignatureAttackFrequency,
       "bsnSignatureAttackChannel": bsnSignatureAttackChannel,
       "bsnSignatureAttackerMacAddress": bsnSignatureAttackerMacAddress,
       "bsnLicenseKeyTrapVariable": bsnLicenseKeyTrapVariable,
       "bsnApFunctionalityDisableReasonCode": bsnApFunctionalityDisableReasonCode,
       "bsnLicenseKeyFeatureSetTrapVariable": bsnLicenseKeyFeatureSetTrapVariable,
       "bsnApRegulatoryDomain": bsnApRegulatoryDomain,
       "bsnAPAuthorizationFailureCause": bsnAPAuthorizationFailureCause,
       "bsnAPIfUpDownCause": bsnAPIfUpDownCause,
       "bsnAPInvalidRadioType": bsnAPInvalidRadioType,
       "locationNotifyContent": locationNotifyContent,
       "bsnSignatureMacInfo": bsnSignatureMacInfo,
       "bsnImpersonatingSourceMacAddr": bsnImpersonatingSourceMacAddr,
       "bsnAPPreviousChannelNumberTrapVariable": bsnAPPreviousChannelNumberTrapVariable,
       "bsnAPReasonCodeTrapVariable": bsnAPReasonCodeTrapVariable,
       "bsnNoiseBeforeChannelUpdate": bsnNoiseBeforeChannelUpdate,
       "bsnNoiseAfterChannelUpdate": bsnNoiseAfterChannelUpdate,
       "bsnInterferenceBeforeChannelUpdate": bsnInterferenceBeforeChannelUpdate,
       "bsnInterferenceAfterChannelUpdate": bsnInterferenceAfterChannelUpdate,
       "bsnTraps": bsnTraps,
       "bsnDot11StationDisassociate": bsnDot11StationDisassociate,
       "bsnDot11StationDeauthenticate": bsnDot11StationDeauthenticate,
       "bsnDot11StationAuthenticateFail": bsnDot11StationAuthenticateFail,
       "bsnDot11StationAssociateFail": bsnDot11StationAssociateFail,
       "bsnAPUp": bsnAPUp,
       "bsnAPDown": bsnAPDown,
       "bsnAPAssociated": bsnAPAssociated,
       "bsnAPDisassociated": bsnAPDisassociated,
       "bsnAPIfUp": bsnAPIfUp,
       "bsnAPIfDown": bsnAPIfDown,
       "bsnAPLoadProfileFailed": bsnAPLoadProfileFailed,
       "bsnAPNoiseProfileFailed": bsnAPNoiseProfileFailed,
       "bsnAPInterferenceProfileFailed": bsnAPInterferenceProfileFailed,
       "bsnAPCoverageProfileFailed": bsnAPCoverageProfileFailed,
       "bsnAPCurrentTxPowerChanged": bsnAPCurrentTxPowerChanged,
       "bsnAPCurrentChannelChanged": bsnAPCurrentChannelChanged,
       "bsnRrmDot11aGroupingDone": bsnRrmDot11aGroupingDone,
       "bsnRrmDot11bGroupingDone": bsnRrmDot11bGroupingDone,
       "bsnConfigSaved": bsnConfigSaved,
       "bsnDot11EssCreated": bsnDot11EssCreated,
       "bsnDot11EssDeleted": bsnDot11EssDeleted,
       "bsnRADIUSServerNotResponding": bsnRADIUSServerNotResponding,
       "bsnAuthenticationFailure": bsnAuthenticationFailure,
       "bsnIpsecEspAuthFailureTrap": bsnIpsecEspAuthFailureTrap,
       "bsnIpsecEspReplayFailureTrap": bsnIpsecEspReplayFailureTrap,
       "bsnIpsecEspInvalidSpiTrap": bsnIpsecEspInvalidSpiTrap,
       "bsnIpsecIkeNegFailure": bsnIpsecIkeNegFailure,
       "bsnIpsecSuiteNegFailure": bsnIpsecSuiteNegFailure,
       "bsnIpsecInvalidCookieTrap": bsnIpsecInvalidCookieTrap,
       "bsnRogueAPDetected": bsnRogueAPDetected,
       "bsnAPLoadProfileUpdatedToPass": bsnAPLoadProfileUpdatedToPass,
       "bsnAPNoiseProfileUpdatedToPass": bsnAPNoiseProfileUpdatedToPass,
       "bsnAPInterferenceProfileUpdatedToPass": bsnAPInterferenceProfileUpdatedToPass,
       "bsnAPCoverageProfileUpdatedToPass": bsnAPCoverageProfileUpdatedToPass,
       "bsnRogueAPRemoved": bsnRogueAPRemoved,
       "bsnRadiosExceedLicenseCount": bsnRadiosExceedLicenseCount,
       "bsnSensedTemperatureTooHigh": bsnSensedTemperatureTooHigh,
       "bsnSensedTemperatureTooLow": bsnSensedTemperatureTooLow,
       "bsnTemperatureSensorFailure": bsnTemperatureSensorFailure,
       "bsnTemperatureSensorClear": bsnTemperatureSensorClear,
       "bsnPOEControllerFailure": bsnPOEControllerFailure,
       "bsnMaxRogueCountExceeded": bsnMaxRogueCountExceeded,
       "bsnMaxRogueCountClear": bsnMaxRogueCountClear,
       "bsnApMaxRogueCountExceeded": bsnApMaxRogueCountExceeded,
       "bsnApMaxRogueCountClear": bsnApMaxRogueCountClear,
       "bsnDot11StationBlacklisted": bsnDot11StationBlacklisted,
       "bsnDot11StationAssociate": bsnDot11StationAssociate,
       "bsnApBigNavDosAttack": bsnApBigNavDosAttack,
       "bsnTooManyUnsuccessLoginAttempts": bsnTooManyUnsuccessLoginAttempts,
       "bsnWepKeyDecryptError": bsnWepKeyDecryptError,
       "bsnWpaMicErrorCounterActivated": bsnWpaMicErrorCounterActivated,
       "bsnRogueAPDetectedOnWiredNetwork": bsnRogueAPDetectedOnWiredNetwork,
       "bsnApHasNoRadioCards": bsnApHasNoRadioCards,
       "bsnDuplicateIpAddressReported": bsnDuplicateIpAddressReported,
       "bsnAPContainedAsARogue": bsnAPContainedAsARogue,
       "bsnTrustedApHasInvalidSsid": bsnTrustedApHasInvalidSsid,
       "bsnTrustedApIsMissing": bsnTrustedApIsMissing,
       "bsnAdhocRogueAutoContained": bsnAdhocRogueAutoContained,
       "bsnRogueApAutoContained": bsnRogueApAutoContained,
       "bsnTrustedApHasInvalidEncryption": bsnTrustedApHasInvalidEncryption,
       "bsnTrustedApHasInvalidRadioPolicy": bsnTrustedApHasInvalidRadioPolicy,
       "bsnNetworkStateChanged": bsnNetworkStateChanged,
       "bsnSignatureAttackDetected": bsnSignatureAttackDetected,
       "bsnAPRadioCardTxFailure": bsnAPRadioCardTxFailure,
       "bsnAPRadioCardTxFailureClear": bsnAPRadioCardTxFailureClear,
       "bsnAPRadioCardRxFailure": bsnAPRadioCardRxFailure,
       "bsnAPRadioCardRxFailureClear": bsnAPRadioCardRxFailureClear,
       "bsnAPImpersonationDetected": bsnAPImpersonationDetected,
       "bsnTrustedApHasInvalidPreamble": bsnTrustedApHasInvalidPreamble,
       "bsnAPIPAddressFallback": bsnAPIPAddressFallback,
       "bsnAPFunctionalityDisabled": bsnAPFunctionalityDisabled,
       "bsnAPRegulatoryDomainMismatch": bsnAPRegulatoryDomainMismatch,
       "bsnRxMulticastQueueFull": bsnRxMulticastQueueFull,
       "bsnRadarChannelDetected": bsnRadarChannelDetected,
       "bsnRadarChannelCleared": bsnRadarChannelCleared,
       "bsnAPAuthorizationFailure": bsnAPAuthorizationFailure,
       "radioCoreDumpTrap": radioCoreDumpTrap,
       "invalidRadioTrap": invalidRadioTrap,
       "countryChangeTrap": countryChangeTrap,
       "unsupportedAPTrap": unsupportedAPTrap,
       "heartbeatLossTrap": heartbeatLossTrap,
       "locationNotifyTrap": locationNotifyTrap,
       "bsnUtility": bsnUtility,
       "bsnSyslog": bsnSyslog,
       "bsnSyslogEnable": bsnSyslogEnable,
       "bsnSyslogRemoteAddress": bsnSyslogRemoteAddress,
       "bsnPing": bsnPing,
       "bsnPingTestTable": bsnPingTestTable,
       "bsnPingTestEntry": bsnPingTestEntry,
       "bsnPingTestId": bsnPingTestId,
       "bsnPingTestIPAddress": bsnPingTestIPAddress,
       "bsnPingTestSendCount": bsnPingTestSendCount,
       "bsnPingTestReceivedCount": bsnPingTestReceivedCount,
       "bsnPingTestStatus": bsnPingTestStatus,
       "bsnPingTestMaxTimeInterval": bsnPingTestMaxTimeInterval,
       "bsnPingTestMinTimeInterval": bsnPingTestMinTimeInterval,
       "bsnPingTestAvgTimeInterval": bsnPingTestAvgTimeInterval,
       "bsnPingTestRowStatus": bsnPingTestRowStatus,
       "bsnLinkTest": bsnLinkTest,
       "bsnLinkTestTable": bsnLinkTestTable,
       "bsnLinkTestEntry": bsnLinkTestEntry,
       "bsnLinkTestId": bsnLinkTestId,
       "bsnLinkTestMacAddress": bsnLinkTestMacAddress,
       "bsnLinkTestSendPktCount": bsnLinkTestSendPktCount,
       "bsnLinkTestSendPktLength": bsnLinkTestSendPktLength,
       "bsnLinkTestReceivedPktCount": bsnLinkTestReceivedPktCount,
       "bsnLinkTestClientRSSI": bsnLinkTestClientRSSI,
       "bsnLinkTestLocalSNR": bsnLinkTestLocalSNR,
       "bsnLinkTestLocalRSSI": bsnLinkTestLocalRSSI,
       "bsnLinkTestStatus": bsnLinkTestStatus,
       "bsnLinkTestRowStatus": bsnLinkTestRowStatus,
       "bsnMobility": bsnMobility,
       "bsnMobilityConfig": bsnMobilityConfig,
       "bsnMobilityProtocolPortNum": bsnMobilityProtocolPortNum,
       "bsnMobilityDynamicDiscovery": bsnMobilityDynamicDiscovery,
       "bsnMobilityStatsReset": bsnMobilityStatsReset,
       "bsnMobilityGroupMembersTable": bsnMobilityGroupMembersTable,
       "bsnMobilityGroupMembersEntry": bsnMobilityGroupMembersEntry,
       "bsnMobilityGroupMemberMacAddress": bsnMobilityGroupMemberMacAddress,
       "bsnMobilityGroupMemberIPAddress": bsnMobilityGroupMemberIPAddress,
       "bsnMobilityGroupMemberGroupName": bsnMobilityGroupMemberGroupName,
       "bsnMobilityGroupMemberRowStatus": bsnMobilityGroupMemberRowStatus,
       "bsnMobilityAnchorsTable": bsnMobilityAnchorsTable,
       "bsnMobilityAnchorsEntry": bsnMobilityAnchorsEntry,
       "bsnMobilityAnchorWlanSsid": bsnMobilityAnchorWlanSsid,
       "bsnMobilityAnchorSwitchIPAddress": bsnMobilityAnchorSwitchIPAddress,
       "bsnMobilityAnchorRowStatus": bsnMobilityAnchorRowStatus,
       "bsnMobilityStats": bsnMobilityStats,
       "bsnTotalHandoffRequests": bsnTotalHandoffRequests,
       "bsnTotalHandoffs": bsnTotalHandoffs,
       "bsnCurrentExportedClients": bsnCurrentExportedClients,
       "bsnTotalExportedClients": bsnTotalExportedClients,
       "bsnCurrentImportedClients": bsnCurrentImportedClients,
       "bsnTotalImportedClients": bsnTotalImportedClients,
       "bsnTotalHandoffErrors": bsnTotalHandoffErrors,
       "bsnTotalCommunicationErrors": bsnTotalCommunicationErrors,
       "bsnMobilityGroupDirectoryTable": bsnMobilityGroupDirectoryTable,
       "bsnMobilityGroupDirectoryEntry": bsnMobilityGroupDirectoryEntry,
       "bsnGroupDirectoryMemberIPAddress": bsnGroupDirectoryMemberIPAddress,
       "bsnGroupDirectoryMemberMacAddress": bsnGroupDirectoryMemberMacAddress,
       "bsnGroupDirectoryDicoveryType": bsnGroupDirectoryDicoveryType,
       "bsnMemberCurrentAnchoredClients": bsnMemberCurrentAnchoredClients,
       "bsnMemberTotalAnchoredClients": bsnMemberTotalAnchoredClients,
       "bsnMemberCurrentExportedClients": bsnMemberCurrentExportedClients,
       "bsnMemberTotalExportedClients": bsnMemberTotalExportedClients,
       "bsnMemberCurrentImportedClients": bsnMemberCurrentImportedClients,
       "bsnMemberTotalImportedClients": bsnMemberTotalImportedClients,
       "bsnMemberTotalHandoffErrors": bsnMemberTotalHandoffErrors,
       "bsnMemberTotalCommunicationErrors": bsnMemberTotalCommunicationErrors,
       "bsnTotalReceiveErrors": bsnTotalReceiveErrors,
       "bsnTotalTransmitErrors": bsnTotalTransmitErrors,
       "bsnTotalResponsesRetransmitted": bsnTotalResponsesRetransmitted,
       "bsnTotalHandoffEndRequestsReceived": bsnTotalHandoffEndRequestsReceived,
       "bsnTotalStateTransitionsDisallowed": bsnTotalStateTransitionsDisallowed,
       "bsnTotalResourceErrors": bsnTotalResourceErrors,
       "bsnTotalHandoffRequestsSent": bsnTotalHandoffRequestsSent,
       "bsnTotalHandoffRepliesReceived": bsnTotalHandoffRepliesReceived,
       "bsnTotalHandoffAsLocalReceived": bsnTotalHandoffAsLocalReceived,
       "bsnTotalHandoffAsForeignReceived": bsnTotalHandoffAsForeignReceived,
       "bsnTotalHandoffDeniesReceived": bsnTotalHandoffDeniesReceived,
       "bsnTotalAnchorRequestsSent": bsnTotalAnchorRequestsSent,
       "bsnTotalAnchorDenyReceived": bsnTotalAnchorDenyReceived,
       "bsnTotalAnchorGrantReceived": bsnTotalAnchorGrantReceived,
       "bsnTotalAnchorTransferReceived": bsnTotalAnchorTransferReceived,
       "bsnTotalHandoffRequestsIgnored": bsnTotalHandoffRequestsIgnored,
       "bsnTotalPingPongHandoffRequestsDropped": bsnTotalPingPongHandoffRequestsDropped,
       "bsnTotalHandoffRequestsDropped": bsnTotalHandoffRequestsDropped,
       "bsnTotalHandoffRequestsDenied": bsnTotalHandoffRequestsDenied,
       "bsnTotalClientHandoffAsLocal": bsnTotalClientHandoffAsLocal,
       "bsnTotalClientHandoffAsForeign": bsnTotalClientHandoffAsForeign,
       "bsnTotalAnchorRequestsReceived": bsnTotalAnchorRequestsReceived,
       "bsnTotalAnchorRequestsDenied": bsnTotalAnchorRequestsDenied,
       "bsnTotalAnchorRequestsGranted": bsnTotalAnchorRequestsGranted,
       "bsnTotalAnchorTransferred": bsnTotalAnchorTransferred,
       "bsnTotalHandoffRequestsReceived": bsnTotalHandoffRequestsReceived,
       "bsnIpsec": bsnIpsec,
       "bsnWrasIpsecCACertificate": bsnWrasIpsecCACertificate,
       "bsnWrasIpsecCACertificateUpdate": bsnWrasIpsecCACertificateUpdate,
       "bsnWrasIpsecCertTable": bsnWrasIpsecCertTable,
       "bsnWrasIpsecCertEntry": bsnWrasIpsecCertEntry,
       "bsnWrasIpsecCertName": bsnWrasIpsecCertName,
       "bsnWrasIpsecCertificateUpdate": bsnWrasIpsecCertificateUpdate,
       "bsnWrasIpsecCertificate": bsnWrasIpsecCertificate,
       "bsnWrasIpsecCertPassword": bsnWrasIpsecCertPassword,
       "bsnWrasIpsecCertStatus": bsnWrasIpsecCertStatus,
       "bsnAPGroupsVlanConfig": bsnAPGroupsVlanConfig,
       "bsnAPGroupsVlanFeature": bsnAPGroupsVlanFeature,
       "bsnAPGroupsVlanTable": bsnAPGroupsVlanTable,
       "bsnAPGroupsVlanEntry": bsnAPGroupsVlanEntry,
       "bsnAPGroupsVlanName": bsnAPGroupsVlanName,
       "bsnAPGroupsVlanDescription": bsnAPGroupsVlanDescription,
       "bsnAPGroupsVlanRowStatus": bsnAPGroupsVlanRowStatus,
       "bsnAPGroupsVlanMappingTable": bsnAPGroupsVlanMappingTable,
       "bsnAPGroupsVlanMappingEntry": bsnAPGroupsVlanMappingEntry,
       "bsnAPGroupsVlanMappingSsid": bsnAPGroupsVlanMappingSsid,
       "bsnAPGroupsVlanMappingInterfaceName": bsnAPGroupsVlanMappingInterfaceName,
       "bsnAPGroupsVlanMappingRowStatus": bsnAPGroupsVlanMappingRowStatus,
       "bsnWrasGroups": bsnWrasGroups,
       "bsnEssGroup": bsnEssGroup,
       "bsnApGroup": bsnApGroup,
       "bsnGlobalDot11Group": bsnGlobalDot11Group,
       "bsnRrmGroup": bsnRrmGroup,
       "bsnAAAGroup": bsnAAAGroup,
       "bsnTrapsGroup": bsnTrapsGroup,
       "bsnUtilityGroup": bsnUtilityGroup,
       "bsnMobilityGroup": bsnMobilityGroup,
       "bsnIpsecGroup": bsnIpsecGroup,
       "bsnWrasDepGroup": bsnWrasDepGroup,
       "bsnWrasObsGroup": bsnWrasObsGroup,
       "bsnWrasTrap": bsnWrasTrap,
       "bsnEssGroupRev1": bsnEssGroupRev1,
       "bsnGlobalDot11GroupRev1": bsnGlobalDot11GroupRev1,
       "bsnAAAGroupRev1": bsnAAAGroupRev1,
       "bsnTrapsGroupRev1": bsnTrapsGroupRev1,
       "bsnWrasTrapRev1": bsnWrasTrapRev1,
       "bsnApGroupRev1": bsnApGroupRev1,
       "bsnUtilityGroupRev1": bsnUtilityGroupRev1,
       "bsnWrasObsGroupRev1": bsnWrasObsGroupRev1,
       "bsnWrasObsTrap": bsnWrasObsTrap,
       "bsnWrasCompliances": bsnWrasCompliances,
       "bsnWrasCompliance": bsnWrasCompliance,
       "bsnWrasComplianceRev1": bsnWrasComplianceRev1}
)
