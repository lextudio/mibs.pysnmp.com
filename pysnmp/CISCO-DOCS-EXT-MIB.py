# SNMP MIB module (CISCO-DOCS-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DOCS-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:42 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(TenthdBmV,
 docsIfCmtsCmStatusDownChannelIfIndex,
 docsIfCmtsCmStatusEntry,
 docsIfCmtsCmStatusIndex,
 docsIfCmtsCmStatusIpAddress,
 docsIfCmtsCmStatusMacAddress,
 docsIfCmtsCmStatusUpChannelIfIndex,
 docsIfCmtsMacEntry,
 docsIfCmtsServiceEntry,
 docsIfUpstreamChannelEntry) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "TenthdBmV",
    "docsIfCmtsCmStatusDownChannelIfIndex",
    "docsIfCmtsCmStatusEntry",
    "docsIfCmtsCmStatusIndex",
    "docsIfCmtsCmStatusIpAddress",
    "docsIfCmtsCmStatusMacAddress",
    "docsIfCmtsCmStatusUpChannelIfIndex",
    "docsIfCmtsMacEntry",
    "docsIfCmtsServiceEntry",
    "docsIfUpstreamChannelEntry")

(ChSetId,) = mibBuilder.importSymbols(
    "DOCS-IF3-MIB",
    "ChSetId")

(InterfaceIndex,
 ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifDescr",
    "ifIndex")

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
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoDocsExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116)
)
ciscoDocsExtMIB.setRevisions(
        ("2013-03-27 00:00",
         "2012-11-21 00:00",
         "2010-06-09 00:00",
         "2006-03-06 00:00",
         "2005-07-01 00:00",
         "2005-04-25 00:00",
         "2003-07-30 00:00",
         "2003-02-20 00:00",
         "2001-10-07 00:00",
         "2001-08-06 00:00",
         "2001-04-01 00:00",
         "2000-07-19 00:00",
         "2000-05-17 00:00",
         "1999-12-28 00:00",
         "1999-01-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CdxResettableCounter32(Gauge32, TextualConvention):
    status = "current"


class CdxUpstreamBondGrpList(OctetString, TextualConvention):
    status = "current"
    displayHint = "320a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 320),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoDocsExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDocsExtMIBObjects = _CiscoDocsExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1)
)
_CdxQosCtrlObjects_ObjectIdentity = ObjectIdentity
cdxQosCtrlObjects = _CdxQosCtrlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1)
)
_CdxQosCtrlUpTable_Object = MibTable
cdxQosCtrlUpTable = _CdxQosCtrlUpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cdxQosCtrlUpTable.setStatus("current")
_CdxQosCtrlUpEntry_Object = MibTableRow
cdxQosCtrlUpEntry = _CdxQosCtrlUpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 1, 1)
)
cdxQosCtrlUpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cdxQosCtrlUpEntry.setStatus("current")
_CdxQosCtrlUpAdmissionCtrl_Type = TruthValue
_CdxQosCtrlUpAdmissionCtrl_Object = MibTableColumn
cdxQosCtrlUpAdmissionCtrl = _CdxQosCtrlUpAdmissionCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 1, 1, 1),
    _CdxQosCtrlUpAdmissionCtrl_Type()
)
cdxQosCtrlUpAdmissionCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxQosCtrlUpAdmissionCtrl.setStatus("current")


class _CdxQosCtrlUpMaxRsvdBWPercent_Type(Integer32):
    """Custom type cdxQosCtrlUpMaxRsvdBWPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_CdxQosCtrlUpMaxRsvdBWPercent_Type.__name__ = "Integer32"
_CdxQosCtrlUpMaxRsvdBWPercent_Object = MibTableColumn
cdxQosCtrlUpMaxRsvdBWPercent = _CdxQosCtrlUpMaxRsvdBWPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 1, 1, 2),
    _CdxQosCtrlUpMaxRsvdBWPercent_Type()
)
cdxQosCtrlUpMaxRsvdBWPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxQosCtrlUpMaxRsvdBWPercent.setStatus("current")
if mibBuilder.loadTexts:
    cdxQosCtrlUpMaxRsvdBWPercent.setUnits("percent")
_CdxQosCtrlUpAdmissionRejects_Type = Counter32
_CdxQosCtrlUpAdmissionRejects_Object = MibTableColumn
cdxQosCtrlUpAdmissionRejects = _CdxQosCtrlUpAdmissionRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 1, 1, 3),
    _CdxQosCtrlUpAdmissionRejects_Type()
)
cdxQosCtrlUpAdmissionRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxQosCtrlUpAdmissionRejects.setStatus("current")


class _CdxQosCtrlUpReservedBW_Type(Integer32):
    """Custom type cdxQosCtrlUpReservedBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 102400000),
    )


_CdxQosCtrlUpReservedBW_Type.__name__ = "Integer32"
_CdxQosCtrlUpReservedBW_Object = MibTableColumn
cdxQosCtrlUpReservedBW = _CdxQosCtrlUpReservedBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 1, 1, 4),
    _CdxQosCtrlUpReservedBW_Type()
)
cdxQosCtrlUpReservedBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxQosCtrlUpReservedBW.setStatus("current")
if mibBuilder.loadTexts:
    cdxQosCtrlUpReservedBW.setUnits("bits/second")


class _CdxQosCtrlUpMaxVirtualBW_Type(Integer32):
    """Custom type cdxQosCtrlUpMaxVirtualBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 102400000),
    )


_CdxQosCtrlUpMaxVirtualBW_Type.__name__ = "Integer32"
_CdxQosCtrlUpMaxVirtualBW_Object = MibTableColumn
cdxQosCtrlUpMaxVirtualBW = _CdxQosCtrlUpMaxVirtualBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 1, 1, 5),
    _CdxQosCtrlUpMaxVirtualBW_Type()
)
cdxQosCtrlUpMaxVirtualBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxQosCtrlUpMaxVirtualBW.setStatus("current")
if mibBuilder.loadTexts:
    cdxQosCtrlUpMaxVirtualBW.setUnits("bits/second")
_CdxQosIfRateLimitTable_Object = MibTable
cdxQosIfRateLimitTable = _CdxQosIfRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cdxQosIfRateLimitTable.setStatus("current")
_CdxQosIfRateLimitEntry_Object = MibTableRow
cdxQosIfRateLimitEntry = _CdxQosIfRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 2, 1)
)
cdxQosIfRateLimitEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cdxQosIfRateLimitEntry.setStatus("current")


class _CdxQosIfRateLimitAlgm_Type(Integer32):
    """Custom type cdxQosIfRateLimitAlgm based on Integer32"""
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
        *(("carLike", 3),
          ("noRateLimit", 1),
          ("oneSecBurst", 2),
          ("shaping", 5),
          ("wtExPacketDiscard", 4))
    )


_CdxQosIfRateLimitAlgm_Type.__name__ = "Integer32"
_CdxQosIfRateLimitAlgm_Object = MibTableColumn
cdxQosIfRateLimitAlgm = _CdxQosIfRateLimitAlgm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 2, 1, 1),
    _CdxQosIfRateLimitAlgm_Type()
)
cdxQosIfRateLimitAlgm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxQosIfRateLimitAlgm.setStatus("current")


class _CdxQosIfRateLimitExpWt_Type(Integer32):
    """Custom type cdxQosIfRateLimitExpWt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CdxQosIfRateLimitExpWt_Type.__name__ = "Integer32"
_CdxQosIfRateLimitExpWt_Object = MibTableColumn
cdxQosIfRateLimitExpWt = _CdxQosIfRateLimitExpWt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 2, 1, 2),
    _CdxQosIfRateLimitExpWt_Type()
)
cdxQosIfRateLimitExpWt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxQosIfRateLimitExpWt.setStatus("current")


class _CdxQosIfRateLimitShpMaxDelay_Type(Integer32):
    """Custom type cdxQosIfRateLimitShpMaxDelay based on Integer32"""
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
        *(("msec1024", 5),
          ("msec128", 2),
          ("msec256", 3),
          ("msec512", 4),
          ("na", 1))
    )


_CdxQosIfRateLimitShpMaxDelay_Type.__name__ = "Integer32"
_CdxQosIfRateLimitShpMaxDelay_Object = MibTableColumn
cdxQosIfRateLimitShpMaxDelay = _CdxQosIfRateLimitShpMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 2, 1, 3),
    _CdxQosIfRateLimitShpMaxDelay_Type()
)
cdxQosIfRateLimitShpMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxQosIfRateLimitShpMaxDelay.setStatus("current")


class _CdxQosIfRateLimitShpGranularity_Type(Integer32):
    """Custom type cdxQosIfRateLimitShpGranularity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("msec1", 2),
          ("msec16", 6),
          ("msec2", 3),
          ("msec4", 4),
          ("msec8", 5),
          ("na", 1))
    )


_CdxQosIfRateLimitShpGranularity_Type.__name__ = "Integer32"
_CdxQosIfRateLimitShpGranularity_Object = MibTableColumn
cdxQosIfRateLimitShpGranularity = _CdxQosIfRateLimitShpGranularity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 2, 1, 4),
    _CdxQosIfRateLimitShpGranularity_Type()
)
cdxQosIfRateLimitShpGranularity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxQosIfRateLimitShpGranularity.setStatus("current")
_CdxCmtsServiceExtTable_Object = MibTable
cdxCmtsServiceExtTable = _CdxCmtsServiceExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cdxCmtsServiceExtTable.setStatus("current")
_CdxCmtsServiceExtEntry_Object = MibTableRow
cdxCmtsServiceExtEntry = _CdxCmtsServiceExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cdxCmtsServiceExtEntry.setStatus("current")
_CdxIfCmtsServiceOutOctets_Type = Counter32
_CdxIfCmtsServiceOutOctets_Object = MibTableColumn
cdxIfCmtsServiceOutOctets = _CdxIfCmtsServiceOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 3, 1, 1),
    _CdxIfCmtsServiceOutOctets_Type()
)
cdxIfCmtsServiceOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsServiceOutOctets.setStatus("current")
_CdxIfCmtsServiceOutPackets_Type = Counter32
_CdxIfCmtsServiceOutPackets_Object = MibTableColumn
cdxIfCmtsServiceOutPackets = _CdxIfCmtsServiceOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 3, 1, 2),
    _CdxIfCmtsServiceOutPackets_Type()
)
cdxIfCmtsServiceOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsServiceOutPackets.setStatus("current")
_CdxQosMaxUpBWExcessRequests_Type = Counter32
_CdxQosMaxUpBWExcessRequests_Object = MibTableColumn
cdxQosMaxUpBWExcessRequests = _CdxQosMaxUpBWExcessRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 3, 1, 3),
    _CdxQosMaxUpBWExcessRequests_Type()
)
cdxQosMaxUpBWExcessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxQosMaxUpBWExcessRequests.setStatus("current")
_CdxQosMaxDownBWExcessPackets_Type = Counter32
_CdxQosMaxDownBWExcessPackets_Object = MibTableColumn
cdxQosMaxDownBWExcessPackets = _CdxQosMaxDownBWExcessPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 3, 1, 4),
    _CdxQosMaxDownBWExcessPackets_Type()
)
cdxQosMaxDownBWExcessPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxQosMaxDownBWExcessPackets.setStatus("current")
_CdxIfCmtsServiceHCInOctets_Type = Counter64
_CdxIfCmtsServiceHCInOctets_Object = MibTableColumn
cdxIfCmtsServiceHCInOctets = _CdxIfCmtsServiceHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 3, 1, 5),
    _CdxIfCmtsServiceHCInOctets_Type()
)
cdxIfCmtsServiceHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsServiceHCInOctets.setStatus("current")
_CdxIfCmtsServiceHCInPackets_Type = Counter64
_CdxIfCmtsServiceHCInPackets_Object = MibTableColumn
cdxIfCmtsServiceHCInPackets = _CdxIfCmtsServiceHCInPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 3, 1, 6),
    _CdxIfCmtsServiceHCInPackets_Type()
)
cdxIfCmtsServiceHCInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsServiceHCInPackets.setStatus("current")
_CdxIfCmtsServiceHCOutOctets_Type = Counter64
_CdxIfCmtsServiceHCOutOctets_Object = MibTableColumn
cdxIfCmtsServiceHCOutOctets = _CdxIfCmtsServiceHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 3, 1, 7),
    _CdxIfCmtsServiceHCOutOctets_Type()
)
cdxIfCmtsServiceHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsServiceHCOutOctets.setStatus("current")
_CdxIfCmtsServiceHCOutPackets_Type = Counter64
_CdxIfCmtsServiceHCOutPackets_Object = MibTableColumn
cdxIfCmtsServiceHCOutPackets = _CdxIfCmtsServiceHCOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 3, 1, 8),
    _CdxIfCmtsServiceHCOutPackets_Type()
)
cdxIfCmtsServiceHCOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsServiceHCOutPackets.setStatus("current")
_CdxUpInfoElemStatsTable_Object = MibTable
cdxUpInfoElemStatsTable = _CdxUpInfoElemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cdxUpInfoElemStatsTable.setStatus("current")
_CdxUpInfoElemStatsEntry_Object = MibTableRow
cdxUpInfoElemStatsEntry = _CdxUpInfoElemStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 4, 1)
)
cdxUpInfoElemStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOCS-EXT-MIB", "cdxUpInfoElemStatsNameCode"),
)
if mibBuilder.loadTexts:
    cdxUpInfoElemStatsEntry.setStatus("current")


class _CdxUpInfoElemStatsNameCode_Type(Integer32):
    """Custom type cdxUpInfoElemStatsNameCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("initMtnIE", 3),
          ("longGrantIE", 6),
          ("reqIE", 1),
          ("reqOrDataIE", 2),
          ("shortGrantIE", 5),
          ("stnMtnIE", 4))
    )


_CdxUpInfoElemStatsNameCode_Type.__name__ = "Integer32"
_CdxUpInfoElemStatsNameCode_Object = MibTableColumn
cdxUpInfoElemStatsNameCode = _CdxUpInfoElemStatsNameCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 4, 1, 1),
    _CdxUpInfoElemStatsNameCode_Type()
)
cdxUpInfoElemStatsNameCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxUpInfoElemStatsNameCode.setStatus("current")
_CdxUpInfoElemStatsIEType_Type = Integer32
_CdxUpInfoElemStatsIEType_Object = MibTableColumn
cdxUpInfoElemStatsIEType = _CdxUpInfoElemStatsIEType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 1, 4, 1, 2),
    _CdxUpInfoElemStatsIEType_Type()
)
cdxUpInfoElemStatsIEType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxUpInfoElemStatsIEType.setStatus("current")
_CdxQosQueueObjects_ObjectIdentity = ObjectIdentity
cdxQosQueueObjects = _CdxQosQueueObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 2)
)
_CdxBWQueueTable_Object = MibTable
cdxBWQueueTable = _CdxBWQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cdxBWQueueTable.setStatus("current")
_CdxBWQueueEntry_Object = MibTableRow
cdxBWQueueEntry = _CdxBWQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 2, 1, 1)
)
cdxBWQueueEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOCS-EXT-MIB", "cdxBWQueueNameCode"),
)
if mibBuilder.loadTexts:
    cdxBWQueueEntry.setStatus("current")


class _CdxBWQueueNameCode_Type(Integer32):
    """Custom type cdxBWQueueNameCode based on Integer32"""
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
        *(("cirQ", 1),
          ("p0BEGrantQ", 3),
          ("p1BEGrantQ", 4),
          ("p2BEGrantQ", 5),
          ("p3BEGrantQ", 6),
          ("p4BEGrantQ", 7),
          ("p5BEGrantQ", 8),
          ("p6BEGrantQ", 9),
          ("p7BEGrantQ", 10),
          ("rngPollQ", 11),
          ("tbeQ", 2))
    )


_CdxBWQueueNameCode_Type.__name__ = "Integer32"
_CdxBWQueueNameCode_Object = MibTableColumn
cdxBWQueueNameCode = _CdxBWQueueNameCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 2, 1, 1, 1),
    _CdxBWQueueNameCode_Type()
)
cdxBWQueueNameCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxBWQueueNameCode.setStatus("current")


class _CdxBWQueueOrder_Type(Integer32):
    """Custom type cdxBWQueueOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CdxBWQueueOrder_Type.__name__ = "Integer32"
_CdxBWQueueOrder_Object = MibTableColumn
cdxBWQueueOrder = _CdxBWQueueOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 2, 1, 1, 2),
    _CdxBWQueueOrder_Type()
)
cdxBWQueueOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxBWQueueOrder.setStatus("current")


class _CdxBWQueueNumServedBeforeYield_Type(Integer32):
    """Custom type cdxBWQueueNumServedBeforeYield based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_CdxBWQueueNumServedBeforeYield_Type.__name__ = "Integer32"
_CdxBWQueueNumServedBeforeYield_Object = MibTableColumn
cdxBWQueueNumServedBeforeYield = _CdxBWQueueNumServedBeforeYield_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 2, 1, 1, 3),
    _CdxBWQueueNumServedBeforeYield_Type()
)
cdxBWQueueNumServedBeforeYield.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxBWQueueNumServedBeforeYield.setStatus("current")


class _CdxBWQueueType_Type(Integer32):
    """Custom type cdxBWQueueType based on Integer32"""
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
        *(("fifo", 3),
          ("other", 2),
          ("priority", 4),
          ("unknown", 1))
    )


_CdxBWQueueType_Type.__name__ = "Integer32"
_CdxBWQueueType_Object = MibTableColumn
cdxBWQueueType = _CdxBWQueueType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 2, 1, 1, 4),
    _CdxBWQueueType_Type()
)
cdxBWQueueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxBWQueueType.setStatus("current")


class _CdxBWQueueMaxDepth_Type(Integer32):
    """Custom type cdxBWQueueMaxDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_CdxBWQueueMaxDepth_Type.__name__ = "Integer32"
_CdxBWQueueMaxDepth_Object = MibTableColumn
cdxBWQueueMaxDepth = _CdxBWQueueMaxDepth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 2, 1, 1, 5),
    _CdxBWQueueMaxDepth_Type()
)
cdxBWQueueMaxDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxBWQueueMaxDepth.setStatus("current")


class _CdxBWQueueDepth_Type(Integer32):
    """Custom type cdxBWQueueDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_CdxBWQueueDepth_Type.__name__ = "Integer32"
_CdxBWQueueDepth_Object = MibTableColumn
cdxBWQueueDepth = _CdxBWQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 2, 1, 1, 6),
    _CdxBWQueueDepth_Type()
)
cdxBWQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxBWQueueDepth.setStatus("current")
_CdxBWQueueDiscards_Type = Counter32
_CdxBWQueueDiscards_Object = MibTableColumn
cdxBWQueueDiscards = _CdxBWQueueDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 2, 1, 1, 7),
    _CdxBWQueueDiscards_Type()
)
cdxBWQueueDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxBWQueueDiscards.setStatus("current")
_CdxCmtsCmCpeObjects_ObjectIdentity = ObjectIdentity
cdxCmtsCmCpeObjects = _CdxCmtsCmCpeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3)
)
_CdxCmCpeTable_Object = MibTable
cdxCmCpeTable = _CdxCmCpeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cdxCmCpeTable.setStatus("current")
_CdxCmCpeEntry_Object = MibTableRow
cdxCmCpeEntry = _CdxCmCpeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 1, 1)
)
cdxCmCpeEntry.setIndexNames(
    (0, "CISCO-DOCS-EXT-MIB", "cdxCmCpeMacAddress"),
)
if mibBuilder.loadTexts:
    cdxCmCpeEntry.setStatus("current")
_CdxCmCpeMacAddress_Type = MacAddress
_CdxCmCpeMacAddress_Object = MibTableColumn
cdxCmCpeMacAddress = _CdxCmCpeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 1, 1, 1),
    _CdxCmCpeMacAddress_Type()
)
cdxCmCpeMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxCmCpeMacAddress.setStatus("current")


class _CdxCmCpeType_Type(Integer32):
    """Custom type cdxCmCpeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cm", 1),
          ("cpe", 2))
    )


_CdxCmCpeType_Type.__name__ = "Integer32"
_CdxCmCpeType_Object = MibTableColumn
cdxCmCpeType = _CdxCmCpeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 1, 1, 2),
    _CdxCmCpeType_Type()
)
cdxCmCpeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmCpeType.setStatus("current")
_CdxCmCpeIpAddress_Type = IpAddress
_CdxCmCpeIpAddress_Object = MibTableColumn
cdxCmCpeIpAddress = _CdxCmCpeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 1, 1, 3),
    _CdxCmCpeIpAddress_Type()
)
cdxCmCpeIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmCpeIpAddress.setStatus("current")
_CdxCmCpeIfIndex_Type = InterfaceIndex
_CdxCmCpeIfIndex_Object = MibTableColumn
cdxCmCpeIfIndex = _CdxCmCpeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 1, 1, 4),
    _CdxCmCpeIfIndex_Type()
)
cdxCmCpeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmCpeIfIndex.setStatus("current")


class _CdxCmCpeCmtsServiceId_Type(Integer32):
    """Custom type cdxCmCpeCmtsServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_CdxCmCpeCmtsServiceId_Type.__name__ = "Integer32"
_CdxCmCpeCmtsServiceId_Object = MibTableColumn
cdxCmCpeCmtsServiceId = _CdxCmCpeCmtsServiceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 1, 1, 5),
    _CdxCmCpeCmtsServiceId_Type()
)
cdxCmCpeCmtsServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmCpeCmtsServiceId.setStatus("current")


class _CdxCmCpeCmStatusIndex_Type(Integer32):
    """Custom type cdxCmCpeCmStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CdxCmCpeCmStatusIndex_Type.__name__ = "Integer32"
_CdxCmCpeCmStatusIndex_Object = MibTableColumn
cdxCmCpeCmStatusIndex = _CdxCmCpeCmStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 1, 1, 6),
    _CdxCmCpeCmStatusIndex_Type()
)
cdxCmCpeCmStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmCpeCmStatusIndex.setStatus("current")
_CdxCmCpeAccessGroup_Type = DisplayString
_CdxCmCpeAccessGroup_Object = MibTableColumn
cdxCmCpeAccessGroup = _CdxCmCpeAccessGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 1, 1, 7),
    _CdxCmCpeAccessGroup_Type()
)
cdxCmCpeAccessGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmCpeAccessGroup.setStatus("current")
_CdxCmCpeResetNow_Type = TruthValue
_CdxCmCpeResetNow_Object = MibTableColumn
cdxCmCpeResetNow = _CdxCmCpeResetNow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 1, 1, 8),
    _CdxCmCpeResetNow_Type()
)
cdxCmCpeResetNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmCpeResetNow.setStatus("current")
_CdxCmCpeDeleteNow_Type = TruthValue
_CdxCmCpeDeleteNow_Object = MibTableColumn
cdxCmCpeDeleteNow = _CdxCmCpeDeleteNow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 1, 1, 9),
    _CdxCmCpeDeleteNow_Type()
)
cdxCmCpeDeleteNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmCpeDeleteNow.setStatus("current")
_CdxCmtsCmStatusExtTable_Object = MibTable
cdxCmtsCmStatusExtTable = _CdxCmtsCmStatusExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cdxCmtsCmStatusExtTable.setStatus("current")
_CdxCmtsCmStatusExtEntry_Object = MibTableRow
cdxCmtsCmStatusExtEntry = _CdxCmtsCmStatusExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cdxCmtsCmStatusExtEntry.setStatus("current")


class _CdxCmtsCmStatusValue_Type(Integer32):
    """Custom type cdxCmtsCmStatusValue based on Integer32"""
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
              27)
        )
    )
    namedValues = NamedValues(
        *(("bpiKekExpired", 23),
          ("bpiTekExpired", 24),
          ("channelChgInitRangingRcvd", 26),
          ("channelChgRangingInProgress", 27),
          ("dhcpGotIpAddr", 18),
          ("initDhcpReqRcvd", 4),
          ("initRangingRcvd", 3),
          ("initTftpPacketRcvd", 13),
          ("initTodRequestRcvd", 14),
          ("kekRejected", 10),
          ("offline", 1),
          ("online", 12),
          ("onlineKekAssigned", 6),
          ("onlineNetAccessDisabled", 5),
          ("onlineTekAssigned", 7),
          ("others", 2),
          ("rangingCompleted", 17),
          ("rangingInProgress", 16),
          ("rejClassFail", 21),
          ("rejIpSpoof", 20),
          ("rejRegNack", 22),
          ("rejStaleConfig", 19),
          ("rejectBadCos", 9),
          ("rejectBadMic", 8),
          ("reset", 15),
          ("shutdown", 25),
          ("tekRejected", 11))
    )


_CdxCmtsCmStatusValue_Type.__name__ = "Integer32"
_CdxCmtsCmStatusValue_Object = MibTableColumn
cdxCmtsCmStatusValue = _CdxCmtsCmStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2, 1, 1),
    _CdxCmtsCmStatusValue_Type()
)
cdxCmtsCmStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsCmStatusValue.setStatus("current")
_CdxIfCmtsCmStatusOnlineTimes_Type = Counter32
_CdxIfCmtsCmStatusOnlineTimes_Object = MibTableColumn
cdxIfCmtsCmStatusOnlineTimes = _CdxIfCmtsCmStatusOnlineTimes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2, 1, 2),
    _CdxIfCmtsCmStatusOnlineTimes_Type()
)
cdxIfCmtsCmStatusOnlineTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsCmStatusOnlineTimes.setStatus("current")


class _CdxIfCmtsCmStatusPercentOnline_Type(Integer32):
    """Custom type cdxIfCmtsCmStatusPercentOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_CdxIfCmtsCmStatusPercentOnline_Type.__name__ = "Integer32"
_CdxIfCmtsCmStatusPercentOnline_Object = MibTableColumn
cdxIfCmtsCmStatusPercentOnline = _CdxIfCmtsCmStatusPercentOnline_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2, 1, 3),
    _CdxIfCmtsCmStatusPercentOnline_Type()
)
cdxIfCmtsCmStatusPercentOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsCmStatusPercentOnline.setStatus("current")
_CdxIfCmtsCmStatusMinOnlineTime_Type = TimeInterval
_CdxIfCmtsCmStatusMinOnlineTime_Object = MibTableColumn
cdxIfCmtsCmStatusMinOnlineTime = _CdxIfCmtsCmStatusMinOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2, 1, 4),
    _CdxIfCmtsCmStatusMinOnlineTime_Type()
)
cdxIfCmtsCmStatusMinOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsCmStatusMinOnlineTime.setStatus("current")
_CdxIfCmtsCmStatusAvgOnlineTime_Type = TimeInterval
_CdxIfCmtsCmStatusAvgOnlineTime_Object = MibTableColumn
cdxIfCmtsCmStatusAvgOnlineTime = _CdxIfCmtsCmStatusAvgOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2, 1, 5),
    _CdxIfCmtsCmStatusAvgOnlineTime_Type()
)
cdxIfCmtsCmStatusAvgOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsCmStatusAvgOnlineTime.setStatus("current")
_CdxIfCmtsCmStatusMaxOnlineTime_Type = TimeInterval
_CdxIfCmtsCmStatusMaxOnlineTime_Object = MibTableColumn
cdxIfCmtsCmStatusMaxOnlineTime = _CdxIfCmtsCmStatusMaxOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2, 1, 6),
    _CdxIfCmtsCmStatusMaxOnlineTime_Type()
)
cdxIfCmtsCmStatusMaxOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsCmStatusMaxOnlineTime.setStatus("current")
_CdxIfCmtsCmStatusMinOfflineTime_Type = TimeInterval
_CdxIfCmtsCmStatusMinOfflineTime_Object = MibTableColumn
cdxIfCmtsCmStatusMinOfflineTime = _CdxIfCmtsCmStatusMinOfflineTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2, 1, 7),
    _CdxIfCmtsCmStatusMinOfflineTime_Type()
)
cdxIfCmtsCmStatusMinOfflineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsCmStatusMinOfflineTime.setStatus("current")
_CdxIfCmtsCmStatusAvgOfflineTime_Type = TimeInterval
_CdxIfCmtsCmStatusAvgOfflineTime_Object = MibTableColumn
cdxIfCmtsCmStatusAvgOfflineTime = _CdxIfCmtsCmStatusAvgOfflineTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2, 1, 8),
    _CdxIfCmtsCmStatusAvgOfflineTime_Type()
)
cdxIfCmtsCmStatusAvgOfflineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsCmStatusAvgOfflineTime.setStatus("current")
_CdxIfCmtsCmStatusMaxOfflineTime_Type = TimeInterval
_CdxIfCmtsCmStatusMaxOfflineTime_Object = MibTableColumn
cdxIfCmtsCmStatusMaxOfflineTime = _CdxIfCmtsCmStatusMaxOfflineTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2, 1, 9),
    _CdxIfCmtsCmStatusMaxOfflineTime_Type()
)
cdxIfCmtsCmStatusMaxOfflineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsCmStatusMaxOfflineTime.setStatus("current")


class _CdxIfCmtsCmStatusDynSidCount_Type(Integer32):
    """Custom type cdxIfCmtsCmStatusDynSidCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_CdxIfCmtsCmStatusDynSidCount_Type.__name__ = "Integer32"
_CdxIfCmtsCmStatusDynSidCount_Object = MibTableColumn
cdxIfCmtsCmStatusDynSidCount = _CdxIfCmtsCmStatusDynSidCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2, 1, 10),
    _CdxIfCmtsCmStatusDynSidCount_Type()
)
cdxIfCmtsCmStatusDynSidCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsCmStatusDynSidCount.setStatus("current")


class _CdxIfCmtsCmStatusAddlInfo_Type(Bits):
    """Custom type cdxIfCmtsCmStatusAddlInfo based on Bits"""
    namedValues = NamedValues(
        *(("modemPowerMaxOut", 1),
          ("noisyPlant", 0))
    )

_CdxIfCmtsCmStatusAddlInfo_Type.__name__ = "Bits"
_CdxIfCmtsCmStatusAddlInfo_Object = MibTableColumn
cdxIfCmtsCmStatusAddlInfo = _CdxIfCmtsCmStatusAddlInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2, 1, 11),
    _CdxIfCmtsCmStatusAddlInfo_Type()
)
cdxIfCmtsCmStatusAddlInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsCmStatusAddlInfo.setStatus("current")
_CdxIfCmtsCmStatusOnlineTimesNum_Type = CdxResettableCounter32
_CdxIfCmtsCmStatusOnlineTimesNum_Object = MibTableColumn
cdxIfCmtsCmStatusOnlineTimesNum = _CdxIfCmtsCmStatusOnlineTimesNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2, 1, 12),
    _CdxIfCmtsCmStatusOnlineTimesNum_Type()
)
cdxIfCmtsCmStatusOnlineTimesNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsCmStatusOnlineTimesNum.setStatus("current")
_CdxIfCmtsCmStatusLastResetTime_Type = TimeStamp
_CdxIfCmtsCmStatusLastResetTime_Object = MibTableColumn
cdxIfCmtsCmStatusLastResetTime = _CdxIfCmtsCmStatusLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 2, 1, 13),
    _CdxIfCmtsCmStatusLastResetTime_Type()
)
cdxIfCmtsCmStatusLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfCmtsCmStatusLastResetTime.setStatus("current")
_CdxCmtsMacExtTable_Object = MibTable
cdxCmtsMacExtTable = _CdxCmtsMacExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cdxCmtsMacExtTable.setStatus("current")
_CdxCmtsMacExtEntry_Object = MibTableRow
cdxCmtsMacExtEntry = _CdxCmtsMacExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    cdxCmtsMacExtEntry.setStatus("current")
_CdxCmtsCmOnOffTrapEnable_Type = TruthValue
_CdxCmtsCmOnOffTrapEnable_Object = MibTableColumn
cdxCmtsCmOnOffTrapEnable = _CdxCmtsCmOnOffTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 3, 1, 1),
    _CdxCmtsCmOnOffTrapEnable_Type()
)
cdxCmtsCmOnOffTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmtsCmOnOffTrapEnable.setStatus("current")


class _CdxCmtsCmOnOffTrapInterval_Type(Integer32):
    """Custom type cdxCmtsCmOnOffTrapInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_CdxCmtsCmOnOffTrapInterval_Type.__name__ = "Integer32"
_CdxCmtsCmOnOffTrapInterval_Object = MibTableColumn
cdxCmtsCmOnOffTrapInterval = _CdxCmtsCmOnOffTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 3, 1, 2),
    _CdxCmtsCmOnOffTrapInterval_Type()
)
cdxCmtsCmOnOffTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmtsCmOnOffTrapInterval.setStatus("current")
if mibBuilder.loadTexts:
    cdxCmtsCmOnOffTrapInterval.setUnits("seconds")


class _CdxCmtsCmDefaultMaxCpes_Type(Integer32):
    """Custom type cdxCmtsCmDefaultMaxCpes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_CdxCmtsCmDefaultMaxCpes_Type.__name__ = "Integer32"
_CdxCmtsCmDefaultMaxCpes_Object = MibTableColumn
cdxCmtsCmDefaultMaxCpes = _CdxCmtsCmDefaultMaxCpes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 3, 1, 3),
    _CdxCmtsCmDefaultMaxCpes_Type()
)
cdxCmtsCmDefaultMaxCpes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmtsCmDefaultMaxCpes.setStatus("current")


class _CdxCmtsCmTotal_Type(Integer32):
    """Custom type cdxCmtsCmTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CdxCmtsCmTotal_Type.__name__ = "Integer32"
_CdxCmtsCmTotal_Object = MibTableColumn
cdxCmtsCmTotal = _CdxCmtsCmTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 3, 1, 4),
    _CdxCmtsCmTotal_Type()
)
cdxCmtsCmTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsCmTotal.setStatus("current")


class _CdxCmtsCmActive_Type(Integer32):
    """Custom type cdxCmtsCmActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CdxCmtsCmActive_Type.__name__ = "Integer32"
_CdxCmtsCmActive_Object = MibTableColumn
cdxCmtsCmActive = _CdxCmtsCmActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 3, 1, 5),
    _CdxCmtsCmActive_Type()
)
cdxCmtsCmActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsCmActive.setStatus("current")


class _CdxCmtsCmRegistered_Type(Integer32):
    """Custom type cdxCmtsCmRegistered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CdxCmtsCmRegistered_Type.__name__ = "Integer32"
_CdxCmtsCmRegistered_Object = MibTableColumn
cdxCmtsCmRegistered = _CdxCmtsCmRegistered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 3, 1, 6),
    _CdxCmtsCmRegistered_Type()
)
cdxCmtsCmRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsCmRegistered.setStatus("current")


class _CdxCmtsCmDMICMode_Type(Integer32):
    """Custom type cdxCmtsCmDMICMode based on Integer32"""
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
        *(("lock", 3),
          ("mark", 2),
          ("notConfigured", 1),
          ("reject", 4))
    )


_CdxCmtsCmDMICMode_Type.__name__ = "Integer32"
_CdxCmtsCmDMICMode_Object = MibTableColumn
cdxCmtsCmDMICMode = _CdxCmtsCmDMICMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 3, 1, 7),
    _CdxCmtsCmDMICMode_Type()
)
cdxCmtsCmDMICMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmtsCmDMICMode.setStatus("current")


class _CdxCmtsCmDMICLockQos_Type(Integer32):
    """Custom type cdxCmtsCmDMICLockQos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_CdxCmtsCmDMICLockQos_Type.__name__ = "Integer32"
_CdxCmtsCmDMICLockQos_Object = MibTableColumn
cdxCmtsCmDMICLockQos = _CdxCmtsCmDMICLockQos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 3, 1, 8),
    _CdxCmtsCmDMICLockQos_Type()
)
cdxCmtsCmDMICLockQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmtsCmDMICLockQos.setStatus("current")


class _CdxCmtsCmChOverTimeExpiration_Type(Integer32):
    """Custom type cdxCmtsCmChOverTimeExpiration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_CdxCmtsCmChOverTimeExpiration_Type.__name__ = "Integer32"
_CdxCmtsCmChOverTimeExpiration_Object = MibScalar
cdxCmtsCmChOverTimeExpiration = _CdxCmtsCmChOverTimeExpiration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 4),
    _CdxCmtsCmChOverTimeExpiration_Type()
)
cdxCmtsCmChOverTimeExpiration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmtsCmChOverTimeExpiration.setStatus("current")
if mibBuilder.loadTexts:
    cdxCmtsCmChOverTimeExpiration.setUnits("minutes")
_CdxCmtsCmChOverTable_Object = MibTable
cdxCmtsCmChOverTable = _CdxCmtsCmChOverTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 5)
)
if mibBuilder.loadTexts:
    cdxCmtsCmChOverTable.setStatus("current")
_CdxCmtsCmChOverEntry_Object = MibTableRow
cdxCmtsCmChOverEntry = _CdxCmtsCmChOverEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 5, 1)
)
cdxCmtsCmChOverEntry.setIndexNames(
    (0, "CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverSerialNumber"),
)
if mibBuilder.loadTexts:
    cdxCmtsCmChOverEntry.setStatus("current")


class _CdxCmtsCmChOverSerialNumber_Type(Integer32):
    """Custom type cdxCmtsCmChOverSerialNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CdxCmtsCmChOverSerialNumber_Type.__name__ = "Integer32"
_CdxCmtsCmChOverSerialNumber_Object = MibTableColumn
cdxCmtsCmChOverSerialNumber = _CdxCmtsCmChOverSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 5, 1, 1),
    _CdxCmtsCmChOverSerialNumber_Type()
)
cdxCmtsCmChOverSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxCmtsCmChOverSerialNumber.setStatus("current")
_CdxCmtsCmChOverMacAddress_Type = MacAddress
_CdxCmtsCmChOverMacAddress_Object = MibTableColumn
cdxCmtsCmChOverMacAddress = _CdxCmtsCmChOverMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 5, 1, 2),
    _CdxCmtsCmChOverMacAddress_Type()
)
cdxCmtsCmChOverMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdxCmtsCmChOverMacAddress.setStatus("current")


class _CdxCmtsCmChOverDownFrequency_Type(Integer32):
    """Custom type cdxCmtsCmChOverDownFrequency based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CdxCmtsCmChOverDownFrequency_Type.__name__ = "Integer32"
_CdxCmtsCmChOverDownFrequency_Object = MibTableColumn
cdxCmtsCmChOverDownFrequency = _CdxCmtsCmChOverDownFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 5, 1, 3),
    _CdxCmtsCmChOverDownFrequency_Type()
)
cdxCmtsCmChOverDownFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdxCmtsCmChOverDownFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cdxCmtsCmChOverDownFrequency.setUnits("hertz")


class _CdxCmtsCmChOverUpChannelId_Type(Integer32):
    """Custom type cdxCmtsCmChOverUpChannelId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_CdxCmtsCmChOverUpChannelId_Type.__name__ = "Integer32"
_CdxCmtsCmChOverUpChannelId_Object = MibTableColumn
cdxCmtsCmChOverUpChannelId = _CdxCmtsCmChOverUpChannelId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 5, 1, 4),
    _CdxCmtsCmChOverUpChannelId_Type()
)
cdxCmtsCmChOverUpChannelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdxCmtsCmChOverUpChannelId.setStatus("current")


class _CdxCmtsCmChOverTrapOnCompletion_Type(TruthValue):
    """Custom type cdxCmtsCmChOverTrapOnCompletion based on TruthValue"""


_CdxCmtsCmChOverTrapOnCompletion_Object = MibTableColumn
cdxCmtsCmChOverTrapOnCompletion = _CdxCmtsCmChOverTrapOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 5, 1, 5),
    _CdxCmtsCmChOverTrapOnCompletion_Type()
)
cdxCmtsCmChOverTrapOnCompletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdxCmtsCmChOverTrapOnCompletion.setStatus("current")
_CdxCmtsCmChOverOpInitiatedTime_Type = TimeStamp
_CdxCmtsCmChOverOpInitiatedTime_Object = MibTableColumn
cdxCmtsCmChOverOpInitiatedTime = _CdxCmtsCmChOverOpInitiatedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 5, 1, 6),
    _CdxCmtsCmChOverOpInitiatedTime_Type()
)
cdxCmtsCmChOverOpInitiatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsCmChOverOpInitiatedTime.setStatus("current")


class _CdxCmtsCmChOverState_Type(Integer32):
    """Custom type cdxCmtsCmChOverState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("commandNotActive", 2),
          ("messageSent", 1),
          ("modemNotFound", 4),
          ("noOpNeeded", 3),
          ("timeOut", 6),
          ("waitToSendMessage", 5))
    )


_CdxCmtsCmChOverState_Type.__name__ = "Integer32"
_CdxCmtsCmChOverState_Object = MibTableColumn
cdxCmtsCmChOverState = _CdxCmtsCmChOverState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 5, 1, 7),
    _CdxCmtsCmChOverState_Type()
)
cdxCmtsCmChOverState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsCmChOverState.setStatus("current")
_CdxCmtsCmChOverRowStatus_Type = RowStatus
_CdxCmtsCmChOverRowStatus_Object = MibTableColumn
cdxCmtsCmChOverRowStatus = _CdxCmtsCmChOverRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 5, 1, 8),
    _CdxCmtsCmChOverRowStatus_Type()
)
cdxCmtsCmChOverRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdxCmtsCmChOverRowStatus.setStatus("current")
_CdxCmtsCmTable_Object = MibTable
cdxCmtsCmTable = _CdxCmtsCmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 6)
)
if mibBuilder.loadTexts:
    cdxCmtsCmTable.setStatus("current")
_CdxCmtsCmEntry_Object = MibTableRow
cdxCmtsCmEntry = _CdxCmtsCmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 6, 1)
)
cdxCmtsCmEntry.setIndexNames(
    (0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"),
)
if mibBuilder.loadTexts:
    cdxCmtsCmEntry.setStatus("current")


class _CdxCmtsCmMaxCpeNumber_Type(Integer32):
    """Custom type cdxCmtsCmMaxCpeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_CdxCmtsCmMaxCpeNumber_Type.__name__ = "Integer32"
_CdxCmtsCmMaxCpeNumber_Object = MibTableColumn
cdxCmtsCmMaxCpeNumber = _CdxCmtsCmMaxCpeNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 6, 1, 1),
    _CdxCmtsCmMaxCpeNumber_Type()
)
cdxCmtsCmMaxCpeNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmtsCmMaxCpeNumber.setStatus("current")


class _CdxCmtsCmCurrCpeNumber_Type(Integer32):
    """Custom type cdxCmtsCmCurrCpeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CdxCmtsCmCurrCpeNumber_Type.__name__ = "Integer32"
_CdxCmtsCmCurrCpeNumber_Object = MibTableColumn
cdxCmtsCmCurrCpeNumber = _CdxCmtsCmCurrCpeNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 6, 1, 2),
    _CdxCmtsCmCurrCpeNumber_Type()
)
cdxCmtsCmCurrCpeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsCmCurrCpeNumber.setStatus("current")


class _CdxCmtsCmQosProfile_Type(Integer32):
    """Custom type cdxCmtsCmQosProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_CdxCmtsCmQosProfile_Type.__name__ = "Integer32"
_CdxCmtsCmQosProfile_Object = MibTableColumn
cdxCmtsCmQosProfile = _CdxCmtsCmQosProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 6, 1, 3),
    _CdxCmtsCmQosProfile_Type()
)
cdxCmtsCmQosProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmtsCmQosProfile.setStatus("current")
_CdxCmtsCmStatusDMICTable_Object = MibTable
cdxCmtsCmStatusDMICTable = _CdxCmtsCmStatusDMICTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 7)
)
if mibBuilder.loadTexts:
    cdxCmtsCmStatusDMICTable.setStatus("current")
_CdxCmtsCmStatusDMICEntry_Object = MibTableRow
cdxCmtsCmStatusDMICEntry = _CdxCmtsCmStatusDMICEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 7, 1)
)
cdxCmtsCmStatusDMICEntry.setIndexNames(
    (0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"),
)
if mibBuilder.loadTexts:
    cdxCmtsCmStatusDMICEntry.setStatus("current")


class _CdxCmtsCmStatusDMICMode_Type(Integer32):
    """Custom type cdxCmtsCmStatusDMICMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lock", 2),
          ("mark", 1),
          ("reject", 3))
    )


_CdxCmtsCmStatusDMICMode_Type.__name__ = "Integer32"
_CdxCmtsCmStatusDMICMode_Object = MibTableColumn
cdxCmtsCmStatusDMICMode = _CdxCmtsCmStatusDMICMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 7, 1, 1),
    _CdxCmtsCmStatusDMICMode_Type()
)
cdxCmtsCmStatusDMICMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsCmStatusDMICMode.setStatus("current")


class _CdxCmtsCmStatusDMICUnLock_Type(TruthValue):
    """Custom type cdxCmtsCmStatusDMICUnLock based on TruthValue"""


_CdxCmtsCmStatusDMICUnLock_Object = MibTableColumn
cdxCmtsCmStatusDMICUnLock = _CdxCmtsCmStatusDMICUnLock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 7, 1, 2),
    _CdxCmtsCmStatusDMICUnLock_Type()
)
cdxCmtsCmStatusDMICUnLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmtsCmStatusDMICUnLock.setStatus("current")
_CdxCmToCpeTable_Object = MibTable
cdxCmToCpeTable = _CdxCmToCpeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 8)
)
if mibBuilder.loadTexts:
    cdxCmToCpeTable.setStatus("current")
_CdxCmToCpeEntry_Object = MibTableRow
cdxCmToCpeEntry = _CdxCmToCpeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 8, 1)
)
cdxCmToCpeEntry.setIndexNames(
    (0, "CISCO-DOCS-EXT-MIB", "cdxCmToCpeCmMacAddress"),
    (0, "CISCO-DOCS-EXT-MIB", "cdxCmToCpeInetAddressType"),
    (0, "CISCO-DOCS-EXT-MIB", "cdxCmToCpeInetAddress"),
)
if mibBuilder.loadTexts:
    cdxCmToCpeEntry.setStatus("current")
_CdxCmToCpeCmMacAddress_Type = MacAddress
_CdxCmToCpeCmMacAddress_Object = MibTableColumn
cdxCmToCpeCmMacAddress = _CdxCmToCpeCmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 8, 1, 1),
    _CdxCmToCpeCmMacAddress_Type()
)
cdxCmToCpeCmMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxCmToCpeCmMacAddress.setStatus("current")
_CdxCmToCpeInetAddressType_Type = InetAddressType
_CdxCmToCpeInetAddressType_Object = MibTableColumn
cdxCmToCpeInetAddressType = _CdxCmToCpeInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 8, 1, 2),
    _CdxCmToCpeInetAddressType_Type()
)
cdxCmToCpeInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmToCpeInetAddressType.setStatus("current")
_CdxCmToCpeInetAddress_Type = InetAddress
_CdxCmToCpeInetAddress_Object = MibTableColumn
cdxCmToCpeInetAddress = _CdxCmToCpeInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 8, 1, 3),
    _CdxCmToCpeInetAddress_Type()
)
cdxCmToCpeInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmToCpeInetAddress.setStatus("current")
_CdxCpeToCmTable_Object = MibTable
cdxCpeToCmTable = _CdxCpeToCmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 9)
)
if mibBuilder.loadTexts:
    cdxCpeToCmTable.setStatus("current")
_CdxCpeToCmEntry_Object = MibTableRow
cdxCpeToCmEntry = _CdxCpeToCmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 9, 1)
)
cdxCpeToCmEntry.setIndexNames(
    (0, "CISCO-DOCS-EXT-MIB", "cdxCpeToCmCpeMacAddress"),
)
if mibBuilder.loadTexts:
    cdxCpeToCmEntry.setStatus("current")
_CdxCpeToCmCpeMacAddress_Type = MacAddress
_CdxCpeToCmCpeMacAddress_Object = MibTableColumn
cdxCpeToCmCpeMacAddress = _CdxCpeToCmCpeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 9, 1, 1),
    _CdxCpeToCmCpeMacAddress_Type()
)
cdxCpeToCmCpeMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxCpeToCmCpeMacAddress.setStatus("current")
_CdxCpeToCmMacAddress_Type = MacAddress
_CdxCpeToCmMacAddress_Object = MibTableColumn
cdxCpeToCmMacAddress = _CdxCpeToCmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 9, 1, 2),
    _CdxCpeToCmMacAddress_Type()
)
cdxCpeToCmMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCpeToCmMacAddress.setStatus("current")
_CdxCpeToCmInetAddressType_Type = InetAddressType
_CdxCpeToCmInetAddressType_Object = MibTableColumn
cdxCpeToCmInetAddressType = _CdxCpeToCmInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 9, 1, 3),
    _CdxCpeToCmInetAddressType_Type()
)
cdxCpeToCmInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCpeToCmInetAddressType.setStatus("current")
_CdxCpeToCmInetAddress_Type = InetAddress
_CdxCpeToCmInetAddress_Object = MibTableColumn
cdxCpeToCmInetAddress = _CdxCpeToCmInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 9, 1, 4),
    _CdxCpeToCmInetAddress_Type()
)
cdxCpeToCmInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCpeToCmInetAddress.setStatus("current")


class _CdxCpeToCmStatusIndex_Type(Integer32):
    """Custom type cdxCpeToCmStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CdxCpeToCmStatusIndex_Type.__name__ = "Integer32"
_CdxCpeToCmStatusIndex_Object = MibTableColumn
cdxCpeToCmStatusIndex = _CdxCpeToCmStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 9, 1, 5),
    _CdxCpeToCmStatusIndex_Type()
)
cdxCpeToCmStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCpeToCmStatusIndex.setStatus("current")
_CdxCpeIpPrefixTable_Object = MibTable
cdxCpeIpPrefixTable = _CdxCpeIpPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 10)
)
if mibBuilder.loadTexts:
    cdxCpeIpPrefixTable.setStatus("current")
_CdxCpeIpPrefixEntry_Object = MibTableRow
cdxCpeIpPrefixEntry = _CdxCpeIpPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 10, 1)
)
cdxCpeIpPrefixEntry.setIndexNames(
    (0, "CISCO-DOCS-EXT-MIB", "cdxCpeIpPrefixCmMacAddress"),
    (0, "CISCO-DOCS-EXT-MIB", "cdxCpeIpPrefixType"),
    (0, "CISCO-DOCS-EXT-MIB", "cdxCpeIpPrefixAddress"),
    (0, "CISCO-DOCS-EXT-MIB", "cdxCpeIpPrefixLen"),
)
if mibBuilder.loadTexts:
    cdxCpeIpPrefixEntry.setStatus("current")
_CdxCpeIpPrefixCmMacAddress_Type = MacAddress
_CdxCpeIpPrefixCmMacAddress_Object = MibTableColumn
cdxCpeIpPrefixCmMacAddress = _CdxCpeIpPrefixCmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 10, 1, 1),
    _CdxCpeIpPrefixCmMacAddress_Type()
)
cdxCpeIpPrefixCmMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxCpeIpPrefixCmMacAddress.setStatus("current")
_CdxCpeIpPrefixType_Type = InetAddressType
_CdxCpeIpPrefixType_Object = MibTableColumn
cdxCpeIpPrefixType = _CdxCpeIpPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 10, 1, 2),
    _CdxCpeIpPrefixType_Type()
)
cdxCpeIpPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxCpeIpPrefixType.setStatus("current")


class _CdxCpeIpPrefixAddress_Type(InetAddress):
    """Custom type cdxCpeIpPrefixAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 96),
    )


_CdxCpeIpPrefixAddress_Type.__name__ = "InetAddress"
_CdxCpeIpPrefixAddress_Object = MibTableColumn
cdxCpeIpPrefixAddress = _CdxCpeIpPrefixAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 10, 1, 3),
    _CdxCpeIpPrefixAddress_Type()
)
cdxCpeIpPrefixAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxCpeIpPrefixAddress.setStatus("current")
_CdxCpeIpPrefixLen_Type = InetAddressPrefixLength
_CdxCpeIpPrefixLen_Object = MibTableColumn
cdxCpeIpPrefixLen = _CdxCpeIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 10, 1, 4),
    _CdxCpeIpPrefixLen_Type()
)
cdxCpeIpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxCpeIpPrefixLen.setStatus("current")
_CdxCpeIpPrefixCpeMacAddress_Type = MacAddress
_CdxCpeIpPrefixCpeMacAddress_Object = MibTableColumn
cdxCpeIpPrefixCpeMacAddress = _CdxCpeIpPrefixCpeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 10, 1, 5),
    _CdxCpeIpPrefixCpeMacAddress_Type()
)
cdxCpeIpPrefixCpeMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCpeIpPrefixCpeMacAddress.setStatus("current")
_CdxCpeIpPrefixCpeType_Type = SnmpAdminString
_CdxCpeIpPrefixCpeType_Object = MibTableColumn
cdxCpeIpPrefixCpeType = _CdxCpeIpPrefixCpeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 3, 10, 1, 6),
    _CdxCpeIpPrefixCpeType_Type()
)
cdxCpeIpPrefixCpeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCpeIpPrefixCpeType.setStatus("current")
_CdxSpecMgmtObjects_ObjectIdentity = ObjectIdentity
cdxSpecMgmtObjects = _CdxSpecMgmtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4)
)
_CdxIfUpstreamChannelExtTable_Object = MibTable
cdxIfUpstreamChannelExtTable = _CdxIfUpstreamChannelExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cdxIfUpstreamChannelExtTable.setStatus("current")
_CdxIfUpstreamChannelExtEntry_Object = MibTableRow
cdxIfUpstreamChannelExtEntry = _CdxIfUpstreamChannelExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    cdxIfUpstreamChannelExtEntry.setStatus("current")


class _CdxIfUpChannelWidth_Type(Integer32):
    """Custom type cdxIfUpChannelWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000000),
    )


_CdxIfUpChannelWidth_Type.__name__ = "Integer32"
_CdxIfUpChannelWidth_Object = MibTableColumn
cdxIfUpChannelWidth = _CdxIfUpChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 1),
    _CdxIfUpChannelWidth_Type()
)
cdxIfUpChannelWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxIfUpChannelWidth.setStatus("current")
if mibBuilder.loadTexts:
    cdxIfUpChannelWidth.setUnits("hertz")
_CdxIfUpChannelModulationProfile_Type = Unsigned32
_CdxIfUpChannelModulationProfile_Object = MibTableColumn
cdxIfUpChannelModulationProfile = _CdxIfUpChannelModulationProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 2),
    _CdxIfUpChannelModulationProfile_Type()
)
cdxIfUpChannelModulationProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxIfUpChannelModulationProfile.setStatus("current")


class _CdxIfUpChannelCmTotal_Type(Integer32):
    """Custom type cdxIfUpChannelCmTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_CdxIfUpChannelCmTotal_Type.__name__ = "Integer32"
_CdxIfUpChannelCmTotal_Object = MibTableColumn
cdxIfUpChannelCmTotal = _CdxIfUpChannelCmTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 3),
    _CdxIfUpChannelCmTotal_Type()
)
cdxIfUpChannelCmTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfUpChannelCmTotal.setStatus("current")


class _CdxIfUpChannelCmActive_Type(Integer32):
    """Custom type cdxIfUpChannelCmActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_CdxIfUpChannelCmActive_Type.__name__ = "Integer32"
_CdxIfUpChannelCmActive_Object = MibTableColumn
cdxIfUpChannelCmActive = _CdxIfUpChannelCmActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 4),
    _CdxIfUpChannelCmActive_Type()
)
cdxIfUpChannelCmActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfUpChannelCmActive.setStatus("current")


class _CdxIfUpChannelCmRegistered_Type(Integer32):
    """Custom type cdxIfUpChannelCmRegistered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_CdxIfUpChannelCmRegistered_Type.__name__ = "Integer32"
_CdxIfUpChannelCmRegistered_Object = MibTableColumn
cdxIfUpChannelCmRegistered = _CdxIfUpChannelCmRegistered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 5),
    _CdxIfUpChannelCmRegistered_Type()
)
cdxIfUpChannelCmRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfUpChannelCmRegistered.setStatus("current")


class _CdxIfUpChannelInputPowerLevel_Type(TenthdBmV):
    """Custom type cdxIfUpChannelInputPowerLevel based on TenthdBmV"""
    subtypeSpec = TenthdBmV.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 250),
    )


_CdxIfUpChannelInputPowerLevel_Type.__name__ = "TenthdBmV"
_CdxIfUpChannelInputPowerLevel_Object = MibTableColumn
cdxIfUpChannelInputPowerLevel = _CdxIfUpChannelInputPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 6),
    _CdxIfUpChannelInputPowerLevel_Type()
)
cdxIfUpChannelInputPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxIfUpChannelInputPowerLevel.setStatus("current")


class _CdxIfUpChannelAvgUtil_Type(Integer32):
    """Custom type cdxIfUpChannelAvgUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CdxIfUpChannelAvgUtil_Type.__name__ = "Integer32"
_CdxIfUpChannelAvgUtil_Object = MibTableColumn
cdxIfUpChannelAvgUtil = _CdxIfUpChannelAvgUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 7),
    _CdxIfUpChannelAvgUtil_Type()
)
cdxIfUpChannelAvgUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfUpChannelAvgUtil.setStatus("current")
if mibBuilder.loadTexts:
    cdxIfUpChannelAvgUtil.setUnits("percent")


class _CdxIfUpChannelAvgContSlots_Type(Integer32):
    """Custom type cdxIfUpChannelAvgContSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CdxIfUpChannelAvgContSlots_Type.__name__ = "Integer32"
_CdxIfUpChannelAvgContSlots_Object = MibTableColumn
cdxIfUpChannelAvgContSlots = _CdxIfUpChannelAvgContSlots_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 8),
    _CdxIfUpChannelAvgContSlots_Type()
)
cdxIfUpChannelAvgContSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfUpChannelAvgContSlots.setStatus("current")
if mibBuilder.loadTexts:
    cdxIfUpChannelAvgContSlots.setUnits("percent")


class _CdxIfUpChannelRangeSlots_Type(Integer32):
    """Custom type cdxIfUpChannelRangeSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CdxIfUpChannelRangeSlots_Type.__name__ = "Integer32"
_CdxIfUpChannelRangeSlots_Object = MibTableColumn
cdxIfUpChannelRangeSlots = _CdxIfUpChannelRangeSlots_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 9),
    _CdxIfUpChannelRangeSlots_Type()
)
cdxIfUpChannelRangeSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfUpChannelRangeSlots.setStatus("current")
if mibBuilder.loadTexts:
    cdxIfUpChannelRangeSlots.setUnits("percent")
_CdxIfUpChannelNumActiveUGS_Type = Unsigned32
_CdxIfUpChannelNumActiveUGS_Object = MibTableColumn
cdxIfUpChannelNumActiveUGS = _CdxIfUpChannelNumActiveUGS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 10),
    _CdxIfUpChannelNumActiveUGS_Type()
)
cdxIfUpChannelNumActiveUGS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfUpChannelNumActiveUGS.setStatus("current")
_CdxIfUpChannelMaxUGSLastOneHour_Type = Unsigned32
_CdxIfUpChannelMaxUGSLastOneHour_Object = MibTableColumn
cdxIfUpChannelMaxUGSLastOneHour = _CdxIfUpChannelMaxUGSLastOneHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 11),
    _CdxIfUpChannelMaxUGSLastOneHour_Type()
)
cdxIfUpChannelMaxUGSLastOneHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfUpChannelMaxUGSLastOneHour.setStatus("current")
_CdxIfUpChannelMinUGSLastOneHour_Type = Unsigned32
_CdxIfUpChannelMinUGSLastOneHour_Object = MibTableColumn
cdxIfUpChannelMinUGSLastOneHour = _CdxIfUpChannelMinUGSLastOneHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 12),
    _CdxIfUpChannelMinUGSLastOneHour_Type()
)
cdxIfUpChannelMinUGSLastOneHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfUpChannelMinUGSLastOneHour.setStatus("current")
_CdxIfUpChannelAvgUGSLastOneHour_Type = Unsigned32
_CdxIfUpChannelAvgUGSLastOneHour_Object = MibTableColumn
cdxIfUpChannelAvgUGSLastOneHour = _CdxIfUpChannelAvgUGSLastOneHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 13),
    _CdxIfUpChannelAvgUGSLastOneHour_Type()
)
cdxIfUpChannelAvgUGSLastOneHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfUpChannelAvgUGSLastOneHour.setStatus("current")
_CdxIfUpChannelMaxUGSLastFiveMins_Type = Unsigned32
_CdxIfUpChannelMaxUGSLastFiveMins_Object = MibTableColumn
cdxIfUpChannelMaxUGSLastFiveMins = _CdxIfUpChannelMaxUGSLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 14),
    _CdxIfUpChannelMaxUGSLastFiveMins_Type()
)
cdxIfUpChannelMaxUGSLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfUpChannelMaxUGSLastFiveMins.setStatus("current")
_CdxIfUpChannelMinUGSLastFiveMins_Type = Unsigned32
_CdxIfUpChannelMinUGSLastFiveMins_Object = MibTableColumn
cdxIfUpChannelMinUGSLastFiveMins = _CdxIfUpChannelMinUGSLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 15),
    _CdxIfUpChannelMinUGSLastFiveMins_Type()
)
cdxIfUpChannelMinUGSLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfUpChannelMinUGSLastFiveMins.setStatus("current")
_CdxIfUpChannelAvgUGSLastFiveMins_Type = Unsigned32
_CdxIfUpChannelAvgUGSLastFiveMins_Object = MibTableColumn
cdxIfUpChannelAvgUGSLastFiveMins = _CdxIfUpChannelAvgUGSLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 4, 1, 1, 16),
    _CdxIfUpChannelAvgUGSLastFiveMins_Type()
)
cdxIfUpChannelAvgUGSLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxIfUpChannelAvgUGSLastFiveMins.setStatus("current")
_CdxWBResilObjects_ObjectIdentity = ObjectIdentity
cdxWBResilObjects = _CdxWBResilObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5)
)


class _CdxWBResilRFChangeDampenTime_Type(Integer32):
    """Custom type cdxWBResilRFChangeDampenTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CdxWBResilRFChangeDampenTime_Type.__name__ = "Integer32"
_CdxWBResilRFChangeDampenTime_Object = MibScalar
cdxWBResilRFChangeDampenTime = _CdxWBResilRFChangeDampenTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 1),
    _CdxWBResilRFChangeDampenTime_Type()
)
cdxWBResilRFChangeDampenTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxWBResilRFChangeDampenTime.setStatus("current")
if mibBuilder.loadTexts:
    cdxWBResilRFChangeDampenTime.setUnits("Second")


class _CdxWBResilRFChangeTriggerPercentage_Type(Integer32):
    """Custom type cdxWBResilRFChangeTriggerPercentage based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CdxWBResilRFChangeTriggerPercentage_Type.__name__ = "Integer32"
_CdxWBResilRFChangeTriggerPercentage_Object = MibScalar
cdxWBResilRFChangeTriggerPercentage = _CdxWBResilRFChangeTriggerPercentage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 2),
    _CdxWBResilRFChangeTriggerPercentage_Type()
)
cdxWBResilRFChangeTriggerPercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxWBResilRFChangeTriggerPercentage.setStatus("current")
if mibBuilder.loadTexts:
    cdxWBResilRFChangeTriggerPercentage.setUnits("Percentage")


class _CdxWBResilRFChangeTriggerCount_Type(Integer32):
    """Custom type cdxWBResilRFChangeTriggerCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CdxWBResilRFChangeTriggerCount_Type.__name__ = "Integer32"
_CdxWBResilRFChangeTriggerCount_Object = MibScalar
cdxWBResilRFChangeTriggerCount = _CdxWBResilRFChangeTriggerCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 3),
    _CdxWBResilRFChangeTriggerCount_Type()
)
cdxWBResilRFChangeTriggerCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxWBResilRFChangeTriggerCount.setStatus("current")


class _CdxWBResilRFChangeTriggerMoveSecondary_Type(TruthValue):
    """Custom type cdxWBResilRFChangeTriggerMoveSecondary based on TruthValue"""


_CdxWBResilRFChangeTriggerMoveSecondary_Object = MibScalar
cdxWBResilRFChangeTriggerMoveSecondary = _CdxWBResilRFChangeTriggerMoveSecondary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 4),
    _CdxWBResilRFChangeTriggerMoveSecondary_Type()
)
cdxWBResilRFChangeTriggerMoveSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxWBResilRFChangeTriggerMoveSecondary.setStatus("current")


class _CdxWBResilNotificationEnable_Type(Bits):
    """Custom type cdxWBResilNotificationEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("cm-pmode", 2),
          ("cm-recover", 1),
          ("event", 0),
          ("rf-down", 4),
          ("rf-up", 3))
    )

_CdxWBResilNotificationEnable_Type.__name__ = "Bits"
_CdxWBResilNotificationEnable_Object = MibScalar
cdxWBResilNotificationEnable = _CdxWBResilNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 5),
    _CdxWBResilNotificationEnable_Type()
)
cdxWBResilNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxWBResilNotificationEnable.setStatus("current")


class _CdxWBResilNotificationsInterval_Type(Integer32):
    """Custom type cdxWBResilNotificationsInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_CdxWBResilNotificationsInterval_Type.__name__ = "Integer32"
_CdxWBResilNotificationsInterval_Object = MibScalar
cdxWBResilNotificationsInterval = _CdxWBResilNotificationsInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 6),
    _CdxWBResilNotificationsInterval_Type()
)
cdxWBResilNotificationsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxWBResilNotificationsInterval.setStatus("current")
if mibBuilder.loadTexts:
    cdxWBResilNotificationsInterval.setUnits("Second")


class _CdxWBResilEventLevel_Type(Integer32):
    """Custom type cdxWBResilEventLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 3),
          ("info", 1),
          ("warning", 2))
    )


_CdxWBResilEventLevel_Type.__name__ = "Integer32"
_CdxWBResilEventLevel_Object = MibScalar
cdxWBResilEventLevel = _CdxWBResilEventLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 7),
    _CdxWBResilEventLevel_Type()
)
cdxWBResilEventLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cdxWBResilEventLevel.setStatus("current")


class _CdxWBResilEventType_Type(Integer32):
    """Custom type cdxWBResilEventType based on Integer32"""
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
        *(("cmEventMddRecovery", 3),
          ("cmEventMddTimeout", 1),
          ("cmEventQamFecFailure", 2),
          ("cmEventQamFecRecovery", 4))
    )


_CdxWBResilEventType_Type.__name__ = "Integer32"
_CdxWBResilEventType_Object = MibScalar
cdxWBResilEventType = _CdxWBResilEventType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 8),
    _CdxWBResilEventType_Type()
)
cdxWBResilEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cdxWBResilEventType.setStatus("current")
_CdxWBResilUpdateTime_Type = DateAndTime
_CdxWBResilUpdateTime_Object = MibScalar
cdxWBResilUpdateTime = _CdxWBResilUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 9),
    _CdxWBResilUpdateTime_Type()
)
cdxWBResilUpdateTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cdxWBResilUpdateTime.setStatus("current")
_CdxWBResilEventTotalCount_Type = Counter32
_CdxWBResilEventTotalCount_Object = MibScalar
cdxWBResilEventTotalCount = _CdxWBResilEventTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 10),
    _CdxWBResilEventTotalCount_Type()
)
cdxWBResilEventTotalCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cdxWBResilEventTotalCount.setStatus("current")
_CdxWBResilEventTotalDupCount_Type = Counter32
_CdxWBResilEventTotalDupCount_Object = MibScalar
cdxWBResilEventTotalDupCount = _CdxWBResilEventTotalDupCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 5, 11),
    _CdxWBResilEventTotalDupCount_Type()
)
cdxWBResilEventTotalDupCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cdxWBResilEventTotalDupCount.setStatus("current")
_CdxDownstreamObjects_ObjectIdentity = ObjectIdentity
cdxDownstreamObjects = _CdxDownstreamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 6)
)
_CdxRFtoPrimaryChannelMappingTable_Object = MibTable
cdxRFtoPrimaryChannelMappingTable = _CdxRFtoPrimaryChannelMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cdxRFtoPrimaryChannelMappingTable.setStatus("current")
_CdxRFtoPrimaryChannelMappingEntry_Object = MibTableRow
cdxRFtoPrimaryChannelMappingEntry = _CdxRFtoPrimaryChannelMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 6, 1, 1)
)
cdxRFtoPrimaryChannelMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cdxRFtoPrimaryChannelMappingEntry.setStatus("current")
_CdxPrimaryChannelIfIndex_Type = InterfaceIndex
_CdxPrimaryChannelIfIndex_Object = MibTableColumn
cdxPrimaryChannelIfIndex = _CdxPrimaryChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 6, 1, 1, 1),
    _CdxPrimaryChannelIfIndex_Type()
)
cdxPrimaryChannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxPrimaryChannelIfIndex.setStatus("current")
_CdxPrimaryChanneltoRFMappingTable_Object = MibTable
cdxPrimaryChanneltoRFMappingTable = _CdxPrimaryChanneltoRFMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 6, 2)
)
if mibBuilder.loadTexts:
    cdxPrimaryChanneltoRFMappingTable.setStatus("current")
_CdxPrimaryChanneltoRFMappingEntry_Object = MibTableRow
cdxPrimaryChanneltoRFMappingEntry = _CdxPrimaryChanneltoRFMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 6, 2, 1)
)
cdxPrimaryChanneltoRFMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cdxPrimaryChanneltoRFMappingEntry.setStatus("current")
_CdxPhysicalRFIfIndex_Type = InterfaceIndex
_CdxPhysicalRFIfIndex_Object = MibTableColumn
cdxPhysicalRFIfIndex = _CdxPhysicalRFIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 6, 2, 1, 1),
    _CdxPhysicalRFIfIndex_Type()
)
cdxPhysicalRFIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxPhysicalRFIfIndex.setStatus("current")
_CdxCmtsMtcCmSfObjects_ObjectIdentity = ObjectIdentity
cdxCmtsMtcCmSfObjects = _CdxCmtsMtcCmSfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7)
)
_CdxCmtsMtcCmTable_Object = MibTable
cdxCmtsMtcCmTable = _CdxCmtsMtcCmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cdxCmtsMtcCmTable.setStatus("current")
_CdxCmtsMtcCmEntry_Object = MibTableRow
cdxCmtsMtcCmEntry = _CdxCmtsMtcCmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 1, 1)
)
cdxCmtsMtcCmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOCS-EXT-MIB", "cdxCmtsMtcTcsId"),
)
if mibBuilder.loadTexts:
    cdxCmtsMtcCmEntry.setStatus("current")
_CdxCmtsMtcTcsId_Type = ChSetId
_CdxCmtsMtcTcsId_Object = MibTableColumn
cdxCmtsMtcTcsId = _CdxCmtsMtcTcsId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 1, 1, 1),
    _CdxCmtsMtcTcsId_Type()
)
cdxCmtsMtcTcsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxCmtsMtcTcsId.setStatus("current")
_CdxCmtsMtcCmTotal_Type = Unsigned32
_CdxCmtsMtcCmTotal_Object = MibTableColumn
cdxCmtsMtcCmTotal = _CdxCmtsMtcCmTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 1, 1, 2),
    _CdxCmtsMtcCmTotal_Type()
)
cdxCmtsMtcCmTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsMtcCmTotal.setStatus("current")
_CdxCMtsMtcCmOperational_Type = Unsigned32
_CdxCMtsMtcCmOperational_Object = MibTableColumn
cdxCMtsMtcCmOperational = _CdxCMtsMtcCmOperational_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 1, 1, 3),
    _CdxCMtsMtcCmOperational_Type()
)
cdxCMtsMtcCmOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCMtsMtcCmOperational.setStatus("current")
_CdxCmtsMtcCmRegistered_Type = Unsigned32
_CdxCmtsMtcCmRegistered_Object = MibTableColumn
cdxCmtsMtcCmRegistered = _CdxCmtsMtcCmRegistered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 1, 1, 4),
    _CdxCmtsMtcCmRegistered_Type()
)
cdxCmtsMtcCmRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsMtcCmRegistered.setStatus("current")
_CdxCmtsMtcCmUnregistered_Type = Unsigned32
_CdxCmtsMtcCmUnregistered_Object = MibTableColumn
cdxCmtsMtcCmUnregistered = _CdxCmtsMtcCmUnregistered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 1, 1, 5),
    _CdxCmtsMtcCmUnregistered_Type()
)
cdxCmtsMtcCmUnregistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsMtcCmUnregistered.setStatus("current")
_CdxCmtsMtcCmOffline_Type = Unsigned32
_CdxCmtsMtcCmOffline_Object = MibTableColumn
cdxCmtsMtcCmOffline = _CdxCmtsMtcCmOffline_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 1, 1, 6),
    _CdxCmtsMtcCmOffline_Type()
)
cdxCmtsMtcCmOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsMtcCmOffline.setStatus("current")
_CdxCmtsMtcCmWideband_Type = Unsigned32
_CdxCmtsMtcCmWideband_Object = MibTableColumn
cdxCmtsMtcCmWideband = _CdxCmtsMtcCmWideband_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 1, 1, 7),
    _CdxCmtsMtcCmWideband_Type()
)
cdxCmtsMtcCmWideband.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsMtcCmWideband.setStatus("current")
_CdxCmtsMtcUpstreamBondGrp_Type = CdxUpstreamBondGrpList
_CdxCmtsMtcUpstreamBondGrp_Object = MibTableColumn
cdxCmtsMtcUpstreamBondGrp = _CdxCmtsMtcUpstreamBondGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 1, 1, 8),
    _CdxCmtsMtcUpstreamBondGrp_Type()
)
cdxCmtsMtcUpstreamBondGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsMtcUpstreamBondGrp.setStatus("current")
_CdxCmtsUscbSflowTable_Object = MibTable
cdxCmtsUscbSflowTable = _CdxCmtsUscbSflowTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2)
)
if mibBuilder.loadTexts:
    cdxCmtsUscbSflowTable.setStatus("current")
_CdxCmtsUscbSflowEntry_Object = MibTableRow
cdxCmtsUscbSflowEntry = _CdxCmtsUscbSflowEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1)
)
cdxCmtsUscbSflowEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOCS-EXT-MIB", "cdxCmtsUsBondingGrpId"),
)
if mibBuilder.loadTexts:
    cdxCmtsUscbSflowEntry.setStatus("current")


class _CdxCmtsUsBondingGrpId_Type(Unsigned32):
    """Custom type cdxCmtsUsBondingGrpId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdxCmtsUsBondingGrpId_Type.__name__ = "Unsigned32"
_CdxCmtsUsBondingGrpId_Object = MibTableColumn
cdxCmtsUsBondingGrpId = _CdxCmtsUsBondingGrpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1, 1),
    _CdxCmtsUsBondingGrpId_Type()
)
cdxCmtsUsBondingGrpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdxCmtsUsBondingGrpId.setStatus("current")
_CdxCmtsUscbSfTotal_Type = Unsigned32
_CdxCmtsUscbSfTotal_Object = MibTableColumn
cdxCmtsUscbSfTotal = _CdxCmtsUscbSfTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1, 2),
    _CdxCmtsUscbSfTotal_Type()
)
cdxCmtsUscbSfTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsUscbSfTotal.setStatus("current")
_CdxCmtsUscbSfPri_Type = Unsigned32
_CdxCmtsUscbSfPri_Object = MibTableColumn
cdxCmtsUscbSfPri = _CdxCmtsUscbSfPri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1, 3),
    _CdxCmtsUscbSfPri_Type()
)
cdxCmtsUscbSfPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsUscbSfPri.setStatus("current")
_CdxCmtsUscbStaticSfBe_Type = Unsigned32
_CdxCmtsUscbStaticSfBe_Object = MibTableColumn
cdxCmtsUscbStaticSfBe = _CdxCmtsUscbStaticSfBe_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1, 4),
    _CdxCmtsUscbStaticSfBe_Type()
)
cdxCmtsUscbStaticSfBe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsUscbStaticSfBe.setStatus("current")
_CdxCmtsUscbStaticSfUgs_Type = Unsigned32
_CdxCmtsUscbStaticSfUgs_Object = MibTableColumn
cdxCmtsUscbStaticSfUgs = _CdxCmtsUscbStaticSfUgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1, 5),
    _CdxCmtsUscbStaticSfUgs_Type()
)
cdxCmtsUscbStaticSfUgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsUscbStaticSfUgs.setStatus("current")
_CdxCmtsUscbStaticSfUgsad_Type = Unsigned32
_CdxCmtsUscbStaticSfUgsad_Object = MibTableColumn
cdxCmtsUscbStaticSfUgsad = _CdxCmtsUscbStaticSfUgsad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1, 6),
    _CdxCmtsUscbStaticSfUgsad_Type()
)
cdxCmtsUscbStaticSfUgsad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsUscbStaticSfUgsad.setStatus("current")
_CdxCmtsUscbStaticSfRtps_Type = Unsigned32
_CdxCmtsUscbStaticSfRtps_Object = MibTableColumn
cdxCmtsUscbStaticSfRtps = _CdxCmtsUscbStaticSfRtps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1, 7),
    _CdxCmtsUscbStaticSfRtps_Type()
)
cdxCmtsUscbStaticSfRtps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsUscbStaticSfRtps.setStatus("current")
_CdxCmtsUscbStaticSfNrtps_Type = Unsigned32
_CdxCmtsUscbStaticSfNrtps_Object = MibTableColumn
cdxCmtsUscbStaticSfNrtps = _CdxCmtsUscbStaticSfNrtps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1, 8),
    _CdxCmtsUscbStaticSfNrtps_Type()
)
cdxCmtsUscbStaticSfNrtps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsUscbStaticSfNrtps.setStatus("current")
_CdxCmtsUscbDynSfBe_Type = Unsigned32
_CdxCmtsUscbDynSfBe_Object = MibTableColumn
cdxCmtsUscbDynSfBe = _CdxCmtsUscbDynSfBe_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1, 9),
    _CdxCmtsUscbDynSfBe_Type()
)
cdxCmtsUscbDynSfBe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsUscbDynSfBe.setStatus("current")
_CdxCmtsUscbDynSfUgs_Type = Unsigned32
_CdxCmtsUscbDynSfUgs_Object = MibTableColumn
cdxCmtsUscbDynSfUgs = _CdxCmtsUscbDynSfUgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1, 10),
    _CdxCmtsUscbDynSfUgs_Type()
)
cdxCmtsUscbDynSfUgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsUscbDynSfUgs.setStatus("current")
_CdxCmtsUscbDynSfUgsad_Type = Unsigned32
_CdxCmtsUscbDynSfUgsad_Object = MibTableColumn
cdxCmtsUscbDynSfUgsad = _CdxCmtsUscbDynSfUgsad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1, 11),
    _CdxCmtsUscbDynSfUgsad_Type()
)
cdxCmtsUscbDynSfUgsad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsUscbDynSfUgsad.setStatus("current")
_CdxCmtsUscbDynSfRtps_Type = Unsigned32
_CdxCmtsUscbDynSfRtps_Object = MibTableColumn
cdxCmtsUscbDynSfRtps = _CdxCmtsUscbDynSfRtps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1, 12),
    _CdxCmtsUscbDynSfRtps_Type()
)
cdxCmtsUscbDynSfRtps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsUscbDynSfRtps.setStatus("current")
_CdxCmtsUscbDynSfNrtps_Type = Unsigned32
_CdxCmtsUscbDynSfNrtps_Object = MibTableColumn
cdxCmtsUscbDynSfNrtps = _CdxCmtsUscbDynSfNrtps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1, 13),
    _CdxCmtsUscbDynSfNrtps_Type()
)
cdxCmtsUscbDynSfNrtps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdxCmtsUscbDynSfNrtps.setStatus("current")
_CdxCmtsUscbDescr_Type = SnmpAdminString
_CdxCmtsUscbDescr_Object = MibTableColumn
cdxCmtsUscbDescr = _CdxCmtsUscbDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 1, 7, 2, 1, 14),
    _CdxCmtsUscbDescr_Type()
)
cdxCmtsUscbDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdxCmtsUscbDescr.setStatus("current")
_CiscoDocsExtNotificationsPrefix_ObjectIdentity = ObjectIdentity
ciscoDocsExtNotificationsPrefix = _CiscoDocsExtNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 2)
)
_CiscoDocsExtNotifications_ObjectIdentity = ObjectIdentity
ciscoDocsExtNotifications = _CiscoDocsExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 2, 0)
)
_CiscoDocsExtConformance_ObjectIdentity = ObjectIdentity
ciscoDocsExtConformance = _CiscoDocsExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3)
)
_CdxDocsExtCompliances_ObjectIdentity = ObjectIdentity
cdxDocsExtCompliances = _CdxDocsExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1)
)
_CdxDocsExtGroups_ObjectIdentity = ObjectIdentity
cdxDocsExtGroups = _CdxDocsExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2)
)
docsIfCmtsServiceEntry.registerAugmentions(
    ("CISCO-DOCS-EXT-MIB",
     "cdxCmtsServiceExtEntry")
)
cdxCmtsServiceExtEntry.setIndexNames(*docsIfCmtsServiceEntry.getIndexNames())
docsIfCmtsCmStatusEntry.registerAugmentions(
    ("CISCO-DOCS-EXT-MIB",
     "cdxCmtsCmStatusExtEntry")
)
cdxCmtsCmStatusExtEntry.setIndexNames(*docsIfCmtsCmStatusEntry.getIndexNames())
docsIfCmtsMacEntry.registerAugmentions(
    ("CISCO-DOCS-EXT-MIB",
     "cdxCmtsMacExtEntry")
)
cdxCmtsMacExtEntry.setIndexNames(*docsIfCmtsMacEntry.getIndexNames())
docsIfUpstreamChannelEntry.registerAugmentions(
    ("CISCO-DOCS-EXT-MIB",
     "cdxIfUpstreamChannelExtEntry")
)
cdxIfUpstreamChannelExtEntry.setIndexNames(*docsIfUpstreamChannelEntry.getIndexNames())

# Managed Objects groups

cdxQosCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 1)
)
cdxQosCtrlGroup.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpAdmissionCtrl"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpMaxRsvdBWPercent"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpAdmissionRejects"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpReservedBW"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpMaxVirtualBW"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosIfRateLimitAlgm"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosIfRateLimitExpWt"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsServiceOutOctets"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsServiceOutPackets"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosMaxUpBWExcessRequests"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosMaxDownBWExcessPackets"))
)
if mibBuilder.loadTexts:
    cdxQosCtrlGroup.setStatus("obsolete")

cdxQosQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 2)
)
cdxQosQueueGroup.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxBWQueueOrder"),
        ("CISCO-DOCS-EXT-MIB", "cdxBWQueueNumServedBeforeYield"),
        ("CISCO-DOCS-EXT-MIB", "cdxBWQueueType"),
        ("CISCO-DOCS-EXT-MIB", "cdxBWQueueMaxDepth"),
        ("CISCO-DOCS-EXT-MIB", "cdxBWQueueDepth"),
        ("CISCO-DOCS-EXT-MIB", "cdxBWQueueDiscards"))
)
if mibBuilder.loadTexts:
    cdxQosQueueGroup.setStatus("current")

cdxCmtsCmCpeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 3)
)
cdxCmtsCmCpeGroup.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmCpeType"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIpAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIfIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmtsServiceId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmStatusIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeAccessGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmStatusValue"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusOnlineTimes"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusPercentOnline"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapEnable"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapInterval"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmDefaultMaxCpes"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTimeExpiration"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverMacAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverDownFrequency"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverUpChannelId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTrapOnCompletion"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverOpInitiatedTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverState"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverRowStatus"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmMaxCpeNumber"))
)
if mibBuilder.loadTexts:
    cdxCmtsCmCpeGroup.setStatus("obsolete")

cdxQosCtrlGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 4)
)
cdxQosCtrlGroupRev1.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpAdmissionCtrl"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpMaxRsvdBWPercent"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpAdmissionRejects"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpReservedBW"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpMaxVirtualBW"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosIfRateLimitAlgm"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosIfRateLimitExpWt"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosIfRateLimitShpGranularity"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosIfRateLimitShpMaxDelay"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsServiceOutOctets"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsServiceOutPackets"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosMaxUpBWExcessRequests"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosMaxDownBWExcessPackets"))
)
if mibBuilder.loadTexts:
    cdxQosCtrlGroupRev1.setStatus("obsolete")

cdxCmtsCmCpeGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 5)
)
cdxCmtsCmCpeGroupRev1.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmCpeType"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIpAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIfIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmtsServiceId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmStatusIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeAccessGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmStatusValue"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusOnlineTimes"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusPercentOnline"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusDynSidCount"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapEnable"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapInterval"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmDefaultMaxCpes"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTimeExpiration"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverMacAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverDownFrequency"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverUpChannelId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTrapOnCompletion"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverOpInitiatedTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverState"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverRowStatus"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmMaxCpeNumber"))
)
if mibBuilder.loadTexts:
    cdxCmtsCmCpeGroupRev1.setStatus("obsolete")

cdxSpecMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 6)
)
cdxSpecMgmtGroup.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelWidth"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelModulationProfile"))
)
if mibBuilder.loadTexts:
    cdxSpecMgmtGroup.setStatus("obsolete")

cdxCmtsCmCpeGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 7)
)
cdxCmtsCmCpeGroupRev2.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmCpeType"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIpAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIfIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmtsServiceId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmStatusIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeAccessGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeResetNow"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmStatusValue"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusOnlineTimes"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusPercentOnline"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusDynSidCount"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapEnable"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapInterval"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmDefaultMaxCpes"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTimeExpiration"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverMacAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverDownFrequency"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverUpChannelId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTrapOnCompletion"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverOpInitiatedTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverState"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverRowStatus"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmMaxCpeNumber"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCurrCpeNumber"))
)
if mibBuilder.loadTexts:
    cdxCmtsCmCpeGroupRev2.setStatus("obsolete")

cdxSpecMgmtGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 8)
)
cdxSpecMgmtGroupRev1.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelWidth"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelModulationProfile"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelCmTotal"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelCmActive"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelCmRegistered"))
)
if mibBuilder.loadTexts:
    cdxSpecMgmtGroupRev1.setStatus("obsolete")

cdxCmtsCmCpeGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 9)
)
cdxCmtsCmCpeGroupRev3.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmCpeType"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIpAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIfIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmtsServiceId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmStatusIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeAccessGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeResetNow"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmStatusValue"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusOnlineTimes"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusPercentOnline"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusDynSidCount"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapEnable"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapInterval"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmDefaultMaxCpes"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmTotal"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmActive"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmRegistered"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTimeExpiration"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverMacAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverDownFrequency"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverUpChannelId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTrapOnCompletion"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverOpInitiatedTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverState"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverRowStatus"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmMaxCpeNumber"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCurrCpeNumber"))
)
if mibBuilder.loadTexts:
    cdxCmtsCmCpeGroupRev3.setStatus("obsolete")

cdxQosCtrlGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 10)
)
cdxQosCtrlGroupRev2.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpAdmissionCtrl"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpMaxRsvdBWPercent"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpAdmissionRejects"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpReservedBW"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosCtrlUpMaxVirtualBW"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosIfRateLimitAlgm"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosIfRateLimitExpWt"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosIfRateLimitShpGranularity"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosIfRateLimitShpMaxDelay"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsServiceOutOctets"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsServiceOutPackets"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosMaxUpBWExcessRequests"),
        ("CISCO-DOCS-EXT-MIB", "cdxQosMaxDownBWExcessPackets"),
        ("CISCO-DOCS-EXT-MIB", "cdxUpInfoElemStatsIEType"))
)
if mibBuilder.loadTexts:
    cdxQosCtrlGroupRev2.setStatus("current")

cdxCmtsCmCpeGroupRev4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 11)
)
cdxCmtsCmCpeGroupRev4.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmCpeType"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIpAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIfIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmtsServiceId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmStatusIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeAccessGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeResetNow"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmStatusValue"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusOnlineTimes"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusPercentOnline"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusDynSidCount"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAddlInfo"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapEnable"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapInterval"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmDefaultMaxCpes"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmTotal"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmActive"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmRegistered"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTimeExpiration"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverMacAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverDownFrequency"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverUpChannelId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTrapOnCompletion"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverOpInitiatedTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverState"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverRowStatus"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmMaxCpeNumber"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCurrCpeNumber"))
)
if mibBuilder.loadTexts:
    cdxCmtsCmCpeGroupRev4.setStatus("obsolete")

cdxSpecMgmtGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 12)
)
cdxSpecMgmtGroupRev2.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelWidth"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelModulationProfile"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelCmTotal"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelCmActive"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelCmRegistered"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelInputPowerLevel"))
)
if mibBuilder.loadTexts:
    cdxSpecMgmtGroupRev2.setStatus("obsolete")

cdxSpecMgmtGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 14)
)
cdxSpecMgmtGroupRev3.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelWidth"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelModulationProfile"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelCmTotal"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelCmActive"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelCmRegistered"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelInputPowerLevel"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelAvgUtil"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelAvgContSlots"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelRangeSlots"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelNumActiveUGS"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelMaxUGSLastOneHour"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelMinUGSLastOneHour"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelAvgUGSLastOneHour"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelMaxUGSLastFiveMins"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelMinUGSLastFiveMins"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfUpChannelAvgUGSLastFiveMins"))
)
if mibBuilder.loadTexts:
    cdxSpecMgmtGroupRev3.setStatus("current")

cdxCmtsCmCpeGroupRev5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 15)
)
cdxCmtsCmCpeGroupRev5.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmCpeType"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIfIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmtsServiceId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmStatusIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeAccessGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeResetNow"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmStatusValue"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusOnlineTimes"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusPercentOnline"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusDynSidCount"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAddlInfo"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapEnable"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapInterval"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmDefaultMaxCpes"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmTotal"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmActive"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmRegistered"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTimeExpiration"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverMacAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverDownFrequency"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverUpChannelId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTrapOnCompletion"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverOpInitiatedTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverState"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverRowStatus"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmMaxCpeNumber"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCurrCpeNumber"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusOnlineTimesNum"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusLastResetTime"))
)
if mibBuilder.loadTexts:
    cdxCmtsCmCpeGroupRev5.setStatus("obsolete")

cdxCmtsCmCpeGroupRev6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 16)
)
cdxCmtsCmCpeGroupRev6.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmCpeType"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIfIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmtsServiceId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmStatusIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeAccessGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeResetNow"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmStatusValue"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusOnlineTimes"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusPercentOnline"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusDynSidCount"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAddlInfo"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapEnable"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapInterval"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmDefaultMaxCpes"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmTotal"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmActive"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmRegistered"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTimeExpiration"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverMacAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverDownFrequency"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverUpChannelId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTrapOnCompletion"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverOpInitiatedTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverState"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverRowStatus"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmMaxCpeNumber"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCurrCpeNumber"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmQosProfile"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusOnlineTimesNum"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusLastResetTime"))
)
if mibBuilder.loadTexts:
    cdxCmtsCmCpeGroupRev6.setStatus("obsolete")

cdxCmtsCmCpeGroupRev7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 17)
)
cdxCmtsCmCpeGroupRev7.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmCpeType"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIpAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIfIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmtsServiceId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmStatusIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeAccessGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeResetNow"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmStatusValue"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusOnlineTimes"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusPercentOnline"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusDynSidCount"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAddlInfo"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapEnable"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapInterval"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmDefaultMaxCpes"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmTotal"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmActive"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmRegistered"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmDMICMode"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmDMICLockQos"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTimeExpiration"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverMacAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverDownFrequency"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverUpChannelId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTrapOnCompletion"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverOpInitiatedTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverState"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverRowStatus"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmMaxCpeNumber"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCurrCpeNumber"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmQosProfile"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmStatusDMICMode"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmStatusDMICUnLock"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusOnlineTimesNum"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusLastResetTime"))
)
if mibBuilder.loadTexts:
    cdxCmtsCmCpeGroupRev7.setStatus("obsolete")

cdxCmtsCmCpeGroupRev8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 18)
)
cdxCmtsCmCpeGroupRev8.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmCpeType"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIpAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeIfIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmtsServiceId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmStatusIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeAccessGroup"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeResetNow"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmStatusValue"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusOnlineTimes"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusPercentOnline"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOnlineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMinOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAvgOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusMaxOfflineTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusDynSidCount"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusAddlInfo"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapEnable"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffTrapInterval"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmDefaultMaxCpes"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmTotal"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmActive"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmRegistered"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmDMICMode"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmDMICLockQos"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTimeExpiration"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverMacAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverDownFrequency"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverUpChannelId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverTrapOnCompletion"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverOpInitiatedTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverState"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverRowStatus"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmMaxCpeNumber"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmCurrCpeNumber"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmQosProfile"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmStatusDMICMode"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmStatusDMICUnLock"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusOnlineTimesNum"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsCmStatusLastResetTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmToCpeInetAddressType"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmToCpeInetAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCpeToCmMacAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCpeToCmInetAddressType"),
        ("CISCO-DOCS-EXT-MIB", "cdxCpeToCmInetAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCpeToCmStatusIndex"))
)
if mibBuilder.loadTexts:
    cdxCmtsCmCpeGroupRev8.setStatus("current")

cdxCmtsCmCpeDeleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 20)
)
cdxCmtsCmCpeDeleteGroup.setObjects(
    ("CISCO-DOCS-EXT-MIB", "cdxCmCpeDeleteNow")
)
if mibBuilder.loadTexts:
    cdxCmtsCmCpeDeleteGroup.setStatus("current")

cdxWBResilGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 21)
)
cdxWBResilGroup.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxWBResilRFChangeDampenTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilRFChangeTriggerPercentage"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilRFChangeTriggerCount"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilRFChangeTriggerMoveSecondary"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilNotificationEnable"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilNotificationsInterval"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilEventLevel"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilEventType"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilUpdateTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilEventTotalCount"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilEventTotalDupCount"))
)
if mibBuilder.loadTexts:
    cdxWBResilGroup.setStatus("current")

cdxQosCtrlGroupExt = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 23)
)
cdxQosCtrlGroupExt.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxIfCmtsServiceHCInOctets"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsServiceHCInPackets"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsServiceHCOutOctets"),
        ("CISCO-DOCS-EXT-MIB", "cdxIfCmtsServiceHCOutPackets"))
)
if mibBuilder.loadTexts:
    cdxQosCtrlGroupExt.setStatus("current")

cdxDownstreamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 24)
)
cdxDownstreamGroup.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxPrimaryChannelIfIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxPhysicalRFIfIndex"))
)
if mibBuilder.loadTexts:
    cdxDownstreamGroup.setStatus("current")

cdxCpeIpPrefixGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 25)
)
cdxCpeIpPrefixGroup.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCpeIpPrefixCpeMacAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCpeIpPrefixCpeType"))
)
if mibBuilder.loadTexts:
    cdxCpeIpPrefixGroup.setStatus("current")

cdxCmtsMtcCmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 26)
)
cdxCmtsMtcCmGroup.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmtsMtcCmTotal"),
        ("CISCO-DOCS-EXT-MIB", "cdxCMtsMtcCmOperational"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsMtcCmRegistered"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsMtcCmUnregistered"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsMtcCmOffline"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsMtcCmWideband"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsMtcUpstreamBondGrp"))
)
if mibBuilder.loadTexts:
    cdxCmtsMtcCmGroup.setStatus("current")

cdxCmtsUscbSflowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 27)
)
cdxCmtsUscbSflowGroup.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmtsUscbSfTotal"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsUscbSfPri"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsUscbStaticSfBe"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsUscbStaticSfUgs"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsUscbStaticSfUgsad"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsUscbStaticSfRtps"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsUscbStaticSfNrtps"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsUscbDynSfBe"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsUscbDynSfUgs"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsUscbDynSfUgsad"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsUscbDynSfRtps"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsUscbDynSfNrtps"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsUscbDescr"))
)
if mibBuilder.loadTexts:
    cdxCmtsUscbSflowGroup.setStatus("current")


# Notification objects

cdxCmtsCmOnOffNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 2, 0, 1)
)
cdxCmtsCmOnOffNotification.setObjects(
      *(("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusIpAddress"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusDownChannelIfIndex"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusUpChannelIfIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmCpeCmtsServiceId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmStatusValue"))
)
if mibBuilder.loadTexts:
    cdxCmtsCmOnOffNotification.setStatus(
        "current"
    )

cdxCmtsCmChOverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 2, 0, 2)
)
cdxCmtsCmChOverNotification.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverMacAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverDownFrequency"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverUpChannelId"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverOpInitiatedTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverState"))
)
if mibBuilder.loadTexts:
    cdxCmtsCmChOverNotification.setStatus(
        "current"
    )

cdxCmtsCmDMICLockNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 2, 0, 3)
)
cdxCmtsCmDMICLockNotification.setObjects(
    ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress")
)
if mibBuilder.loadTexts:
    cdxCmtsCmDMICLockNotification.setStatus(
        "current"
    )

cdxWBResilRFDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 2, 0, 4)
)
cdxWBResilRFDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilEventLevel"))
)
if mibBuilder.loadTexts:
    cdxWBResilRFDown.setStatus(
        "current"
    )

cdxWBResilRFUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 2, 0, 5)
)
cdxWBResilRFUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilEventLevel"))
)
if mibBuilder.loadTexts:
    cdxWBResilRFUp.setStatus(
        "current"
    )

cdxWBResilCMPartialServiceNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 2, 0, 6)
)
cdxWBResilCMPartialServiceNotif.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusDownChannelIfIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilEventLevel"))
)
if mibBuilder.loadTexts:
    cdxWBResilCMPartialServiceNotif.setStatus(
        "current"
    )

cdxWBResilCMFullServiceNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 2, 0, 7)
)
cdxWBResilCMFullServiceNotif.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusDownChannelIfIndex"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilEventLevel"))
)
if mibBuilder.loadTexts:
    cdxWBResilCMFullServiceNotif.setStatus(
        "current"
    )

cdxWBResilEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 2, 0, 8)
)
cdxWBResilEvent.setObjects(
      *(("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilEventType"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilUpdateTime"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilEventTotalCount"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilEventTotalDupCount"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilEventLevel"))
)
if mibBuilder.loadTexts:
    cdxWBResilEvent.setStatus(
        "current"
    )


# Notifications groups

cdxNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 13)
)
cdxNotifGroup.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffNotification"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverNotification"))
)
if mibBuilder.loadTexts:
    cdxNotifGroup.setStatus(
        "obsolete"
    )

cdxNotifGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 19)
)
cdxNotifGroupRev1.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxCmtsCmOnOffNotification"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmChOverNotification"),
        ("CISCO-DOCS-EXT-MIB", "cdxCmtsCmDMICLockNotification"))
)
if mibBuilder.loadTexts:
    cdxNotifGroupRev1.setStatus(
        "current"
    )

cdxNotifGroupExt = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 2, 22)
)
cdxNotifGroupExt.setObjects(
      *(("CISCO-DOCS-EXT-MIB", "cdxWBResilRFDown"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilRFUp"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilCMPartialServiceNotif"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilCMFullServiceNotif"),
        ("CISCO-DOCS-EXT-MIB", "cdxWBResilEvent"))
)
if mibBuilder.loadTexts:
    cdxNotifGroupExt.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cdxDocsExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cdxDocsExtCompliance.setStatus(
        "obsolete"
    )

cdxDocsExtComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cdxDocsExtComplianceRev1.setStatus(
        "obsolete"
    )

cdxDocsExtComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cdxDocsExtComplianceRev2.setStatus(
        "obsolete"
    )

cdxDocsExtComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1, 4)
)
if mibBuilder.loadTexts:
    cdxDocsExtComplianceRev3.setStatus(
        "obsolete"
    )

cdxDocsExtComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1, 5)
)
if mibBuilder.loadTexts:
    cdxDocsExtComplianceRev4.setStatus(
        "obsolete"
    )

cdxDocsExtComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1, 6)
)
if mibBuilder.loadTexts:
    cdxDocsExtComplianceRev5.setStatus(
        "obsolete"
    )

cdxDocsExtComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1, 7)
)
if mibBuilder.loadTexts:
    cdxDocsExtComplianceRev6.setStatus(
        "obsolete"
    )

cdxDocsExtComplianceRev7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1, 8)
)
if mibBuilder.loadTexts:
    cdxDocsExtComplianceRev7.setStatus(
        "obsolete"
    )

cdxDocsExtComplianceRev8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1, 9)
)
if mibBuilder.loadTexts:
    cdxDocsExtComplianceRev8.setStatus(
        "obsolete"
    )

cdxDocsExtComplianceRev9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1, 10)
)
if mibBuilder.loadTexts:
    cdxDocsExtComplianceRev9.setStatus(
        "obsolete"
    )

cdxDocsExtComplianceRev10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1, 11)
)
if mibBuilder.loadTexts:
    cdxDocsExtComplianceRev10.setStatus(
        "obsolete"
    )

cdxDocsExtComplianceRev11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1, 12)
)
if mibBuilder.loadTexts:
    cdxDocsExtComplianceRev11.setStatus(
        "deprecated"
    )

cdxDocsExtComplianceRev12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 116, 3, 1, 13)
)
if mibBuilder.loadTexts:
    cdxDocsExtComplianceRev12.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DOCS-EXT-MIB",
    **{"CdxResettableCounter32": CdxResettableCounter32,
       "CdxUpstreamBondGrpList": CdxUpstreamBondGrpList,
       "ciscoDocsExtMIB": ciscoDocsExtMIB,
       "ciscoDocsExtMIBObjects": ciscoDocsExtMIBObjects,
       "cdxQosCtrlObjects": cdxQosCtrlObjects,
       "cdxQosCtrlUpTable": cdxQosCtrlUpTable,
       "cdxQosCtrlUpEntry": cdxQosCtrlUpEntry,
       "cdxQosCtrlUpAdmissionCtrl": cdxQosCtrlUpAdmissionCtrl,
       "cdxQosCtrlUpMaxRsvdBWPercent": cdxQosCtrlUpMaxRsvdBWPercent,
       "cdxQosCtrlUpAdmissionRejects": cdxQosCtrlUpAdmissionRejects,
       "cdxQosCtrlUpReservedBW": cdxQosCtrlUpReservedBW,
       "cdxQosCtrlUpMaxVirtualBW": cdxQosCtrlUpMaxVirtualBW,
       "cdxQosIfRateLimitTable": cdxQosIfRateLimitTable,
       "cdxQosIfRateLimitEntry": cdxQosIfRateLimitEntry,
       "cdxQosIfRateLimitAlgm": cdxQosIfRateLimitAlgm,
       "cdxQosIfRateLimitExpWt": cdxQosIfRateLimitExpWt,
       "cdxQosIfRateLimitShpMaxDelay": cdxQosIfRateLimitShpMaxDelay,
       "cdxQosIfRateLimitShpGranularity": cdxQosIfRateLimitShpGranularity,
       "cdxCmtsServiceExtTable": cdxCmtsServiceExtTable,
       "cdxCmtsServiceExtEntry": cdxCmtsServiceExtEntry,
       "cdxIfCmtsServiceOutOctets": cdxIfCmtsServiceOutOctets,
       "cdxIfCmtsServiceOutPackets": cdxIfCmtsServiceOutPackets,
       "cdxQosMaxUpBWExcessRequests": cdxQosMaxUpBWExcessRequests,
       "cdxQosMaxDownBWExcessPackets": cdxQosMaxDownBWExcessPackets,
       "cdxIfCmtsServiceHCInOctets": cdxIfCmtsServiceHCInOctets,
       "cdxIfCmtsServiceHCInPackets": cdxIfCmtsServiceHCInPackets,
       "cdxIfCmtsServiceHCOutOctets": cdxIfCmtsServiceHCOutOctets,
       "cdxIfCmtsServiceHCOutPackets": cdxIfCmtsServiceHCOutPackets,
       "cdxUpInfoElemStatsTable": cdxUpInfoElemStatsTable,
       "cdxUpInfoElemStatsEntry": cdxUpInfoElemStatsEntry,
       "cdxUpInfoElemStatsNameCode": cdxUpInfoElemStatsNameCode,
       "cdxUpInfoElemStatsIEType": cdxUpInfoElemStatsIEType,
       "cdxQosQueueObjects": cdxQosQueueObjects,
       "cdxBWQueueTable": cdxBWQueueTable,
       "cdxBWQueueEntry": cdxBWQueueEntry,
       "cdxBWQueueNameCode": cdxBWQueueNameCode,
       "cdxBWQueueOrder": cdxBWQueueOrder,
       "cdxBWQueueNumServedBeforeYield": cdxBWQueueNumServedBeforeYield,
       "cdxBWQueueType": cdxBWQueueType,
       "cdxBWQueueMaxDepth": cdxBWQueueMaxDepth,
       "cdxBWQueueDepth": cdxBWQueueDepth,
       "cdxBWQueueDiscards": cdxBWQueueDiscards,
       "cdxCmtsCmCpeObjects": cdxCmtsCmCpeObjects,
       "cdxCmCpeTable": cdxCmCpeTable,
       "cdxCmCpeEntry": cdxCmCpeEntry,
       "cdxCmCpeMacAddress": cdxCmCpeMacAddress,
       "cdxCmCpeType": cdxCmCpeType,
       "cdxCmCpeIpAddress": cdxCmCpeIpAddress,
       "cdxCmCpeIfIndex": cdxCmCpeIfIndex,
       "cdxCmCpeCmtsServiceId": cdxCmCpeCmtsServiceId,
       "cdxCmCpeCmStatusIndex": cdxCmCpeCmStatusIndex,
       "cdxCmCpeAccessGroup": cdxCmCpeAccessGroup,
       "cdxCmCpeResetNow": cdxCmCpeResetNow,
       "cdxCmCpeDeleteNow": cdxCmCpeDeleteNow,
       "cdxCmtsCmStatusExtTable": cdxCmtsCmStatusExtTable,
       "cdxCmtsCmStatusExtEntry": cdxCmtsCmStatusExtEntry,
       "cdxCmtsCmStatusValue": cdxCmtsCmStatusValue,
       "cdxIfCmtsCmStatusOnlineTimes": cdxIfCmtsCmStatusOnlineTimes,
       "cdxIfCmtsCmStatusPercentOnline": cdxIfCmtsCmStatusPercentOnline,
       "cdxIfCmtsCmStatusMinOnlineTime": cdxIfCmtsCmStatusMinOnlineTime,
       "cdxIfCmtsCmStatusAvgOnlineTime": cdxIfCmtsCmStatusAvgOnlineTime,
       "cdxIfCmtsCmStatusMaxOnlineTime": cdxIfCmtsCmStatusMaxOnlineTime,
       "cdxIfCmtsCmStatusMinOfflineTime": cdxIfCmtsCmStatusMinOfflineTime,
       "cdxIfCmtsCmStatusAvgOfflineTime": cdxIfCmtsCmStatusAvgOfflineTime,
       "cdxIfCmtsCmStatusMaxOfflineTime": cdxIfCmtsCmStatusMaxOfflineTime,
       "cdxIfCmtsCmStatusDynSidCount": cdxIfCmtsCmStatusDynSidCount,
       "cdxIfCmtsCmStatusAddlInfo": cdxIfCmtsCmStatusAddlInfo,
       "cdxIfCmtsCmStatusOnlineTimesNum": cdxIfCmtsCmStatusOnlineTimesNum,
       "cdxIfCmtsCmStatusLastResetTime": cdxIfCmtsCmStatusLastResetTime,
       "cdxCmtsMacExtTable": cdxCmtsMacExtTable,
       "cdxCmtsMacExtEntry": cdxCmtsMacExtEntry,
       "cdxCmtsCmOnOffTrapEnable": cdxCmtsCmOnOffTrapEnable,
       "cdxCmtsCmOnOffTrapInterval": cdxCmtsCmOnOffTrapInterval,
       "cdxCmtsCmDefaultMaxCpes": cdxCmtsCmDefaultMaxCpes,
       "cdxCmtsCmTotal": cdxCmtsCmTotal,
       "cdxCmtsCmActive": cdxCmtsCmActive,
       "cdxCmtsCmRegistered": cdxCmtsCmRegistered,
       "cdxCmtsCmDMICMode": cdxCmtsCmDMICMode,
       "cdxCmtsCmDMICLockQos": cdxCmtsCmDMICLockQos,
       "cdxCmtsCmChOverTimeExpiration": cdxCmtsCmChOverTimeExpiration,
       "cdxCmtsCmChOverTable": cdxCmtsCmChOverTable,
       "cdxCmtsCmChOverEntry": cdxCmtsCmChOverEntry,
       "cdxCmtsCmChOverSerialNumber": cdxCmtsCmChOverSerialNumber,
       "cdxCmtsCmChOverMacAddress": cdxCmtsCmChOverMacAddress,
       "cdxCmtsCmChOverDownFrequency": cdxCmtsCmChOverDownFrequency,
       "cdxCmtsCmChOverUpChannelId": cdxCmtsCmChOverUpChannelId,
       "cdxCmtsCmChOverTrapOnCompletion": cdxCmtsCmChOverTrapOnCompletion,
       "cdxCmtsCmChOverOpInitiatedTime": cdxCmtsCmChOverOpInitiatedTime,
       "cdxCmtsCmChOverState": cdxCmtsCmChOverState,
       "cdxCmtsCmChOverRowStatus": cdxCmtsCmChOverRowStatus,
       "cdxCmtsCmTable": cdxCmtsCmTable,
       "cdxCmtsCmEntry": cdxCmtsCmEntry,
       "cdxCmtsCmMaxCpeNumber": cdxCmtsCmMaxCpeNumber,
       "cdxCmtsCmCurrCpeNumber": cdxCmtsCmCurrCpeNumber,
       "cdxCmtsCmQosProfile": cdxCmtsCmQosProfile,
       "cdxCmtsCmStatusDMICTable": cdxCmtsCmStatusDMICTable,
       "cdxCmtsCmStatusDMICEntry": cdxCmtsCmStatusDMICEntry,
       "cdxCmtsCmStatusDMICMode": cdxCmtsCmStatusDMICMode,
       "cdxCmtsCmStatusDMICUnLock": cdxCmtsCmStatusDMICUnLock,
       "cdxCmToCpeTable": cdxCmToCpeTable,
       "cdxCmToCpeEntry": cdxCmToCpeEntry,
       "cdxCmToCpeCmMacAddress": cdxCmToCpeCmMacAddress,
       "cdxCmToCpeInetAddressType": cdxCmToCpeInetAddressType,
       "cdxCmToCpeInetAddress": cdxCmToCpeInetAddress,
       "cdxCpeToCmTable": cdxCpeToCmTable,
       "cdxCpeToCmEntry": cdxCpeToCmEntry,
       "cdxCpeToCmCpeMacAddress": cdxCpeToCmCpeMacAddress,
       "cdxCpeToCmMacAddress": cdxCpeToCmMacAddress,
       "cdxCpeToCmInetAddressType": cdxCpeToCmInetAddressType,
       "cdxCpeToCmInetAddress": cdxCpeToCmInetAddress,
       "cdxCpeToCmStatusIndex": cdxCpeToCmStatusIndex,
       "cdxCpeIpPrefixTable": cdxCpeIpPrefixTable,
       "cdxCpeIpPrefixEntry": cdxCpeIpPrefixEntry,
       "cdxCpeIpPrefixCmMacAddress": cdxCpeIpPrefixCmMacAddress,
       "cdxCpeIpPrefixType": cdxCpeIpPrefixType,
       "cdxCpeIpPrefixAddress": cdxCpeIpPrefixAddress,
       "cdxCpeIpPrefixLen": cdxCpeIpPrefixLen,
       "cdxCpeIpPrefixCpeMacAddress": cdxCpeIpPrefixCpeMacAddress,
       "cdxCpeIpPrefixCpeType": cdxCpeIpPrefixCpeType,
       "cdxSpecMgmtObjects": cdxSpecMgmtObjects,
       "cdxIfUpstreamChannelExtTable": cdxIfUpstreamChannelExtTable,
       "cdxIfUpstreamChannelExtEntry": cdxIfUpstreamChannelExtEntry,
       "cdxIfUpChannelWidth": cdxIfUpChannelWidth,
       "cdxIfUpChannelModulationProfile": cdxIfUpChannelModulationProfile,
       "cdxIfUpChannelCmTotal": cdxIfUpChannelCmTotal,
       "cdxIfUpChannelCmActive": cdxIfUpChannelCmActive,
       "cdxIfUpChannelCmRegistered": cdxIfUpChannelCmRegistered,
       "cdxIfUpChannelInputPowerLevel": cdxIfUpChannelInputPowerLevel,
       "cdxIfUpChannelAvgUtil": cdxIfUpChannelAvgUtil,
       "cdxIfUpChannelAvgContSlots": cdxIfUpChannelAvgContSlots,
       "cdxIfUpChannelRangeSlots": cdxIfUpChannelRangeSlots,
       "cdxIfUpChannelNumActiveUGS": cdxIfUpChannelNumActiveUGS,
       "cdxIfUpChannelMaxUGSLastOneHour": cdxIfUpChannelMaxUGSLastOneHour,
       "cdxIfUpChannelMinUGSLastOneHour": cdxIfUpChannelMinUGSLastOneHour,
       "cdxIfUpChannelAvgUGSLastOneHour": cdxIfUpChannelAvgUGSLastOneHour,
       "cdxIfUpChannelMaxUGSLastFiveMins": cdxIfUpChannelMaxUGSLastFiveMins,
       "cdxIfUpChannelMinUGSLastFiveMins": cdxIfUpChannelMinUGSLastFiveMins,
       "cdxIfUpChannelAvgUGSLastFiveMins": cdxIfUpChannelAvgUGSLastFiveMins,
       "cdxWBResilObjects": cdxWBResilObjects,
       "cdxWBResilRFChangeDampenTime": cdxWBResilRFChangeDampenTime,
       "cdxWBResilRFChangeTriggerPercentage": cdxWBResilRFChangeTriggerPercentage,
       "cdxWBResilRFChangeTriggerCount": cdxWBResilRFChangeTriggerCount,
       "cdxWBResilRFChangeTriggerMoveSecondary": cdxWBResilRFChangeTriggerMoveSecondary,
       "cdxWBResilNotificationEnable": cdxWBResilNotificationEnable,
       "cdxWBResilNotificationsInterval": cdxWBResilNotificationsInterval,
       "cdxWBResilEventLevel": cdxWBResilEventLevel,
       "cdxWBResilEventType": cdxWBResilEventType,
       "cdxWBResilUpdateTime": cdxWBResilUpdateTime,
       "cdxWBResilEventTotalCount": cdxWBResilEventTotalCount,
       "cdxWBResilEventTotalDupCount": cdxWBResilEventTotalDupCount,
       "cdxDownstreamObjects": cdxDownstreamObjects,
       "cdxRFtoPrimaryChannelMappingTable": cdxRFtoPrimaryChannelMappingTable,
       "cdxRFtoPrimaryChannelMappingEntry": cdxRFtoPrimaryChannelMappingEntry,
       "cdxPrimaryChannelIfIndex": cdxPrimaryChannelIfIndex,
       "cdxPrimaryChanneltoRFMappingTable": cdxPrimaryChanneltoRFMappingTable,
       "cdxPrimaryChanneltoRFMappingEntry": cdxPrimaryChanneltoRFMappingEntry,
       "cdxPhysicalRFIfIndex": cdxPhysicalRFIfIndex,
       "cdxCmtsMtcCmSfObjects": cdxCmtsMtcCmSfObjects,
       "cdxCmtsMtcCmTable": cdxCmtsMtcCmTable,
       "cdxCmtsMtcCmEntry": cdxCmtsMtcCmEntry,
       "cdxCmtsMtcTcsId": cdxCmtsMtcTcsId,
       "cdxCmtsMtcCmTotal": cdxCmtsMtcCmTotal,
       "cdxCMtsMtcCmOperational": cdxCMtsMtcCmOperational,
       "cdxCmtsMtcCmRegistered": cdxCmtsMtcCmRegistered,
       "cdxCmtsMtcCmUnregistered": cdxCmtsMtcCmUnregistered,
       "cdxCmtsMtcCmOffline": cdxCmtsMtcCmOffline,
       "cdxCmtsMtcCmWideband": cdxCmtsMtcCmWideband,
       "cdxCmtsMtcUpstreamBondGrp": cdxCmtsMtcUpstreamBondGrp,
       "cdxCmtsUscbSflowTable": cdxCmtsUscbSflowTable,
       "cdxCmtsUscbSflowEntry": cdxCmtsUscbSflowEntry,
       "cdxCmtsUsBondingGrpId": cdxCmtsUsBondingGrpId,
       "cdxCmtsUscbSfTotal": cdxCmtsUscbSfTotal,
       "cdxCmtsUscbSfPri": cdxCmtsUscbSfPri,
       "cdxCmtsUscbStaticSfBe": cdxCmtsUscbStaticSfBe,
       "cdxCmtsUscbStaticSfUgs": cdxCmtsUscbStaticSfUgs,
       "cdxCmtsUscbStaticSfUgsad": cdxCmtsUscbStaticSfUgsad,
       "cdxCmtsUscbStaticSfRtps": cdxCmtsUscbStaticSfRtps,
       "cdxCmtsUscbStaticSfNrtps": cdxCmtsUscbStaticSfNrtps,
       "cdxCmtsUscbDynSfBe": cdxCmtsUscbDynSfBe,
       "cdxCmtsUscbDynSfUgs": cdxCmtsUscbDynSfUgs,
       "cdxCmtsUscbDynSfUgsad": cdxCmtsUscbDynSfUgsad,
       "cdxCmtsUscbDynSfRtps": cdxCmtsUscbDynSfRtps,
       "cdxCmtsUscbDynSfNrtps": cdxCmtsUscbDynSfNrtps,
       "cdxCmtsUscbDescr": cdxCmtsUscbDescr,
       "ciscoDocsExtNotificationsPrefix": ciscoDocsExtNotificationsPrefix,
       "ciscoDocsExtNotifications": ciscoDocsExtNotifications,
       "cdxCmtsCmOnOffNotification": cdxCmtsCmOnOffNotification,
       "cdxCmtsCmChOverNotification": cdxCmtsCmChOverNotification,
       "cdxCmtsCmDMICLockNotification": cdxCmtsCmDMICLockNotification,
       "cdxWBResilRFDown": cdxWBResilRFDown,
       "cdxWBResilRFUp": cdxWBResilRFUp,
       "cdxWBResilCMPartialServiceNotif": cdxWBResilCMPartialServiceNotif,
       "cdxWBResilCMFullServiceNotif": cdxWBResilCMFullServiceNotif,
       "cdxWBResilEvent": cdxWBResilEvent,
       "ciscoDocsExtConformance": ciscoDocsExtConformance,
       "cdxDocsExtCompliances": cdxDocsExtCompliances,
       "cdxDocsExtCompliance": cdxDocsExtCompliance,
       "cdxDocsExtComplianceRev1": cdxDocsExtComplianceRev1,
       "cdxDocsExtComplianceRev2": cdxDocsExtComplianceRev2,
       "cdxDocsExtComplianceRev3": cdxDocsExtComplianceRev3,
       "cdxDocsExtComplianceRev4": cdxDocsExtComplianceRev4,
       "cdxDocsExtComplianceRev5": cdxDocsExtComplianceRev5,
       "cdxDocsExtComplianceRev6": cdxDocsExtComplianceRev6,
       "cdxDocsExtComplianceRev7": cdxDocsExtComplianceRev7,
       "cdxDocsExtComplianceRev8": cdxDocsExtComplianceRev8,
       "cdxDocsExtComplianceRev9": cdxDocsExtComplianceRev9,
       "cdxDocsExtComplianceRev10": cdxDocsExtComplianceRev10,
       "cdxDocsExtComplianceRev11": cdxDocsExtComplianceRev11,
       "cdxDocsExtComplianceRev12": cdxDocsExtComplianceRev12,
       "cdxDocsExtGroups": cdxDocsExtGroups,
       "cdxQosCtrlGroup": cdxQosCtrlGroup,
       "cdxQosQueueGroup": cdxQosQueueGroup,
       "cdxCmtsCmCpeGroup": cdxCmtsCmCpeGroup,
       "cdxQosCtrlGroupRev1": cdxQosCtrlGroupRev1,
       "cdxCmtsCmCpeGroupRev1": cdxCmtsCmCpeGroupRev1,
       "cdxSpecMgmtGroup": cdxSpecMgmtGroup,
       "cdxCmtsCmCpeGroupRev2": cdxCmtsCmCpeGroupRev2,
       "cdxSpecMgmtGroupRev1": cdxSpecMgmtGroupRev1,
       "cdxCmtsCmCpeGroupRev3": cdxCmtsCmCpeGroupRev3,
       "cdxQosCtrlGroupRev2": cdxQosCtrlGroupRev2,
       "cdxCmtsCmCpeGroupRev4": cdxCmtsCmCpeGroupRev4,
       "cdxSpecMgmtGroupRev2": cdxSpecMgmtGroupRev2,
       "cdxNotifGroup": cdxNotifGroup,
       "cdxSpecMgmtGroupRev3": cdxSpecMgmtGroupRev3,
       "cdxCmtsCmCpeGroupRev5": cdxCmtsCmCpeGroupRev5,
       "cdxCmtsCmCpeGroupRev6": cdxCmtsCmCpeGroupRev6,
       "cdxCmtsCmCpeGroupRev7": cdxCmtsCmCpeGroupRev7,
       "cdxCmtsCmCpeGroupRev8": cdxCmtsCmCpeGroupRev8,
       "cdxNotifGroupRev1": cdxNotifGroupRev1,
       "cdxCmtsCmCpeDeleteGroup": cdxCmtsCmCpeDeleteGroup,
       "cdxWBResilGroup": cdxWBResilGroup,
       "cdxNotifGroupExt": cdxNotifGroupExt,
       "cdxQosCtrlGroupExt": cdxQosCtrlGroupExt,
       "cdxDownstreamGroup": cdxDownstreamGroup,
       "cdxCpeIpPrefixGroup": cdxCpeIpPrefixGroup,
       "cdxCmtsMtcCmGroup": cdxCmtsMtcCmGroup,
       "cdxCmtsUscbSflowGroup": cdxCmtsUscbSflowGroup}
)
