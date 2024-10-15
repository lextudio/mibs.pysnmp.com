# SNMP MIB module (DOCS-LOADBAL3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOCS-LOADBAL3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:05 2024
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

(NodeName,) = mibBuilder.importSymbols(
    "CLAB-TOPO-MIB",
    "NodeName")

(ChannelList,
 RcpId,
 docsIf3CmtsCmRegStatusEntry) = mibBuilder.importSymbols(
    "DOCS-IF3-MIB",
    "ChannelList",
    "RcpId",
    "docsIf3CmtsCmRegStatusEntry")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

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
 MacAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

docsLoadbal3Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22)
)
docsLoadbal3Mib.setRevisions(
        ("2008-05-22 00:00",
         "2007-12-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ChChgInitTechMap(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_DocsLoadbal3MibObjects_ObjectIdentity = ObjectIdentity
docsLoadbal3MibObjects = _DocsLoadbal3MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1)
)
_DocsLoadbal3System_ObjectIdentity = ObjectIdentity
docsLoadbal3System = _DocsLoadbal3System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 1)
)


class _DocsLoadbal3SystemEnable_Type(TruthValue):
    """Custom type docsLoadbal3SystemEnable based on TruthValue"""


_DocsLoadbal3SystemEnable_Object = MibScalar
docsLoadbal3SystemEnable = _DocsLoadbal3SystemEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 1, 1),
    _DocsLoadbal3SystemEnable_Type()
)
docsLoadbal3SystemEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadbal3SystemEnable.setStatus("current")
_DocsLoadbal3SystemEnableError_Type = SnmpAdminString
_DocsLoadbal3SystemEnableError_Object = MibScalar
docsLoadbal3SystemEnableError = _DocsLoadbal3SystemEnableError_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 1, 2),
    _DocsLoadbal3SystemEnableError_Type()
)
docsLoadbal3SystemEnableError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadbal3SystemEnableError.setStatus("current")
_DocsLoadbal3ChgOverGroup_ObjectIdentity = ObjectIdentity
docsLoadbal3ChgOverGroup = _DocsLoadbal3ChgOverGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 2)
)


class _DocsLoadbal3ChgOverGroupMacAddress_Type(MacAddress):
    """Custom type docsLoadbal3ChgOverGroupMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_DocsLoadbal3ChgOverGroupMacAddress_Object = MibScalar
docsLoadbal3ChgOverGroupMacAddress = _DocsLoadbal3ChgOverGroupMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 2, 1),
    _DocsLoadbal3ChgOverGroupMacAddress_Type()
)
docsLoadbal3ChgOverGroupMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadbal3ChgOverGroupMacAddress.setStatus("current")
_DocsLoadbal3ChgOverGroupInitTech_Type = ChChgInitTechMap
_DocsLoadbal3ChgOverGroupInitTech_Object = MibScalar
docsLoadbal3ChgOverGroupInitTech = _DocsLoadbal3ChgOverGroupInitTech_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 2, 2),
    _DocsLoadbal3ChgOverGroupInitTech_Type()
)
docsLoadbal3ChgOverGroupInitTech.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadbal3ChgOverGroupInitTech.setStatus("current")


class _DocsLoadbal3ChgOverGroupForceUCC_Type(TruthValue):
    """Custom type docsLoadbal3ChgOverGroupForceUCC based on TruthValue"""


_DocsLoadbal3ChgOverGroupForceUCC_Object = MibScalar
docsLoadbal3ChgOverGroupForceUCC = _DocsLoadbal3ChgOverGroupForceUCC_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 2, 3),
    _DocsLoadbal3ChgOverGroupForceUCC_Type()
)
docsLoadbal3ChgOverGroupForceUCC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadbal3ChgOverGroupForceUCC.setStatus("current")


class _DocsLoadbal3ChgOverGroupdownFrequency_Type(Unsigned32):
    """Custom type docsLoadbal3ChgOverGroupdownFrequency based on Unsigned32"""
    defaultValue = 0


_DocsLoadbal3ChgOverGroupdownFrequency_Object = MibScalar
docsLoadbal3ChgOverGroupdownFrequency = _DocsLoadbal3ChgOverGroupdownFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 2, 4),
    _DocsLoadbal3ChgOverGroupdownFrequency_Type()
)
docsLoadbal3ChgOverGroupdownFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadbal3ChgOverGroupdownFrequency.setStatus("current")


class _DocsLoadbal3ChgOverGroupMdIfIndex_Type(InterfaceIndexOrZero):
    """Custom type docsLoadbal3ChgOverGroupMdIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_DocsLoadbal3ChgOverGroupMdIfIndex_Object = MibScalar
docsLoadbal3ChgOverGroupMdIfIndex = _DocsLoadbal3ChgOverGroupMdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 2, 5),
    _DocsLoadbal3ChgOverGroupMdIfIndex_Type()
)
docsLoadbal3ChgOverGroupMdIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadbal3ChgOverGroupMdIfIndex.setStatus("current")


class _DocsLoadbal3ChgOverGroupRcpId_Type(RcpId):
    """Custom type docsLoadbal3ChgOverGroupRcpId based on RcpId"""
    defaultHexValue = "0000000000"


_DocsLoadbal3ChgOverGroupRcpId_Object = MibScalar
docsLoadbal3ChgOverGroupRcpId = _DocsLoadbal3ChgOverGroupRcpId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 2, 6),
    _DocsLoadbal3ChgOverGroupRcpId_Type()
)
docsLoadbal3ChgOverGroupRcpId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadbal3ChgOverGroupRcpId.setStatus("current")


class _DocsLoadbal3ChgOverGroupRccId_Type(Unsigned32):
    """Custom type docsLoadbal3ChgOverGroupRccId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsLoadbal3ChgOverGroupRccId_Type.__name__ = "Unsigned32"
_DocsLoadbal3ChgOverGroupRccId_Object = MibScalar
docsLoadbal3ChgOverGroupRccId = _DocsLoadbal3ChgOverGroupRccId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 2, 7),
    _DocsLoadbal3ChgOverGroupRccId_Type()
)
docsLoadbal3ChgOverGroupRccId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadbal3ChgOverGroupRccId.setStatus("current")


class _DocsLoadbal3ChgOverGroupUsChSet_Type(ChannelList):
    """Custom type docsLoadbal3ChgOverGroupUsChSet based on ChannelList"""
    defaultHexValue = ""


_DocsLoadbal3ChgOverGroupUsChSet_Object = MibScalar
docsLoadbal3ChgOverGroupUsChSet = _DocsLoadbal3ChgOverGroupUsChSet_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 2, 8),
    _DocsLoadbal3ChgOverGroupUsChSet_Type()
)
docsLoadbal3ChgOverGroupUsChSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadbal3ChgOverGroupUsChSet.setStatus("current")


class _DocsLoadbal3ChgOverGroupServiceFlowInfo_Type(OctetString):
    """Custom type docsLoadbal3ChgOverGroupServiceFlowInfo based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DocsLoadbal3ChgOverGroupServiceFlowInfo_Type.__name__ = "OctetString"
_DocsLoadbal3ChgOverGroupServiceFlowInfo_Object = MibScalar
docsLoadbal3ChgOverGroupServiceFlowInfo = _DocsLoadbal3ChgOverGroupServiceFlowInfo_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 2, 9),
    _DocsLoadbal3ChgOverGroupServiceFlowInfo_Type()
)
docsLoadbal3ChgOverGroupServiceFlowInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadbal3ChgOverGroupServiceFlowInfo.setStatus("current")


class _DocsLoadbal3ChgOverGroupTransactionId_Type(Unsigned32):
    """Custom type docsLoadbal3ChgOverGroupTransactionId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsLoadbal3ChgOverGroupTransactionId_Type.__name__ = "Unsigned32"
_DocsLoadbal3ChgOverGroupTransactionId_Object = MibScalar
docsLoadbal3ChgOverGroupTransactionId = _DocsLoadbal3ChgOverGroupTransactionId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 2, 10),
    _DocsLoadbal3ChgOverGroupTransactionId_Type()
)
docsLoadbal3ChgOverGroupTransactionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadbal3ChgOverGroupTransactionId.setStatus("current")


class _DocsLoadbal3ChgOverGroupCommit_Type(TruthValue):
    """Custom type docsLoadbal3ChgOverGroupCommit based on TruthValue"""


_DocsLoadbal3ChgOverGroupCommit_Object = MibScalar
docsLoadbal3ChgOverGroupCommit = _DocsLoadbal3ChgOverGroupCommit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 2, 11),
    _DocsLoadbal3ChgOverGroupCommit_Type()
)
docsLoadbal3ChgOverGroupCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadbal3ChgOverGroupCommit.setStatus("current")
_DocsLoadbal3ChgOverGroupLastCommit_Type = TimeStamp
_DocsLoadbal3ChgOverGroupLastCommit_Object = MibScalar
docsLoadbal3ChgOverGroupLastCommit = _DocsLoadbal3ChgOverGroupLastCommit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 2, 12),
    _DocsLoadbal3ChgOverGroupLastCommit_Type()
)
docsLoadbal3ChgOverGroupLastCommit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadbal3ChgOverGroupLastCommit.setStatus("current")
_DocsLoadbal3ChgOverStatusTable_Object = MibTable
docsLoadbal3ChgOverStatusTable = _DocsLoadbal3ChgOverStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 3)
)
if mibBuilder.loadTexts:
    docsLoadbal3ChgOverStatusTable.setStatus("current")
_DocsLoadbal3ChgOverStatusEntry_Object = MibTableRow
docsLoadbal3ChgOverStatusEntry = _DocsLoadbal3ChgOverStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 3, 1)
)
docsLoadbal3ChgOverStatusEntry.setIndexNames(
    (0, "DOCS-LOADBAL3-MIB", "docsLoadbal3ChgOverStatusId"),
)
if mibBuilder.loadTexts:
    docsLoadbal3ChgOverStatusEntry.setStatus("current")
_DocsLoadbal3ChgOverStatusId_Type = Unsigned32
_DocsLoadbal3ChgOverStatusId_Object = MibTableColumn
docsLoadbal3ChgOverStatusId = _DocsLoadbal3ChgOverStatusId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 3, 1, 1),
    _DocsLoadbal3ChgOverStatusId_Type()
)
docsLoadbal3ChgOverStatusId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsLoadbal3ChgOverStatusId.setStatus("current")
_DocsLoadbal3ChgOverStatusMacAddr_Type = MacAddress
_DocsLoadbal3ChgOverStatusMacAddr_Object = MibTableColumn
docsLoadbal3ChgOverStatusMacAddr = _DocsLoadbal3ChgOverStatusMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 3, 1, 2),
    _DocsLoadbal3ChgOverStatusMacAddr_Type()
)
docsLoadbal3ChgOverStatusMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadbal3ChgOverStatusMacAddr.setStatus("current")
_DocsLoadbal3ChgOverStatusInitTech_Type = ChChgInitTechMap
_DocsLoadbal3ChgOverStatusInitTech_Object = MibTableColumn
docsLoadbal3ChgOverStatusInitTech = _DocsLoadbal3ChgOverStatusInitTech_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 3, 1, 3),
    _DocsLoadbal3ChgOverStatusInitTech_Type()
)
docsLoadbal3ChgOverStatusInitTech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadbal3ChgOverStatusInitTech.setStatus("current")


class _DocsLoadbal3ChgOverStatusDownFrequency_Type(Unsigned32):
    """Custom type docsLoadbal3ChgOverStatusDownFrequency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_DocsLoadbal3ChgOverStatusDownFrequency_Type.__name__ = "Unsigned32"
_DocsLoadbal3ChgOverStatusDownFrequency_Object = MibTableColumn
docsLoadbal3ChgOverStatusDownFrequency = _DocsLoadbal3ChgOverStatusDownFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 3, 1, 4),
    _DocsLoadbal3ChgOverStatusDownFrequency_Type()
)
docsLoadbal3ChgOverStatusDownFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadbal3ChgOverStatusDownFrequency.setStatus("current")
_DocsLoadbal3ChgOverStatusMdIfIndex_Type = InterfaceIndex
_DocsLoadbal3ChgOverStatusMdIfIndex_Object = MibTableColumn
docsLoadbal3ChgOverStatusMdIfIndex = _DocsLoadbal3ChgOverStatusMdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 3, 1, 5),
    _DocsLoadbal3ChgOverStatusMdIfIndex_Type()
)
docsLoadbal3ChgOverStatusMdIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadbal3ChgOverStatusMdIfIndex.setStatus("current")
_DocsLoadbal3ChgOverStatusRcpId_Type = RcpId
_DocsLoadbal3ChgOverStatusRcpId_Object = MibTableColumn
docsLoadbal3ChgOverStatusRcpId = _DocsLoadbal3ChgOverStatusRcpId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 3, 1, 6),
    _DocsLoadbal3ChgOverStatusRcpId_Type()
)
docsLoadbal3ChgOverStatusRcpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadbal3ChgOverStatusRcpId.setStatus("current")


class _DocsLoadbal3ChgOverStatusRccId_Type(Unsigned32):
    """Custom type docsLoadbal3ChgOverStatusRccId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsLoadbal3ChgOverStatusRccId_Type.__name__ = "Unsigned32"
_DocsLoadbal3ChgOverStatusRccId_Object = MibTableColumn
docsLoadbal3ChgOverStatusRccId = _DocsLoadbal3ChgOverStatusRccId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 3, 1, 7),
    _DocsLoadbal3ChgOverStatusRccId_Type()
)
docsLoadbal3ChgOverStatusRccId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadbal3ChgOverStatusRccId.setStatus("current")
_DocsLoadbal3ChgOverStatusUsChSet_Type = ChannelList
_DocsLoadbal3ChgOverStatusUsChSet_Object = MibTableColumn
docsLoadbal3ChgOverStatusUsChSet = _DocsLoadbal3ChgOverStatusUsChSet_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 3, 1, 8),
    _DocsLoadbal3ChgOverStatusUsChSet_Type()
)
docsLoadbal3ChgOverStatusUsChSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadbal3ChgOverStatusUsChSet.setStatus("current")


class _DocsLoadbal3ChgOverStatusServiceFlowInfo_Type(OctetString):
    """Custom type docsLoadbal3ChgOverStatusServiceFlowInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 484),
    )


_DocsLoadbal3ChgOverStatusServiceFlowInfo_Type.__name__ = "OctetString"
_DocsLoadbal3ChgOverStatusServiceFlowInfo_Object = MibTableColumn
docsLoadbal3ChgOverStatusServiceFlowInfo = _DocsLoadbal3ChgOverStatusServiceFlowInfo_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 3, 1, 9),
    _DocsLoadbal3ChgOverStatusServiceFlowInfo_Type()
)
docsLoadbal3ChgOverStatusServiceFlowInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadbal3ChgOverStatusServiceFlowInfo.setStatus("current")


class _DocsLoadbal3ChgOverStatusCmd_Type(Integer32):
    """Custom type docsLoadbal3ChgOverStatusCmd based on Integer32"""
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
        *(("crossMD", 4),
          ("dbc", 3),
          ("dcc", 2),
          ("ucc", 1))
    )


_DocsLoadbal3ChgOverStatusCmd_Type.__name__ = "Integer32"
_DocsLoadbal3ChgOverStatusCmd_Object = MibTableColumn
docsLoadbal3ChgOverStatusCmd = _DocsLoadbal3ChgOverStatusCmd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 3, 1, 10),
    _DocsLoadbal3ChgOverStatusCmd_Type()
)
docsLoadbal3ChgOverStatusCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadbal3ChgOverStatusCmd.setStatus("current")


class _DocsLoadbal3ChgOverStatusTransactionId_Type(Unsigned32):
    """Custom type docsLoadbal3ChgOverStatusTransactionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsLoadbal3ChgOverStatusTransactionId_Type.__name__ = "Unsigned32"
_DocsLoadbal3ChgOverStatusTransactionId_Object = MibTableColumn
docsLoadbal3ChgOverStatusTransactionId = _DocsLoadbal3ChgOverStatusTransactionId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 3, 1, 11),
    _DocsLoadbal3ChgOverStatusTransactionId_Type()
)
docsLoadbal3ChgOverStatusTransactionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadbal3ChgOverStatusTransactionId.setStatus("current")


class _DocsLoadbal3ChgOverStatusValue_Type(Integer32):
    """Custom type docsLoadbal3ChgOverStatusValue based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("cmOperationRejected", 5),
          ("cmtsOperationRejected", 6),
          ("dbcTimeout", 11),
          ("messageSent", 1),
          ("modemDeparting", 3),
          ("noOpNeeded", 2),
          ("rejectinit", 9),
          ("success", 10),
          ("timeOutT13", 7),
          ("timeOutT15", 8),
          ("waitToSendMessage", 4))
    )


_DocsLoadbal3ChgOverStatusValue_Type.__name__ = "Integer32"
_DocsLoadbal3ChgOverStatusValue_Object = MibTableColumn
docsLoadbal3ChgOverStatusValue = _DocsLoadbal3ChgOverStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 3, 1, 12),
    _DocsLoadbal3ChgOverStatusValue_Type()
)
docsLoadbal3ChgOverStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadbal3ChgOverStatusValue.setStatus("current")
_DocsLoadbal3ChgOverStatusUpdate_Type = TimeStamp
_DocsLoadbal3ChgOverStatusUpdate_Object = MibTableColumn
docsLoadbal3ChgOverStatusUpdate = _DocsLoadbal3ChgOverStatusUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 3, 1, 13),
    _DocsLoadbal3ChgOverStatusUpdate_Type()
)
docsLoadbal3ChgOverStatusUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadbal3ChgOverStatusUpdate.setStatus("current")
_DocsLoadbal3CmtsCmParamsTable_Object = MibTable
docsLoadbal3CmtsCmParamsTable = _DocsLoadbal3CmtsCmParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 4)
)
if mibBuilder.loadTexts:
    docsLoadbal3CmtsCmParamsTable.setStatus("current")
_DocsLoadbal3CmtsCmParamsEntry_Object = MibTableRow
docsLoadbal3CmtsCmParamsEntry = _DocsLoadbal3CmtsCmParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 4, 1)
)
if mibBuilder.loadTexts:
    docsLoadbal3CmtsCmParamsEntry.setStatus("current")
_DocsLoadbal3CmtsCmParamsProvGrpId_Type = Unsigned32
_DocsLoadbal3CmtsCmParamsProvGrpId_Object = MibTableColumn
docsLoadbal3CmtsCmParamsProvGrpId = _DocsLoadbal3CmtsCmParamsProvGrpId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 4, 1, 1),
    _DocsLoadbal3CmtsCmParamsProvGrpId_Type()
)
docsLoadbal3CmtsCmParamsProvGrpId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadbal3CmtsCmParamsProvGrpId.setStatus("current")
_DocsLoadbal3CmtsCmParamsCurrentGrpId_Type = Unsigned32
_DocsLoadbal3CmtsCmParamsCurrentGrpId_Object = MibTableColumn
docsLoadbal3CmtsCmParamsCurrentGrpId = _DocsLoadbal3CmtsCmParamsCurrentGrpId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 4, 1, 2),
    _DocsLoadbal3CmtsCmParamsCurrentGrpId_Type()
)
docsLoadbal3CmtsCmParamsCurrentGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadbal3CmtsCmParamsCurrentGrpId.setStatus("current")


class _DocsLoadbal3CmtsCmParamsProvServiceTypeID_Type(SnmpAdminString):
    """Custom type docsLoadbal3CmtsCmParamsProvServiceTypeID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DocsLoadbal3CmtsCmParamsProvServiceTypeID_Type.__name__ = "SnmpAdminString"
_DocsLoadbal3CmtsCmParamsProvServiceTypeID_Object = MibTableColumn
docsLoadbal3CmtsCmParamsProvServiceTypeID = _DocsLoadbal3CmtsCmParamsProvServiceTypeID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 4, 1, 3),
    _DocsLoadbal3CmtsCmParamsProvServiceTypeID_Type()
)
docsLoadbal3CmtsCmParamsProvServiceTypeID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadbal3CmtsCmParamsProvServiceTypeID.setStatus("current")


class _DocsLoadbal3CmtsCmParamsCurrentServiceTypeID_Type(SnmpAdminString):
    """Custom type docsLoadbal3CmtsCmParamsCurrentServiceTypeID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DocsLoadbal3CmtsCmParamsCurrentServiceTypeID_Type.__name__ = "SnmpAdminString"
_DocsLoadbal3CmtsCmParamsCurrentServiceTypeID_Object = MibTableColumn
docsLoadbal3CmtsCmParamsCurrentServiceTypeID = _DocsLoadbal3CmtsCmParamsCurrentServiceTypeID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 4, 1, 4),
    _DocsLoadbal3CmtsCmParamsCurrentServiceTypeID_Type()
)
docsLoadbal3CmtsCmParamsCurrentServiceTypeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadbal3CmtsCmParamsCurrentServiceTypeID.setStatus("current")
_DocsLoadbal3CmtsCmParamsPolicyId_Type = Unsigned32
_DocsLoadbal3CmtsCmParamsPolicyId_Object = MibTableColumn
docsLoadbal3CmtsCmParamsPolicyId = _DocsLoadbal3CmtsCmParamsPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 4, 1, 5),
    _DocsLoadbal3CmtsCmParamsPolicyId_Type()
)
docsLoadbal3CmtsCmParamsPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadbal3CmtsCmParamsPolicyId.setStatus("current")
_DocsLoadbal3CmtsCmParamsPriority_Type = Unsigned32
_DocsLoadbal3CmtsCmParamsPriority_Object = MibTableColumn
docsLoadbal3CmtsCmParamsPriority = _DocsLoadbal3CmtsCmParamsPriority_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 4, 1, 6),
    _DocsLoadbal3CmtsCmParamsPriority_Type()
)
docsLoadbal3CmtsCmParamsPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadbal3CmtsCmParamsPriority.setStatus("current")
_DocsLoadbal3GeneralGrpDefaults_ObjectIdentity = ObjectIdentity
docsLoadbal3GeneralGrpDefaults = _DocsLoadbal3GeneralGrpDefaults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 5)
)


class _DocsLoadbal3GeneralGrpDefaultsEnable_Type(TruthValue):
    """Custom type docsLoadbal3GeneralGrpDefaultsEnable based on TruthValue"""


_DocsLoadbal3GeneralGrpDefaultsEnable_Object = MibScalar
docsLoadbal3GeneralGrpDefaultsEnable = _DocsLoadbal3GeneralGrpDefaultsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 5, 1),
    _DocsLoadbal3GeneralGrpDefaultsEnable_Type()
)
docsLoadbal3GeneralGrpDefaultsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadbal3GeneralGrpDefaultsEnable.setStatus("current")


class _DocsLoadbal3GeneralGrpDefaultsPolicyId_Type(Unsigned32):
    """Custom type docsLoadbal3GeneralGrpDefaultsPolicyId based on Unsigned32"""
    defaultValue = 0


_DocsLoadbal3GeneralGrpDefaultsPolicyId_Object = MibScalar
docsLoadbal3GeneralGrpDefaultsPolicyId = _DocsLoadbal3GeneralGrpDefaultsPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 5, 2),
    _DocsLoadbal3GeneralGrpDefaultsPolicyId_Type()
)
docsLoadbal3GeneralGrpDefaultsPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadbal3GeneralGrpDefaultsPolicyId.setStatus("current")


class _DocsLoadbal3GeneralGrpDefaultsInitTech_Type(ChChgInitTechMap):
    """Custom type docsLoadbal3GeneralGrpDefaultsInitTech based on ChChgInitTechMap"""
    defaultHexValue = "F8"


_DocsLoadbal3GeneralGrpDefaultsInitTech_Object = MibScalar
docsLoadbal3GeneralGrpDefaultsInitTech = _DocsLoadbal3GeneralGrpDefaultsInitTech_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 5, 3),
    _DocsLoadbal3GeneralGrpDefaultsInitTech_Type()
)
docsLoadbal3GeneralGrpDefaultsInitTech.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadbal3GeneralGrpDefaultsInitTech.setStatus("current")
_DocsLoadbal3GeneralGrpCfgTable_Object = MibTable
docsLoadbal3GeneralGrpCfgTable = _DocsLoadbal3GeneralGrpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 6)
)
if mibBuilder.loadTexts:
    docsLoadbal3GeneralGrpCfgTable.setStatus("current")
_DocsLoadbal3GeneralGrpCfgEntry_Object = MibTableRow
docsLoadbal3GeneralGrpCfgEntry = _DocsLoadbal3GeneralGrpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 6, 1)
)
docsLoadbal3GeneralGrpCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-LOADBAL3-MIB", "docsLoadbal3GeneralGrpCfgNodeName"),
)
if mibBuilder.loadTexts:
    docsLoadbal3GeneralGrpCfgEntry.setStatus("current")
_DocsLoadbal3GeneralGrpCfgNodeName_Type = NodeName
_DocsLoadbal3GeneralGrpCfgNodeName_Object = MibTableColumn
docsLoadbal3GeneralGrpCfgNodeName = _DocsLoadbal3GeneralGrpCfgNodeName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 6, 1, 1),
    _DocsLoadbal3GeneralGrpCfgNodeName_Type()
)
docsLoadbal3GeneralGrpCfgNodeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsLoadbal3GeneralGrpCfgNodeName.setStatus("current")


class _DocsLoadbal3GeneralGrpCfgEnable_Type(TruthValue):
    """Custom type docsLoadbal3GeneralGrpCfgEnable based on TruthValue"""


_DocsLoadbal3GeneralGrpCfgEnable_Object = MibTableColumn
docsLoadbal3GeneralGrpCfgEnable = _DocsLoadbal3GeneralGrpCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 6, 1, 2),
    _DocsLoadbal3GeneralGrpCfgEnable_Type()
)
docsLoadbal3GeneralGrpCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadbal3GeneralGrpCfgEnable.setStatus("current")


class _DocsLoadbal3GeneralGrpCfgPolicyId_Type(Unsigned32):
    """Custom type docsLoadbal3GeneralGrpCfgPolicyId based on Unsigned32"""
    defaultValue = 0


_DocsLoadbal3GeneralGrpCfgPolicyId_Object = MibTableColumn
docsLoadbal3GeneralGrpCfgPolicyId = _DocsLoadbal3GeneralGrpCfgPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 6, 1, 3),
    _DocsLoadbal3GeneralGrpCfgPolicyId_Type()
)
docsLoadbal3GeneralGrpCfgPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadbal3GeneralGrpCfgPolicyId.setStatus("current")


class _DocsLoadbal3GeneralGrpCfgInitTech_Type(ChChgInitTechMap):
    """Custom type docsLoadbal3GeneralGrpCfgInitTech based on ChChgInitTechMap"""
    defaultHexValue = "00"


_DocsLoadbal3GeneralGrpCfgInitTech_Object = MibTableColumn
docsLoadbal3GeneralGrpCfgInitTech = _DocsLoadbal3GeneralGrpCfgInitTech_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 6, 1, 4),
    _DocsLoadbal3GeneralGrpCfgInitTech_Type()
)
docsLoadbal3GeneralGrpCfgInitTech.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadbal3GeneralGrpCfgInitTech.setStatus("current")
_DocsLoadbal3GeneralGrpCfgStatus_Type = RowStatus
_DocsLoadbal3GeneralGrpCfgStatus_Object = MibTableColumn
docsLoadbal3GeneralGrpCfgStatus = _DocsLoadbal3GeneralGrpCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 6, 1, 5),
    _DocsLoadbal3GeneralGrpCfgStatus_Type()
)
docsLoadbal3GeneralGrpCfgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadbal3GeneralGrpCfgStatus.setStatus("current")
_DocsLoadbal3ResGrpCfgTable_Object = MibTable
docsLoadbal3ResGrpCfgTable = _DocsLoadbal3ResGrpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 7)
)
if mibBuilder.loadTexts:
    docsLoadbal3ResGrpCfgTable.setStatus("current")
_DocsLoadbal3ResGrpCfgEntry_Object = MibTableRow
docsLoadbal3ResGrpCfgEntry = _DocsLoadbal3ResGrpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 7, 1)
)
docsLoadbal3ResGrpCfgEntry.setIndexNames(
    (0, "DOCS-LOADBAL3-MIB", "docsLoadbal3ResGrpCfgId"),
)
if mibBuilder.loadTexts:
    docsLoadbal3ResGrpCfgEntry.setStatus("current")
_DocsLoadbal3ResGrpCfgId_Type = Unsigned32
_DocsLoadbal3ResGrpCfgId_Object = MibTableColumn
docsLoadbal3ResGrpCfgId = _DocsLoadbal3ResGrpCfgId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 7, 1, 1),
    _DocsLoadbal3ResGrpCfgId_Type()
)
docsLoadbal3ResGrpCfgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsLoadbal3ResGrpCfgId.setStatus("current")
_DocsLoadbal3ResGrpCfgMdIfIndex_Type = InterfaceIndexOrZero
_DocsLoadbal3ResGrpCfgMdIfIndex_Object = MibTableColumn
docsLoadbal3ResGrpCfgMdIfIndex = _DocsLoadbal3ResGrpCfgMdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 7, 1, 2),
    _DocsLoadbal3ResGrpCfgMdIfIndex_Type()
)
docsLoadbal3ResGrpCfgMdIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadbal3ResGrpCfgMdIfIndex.setStatus("current")


class _DocsLoadbal3ResGrpCfgDsChList_Type(ChannelList):
    """Custom type docsLoadbal3ResGrpCfgDsChList based on ChannelList"""
    defaultHexValue = ""


_DocsLoadbal3ResGrpCfgDsChList_Object = MibTableColumn
docsLoadbal3ResGrpCfgDsChList = _DocsLoadbal3ResGrpCfgDsChList_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 7, 1, 3),
    _DocsLoadbal3ResGrpCfgDsChList_Type()
)
docsLoadbal3ResGrpCfgDsChList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadbal3ResGrpCfgDsChList.setStatus("current")


class _DocsLoadbal3ResGrpCfgUsChList_Type(ChannelList):
    """Custom type docsLoadbal3ResGrpCfgUsChList based on ChannelList"""
    defaultHexValue = ""


_DocsLoadbal3ResGrpCfgUsChList_Object = MibTableColumn
docsLoadbal3ResGrpCfgUsChList = _DocsLoadbal3ResGrpCfgUsChList_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 7, 1, 4),
    _DocsLoadbal3ResGrpCfgUsChList_Type()
)
docsLoadbal3ResGrpCfgUsChList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadbal3ResGrpCfgUsChList.setStatus("current")


class _DocsLoadbal3ResGrpCfgEnable_Type(TruthValue):
    """Custom type docsLoadbal3ResGrpCfgEnable based on TruthValue"""


_DocsLoadbal3ResGrpCfgEnable_Object = MibTableColumn
docsLoadbal3ResGrpCfgEnable = _DocsLoadbal3ResGrpCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 7, 1, 5),
    _DocsLoadbal3ResGrpCfgEnable_Type()
)
docsLoadbal3ResGrpCfgEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadbal3ResGrpCfgEnable.setStatus("current")


class _DocsLoadbal3ResGrpCfgInitTech_Type(ChChgInitTechMap):
    """Custom type docsLoadbal3ResGrpCfgInitTech based on ChChgInitTechMap"""
    defaultHexValue = "F8"


_DocsLoadbal3ResGrpCfgInitTech_Object = MibTableColumn
docsLoadbal3ResGrpCfgInitTech = _DocsLoadbal3ResGrpCfgInitTech_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 7, 1, 6),
    _DocsLoadbal3ResGrpCfgInitTech_Type()
)
docsLoadbal3ResGrpCfgInitTech.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadbal3ResGrpCfgInitTech.setStatus("current")


class _DocsLoadbal3ResGrpCfgPolicyId_Type(Unsigned32):
    """Custom type docsLoadbal3ResGrpCfgPolicyId based on Unsigned32"""
    defaultValue = 0


_DocsLoadbal3ResGrpCfgPolicyId_Object = MibTableColumn
docsLoadbal3ResGrpCfgPolicyId = _DocsLoadbal3ResGrpCfgPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 7, 1, 7),
    _DocsLoadbal3ResGrpCfgPolicyId_Type()
)
docsLoadbal3ResGrpCfgPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadbal3ResGrpCfgPolicyId.setStatus("current")
_DocsLoadbal3ResGrpCfgServiceTypeId_Type = SnmpTagList
_DocsLoadbal3ResGrpCfgServiceTypeId_Object = MibTableColumn
docsLoadbal3ResGrpCfgServiceTypeId = _DocsLoadbal3ResGrpCfgServiceTypeId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 7, 1, 8),
    _DocsLoadbal3ResGrpCfgServiceTypeId_Type()
)
docsLoadbal3ResGrpCfgServiceTypeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadbal3ResGrpCfgServiceTypeId.setStatus("current")
_DocsLoadbal3ResGrpCfgStatus_Type = RowStatus
_DocsLoadbal3ResGrpCfgStatus_Object = MibTableColumn
docsLoadbal3ResGrpCfgStatus = _DocsLoadbal3ResGrpCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 7, 1, 9),
    _DocsLoadbal3ResGrpCfgStatus_Type()
)
docsLoadbal3ResGrpCfgStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadbal3ResGrpCfgStatus.setStatus("current")
_DocsLoadbal3GrpStatusTable_Object = MibTable
docsLoadbal3GrpStatusTable = _DocsLoadbal3GrpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 8)
)
if mibBuilder.loadTexts:
    docsLoadbal3GrpStatusTable.setStatus("current")
_DocsLoadbal3GrpStatusEntry_Object = MibTableRow
docsLoadbal3GrpStatusEntry = _DocsLoadbal3GrpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 8, 1)
)
docsLoadbal3GrpStatusEntry.setIndexNames(
    (0, "DOCS-LOADBAL3-MIB", "docsLoadbal3GrpStatusId"),
)
if mibBuilder.loadTexts:
    docsLoadbal3GrpStatusEntry.setStatus("current")
_DocsLoadbal3GrpStatusId_Type = Unsigned32
_DocsLoadbal3GrpStatusId_Object = MibTableColumn
docsLoadbal3GrpStatusId = _DocsLoadbal3GrpStatusId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 8, 1, 1),
    _DocsLoadbal3GrpStatusId_Type()
)
docsLoadbal3GrpStatusId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsLoadbal3GrpStatusId.setStatus("current")
_DocsLoadbal3GrpStatusCfgIdOrZero_Type = Unsigned32
_DocsLoadbal3GrpStatusCfgIdOrZero_Object = MibTableColumn
docsLoadbal3GrpStatusCfgIdOrZero = _DocsLoadbal3GrpStatusCfgIdOrZero_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 8, 1, 2),
    _DocsLoadbal3GrpStatusCfgIdOrZero_Type()
)
docsLoadbal3GrpStatusCfgIdOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadbal3GrpStatusCfgIdOrZero.setStatus("current")
_DocsLoadbal3GrpStatusMdIfIndex_Type = InterfaceIndexOrZero
_DocsLoadbal3GrpStatusMdIfIndex_Object = MibTableColumn
docsLoadbal3GrpStatusMdIfIndex = _DocsLoadbal3GrpStatusMdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 8, 1, 3),
    _DocsLoadbal3GrpStatusMdIfIndex_Type()
)
docsLoadbal3GrpStatusMdIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadbal3GrpStatusMdIfIndex.setStatus("current")
_DocsLoadbal3GrpStatusMdCmSgId_Type = Unsigned32
_DocsLoadbal3GrpStatusMdCmSgId_Object = MibTableColumn
docsLoadbal3GrpStatusMdCmSgId = _DocsLoadbal3GrpStatusMdCmSgId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 8, 1, 4),
    _DocsLoadbal3GrpStatusMdCmSgId_Type()
)
docsLoadbal3GrpStatusMdCmSgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadbal3GrpStatusMdCmSgId.setStatus("current")
_DocsLoadbal3GrpStatusDsChList_Type = ChannelList
_DocsLoadbal3GrpStatusDsChList_Object = MibTableColumn
docsLoadbal3GrpStatusDsChList = _DocsLoadbal3GrpStatusDsChList_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 8, 1, 5),
    _DocsLoadbal3GrpStatusDsChList_Type()
)
docsLoadbal3GrpStatusDsChList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadbal3GrpStatusDsChList.setStatus("current")
_DocsLoadbal3GrpStatusUsChList_Type = ChannelList
_DocsLoadbal3GrpStatusUsChList_Object = MibTableColumn
docsLoadbal3GrpStatusUsChList = _DocsLoadbal3GrpStatusUsChList_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 8, 1, 6),
    _DocsLoadbal3GrpStatusUsChList_Type()
)
docsLoadbal3GrpStatusUsChList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadbal3GrpStatusUsChList.setStatus("current")
_DocsLoadbal3GrpStatusEnable_Type = TruthValue
_DocsLoadbal3GrpStatusEnable_Object = MibTableColumn
docsLoadbal3GrpStatusEnable = _DocsLoadbal3GrpStatusEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 8, 1, 7),
    _DocsLoadbal3GrpStatusEnable_Type()
)
docsLoadbal3GrpStatusEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadbal3GrpStatusEnable.setStatus("current")
_DocsLoadbal3GrpStatusInitTech_Type = ChChgInitTechMap
_DocsLoadbal3GrpStatusInitTech_Object = MibTableColumn
docsLoadbal3GrpStatusInitTech = _DocsLoadbal3GrpStatusInitTech_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 8, 1, 8),
    _DocsLoadbal3GrpStatusInitTech_Type()
)
docsLoadbal3GrpStatusInitTech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadbal3GrpStatusInitTech.setStatus("current")
_DocsLoadbal3GrpStatusPolicyId_Type = Unsigned32
_DocsLoadbal3GrpStatusPolicyId_Object = MibTableColumn
docsLoadbal3GrpStatusPolicyId = _DocsLoadbal3GrpStatusPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 8, 1, 9),
    _DocsLoadbal3GrpStatusPolicyId_Type()
)
docsLoadbal3GrpStatusPolicyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadbal3GrpStatusPolicyId.setStatus("current")
_DocsLoadbal3GrpStatusChgOverSuccess_Type = Counter32
_DocsLoadbal3GrpStatusChgOverSuccess_Object = MibTableColumn
docsLoadbal3GrpStatusChgOverSuccess = _DocsLoadbal3GrpStatusChgOverSuccess_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 8, 1, 10),
    _DocsLoadbal3GrpStatusChgOverSuccess_Type()
)
docsLoadbal3GrpStatusChgOverSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadbal3GrpStatusChgOverSuccess.setStatus("current")
_DocsLoadbal3GrpStatusChgOverFails_Type = Counter32
_DocsLoadbal3GrpStatusChgOverFails_Object = MibTableColumn
docsLoadbal3GrpStatusChgOverFails = _DocsLoadbal3GrpStatusChgOverFails_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 8, 1, 11),
    _DocsLoadbal3GrpStatusChgOverFails_Type()
)
docsLoadbal3GrpStatusChgOverFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadbal3GrpStatusChgOverFails.setStatus("current")
_DocsLoadbal3RestrictCmCfgTable_Object = MibTable
docsLoadbal3RestrictCmCfgTable = _DocsLoadbal3RestrictCmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 9)
)
if mibBuilder.loadTexts:
    docsLoadbal3RestrictCmCfgTable.setStatus("current")
_DocsLoadbal3RestrictCmCfgEntry_Object = MibTableRow
docsLoadbal3RestrictCmCfgEntry = _DocsLoadbal3RestrictCmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 9, 1)
)
docsLoadbal3RestrictCmCfgEntry.setIndexNames(
    (0, "DOCS-LOADBAL3-MIB", "docsLoadbal3RestrictCmCfgId"),
)
if mibBuilder.loadTexts:
    docsLoadbal3RestrictCmCfgEntry.setStatus("current")
_DocsLoadbal3RestrictCmCfgId_Type = Unsigned32
_DocsLoadbal3RestrictCmCfgId_Object = MibTableColumn
docsLoadbal3RestrictCmCfgId = _DocsLoadbal3RestrictCmCfgId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 9, 1, 1),
    _DocsLoadbal3RestrictCmCfgId_Type()
)
docsLoadbal3RestrictCmCfgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsLoadbal3RestrictCmCfgId.setStatus("current")


class _DocsLoadbal3RestrictCmCfgMacAddr_Type(MacAddress):
    """Custom type docsLoadbal3RestrictCmCfgMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_DocsLoadbal3RestrictCmCfgMacAddr_Object = MibTableColumn
docsLoadbal3RestrictCmCfgMacAddr = _DocsLoadbal3RestrictCmCfgMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 9, 1, 2),
    _DocsLoadbal3RestrictCmCfgMacAddr_Type()
)
docsLoadbal3RestrictCmCfgMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadbal3RestrictCmCfgMacAddr.setStatus("current")


class _DocsLoadbal3RestrictCmCfgMacAddrMask_Type(MacAddress):
    """Custom type docsLoadbal3RestrictCmCfgMacAddrMask based on MacAddress"""
    defaultHexValue = "FFFFFFFFFFFF"


_DocsLoadbal3RestrictCmCfgMacAddrMask_Object = MibTableColumn
docsLoadbal3RestrictCmCfgMacAddrMask = _DocsLoadbal3RestrictCmCfgMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 9, 1, 3),
    _DocsLoadbal3RestrictCmCfgMacAddrMask_Type()
)
docsLoadbal3RestrictCmCfgMacAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadbal3RestrictCmCfgMacAddrMask.setStatus("current")


class _DocsLoadbal3RestrictCmCfgGrpId_Type(Unsigned32):
    """Custom type docsLoadbal3RestrictCmCfgGrpId based on Unsigned32"""
    defaultValue = 0


_DocsLoadbal3RestrictCmCfgGrpId_Object = MibTableColumn
docsLoadbal3RestrictCmCfgGrpId = _DocsLoadbal3RestrictCmCfgGrpId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 9, 1, 4),
    _DocsLoadbal3RestrictCmCfgGrpId_Type()
)
docsLoadbal3RestrictCmCfgGrpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadbal3RestrictCmCfgGrpId.setStatus("current")


class _DocsLoadbal3RestrictCmCfgServiceTypeId_Type(OctetString):
    """Custom type docsLoadbal3RestrictCmCfgServiceTypeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DocsLoadbal3RestrictCmCfgServiceTypeId_Type.__name__ = "OctetString"
_DocsLoadbal3RestrictCmCfgServiceTypeId_Object = MibTableColumn
docsLoadbal3RestrictCmCfgServiceTypeId = _DocsLoadbal3RestrictCmCfgServiceTypeId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 9, 1, 5),
    _DocsLoadbal3RestrictCmCfgServiceTypeId_Type()
)
docsLoadbal3RestrictCmCfgServiceTypeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadbal3RestrictCmCfgServiceTypeId.setStatus("current")
_DocsLoadbal3RestrictCmCfgStatus_Type = RowStatus
_DocsLoadbal3RestrictCmCfgStatus_Object = MibTableColumn
docsLoadbal3RestrictCmCfgStatus = _DocsLoadbal3RestrictCmCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 9, 1, 6),
    _DocsLoadbal3RestrictCmCfgStatus_Type()
)
docsLoadbal3RestrictCmCfgStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadbal3RestrictCmCfgStatus.setStatus("current")
_DocsLoadbal3PolicyTable_Object = MibTable
docsLoadbal3PolicyTable = _DocsLoadbal3PolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 10)
)
if mibBuilder.loadTexts:
    docsLoadbal3PolicyTable.setStatus("current")
_DocsLoadbal3PolicyEntry_Object = MibTableRow
docsLoadbal3PolicyEntry = _DocsLoadbal3PolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 10, 1)
)
docsLoadbal3PolicyEntry.setIndexNames(
    (0, "DOCS-LOADBAL3-MIB", "docsLoadbal3PolicyId"),
    (0, "DOCS-LOADBAL3-MIB", "docsLoadbal3PolicyRuleId"),
)
if mibBuilder.loadTexts:
    docsLoadbal3PolicyEntry.setStatus("current")
_DocsLoadbal3PolicyId_Type = Unsigned32
_DocsLoadbal3PolicyId_Object = MibTableColumn
docsLoadbal3PolicyId = _DocsLoadbal3PolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 10, 1, 1),
    _DocsLoadbal3PolicyId_Type()
)
docsLoadbal3PolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsLoadbal3PolicyId.setStatus("current")
_DocsLoadbal3PolicyRuleId_Type = Unsigned32
_DocsLoadbal3PolicyRuleId_Object = MibTableColumn
docsLoadbal3PolicyRuleId = _DocsLoadbal3PolicyRuleId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 10, 1, 2),
    _DocsLoadbal3PolicyRuleId_Type()
)
docsLoadbal3PolicyRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsLoadbal3PolicyRuleId.setStatus("current")
_DocsLoadbal3PolicyPtr_Type = RowPointer
_DocsLoadbal3PolicyPtr_Object = MibTableColumn
docsLoadbal3PolicyPtr = _DocsLoadbal3PolicyPtr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 10, 1, 3),
    _DocsLoadbal3PolicyPtr_Type()
)
docsLoadbal3PolicyPtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadbal3PolicyPtr.setStatus("current")
_DocsLoadbal3PolicyRowStatus_Type = RowStatus
_DocsLoadbal3PolicyRowStatus_Object = MibTableColumn
docsLoadbal3PolicyRowStatus = _DocsLoadbal3PolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 10, 1, 4),
    _DocsLoadbal3PolicyRowStatus_Type()
)
docsLoadbal3PolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadbal3PolicyRowStatus.setStatus("current")
_DocsLoadbal3BasicRuleTable_Object = MibTable
docsLoadbal3BasicRuleTable = _DocsLoadbal3BasicRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 11)
)
if mibBuilder.loadTexts:
    docsLoadbal3BasicRuleTable.setStatus("current")
_DocsLoadbal3BasicRuleEntry_Object = MibTableRow
docsLoadbal3BasicRuleEntry = _DocsLoadbal3BasicRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 11, 1)
)
docsLoadbal3BasicRuleEntry.setIndexNames(
    (0, "DOCS-LOADBAL3-MIB", "docsLoadbal3BasicRuleId"),
)
if mibBuilder.loadTexts:
    docsLoadbal3BasicRuleEntry.setStatus("current")
_DocsLoadbal3BasicRuleId_Type = Unsigned32
_DocsLoadbal3BasicRuleId_Object = MibTableColumn
docsLoadbal3BasicRuleId = _DocsLoadbal3BasicRuleId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 11, 1, 1),
    _DocsLoadbal3BasicRuleId_Type()
)
docsLoadbal3BasicRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsLoadbal3BasicRuleId.setStatus("current")


class _DocsLoadbal3BasicRuleEnable_Type(Integer32):
    """Custom type docsLoadbal3BasicRuleEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("disabledPeriod", 3),
          ("enabled", 1))
    )


_DocsLoadbal3BasicRuleEnable_Type.__name__ = "Integer32"
_DocsLoadbal3BasicRuleEnable_Object = MibTableColumn
docsLoadbal3BasicRuleEnable = _DocsLoadbal3BasicRuleEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 11, 1, 2),
    _DocsLoadbal3BasicRuleEnable_Type()
)
docsLoadbal3BasicRuleEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadbal3BasicRuleEnable.setStatus("current")


class _DocsLoadbal3BasicRuleDisStart_Type(Unsigned32):
    """Custom type docsLoadbal3BasicRuleDisStart based on Unsigned32"""
    defaultValue = 0


_DocsLoadbal3BasicRuleDisStart_Object = MibTableColumn
docsLoadbal3BasicRuleDisStart = _DocsLoadbal3BasicRuleDisStart_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 11, 1, 3),
    _DocsLoadbal3BasicRuleDisStart_Type()
)
docsLoadbal3BasicRuleDisStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadbal3BasicRuleDisStart.setStatus("current")


class _DocsLoadbal3BasicRuleDisPeriod_Type(Unsigned32):
    """Custom type docsLoadbal3BasicRuleDisPeriod based on Unsigned32"""
    defaultValue = 0


_DocsLoadbal3BasicRuleDisPeriod_Object = MibTableColumn
docsLoadbal3BasicRuleDisPeriod = _DocsLoadbal3BasicRuleDisPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 11, 1, 4),
    _DocsLoadbal3BasicRuleDisPeriod_Type()
)
docsLoadbal3BasicRuleDisPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadbal3BasicRuleDisPeriod.setStatus("current")
_DocsLoadbal3BasicRuleRowStatus_Type = RowStatus
_DocsLoadbal3BasicRuleRowStatus_Object = MibTableColumn
docsLoadbal3BasicRuleRowStatus = _DocsLoadbal3BasicRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 1, 11, 1, 5),
    _DocsLoadbal3BasicRuleRowStatus_Type()
)
docsLoadbal3BasicRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadbal3BasicRuleRowStatus.setStatus("current")
_DocsLoadbal3MibConformance_ObjectIdentity = ObjectIdentity
docsLoadbal3MibConformance = _DocsLoadbal3MibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 2)
)
_DocsLoadbal3MibCompliances_ObjectIdentity = ObjectIdentity
docsLoadbal3MibCompliances = _DocsLoadbal3MibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 2, 1)
)
_DocsLoadbal3MibGroups_ObjectIdentity = ObjectIdentity
docsLoadbal3MibGroups = _DocsLoadbal3MibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 2, 2)
)
docsIf3CmtsCmRegStatusEntry.registerAugmentions(
    ("DOCS-LOADBAL3-MIB",
     "docsLoadbal3CmtsCmParamsEntry")
)
docsLoadbal3CmtsCmParamsEntry.setIndexNames(*docsIf3CmtsCmRegStatusEntry.getIndexNames())

# Managed Objects groups

docsLoadbal3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 2, 2, 1)
)
docsLoadbal3Group.setObjects(
      *(("DOCS-LOADBAL3-MIB", "docsLoadbal3SystemEnable"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3SystemEnableError"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3PolicyPtr"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3PolicyRowStatus"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3BasicRuleEnable"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3BasicRuleDisStart"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3BasicRuleDisPeriod"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3BasicRuleRowStatus"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ChgOverGroupMacAddress"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ChgOverGroupInitTech"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ChgOverGroupForceUCC"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ChgOverGroupdownFrequency"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ChgOverGroupMdIfIndex"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ChgOverGroupRcpId"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ChgOverGroupRccId"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ChgOverGroupUsChSet"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ChgOverGroupServiceFlowInfo"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ChgOverGroupTransactionId"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ChgOverGroupCommit"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ChgOverGroupLastCommit"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ChgOverStatusMacAddr"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ChgOverStatusInitTech"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ChgOverStatusDownFrequency"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ChgOverStatusMdIfIndex"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ChgOverStatusRcpId"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ChgOverStatusRccId"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ChgOverStatusUsChSet"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ChgOverStatusServiceFlowInfo"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ChgOverStatusCmd"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ChgOverStatusTransactionId"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ChgOverStatusValue"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ChgOverStatusUpdate"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3CmtsCmParamsProvGrpId"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3CmtsCmParamsCurrentGrpId"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3CmtsCmParamsProvServiceTypeID"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3CmtsCmParamsCurrentServiceTypeID"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3CmtsCmParamsPolicyId"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3CmtsCmParamsPriority"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3GeneralGrpDefaultsEnable"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3GeneralGrpDefaultsPolicyId"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3GeneralGrpDefaultsInitTech"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3GeneralGrpCfgEnable"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3GeneralGrpCfgPolicyId"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3GeneralGrpCfgInitTech"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3GeneralGrpCfgStatus"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ResGrpCfgMdIfIndex"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ResGrpCfgDsChList"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ResGrpCfgUsChList"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ResGrpCfgEnable"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ResGrpCfgInitTech"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ResGrpCfgPolicyId"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ResGrpCfgServiceTypeId"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3ResGrpCfgStatus"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3GrpStatusCfgIdOrZero"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3GrpStatusMdIfIndex"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3GrpStatusMdCmSgId"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3GrpStatusDsChList"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3GrpStatusUsChList"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3GrpStatusEnable"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3GrpStatusInitTech"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3GrpStatusPolicyId"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3GrpStatusChgOverSuccess"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3GrpStatusChgOverFails"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3RestrictCmCfgMacAddr"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3RestrictCmCfgMacAddrMask"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3RestrictCmCfgGrpId"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3RestrictCmCfgServiceTypeId"),
        ("DOCS-LOADBAL3-MIB", "docsLoadbal3RestrictCmCfgStatus"))
)
if mibBuilder.loadTexts:
    docsLoadbal3Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

docsLoadbal3Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 22, 2, 1, 1)
)
if mibBuilder.loadTexts:
    docsLoadbal3Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-LOADBAL3-MIB",
    **{"ChChgInitTechMap": ChChgInitTechMap,
       "docsLoadbal3Mib": docsLoadbal3Mib,
       "docsLoadbal3MibObjects": docsLoadbal3MibObjects,
       "docsLoadbal3System": docsLoadbal3System,
       "docsLoadbal3SystemEnable": docsLoadbal3SystemEnable,
       "docsLoadbal3SystemEnableError": docsLoadbal3SystemEnableError,
       "docsLoadbal3ChgOverGroup": docsLoadbal3ChgOverGroup,
       "docsLoadbal3ChgOverGroupMacAddress": docsLoadbal3ChgOverGroupMacAddress,
       "docsLoadbal3ChgOverGroupInitTech": docsLoadbal3ChgOverGroupInitTech,
       "docsLoadbal3ChgOverGroupForceUCC": docsLoadbal3ChgOverGroupForceUCC,
       "docsLoadbal3ChgOverGroupdownFrequency": docsLoadbal3ChgOverGroupdownFrequency,
       "docsLoadbal3ChgOverGroupMdIfIndex": docsLoadbal3ChgOverGroupMdIfIndex,
       "docsLoadbal3ChgOverGroupRcpId": docsLoadbal3ChgOverGroupRcpId,
       "docsLoadbal3ChgOverGroupRccId": docsLoadbal3ChgOverGroupRccId,
       "docsLoadbal3ChgOverGroupUsChSet": docsLoadbal3ChgOverGroupUsChSet,
       "docsLoadbal3ChgOverGroupServiceFlowInfo": docsLoadbal3ChgOverGroupServiceFlowInfo,
       "docsLoadbal3ChgOverGroupTransactionId": docsLoadbal3ChgOverGroupTransactionId,
       "docsLoadbal3ChgOverGroupCommit": docsLoadbal3ChgOverGroupCommit,
       "docsLoadbal3ChgOverGroupLastCommit": docsLoadbal3ChgOverGroupLastCommit,
       "docsLoadbal3ChgOverStatusTable": docsLoadbal3ChgOverStatusTable,
       "docsLoadbal3ChgOverStatusEntry": docsLoadbal3ChgOverStatusEntry,
       "docsLoadbal3ChgOverStatusId": docsLoadbal3ChgOverStatusId,
       "docsLoadbal3ChgOverStatusMacAddr": docsLoadbal3ChgOverStatusMacAddr,
       "docsLoadbal3ChgOverStatusInitTech": docsLoadbal3ChgOverStatusInitTech,
       "docsLoadbal3ChgOverStatusDownFrequency": docsLoadbal3ChgOverStatusDownFrequency,
       "docsLoadbal3ChgOverStatusMdIfIndex": docsLoadbal3ChgOverStatusMdIfIndex,
       "docsLoadbal3ChgOverStatusRcpId": docsLoadbal3ChgOverStatusRcpId,
       "docsLoadbal3ChgOverStatusRccId": docsLoadbal3ChgOverStatusRccId,
       "docsLoadbal3ChgOverStatusUsChSet": docsLoadbal3ChgOverStatusUsChSet,
       "docsLoadbal3ChgOverStatusServiceFlowInfo": docsLoadbal3ChgOverStatusServiceFlowInfo,
       "docsLoadbal3ChgOverStatusCmd": docsLoadbal3ChgOverStatusCmd,
       "docsLoadbal3ChgOverStatusTransactionId": docsLoadbal3ChgOverStatusTransactionId,
       "docsLoadbal3ChgOverStatusValue": docsLoadbal3ChgOverStatusValue,
       "docsLoadbal3ChgOverStatusUpdate": docsLoadbal3ChgOverStatusUpdate,
       "docsLoadbal3CmtsCmParamsTable": docsLoadbal3CmtsCmParamsTable,
       "docsLoadbal3CmtsCmParamsEntry": docsLoadbal3CmtsCmParamsEntry,
       "docsLoadbal3CmtsCmParamsProvGrpId": docsLoadbal3CmtsCmParamsProvGrpId,
       "docsLoadbal3CmtsCmParamsCurrentGrpId": docsLoadbal3CmtsCmParamsCurrentGrpId,
       "docsLoadbal3CmtsCmParamsProvServiceTypeID": docsLoadbal3CmtsCmParamsProvServiceTypeID,
       "docsLoadbal3CmtsCmParamsCurrentServiceTypeID": docsLoadbal3CmtsCmParamsCurrentServiceTypeID,
       "docsLoadbal3CmtsCmParamsPolicyId": docsLoadbal3CmtsCmParamsPolicyId,
       "docsLoadbal3CmtsCmParamsPriority": docsLoadbal3CmtsCmParamsPriority,
       "docsLoadbal3GeneralGrpDefaults": docsLoadbal3GeneralGrpDefaults,
       "docsLoadbal3GeneralGrpDefaultsEnable": docsLoadbal3GeneralGrpDefaultsEnable,
       "docsLoadbal3GeneralGrpDefaultsPolicyId": docsLoadbal3GeneralGrpDefaultsPolicyId,
       "docsLoadbal3GeneralGrpDefaultsInitTech": docsLoadbal3GeneralGrpDefaultsInitTech,
       "docsLoadbal3GeneralGrpCfgTable": docsLoadbal3GeneralGrpCfgTable,
       "docsLoadbal3GeneralGrpCfgEntry": docsLoadbal3GeneralGrpCfgEntry,
       "docsLoadbal3GeneralGrpCfgNodeName": docsLoadbal3GeneralGrpCfgNodeName,
       "docsLoadbal3GeneralGrpCfgEnable": docsLoadbal3GeneralGrpCfgEnable,
       "docsLoadbal3GeneralGrpCfgPolicyId": docsLoadbal3GeneralGrpCfgPolicyId,
       "docsLoadbal3GeneralGrpCfgInitTech": docsLoadbal3GeneralGrpCfgInitTech,
       "docsLoadbal3GeneralGrpCfgStatus": docsLoadbal3GeneralGrpCfgStatus,
       "docsLoadbal3ResGrpCfgTable": docsLoadbal3ResGrpCfgTable,
       "docsLoadbal3ResGrpCfgEntry": docsLoadbal3ResGrpCfgEntry,
       "docsLoadbal3ResGrpCfgId": docsLoadbal3ResGrpCfgId,
       "docsLoadbal3ResGrpCfgMdIfIndex": docsLoadbal3ResGrpCfgMdIfIndex,
       "docsLoadbal3ResGrpCfgDsChList": docsLoadbal3ResGrpCfgDsChList,
       "docsLoadbal3ResGrpCfgUsChList": docsLoadbal3ResGrpCfgUsChList,
       "docsLoadbal3ResGrpCfgEnable": docsLoadbal3ResGrpCfgEnable,
       "docsLoadbal3ResGrpCfgInitTech": docsLoadbal3ResGrpCfgInitTech,
       "docsLoadbal3ResGrpCfgPolicyId": docsLoadbal3ResGrpCfgPolicyId,
       "docsLoadbal3ResGrpCfgServiceTypeId": docsLoadbal3ResGrpCfgServiceTypeId,
       "docsLoadbal3ResGrpCfgStatus": docsLoadbal3ResGrpCfgStatus,
       "docsLoadbal3GrpStatusTable": docsLoadbal3GrpStatusTable,
       "docsLoadbal3GrpStatusEntry": docsLoadbal3GrpStatusEntry,
       "docsLoadbal3GrpStatusId": docsLoadbal3GrpStatusId,
       "docsLoadbal3GrpStatusCfgIdOrZero": docsLoadbal3GrpStatusCfgIdOrZero,
       "docsLoadbal3GrpStatusMdIfIndex": docsLoadbal3GrpStatusMdIfIndex,
       "docsLoadbal3GrpStatusMdCmSgId": docsLoadbal3GrpStatusMdCmSgId,
       "docsLoadbal3GrpStatusDsChList": docsLoadbal3GrpStatusDsChList,
       "docsLoadbal3GrpStatusUsChList": docsLoadbal3GrpStatusUsChList,
       "docsLoadbal3GrpStatusEnable": docsLoadbal3GrpStatusEnable,
       "docsLoadbal3GrpStatusInitTech": docsLoadbal3GrpStatusInitTech,
       "docsLoadbal3GrpStatusPolicyId": docsLoadbal3GrpStatusPolicyId,
       "docsLoadbal3GrpStatusChgOverSuccess": docsLoadbal3GrpStatusChgOverSuccess,
       "docsLoadbal3GrpStatusChgOverFails": docsLoadbal3GrpStatusChgOverFails,
       "docsLoadbal3RestrictCmCfgTable": docsLoadbal3RestrictCmCfgTable,
       "docsLoadbal3RestrictCmCfgEntry": docsLoadbal3RestrictCmCfgEntry,
       "docsLoadbal3RestrictCmCfgId": docsLoadbal3RestrictCmCfgId,
       "docsLoadbal3RestrictCmCfgMacAddr": docsLoadbal3RestrictCmCfgMacAddr,
       "docsLoadbal3RestrictCmCfgMacAddrMask": docsLoadbal3RestrictCmCfgMacAddrMask,
       "docsLoadbal3RestrictCmCfgGrpId": docsLoadbal3RestrictCmCfgGrpId,
       "docsLoadbal3RestrictCmCfgServiceTypeId": docsLoadbal3RestrictCmCfgServiceTypeId,
       "docsLoadbal3RestrictCmCfgStatus": docsLoadbal3RestrictCmCfgStatus,
       "docsLoadbal3PolicyTable": docsLoadbal3PolicyTable,
       "docsLoadbal3PolicyEntry": docsLoadbal3PolicyEntry,
       "docsLoadbal3PolicyId": docsLoadbal3PolicyId,
       "docsLoadbal3PolicyRuleId": docsLoadbal3PolicyRuleId,
       "docsLoadbal3PolicyPtr": docsLoadbal3PolicyPtr,
       "docsLoadbal3PolicyRowStatus": docsLoadbal3PolicyRowStatus,
       "docsLoadbal3BasicRuleTable": docsLoadbal3BasicRuleTable,
       "docsLoadbal3BasicRuleEntry": docsLoadbal3BasicRuleEntry,
       "docsLoadbal3BasicRuleId": docsLoadbal3BasicRuleId,
       "docsLoadbal3BasicRuleEnable": docsLoadbal3BasicRuleEnable,
       "docsLoadbal3BasicRuleDisStart": docsLoadbal3BasicRuleDisStart,
       "docsLoadbal3BasicRuleDisPeriod": docsLoadbal3BasicRuleDisPeriod,
       "docsLoadbal3BasicRuleRowStatus": docsLoadbal3BasicRuleRowStatus,
       "docsLoadbal3MibConformance": docsLoadbal3MibConformance,
       "docsLoadbal3MibCompliances": docsLoadbal3MibCompliances,
       "docsLoadbal3Compliance": docsLoadbal3Compliance,
       "docsLoadbal3MibGroups": docsLoadbal3MibGroups,
       "docsLoadbal3Group": docsLoadbal3Group}
)
