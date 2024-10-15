# SNMP MIB module (DOCS-SEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOCS-SEC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:07 2024
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

(clabProjDocsis,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjDocsis")

(docsBpi2CodeDownloadControl,) = mibBuilder.importSymbols(
    "DOCS-IETF-BPI2-MIB",
    "docsBpi2CodeDownloadControl")

(docsIf3CmtsCmRegStatusEntry,
 docsIf3CmtsCmRegStatusId) = mibBuilder.importSymbols(
    "DOCS-IF3-MIB",
    "docsIf3CmtsCmRegStatusEntry",
    "docsIf3CmtsCmRegStatusId")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(SnmpTagList,) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "SnmpTagList")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

docsSecMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11)
)
docsSecMib.setRevisions(
        ("2016-01-13 00:00",
         "2015-03-26 00:00",
         "2010-01-15 00:00",
         "2009-05-29 00:00",
         "2007-02-23 00:00",
         "2006-12-07 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DocsCvcCaCertificateChain(OctetString, TextualConvention):
    status = "current"
    displayHint = "*"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8192),
    )



# MIB Managed Objects in the order of their OIDs

_DocsBpi2CodeUpdateCvcChain_Type = DocsCvcCaCertificateChain
_DocsBpi2CodeUpdateCvcChain_Object = MibScalar
docsBpi2CodeUpdateCvcChain = _DocsBpi2CodeUpdateCvcChain_Object(
    (1, 3, 6, 1, 2, 1, 126, 1, 4, 10),
    _DocsBpi2CodeUpdateCvcChain_Type()
)
docsBpi2CodeUpdateCvcChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsBpi2CodeUpdateCvcChain.setStatus("deprecated")
_DocsSecMibObjects_ObjectIdentity = ObjectIdentity
docsSecMibObjects = _DocsSecMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1)
)
_DocsSecCmtsServerCfg_ObjectIdentity = ObjectIdentity
docsSecCmtsServerCfg = _DocsSecCmtsServerCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 1)
)


class _DocsSecCmtsServerCfgTftpOptions_Type(Bits):
    """Custom type docsSecCmtsServerCfgTftpOptions based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("hwAddr", 0),
          ("netAddr", 1))
    )

_DocsSecCmtsServerCfgTftpOptions_Type.__name__ = "Bits"
_DocsSecCmtsServerCfgTftpOptions_Object = MibScalar
docsSecCmtsServerCfgTftpOptions = _DocsSecCmtsServerCfgTftpOptions_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 1, 1),
    _DocsSecCmtsServerCfgTftpOptions_Type()
)
docsSecCmtsServerCfgTftpOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSecCmtsServerCfgTftpOptions.setStatus("current")


class _DocsSecCmtsServerCfgConfigFileLearningEnable_Type(TruthValue):
    """Custom type docsSecCmtsServerCfgConfigFileLearningEnable based on TruthValue"""


_DocsSecCmtsServerCfgConfigFileLearningEnable_Object = MibScalar
docsSecCmtsServerCfgConfigFileLearningEnable = _DocsSecCmtsServerCfgConfigFileLearningEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 1, 2),
    _DocsSecCmtsServerCfgConfigFileLearningEnable_Type()
)
docsSecCmtsServerCfgConfigFileLearningEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSecCmtsServerCfgConfigFileLearningEnable.setStatus("current")
_DocsSecCmtsEncrypt_ObjectIdentity = ObjectIdentity
docsSecCmtsEncrypt = _DocsSecCmtsEncrypt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 2)
)


class _DocsSecCmtsEncryptEncryptAlgPriority_Type(SnmpTagList):
    """Custom type docsSecCmtsEncryptEncryptAlgPriority based on SnmpTagList"""
    defaultValue = OctetString("aes128CbcMode des56CbcMode des40CbcMode")


_DocsSecCmtsEncryptEncryptAlgPriority_Object = MibScalar
docsSecCmtsEncryptEncryptAlgPriority = _DocsSecCmtsEncryptEncryptAlgPriority_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 2, 1),
    _DocsSecCmtsEncryptEncryptAlgPriority_Type()
)
docsSecCmtsEncryptEncryptAlgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSecCmtsEncryptEncryptAlgPriority.setStatus("current")
_DocsSecCmtsCmEaeExclusionTable_Object = MibTable
docsSecCmtsCmEaeExclusionTable = _DocsSecCmtsCmEaeExclusionTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 3)
)
if mibBuilder.loadTexts:
    docsSecCmtsCmEaeExclusionTable.setStatus("current")
_DocsSecCmtsCmEaeExclusionEntry_Object = MibTableRow
docsSecCmtsCmEaeExclusionEntry = _DocsSecCmtsCmEaeExclusionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 3, 1)
)
docsSecCmtsCmEaeExclusionEntry.setIndexNames(
    (0, "DOCS-SEC-MIB", "docsSecCmtsCmEaeExclusionId"),
)
if mibBuilder.loadTexts:
    docsSecCmtsCmEaeExclusionEntry.setStatus("current")


class _DocsSecCmtsCmEaeExclusionId_Type(Unsigned32):
    """Custom type docsSecCmtsCmEaeExclusionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsSecCmtsCmEaeExclusionId_Type.__name__ = "Unsigned32"
_DocsSecCmtsCmEaeExclusionId_Object = MibTableColumn
docsSecCmtsCmEaeExclusionId = _DocsSecCmtsCmEaeExclusionId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 3, 1, 1),
    _DocsSecCmtsCmEaeExclusionId_Type()
)
docsSecCmtsCmEaeExclusionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsSecCmtsCmEaeExclusionId.setStatus("current")


class _DocsSecCmtsCmEaeExclusionMacAddr_Type(MacAddress):
    """Custom type docsSecCmtsCmEaeExclusionMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_DocsSecCmtsCmEaeExclusionMacAddr_Object = MibTableColumn
docsSecCmtsCmEaeExclusionMacAddr = _DocsSecCmtsCmEaeExclusionMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 3, 1, 2),
    _DocsSecCmtsCmEaeExclusionMacAddr_Type()
)
docsSecCmtsCmEaeExclusionMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSecCmtsCmEaeExclusionMacAddr.setStatus("current")


class _DocsSecCmtsCmEaeExclusionMacAddrMask_Type(MacAddress):
    """Custom type docsSecCmtsCmEaeExclusionMacAddrMask based on MacAddress"""
    defaultHexValue = "FFFFFFFFFFFF"


_DocsSecCmtsCmEaeExclusionMacAddrMask_Object = MibTableColumn
docsSecCmtsCmEaeExclusionMacAddrMask = _DocsSecCmtsCmEaeExclusionMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 3, 1, 3),
    _DocsSecCmtsCmEaeExclusionMacAddrMask_Type()
)
docsSecCmtsCmEaeExclusionMacAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSecCmtsCmEaeExclusionMacAddrMask.setStatus("current")
_DocsSecCmtsCmEaeExclusionRowStatus_Type = RowStatus
_DocsSecCmtsCmEaeExclusionRowStatus_Object = MibTableColumn
docsSecCmtsCmEaeExclusionRowStatus = _DocsSecCmtsCmEaeExclusionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 3, 1, 4),
    _DocsSecCmtsCmEaeExclusionRowStatus_Type()
)
docsSecCmtsCmEaeExclusionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSecCmtsCmEaeExclusionRowStatus.setStatus("current")
_DocsSecCmtsSavControl_ObjectIdentity = ObjectIdentity
docsSecCmtsSavControl = _DocsSecCmtsSavControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 4)
)


class _DocsSecCmtsSavControlCmAuthEnable_Type(TruthValue):
    """Custom type docsSecCmtsSavControlCmAuthEnable based on TruthValue"""


_DocsSecCmtsSavControlCmAuthEnable_Object = MibScalar
docsSecCmtsSavControlCmAuthEnable = _DocsSecCmtsSavControlCmAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 4, 1),
    _DocsSecCmtsSavControlCmAuthEnable_Type()
)
docsSecCmtsSavControlCmAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSecCmtsSavControlCmAuthEnable.setStatus("current")
_DocsSecSavCmAuthTable_Object = MibTable
docsSecSavCmAuthTable = _DocsSecSavCmAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 5)
)
if mibBuilder.loadTexts:
    docsSecSavCmAuthTable.setStatus("current")
_DocsSecSavCmAuthEntry_Object = MibTableRow
docsSecSavCmAuthEntry = _DocsSecSavCmAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 5, 1)
)
docsSecSavCmAuthEntry.setIndexNames(
    (0, "DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusId"),
)
if mibBuilder.loadTexts:
    docsSecSavCmAuthEntry.setStatus("current")
_DocsSecSavCmAuthGrpName_Type = SnmpAdminString
_DocsSecSavCmAuthGrpName_Object = MibTableColumn
docsSecSavCmAuthGrpName = _DocsSecSavCmAuthGrpName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 5, 1, 1),
    _DocsSecSavCmAuthGrpName_Type()
)
docsSecSavCmAuthGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsSecSavCmAuthGrpName.setStatus("current")
_DocsSecSavCmAuthStaticPrefixListId_Type = Unsigned32
_DocsSecSavCmAuthStaticPrefixListId_Object = MibTableColumn
docsSecSavCmAuthStaticPrefixListId = _DocsSecSavCmAuthStaticPrefixListId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 5, 1, 2),
    _DocsSecSavCmAuthStaticPrefixListId_Type()
)
docsSecSavCmAuthStaticPrefixListId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsSecSavCmAuthStaticPrefixListId.setStatus("current")
_DocsSecSavCfgListTable_Object = MibTable
docsSecSavCfgListTable = _DocsSecSavCfgListTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 6)
)
if mibBuilder.loadTexts:
    docsSecSavCfgListTable.setStatus("current")
_DocsSecSavCfgListEntry_Object = MibTableRow
docsSecSavCfgListEntry = _DocsSecSavCfgListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 6, 1)
)
docsSecSavCfgListEntry.setIndexNames(
    (0, "DOCS-SEC-MIB", "docsSecSavCfgListName"),
    (0, "DOCS-SEC-MIB", "docsSecSavCfgListRuleId"),
)
if mibBuilder.loadTexts:
    docsSecSavCfgListEntry.setStatus("current")


class _DocsSecSavCfgListName_Type(SnmpAdminString):
    """Custom type docsSecSavCfgListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DocsSecSavCfgListName_Type.__name__ = "SnmpAdminString"
_DocsSecSavCfgListName_Object = MibTableColumn
docsSecSavCfgListName = _DocsSecSavCfgListName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 6, 1, 1),
    _DocsSecSavCfgListName_Type()
)
docsSecSavCfgListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsSecSavCfgListName.setStatus("current")


class _DocsSecSavCfgListRuleId_Type(Unsigned32):
    """Custom type docsSecSavCfgListRuleId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsSecSavCfgListRuleId_Type.__name__ = "Unsigned32"
_DocsSecSavCfgListRuleId_Object = MibTableColumn
docsSecSavCfgListRuleId = _DocsSecSavCfgListRuleId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 6, 1, 2),
    _DocsSecSavCfgListRuleId_Type()
)
docsSecSavCfgListRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsSecSavCfgListRuleId.setStatus("current")
_DocsSecSavCfgListPrefixAddrType_Type = InetAddressType
_DocsSecSavCfgListPrefixAddrType_Object = MibTableColumn
docsSecSavCfgListPrefixAddrType = _DocsSecSavCfgListPrefixAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 6, 1, 3),
    _DocsSecSavCfgListPrefixAddrType_Type()
)
docsSecSavCfgListPrefixAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSecSavCfgListPrefixAddrType.setStatus("current")
_DocsSecSavCfgListPrefixAddr_Type = InetAddress
_DocsSecSavCfgListPrefixAddr_Object = MibTableColumn
docsSecSavCfgListPrefixAddr = _DocsSecSavCfgListPrefixAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 6, 1, 4),
    _DocsSecSavCfgListPrefixAddr_Type()
)
docsSecSavCfgListPrefixAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSecSavCfgListPrefixAddr.setStatus("current")
_DocsSecSavCfgListPrefixLen_Type = InetAddressPrefixLength
_DocsSecSavCfgListPrefixLen_Object = MibTableColumn
docsSecSavCfgListPrefixLen = _DocsSecSavCfgListPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 6, 1, 5),
    _DocsSecSavCfgListPrefixLen_Type()
)
docsSecSavCfgListPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSecSavCfgListPrefixLen.setStatus("current")
_DocsSecSavCfgListRowStatus_Type = RowStatus
_DocsSecSavCfgListRowStatus_Object = MibTableColumn
docsSecSavCfgListRowStatus = _DocsSecSavCfgListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 6, 1, 6),
    _DocsSecSavCfgListRowStatus_Type()
)
docsSecSavCfgListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSecSavCfgListRowStatus.setStatus("current")
_DocsSecSavStaticListTable_Object = MibTable
docsSecSavStaticListTable = _DocsSecSavStaticListTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 7)
)
if mibBuilder.loadTexts:
    docsSecSavStaticListTable.setStatus("current")
_DocsSecSavStaticListEntry_Object = MibTableRow
docsSecSavStaticListEntry = _DocsSecSavStaticListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 7, 1)
)
docsSecSavStaticListEntry.setIndexNames(
    (0, "DOCS-SEC-MIB", "docsSecSavStaticListId"),
    (0, "DOCS-SEC-MIB", "docsSecSavStaticListRuleId"),
)
if mibBuilder.loadTexts:
    docsSecSavStaticListEntry.setStatus("current")


class _DocsSecSavStaticListId_Type(Unsigned32):
    """Custom type docsSecSavStaticListId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsSecSavStaticListId_Type.__name__ = "Unsigned32"
_DocsSecSavStaticListId_Object = MibTableColumn
docsSecSavStaticListId = _DocsSecSavStaticListId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 7, 1, 1),
    _DocsSecSavStaticListId_Type()
)
docsSecSavStaticListId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsSecSavStaticListId.setStatus("current")


class _DocsSecSavStaticListRuleId_Type(Unsigned32):
    """Custom type docsSecSavStaticListRuleId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsSecSavStaticListRuleId_Type.__name__ = "Unsigned32"
_DocsSecSavStaticListRuleId_Object = MibTableColumn
docsSecSavStaticListRuleId = _DocsSecSavStaticListRuleId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 7, 1, 2),
    _DocsSecSavStaticListRuleId_Type()
)
docsSecSavStaticListRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsSecSavStaticListRuleId.setStatus("current")
_DocsSecSavStaticListPrefixAddrType_Type = InetAddressType
_DocsSecSavStaticListPrefixAddrType_Object = MibTableColumn
docsSecSavStaticListPrefixAddrType = _DocsSecSavStaticListPrefixAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 7, 1, 3),
    _DocsSecSavStaticListPrefixAddrType_Type()
)
docsSecSavStaticListPrefixAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsSecSavStaticListPrefixAddrType.setStatus("current")
_DocsSecSavStaticListPrefixAddr_Type = InetAddress
_DocsSecSavStaticListPrefixAddr_Object = MibTableColumn
docsSecSavStaticListPrefixAddr = _DocsSecSavStaticListPrefixAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 7, 1, 4),
    _DocsSecSavStaticListPrefixAddr_Type()
)
docsSecSavStaticListPrefixAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsSecSavStaticListPrefixAddr.setStatus("current")
_DocsSecSavStaticListPrefixLen_Type = InetAddressPrefixLength
_DocsSecSavStaticListPrefixLen_Object = MibTableColumn
docsSecSavStaticListPrefixLen = _DocsSecSavStaticListPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 7, 1, 5),
    _DocsSecSavStaticListPrefixLen_Type()
)
docsSecSavStaticListPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsSecSavStaticListPrefixLen.setStatus("current")
_DocsSecCmtsCmSavStatsTable_Object = MibTable
docsSecCmtsCmSavStatsTable = _DocsSecCmtsCmSavStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 8)
)
if mibBuilder.loadTexts:
    docsSecCmtsCmSavStatsTable.setStatus("current")
_DocsSecCmtsCmSavStatsEntry_Object = MibTableRow
docsSecCmtsCmSavStatsEntry = _DocsSecCmtsCmSavStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 8, 1)
)
if mibBuilder.loadTexts:
    docsSecCmtsCmSavStatsEntry.setStatus("current")
_DocsSecCmtsCmSavStatsSavDiscards_Type = Counter32
_DocsSecCmtsCmSavStatsSavDiscards_Object = MibTableColumn
docsSecCmtsCmSavStatsSavDiscards = _DocsSecCmtsCmSavStatsSavDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 8, 1, 1),
    _DocsSecCmtsCmSavStatsSavDiscards_Type()
)
docsSecCmtsCmSavStatsSavDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsSecCmtsCmSavStatsSavDiscards.setStatus("current")
_DocsSecCmtsCertificate_ObjectIdentity = ObjectIdentity
docsSecCmtsCertificate = _DocsSecCmtsCertificate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 9)
)


class _DocsSecCmtsCertificateCertRevocationMethod_Type(Integer32):
    """Custom type docsSecCmtsCertificateCertRevocationMethod based on Integer32"""
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
        *(("crl", 2),
          ("crlAndOcsp", 4),
          ("none", 1),
          ("ocsp", 3))
    )


_DocsSecCmtsCertificateCertRevocationMethod_Type.__name__ = "Integer32"
_DocsSecCmtsCertificateCertRevocationMethod_Object = MibScalar
docsSecCmtsCertificateCertRevocationMethod = _DocsSecCmtsCertificateCertRevocationMethod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 9, 1),
    _DocsSecCmtsCertificateCertRevocationMethod_Type()
)
docsSecCmtsCertificateCertRevocationMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSecCmtsCertificateCertRevocationMethod.setStatus("current")
_DocsSecCmtsCertRevocationList_ObjectIdentity = ObjectIdentity
docsSecCmtsCertRevocationList = _DocsSecCmtsCertRevocationList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 10)
)
_DocsSecCmtsCertRevocationListUrl_Type = SnmpAdminString
_DocsSecCmtsCertRevocationListUrl_Object = MibScalar
docsSecCmtsCertRevocationListUrl = _DocsSecCmtsCertRevocationListUrl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 10, 1),
    _DocsSecCmtsCertRevocationListUrl_Type()
)
docsSecCmtsCertRevocationListUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSecCmtsCertRevocationListUrl.setStatus("current")


class _DocsSecCmtsCertRevocationListRefreshInterval_Type(Unsigned32):
    """Custom type docsSecCmtsCertRevocationListRefreshInterval based on Unsigned32"""
    defaultValue = 10080

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 524160),
    )


_DocsSecCmtsCertRevocationListRefreshInterval_Type.__name__ = "Unsigned32"
_DocsSecCmtsCertRevocationListRefreshInterval_Object = MibScalar
docsSecCmtsCertRevocationListRefreshInterval = _DocsSecCmtsCertRevocationListRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 10, 2),
    _DocsSecCmtsCertRevocationListRefreshInterval_Type()
)
docsSecCmtsCertRevocationListRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSecCmtsCertRevocationListRefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    docsSecCmtsCertRevocationListRefreshInterval.setUnits("minutes")
_DocsSecCmtsCertRevocationListLastUpdate_Type = DateAndTime
_DocsSecCmtsCertRevocationListLastUpdate_Object = MibScalar
docsSecCmtsCertRevocationListLastUpdate = _DocsSecCmtsCertRevocationListLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 10, 3),
    _DocsSecCmtsCertRevocationListLastUpdate_Type()
)
docsSecCmtsCertRevocationListLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsSecCmtsCertRevocationListLastUpdate.setStatus("current")
_DocsSecCmtsOnlineCertStatusProtocol_ObjectIdentity = ObjectIdentity
docsSecCmtsOnlineCertStatusProtocol = _DocsSecCmtsOnlineCertStatusProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 11)
)
_DocsSecCmtsOnlineCertStatusProtocolUrl_Type = SnmpAdminString
_DocsSecCmtsOnlineCertStatusProtocolUrl_Object = MibScalar
docsSecCmtsOnlineCertStatusProtocolUrl = _DocsSecCmtsOnlineCertStatusProtocolUrl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 11, 1),
    _DocsSecCmtsOnlineCertStatusProtocolUrl_Type()
)
docsSecCmtsOnlineCertStatusProtocolUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSecCmtsOnlineCertStatusProtocolUrl.setStatus("current")


class _DocsSecCmtsOnlineCertStatusProtocolSignatureBypass_Type(TruthValue):
    """Custom type docsSecCmtsOnlineCertStatusProtocolSignatureBypass based on TruthValue"""


_DocsSecCmtsOnlineCertStatusProtocolSignatureBypass_Object = MibScalar
docsSecCmtsOnlineCertStatusProtocolSignatureBypass = _DocsSecCmtsOnlineCertStatusProtocolSignatureBypass_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 11, 2),
    _DocsSecCmtsOnlineCertStatusProtocolSignatureBypass_Type()
)
docsSecCmtsOnlineCertStatusProtocolSignatureBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSecCmtsOnlineCertStatusProtocolSignatureBypass.setStatus("current")
_DocsSecCmtsCmBpi2EnforceExclusionTable_Object = MibTable
docsSecCmtsCmBpi2EnforceExclusionTable = _DocsSecCmtsCmBpi2EnforceExclusionTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 12)
)
if mibBuilder.loadTexts:
    docsSecCmtsCmBpi2EnforceExclusionTable.setStatus("current")
_DocsSecCmtsCmBpi2EnforceExclusionEntry_Object = MibTableRow
docsSecCmtsCmBpi2EnforceExclusionEntry = _DocsSecCmtsCmBpi2EnforceExclusionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 12, 1)
)
docsSecCmtsCmBpi2EnforceExclusionEntry.setIndexNames(
    (0, "DOCS-SEC-MIB", "docsSecCmtsCmBpi2EnforceExclusionId"),
)
if mibBuilder.loadTexts:
    docsSecCmtsCmBpi2EnforceExclusionEntry.setStatus("current")


class _DocsSecCmtsCmBpi2EnforceExclusionId_Type(Unsigned32):
    """Custom type docsSecCmtsCmBpi2EnforceExclusionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsSecCmtsCmBpi2EnforceExclusionId_Type.__name__ = "Unsigned32"
_DocsSecCmtsCmBpi2EnforceExclusionId_Object = MibTableColumn
docsSecCmtsCmBpi2EnforceExclusionId = _DocsSecCmtsCmBpi2EnforceExclusionId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 12, 1, 1),
    _DocsSecCmtsCmBpi2EnforceExclusionId_Type()
)
docsSecCmtsCmBpi2EnforceExclusionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsSecCmtsCmBpi2EnforceExclusionId.setStatus("current")


class _DocsSecCmtsCmBpi2EnforceExclusionMacAddr_Type(MacAddress):
    """Custom type docsSecCmtsCmBpi2EnforceExclusionMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_DocsSecCmtsCmBpi2EnforceExclusionMacAddr_Object = MibTableColumn
docsSecCmtsCmBpi2EnforceExclusionMacAddr = _DocsSecCmtsCmBpi2EnforceExclusionMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 12, 1, 2),
    _DocsSecCmtsCmBpi2EnforceExclusionMacAddr_Type()
)
docsSecCmtsCmBpi2EnforceExclusionMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSecCmtsCmBpi2EnforceExclusionMacAddr.setStatus("current")


class _DocsSecCmtsCmBpi2EnforceExclusionMacAddrMask_Type(MacAddress):
    """Custom type docsSecCmtsCmBpi2EnforceExclusionMacAddrMask based on MacAddress"""
    defaultHexValue = "FFFFFFFFFFFF"


_DocsSecCmtsCmBpi2EnforceExclusionMacAddrMask_Object = MibTableColumn
docsSecCmtsCmBpi2EnforceExclusionMacAddrMask = _DocsSecCmtsCmBpi2EnforceExclusionMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 12, 1, 3),
    _DocsSecCmtsCmBpi2EnforceExclusionMacAddrMask_Type()
)
docsSecCmtsCmBpi2EnforceExclusionMacAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSecCmtsCmBpi2EnforceExclusionMacAddrMask.setStatus("current")
_DocsSecCmtsCmBpi2EnforceExclusionRowStatus_Type = RowStatus
_DocsSecCmtsCmBpi2EnforceExclusionRowStatus_Object = MibTableColumn
docsSecCmtsCmBpi2EnforceExclusionRowStatus = _DocsSecCmtsCmBpi2EnforceExclusionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 12, 1, 4),
    _DocsSecCmtsCmBpi2EnforceExclusionRowStatus_Type()
)
docsSecCmtsCmBpi2EnforceExclusionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSecCmtsCmBpi2EnforceExclusionRowStatus.setStatus("current")
_DocsSecMibConformance_ObjectIdentity = ObjectIdentity
docsSecMibConformance = _DocsSecMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 2)
)
_DocsSecMibCompliances_ObjectIdentity = ObjectIdentity
docsSecMibCompliances = _DocsSecMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 2, 1)
)
_DocsSecMibGroups_ObjectIdentity = ObjectIdentity
docsSecMibGroups = _DocsSecMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 2, 2)
)
docsIf3CmtsCmRegStatusEntry.registerAugmentions(
    ("DOCS-SEC-MIB",
     "docsSecCmtsCmSavStatsEntry")
)
docsSecCmtsCmSavStatsEntry.setIndexNames(*docsIf3CmtsCmRegStatusEntry.getIndexNames())

# Managed Objects groups

docsSecGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 2, 2, 1)
)
docsSecGroup.setObjects(
      *(("DOCS-SEC-MIB", "docsSecCmtsCertRevocationListUrl"),
        ("DOCS-SEC-MIB", "docsSecCmtsCertRevocationListRefreshInterval"),
        ("DOCS-SEC-MIB", "docsSecCmtsCertRevocationListLastUpdate"),
        ("DOCS-SEC-MIB", "docsSecCmtsOnlineCertStatusProtocolUrl"),
        ("DOCS-SEC-MIB", "docsSecCmtsOnlineCertStatusProtocolSignatureBypass"),
        ("DOCS-SEC-MIB", "docsSecCmtsServerCfgTftpOptions"),
        ("DOCS-SEC-MIB", "docsSecCmtsServerCfgConfigFileLearningEnable"),
        ("DOCS-SEC-MIB", "docsSecCmtsEncryptEncryptAlgPriority"),
        ("DOCS-SEC-MIB", "docsSecCmtsSavControlCmAuthEnable"),
        ("DOCS-SEC-MIB", "docsSecCmtsCmEaeExclusionMacAddr"),
        ("DOCS-SEC-MIB", "docsSecCmtsCmEaeExclusionMacAddrMask"),
        ("DOCS-SEC-MIB", "docsSecCmtsCmEaeExclusionRowStatus"),
        ("DOCS-SEC-MIB", "docsSecSavCmAuthGrpName"),
        ("DOCS-SEC-MIB", "docsSecSavCmAuthStaticPrefixListId"),
        ("DOCS-SEC-MIB", "docsSecSavCfgListPrefixAddrType"),
        ("DOCS-SEC-MIB", "docsSecSavCfgListPrefixAddr"),
        ("DOCS-SEC-MIB", "docsSecSavCfgListPrefixLen"),
        ("DOCS-SEC-MIB", "docsSecSavCfgListRowStatus"),
        ("DOCS-SEC-MIB", "docsSecSavStaticListPrefixAddrType"),
        ("DOCS-SEC-MIB", "docsSecSavStaticListPrefixAddr"),
        ("DOCS-SEC-MIB", "docsSecSavStaticListPrefixLen"),
        ("DOCS-SEC-MIB", "docsSecCmtsCmSavStatsSavDiscards"),
        ("DOCS-SEC-MIB", "docsSecCmtsCertificateCertRevocationMethod"),
        ("DOCS-SEC-MIB", "docsSecCmtsCmBpi2EnforceExclusionMacAddr"),
        ("DOCS-SEC-MIB", "docsSecCmtsCmBpi2EnforceExclusionMacAddrMask"),
        ("DOCS-SEC-MIB", "docsSecCmtsCmBpi2EnforceExclusionRowStatus"))
)
if mibBuilder.loadTexts:
    docsSecGroup.setStatus("current")

docsSecCmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 2, 2, 2)
)
docsSecCmGroup.setObjects(
    ("DOCS-SEC-MIB", "docsBpi2CodeUpdateCvcChain")
)
if mibBuilder.loadTexts:
    docsSecCmGroup.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

docsSecCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 2, 1, 1)
)
if mibBuilder.loadTexts:
    docsSecCompliance.setStatus(
        "current"
    )

docsSecCmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 2, 1, 2)
)
if mibBuilder.loadTexts:
    docsSecCmCompliance.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-SEC-MIB",
    **{"DocsCvcCaCertificateChain": DocsCvcCaCertificateChain,
       "docsBpi2CodeUpdateCvcChain": docsBpi2CodeUpdateCvcChain,
       "docsSecMib": docsSecMib,
       "docsSecMibObjects": docsSecMibObjects,
       "docsSecCmtsServerCfg": docsSecCmtsServerCfg,
       "docsSecCmtsServerCfgTftpOptions": docsSecCmtsServerCfgTftpOptions,
       "docsSecCmtsServerCfgConfigFileLearningEnable": docsSecCmtsServerCfgConfigFileLearningEnable,
       "docsSecCmtsEncrypt": docsSecCmtsEncrypt,
       "docsSecCmtsEncryptEncryptAlgPriority": docsSecCmtsEncryptEncryptAlgPriority,
       "docsSecCmtsCmEaeExclusionTable": docsSecCmtsCmEaeExclusionTable,
       "docsSecCmtsCmEaeExclusionEntry": docsSecCmtsCmEaeExclusionEntry,
       "docsSecCmtsCmEaeExclusionId": docsSecCmtsCmEaeExclusionId,
       "docsSecCmtsCmEaeExclusionMacAddr": docsSecCmtsCmEaeExclusionMacAddr,
       "docsSecCmtsCmEaeExclusionMacAddrMask": docsSecCmtsCmEaeExclusionMacAddrMask,
       "docsSecCmtsCmEaeExclusionRowStatus": docsSecCmtsCmEaeExclusionRowStatus,
       "docsSecCmtsSavControl": docsSecCmtsSavControl,
       "docsSecCmtsSavControlCmAuthEnable": docsSecCmtsSavControlCmAuthEnable,
       "docsSecSavCmAuthTable": docsSecSavCmAuthTable,
       "docsSecSavCmAuthEntry": docsSecSavCmAuthEntry,
       "docsSecSavCmAuthGrpName": docsSecSavCmAuthGrpName,
       "docsSecSavCmAuthStaticPrefixListId": docsSecSavCmAuthStaticPrefixListId,
       "docsSecSavCfgListTable": docsSecSavCfgListTable,
       "docsSecSavCfgListEntry": docsSecSavCfgListEntry,
       "docsSecSavCfgListName": docsSecSavCfgListName,
       "docsSecSavCfgListRuleId": docsSecSavCfgListRuleId,
       "docsSecSavCfgListPrefixAddrType": docsSecSavCfgListPrefixAddrType,
       "docsSecSavCfgListPrefixAddr": docsSecSavCfgListPrefixAddr,
       "docsSecSavCfgListPrefixLen": docsSecSavCfgListPrefixLen,
       "docsSecSavCfgListRowStatus": docsSecSavCfgListRowStatus,
       "docsSecSavStaticListTable": docsSecSavStaticListTable,
       "docsSecSavStaticListEntry": docsSecSavStaticListEntry,
       "docsSecSavStaticListId": docsSecSavStaticListId,
       "docsSecSavStaticListRuleId": docsSecSavStaticListRuleId,
       "docsSecSavStaticListPrefixAddrType": docsSecSavStaticListPrefixAddrType,
       "docsSecSavStaticListPrefixAddr": docsSecSavStaticListPrefixAddr,
       "docsSecSavStaticListPrefixLen": docsSecSavStaticListPrefixLen,
       "docsSecCmtsCmSavStatsTable": docsSecCmtsCmSavStatsTable,
       "docsSecCmtsCmSavStatsEntry": docsSecCmtsCmSavStatsEntry,
       "docsSecCmtsCmSavStatsSavDiscards": docsSecCmtsCmSavStatsSavDiscards,
       "docsSecCmtsCertificate": docsSecCmtsCertificate,
       "docsSecCmtsCertificateCertRevocationMethod": docsSecCmtsCertificateCertRevocationMethod,
       "docsSecCmtsCertRevocationList": docsSecCmtsCertRevocationList,
       "docsSecCmtsCertRevocationListUrl": docsSecCmtsCertRevocationListUrl,
       "docsSecCmtsCertRevocationListRefreshInterval": docsSecCmtsCertRevocationListRefreshInterval,
       "docsSecCmtsCertRevocationListLastUpdate": docsSecCmtsCertRevocationListLastUpdate,
       "docsSecCmtsOnlineCertStatusProtocol": docsSecCmtsOnlineCertStatusProtocol,
       "docsSecCmtsOnlineCertStatusProtocolUrl": docsSecCmtsOnlineCertStatusProtocolUrl,
       "docsSecCmtsOnlineCertStatusProtocolSignatureBypass": docsSecCmtsOnlineCertStatusProtocolSignatureBypass,
       "docsSecCmtsCmBpi2EnforceExclusionTable": docsSecCmtsCmBpi2EnforceExclusionTable,
       "docsSecCmtsCmBpi2EnforceExclusionEntry": docsSecCmtsCmBpi2EnforceExclusionEntry,
       "docsSecCmtsCmBpi2EnforceExclusionId": docsSecCmtsCmBpi2EnforceExclusionId,
       "docsSecCmtsCmBpi2EnforceExclusionMacAddr": docsSecCmtsCmBpi2EnforceExclusionMacAddr,
       "docsSecCmtsCmBpi2EnforceExclusionMacAddrMask": docsSecCmtsCmBpi2EnforceExclusionMacAddrMask,
       "docsSecCmtsCmBpi2EnforceExclusionRowStatus": docsSecCmtsCmBpi2EnforceExclusionRowStatus,
       "docsSecMibConformance": docsSecMibConformance,
       "docsSecMibCompliances": docsSecMibCompliances,
       "docsSecCompliance": docsSecCompliance,
       "docsSecCmCompliance": docsSecCmCompliance,
       "docsSecMibGroups": docsSecMibGroups,
       "docsSecGroup": docsSecGroup,
       "docsSecCmGroup": docsSecCmGroup}
)
