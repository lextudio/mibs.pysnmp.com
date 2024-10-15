# SNMP MIB module (DOCS-LOADBALANCING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOCS-LOADBALANCING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:52 2024
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

(docsIfCmtsCmStatusEntry,
 docsIfCmtsCmStatusIndex) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "docsIfCmtsCmStatusEntry",
    "docsIfCmtsCmStatusIndex")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 iso,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "iso",
    "zeroDotZero")

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

docsLoadBalanceMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2)
)
docsLoadBalanceMib.setRevisions(
        ("2004-03-10 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ChannelChgInitTechMap(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_DocsLoadBalNotifications_ObjectIdentity = ObjectIdentity
docsLoadBalNotifications = _DocsLoadBalNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 0)
)
_DocsLoadBalMibObjects_ObjectIdentity = ObjectIdentity
docsLoadBalMibObjects = _DocsLoadBalMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1)
)
_DocsLoadBalSystem_ObjectIdentity = ObjectIdentity
docsLoadBalSystem = _DocsLoadBalSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 1)
)
_DocsLoadBalEnable_Type = TruthValue
_DocsLoadBalEnable_Object = MibScalar
docsLoadBalEnable = _DocsLoadBalEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 1, 1),
    _DocsLoadBalEnable_Type()
)
docsLoadBalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadBalEnable.setStatus("current")
_DocsLoadBalCmtsCmStatusTable_Object = MibTable
docsLoadBalCmtsCmStatusTable = _DocsLoadBalCmtsCmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    docsLoadBalCmtsCmStatusTable.setStatus("current")
_DocsLoadBalCmtsCmStatusEntry_Object = MibTableRow
docsLoadBalCmtsCmStatusEntry = _DocsLoadBalCmtsCmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    docsLoadBalCmtsCmStatusEntry.setStatus("current")
_DocsLoadBalCmtsCmStatusGroupId_Type = Unsigned32
_DocsLoadBalCmtsCmStatusGroupId_Object = MibTableColumn
docsLoadBalCmtsCmStatusGroupId = _DocsLoadBalCmtsCmStatusGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 1, 4, 1, 1),
    _DocsLoadBalCmtsCmStatusGroupId_Type()
)
docsLoadBalCmtsCmStatusGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadBalCmtsCmStatusGroupId.setStatus("current")
_DocsLoadBalCmtsCmStatusPolicyId_Type = Unsigned32
_DocsLoadBalCmtsCmStatusPolicyId_Object = MibTableColumn
docsLoadBalCmtsCmStatusPolicyId = _DocsLoadBalCmtsCmStatusPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 1, 4, 1, 2),
    _DocsLoadBalCmtsCmStatusPolicyId_Type()
)
docsLoadBalCmtsCmStatusPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadBalCmtsCmStatusPolicyId.setStatus("current")
_DocsLoadBalCmtsCmStatusPriority_Type = Unsigned32
_DocsLoadBalCmtsCmStatusPriority_Object = MibTableColumn
docsLoadBalCmtsCmStatusPriority = _DocsLoadBalCmtsCmStatusPriority_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 1, 4, 1, 3),
    _DocsLoadBalCmtsCmStatusPriority_Type()
)
docsLoadBalCmtsCmStatusPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadBalCmtsCmStatusPriority.setStatus("current")
_DocsLoadBalChgOverObjects_ObjectIdentity = ObjectIdentity
docsLoadBalChgOverObjects = _DocsLoadBalChgOverObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 2)
)
_DocsLoadBalChgOverGroup_ObjectIdentity = ObjectIdentity
docsLoadBalChgOverGroup = _DocsLoadBalChgOverGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 2, 1)
)


class _DocsLoadBalChgOverMacAddress_Type(MacAddress):
    """Custom type docsLoadBalChgOverMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_DocsLoadBalChgOverMacAddress_Object = MibScalar
docsLoadBalChgOverMacAddress = _DocsLoadBalChgOverMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 2, 1, 1),
    _DocsLoadBalChgOverMacAddress_Type()
)
docsLoadBalChgOverMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadBalChgOverMacAddress.setStatus("current")


class _DocsLoadBalChgOverDownFrequency_Type(Integer32):
    """Custom type docsLoadBalChgOverDownFrequency based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_DocsLoadBalChgOverDownFrequency_Type.__name__ = "Integer32"
_DocsLoadBalChgOverDownFrequency_Object = MibScalar
docsLoadBalChgOverDownFrequency = _DocsLoadBalChgOverDownFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 2, 1, 2),
    _DocsLoadBalChgOverDownFrequency_Type()
)
docsLoadBalChgOverDownFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadBalChgOverDownFrequency.setStatus("current")
if mibBuilder.loadTexts:
    docsLoadBalChgOverDownFrequency.setUnits("hertz")


class _DocsLoadBalChgOverUpChannelId_Type(Integer32):
    """Custom type docsLoadBalChgOverUpChannelId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_DocsLoadBalChgOverUpChannelId_Type.__name__ = "Integer32"
_DocsLoadBalChgOverUpChannelId_Object = MibScalar
docsLoadBalChgOverUpChannelId = _DocsLoadBalChgOverUpChannelId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 2, 1, 3),
    _DocsLoadBalChgOverUpChannelId_Type()
)
docsLoadBalChgOverUpChannelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadBalChgOverUpChannelId.setStatus("current")
_DocsLoadBalChgOverInitTech_Type = ChannelChgInitTechMap
_DocsLoadBalChgOverInitTech_Object = MibScalar
docsLoadBalChgOverInitTech = _DocsLoadBalChgOverInitTech_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 2, 1, 4),
    _DocsLoadBalChgOverInitTech_Type()
)
docsLoadBalChgOverInitTech.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadBalChgOverInitTech.setStatus("current")


class _DocsLoadBalChgOverCmd_Type(Integer32):
    """Custom type docsLoadBalChgOverCmd based on Integer32"""
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
        *(("any", 1),
          ("dcc", 2),
          ("ucc", 3))
    )


_DocsLoadBalChgOverCmd_Type.__name__ = "Integer32"
_DocsLoadBalChgOverCmd_Object = MibScalar
docsLoadBalChgOverCmd = _DocsLoadBalChgOverCmd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 2, 1, 5),
    _DocsLoadBalChgOverCmd_Type()
)
docsLoadBalChgOverCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadBalChgOverCmd.setStatus("current")


class _DocsLoadBalChgOverCommit_Type(TruthValue):
    """Custom type docsLoadBalChgOverCommit based on TruthValue"""


_DocsLoadBalChgOverCommit_Object = MibScalar
docsLoadBalChgOverCommit = _DocsLoadBalChgOverCommit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 2, 1, 6),
    _DocsLoadBalChgOverCommit_Type()
)
docsLoadBalChgOverCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsLoadBalChgOverCommit.setStatus("current")
_DocsLoadBalChgOverLastCommit_Type = TimeStamp
_DocsLoadBalChgOverLastCommit_Object = MibScalar
docsLoadBalChgOverLastCommit = _DocsLoadBalChgOverLastCommit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 2, 1, 7),
    _DocsLoadBalChgOverLastCommit_Type()
)
docsLoadBalChgOverLastCommit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadBalChgOverLastCommit.setStatus("current")
_DocsLoadBalChgOverStatusTable_Object = MibTable
docsLoadBalChgOverStatusTable = _DocsLoadBalChgOverStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    docsLoadBalChgOverStatusTable.setStatus("current")
_DocsLoadBalChgOverStatusEntry_Object = MibTableRow
docsLoadBalChgOverStatusEntry = _DocsLoadBalChgOverStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 2, 2, 1)
)
docsLoadBalChgOverStatusEntry.setIndexNames(
    (0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"),
)
if mibBuilder.loadTexts:
    docsLoadBalChgOverStatusEntry.setStatus("current")
_DocsLoadBalChgOverStatusMacAddr_Type = MacAddress
_DocsLoadBalChgOverStatusMacAddr_Object = MibTableColumn
docsLoadBalChgOverStatusMacAddr = _DocsLoadBalChgOverStatusMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 2, 2, 1, 1),
    _DocsLoadBalChgOverStatusMacAddr_Type()
)
docsLoadBalChgOverStatusMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadBalChgOverStatusMacAddr.setStatus("current")


class _DocsLoadBalChgOverStatusDownFreq_Type(Integer32):
    """Custom type docsLoadBalChgOverStatusDownFreq based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_DocsLoadBalChgOverStatusDownFreq_Type.__name__ = "Integer32"
_DocsLoadBalChgOverStatusDownFreq_Object = MibTableColumn
docsLoadBalChgOverStatusDownFreq = _DocsLoadBalChgOverStatusDownFreq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 2, 2, 1, 2),
    _DocsLoadBalChgOverStatusDownFreq_Type()
)
docsLoadBalChgOverStatusDownFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadBalChgOverStatusDownFreq.setStatus("current")
if mibBuilder.loadTexts:
    docsLoadBalChgOverStatusDownFreq.setUnits("hertz")


class _DocsLoadBalChgOverStatusUpChnId_Type(Integer32):
    """Custom type docsLoadBalChgOverStatusUpChnId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_DocsLoadBalChgOverStatusUpChnId_Type.__name__ = "Integer32"
_DocsLoadBalChgOverStatusUpChnId_Object = MibTableColumn
docsLoadBalChgOverStatusUpChnId = _DocsLoadBalChgOverStatusUpChnId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 2, 2, 1, 3),
    _DocsLoadBalChgOverStatusUpChnId_Type()
)
docsLoadBalChgOverStatusUpChnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadBalChgOverStatusUpChnId.setStatus("current")
_DocsLoadBalChgOverStatusInitTech_Type = ChannelChgInitTechMap
_DocsLoadBalChgOverStatusInitTech_Object = MibTableColumn
docsLoadBalChgOverStatusInitTech = _DocsLoadBalChgOverStatusInitTech_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 2, 2, 1, 4),
    _DocsLoadBalChgOverStatusInitTech_Type()
)
docsLoadBalChgOverStatusInitTech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadBalChgOverStatusInitTech.setStatus("current")


class _DocsLoadBalChgOverStatusCmd_Type(Integer32):
    """Custom type docsLoadBalChgOverStatusCmd based on Integer32"""
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
        *(("any", 1),
          ("dcc", 2),
          ("ucc", 3))
    )


_DocsLoadBalChgOverStatusCmd_Type.__name__ = "Integer32"
_DocsLoadBalChgOverStatusCmd_Object = MibTableColumn
docsLoadBalChgOverStatusCmd = _DocsLoadBalChgOverStatusCmd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 2, 2, 1, 5),
    _DocsLoadBalChgOverStatusCmd_Type()
)
docsLoadBalChgOverStatusCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadBalChgOverStatusCmd.setStatus("current")


class _DocsLoadBalChgOverStatusValue_Type(Integer32):
    """Custom type docsLoadBalChgOverStatusValue based on Integer32"""
    defaultValue = 4

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
        *(("cmOperationRejected", 5),
          ("cmtsOperationRejected", 6),
          ("messageSent", 1),
          ("modemDeparting", 3),
          ("noOpNeeded", 2),
          ("rejectinit", 9),
          ("success", 10),
          ("timeOutT13", 7),
          ("timeOutT15", 8),
          ("waitToSendMessage", 4))
    )


_DocsLoadBalChgOverStatusValue_Type.__name__ = "Integer32"
_DocsLoadBalChgOverStatusValue_Object = MibTableColumn
docsLoadBalChgOverStatusValue = _DocsLoadBalChgOverStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 2, 2, 1, 6),
    _DocsLoadBalChgOverStatusValue_Type()
)
docsLoadBalChgOverStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadBalChgOverStatusValue.setStatus("current")
_DocsLoadBalChgOverStatusUpdate_Type = TimeStamp
_DocsLoadBalChgOverStatusUpdate_Object = MibTableColumn
docsLoadBalChgOverStatusUpdate = _DocsLoadBalChgOverStatusUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 2, 2, 1, 7),
    _DocsLoadBalChgOverStatusUpdate_Type()
)
docsLoadBalChgOverStatusUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadBalChgOverStatusUpdate.setStatus("current")
_DocsLoadBalGrpObjects_ObjectIdentity = ObjectIdentity
docsLoadBalGrpObjects = _DocsLoadBalGrpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 3)
)
_DocsLoadBalGrpTable_Object = MibTable
docsLoadBalGrpTable = _DocsLoadBalGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    docsLoadBalGrpTable.setStatus("current")
_DocsLoadBalGrpEntry_Object = MibTableRow
docsLoadBalGrpEntry = _DocsLoadBalGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 3, 1, 1)
)
docsLoadBalGrpEntry.setIndexNames(
    (0, "DOCS-LOADBALANCING-MIB", "docsLoadBalGrpId"),
)
if mibBuilder.loadTexts:
    docsLoadBalGrpEntry.setStatus("current")


class _DocsLoadBalGrpId_Type(Unsigned32):
    """Custom type docsLoadBalGrpId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsLoadBalGrpId_Type.__name__ = "Unsigned32"
_DocsLoadBalGrpId_Object = MibTableColumn
docsLoadBalGrpId = _DocsLoadBalGrpId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 3, 1, 1, 1),
    _DocsLoadBalGrpId_Type()
)
docsLoadBalGrpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsLoadBalGrpId.setStatus("current")


class _DocsLoadBalGrpIsRestricted_Type(TruthValue):
    """Custom type docsLoadBalGrpIsRestricted based on TruthValue"""


_DocsLoadBalGrpIsRestricted_Object = MibTableColumn
docsLoadBalGrpIsRestricted = _DocsLoadBalGrpIsRestricted_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 3, 1, 1, 2),
    _DocsLoadBalGrpIsRestricted_Type()
)
docsLoadBalGrpIsRestricted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadBalGrpIsRestricted.setStatus("current")
_DocsLoadBalGrpInitTech_Type = ChannelChgInitTechMap
_DocsLoadBalGrpInitTech_Object = MibTableColumn
docsLoadBalGrpInitTech = _DocsLoadBalGrpInitTech_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 3, 1, 1, 3),
    _DocsLoadBalGrpInitTech_Type()
)
docsLoadBalGrpInitTech.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadBalGrpInitTech.setStatus("current")


class _DocsLoadBalGrpDefaultPolicy_Type(Unsigned32):
    """Custom type docsLoadBalGrpDefaultPolicy based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DocsLoadBalGrpDefaultPolicy_Type.__name__ = "Unsigned32"
_DocsLoadBalGrpDefaultPolicy_Object = MibTableColumn
docsLoadBalGrpDefaultPolicy = _DocsLoadBalGrpDefaultPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 3, 1, 1, 4),
    _DocsLoadBalGrpDefaultPolicy_Type()
)
docsLoadBalGrpDefaultPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadBalGrpDefaultPolicy.setStatus("current")


class _DocsLoadBalGrpEnable_Type(TruthValue):
    """Custom type docsLoadBalGrpEnable based on TruthValue"""


_DocsLoadBalGrpEnable_Object = MibTableColumn
docsLoadBalGrpEnable = _DocsLoadBalGrpEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 3, 1, 1, 5),
    _DocsLoadBalGrpEnable_Type()
)
docsLoadBalGrpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadBalGrpEnable.setStatus("current")
_DocsLoadBalGrpChgOverSuccess_Type = Counter32
_DocsLoadBalGrpChgOverSuccess_Object = MibTableColumn
docsLoadBalGrpChgOverSuccess = _DocsLoadBalGrpChgOverSuccess_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 3, 1, 1, 6),
    _DocsLoadBalGrpChgOverSuccess_Type()
)
docsLoadBalGrpChgOverSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadBalGrpChgOverSuccess.setStatus("current")
_DocsLoadBalGrpChgOverFails_Type = Counter32
_DocsLoadBalGrpChgOverFails_Object = MibTableColumn
docsLoadBalGrpChgOverFails = _DocsLoadBalGrpChgOverFails_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 3, 1, 1, 7),
    _DocsLoadBalGrpChgOverFails_Type()
)
docsLoadBalGrpChgOverFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadBalGrpChgOverFails.setStatus("current")
_DocsLoadBalGrpStatus_Type = RowStatus
_DocsLoadBalGrpStatus_Object = MibTableColumn
docsLoadBalGrpStatus = _DocsLoadBalGrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 3, 1, 1, 8),
    _DocsLoadBalGrpStatus_Type()
)
docsLoadBalGrpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadBalGrpStatus.setStatus("current")
_DocsLoadBalChannelTable_Object = MibTable
docsLoadBalChannelTable = _DocsLoadBalChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    docsLoadBalChannelTable.setStatus("current")
_DocsLoadBalChannelEntry_Object = MibTableRow
docsLoadBalChannelEntry = _DocsLoadBalChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 3, 2, 1)
)
docsLoadBalChannelEntry.setIndexNames(
    (0, "DOCS-LOADBALANCING-MIB", "docsLoadBalGrpId"),
    (0, "DOCS-LOADBALANCING-MIB", "docsLoadBalChannelIfIndex"),
)
if mibBuilder.loadTexts:
    docsLoadBalChannelEntry.setStatus("current")
_DocsLoadBalChannelIfIndex_Type = InterfaceIndex
_DocsLoadBalChannelIfIndex_Object = MibTableColumn
docsLoadBalChannelIfIndex = _DocsLoadBalChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 3, 2, 1, 1),
    _DocsLoadBalChannelIfIndex_Type()
)
docsLoadBalChannelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsLoadBalChannelIfIndex.setStatus("current")
_DocsLoadBalChannelStatus_Type = RowStatus
_DocsLoadBalChannelStatus_Object = MibTableColumn
docsLoadBalChannelStatus = _DocsLoadBalChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 3, 2, 1, 2),
    _DocsLoadBalChannelStatus_Type()
)
docsLoadBalChannelStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadBalChannelStatus.setStatus("current")
_DocsLoadBalChnPairsTable_Object = MibTable
docsLoadBalChnPairsTable = _DocsLoadBalChnPairsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    docsLoadBalChnPairsTable.setStatus("current")
_DocsLoadBalChnPairsEntry_Object = MibTableRow
docsLoadBalChnPairsEntry = _DocsLoadBalChnPairsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 3, 3, 1)
)
docsLoadBalChnPairsEntry.setIndexNames(
    (0, "DOCS-LOADBALANCING-MIB", "docsLoadBalGrpId"),
    (0, "DOCS-LOADBALANCING-MIB", "docsLoadBalChnPairsIfIndexDepart"),
    (0, "DOCS-LOADBALANCING-MIB", "docsLoadBalChnPairsIfIndexArrive"),
)
if mibBuilder.loadTexts:
    docsLoadBalChnPairsEntry.setStatus("current")
_DocsLoadBalChnPairsIfIndexDepart_Type = InterfaceIndex
_DocsLoadBalChnPairsIfIndexDepart_Object = MibTableColumn
docsLoadBalChnPairsIfIndexDepart = _DocsLoadBalChnPairsIfIndexDepart_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 3, 3, 1, 1),
    _DocsLoadBalChnPairsIfIndexDepart_Type()
)
docsLoadBalChnPairsIfIndexDepart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsLoadBalChnPairsIfIndexDepart.setStatus("current")
_DocsLoadBalChnPairsIfIndexArrive_Type = InterfaceIndex
_DocsLoadBalChnPairsIfIndexArrive_Object = MibTableColumn
docsLoadBalChnPairsIfIndexArrive = _DocsLoadBalChnPairsIfIndexArrive_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 3, 3, 1, 2),
    _DocsLoadBalChnPairsIfIndexArrive_Type()
)
docsLoadBalChnPairsIfIndexArrive.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsLoadBalChnPairsIfIndexArrive.setStatus("current")


class _DocsLoadBalChnPairsOperStatus_Type(Integer32):
    """Custom type docsLoadBalChnPairsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notOperational", 2),
          ("operational", 1))
    )


_DocsLoadBalChnPairsOperStatus_Type.__name__ = "Integer32"
_DocsLoadBalChnPairsOperStatus_Object = MibTableColumn
docsLoadBalChnPairsOperStatus = _DocsLoadBalChnPairsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 3, 3, 1, 3),
    _DocsLoadBalChnPairsOperStatus_Type()
)
docsLoadBalChnPairsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsLoadBalChnPairsOperStatus.setStatus("current")
_DocsLoadBalChnPairsInitTech_Type = ChannelChgInitTechMap
_DocsLoadBalChnPairsInitTech_Object = MibTableColumn
docsLoadBalChnPairsInitTech = _DocsLoadBalChnPairsInitTech_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 3, 3, 1, 4),
    _DocsLoadBalChnPairsInitTech_Type()
)
docsLoadBalChnPairsInitTech.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadBalChnPairsInitTech.setStatus("current")
_DocsLoadBalChnPairsRowStatus_Type = RowStatus
_DocsLoadBalChnPairsRowStatus_Object = MibTableColumn
docsLoadBalChnPairsRowStatus = _DocsLoadBalChnPairsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 3, 3, 1, 5),
    _DocsLoadBalChnPairsRowStatus_Type()
)
docsLoadBalChnPairsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadBalChnPairsRowStatus.setStatus("current")
_DocsLoadBalRestrictCmTable_Object = MibTable
docsLoadBalRestrictCmTable = _DocsLoadBalRestrictCmTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 3, 4)
)
if mibBuilder.loadTexts:
    docsLoadBalRestrictCmTable.setStatus("current")
_DocsLoadBalRestrictCmEntry_Object = MibTableRow
docsLoadBalRestrictCmEntry = _DocsLoadBalRestrictCmEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 3, 4, 1)
)
docsLoadBalRestrictCmEntry.setIndexNames(
    (0, "DOCS-LOADBALANCING-MIB", "docsLoadBalGrpId"),
    (0, "DOCS-LOADBALANCING-MIB", "docsLoadBalRestrictCmIndex"),
)
if mibBuilder.loadTexts:
    docsLoadBalRestrictCmEntry.setStatus("current")


class _DocsLoadBalRestrictCmIndex_Type(Unsigned32):
    """Custom type docsLoadBalRestrictCmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsLoadBalRestrictCmIndex_Type.__name__ = "Unsigned32"
_DocsLoadBalRestrictCmIndex_Object = MibTableColumn
docsLoadBalRestrictCmIndex = _DocsLoadBalRestrictCmIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 3, 4, 1, 1),
    _DocsLoadBalRestrictCmIndex_Type()
)
docsLoadBalRestrictCmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsLoadBalRestrictCmIndex.setStatus("current")
_DocsLoadBalRestrictCmMACAddr_Type = MacAddress
_DocsLoadBalRestrictCmMACAddr_Object = MibTableColumn
docsLoadBalRestrictCmMACAddr = _DocsLoadBalRestrictCmMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 3, 4, 1, 2),
    _DocsLoadBalRestrictCmMACAddr_Type()
)
docsLoadBalRestrictCmMACAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadBalRestrictCmMACAddr.setStatus("current")


class _DocsLoadBalRestrictCmMacAddrMask_Type(OctetString):
    """Custom type docsLoadBalRestrictCmMacAddrMask based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(6, 6),
    )


_DocsLoadBalRestrictCmMacAddrMask_Type.__name__ = "OctetString"
_DocsLoadBalRestrictCmMacAddrMask_Object = MibTableColumn
docsLoadBalRestrictCmMacAddrMask = _DocsLoadBalRestrictCmMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 3, 4, 1, 3),
    _DocsLoadBalRestrictCmMacAddrMask_Type()
)
docsLoadBalRestrictCmMacAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadBalRestrictCmMacAddrMask.setStatus("current")
_DocsLoadBalRestrictCmStatus_Type = RowStatus
_DocsLoadBalRestrictCmStatus_Object = MibTableColumn
docsLoadBalRestrictCmStatus = _DocsLoadBalRestrictCmStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 3, 4, 1, 4),
    _DocsLoadBalRestrictCmStatus_Type()
)
docsLoadBalRestrictCmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadBalRestrictCmStatus.setStatus("current")
_DocsLoadBalPolicyObjects_ObjectIdentity = ObjectIdentity
docsLoadBalPolicyObjects = _DocsLoadBalPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 4)
)
_DocsLoadBalPolicyTable_Object = MibTable
docsLoadBalPolicyTable = _DocsLoadBalPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    docsLoadBalPolicyTable.setStatus("current")
_DocsLoadBalPolicyEntry_Object = MibTableRow
docsLoadBalPolicyEntry = _DocsLoadBalPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 4, 1, 1)
)
docsLoadBalPolicyEntry.setIndexNames(
    (0, "DOCS-LOADBALANCING-MIB", "docsLoadBalPolicyId"),
    (0, "DOCS-LOADBALANCING-MIB", "docsLoadBalPolicyRuleId"),
)
if mibBuilder.loadTexts:
    docsLoadBalPolicyEntry.setStatus("current")


class _DocsLoadBalPolicyId_Type(Unsigned32):
    """Custom type docsLoadBalPolicyId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsLoadBalPolicyId_Type.__name__ = "Unsigned32"
_DocsLoadBalPolicyId_Object = MibTableColumn
docsLoadBalPolicyId = _DocsLoadBalPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 4, 1, 1, 1),
    _DocsLoadBalPolicyId_Type()
)
docsLoadBalPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsLoadBalPolicyId.setStatus("current")


class _DocsLoadBalPolicyRuleId_Type(Unsigned32):
    """Custom type docsLoadBalPolicyRuleId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsLoadBalPolicyRuleId_Type.__name__ = "Unsigned32"
_DocsLoadBalPolicyRuleId_Object = MibTableColumn
docsLoadBalPolicyRuleId = _DocsLoadBalPolicyRuleId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 4, 1, 1, 2),
    _DocsLoadBalPolicyRuleId_Type()
)
docsLoadBalPolicyRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsLoadBalPolicyRuleId.setStatus("current")


class _DocsLoadBalPolicyRulePtr_Type(RowPointer):
    """Custom type docsLoadBalPolicyRulePtr based on RowPointer"""
    defaultValue = (0, 0)


_DocsLoadBalPolicyRulePtr_Object = MibTableColumn
docsLoadBalPolicyRulePtr = _DocsLoadBalPolicyRulePtr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 4, 1, 1, 3),
    _DocsLoadBalPolicyRulePtr_Type()
)
docsLoadBalPolicyRulePtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadBalPolicyRulePtr.setStatus("current")
_DocsLoadBalPolicyRowStatus_Type = RowStatus
_DocsLoadBalPolicyRowStatus_Object = MibTableColumn
docsLoadBalPolicyRowStatus = _DocsLoadBalPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 4, 1, 1, 5),
    _DocsLoadBalPolicyRowStatus_Type()
)
docsLoadBalPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadBalPolicyRowStatus.setStatus("current")
_DocsLoadBalBasicRuleTable_Object = MibTable
docsLoadBalBasicRuleTable = _DocsLoadBalBasicRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    docsLoadBalBasicRuleTable.setStatus("current")
_DocsLoadBalBasicRuleEntry_Object = MibTableRow
docsLoadBalBasicRuleEntry = _DocsLoadBalBasicRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 4, 2, 1)
)
docsLoadBalBasicRuleEntry.setIndexNames(
    (0, "DOCS-LOADBALANCING-MIB", "docsLoadBalBasicRuleId"),
)
if mibBuilder.loadTexts:
    docsLoadBalBasicRuleEntry.setStatus("current")


class _DocsLoadBalBasicRuleId_Type(Unsigned32):
    """Custom type docsLoadBalBasicRuleId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsLoadBalBasicRuleId_Type.__name__ = "Unsigned32"
_DocsLoadBalBasicRuleId_Object = MibTableColumn
docsLoadBalBasicRuleId = _DocsLoadBalBasicRuleId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 4, 2, 1, 1),
    _DocsLoadBalBasicRuleId_Type()
)
docsLoadBalBasicRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsLoadBalBasicRuleId.setStatus("current")


class _DocsLoadBalBasicRuleEnable_Type(Integer32):
    """Custom type docsLoadBalBasicRuleEnable based on Integer32"""
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


_DocsLoadBalBasicRuleEnable_Type.__name__ = "Integer32"
_DocsLoadBalBasicRuleEnable_Object = MibTableColumn
docsLoadBalBasicRuleEnable = _DocsLoadBalBasicRuleEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 4, 2, 1, 2),
    _DocsLoadBalBasicRuleEnable_Type()
)
docsLoadBalBasicRuleEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadBalBasicRuleEnable.setStatus("current")


class _DocsLoadBalBasicRuleDisStart_Type(Unsigned32):
    """Custom type docsLoadBalBasicRuleDisStart based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_DocsLoadBalBasicRuleDisStart_Type.__name__ = "Unsigned32"
_DocsLoadBalBasicRuleDisStart_Object = MibTableColumn
docsLoadBalBasicRuleDisStart = _DocsLoadBalBasicRuleDisStart_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 4, 2, 1, 3),
    _DocsLoadBalBasicRuleDisStart_Type()
)
docsLoadBalBasicRuleDisStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadBalBasicRuleDisStart.setStatus("current")
if mibBuilder.loadTexts:
    docsLoadBalBasicRuleDisStart.setUnits("seconds")


class _DocsLoadBalBasicRuleDisPeriod_Type(Unsigned32):
    """Custom type docsLoadBalBasicRuleDisPeriod based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_DocsLoadBalBasicRuleDisPeriod_Type.__name__ = "Unsigned32"
_DocsLoadBalBasicRuleDisPeriod_Object = MibTableColumn
docsLoadBalBasicRuleDisPeriod = _DocsLoadBalBasicRuleDisPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 4, 2, 1, 4),
    _DocsLoadBalBasicRuleDisPeriod_Type()
)
docsLoadBalBasicRuleDisPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadBalBasicRuleDisPeriod.setStatus("current")
if mibBuilder.loadTexts:
    docsLoadBalBasicRuleDisPeriod.setUnits("seconds")
_DocsLoadBalBasicRuleRowStatus_Type = RowStatus
_DocsLoadBalBasicRuleRowStatus_Object = MibTableColumn
docsLoadBalBasicRuleRowStatus = _DocsLoadBalBasicRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 1, 4, 2, 1, 5),
    _DocsLoadBalBasicRuleRowStatus_Type()
)
docsLoadBalBasicRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsLoadBalBasicRuleRowStatus.setStatus("current")
_DocsLoadBalConformance_ObjectIdentity = ObjectIdentity
docsLoadBalConformance = _DocsLoadBalConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 2)
)
_DocsLoadBalCompliances_ObjectIdentity = ObjectIdentity
docsLoadBalCompliances = _DocsLoadBalCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 2, 1)
)
_DocsLoadBalGroups_ObjectIdentity = ObjectIdentity
docsLoadBalGroups = _DocsLoadBalGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 2, 2)
)
docsIfCmtsCmStatusEntry.registerAugmentions(
    ("DOCS-LOADBALANCING-MIB",
     "docsLoadBalCmtsCmStatusEntry")
)
docsLoadBalCmtsCmStatusEntry.setIndexNames(*docsIfCmtsCmStatusEntry.getIndexNames())

# Managed Objects groups

docsLoadBalSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 2, 2, 1)
)
docsLoadBalSystemGroup.setObjects(
      *(("DOCS-LOADBALANCING-MIB", "docsLoadBalEnable"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalChgOverMacAddress"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalChgOverDownFrequency"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalChgOverUpChannelId"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalChgOverInitTech"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalChgOverCmd"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalChgOverCommit"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalChgOverLastCommit"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalChgOverStatusMacAddr"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalChgOverStatusDownFreq"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalChgOverStatusUpChnId"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalChgOverStatusInitTech"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalChgOverStatusCmd"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalChgOverStatusValue"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalChgOverStatusUpdate"))
)
if mibBuilder.loadTexts:
    docsLoadBalSystemGroup.setStatus("current")

docsLoadBalParametersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 2, 2, 2)
)
docsLoadBalParametersGroup.setObjects(
      *(("DOCS-LOADBALANCING-MIB", "docsLoadBalGrpIsRestricted"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalGrpInitTech"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalGrpDefaultPolicy"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalGrpEnable"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalGrpChgOverSuccess"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalGrpChgOverFails"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalGrpStatus"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalChannelStatus"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalChnPairsOperStatus"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalChnPairsInitTech"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalChnPairsRowStatus"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalRestrictCmMACAddr"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalRestrictCmMacAddrMask"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalRestrictCmStatus"))
)
if mibBuilder.loadTexts:
    docsLoadBalParametersGroup.setStatus("current")

docsLoadBalPoliciesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 2, 2, 3)
)
docsLoadBalPoliciesGroup.setObjects(
      *(("DOCS-LOADBALANCING-MIB", "docsLoadBalPolicyRulePtr"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalPolicyRowStatus"))
)
if mibBuilder.loadTexts:
    docsLoadBalPoliciesGroup.setStatus("current")

docsLoadBalBasicRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 2, 2, 4)
)
docsLoadBalBasicRuleGroup.setObjects(
      *(("DOCS-LOADBALANCING-MIB", "docsLoadBalBasicRuleEnable"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalBasicRuleDisStart"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalBasicRuleDisPeriod"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalBasicRuleRowStatus"))
)
if mibBuilder.loadTexts:
    docsLoadBalBasicRuleGroup.setStatus("current")

docsLoadBalCmtsCmStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 2, 2, 5)
)
docsLoadBalCmtsCmStatusGroup.setObjects(
      *(("DOCS-LOADBALANCING-MIB", "docsLoadBalCmtsCmStatusGroupId"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalCmtsCmStatusPolicyId"),
        ("DOCS-LOADBALANCING-MIB", "docsLoadBalCmtsCmStatusPriority"))
)
if mibBuilder.loadTexts:
    docsLoadBalCmtsCmStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

docsLoadBalBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    docsLoadBalBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-LOADBALANCING-MIB",
    **{"ChannelChgInitTechMap": ChannelChgInitTechMap,
       "docsLoadBalanceMib": docsLoadBalanceMib,
       "docsLoadBalNotifications": docsLoadBalNotifications,
       "docsLoadBalMibObjects": docsLoadBalMibObjects,
       "docsLoadBalSystem": docsLoadBalSystem,
       "docsLoadBalEnable": docsLoadBalEnable,
       "docsLoadBalCmtsCmStatusTable": docsLoadBalCmtsCmStatusTable,
       "docsLoadBalCmtsCmStatusEntry": docsLoadBalCmtsCmStatusEntry,
       "docsLoadBalCmtsCmStatusGroupId": docsLoadBalCmtsCmStatusGroupId,
       "docsLoadBalCmtsCmStatusPolicyId": docsLoadBalCmtsCmStatusPolicyId,
       "docsLoadBalCmtsCmStatusPriority": docsLoadBalCmtsCmStatusPriority,
       "docsLoadBalChgOverObjects": docsLoadBalChgOverObjects,
       "docsLoadBalChgOverGroup": docsLoadBalChgOverGroup,
       "docsLoadBalChgOverMacAddress": docsLoadBalChgOverMacAddress,
       "docsLoadBalChgOverDownFrequency": docsLoadBalChgOverDownFrequency,
       "docsLoadBalChgOverUpChannelId": docsLoadBalChgOverUpChannelId,
       "docsLoadBalChgOverInitTech": docsLoadBalChgOverInitTech,
       "docsLoadBalChgOverCmd": docsLoadBalChgOverCmd,
       "docsLoadBalChgOverCommit": docsLoadBalChgOverCommit,
       "docsLoadBalChgOverLastCommit": docsLoadBalChgOverLastCommit,
       "docsLoadBalChgOverStatusTable": docsLoadBalChgOverStatusTable,
       "docsLoadBalChgOverStatusEntry": docsLoadBalChgOverStatusEntry,
       "docsLoadBalChgOverStatusMacAddr": docsLoadBalChgOverStatusMacAddr,
       "docsLoadBalChgOverStatusDownFreq": docsLoadBalChgOverStatusDownFreq,
       "docsLoadBalChgOverStatusUpChnId": docsLoadBalChgOverStatusUpChnId,
       "docsLoadBalChgOverStatusInitTech": docsLoadBalChgOverStatusInitTech,
       "docsLoadBalChgOverStatusCmd": docsLoadBalChgOverStatusCmd,
       "docsLoadBalChgOverStatusValue": docsLoadBalChgOverStatusValue,
       "docsLoadBalChgOverStatusUpdate": docsLoadBalChgOverStatusUpdate,
       "docsLoadBalGrpObjects": docsLoadBalGrpObjects,
       "docsLoadBalGrpTable": docsLoadBalGrpTable,
       "docsLoadBalGrpEntry": docsLoadBalGrpEntry,
       "docsLoadBalGrpId": docsLoadBalGrpId,
       "docsLoadBalGrpIsRestricted": docsLoadBalGrpIsRestricted,
       "docsLoadBalGrpInitTech": docsLoadBalGrpInitTech,
       "docsLoadBalGrpDefaultPolicy": docsLoadBalGrpDefaultPolicy,
       "docsLoadBalGrpEnable": docsLoadBalGrpEnable,
       "docsLoadBalGrpChgOverSuccess": docsLoadBalGrpChgOverSuccess,
       "docsLoadBalGrpChgOverFails": docsLoadBalGrpChgOverFails,
       "docsLoadBalGrpStatus": docsLoadBalGrpStatus,
       "docsLoadBalChannelTable": docsLoadBalChannelTable,
       "docsLoadBalChannelEntry": docsLoadBalChannelEntry,
       "docsLoadBalChannelIfIndex": docsLoadBalChannelIfIndex,
       "docsLoadBalChannelStatus": docsLoadBalChannelStatus,
       "docsLoadBalChnPairsTable": docsLoadBalChnPairsTable,
       "docsLoadBalChnPairsEntry": docsLoadBalChnPairsEntry,
       "docsLoadBalChnPairsIfIndexDepart": docsLoadBalChnPairsIfIndexDepart,
       "docsLoadBalChnPairsIfIndexArrive": docsLoadBalChnPairsIfIndexArrive,
       "docsLoadBalChnPairsOperStatus": docsLoadBalChnPairsOperStatus,
       "docsLoadBalChnPairsInitTech": docsLoadBalChnPairsInitTech,
       "docsLoadBalChnPairsRowStatus": docsLoadBalChnPairsRowStatus,
       "docsLoadBalRestrictCmTable": docsLoadBalRestrictCmTable,
       "docsLoadBalRestrictCmEntry": docsLoadBalRestrictCmEntry,
       "docsLoadBalRestrictCmIndex": docsLoadBalRestrictCmIndex,
       "docsLoadBalRestrictCmMACAddr": docsLoadBalRestrictCmMACAddr,
       "docsLoadBalRestrictCmMacAddrMask": docsLoadBalRestrictCmMacAddrMask,
       "docsLoadBalRestrictCmStatus": docsLoadBalRestrictCmStatus,
       "docsLoadBalPolicyObjects": docsLoadBalPolicyObjects,
       "docsLoadBalPolicyTable": docsLoadBalPolicyTable,
       "docsLoadBalPolicyEntry": docsLoadBalPolicyEntry,
       "docsLoadBalPolicyId": docsLoadBalPolicyId,
       "docsLoadBalPolicyRuleId": docsLoadBalPolicyRuleId,
       "docsLoadBalPolicyRulePtr": docsLoadBalPolicyRulePtr,
       "docsLoadBalPolicyRowStatus": docsLoadBalPolicyRowStatus,
       "docsLoadBalBasicRuleTable": docsLoadBalBasicRuleTable,
       "docsLoadBalBasicRuleEntry": docsLoadBalBasicRuleEntry,
       "docsLoadBalBasicRuleId": docsLoadBalBasicRuleId,
       "docsLoadBalBasicRuleEnable": docsLoadBalBasicRuleEnable,
       "docsLoadBalBasicRuleDisStart": docsLoadBalBasicRuleDisStart,
       "docsLoadBalBasicRuleDisPeriod": docsLoadBalBasicRuleDisPeriod,
       "docsLoadBalBasicRuleRowStatus": docsLoadBalBasicRuleRowStatus,
       "docsLoadBalConformance": docsLoadBalConformance,
       "docsLoadBalCompliances": docsLoadBalCompliances,
       "docsLoadBalBasicCompliance": docsLoadBalBasicCompliance,
       "docsLoadBalGroups": docsLoadBalGroups,
       "docsLoadBalSystemGroup": docsLoadBalSystemGroup,
       "docsLoadBalParametersGroup": docsLoadBalParametersGroup,
       "docsLoadBalPoliciesGroup": docsLoadBalPoliciesGroup,
       "docsLoadBalBasicRuleGroup": docsLoadBalBasicRuleGroup,
       "docsLoadBalCmtsCmStatusGroup": docsLoadBalCmtsCmStatusGroup}
)
