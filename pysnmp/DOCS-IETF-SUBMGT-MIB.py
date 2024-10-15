# SNMP MIB module (DOCS-IETF-SUBMGT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOCS-IETF-SUBMGT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:41 2024
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

(diffServActionStorage,
 diffServAlgDropStatus,
 diffServAlgDropStorage,
 diffServAlgDropType,
 diffServClfrElementStatus,
 diffServClfrElementStorage,
 diffServClfrStatus,
 diffServClfrStorage,
 diffServCountActStorage,
 diffServDataPathStatus,
 diffServDataPathStorage,
 diffServMIBActionGroup,
 diffServMIBAlgDropGroup,
 diffServMIBClfrElementGroup,
 diffServMIBClfrGroup,
 diffServMIBCounterGroup,
 diffServMIBDataPathGroup,
 diffServMIBMultiFieldClfrGroup,
 diffServMultiFieldClfrAddrType,
 diffServMultiFieldClfrDstAddr,
 diffServMultiFieldClfrSrcAddr,
 diffServMultiFieldClfrStorage) = mibBuilder.importSymbols(
    "DIFFSERV-MIB",
    "diffServActionStorage",
    "diffServAlgDropStatus",
    "diffServAlgDropStorage",
    "diffServAlgDropType",
    "diffServClfrElementStatus",
    "diffServClfrElementStorage",
    "diffServClfrStatus",
    "diffServClfrStorage",
    "diffServCountActStorage",
    "diffServDataPathStatus",
    "diffServDataPathStorage",
    "diffServMIBActionGroup",
    "diffServMIBAlgDropGroup",
    "diffServMIBClfrElementGroup",
    "diffServMIBClfrGroup",
    "diffServMIBCounterGroup",
    "diffServMIBDataPathGroup",
    "diffServMIBMultiFieldClfrGroup",
    "diffServMultiFieldClfrAddrType",
    "diffServMultiFieldClfrDstAddr",
    "diffServMultiFieldClfrSrcAddr",
    "diffServMultiFieldClfrStorage")

(docsIfCmtsCmStatusEntry,
 docsIfCmtsCmStatusIndex) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "docsIfCmtsCmStatusEntry",
    "docsIfCmtsCmStatusIndex")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "mib-2")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

docsSubMgt = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 125)
)
docsSubMgt.setRevisions(
        ("2005-03-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DocsSubMgtObjects_ObjectIdentity = ObjectIdentity
docsSubMgtObjects = _DocsSubMgtObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 125, 1)
)
_DocsSubMgtCpeControlTable_Object = MibTable
docsSubMgtCpeControlTable = _DocsSubMgtCpeControlTable_Object(
    (1, 3, 6, 1, 2, 1, 125, 1, 1)
)
if mibBuilder.loadTexts:
    docsSubMgtCpeControlTable.setStatus("current")
_DocsSubMgtCpeControlEntry_Object = MibTableRow
docsSubMgtCpeControlEntry = _DocsSubMgtCpeControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 125, 1, 1, 1)
)
if mibBuilder.loadTexts:
    docsSubMgtCpeControlEntry.setStatus("current")


class _DocsSubMgtCpeControlMaxCpeIp_Type(Integer32):
    """Custom type docsSubMgtCpeControlMaxCpeIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DocsSubMgtCpeControlMaxCpeIp_Type.__name__ = "Integer32"
_DocsSubMgtCpeControlMaxCpeIp_Object = MibTableColumn
docsSubMgtCpeControlMaxCpeIp = _DocsSubMgtCpeControlMaxCpeIp_Object(
    (1, 3, 6, 1, 2, 1, 125, 1, 1, 1, 1),
    _DocsSubMgtCpeControlMaxCpeIp_Type()
)
docsSubMgtCpeControlMaxCpeIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubMgtCpeControlMaxCpeIp.setStatus("current")
_DocsSubMgtCpeControlActive_Type = TruthValue
_DocsSubMgtCpeControlActive_Object = MibTableColumn
docsSubMgtCpeControlActive = _DocsSubMgtCpeControlActive_Object(
    (1, 3, 6, 1, 2, 1, 125, 1, 1, 1, 2),
    _DocsSubMgtCpeControlActive_Type()
)
docsSubMgtCpeControlActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubMgtCpeControlActive.setStatus("current")
_DocsSubMgtCpeControlLearnable_Type = TruthValue
_DocsSubMgtCpeControlLearnable_Object = MibTableColumn
docsSubMgtCpeControlLearnable = _DocsSubMgtCpeControlLearnable_Object(
    (1, 3, 6, 1, 2, 1, 125, 1, 1, 1, 3),
    _DocsSubMgtCpeControlLearnable_Type()
)
docsSubMgtCpeControlLearnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubMgtCpeControlLearnable.setStatus("current")
_DocsSubMgtCpeControlReset_Type = TruthValue
_DocsSubMgtCpeControlReset_Object = MibTableColumn
docsSubMgtCpeControlReset = _DocsSubMgtCpeControlReset_Object(
    (1, 3, 6, 1, 2, 1, 125, 1, 1, 1, 4),
    _DocsSubMgtCpeControlReset_Type()
)
docsSubMgtCpeControlReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubMgtCpeControlReset.setStatus("current")


class _DocsSubMgtCpeControlLastReset_Type(TimeStamp):
    """Custom type docsSubMgtCpeControlLastReset based on TimeStamp"""
    defaultValue = 0


_DocsSubMgtCpeControlLastReset_Object = MibTableColumn
docsSubMgtCpeControlLastReset = _DocsSubMgtCpeControlLastReset_Object(
    (1, 3, 6, 1, 2, 1, 125, 1, 1, 1, 5),
    _DocsSubMgtCpeControlLastReset_Type()
)
docsSubMgtCpeControlLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsSubMgtCpeControlLastReset.setStatus("current")


class _DocsSubMgtCpeMaxIpDefault_Type(Integer32):
    """Custom type docsSubMgtCpeMaxIpDefault based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DocsSubMgtCpeMaxIpDefault_Type.__name__ = "Integer32"
_DocsSubMgtCpeMaxIpDefault_Object = MibScalar
docsSubMgtCpeMaxIpDefault = _DocsSubMgtCpeMaxIpDefault_Object(
    (1, 3, 6, 1, 2, 1, 125, 1, 2),
    _DocsSubMgtCpeMaxIpDefault_Type()
)
docsSubMgtCpeMaxIpDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubMgtCpeMaxIpDefault.setStatus("current")


class _DocsSubMgtCpeActiveDefault_Type(TruthValue):
    """Custom type docsSubMgtCpeActiveDefault based on TruthValue"""


_DocsSubMgtCpeActiveDefault_Object = MibScalar
docsSubMgtCpeActiveDefault = _DocsSubMgtCpeActiveDefault_Object(
    (1, 3, 6, 1, 2, 1, 125, 1, 3),
    _DocsSubMgtCpeActiveDefault_Type()
)
docsSubMgtCpeActiveDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubMgtCpeActiveDefault.setStatus("current")


class _DocsSubMgtCpeLearnableDefault_Type(TruthValue):
    """Custom type docsSubMgtCpeLearnableDefault based on TruthValue"""


_DocsSubMgtCpeLearnableDefault_Object = MibScalar
docsSubMgtCpeLearnableDefault = _DocsSubMgtCpeLearnableDefault_Object(
    (1, 3, 6, 1, 2, 1, 125, 1, 4),
    _DocsSubMgtCpeLearnableDefault_Type()
)
docsSubMgtCpeLearnableDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubMgtCpeLearnableDefault.setStatus("current")
_DocsSubMgtCpeIpTable_Object = MibTable
docsSubMgtCpeIpTable = _DocsSubMgtCpeIpTable_Object(
    (1, 3, 6, 1, 2, 1, 125, 1, 5)
)
if mibBuilder.loadTexts:
    docsSubMgtCpeIpTable.setStatus("current")
_DocsSubMgtCpeIpEntry_Object = MibTableRow
docsSubMgtCpeIpEntry = _DocsSubMgtCpeIpEntry_Object(
    (1, 3, 6, 1, 2, 1, 125, 1, 5, 1)
)
docsSubMgtCpeIpEntry.setIndexNames(
    (0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"),
    (0, "DOCS-IETF-SUBMGT-MIB", "docsSubMgtCpeIpIndex"),
)
if mibBuilder.loadTexts:
    docsSubMgtCpeIpEntry.setStatus("current")


class _DocsSubMgtCpeIpIndex_Type(Integer32):
    """Custom type docsSubMgtCpeIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DocsSubMgtCpeIpIndex_Type.__name__ = "Integer32"
_DocsSubMgtCpeIpIndex_Object = MibTableColumn
docsSubMgtCpeIpIndex = _DocsSubMgtCpeIpIndex_Object(
    (1, 3, 6, 1, 2, 1, 125, 1, 5, 1, 1),
    _DocsSubMgtCpeIpIndex_Type()
)
docsSubMgtCpeIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsSubMgtCpeIpIndex.setStatus("current")
_DocsSubMgtCpeIpAddressType_Type = InetAddressType
_DocsSubMgtCpeIpAddressType_Object = MibTableColumn
docsSubMgtCpeIpAddressType = _DocsSubMgtCpeIpAddressType_Object(
    (1, 3, 6, 1, 2, 1, 125, 1, 5, 1, 2),
    _DocsSubMgtCpeIpAddressType_Type()
)
docsSubMgtCpeIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsSubMgtCpeIpAddressType.setStatus("current")
_DocsSubMgtCpeIpAddr_Type = InetAddress
_DocsSubMgtCpeIpAddr_Object = MibTableColumn
docsSubMgtCpeIpAddr = _DocsSubMgtCpeIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 125, 1, 5, 1, 3),
    _DocsSubMgtCpeIpAddr_Type()
)
docsSubMgtCpeIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsSubMgtCpeIpAddr.setStatus("current")
_DocsSubMgtCpeIpLearned_Type = TruthValue
_DocsSubMgtCpeIpLearned_Object = MibTableColumn
docsSubMgtCpeIpLearned = _DocsSubMgtCpeIpLearned_Object(
    (1, 3, 6, 1, 2, 1, 125, 1, 5, 1, 4),
    _DocsSubMgtCpeIpLearned_Type()
)
docsSubMgtCpeIpLearned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsSubMgtCpeIpLearned.setStatus("current")
_DocsSubMgtCmFilterTable_Object = MibTable
docsSubMgtCmFilterTable = _DocsSubMgtCmFilterTable_Object(
    (1, 3, 6, 1, 2, 1, 125, 1, 6)
)
if mibBuilder.loadTexts:
    docsSubMgtCmFilterTable.setStatus("current")
_DocsSubMgtCmFilterEntry_Object = MibTableRow
docsSubMgtCmFilterEntry = _DocsSubMgtCmFilterEntry_Object(
    (1, 3, 6, 1, 2, 1, 125, 1, 6, 1)
)
if mibBuilder.loadTexts:
    docsSubMgtCmFilterEntry.setStatus("current")


class _DocsSubMgtCmFilterSubDownstream_Type(Integer32):
    """Custom type docsSubMgtCmFilterSubDownstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsSubMgtCmFilterSubDownstream_Type.__name__ = "Integer32"
_DocsSubMgtCmFilterSubDownstream_Object = MibTableColumn
docsSubMgtCmFilterSubDownstream = _DocsSubMgtCmFilterSubDownstream_Object(
    (1, 3, 6, 1, 2, 1, 125, 1, 6, 1, 1),
    _DocsSubMgtCmFilterSubDownstream_Type()
)
docsSubMgtCmFilterSubDownstream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubMgtCmFilterSubDownstream.setStatus("current")


class _DocsSubMgtCmFilterSubUpstream_Type(Integer32):
    """Custom type docsSubMgtCmFilterSubUpstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsSubMgtCmFilterSubUpstream_Type.__name__ = "Integer32"
_DocsSubMgtCmFilterSubUpstream_Object = MibTableColumn
docsSubMgtCmFilterSubUpstream = _DocsSubMgtCmFilterSubUpstream_Object(
    (1, 3, 6, 1, 2, 1, 125, 1, 6, 1, 2),
    _DocsSubMgtCmFilterSubUpstream_Type()
)
docsSubMgtCmFilterSubUpstream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubMgtCmFilterSubUpstream.setStatus("current")


class _DocsSubMgtCmFilterCmDownstream_Type(Integer32):
    """Custom type docsSubMgtCmFilterCmDownstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsSubMgtCmFilterCmDownstream_Type.__name__ = "Integer32"
_DocsSubMgtCmFilterCmDownstream_Object = MibTableColumn
docsSubMgtCmFilterCmDownstream = _DocsSubMgtCmFilterCmDownstream_Object(
    (1, 3, 6, 1, 2, 1, 125, 1, 6, 1, 3),
    _DocsSubMgtCmFilterCmDownstream_Type()
)
docsSubMgtCmFilterCmDownstream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubMgtCmFilterCmDownstream.setStatus("current")


class _DocsSubMgtCmFilterCmUpstream_Type(Integer32):
    """Custom type docsSubMgtCmFilterCmUpstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsSubMgtCmFilterCmUpstream_Type.__name__ = "Integer32"
_DocsSubMgtCmFilterCmUpstream_Object = MibTableColumn
docsSubMgtCmFilterCmUpstream = _DocsSubMgtCmFilterCmUpstream_Object(
    (1, 3, 6, 1, 2, 1, 125, 1, 6, 1, 4),
    _DocsSubMgtCmFilterCmUpstream_Type()
)
docsSubMgtCmFilterCmUpstream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubMgtCmFilterCmUpstream.setStatus("current")
_DocsSubMgtFilterGroupTable_Object = MibTable
docsSubMgtFilterGroupTable = _DocsSubMgtFilterGroupTable_Object(
    (1, 3, 6, 1, 2, 1, 125, 1, 7)
)
if mibBuilder.loadTexts:
    docsSubMgtFilterGroupTable.setStatus("current")
_DocsSubMgtFilterGroupEntry_Object = MibTableRow
docsSubMgtFilterGroupEntry = _DocsSubMgtFilterGroupEntry_Object(
    (1, 3, 6, 1, 2, 1, 125, 1, 7, 1)
)
docsSubMgtFilterGroupEntry.setIndexNames(
    (0, "DOCS-IETF-SUBMGT-MIB", "docsSubMgtFilterGroupIndex"),
)
if mibBuilder.loadTexts:
    docsSubMgtFilterGroupEntry.setStatus("current")


class _DocsSubMgtFilterGroupIndex_Type(Integer32):
    """Custom type docsSubMgtFilterGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DocsSubMgtFilterGroupIndex_Type.__name__ = "Integer32"
_DocsSubMgtFilterGroupIndex_Object = MibTableColumn
docsSubMgtFilterGroupIndex = _DocsSubMgtFilterGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 125, 1, 7, 1, 1),
    _DocsSubMgtFilterGroupIndex_Type()
)
docsSubMgtFilterGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsSubMgtFilterGroupIndex.setStatus("current")
_DocsSubMgtConformance_ObjectIdentity = ObjectIdentity
docsSubMgtConformance = _DocsSubMgtConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 125, 2)
)
_DocsSubMgtCompliances_ObjectIdentity = ObjectIdentity
docsSubMgtCompliances = _DocsSubMgtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 125, 2, 1)
)
_DocsSubMgtGroups_ObjectIdentity = ObjectIdentity
docsSubMgtGroups = _DocsSubMgtGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 125, 2, 2)
)
docsIfCmtsCmStatusEntry.registerAugmentions(
    ("DOCS-IETF-SUBMGT-MIB",
     "docsSubMgtCpeControlEntry")
)
docsSubMgtCpeControlEntry.setIndexNames(*docsIfCmtsCmStatusEntry.getIndexNames())
docsIfCmtsCmStatusEntry.registerAugmentions(
    ("DOCS-IETF-SUBMGT-MIB",
     "docsSubMgtCmFilterEntry")
)
docsSubMgtCmFilterEntry.setIndexNames(*docsIfCmtsCmStatusEntry.getIndexNames())

# Managed Objects groups

docsSubMgtGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 125, 2, 2, 1)
)
docsSubMgtGroup.setObjects(
      *(("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCpeControlMaxCpeIp"),
        ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCpeControlActive"),
        ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCpeControlLearnable"),
        ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCpeControlReset"),
        ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCpeControlLastReset"),
        ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCpeMaxIpDefault"),
        ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCpeActiveDefault"),
        ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCpeLearnableDefault"),
        ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCpeIpAddressType"),
        ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCpeIpAddr"),
        ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCpeIpLearned"),
        ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCmFilterSubDownstream"),
        ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCmFilterSubUpstream"),
        ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCmFilterCmDownstream"),
        ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCmFilterCmUpstream"),
        ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtFilterGroupIndex"))
)
if mibBuilder.loadTexts:
    docsSubMgtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

docsSubMgtBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 125, 2, 1, 1)
)
if mibBuilder.loadTexts:
    docsSubMgtBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-IETF-SUBMGT-MIB",
    **{"docsSubMgt": docsSubMgt,
       "docsSubMgtObjects": docsSubMgtObjects,
       "docsSubMgtCpeControlTable": docsSubMgtCpeControlTable,
       "docsSubMgtCpeControlEntry": docsSubMgtCpeControlEntry,
       "docsSubMgtCpeControlMaxCpeIp": docsSubMgtCpeControlMaxCpeIp,
       "docsSubMgtCpeControlActive": docsSubMgtCpeControlActive,
       "docsSubMgtCpeControlLearnable": docsSubMgtCpeControlLearnable,
       "docsSubMgtCpeControlReset": docsSubMgtCpeControlReset,
       "docsSubMgtCpeControlLastReset": docsSubMgtCpeControlLastReset,
       "docsSubMgtCpeMaxIpDefault": docsSubMgtCpeMaxIpDefault,
       "docsSubMgtCpeActiveDefault": docsSubMgtCpeActiveDefault,
       "docsSubMgtCpeLearnableDefault": docsSubMgtCpeLearnableDefault,
       "docsSubMgtCpeIpTable": docsSubMgtCpeIpTable,
       "docsSubMgtCpeIpEntry": docsSubMgtCpeIpEntry,
       "docsSubMgtCpeIpIndex": docsSubMgtCpeIpIndex,
       "docsSubMgtCpeIpAddressType": docsSubMgtCpeIpAddressType,
       "docsSubMgtCpeIpAddr": docsSubMgtCpeIpAddr,
       "docsSubMgtCpeIpLearned": docsSubMgtCpeIpLearned,
       "docsSubMgtCmFilterTable": docsSubMgtCmFilterTable,
       "docsSubMgtCmFilterEntry": docsSubMgtCmFilterEntry,
       "docsSubMgtCmFilterSubDownstream": docsSubMgtCmFilterSubDownstream,
       "docsSubMgtCmFilterSubUpstream": docsSubMgtCmFilterSubUpstream,
       "docsSubMgtCmFilterCmDownstream": docsSubMgtCmFilterCmDownstream,
       "docsSubMgtCmFilterCmUpstream": docsSubMgtCmFilterCmUpstream,
       "docsSubMgtFilterGroupTable": docsSubMgtFilterGroupTable,
       "docsSubMgtFilterGroupEntry": docsSubMgtFilterGroupEntry,
       "docsSubMgtFilterGroupIndex": docsSubMgtFilterGroupIndex,
       "docsSubMgtConformance": docsSubMgtConformance,
       "docsSubMgtCompliances": docsSubMgtCompliances,
       "docsSubMgtBasicCompliance": docsSubMgtBasicCompliance,
       "docsSubMgtGroups": docsSubMgtGroups,
       "docsSubMgtGroup": docsSubMgtGroup}
)
