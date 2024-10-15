# SNMP MIB module (CISCO-LWAPP-WLAN-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-WLAN-SECURITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:09 2024
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

(CLSecEncryptType,
 CLSecKeyFormat) = mibBuilder.importSymbols(
    "CISCO-LWAPP-TC-MIB",
    "CLSecEncryptType",
    "CLSecKeyFormat")

(cLWlanIndex,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-WLAN-MIB",
    "cLWlanIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappWlanSecurityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 521)
)
ciscoLwappWlanSecurityMIB.setRevisions(
        ("2015-06-03 00:00",
         "2008-01-15 00:00",
         "2007-11-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappWlanSecurityMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappWlanSecurityMIBNotifs = _CiscoLwappWlanSecurityMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 0)
)
_CiscoLwappWlanSecurityMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappWlanSecurityMIBObjects = _CiscoLwappWlanSecurityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1)
)
_ClwsCckmConfig_ObjectIdentity = ObjectIdentity
clwsCckmConfig = _ClwsCckmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1)
)
_CLWSecDot11EssCckmTable_Object = MibTable
cLWSecDot11EssCckmTable = _CLWSecDot11EssCckmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cLWSecDot11EssCckmTable.setStatus("current")
_CLWSecDot11EssCckmEntry_Object = MibTableRow
cLWSecDot11EssCckmEntry = _CLWSecDot11EssCckmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1)
)
cLWSecDot11EssCckmEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLWSecDot11EssCckmEntry.setStatus("current")


class _CLWSecDot11EssCckmWpaSupport_Type(TruthValue):
    """Custom type cLWSecDot11EssCckmWpaSupport based on TruthValue"""


_CLWSecDot11EssCckmWpaSupport_Object = MibTableColumn
cLWSecDot11EssCckmWpaSupport = _CLWSecDot11EssCckmWpaSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 1),
    _CLWSecDot11EssCckmWpaSupport_Type()
)
cLWSecDot11EssCckmWpaSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssCckmWpaSupport.setStatus("current")


class _CLWSecDot11EssCckmWpa1Security_Type(TruthValue):
    """Custom type cLWSecDot11EssCckmWpa1Security based on TruthValue"""


_CLWSecDot11EssCckmWpa1Security_Object = MibTableColumn
cLWSecDot11EssCckmWpa1Security = _CLWSecDot11EssCckmWpa1Security_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 2),
    _CLWSecDot11EssCckmWpa1Security_Type()
)
cLWSecDot11EssCckmWpa1Security.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssCckmWpa1Security.setStatus("current")


class _CLWSecDot11EssCckmWpa1EncType_Type(CLSecEncryptType):
    """Custom type cLWSecDot11EssCckmWpa1EncType based on CLSecEncryptType"""
    defaultBinValue = "0"


_CLWSecDot11EssCckmWpa1EncType_Object = MibTableColumn
cLWSecDot11EssCckmWpa1EncType = _CLWSecDot11EssCckmWpa1EncType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 3),
    _CLWSecDot11EssCckmWpa1EncType_Type()
)
cLWSecDot11EssCckmWpa1EncType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssCckmWpa1EncType.setStatus("current")


class _CLWSecDot11EssCckmWpa2Security_Type(TruthValue):
    """Custom type cLWSecDot11EssCckmWpa2Security based on TruthValue"""


_CLWSecDot11EssCckmWpa2Security_Object = MibTableColumn
cLWSecDot11EssCckmWpa2Security = _CLWSecDot11EssCckmWpa2Security_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 4),
    _CLWSecDot11EssCckmWpa2Security_Type()
)
cLWSecDot11EssCckmWpa2Security.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssCckmWpa2Security.setStatus("current")


class _CLWSecDot11EssCckmWpa2EncType_Type(CLSecEncryptType):
    """Custom type cLWSecDot11EssCckmWpa2EncType based on CLSecEncryptType"""
    defaultBinValue = "0"


_CLWSecDot11EssCckmWpa2EncType_Object = MibTableColumn
cLWSecDot11EssCckmWpa2EncType = _CLWSecDot11EssCckmWpa2EncType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 5),
    _CLWSecDot11EssCckmWpa2EncType_Type()
)
cLWSecDot11EssCckmWpa2EncType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssCckmWpa2EncType.setStatus("current")


class _CLWSecDot11EssCckmKeyMgmtMode_Type(Bits):
    """Custom type cLWSecDot11EssCckmKeyMgmtMode based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("cckm", 1),
          ("dot1x", 0),
          ("ftDot1x", 3),
          ("ftPsk", 4),
          ("pfmDot1x", 5),
          ("pfmPsk", 6),
          ("psk", 2))
    )

_CLWSecDot11EssCckmKeyMgmtMode_Type.__name__ = "Bits"
_CLWSecDot11EssCckmKeyMgmtMode_Object = MibTableColumn
cLWSecDot11EssCckmKeyMgmtMode = _CLWSecDot11EssCckmKeyMgmtMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 6),
    _CLWSecDot11EssCckmKeyMgmtMode_Type()
)
cLWSecDot11EssCckmKeyMgmtMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssCckmKeyMgmtMode.setStatus("current")


class _CLWSecDot11EssPskFmt_Type(CLSecKeyFormat):
    """Custom type cLWSecDot11EssPskFmt based on CLSecKeyFormat"""


_CLWSecDot11EssPskFmt_Object = MibTableColumn
cLWSecDot11EssPskFmt = _CLWSecDot11EssPskFmt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 7),
    _CLWSecDot11EssPskFmt_Type()
)
cLWSecDot11EssPskFmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssPskFmt.setStatus("current")


class _CLWSecDot11EssPsk_Type(OctetString):
    """Custom type cLWSecDot11EssPsk based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 64),
    )


_CLWSecDot11EssPsk_Type.__name__ = "OctetString"
_CLWSecDot11EssPsk_Object = MibTableColumn
cLWSecDot11EssPsk = _CLWSecDot11EssPsk_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 8),
    _CLWSecDot11EssPsk_Type()
)
cLWSecDot11EssPsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssPsk.setStatus("current")
_CLWSecDot11EssCckmGtkRandomize_Type = TruthValue
_CLWSecDot11EssCckmGtkRandomize_Object = MibTableColumn
cLWSecDot11EssCckmGtkRandomize = _CLWSecDot11EssCckmGtkRandomize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 9),
    _CLWSecDot11EssCckmGtkRandomize_Type()
)
cLWSecDot11EssCckmGtkRandomize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssCckmGtkRandomize.setStatus("current")
_CLWSecDot11EssFtEnable_Type = TruthValue
_CLWSecDot11EssFtEnable_Object = MibTableColumn
cLWSecDot11EssFtEnable = _CLWSecDot11EssFtEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 10),
    _CLWSecDot11EssFtEnable_Type()
)
cLWSecDot11EssFtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssFtEnable.setStatus("current")
_CLWSecDot11EssFtReassocTime_Type = Unsigned32
_CLWSecDot11EssFtReassocTime_Object = MibTableColumn
cLWSecDot11EssFtReassocTime = _CLWSecDot11EssFtReassocTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 11),
    _CLWSecDot11EssFtReassocTime_Type()
)
cLWSecDot11EssFtReassocTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssFtReassocTime.setStatus("current")
if mibBuilder.loadTexts:
    cLWSecDot11EssFtReassocTime.setUnits("seconds")
_CLWSecDot11EssFtOverDs_Type = TruthValue
_CLWSecDot11EssFtOverDs_Object = MibTableColumn
cLWSecDot11EssFtOverDs = _CLWSecDot11EssFtOverDs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 12),
    _CLWSecDot11EssFtOverDs_Type()
)
cLWSecDot11EssFtOverDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssFtOverDs.setStatus("current")


class _CLWSecDot11Ess11wPfm_Type(Integer32):
    """Custom type cLWSecDot11Ess11wPfm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("optional", 2),
          ("required", 3))
    )


_CLWSecDot11Ess11wPfm_Type.__name__ = "Integer32"
_CLWSecDot11Ess11wPfm_Object = MibTableColumn
cLWSecDot11Ess11wPfm = _CLWSecDot11Ess11wPfm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 13),
    _CLWSecDot11Ess11wPfm_Type()
)
cLWSecDot11Ess11wPfm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11Ess11wPfm.setStatus("current")
_CLWSecDot11EssRetryTime_Type = Unsigned32
_CLWSecDot11EssRetryTime_Object = MibTableColumn
cLWSecDot11EssRetryTime = _CLWSecDot11EssRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 14),
    _CLWSecDot11EssRetryTime_Type()
)
cLWSecDot11EssRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssRetryTime.setStatus("current")
if mibBuilder.loadTexts:
    cLWSecDot11EssRetryTime.setUnits("milliseconds")
_CLWSecDot11EssComebackTime_Type = Unsigned32
_CLWSecDot11EssComebackTime_Object = MibTableColumn
cLWSecDot11EssComebackTime = _CLWSecDot11EssComebackTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 15),
    _CLWSecDot11EssComebackTime_Type()
)
cLWSecDot11EssComebackTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssComebackTime.setStatus("current")
if mibBuilder.loadTexts:
    cLWSecDot11EssComebackTime.setUnits("seconds")
_CLWSecDot11EssCkipTable_Object = MibTable
cLWSecDot11EssCkipTable = _CLWSecDot11EssCkipTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cLWSecDot11EssCkipTable.setStatus("current")
_CLWSecDot11EssCkipEntry_Object = MibTableRow
cLWSecDot11EssCkipEntry = _CLWSecDot11EssCkipEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 2, 1)
)
cLWSecDot11EssCkipEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLWSecDot11EssCkipEntry.setStatus("current")


class _CLWSecDot11EssCkipSecurity_Type(TruthValue):
    """Custom type cLWSecDot11EssCkipSecurity based on TruthValue"""


_CLWSecDot11EssCkipSecurity_Object = MibTableColumn
cLWSecDot11EssCkipSecurity = _CLWSecDot11EssCkipSecurity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 2, 1, 1),
    _CLWSecDot11EssCkipSecurity_Type()
)
cLWSecDot11EssCkipSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssCkipSecurity.setStatus("current")


class _CLWSecDot11EssCkipKeyIndex_Type(Unsigned32):
    """Custom type cLWSecDot11EssCkipKeyIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_CLWSecDot11EssCkipKeyIndex_Type.__name__ = "Unsigned32"
_CLWSecDot11EssCkipKeyIndex_Object = MibTableColumn
cLWSecDot11EssCkipKeyIndex = _CLWSecDot11EssCkipKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 2, 1, 2),
    _CLWSecDot11EssCkipKeyIndex_Type()
)
cLWSecDot11EssCkipKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssCkipKeyIndex.setStatus("current")


class _CLWSecDot11EssCkipKeyLength_Type(Integer32):
    """Custom type cLWSecDot11EssCkipKeyLength based on Integer32"""
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
        *(("len104", 3),
          ("len40", 2),
          ("none", 1))
    )


_CLWSecDot11EssCkipKeyLength_Type.__name__ = "Integer32"
_CLWSecDot11EssCkipKeyLength_Object = MibTableColumn
cLWSecDot11EssCkipKeyLength = _CLWSecDot11EssCkipKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 2, 1, 3),
    _CLWSecDot11EssCkipKeyLength_Type()
)
cLWSecDot11EssCkipKeyLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssCkipKeyLength.setStatus("current")


class _CLWSecDot11EssCkipKeyFmt_Type(CLSecKeyFormat):
    """Custom type cLWSecDot11EssCkipKeyFmt based on CLSecKeyFormat"""


_CLWSecDot11EssCkipKeyFmt_Object = MibTableColumn
cLWSecDot11EssCkipKeyFmt = _CLWSecDot11EssCkipKeyFmt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 2, 1, 4),
    _CLWSecDot11EssCkipKeyFmt_Type()
)
cLWSecDot11EssCkipKeyFmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssCkipKeyFmt.setStatus("current")


class _CLWSecDot11EssCkipKey_Type(OctetString):
    """Custom type cLWSecDot11EssCkipKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 26),
    )


_CLWSecDot11EssCkipKey_Type.__name__ = "OctetString"
_CLWSecDot11EssCkipKey_Object = MibTableColumn
cLWSecDot11EssCkipKey = _CLWSecDot11EssCkipKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 2, 1, 5),
    _CLWSecDot11EssCkipKey_Type()
)
cLWSecDot11EssCkipKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssCkipKey.setStatus("current")


class _CLWSecDot11EssCkipMMHMode_Type(TruthValue):
    """Custom type cLWSecDot11EssCkipMMHMode based on TruthValue"""


_CLWSecDot11EssCkipMMHMode_Object = MibTableColumn
cLWSecDot11EssCkipMMHMode = _CLWSecDot11EssCkipMMHMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 2, 1, 6),
    _CLWSecDot11EssCkipMMHMode_Type()
)
cLWSecDot11EssCkipMMHMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssCkipMMHMode.setStatus("current")


class _CLWSecDot11EssCkipKPEnable_Type(TruthValue):
    """Custom type cLWSecDot11EssCkipKPEnable based on TruthValue"""


_CLWSecDot11EssCkipKPEnable_Object = MibTableColumn
cLWSecDot11EssCkipKPEnable = _CLWSecDot11EssCkipKPEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 2, 1, 7),
    _CLWSecDot11EssCkipKPEnable_Type()
)
cLWSecDot11EssCkipKPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssCkipKPEnable.setStatus("current")
_ClwsCkipConfig_ObjectIdentity = ObjectIdentity
clwsCkipConfig = _ClwsCkipConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 2)
)
_ClwsWebPolicyConfig_ObjectIdentity = ObjectIdentity
clwsWebPolicyConfig = _ClwsWebPolicyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 3)
)
_CLWSecDot11EssWebPolicyTable_Object = MibTable
cLWSecDot11EssWebPolicyTable = _CLWSecDot11EssWebPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cLWSecDot11EssWebPolicyTable.setStatus("current")
_CLWSecDot11EssWebPolicyEntry_Object = MibTableRow
cLWSecDot11EssWebPolicyEntry = _CLWSecDot11EssWebPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 3, 1, 1)
)
cLWSecDot11EssWebPolicyEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLWSecDot11EssWebPolicyEntry.setStatus("current")


class _CLWSecDot11EssWebPolicyCondRedirect_Type(TruthValue):
    """Custom type cLWSecDot11EssWebPolicyCondRedirect based on TruthValue"""


_CLWSecDot11EssWebPolicyCondRedirect_Object = MibTableColumn
cLWSecDot11EssWebPolicyCondRedirect = _CLWSecDot11EssWebPolicyCondRedirect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 3, 1, 1, 1),
    _CLWSecDot11EssWebPolicyCondRedirect_Type()
)
cLWSecDot11EssWebPolicyCondRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssWebPolicyCondRedirect.setStatus("current")


class _CLWSecDot11EssWebPolicySplashPageWebRedirect_Type(TruthValue):
    """Custom type cLWSecDot11EssWebPolicySplashPageWebRedirect based on TruthValue"""


_CLWSecDot11EssWebPolicySplashPageWebRedirect_Object = MibTableColumn
cLWSecDot11EssWebPolicySplashPageWebRedirect = _CLWSecDot11EssWebPolicySplashPageWebRedirect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 3, 1, 1, 2),
    _CLWSecDot11EssWebPolicySplashPageWebRedirect_Type()
)
cLWSecDot11EssWebPolicySplashPageWebRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssWebPolicySplashPageWebRedirect.setStatus("current")
_ClwsAaaConfig_ObjectIdentity = ObjectIdentity
clwsAaaConfig = _ClwsAaaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 4)
)


class _CLWSecAaaRadiusAuthCallStationIdType_Type(Integer32):
    """Custom type cLWSecAaaRadiusAuthCallStationIdType based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("apGroupName", 7),
          ("apLabelAddress", 12),
          ("apLabelAddressSsid", 13),
          ("apLocation", 8),
          ("apMacAddress", 3),
          ("apMacAddressSsid", 4),
          ("apMacEthAddress", 10),
          ("apMacEthAddressSsid", 11),
          ("apName", 6),
          ("apNameSsid", 5),
          ("apVlanId", 9),
          ("ipAddr", 1),
          ("macAddr", 2))
    )


_CLWSecAaaRadiusAuthCallStationIdType_Type.__name__ = "Integer32"
_CLWSecAaaRadiusAuthCallStationIdType_Object = MibScalar
cLWSecAaaRadiusAuthCallStationIdType = _CLWSecAaaRadiusAuthCallStationIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 4, 1),
    _CLWSecAaaRadiusAuthCallStationIdType_Type()
)
cLWSecAaaRadiusAuthCallStationIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecAaaRadiusAuthCallStationIdType.setStatus("current")


class _CLWSecAaaRadiusAccUsernameDelimiter_Type(Integer32):
    """Custom type cLWSecAaaRadiusAccUsernameDelimiter based on Integer32"""
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
        *(("colon", 3),
          ("hyphen", 2),
          ("noDelimiter", 1),
          ("singleHyphen", 4))
    )


_CLWSecAaaRadiusAccUsernameDelimiter_Type.__name__ = "Integer32"
_CLWSecAaaRadiusAccUsernameDelimiter_Object = MibScalar
cLWSecAaaRadiusAccUsernameDelimiter = _CLWSecAaaRadiusAccUsernameDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 4, 2),
    _CLWSecAaaRadiusAccUsernameDelimiter_Type()
)
cLWSecAaaRadiusAccUsernameDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecAaaRadiusAccUsernameDelimiter.setStatus("current")
_CiscoLwappWlanSecurityMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappWlanSecurityMIBConform = _CiscoLwappWlanSecurityMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2)
)
_CiscoLwappWlanSecurityMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappWlanSecurityMIBCompliances = _CiscoLwappWlanSecurityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 1)
)
_CiscoLwappWlanSecurityMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappWlanSecurityMIBGroups = _CiscoLwappWlanSecurityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 2)
)

# Managed Objects groups

ciscoLwappWlanSecurityCckmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 2, 1)
)
ciscoLwappWlanSecurityCckmConfigGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCckmWpaSupport"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCckmWpa1Security"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCckmWpa1EncType"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCckmWpa2Security"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCckmWpa2EncType"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCckmKeyMgmtMode"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssPskFmt"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssPsk"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanSecurityCckmConfigGroup.setStatus("current")

ciscoLwappWlanSecurityCkipConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 2, 2)
)
ciscoLwappWlanSecurityCkipConfigGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCkipSecurity"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCkipKeyIndex"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCkipKeyLength"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCkipKeyFmt"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCkipKey"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCkipMMHMode"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCkipKPEnable"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanSecurityCkipConfigGroup.setStatus("current")

ciscoLwappWlanSecurityWebPolicyConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 2, 3)
)
ciscoLwappWlanSecurityWebPolicyConfigGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssWebPolicyCondRedirect"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssWebPolicySplashPageWebRedirect"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanSecurityWebPolicyConfigGroup.setStatus("current")

ciscoLwappWlanSecurityAaaConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 2, 4)
)
ciscoLwappWlanSecurityAaaConfigGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecAaaRadiusAuthCallStationIdType"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecAaaRadiusAccUsernameDelimiter"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanSecurityAaaConfigGroup.setStatus("current")

ciscoLwappWlanSecurityFtConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 2, 5)
)
ciscoLwappWlanSecurityFtConfigGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssFtEnable"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssFtReassocTime"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssFtOverDs"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanSecurityFtConfigGroup.setStatus("current")

ciscoLwappWlanSecurityPfmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 2, 6)
)
ciscoLwappWlanSecurityPfmConfigGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11Ess11wPfm"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssRetryTime"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssComebackTime"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanSecurityPfmConfigGroup.setStatus("current")

ciscoLwappWlanSecurityCckmConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 2, 7)
)
ciscoLwappWlanSecurityCckmConfigGroup1.setObjects(
    ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCckmGtkRandomize")
)
if mibBuilder.loadTexts:
    ciscoLwappWlanSecurityCckmConfigGroup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappWlanSecurityMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappWlanSecurityMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappWlanSecurityMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappWlanSecurityMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoLwappWlanSecurityMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoLwappWlanSecurityMIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-WLAN-SECURITY-MIB",
    **{"ciscoLwappWlanSecurityMIB": ciscoLwappWlanSecurityMIB,
       "ciscoLwappWlanSecurityMIBNotifs": ciscoLwappWlanSecurityMIBNotifs,
       "ciscoLwappWlanSecurityMIBObjects": ciscoLwappWlanSecurityMIBObjects,
       "clwsCckmConfig": clwsCckmConfig,
       "cLWSecDot11EssCckmTable": cLWSecDot11EssCckmTable,
       "cLWSecDot11EssCckmEntry": cLWSecDot11EssCckmEntry,
       "cLWSecDot11EssCckmWpaSupport": cLWSecDot11EssCckmWpaSupport,
       "cLWSecDot11EssCckmWpa1Security": cLWSecDot11EssCckmWpa1Security,
       "cLWSecDot11EssCckmWpa1EncType": cLWSecDot11EssCckmWpa1EncType,
       "cLWSecDot11EssCckmWpa2Security": cLWSecDot11EssCckmWpa2Security,
       "cLWSecDot11EssCckmWpa2EncType": cLWSecDot11EssCckmWpa2EncType,
       "cLWSecDot11EssCckmKeyMgmtMode": cLWSecDot11EssCckmKeyMgmtMode,
       "cLWSecDot11EssPskFmt": cLWSecDot11EssPskFmt,
       "cLWSecDot11EssPsk": cLWSecDot11EssPsk,
       "cLWSecDot11EssCckmGtkRandomize": cLWSecDot11EssCckmGtkRandomize,
       "cLWSecDot11EssFtEnable": cLWSecDot11EssFtEnable,
       "cLWSecDot11EssFtReassocTime": cLWSecDot11EssFtReassocTime,
       "cLWSecDot11EssFtOverDs": cLWSecDot11EssFtOverDs,
       "cLWSecDot11Ess11wPfm": cLWSecDot11Ess11wPfm,
       "cLWSecDot11EssRetryTime": cLWSecDot11EssRetryTime,
       "cLWSecDot11EssComebackTime": cLWSecDot11EssComebackTime,
       "cLWSecDot11EssCkipTable": cLWSecDot11EssCkipTable,
       "cLWSecDot11EssCkipEntry": cLWSecDot11EssCkipEntry,
       "cLWSecDot11EssCkipSecurity": cLWSecDot11EssCkipSecurity,
       "cLWSecDot11EssCkipKeyIndex": cLWSecDot11EssCkipKeyIndex,
       "cLWSecDot11EssCkipKeyLength": cLWSecDot11EssCkipKeyLength,
       "cLWSecDot11EssCkipKeyFmt": cLWSecDot11EssCkipKeyFmt,
       "cLWSecDot11EssCkipKey": cLWSecDot11EssCkipKey,
       "cLWSecDot11EssCkipMMHMode": cLWSecDot11EssCkipMMHMode,
       "cLWSecDot11EssCkipKPEnable": cLWSecDot11EssCkipKPEnable,
       "clwsCkipConfig": clwsCkipConfig,
       "clwsWebPolicyConfig": clwsWebPolicyConfig,
       "cLWSecDot11EssWebPolicyTable": cLWSecDot11EssWebPolicyTable,
       "cLWSecDot11EssWebPolicyEntry": cLWSecDot11EssWebPolicyEntry,
       "cLWSecDot11EssWebPolicyCondRedirect": cLWSecDot11EssWebPolicyCondRedirect,
       "cLWSecDot11EssWebPolicySplashPageWebRedirect": cLWSecDot11EssWebPolicySplashPageWebRedirect,
       "clwsAaaConfig": clwsAaaConfig,
       "cLWSecAaaRadiusAuthCallStationIdType": cLWSecAaaRadiusAuthCallStationIdType,
       "cLWSecAaaRadiusAccUsernameDelimiter": cLWSecAaaRadiusAccUsernameDelimiter,
       "ciscoLwappWlanSecurityMIBConform": ciscoLwappWlanSecurityMIBConform,
       "ciscoLwappWlanSecurityMIBCompliances": ciscoLwappWlanSecurityMIBCompliances,
       "ciscoLwappWlanSecurityMIBCompliance": ciscoLwappWlanSecurityMIBCompliance,
       "ciscoLwappWlanSecurityMIBComplianceRev1": ciscoLwappWlanSecurityMIBComplianceRev1,
       "ciscoLwappWlanSecurityMIBComplianceRev2": ciscoLwappWlanSecurityMIBComplianceRev2,
       "ciscoLwappWlanSecurityMIBGroups": ciscoLwappWlanSecurityMIBGroups,
       "ciscoLwappWlanSecurityCckmConfigGroup": ciscoLwappWlanSecurityCckmConfigGroup,
       "ciscoLwappWlanSecurityCkipConfigGroup": ciscoLwappWlanSecurityCkipConfigGroup,
       "ciscoLwappWlanSecurityWebPolicyConfigGroup": ciscoLwappWlanSecurityWebPolicyConfigGroup,
       "ciscoLwappWlanSecurityAaaConfigGroup": ciscoLwappWlanSecurityAaaConfigGroup,
       "ciscoLwappWlanSecurityFtConfigGroup": ciscoLwappWlanSecurityFtConfigGroup,
       "ciscoLwappWlanSecurityPfmConfigGroup": ciscoLwappWlanSecurityPfmConfigGroup,
       "ciscoLwappWlanSecurityCckmConfigGroup1": ciscoLwappWlanSecurityCckmConfigGroup1}
)
