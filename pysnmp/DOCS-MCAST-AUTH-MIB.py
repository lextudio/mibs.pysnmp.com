# SNMP MIB module (DOCS-MCAST-AUTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOCS-MCAST-AUTH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:54 2024
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

(docsIf3CmtsCmRegStatusId,) = mibBuilder.importSymbols(
    "DOCS-IF3-MIB",
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

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

docsMcastAuthMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19)
)
docsMcastAuthMib.setRevisions(
        ("2007-12-06 00:00",
         "2006-12-07 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DocsMcastAuthMibObjects_ObjectIdentity = ObjectIdentity
docsMcastAuthMibObjects = _DocsMcastAuthMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1)
)
_DocsMcastAuthCtrl_ObjectIdentity = ObjectIdentity
docsMcastAuthCtrl = _DocsMcastAuthCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 1)
)


class _DocsMcastAuthCtrlEnable_Type(Integer32):
    """Custom type docsMcastAuthCtrlEnable based on Integer32"""
    defaultValue = 2

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


_DocsMcastAuthCtrlEnable_Type.__name__ = "Integer32"
_DocsMcastAuthCtrlEnable_Object = MibScalar
docsMcastAuthCtrlEnable = _DocsMcastAuthCtrlEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 1, 1),
    _DocsMcastAuthCtrlEnable_Type()
)
docsMcastAuthCtrlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsMcastAuthCtrlEnable.setStatus("current")


class _DocsMcastAuthCtrlDefProfileNameList_Type(SnmpTagList):
    """Custom type docsMcastAuthCtrlDefProfileNameList based on SnmpTagList"""
    defaultHexValue = ""


_DocsMcastAuthCtrlDefProfileNameList_Object = MibScalar
docsMcastAuthCtrlDefProfileNameList = _DocsMcastAuthCtrlDefProfileNameList_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 1, 2),
    _DocsMcastAuthCtrlDefProfileNameList_Type()
)
docsMcastAuthCtrlDefProfileNameList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsMcastAuthCtrlDefProfileNameList.setStatus("current")


class _DocsMcastAuthCtrlDefAction_Type(Integer32):
    """Custom type docsMcastAuthCtrlDefAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_DocsMcastAuthCtrlDefAction_Type.__name__ = "Integer32"
_DocsMcastAuthCtrlDefAction_Object = MibScalar
docsMcastAuthCtrlDefAction = _DocsMcastAuthCtrlDefAction_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 1, 3),
    _DocsMcastAuthCtrlDefAction_Type()
)
docsMcastAuthCtrlDefAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsMcastAuthCtrlDefAction.setStatus("current")


class _DocsMcastAuthCtrlDefMaxNumSess_Type(Unsigned32):
    """Custom type docsMcastAuthCtrlDefMaxNumSess based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsMcastAuthCtrlDefMaxNumSess_Type.__name__ = "Unsigned32"
_DocsMcastAuthCtrlDefMaxNumSess_Object = MibScalar
docsMcastAuthCtrlDefMaxNumSess = _DocsMcastAuthCtrlDefMaxNumSess_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 1, 4),
    _DocsMcastAuthCtrlDefMaxNumSess_Type()
)
docsMcastAuthCtrlDefMaxNumSess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsMcastAuthCtrlDefMaxNumSess.setStatus("current")
_DocsMcastAuthCmtsCmStatusTable_Object = MibTable
docsMcastAuthCmtsCmStatusTable = _DocsMcastAuthCmtsCmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 2)
)
if mibBuilder.loadTexts:
    docsMcastAuthCmtsCmStatusTable.setStatus("current")
_DocsMcastAuthCmtsCmStatusEntry_Object = MibTableRow
docsMcastAuthCmtsCmStatusEntry = _DocsMcastAuthCmtsCmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 2, 1)
)
docsMcastAuthCmtsCmStatusEntry.setIndexNames(
    (0, "DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusId"),
)
if mibBuilder.loadTexts:
    docsMcastAuthCmtsCmStatusEntry.setStatus("current")
_DocsMcastAuthCmtsCmStatusCfgProfileNameList_Type = SnmpTagList
_DocsMcastAuthCmtsCmStatusCfgProfileNameList_Object = MibTableColumn
docsMcastAuthCmtsCmStatusCfgProfileNameList = _DocsMcastAuthCmtsCmStatusCfgProfileNameList_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 2, 1, 1),
    _DocsMcastAuthCmtsCmStatusCfgProfileNameList_Type()
)
docsMcastAuthCmtsCmStatusCfgProfileNameList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsMcastAuthCmtsCmStatusCfgProfileNameList.setStatus("current")
_DocsMcastAuthCmtsCmStatusCfgListId_Type = Unsigned32
_DocsMcastAuthCmtsCmStatusCfgListId_Object = MibTableColumn
docsMcastAuthCmtsCmStatusCfgListId = _DocsMcastAuthCmtsCmStatusCfgListId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 2, 1, 2),
    _DocsMcastAuthCmtsCmStatusCfgListId_Type()
)
docsMcastAuthCmtsCmStatusCfgListId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsMcastAuthCmtsCmStatusCfgListId.setStatus("current")


class _DocsMcastAuthCmtsCmStatusMaxNumSess_Type(Unsigned32):
    """Custom type docsMcastAuthCmtsCmStatusMaxNumSess based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsMcastAuthCmtsCmStatusMaxNumSess_Type.__name__ = "Unsigned32"
_DocsMcastAuthCmtsCmStatusMaxNumSess_Object = MibTableColumn
docsMcastAuthCmtsCmStatusMaxNumSess = _DocsMcastAuthCmtsCmStatusMaxNumSess_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 2, 1, 3),
    _DocsMcastAuthCmtsCmStatusMaxNumSess_Type()
)
docsMcastAuthCmtsCmStatusMaxNumSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsMcastAuthCmtsCmStatusMaxNumSess.setStatus("current")
if mibBuilder.loadTexts:
    docsMcastAuthCmtsCmStatusMaxNumSess.setUnits("sessions")


class _DocsMcastAuthCmtsCmStatusCfgParamFlag_Type(Bits):
    """Custom type docsMcastAuthCmtsCmStatusCfgParamFlag based on Bits"""
    namedValues = NamedValues(
        *(("maxNumSessions", 2),
          ("profile", 0),
          ("staticMulticast", 1))
    )

_DocsMcastAuthCmtsCmStatusCfgParamFlag_Type.__name__ = "Bits"
_DocsMcastAuthCmtsCmStatusCfgParamFlag_Object = MibTableColumn
docsMcastAuthCmtsCmStatusCfgParamFlag = _DocsMcastAuthCmtsCmStatusCfgParamFlag_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 2, 1, 4),
    _DocsMcastAuthCmtsCmStatusCfgParamFlag_Type()
)
docsMcastAuthCmtsCmStatusCfgParamFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsMcastAuthCmtsCmStatusCfgParamFlag.setStatus("current")
_DocsMcastAuthProfileSessRuleTable_Object = MibTable
docsMcastAuthProfileSessRuleTable = _DocsMcastAuthProfileSessRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 3)
)
if mibBuilder.loadTexts:
    docsMcastAuthProfileSessRuleTable.setStatus("current")
_DocsMcastAuthProfileSessRuleEntry_Object = MibTableRow
docsMcastAuthProfileSessRuleEntry = _DocsMcastAuthProfileSessRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 3, 1)
)
docsMcastAuthProfileSessRuleEntry.setIndexNames(
    (0, "DOCS-MCAST-AUTH-MIB", "docsMcastAuthProfilesName"),
    (0, "DOCS-MCAST-AUTH-MIB", "docsMcastAuthProfileSessRuleId"),
)
if mibBuilder.loadTexts:
    docsMcastAuthProfileSessRuleEntry.setStatus("current")


class _DocsMcastAuthProfileSessRuleId_Type(Unsigned32):
    """Custom type docsMcastAuthProfileSessRuleId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsMcastAuthProfileSessRuleId_Type.__name__ = "Unsigned32"
_DocsMcastAuthProfileSessRuleId_Object = MibTableColumn
docsMcastAuthProfileSessRuleId = _DocsMcastAuthProfileSessRuleId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 3, 1, 1),
    _DocsMcastAuthProfileSessRuleId_Type()
)
docsMcastAuthProfileSessRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsMcastAuthProfileSessRuleId.setStatus("current")


class _DocsMcastAuthProfileSessRulePriority_Type(Unsigned32):
    """Custom type docsMcastAuthProfileSessRulePriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsMcastAuthProfileSessRulePriority_Type.__name__ = "Unsigned32"
_DocsMcastAuthProfileSessRulePriority_Object = MibTableColumn
docsMcastAuthProfileSessRulePriority = _DocsMcastAuthProfileSessRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 3, 1, 2),
    _DocsMcastAuthProfileSessRulePriority_Type()
)
docsMcastAuthProfileSessRulePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastAuthProfileSessRulePriority.setStatus("current")
_DocsMcastAuthProfileSessRulePrefixAddrType_Type = InetAddressType
_DocsMcastAuthProfileSessRulePrefixAddrType_Object = MibTableColumn
docsMcastAuthProfileSessRulePrefixAddrType = _DocsMcastAuthProfileSessRulePrefixAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 3, 1, 3),
    _DocsMcastAuthProfileSessRulePrefixAddrType_Type()
)
docsMcastAuthProfileSessRulePrefixAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastAuthProfileSessRulePrefixAddrType.setStatus("current")
_DocsMcastAuthProfileSessRuleSrcPrefixAddr_Type = InetAddress
_DocsMcastAuthProfileSessRuleSrcPrefixAddr_Object = MibTableColumn
docsMcastAuthProfileSessRuleSrcPrefixAddr = _DocsMcastAuthProfileSessRuleSrcPrefixAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 3, 1, 4),
    _DocsMcastAuthProfileSessRuleSrcPrefixAddr_Type()
)
docsMcastAuthProfileSessRuleSrcPrefixAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastAuthProfileSessRuleSrcPrefixAddr.setStatus("current")
_DocsMcastAuthProfileSessRuleSrcPrefixLen_Type = InetAddressPrefixLength
_DocsMcastAuthProfileSessRuleSrcPrefixLen_Object = MibTableColumn
docsMcastAuthProfileSessRuleSrcPrefixLen = _DocsMcastAuthProfileSessRuleSrcPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 3, 1, 5),
    _DocsMcastAuthProfileSessRuleSrcPrefixLen_Type()
)
docsMcastAuthProfileSessRuleSrcPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastAuthProfileSessRuleSrcPrefixLen.setStatus("current")
_DocsMcastAuthProfileSessRuleGrpPrefixAddr_Type = InetAddress
_DocsMcastAuthProfileSessRuleGrpPrefixAddr_Object = MibTableColumn
docsMcastAuthProfileSessRuleGrpPrefixAddr = _DocsMcastAuthProfileSessRuleGrpPrefixAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 3, 1, 6),
    _DocsMcastAuthProfileSessRuleGrpPrefixAddr_Type()
)
docsMcastAuthProfileSessRuleGrpPrefixAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastAuthProfileSessRuleGrpPrefixAddr.setStatus("current")
_DocsMcastAuthProfileSessRuleGrpPrefixLen_Type = InetAddressPrefixLength
_DocsMcastAuthProfileSessRuleGrpPrefixLen_Object = MibTableColumn
docsMcastAuthProfileSessRuleGrpPrefixLen = _DocsMcastAuthProfileSessRuleGrpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 3, 1, 7),
    _DocsMcastAuthProfileSessRuleGrpPrefixLen_Type()
)
docsMcastAuthProfileSessRuleGrpPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastAuthProfileSessRuleGrpPrefixLen.setStatus("current")


class _DocsMcastAuthProfileSessRuleAction_Type(Integer32):
    """Custom type docsMcastAuthProfileSessRuleAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("deny", 2))
    )


_DocsMcastAuthProfileSessRuleAction_Type.__name__ = "Integer32"
_DocsMcastAuthProfileSessRuleAction_Object = MibTableColumn
docsMcastAuthProfileSessRuleAction = _DocsMcastAuthProfileSessRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 3, 1, 8),
    _DocsMcastAuthProfileSessRuleAction_Type()
)
docsMcastAuthProfileSessRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastAuthProfileSessRuleAction.setStatus("current")
_DocsMcastAuthProfileSessRuleRowStatus_Type = RowStatus
_DocsMcastAuthProfileSessRuleRowStatus_Object = MibTableColumn
docsMcastAuthProfileSessRuleRowStatus = _DocsMcastAuthProfileSessRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 3, 1, 9),
    _DocsMcastAuthProfileSessRuleRowStatus_Type()
)
docsMcastAuthProfileSessRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastAuthProfileSessRuleRowStatus.setStatus("current")
_DocsMcastAuthStaticSessRuleTable_Object = MibTable
docsMcastAuthStaticSessRuleTable = _DocsMcastAuthStaticSessRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 4)
)
if mibBuilder.loadTexts:
    docsMcastAuthStaticSessRuleTable.setStatus("current")
_DocsMcastAuthStaticSessRuleEntry_Object = MibTableRow
docsMcastAuthStaticSessRuleEntry = _DocsMcastAuthStaticSessRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 4, 1)
)
docsMcastAuthStaticSessRuleEntry.setIndexNames(
    (0, "DOCS-MCAST-AUTH-MIB", "docsMcastAuthStaticSessRuleCfgListId"),
    (0, "DOCS-MCAST-AUTH-MIB", "docsMcastAuthStaticSessRuleId"),
)
if mibBuilder.loadTexts:
    docsMcastAuthStaticSessRuleEntry.setStatus("current")


class _DocsMcastAuthStaticSessRuleCfgListId_Type(Unsigned32):
    """Custom type docsMcastAuthStaticSessRuleCfgListId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsMcastAuthStaticSessRuleCfgListId_Type.__name__ = "Unsigned32"
_DocsMcastAuthStaticSessRuleCfgListId_Object = MibTableColumn
docsMcastAuthStaticSessRuleCfgListId = _DocsMcastAuthStaticSessRuleCfgListId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 4, 1, 1),
    _DocsMcastAuthStaticSessRuleCfgListId_Type()
)
docsMcastAuthStaticSessRuleCfgListId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsMcastAuthStaticSessRuleCfgListId.setStatus("current")


class _DocsMcastAuthStaticSessRuleId_Type(Unsigned32):
    """Custom type docsMcastAuthStaticSessRuleId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsMcastAuthStaticSessRuleId_Type.__name__ = "Unsigned32"
_DocsMcastAuthStaticSessRuleId_Object = MibTableColumn
docsMcastAuthStaticSessRuleId = _DocsMcastAuthStaticSessRuleId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 4, 1, 2),
    _DocsMcastAuthStaticSessRuleId_Type()
)
docsMcastAuthStaticSessRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsMcastAuthStaticSessRuleId.setStatus("current")


class _DocsMcastAuthStaticSessRulePriority_Type(Unsigned32):
    """Custom type docsMcastAuthStaticSessRulePriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsMcastAuthStaticSessRulePriority_Type.__name__ = "Unsigned32"
_DocsMcastAuthStaticSessRulePriority_Object = MibTableColumn
docsMcastAuthStaticSessRulePriority = _DocsMcastAuthStaticSessRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 4, 1, 3),
    _DocsMcastAuthStaticSessRulePriority_Type()
)
docsMcastAuthStaticSessRulePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsMcastAuthStaticSessRulePriority.setStatus("current")
_DocsMcastAuthStaticSessRulePrefixAddrType_Type = InetAddressType
_DocsMcastAuthStaticSessRulePrefixAddrType_Object = MibTableColumn
docsMcastAuthStaticSessRulePrefixAddrType = _DocsMcastAuthStaticSessRulePrefixAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 4, 1, 4),
    _DocsMcastAuthStaticSessRulePrefixAddrType_Type()
)
docsMcastAuthStaticSessRulePrefixAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsMcastAuthStaticSessRulePrefixAddrType.setStatus("current")
_DocsMcastAuthStaticSessRuleSrcPrefixAddr_Type = InetAddress
_DocsMcastAuthStaticSessRuleSrcPrefixAddr_Object = MibTableColumn
docsMcastAuthStaticSessRuleSrcPrefixAddr = _DocsMcastAuthStaticSessRuleSrcPrefixAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 4, 1, 5),
    _DocsMcastAuthStaticSessRuleSrcPrefixAddr_Type()
)
docsMcastAuthStaticSessRuleSrcPrefixAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsMcastAuthStaticSessRuleSrcPrefixAddr.setStatus("current")
_DocsMcastAuthStaticSessRuleSrcPrefixLen_Type = InetAddressPrefixLength
_DocsMcastAuthStaticSessRuleSrcPrefixLen_Object = MibTableColumn
docsMcastAuthStaticSessRuleSrcPrefixLen = _DocsMcastAuthStaticSessRuleSrcPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 4, 1, 6),
    _DocsMcastAuthStaticSessRuleSrcPrefixLen_Type()
)
docsMcastAuthStaticSessRuleSrcPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsMcastAuthStaticSessRuleSrcPrefixLen.setStatus("current")
_DocsMcastAuthStaticSessRuleGrpPrefixAddr_Type = InetAddress
_DocsMcastAuthStaticSessRuleGrpPrefixAddr_Object = MibTableColumn
docsMcastAuthStaticSessRuleGrpPrefixAddr = _DocsMcastAuthStaticSessRuleGrpPrefixAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 4, 1, 7),
    _DocsMcastAuthStaticSessRuleGrpPrefixAddr_Type()
)
docsMcastAuthStaticSessRuleGrpPrefixAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsMcastAuthStaticSessRuleGrpPrefixAddr.setStatus("current")
_DocsMcastAuthStaticSessRuleGrpPrefixLen_Type = InetAddressPrefixLength
_DocsMcastAuthStaticSessRuleGrpPrefixLen_Object = MibTableColumn
docsMcastAuthStaticSessRuleGrpPrefixLen = _DocsMcastAuthStaticSessRuleGrpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 4, 1, 8),
    _DocsMcastAuthStaticSessRuleGrpPrefixLen_Type()
)
docsMcastAuthStaticSessRuleGrpPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsMcastAuthStaticSessRuleGrpPrefixLen.setStatus("current")


class _DocsMcastAuthStaticSessRuleAction_Type(Integer32):
    """Custom type docsMcastAuthStaticSessRuleAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_DocsMcastAuthStaticSessRuleAction_Type.__name__ = "Integer32"
_DocsMcastAuthStaticSessRuleAction_Object = MibTableColumn
docsMcastAuthStaticSessRuleAction = _DocsMcastAuthStaticSessRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 4, 1, 9),
    _DocsMcastAuthStaticSessRuleAction_Type()
)
docsMcastAuthStaticSessRuleAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsMcastAuthStaticSessRuleAction.setStatus("current")
_DocsMcastAuthProfilesTable_Object = MibTable
docsMcastAuthProfilesTable = _DocsMcastAuthProfilesTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 5)
)
if mibBuilder.loadTexts:
    docsMcastAuthProfilesTable.setStatus("current")
_DocsMcastAuthProfilesEntry_Object = MibTableRow
docsMcastAuthProfilesEntry = _DocsMcastAuthProfilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 5, 1)
)
docsMcastAuthProfilesEntry.setIndexNames(
    (0, "DOCS-MCAST-AUTH-MIB", "docsMcastAuthProfilesName"),
)
if mibBuilder.loadTexts:
    docsMcastAuthProfilesEntry.setStatus("current")


class _DocsMcastAuthProfilesName_Type(SnmpAdminString):
    """Custom type docsMcastAuthProfilesName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_DocsMcastAuthProfilesName_Type.__name__ = "SnmpAdminString"
_DocsMcastAuthProfilesName_Object = MibTableColumn
docsMcastAuthProfilesName = _DocsMcastAuthProfilesName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 5, 1, 1),
    _DocsMcastAuthProfilesName_Type()
)
docsMcastAuthProfilesName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsMcastAuthProfilesName.setStatus("current")
_DocsMcastAuthProfilesDescription_Type = SnmpAdminString
_DocsMcastAuthProfilesDescription_Object = MibTableColumn
docsMcastAuthProfilesDescription = _DocsMcastAuthProfilesDescription_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 5, 1, 2),
    _DocsMcastAuthProfilesDescription_Type()
)
docsMcastAuthProfilesDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastAuthProfilesDescription.setStatus("current")
_DocsMcastAuthProfilesRowStatus_Type = RowStatus
_DocsMcastAuthProfilesRowStatus_Object = MibTableColumn
docsMcastAuthProfilesRowStatus = _DocsMcastAuthProfilesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 5, 1, 3),
    _DocsMcastAuthProfilesRowStatus_Type()
)
docsMcastAuthProfilesRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsMcastAuthProfilesRowStatus.setStatus("current")
_DocsMcastAuthMibConformance_ObjectIdentity = ObjectIdentity
docsMcastAuthMibConformance = _DocsMcastAuthMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 2)
)
_DocsMcastAuthMibCompliances_ObjectIdentity = ObjectIdentity
docsMcastAuthMibCompliances = _DocsMcastAuthMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 2, 1)
)
_DocsMcastAuthMibGroups_ObjectIdentity = ObjectIdentity
docsMcastAuthMibGroups = _DocsMcastAuthMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 2, 2)
)

# Managed Objects groups

docsMcastAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 2, 2, 1)
)
docsMcastAuthGroup.setObjects(
      *(("DOCS-MCAST-AUTH-MIB", "docsMcastAuthCtrlEnable"),
        ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthCtrlDefProfileNameList"),
        ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthCtrlDefAction"),
        ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthCtrlDefMaxNumSess"),
        ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthCmtsCmStatusCfgProfileNameList"),
        ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthCmtsCmStatusCfgListId"),
        ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthCmtsCmStatusMaxNumSess"),
        ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthCmtsCmStatusCfgParamFlag"),
        ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthProfileSessRulePriority"),
        ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthProfileSessRulePrefixAddrType"),
        ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthProfileSessRuleSrcPrefixAddr"),
        ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthProfileSessRuleSrcPrefixLen"),
        ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthProfileSessRuleGrpPrefixAddr"),
        ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthProfileSessRuleGrpPrefixLen"),
        ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthProfileSessRuleAction"),
        ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthProfileSessRuleRowStatus"),
        ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthStaticSessRulePriority"),
        ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthStaticSessRulePrefixAddrType"),
        ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthStaticSessRuleSrcPrefixAddr"),
        ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthStaticSessRuleSrcPrefixLen"),
        ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthStaticSessRuleGrpPrefixAddr"),
        ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthStaticSessRuleGrpPrefixLen"),
        ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthStaticSessRuleAction"),
        ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthProfilesDescription"),
        ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthProfilesRowStatus"))
)
if mibBuilder.loadTexts:
    docsMcastAuthGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

docsMcastAuthCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 2, 1, 1)
)
if mibBuilder.loadTexts:
    docsMcastAuthCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-MCAST-AUTH-MIB",
    **{"docsMcastAuthMib": docsMcastAuthMib,
       "docsMcastAuthMibObjects": docsMcastAuthMibObjects,
       "docsMcastAuthCtrl": docsMcastAuthCtrl,
       "docsMcastAuthCtrlEnable": docsMcastAuthCtrlEnable,
       "docsMcastAuthCtrlDefProfileNameList": docsMcastAuthCtrlDefProfileNameList,
       "docsMcastAuthCtrlDefAction": docsMcastAuthCtrlDefAction,
       "docsMcastAuthCtrlDefMaxNumSess": docsMcastAuthCtrlDefMaxNumSess,
       "docsMcastAuthCmtsCmStatusTable": docsMcastAuthCmtsCmStatusTable,
       "docsMcastAuthCmtsCmStatusEntry": docsMcastAuthCmtsCmStatusEntry,
       "docsMcastAuthCmtsCmStatusCfgProfileNameList": docsMcastAuthCmtsCmStatusCfgProfileNameList,
       "docsMcastAuthCmtsCmStatusCfgListId": docsMcastAuthCmtsCmStatusCfgListId,
       "docsMcastAuthCmtsCmStatusMaxNumSess": docsMcastAuthCmtsCmStatusMaxNumSess,
       "docsMcastAuthCmtsCmStatusCfgParamFlag": docsMcastAuthCmtsCmStatusCfgParamFlag,
       "docsMcastAuthProfileSessRuleTable": docsMcastAuthProfileSessRuleTable,
       "docsMcastAuthProfileSessRuleEntry": docsMcastAuthProfileSessRuleEntry,
       "docsMcastAuthProfileSessRuleId": docsMcastAuthProfileSessRuleId,
       "docsMcastAuthProfileSessRulePriority": docsMcastAuthProfileSessRulePriority,
       "docsMcastAuthProfileSessRulePrefixAddrType": docsMcastAuthProfileSessRulePrefixAddrType,
       "docsMcastAuthProfileSessRuleSrcPrefixAddr": docsMcastAuthProfileSessRuleSrcPrefixAddr,
       "docsMcastAuthProfileSessRuleSrcPrefixLen": docsMcastAuthProfileSessRuleSrcPrefixLen,
       "docsMcastAuthProfileSessRuleGrpPrefixAddr": docsMcastAuthProfileSessRuleGrpPrefixAddr,
       "docsMcastAuthProfileSessRuleGrpPrefixLen": docsMcastAuthProfileSessRuleGrpPrefixLen,
       "docsMcastAuthProfileSessRuleAction": docsMcastAuthProfileSessRuleAction,
       "docsMcastAuthProfileSessRuleRowStatus": docsMcastAuthProfileSessRuleRowStatus,
       "docsMcastAuthStaticSessRuleTable": docsMcastAuthStaticSessRuleTable,
       "docsMcastAuthStaticSessRuleEntry": docsMcastAuthStaticSessRuleEntry,
       "docsMcastAuthStaticSessRuleCfgListId": docsMcastAuthStaticSessRuleCfgListId,
       "docsMcastAuthStaticSessRuleId": docsMcastAuthStaticSessRuleId,
       "docsMcastAuthStaticSessRulePriority": docsMcastAuthStaticSessRulePriority,
       "docsMcastAuthStaticSessRulePrefixAddrType": docsMcastAuthStaticSessRulePrefixAddrType,
       "docsMcastAuthStaticSessRuleSrcPrefixAddr": docsMcastAuthStaticSessRuleSrcPrefixAddr,
       "docsMcastAuthStaticSessRuleSrcPrefixLen": docsMcastAuthStaticSessRuleSrcPrefixLen,
       "docsMcastAuthStaticSessRuleGrpPrefixAddr": docsMcastAuthStaticSessRuleGrpPrefixAddr,
       "docsMcastAuthStaticSessRuleGrpPrefixLen": docsMcastAuthStaticSessRuleGrpPrefixLen,
       "docsMcastAuthStaticSessRuleAction": docsMcastAuthStaticSessRuleAction,
       "docsMcastAuthProfilesTable": docsMcastAuthProfilesTable,
       "docsMcastAuthProfilesEntry": docsMcastAuthProfilesEntry,
       "docsMcastAuthProfilesName": docsMcastAuthProfilesName,
       "docsMcastAuthProfilesDescription": docsMcastAuthProfilesDescription,
       "docsMcastAuthProfilesRowStatus": docsMcastAuthProfilesRowStatus,
       "docsMcastAuthMibConformance": docsMcastAuthMibConformance,
       "docsMcastAuthMibCompliances": docsMcastAuthMibCompliances,
       "docsMcastAuthCompliance": docsMcastAuthCompliance,
       "docsMcastAuthMibGroups": docsMcastAuthMibGroups,
       "docsMcastAuthGroup": docsMcastAuthGroup}
)
