# SNMP MIB module (DOCS-IF31-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOCS-IF31-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:47 2024
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

(TenthdBmV,
 docsIfUpstreamChannelEntry) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "TenthdBmV",
    "docsIfUpstreamChannelEntry")

(AttributeMask,
 IfDirection,
 RangingState,
 docsIf3CmtsCmRegStatusEntry,
 docsIf3CmtsCmRegStatusId) = mibBuilder.importSymbols(
    "DOCS-IF3-MIB",
    "AttributeMask",
    "IfDirection",
    "RangingState",
    "docsIf3CmtsCmRegStatusEntry",
    "docsIf3CmtsCmRegStatusId")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

docsIf31Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28)
)
docsIf31Mib.setRevisions(
        ("2017-05-25 00:00",
         "2016-12-15 00:00",
         "2016-08-18 00:00",
         "2016-05-05 00:00",
         "2015-11-04 00:00",
         "2015-07-15 00:00",
         "2015-05-20 00:00",
         "2015-04-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ClabsDocsisVersion(Integer32, TextualConvention):
    status = "current"
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
        *(("docsis10", 1),
          ("docsis11", 2),
          ("docsis20", 3),
          ("docsis30", 4),
          ("docsis31", 5),
          ("other", 0))
    )



class EmIdList(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x,"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(2, 2),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(6, 6),
    )



class SubcarrierSpacingType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 25),
        ValueRangeConstraint(50, 50),
    )



class PrimaryDsIndicatorType(Integer32, TextualConvention):
    status = "current"
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
        *(("backupPrimary", 3),
          ("nonPrimary", 4),
          ("other", 1),
          ("primary", 2))
    )



class OfdmProfiles(Bits, TextualConvention):
    status = "current"


class DsOfdmCyclicPrefix(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(192, 192),
        ValueRangeConstraint(256, 256),
        ValueRangeConstraint(512, 512),
        ValueRangeConstraint(768, 768),
        ValueRangeConstraint(1024, 1024),
    )



class UsOfdmaCyclicPrefix(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 96),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(192, 192),
        ValueRangeConstraint(224, 224),
        ValueRangeConstraint(256, 256),
        ValueRangeConstraint(288, 288),
        ValueRangeConstraint(320, 320),
        ValueRangeConstraint(384, 384),
        ValueRangeConstraint(512, 512),
        ValueRangeConstraint(640, 640),
    )



class DsOfdmRollOffPeriod(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(192, 192),
        ValueRangeConstraint(256, 256),
    )



class UsOfdmaRollOffPeriod(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(96, 96),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(192, 192),
        ValueRangeConstraint(224, 224),
    )



class TimeInterleaverDepth(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )



class DsOfdmModulationType(Integer32, TextualConvention):
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("qam1024", 9),
          ("qam128", 6),
          ("qam16", 4),
          ("qam16384", 13),
          ("qam2048", 10),
          ("qam256", 7),
          ("qam4096", 11),
          ("qam512", 8),
          ("qam64", 5),
          ("qam8192", 12),
          ("qpsk", 3),
          ("zeroValued", 2))
    )



class UsOfdmaModulationType(Integer32, TextualConvention):
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("bpsk", 3),
          ("other", 1),
          ("qam1024", 12),
          ("qam128", 9),
          ("qam16", 6),
          ("qam2048", 13),
          ("qam256", 10),
          ("qam32", 7),
          ("qam4096", 14),
          ("qam512", 11),
          ("qam64", 8),
          ("qam8", 5),
          ("qpsk", 4),
          ("zeroValued", 2))
    )



class PartialChannelType(Bits, TextualConvention):
    status = "current"


class PartialServiceType(Integer32, TextualConvention):
    status = "current"
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
        *(("none", 2),
          ("other", 1),
          ("partialSvcDsAndUsImpaired", 5),
          ("partialSvcDsOnlyImpaired", 3),
          ("partialSvcUsOnlyImpaired", 4))
    )



class PartialChanReasonType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              16,
              18,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("dpdMismatch", 18),
          ("dsOfdmProfileFailure", 16),
          ("ncpProfileFailure", 20),
          ("none", 0),
          ("plcFailure", 21))
    )



class PartialSvcReasonType(Integer32, TextualConvention):
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
        *(("lostFecLock", 2),
          ("none", 0),
          ("secondaryChanMddTimeout", 1))
    )



class HundredthdBmV(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-2"


class HundredthdB(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-2"


# MIB Managed Objects in the order of their OIDs

_DocsIf31Notifications_ObjectIdentity = ObjectIdentity
docsIf31Notifications = _DocsIf31Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 0)
)
_DocsIf31MibObjects_ObjectIdentity = ObjectIdentity
docsIf31MibObjects = _DocsIf31MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1)
)
_DocsIf31DocsisBaseCapability_Type = ClabsDocsisVersion
_DocsIf31DocsisBaseCapability_Object = MibScalar
docsIf31DocsisBaseCapability = _DocsIf31DocsisBaseCapability_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 1),
    _DocsIf31DocsisBaseCapability_Type()
)
docsIf31DocsisBaseCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31DocsisBaseCapability.setStatus("current")
_DocsIf31RxChStatusTable_Object = MibTable
docsIf31RxChStatusTable = _DocsIf31RxChStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 2)
)
if mibBuilder.loadTexts:
    docsIf31RxChStatusTable.setStatus("current")
_DocsIf31RxChStatusEntry_Object = MibTableRow
docsIf31RxChStatusEntry = _DocsIf31RxChStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 2, 1)
)
docsIf31RxChStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIf31RxChStatusEntry.setStatus("current")
_DocsIf31RxChStatusPrimaryDsIndicator_Type = PrimaryDsIndicatorType
_DocsIf31RxChStatusPrimaryDsIndicator_Object = MibTableColumn
docsIf31RxChStatusPrimaryDsIndicator = _DocsIf31RxChStatusPrimaryDsIndicator_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 2, 1, 1),
    _DocsIf31RxChStatusPrimaryDsIndicator_Type()
)
docsIf31RxChStatusPrimaryDsIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31RxChStatusPrimaryDsIndicator.setStatus("current")
_DocsIf31RxChStatusOfdmProfiles_Type = OfdmProfiles
_DocsIf31RxChStatusOfdmProfiles_Object = MibTableColumn
docsIf31RxChStatusOfdmProfiles = _DocsIf31RxChStatusOfdmProfiles_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 2, 1, 2),
    _DocsIf31RxChStatusOfdmProfiles_Type()
)
docsIf31RxChStatusOfdmProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31RxChStatusOfdmProfiles.setStatus("current")
_DocsIf31CmtsCmRegStatusTable_Object = MibTable
docsIf31CmtsCmRegStatusTable = _DocsIf31CmtsCmRegStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 3)
)
if mibBuilder.loadTexts:
    docsIf31CmtsCmRegStatusTable.setStatus("current")
_DocsIf31CmtsCmRegStatusEntry_Object = MibTableRow
docsIf31CmtsCmRegStatusEntry = _DocsIf31CmtsCmRegStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 3, 1)
)
if mibBuilder.loadTexts:
    docsIf31CmtsCmRegStatusEntry.setStatus("current")
_DocsIf31CmtsCmRegStatusAssignedEmIds_Type = EmIdList
_DocsIf31CmtsCmRegStatusAssignedEmIds_Object = MibTableColumn
docsIf31CmtsCmRegStatusAssignedEmIds = _DocsIf31CmtsCmRegStatusAssignedEmIds_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 3, 1, 1),
    _DocsIf31CmtsCmRegStatusAssignedEmIds_Type()
)
docsIf31CmtsCmRegStatusAssignedEmIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmRegStatusAssignedEmIds.setStatus("current")


class _DocsIf31CmtsCmRegStatusDsProfileIdList_Type(OctetString):
    """Custom type docsIf31CmtsCmRegStatusDsProfileIdList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(6, 72),
    )


_DocsIf31CmtsCmRegStatusDsProfileIdList_Type.__name__ = "OctetString"
_DocsIf31CmtsCmRegStatusDsProfileIdList_Object = MibTableColumn
docsIf31CmtsCmRegStatusDsProfileIdList = _DocsIf31CmtsCmRegStatusDsProfileIdList_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 3, 1, 2),
    _DocsIf31CmtsCmRegStatusDsProfileIdList_Type()
)
docsIf31CmtsCmRegStatusDsProfileIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmRegStatusDsProfileIdList.setStatus("current")


class _DocsIf31CmtsCmRegStatusUsProfileIucList_Type(OctetString):
    """Custom type docsIf31CmtsCmRegStatusUsProfileIucList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(6, 72),
    )


_DocsIf31CmtsCmRegStatusUsProfileIucList_Type.__name__ = "OctetString"
_DocsIf31CmtsCmRegStatusUsProfileIucList_Object = MibTableColumn
docsIf31CmtsCmRegStatusUsProfileIucList = _DocsIf31CmtsCmRegStatusUsProfileIucList_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 3, 1, 3),
    _DocsIf31CmtsCmRegStatusUsProfileIucList_Type()
)
docsIf31CmtsCmRegStatusUsProfileIucList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmRegStatusUsProfileIucList.setStatus("current")


class _DocsIf31CmtsCmRegStatusTcsPhigh_Type(Unsigned32):
    """Custom type docsIf31CmtsCmRegStatusTcsPhigh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(68, 320),
    )


_DocsIf31CmtsCmRegStatusTcsPhigh_Type.__name__ = "Unsigned32"
_DocsIf31CmtsCmRegStatusTcsPhigh_Object = MibTableColumn
docsIf31CmtsCmRegStatusTcsPhigh = _DocsIf31CmtsCmRegStatusTcsPhigh_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 3, 1, 4),
    _DocsIf31CmtsCmRegStatusTcsPhigh_Type()
)
docsIf31CmtsCmRegStatusTcsPhigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmRegStatusTcsPhigh.setStatus("current")
_DocsIf31CmtsCmRegStatusTcsDrwTop_Type = Unsigned32
_DocsIf31CmtsCmRegStatusTcsDrwTop_Object = MibTableColumn
docsIf31CmtsCmRegStatusTcsDrwTop = _DocsIf31CmtsCmRegStatusTcsDrwTop_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 3, 1, 5),
    _DocsIf31CmtsCmRegStatusTcsDrwTop_Type()
)
docsIf31CmtsCmRegStatusTcsDrwTop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmRegStatusTcsDrwTop.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsCmRegStatusTcsDrwTop.setUnits("dBmV")
_DocsIf31CmtsCmRegStatusMinUsableDsFreq_Type = Unsigned32
_DocsIf31CmtsCmRegStatusMinUsableDsFreq_Object = MibTableColumn
docsIf31CmtsCmRegStatusMinUsableDsFreq = _DocsIf31CmtsCmRegStatusMinUsableDsFreq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 3, 1, 6),
    _DocsIf31CmtsCmRegStatusMinUsableDsFreq_Type()
)
docsIf31CmtsCmRegStatusMinUsableDsFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmRegStatusMinUsableDsFreq.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsCmRegStatusMinUsableDsFreq.setUnits("Hz")
_DocsIf31CmtsCmRegStatusMaxUsableDsFreq_Type = Unsigned32
_DocsIf31CmtsCmRegStatusMaxUsableDsFreq_Object = MibTableColumn
docsIf31CmtsCmRegStatusMaxUsableDsFreq = _DocsIf31CmtsCmRegStatusMaxUsableDsFreq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 3, 1, 7),
    _DocsIf31CmtsCmRegStatusMaxUsableDsFreq_Type()
)
docsIf31CmtsCmRegStatusMaxUsableDsFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmRegStatusMaxUsableDsFreq.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsCmRegStatusMaxUsableDsFreq.setUnits("Hz")
_DocsIf31CmtsCmRegStatusMaxUsableUsFreq_Type = Unsigned32
_DocsIf31CmtsCmRegStatusMaxUsableUsFreq_Object = MibTableColumn
docsIf31CmtsCmRegStatusMaxUsableUsFreq = _DocsIf31CmtsCmRegStatusMaxUsableUsFreq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 3, 1, 8),
    _DocsIf31CmtsCmRegStatusMaxUsableUsFreq_Type()
)
docsIf31CmtsCmRegStatusMaxUsableUsFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmRegStatusMaxUsableUsFreq.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsCmRegStatusMaxUsableUsFreq.setUnits("Hz")
_DocsIf31CmtsCmRegStatusPartialSvcState_Type = PartialServiceType
_DocsIf31CmtsCmRegStatusPartialSvcState_Object = MibTableColumn
docsIf31CmtsCmRegStatusPartialSvcState = _DocsIf31CmtsCmRegStatusPartialSvcState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 3, 1, 9),
    _DocsIf31CmtsCmRegStatusPartialSvcState_Type()
)
docsIf31CmtsCmRegStatusPartialSvcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmRegStatusPartialSvcState.setStatus("current")
_DocsIf31CmtsCmRegStatusPartialChanState_Type = PartialChannelType
_DocsIf31CmtsCmRegStatusPartialChanState_Object = MibTableColumn
docsIf31CmtsCmRegStatusPartialChanState = _DocsIf31CmtsCmRegStatusPartialChanState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 3, 1, 10),
    _DocsIf31CmtsCmRegStatusPartialChanState_Type()
)
docsIf31CmtsCmRegStatusPartialChanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmRegStatusPartialChanState.setStatus("current")
_DocsIf31CmtsCmUsOfdmaChannelStatusTable_Object = MibTable
docsIf31CmtsCmUsOfdmaChannelStatusTable = _DocsIf31CmtsCmUsOfdmaChannelStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 4)
)
if mibBuilder.loadTexts:
    docsIf31CmtsCmUsOfdmaChannelStatusTable.setStatus("current")
_DocsIf31CmtsCmUsOfdmaChannelStatusEntry_Object = MibTableRow
docsIf31CmtsCmUsOfdmaChannelStatusEntry = _DocsIf31CmtsCmUsOfdmaChannelStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 4, 1)
)
docsIf31CmtsCmUsOfdmaChannelStatusEntry.setIndexNames(
    (0, "DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIf31CmtsCmUsOfdmaChannelStatusEntry.setStatus("current")
_DocsIf31CmtsCmUsOfdmaChannelRxPower_Type = TenthdBmV
_DocsIf31CmtsCmUsOfdmaChannelRxPower_Object = MibTableColumn
docsIf31CmtsCmUsOfdmaChannelRxPower = _DocsIf31CmtsCmUsOfdmaChannelRxPower_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 4, 1, 1),
    _DocsIf31CmtsCmUsOfdmaChannelRxPower_Type()
)
docsIf31CmtsCmUsOfdmaChannelRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmUsOfdmaChannelRxPower.setStatus("current")
_DocsIf31CmtsCmUsOfdmaChannelMeanRxMer_Type = HundredthdB
_DocsIf31CmtsCmUsOfdmaChannelMeanRxMer_Object = MibTableColumn
docsIf31CmtsCmUsOfdmaChannelMeanRxMer = _DocsIf31CmtsCmUsOfdmaChannelMeanRxMer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 4, 1, 2),
    _DocsIf31CmtsCmUsOfdmaChannelMeanRxMer_Type()
)
docsIf31CmtsCmUsOfdmaChannelMeanRxMer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmUsOfdmaChannelMeanRxMer.setStatus("current")
_DocsIf31CmtsCmUsOfdmaChannelStdDevRxMer_Type = HundredthdB
_DocsIf31CmtsCmUsOfdmaChannelStdDevRxMer_Object = MibTableColumn
docsIf31CmtsCmUsOfdmaChannelStdDevRxMer = _DocsIf31CmtsCmUsOfdmaChannelStdDevRxMer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 4, 1, 3),
    _DocsIf31CmtsCmUsOfdmaChannelStdDevRxMer_Type()
)
docsIf31CmtsCmUsOfdmaChannelStdDevRxMer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmUsOfdmaChannelStdDevRxMer.setStatus("current")


class _DocsIf31CmtsCmUsOfdmaChannelRxMerThreshold_Type(Unsigned32):
    """Custom type docsIf31CmtsCmUsOfdmaChannelRxMerThreshold based on Unsigned32"""
    defaultValue = 2


_DocsIf31CmtsCmUsOfdmaChannelRxMerThreshold_Object = MibTableColumn
docsIf31CmtsCmUsOfdmaChannelRxMerThreshold = _DocsIf31CmtsCmUsOfdmaChannelRxMerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 4, 1, 4),
    _DocsIf31CmtsCmUsOfdmaChannelRxMerThreshold_Type()
)
docsIf31CmtsCmUsOfdmaChannelRxMerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf31CmtsCmUsOfdmaChannelRxMerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsCmUsOfdmaChannelRxMerThreshold.setUnits("percentile")
_DocsIf31CmtsCmUsOfdmaChannelThresholdRxMerValue_Type = HundredthdB
_DocsIf31CmtsCmUsOfdmaChannelThresholdRxMerValue_Object = MibTableColumn
docsIf31CmtsCmUsOfdmaChannelThresholdRxMerValue = _DocsIf31CmtsCmUsOfdmaChannelThresholdRxMerValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 4, 1, 5),
    _DocsIf31CmtsCmUsOfdmaChannelThresholdRxMerValue_Type()
)
docsIf31CmtsCmUsOfdmaChannelThresholdRxMerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmUsOfdmaChannelThresholdRxMerValue.setStatus("current")
_DocsIf31CmtsCmUsOfdmaChannelThresholdRxMerHighestFreq_Type = Unsigned32
_DocsIf31CmtsCmUsOfdmaChannelThresholdRxMerHighestFreq_Object = MibTableColumn
docsIf31CmtsCmUsOfdmaChannelThresholdRxMerHighestFreq = _DocsIf31CmtsCmUsOfdmaChannelThresholdRxMerHighestFreq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 4, 1, 6),
    _DocsIf31CmtsCmUsOfdmaChannelThresholdRxMerHighestFreq_Type()
)
docsIf31CmtsCmUsOfdmaChannelThresholdRxMerHighestFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmUsOfdmaChannelThresholdRxMerHighestFreq.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsCmUsOfdmaChannelThresholdRxMerHighestFreq.setUnits("Hz")
_DocsIf31CmtsCmUsOfdmaChannelMicroreflections_Type = Unsigned32
_DocsIf31CmtsCmUsOfdmaChannelMicroreflections_Object = MibTableColumn
docsIf31CmtsCmUsOfdmaChannelMicroreflections = _DocsIf31CmtsCmUsOfdmaChannelMicroreflections_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 4, 1, 7),
    _DocsIf31CmtsCmUsOfdmaChannelMicroreflections_Type()
)
docsIf31CmtsCmUsOfdmaChannelMicroreflections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmUsOfdmaChannelMicroreflections.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsCmUsOfdmaChannelMicroreflections.setUnits("dBc")
_DocsIf31CmtsCmUsOfdmaChannelHighResolutionTimingOffset_Type = Integer32
_DocsIf31CmtsCmUsOfdmaChannelHighResolutionTimingOffset_Object = MibTableColumn
docsIf31CmtsCmUsOfdmaChannelHighResolutionTimingOffset = _DocsIf31CmtsCmUsOfdmaChannelHighResolutionTimingOffset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 4, 1, 8),
    _DocsIf31CmtsCmUsOfdmaChannelHighResolutionTimingOffset_Type()
)
docsIf31CmtsCmUsOfdmaChannelHighResolutionTimingOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmUsOfdmaChannelHighResolutionTimingOffset.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsCmUsOfdmaChannelHighResolutionTimingOffset.setUnits("time tick/(64*256)")
_DocsIf31CmtsCmUsOfdmaChannelIsMuted_Type = TruthValue
_DocsIf31CmtsCmUsOfdmaChannelIsMuted_Object = MibTableColumn
docsIf31CmtsCmUsOfdmaChannelIsMuted = _DocsIf31CmtsCmUsOfdmaChannelIsMuted_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 4, 1, 9),
    _DocsIf31CmtsCmUsOfdmaChannelIsMuted_Type()
)
docsIf31CmtsCmUsOfdmaChannelIsMuted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmUsOfdmaChannelIsMuted.setStatus("current")
_DocsIf31CmtsCmUsOfdmaChannelRangingStatus_Type = RangingState
_DocsIf31CmtsCmUsOfdmaChannelRangingStatus_Object = MibTableColumn
docsIf31CmtsCmUsOfdmaChannelRangingStatus = _DocsIf31CmtsCmUsOfdmaChannelRangingStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 4, 1, 10),
    _DocsIf31CmtsCmUsOfdmaChannelRangingStatus_Type()
)
docsIf31CmtsCmUsOfdmaChannelRangingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmUsOfdmaChannelRangingStatus.setStatus("current")
_DocsIf31CmtsCmUsOfdmaChannelCurPartialSvcReasonCode_Type = PartialSvcReasonType
_DocsIf31CmtsCmUsOfdmaChannelCurPartialSvcReasonCode_Object = MibTableColumn
docsIf31CmtsCmUsOfdmaChannelCurPartialSvcReasonCode = _DocsIf31CmtsCmUsOfdmaChannelCurPartialSvcReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 4, 1, 11),
    _DocsIf31CmtsCmUsOfdmaChannelCurPartialSvcReasonCode_Type()
)
docsIf31CmtsCmUsOfdmaChannelCurPartialSvcReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmUsOfdmaChannelCurPartialSvcReasonCode.setStatus("current")
_DocsIf31CmtsCmUsOfdmaChannelLastPartialSvcTime_Type = DateAndTime
_DocsIf31CmtsCmUsOfdmaChannelLastPartialSvcTime_Object = MibTableColumn
docsIf31CmtsCmUsOfdmaChannelLastPartialSvcTime = _DocsIf31CmtsCmUsOfdmaChannelLastPartialSvcTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 4, 1, 12),
    _DocsIf31CmtsCmUsOfdmaChannelLastPartialSvcTime_Type()
)
docsIf31CmtsCmUsOfdmaChannelLastPartialSvcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmUsOfdmaChannelLastPartialSvcTime.setStatus("current")
_DocsIf31CmtsCmUsOfdmaChannelLastPartialSvcReasonCode_Type = PartialSvcReasonType
_DocsIf31CmtsCmUsOfdmaChannelLastPartialSvcReasonCode_Object = MibTableColumn
docsIf31CmtsCmUsOfdmaChannelLastPartialSvcReasonCode = _DocsIf31CmtsCmUsOfdmaChannelLastPartialSvcReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 4, 1, 13),
    _DocsIf31CmtsCmUsOfdmaChannelLastPartialSvcReasonCode_Type()
)
docsIf31CmtsCmUsOfdmaChannelLastPartialSvcReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmUsOfdmaChannelLastPartialSvcReasonCode.setStatus("current")
_DocsIf31CmtsCmUsOfdmaChannelNumPartialSvcIncidents_Type = Counter32
_DocsIf31CmtsCmUsOfdmaChannelNumPartialSvcIncidents_Object = MibTableColumn
docsIf31CmtsCmUsOfdmaChannelNumPartialSvcIncidents = _DocsIf31CmtsCmUsOfdmaChannelNumPartialSvcIncidents_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 4, 1, 14),
    _DocsIf31CmtsCmUsOfdmaChannelNumPartialSvcIncidents_Type()
)
docsIf31CmtsCmUsOfdmaChannelNumPartialSvcIncidents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmUsOfdmaChannelNumPartialSvcIncidents.setStatus("current")
_DocsIf31CmtsCmUsOfdmaProfileStatusTable_Object = MibTable
docsIf31CmtsCmUsOfdmaProfileStatusTable = _DocsIf31CmtsCmUsOfdmaProfileStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 5)
)
if mibBuilder.loadTexts:
    docsIf31CmtsCmUsOfdmaProfileStatusTable.setStatus("current")
_DocsIf31CmtsCmUsOfdmaProfileStatusEntry_Object = MibTableRow
docsIf31CmtsCmUsOfdmaProfileStatusEntry = _DocsIf31CmtsCmUsOfdmaProfileStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 5, 1)
)
docsIf31CmtsCmUsOfdmaProfileStatusEntry.setIndexNames(
    (0, "DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusId"),
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaDataIucStatsDataIuc"),
)
if mibBuilder.loadTexts:
    docsIf31CmtsCmUsOfdmaProfileStatusEntry.setStatus("current")
_DocsIf31CmtsCmUsOfdmaProfileTotalCodewords_Type = Counter64
_DocsIf31CmtsCmUsOfdmaProfileTotalCodewords_Object = MibTableColumn
docsIf31CmtsCmUsOfdmaProfileTotalCodewords = _DocsIf31CmtsCmUsOfdmaProfileTotalCodewords_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 5, 1, 1),
    _DocsIf31CmtsCmUsOfdmaProfileTotalCodewords_Type()
)
docsIf31CmtsCmUsOfdmaProfileTotalCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmUsOfdmaProfileTotalCodewords.setStatus("current")
_DocsIf31CmtsCmUsOfdmaProfileCorrectedCodewords_Type = Counter64
_DocsIf31CmtsCmUsOfdmaProfileCorrectedCodewords_Object = MibTableColumn
docsIf31CmtsCmUsOfdmaProfileCorrectedCodewords = _DocsIf31CmtsCmUsOfdmaProfileCorrectedCodewords_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 5, 1, 2),
    _DocsIf31CmtsCmUsOfdmaProfileCorrectedCodewords_Type()
)
docsIf31CmtsCmUsOfdmaProfileCorrectedCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmUsOfdmaProfileCorrectedCodewords.setStatus("current")
_DocsIf31CmtsCmUsOfdmaProfileUnreliableCodewords_Type = Counter64
_DocsIf31CmtsCmUsOfdmaProfileUnreliableCodewords_Object = MibTableColumn
docsIf31CmtsCmUsOfdmaProfileUnreliableCodewords = _DocsIf31CmtsCmUsOfdmaProfileUnreliableCodewords_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 5, 1, 3),
    _DocsIf31CmtsCmUsOfdmaProfileUnreliableCodewords_Type()
)
docsIf31CmtsCmUsOfdmaProfileUnreliableCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmUsOfdmaProfileUnreliableCodewords.setStatus("current")
_DocsIf31CmtsCmDsOfdmChannelStatusTable_Object = MibTable
docsIf31CmtsCmDsOfdmChannelStatusTable = _DocsIf31CmtsCmDsOfdmChannelStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 6)
)
if mibBuilder.loadTexts:
    docsIf31CmtsCmDsOfdmChannelStatusTable.setStatus("current")
_DocsIf31CmtsCmDsOfdmChannelStatusEntry_Object = MibTableRow
docsIf31CmtsCmDsOfdmChannelStatusEntry = _DocsIf31CmtsCmDsOfdmChannelStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 6, 1)
)
docsIf31CmtsCmDsOfdmChannelStatusEntry.setIndexNames(
    (0, "DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIf31CmtsCmDsOfdmChannelStatusEntry.setStatus("current")
_DocsIf31CmtsCmDsOfdmChannelCurPartialSvcReasonCode_Type = PartialSvcReasonType
_DocsIf31CmtsCmDsOfdmChannelCurPartialSvcReasonCode_Object = MibTableColumn
docsIf31CmtsCmDsOfdmChannelCurPartialSvcReasonCode = _DocsIf31CmtsCmDsOfdmChannelCurPartialSvcReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 6, 1, 1),
    _DocsIf31CmtsCmDsOfdmChannelCurPartialSvcReasonCode_Type()
)
docsIf31CmtsCmDsOfdmChannelCurPartialSvcReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmDsOfdmChannelCurPartialSvcReasonCode.setStatus("current")
_DocsIf31CmtsCmDsOfdmChannelLastPartialSvcTime_Type = DateAndTime
_DocsIf31CmtsCmDsOfdmChannelLastPartialSvcTime_Object = MibTableColumn
docsIf31CmtsCmDsOfdmChannelLastPartialSvcTime = _DocsIf31CmtsCmDsOfdmChannelLastPartialSvcTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 6, 1, 2),
    _DocsIf31CmtsCmDsOfdmChannelLastPartialSvcTime_Type()
)
docsIf31CmtsCmDsOfdmChannelLastPartialSvcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmDsOfdmChannelLastPartialSvcTime.setStatus("current")
_DocsIf31CmtsCmDsOfdmChannelLastPartialSvcReasonCode_Type = PartialSvcReasonType
_DocsIf31CmtsCmDsOfdmChannelLastPartialSvcReasonCode_Object = MibTableColumn
docsIf31CmtsCmDsOfdmChannelLastPartialSvcReasonCode = _DocsIf31CmtsCmDsOfdmChannelLastPartialSvcReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 6, 1, 3),
    _DocsIf31CmtsCmDsOfdmChannelLastPartialSvcReasonCode_Type()
)
docsIf31CmtsCmDsOfdmChannelLastPartialSvcReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmDsOfdmChannelLastPartialSvcReasonCode.setStatus("current")
_DocsIf31CmtsCmDsOfdmChannelNumPartialSvcIncidents_Type = Counter32
_DocsIf31CmtsCmDsOfdmChannelNumPartialSvcIncidents_Object = MibTableColumn
docsIf31CmtsCmDsOfdmChannelNumPartialSvcIncidents = _DocsIf31CmtsCmDsOfdmChannelNumPartialSvcIncidents_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 6, 1, 4),
    _DocsIf31CmtsCmDsOfdmChannelNumPartialSvcIncidents_Type()
)
docsIf31CmtsCmDsOfdmChannelNumPartialSvcIncidents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmDsOfdmChannelNumPartialSvcIncidents.setStatus("current")
_DocsIf31CmtsCmDsOfdmChannelNumPartialChanIncidents_Type = Counter32
_DocsIf31CmtsCmDsOfdmChannelNumPartialChanIncidents_Object = MibTableColumn
docsIf31CmtsCmDsOfdmChannelNumPartialChanIncidents = _DocsIf31CmtsCmDsOfdmChannelNumPartialChanIncidents_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 6, 1, 5),
    _DocsIf31CmtsCmDsOfdmChannelNumPartialChanIncidents_Type()
)
docsIf31CmtsCmDsOfdmChannelNumPartialChanIncidents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmDsOfdmChannelNumPartialChanIncidents.setStatus("current")
_DocsIf31CmtsCmDsOfdmProfileStatusTable_Object = MibTable
docsIf31CmtsCmDsOfdmProfileStatusTable = _DocsIf31CmtsCmDsOfdmProfileStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 7)
)
if mibBuilder.loadTexts:
    docsIf31CmtsCmDsOfdmProfileStatusTable.setStatus("current")
_DocsIf31CmtsCmDsOfdmProfileStatusEntry_Object = MibTableRow
docsIf31CmtsCmDsOfdmProfileStatusEntry = _DocsIf31CmtsCmDsOfdmProfileStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 7, 1)
)
docsIf31CmtsCmDsOfdmProfileStatusEntry.setIndexNames(
    (0, "DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusId"),
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF31-MIB", "docsIf31CmtsDsOfdmProfileStatsProfileId"),
)
if mibBuilder.loadTexts:
    docsIf31CmtsCmDsOfdmProfileStatusEntry.setStatus("current")
_DocsIf31CmtsCmDsOfdmProfilePartialChanReasonCode_Type = PartialChanReasonType
_DocsIf31CmtsCmDsOfdmProfilePartialChanReasonCode_Object = MibTableColumn
docsIf31CmtsCmDsOfdmProfilePartialChanReasonCode = _DocsIf31CmtsCmDsOfdmProfilePartialChanReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 7, 1, 1),
    _DocsIf31CmtsCmDsOfdmProfilePartialChanReasonCode_Type()
)
docsIf31CmtsCmDsOfdmProfilePartialChanReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmDsOfdmProfilePartialChanReasonCode.setStatus("current")
_DocsIf31CmtsCmDsOfdmProfileLastPartialChanTime_Type = DateAndTime
_DocsIf31CmtsCmDsOfdmProfileLastPartialChanTime_Object = MibTableColumn
docsIf31CmtsCmDsOfdmProfileLastPartialChanTime = _DocsIf31CmtsCmDsOfdmProfileLastPartialChanTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 7, 1, 2),
    _DocsIf31CmtsCmDsOfdmProfileLastPartialChanTime_Type()
)
docsIf31CmtsCmDsOfdmProfileLastPartialChanTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmDsOfdmProfileLastPartialChanTime.setStatus("current")
_DocsIf31CmtsCmDsOfdmProfileLastPartialChanReasonCode_Type = PartialChanReasonType
_DocsIf31CmtsCmDsOfdmProfileLastPartialChanReasonCode_Object = MibTableColumn
docsIf31CmtsCmDsOfdmProfileLastPartialChanReasonCode = _DocsIf31CmtsCmDsOfdmProfileLastPartialChanReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 7, 1, 3),
    _DocsIf31CmtsCmDsOfdmProfileLastPartialChanReasonCode_Type()
)
docsIf31CmtsCmDsOfdmProfileLastPartialChanReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmDsOfdmProfileLastPartialChanReasonCode.setStatus("current")
_DocsIf31CmtsCmEmStatsTable_Object = MibTable
docsIf31CmtsCmEmStatsTable = _DocsIf31CmtsCmEmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 8)
)
if mibBuilder.loadTexts:
    docsIf31CmtsCmEmStatsTable.setStatus("current")
_DocsIf31CmtsCmEmStatsEntry_Object = MibTableRow
docsIf31CmtsCmEmStatsEntry = _DocsIf31CmtsCmEmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 8, 1)
)
docsIf31CmtsCmEmStatsEntry.setIndexNames(
    (0, "DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusId"),
)
if mibBuilder.loadTexts:
    docsIf31CmtsCmEmStatsEntry.setStatus("current")
_DocsIf31CmtsCmEmStatsEm1x1ModeTotalDuration_Type = Unsigned32
_DocsIf31CmtsCmEmStatsEm1x1ModeTotalDuration_Object = MibTableColumn
docsIf31CmtsCmEmStatsEm1x1ModeTotalDuration = _DocsIf31CmtsCmEmStatsEm1x1ModeTotalDuration_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 8, 1, 1),
    _DocsIf31CmtsCmEmStatsEm1x1ModeTotalDuration_Type()
)
docsIf31CmtsCmEmStatsEm1x1ModeTotalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmEmStatsEm1x1ModeTotalDuration.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsCmEmStatsEm1x1ModeTotalDuration.setUnits("seconds")
_DocsIf31CmtsCmEmStatsDlsModeTotalDuration_Type = Unsigned32
_DocsIf31CmtsCmEmStatsDlsModeTotalDuration_Object = MibTableColumn
docsIf31CmtsCmEmStatsDlsModeTotalDuration = _DocsIf31CmtsCmEmStatsDlsModeTotalDuration_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 8, 1, 2),
    _DocsIf31CmtsCmEmStatsDlsModeTotalDuration_Type()
)
docsIf31CmtsCmEmStatsDlsModeTotalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmEmStatsDlsModeTotalDuration.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsCmEmStatsDlsModeTotalDuration.setUnits("seconds")
_DocsIf31CmtsCmEmStatsLastDlsTime_Type = DateAndTime
_DocsIf31CmtsCmEmStatsLastDlsTime_Object = MibTableColumn
docsIf31CmtsCmEmStatsLastDlsTime = _DocsIf31CmtsCmEmStatsLastDlsTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 8, 1, 3),
    _DocsIf31CmtsCmEmStatsLastDlsTime_Type()
)
docsIf31CmtsCmEmStatsLastDlsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmEmStatsLastDlsTime.setStatus("current")
_DocsIf31CmtsCmEmStatsDlsWakeupEvents_Type = Counter32
_DocsIf31CmtsCmEmStatsDlsWakeupEvents_Object = MibTableColumn
docsIf31CmtsCmEmStatsDlsWakeupEvents = _DocsIf31CmtsCmEmStatsDlsWakeupEvents_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 8, 1, 4),
    _DocsIf31CmtsCmEmStatsDlsWakeupEvents_Type()
)
docsIf31CmtsCmEmStatsDlsWakeupEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsCmEmStatsDlsWakeupEvents.setStatus("current")
_DocsIf31CmDsOfdmChanTable_Object = MibTable
docsIf31CmDsOfdmChanTable = _DocsIf31CmDsOfdmChanTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 9)
)
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChanTable.setStatus("current")
_DocsIf31CmDsOfdmChanEntry_Object = MibTableRow
docsIf31CmDsOfdmChanEntry = _DocsIf31CmDsOfdmChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 9, 1)
)
docsIf31CmDsOfdmChanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChanEntry.setStatus("current")


class _DocsIf31CmDsOfdmChanChannelId_Type(Integer32):
    """Custom type docsIf31CmDsOfdmChanChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsIf31CmDsOfdmChanChannelId_Type.__name__ = "Integer32"
_DocsIf31CmDsOfdmChanChannelId_Object = MibTableColumn
docsIf31CmDsOfdmChanChannelId = _DocsIf31CmDsOfdmChanChannelId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 9, 1, 1),
    _DocsIf31CmDsOfdmChanChannelId_Type()
)
docsIf31CmDsOfdmChanChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChanChannelId.setStatus("current")
_DocsIf31CmDsOfdmChanChanIndicator_Type = PrimaryDsIndicatorType
_DocsIf31CmDsOfdmChanChanIndicator_Object = MibTableColumn
docsIf31CmDsOfdmChanChanIndicator = _DocsIf31CmDsOfdmChanChanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 9, 1, 2),
    _DocsIf31CmDsOfdmChanChanIndicator_Type()
)
docsIf31CmDsOfdmChanChanIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChanChanIndicator.setStatus("current")
_DocsIf31CmDsOfdmChanSubcarrierZeroFreq_Type = Unsigned32
_DocsIf31CmDsOfdmChanSubcarrierZeroFreq_Object = MibTableColumn
docsIf31CmDsOfdmChanSubcarrierZeroFreq = _DocsIf31CmDsOfdmChanSubcarrierZeroFreq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 9, 1, 3),
    _DocsIf31CmDsOfdmChanSubcarrierZeroFreq_Type()
)
docsIf31CmDsOfdmChanSubcarrierZeroFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChanSubcarrierZeroFreq.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChanSubcarrierZeroFreq.setUnits("Hz")
_DocsIf31CmDsOfdmChanFirstActiveSubcarrierNum_Type = Unsigned32
_DocsIf31CmDsOfdmChanFirstActiveSubcarrierNum_Object = MibTableColumn
docsIf31CmDsOfdmChanFirstActiveSubcarrierNum = _DocsIf31CmDsOfdmChanFirstActiveSubcarrierNum_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 9, 1, 4),
    _DocsIf31CmDsOfdmChanFirstActiveSubcarrierNum_Type()
)
docsIf31CmDsOfdmChanFirstActiveSubcarrierNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChanFirstActiveSubcarrierNum.setStatus("current")
_DocsIf31CmDsOfdmChanLastActiveSubcarrierNum_Type = Unsigned32
_DocsIf31CmDsOfdmChanLastActiveSubcarrierNum_Object = MibTableColumn
docsIf31CmDsOfdmChanLastActiveSubcarrierNum = _DocsIf31CmDsOfdmChanLastActiveSubcarrierNum_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 9, 1, 5),
    _DocsIf31CmDsOfdmChanLastActiveSubcarrierNum_Type()
)
docsIf31CmDsOfdmChanLastActiveSubcarrierNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChanLastActiveSubcarrierNum.setStatus("current")
_DocsIf31CmDsOfdmChanNumActiveSubcarriers_Type = Unsigned32
_DocsIf31CmDsOfdmChanNumActiveSubcarriers_Object = MibTableColumn
docsIf31CmDsOfdmChanNumActiveSubcarriers = _DocsIf31CmDsOfdmChanNumActiveSubcarriers_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 9, 1, 6),
    _DocsIf31CmDsOfdmChanNumActiveSubcarriers_Type()
)
docsIf31CmDsOfdmChanNumActiveSubcarriers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChanNumActiveSubcarriers.setStatus("current")
_DocsIf31CmDsOfdmChanSubcarrierSpacing_Type = SubcarrierSpacingType
_DocsIf31CmDsOfdmChanSubcarrierSpacing_Object = MibTableColumn
docsIf31CmDsOfdmChanSubcarrierSpacing = _DocsIf31CmDsOfdmChanSubcarrierSpacing_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 9, 1, 7),
    _DocsIf31CmDsOfdmChanSubcarrierSpacing_Type()
)
docsIf31CmDsOfdmChanSubcarrierSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChanSubcarrierSpacing.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChanSubcarrierSpacing.setUnits("kHz")
_DocsIf31CmDsOfdmChanCyclicPrefix_Type = DsOfdmCyclicPrefix
_DocsIf31CmDsOfdmChanCyclicPrefix_Object = MibTableColumn
docsIf31CmDsOfdmChanCyclicPrefix = _DocsIf31CmDsOfdmChanCyclicPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 9, 1, 8),
    _DocsIf31CmDsOfdmChanCyclicPrefix_Type()
)
docsIf31CmDsOfdmChanCyclicPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChanCyclicPrefix.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChanCyclicPrefix.setUnits("number of samples")
_DocsIf31CmDsOfdmChanRollOffPeriod_Type = DsOfdmRollOffPeriod
_DocsIf31CmDsOfdmChanRollOffPeriod_Object = MibTableColumn
docsIf31CmDsOfdmChanRollOffPeriod = _DocsIf31CmDsOfdmChanRollOffPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 9, 1, 9),
    _DocsIf31CmDsOfdmChanRollOffPeriod_Type()
)
docsIf31CmDsOfdmChanRollOffPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChanRollOffPeriod.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChanRollOffPeriod.setUnits("number of samples")
_DocsIf31CmDsOfdmChanPlcFreq_Type = Unsigned32
_DocsIf31CmDsOfdmChanPlcFreq_Object = MibTableColumn
docsIf31CmDsOfdmChanPlcFreq = _DocsIf31CmDsOfdmChanPlcFreq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 9, 1, 10),
    _DocsIf31CmDsOfdmChanPlcFreq_Type()
)
docsIf31CmDsOfdmChanPlcFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChanPlcFreq.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChanPlcFreq.setUnits("Hz")
_DocsIf31CmDsOfdmChanNumPilots_Type = Unsigned32
_DocsIf31CmDsOfdmChanNumPilots_Object = MibTableColumn
docsIf31CmDsOfdmChanNumPilots = _DocsIf31CmDsOfdmChanNumPilots_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 9, 1, 11),
    _DocsIf31CmDsOfdmChanNumPilots_Type()
)
docsIf31CmDsOfdmChanNumPilots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChanNumPilots.setStatus("current")
_DocsIf31CmDsOfdmChanTimeInterleaverDepth_Type = TimeInterleaverDepth
_DocsIf31CmDsOfdmChanTimeInterleaverDepth_Object = MibTableColumn
docsIf31CmDsOfdmChanTimeInterleaverDepth = _DocsIf31CmDsOfdmChanTimeInterleaverDepth_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 9, 1, 12),
    _DocsIf31CmDsOfdmChanTimeInterleaverDepth_Type()
)
docsIf31CmDsOfdmChanTimeInterleaverDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChanTimeInterleaverDepth.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChanTimeInterleaverDepth.setUnits("symbols")
_DocsIf31CmDsOfdmChanPlcTotalCodewords_Type = Counter64
_DocsIf31CmDsOfdmChanPlcTotalCodewords_Object = MibTableColumn
docsIf31CmDsOfdmChanPlcTotalCodewords = _DocsIf31CmDsOfdmChanPlcTotalCodewords_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 9, 1, 13),
    _DocsIf31CmDsOfdmChanPlcTotalCodewords_Type()
)
docsIf31CmDsOfdmChanPlcTotalCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChanPlcTotalCodewords.setStatus("current")
_DocsIf31CmDsOfdmChanPlcUnreliableCodewords_Type = Counter64
_DocsIf31CmDsOfdmChanPlcUnreliableCodewords_Object = MibTableColumn
docsIf31CmDsOfdmChanPlcUnreliableCodewords = _DocsIf31CmDsOfdmChanPlcUnreliableCodewords_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 9, 1, 14),
    _DocsIf31CmDsOfdmChanPlcUnreliableCodewords_Type()
)
docsIf31CmDsOfdmChanPlcUnreliableCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChanPlcUnreliableCodewords.setStatus("current")
_DocsIf31CmDsOfdmChanNcpTotalFields_Type = Counter64
_DocsIf31CmDsOfdmChanNcpTotalFields_Object = MibTableColumn
docsIf31CmDsOfdmChanNcpTotalFields = _DocsIf31CmDsOfdmChanNcpTotalFields_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 9, 1, 15),
    _DocsIf31CmDsOfdmChanNcpTotalFields_Type()
)
docsIf31CmDsOfdmChanNcpTotalFields.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChanNcpTotalFields.setStatus("current")
_DocsIf31CmDsOfdmChanNcpFieldCrcFailures_Type = Counter64
_DocsIf31CmDsOfdmChanNcpFieldCrcFailures_Object = MibTableColumn
docsIf31CmDsOfdmChanNcpFieldCrcFailures = _DocsIf31CmDsOfdmChanNcpFieldCrcFailures_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 9, 1, 16),
    _DocsIf31CmDsOfdmChanNcpFieldCrcFailures_Type()
)
docsIf31CmDsOfdmChanNcpFieldCrcFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChanNcpFieldCrcFailures.setStatus("current")
_DocsIf31CmDsOfdmProfileStatsTable_Object = MibTable
docsIf31CmDsOfdmProfileStatsTable = _DocsIf31CmDsOfdmProfileStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 10)
)
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmProfileStatsTable.setStatus("current")
_DocsIf31CmDsOfdmProfileStatsEntry_Object = MibTableRow
docsIf31CmDsOfdmProfileStatsEntry = _DocsIf31CmDsOfdmProfileStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 10, 1)
)
docsIf31CmDsOfdmProfileStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF31-MIB", "docsIf31CmDsOfdmProfileStatsProfileId"),
)
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmProfileStatsEntry.setStatus("current")


class _DocsIf31CmDsOfdmProfileStatsProfileId_Type(Unsigned32):
    """Custom type docsIf31CmDsOfdmProfileStatsProfileId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsIf31CmDsOfdmProfileStatsProfileId_Type.__name__ = "Unsigned32"
_DocsIf31CmDsOfdmProfileStatsProfileId_Object = MibTableColumn
docsIf31CmDsOfdmProfileStatsProfileId = _DocsIf31CmDsOfdmProfileStatsProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 10, 1, 1),
    _DocsIf31CmDsOfdmProfileStatsProfileId_Type()
)
docsIf31CmDsOfdmProfileStatsProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmProfileStatsProfileId.setStatus("current")


class _DocsIf31CmDsOfdmProfileStatsConfigChangeCt_Type(Unsigned32):
    """Custom type docsIf31CmDsOfdmProfileStatsConfigChangeCt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsIf31CmDsOfdmProfileStatsConfigChangeCt_Type.__name__ = "Unsigned32"
_DocsIf31CmDsOfdmProfileStatsConfigChangeCt_Object = MibTableColumn
docsIf31CmDsOfdmProfileStatsConfigChangeCt = _DocsIf31CmDsOfdmProfileStatsConfigChangeCt_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 10, 1, 2),
    _DocsIf31CmDsOfdmProfileStatsConfigChangeCt_Type()
)
docsIf31CmDsOfdmProfileStatsConfigChangeCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmProfileStatsConfigChangeCt.setStatus("current")
_DocsIf31CmDsOfdmProfileStatsTotalCodewords_Type = Counter64
_DocsIf31CmDsOfdmProfileStatsTotalCodewords_Object = MibTableColumn
docsIf31CmDsOfdmProfileStatsTotalCodewords = _DocsIf31CmDsOfdmProfileStatsTotalCodewords_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 10, 1, 3),
    _DocsIf31CmDsOfdmProfileStatsTotalCodewords_Type()
)
docsIf31CmDsOfdmProfileStatsTotalCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmProfileStatsTotalCodewords.setStatus("current")
_DocsIf31CmDsOfdmProfileStatsCorrectedCodewords_Type = Counter64
_DocsIf31CmDsOfdmProfileStatsCorrectedCodewords_Object = MibTableColumn
docsIf31CmDsOfdmProfileStatsCorrectedCodewords = _DocsIf31CmDsOfdmProfileStatsCorrectedCodewords_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 10, 1, 4),
    _DocsIf31CmDsOfdmProfileStatsCorrectedCodewords_Type()
)
docsIf31CmDsOfdmProfileStatsCorrectedCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmProfileStatsCorrectedCodewords.setStatus("current")
_DocsIf31CmDsOfdmProfileStatsUncorrectableCodewords_Type = Counter64
_DocsIf31CmDsOfdmProfileStatsUncorrectableCodewords_Object = MibTableColumn
docsIf31CmDsOfdmProfileStatsUncorrectableCodewords = _DocsIf31CmDsOfdmProfileStatsUncorrectableCodewords_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 10, 1, 5),
    _DocsIf31CmDsOfdmProfileStatsUncorrectableCodewords_Type()
)
docsIf31CmDsOfdmProfileStatsUncorrectableCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmProfileStatsUncorrectableCodewords.setStatus("current")
_DocsIf31CmDsOfdmProfileStatsInOctets_Type = Counter64
_DocsIf31CmDsOfdmProfileStatsInOctets_Object = MibTableColumn
docsIf31CmDsOfdmProfileStatsInOctets = _DocsIf31CmDsOfdmProfileStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 10, 1, 6),
    _DocsIf31CmDsOfdmProfileStatsInOctets_Type()
)
docsIf31CmDsOfdmProfileStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmProfileStatsInOctets.setStatus("current")
_DocsIf31CmDsOfdmProfileStatsInUnicastOctets_Type = Counter64
_DocsIf31CmDsOfdmProfileStatsInUnicastOctets_Object = MibTableColumn
docsIf31CmDsOfdmProfileStatsInUnicastOctets = _DocsIf31CmDsOfdmProfileStatsInUnicastOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 10, 1, 7),
    _DocsIf31CmDsOfdmProfileStatsInUnicastOctets_Type()
)
docsIf31CmDsOfdmProfileStatsInUnicastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmProfileStatsInUnicastOctets.setStatus("current")
_DocsIf31CmDsOfdmProfileStatsInMulticastOctets_Type = Counter64
_DocsIf31CmDsOfdmProfileStatsInMulticastOctets_Object = MibTableColumn
docsIf31CmDsOfdmProfileStatsInMulticastOctets = _DocsIf31CmDsOfdmProfileStatsInMulticastOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 10, 1, 8),
    _DocsIf31CmDsOfdmProfileStatsInMulticastOctets_Type()
)
docsIf31CmDsOfdmProfileStatsInMulticastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmProfileStatsInMulticastOctets.setStatus("current")
_DocsIf31CmDsOfdmProfileStatsInFrames_Type = Counter64
_DocsIf31CmDsOfdmProfileStatsInFrames_Object = MibTableColumn
docsIf31CmDsOfdmProfileStatsInFrames = _DocsIf31CmDsOfdmProfileStatsInFrames_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 10, 1, 9),
    _DocsIf31CmDsOfdmProfileStatsInFrames_Type()
)
docsIf31CmDsOfdmProfileStatsInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmProfileStatsInFrames.setStatus("current")
_DocsIf31CmDsOfdmProfileStatsInUnicastFrames_Type = Counter64
_DocsIf31CmDsOfdmProfileStatsInUnicastFrames_Object = MibTableColumn
docsIf31CmDsOfdmProfileStatsInUnicastFrames = _DocsIf31CmDsOfdmProfileStatsInUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 10, 1, 10),
    _DocsIf31CmDsOfdmProfileStatsInUnicastFrames_Type()
)
docsIf31CmDsOfdmProfileStatsInUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmProfileStatsInUnicastFrames.setStatus("current")
_DocsIf31CmDsOfdmProfileStatsInMulticastFrames_Type = Counter64
_DocsIf31CmDsOfdmProfileStatsInMulticastFrames_Object = MibTableColumn
docsIf31CmDsOfdmProfileStatsInMulticastFrames = _DocsIf31CmDsOfdmProfileStatsInMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 10, 1, 11),
    _DocsIf31CmDsOfdmProfileStatsInMulticastFrames_Type()
)
docsIf31CmDsOfdmProfileStatsInMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmProfileStatsInMulticastFrames.setStatus("current")
_DocsIf31CmDsOfdmProfileStatsInFrameCrcFailures_Type = Counter64
_DocsIf31CmDsOfdmProfileStatsInFrameCrcFailures_Object = MibTableColumn
docsIf31CmDsOfdmProfileStatsInFrameCrcFailures = _DocsIf31CmDsOfdmProfileStatsInFrameCrcFailures_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 10, 1, 12),
    _DocsIf31CmDsOfdmProfileStatsInFrameCrcFailures_Type()
)
docsIf31CmDsOfdmProfileStatsInFrameCrcFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmProfileStatsInFrameCrcFailures.setStatus("current")
_DocsIf31CmDsOfdmProfileStatsCtrDiscontinuityTime_Type = TimeStamp
_DocsIf31CmDsOfdmProfileStatsCtrDiscontinuityTime_Object = MibTableColumn
docsIf31CmDsOfdmProfileStatsCtrDiscontinuityTime = _DocsIf31CmDsOfdmProfileStatsCtrDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 10, 1, 13),
    _DocsIf31CmDsOfdmProfileStatsCtrDiscontinuityTime_Type()
)
docsIf31CmDsOfdmProfileStatsCtrDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmProfileStatsCtrDiscontinuityTime.setStatus("current")
_DocsIf31CmDsOfdmChannelPowerTable_Object = MibTable
docsIf31CmDsOfdmChannelPowerTable = _DocsIf31CmDsOfdmChannelPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 11)
)
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChannelPowerTable.setStatus("current")
_DocsIf31CmDsOfdmChannelPowerEntry_Object = MibTableRow
docsIf31CmDsOfdmChannelPowerEntry = _DocsIf31CmDsOfdmChannelPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 11, 1)
)
docsIf31CmDsOfdmChannelPowerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF31-MIB", "docsIf31CmDsOfdmChannelBandIndex"),
)
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChannelPowerEntry.setStatus("current")
_DocsIf31CmDsOfdmChannelBandIndex_Type = Unsigned32
_DocsIf31CmDsOfdmChannelBandIndex_Object = MibTableColumn
docsIf31CmDsOfdmChannelBandIndex = _DocsIf31CmDsOfdmChannelBandIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 11, 1, 1),
    _DocsIf31CmDsOfdmChannelBandIndex_Type()
)
docsIf31CmDsOfdmChannelBandIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChannelBandIndex.setStatus("current")
_DocsIf31CmDsOfdmChannelPowerCenterFrequency_Type = Unsigned32
_DocsIf31CmDsOfdmChannelPowerCenterFrequency_Object = MibTableColumn
docsIf31CmDsOfdmChannelPowerCenterFrequency = _DocsIf31CmDsOfdmChannelPowerCenterFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 11, 1, 2),
    _DocsIf31CmDsOfdmChannelPowerCenterFrequency_Type()
)
docsIf31CmDsOfdmChannelPowerCenterFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChannelPowerCenterFrequency.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChannelPowerCenterFrequency.setUnits("Hz")
_DocsIf31CmDsOfdmChannelPowerRxPower_Type = TenthdBmV
_DocsIf31CmDsOfdmChannelPowerRxPower_Object = MibTableColumn
docsIf31CmDsOfdmChannelPowerRxPower = _DocsIf31CmDsOfdmChannelPowerRxPower_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 11, 1, 3),
    _DocsIf31CmDsOfdmChannelPowerRxPower_Type()
)
docsIf31CmDsOfdmChannelPowerRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChannelPowerRxPower.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmDsOfdmChannelPowerRxPower.setUnits("TenthdBmV")
_DocsIf31CmStatusOfdmaUsTable_Object = MibTable
docsIf31CmStatusOfdmaUsTable = _DocsIf31CmStatusOfdmaUsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 12)
)
if mibBuilder.loadTexts:
    docsIf31CmStatusOfdmaUsTable.setStatus("current")
_DocsIf31CmStatusOfdmaUsEntry_Object = MibTableRow
docsIf31CmStatusOfdmaUsEntry = _DocsIf31CmStatusOfdmaUsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 12, 1)
)
docsIf31CmStatusOfdmaUsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIf31CmStatusOfdmaUsEntry.setStatus("current")
_DocsIf31CmStatusOfdmaUsT3Timeouts_Type = Counter32
_DocsIf31CmStatusOfdmaUsT3Timeouts_Object = MibTableColumn
docsIf31CmStatusOfdmaUsT3Timeouts = _DocsIf31CmStatusOfdmaUsT3Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 12, 1, 2),
    _DocsIf31CmStatusOfdmaUsT3Timeouts_Type()
)
docsIf31CmStatusOfdmaUsT3Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmStatusOfdmaUsT3Timeouts.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmStatusOfdmaUsT3Timeouts.setUnits("timeouts")
_DocsIf31CmStatusOfdmaUsT4Timeouts_Type = Counter32
_DocsIf31CmStatusOfdmaUsT4Timeouts_Object = MibTableColumn
docsIf31CmStatusOfdmaUsT4Timeouts = _DocsIf31CmStatusOfdmaUsT4Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 12, 1, 3),
    _DocsIf31CmStatusOfdmaUsT4Timeouts_Type()
)
docsIf31CmStatusOfdmaUsT4Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmStatusOfdmaUsT4Timeouts.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmStatusOfdmaUsT4Timeouts.setUnits("timeouts")
_DocsIf31CmStatusOfdmaUsRangingAborteds_Type = Counter32
_DocsIf31CmStatusOfdmaUsRangingAborteds_Object = MibTableColumn
docsIf31CmStatusOfdmaUsRangingAborteds = _DocsIf31CmStatusOfdmaUsRangingAborteds_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 12, 1, 4),
    _DocsIf31CmStatusOfdmaUsRangingAborteds_Type()
)
docsIf31CmStatusOfdmaUsRangingAborteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmStatusOfdmaUsRangingAborteds.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmStatusOfdmaUsRangingAborteds.setUnits("attempts")
_DocsIf31CmStatusOfdmaUsT3Exceededs_Type = Counter32
_DocsIf31CmStatusOfdmaUsT3Exceededs_Object = MibTableColumn
docsIf31CmStatusOfdmaUsT3Exceededs = _DocsIf31CmStatusOfdmaUsT3Exceededs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 12, 1, 5),
    _DocsIf31CmStatusOfdmaUsT3Exceededs_Type()
)
docsIf31CmStatusOfdmaUsT3Exceededs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmStatusOfdmaUsT3Exceededs.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmStatusOfdmaUsT3Exceededs.setUnits("timeouts")
_DocsIf31CmStatusOfdmaUsIsMuted_Type = TruthValue
_DocsIf31CmStatusOfdmaUsIsMuted_Object = MibTableColumn
docsIf31CmStatusOfdmaUsIsMuted = _DocsIf31CmStatusOfdmaUsIsMuted_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 12, 1, 6),
    _DocsIf31CmStatusOfdmaUsIsMuted_Type()
)
docsIf31CmStatusOfdmaUsIsMuted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmStatusOfdmaUsIsMuted.setStatus("current")
_DocsIf31CmStatusOfdmaUsRangingStatus_Type = RangingState
_DocsIf31CmStatusOfdmaUsRangingStatus_Object = MibTableColumn
docsIf31CmStatusOfdmaUsRangingStatus = _DocsIf31CmStatusOfdmaUsRangingStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 12, 1, 7),
    _DocsIf31CmStatusOfdmaUsRangingStatus_Type()
)
docsIf31CmStatusOfdmaUsRangingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmStatusOfdmaUsRangingStatus.setStatus("current")
_DocsIf31CmUsOfdmaChanTable_Object = MibTable
docsIf31CmUsOfdmaChanTable = _DocsIf31CmUsOfdmaChanTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 13)
)
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaChanTable.setStatus("current")
_DocsIf31CmUsOfdmaChanEntry_Object = MibTableRow
docsIf31CmUsOfdmaChanEntry = _DocsIf31CmUsOfdmaChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 13, 1)
)
docsIf31CmUsOfdmaChanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaChanEntry.setStatus("current")


class _DocsIf31CmUsOfdmaChanConfigChangeCt_Type(Unsigned32):
    """Custom type docsIf31CmUsOfdmaChanConfigChangeCt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsIf31CmUsOfdmaChanConfigChangeCt_Type.__name__ = "Unsigned32"
_DocsIf31CmUsOfdmaChanConfigChangeCt_Object = MibTableColumn
docsIf31CmUsOfdmaChanConfigChangeCt = _DocsIf31CmUsOfdmaChanConfigChangeCt_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 13, 1, 1),
    _DocsIf31CmUsOfdmaChanConfigChangeCt_Type()
)
docsIf31CmUsOfdmaChanConfigChangeCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaChanConfigChangeCt.setStatus("current")
_DocsIf31CmUsOfdmaChanSubcarrierZeroFreq_Type = Unsigned32
_DocsIf31CmUsOfdmaChanSubcarrierZeroFreq_Object = MibTableColumn
docsIf31CmUsOfdmaChanSubcarrierZeroFreq = _DocsIf31CmUsOfdmaChanSubcarrierZeroFreq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 13, 1, 2),
    _DocsIf31CmUsOfdmaChanSubcarrierZeroFreq_Type()
)
docsIf31CmUsOfdmaChanSubcarrierZeroFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaChanSubcarrierZeroFreq.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaChanSubcarrierZeroFreq.setUnits("Hz")
_DocsIf31CmUsOfdmaChanFirstActiveSubcarrierNum_Type = Unsigned32
_DocsIf31CmUsOfdmaChanFirstActiveSubcarrierNum_Object = MibTableColumn
docsIf31CmUsOfdmaChanFirstActiveSubcarrierNum = _DocsIf31CmUsOfdmaChanFirstActiveSubcarrierNum_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 13, 1, 3),
    _DocsIf31CmUsOfdmaChanFirstActiveSubcarrierNum_Type()
)
docsIf31CmUsOfdmaChanFirstActiveSubcarrierNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaChanFirstActiveSubcarrierNum.setStatus("current")
_DocsIf31CmUsOfdmaChanLastActiveSubcarrierNum_Type = Unsigned32
_DocsIf31CmUsOfdmaChanLastActiveSubcarrierNum_Object = MibTableColumn
docsIf31CmUsOfdmaChanLastActiveSubcarrierNum = _DocsIf31CmUsOfdmaChanLastActiveSubcarrierNum_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 13, 1, 4),
    _DocsIf31CmUsOfdmaChanLastActiveSubcarrierNum_Type()
)
docsIf31CmUsOfdmaChanLastActiveSubcarrierNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaChanLastActiveSubcarrierNum.setStatus("current")
_DocsIf31CmUsOfdmaChanNumActiveSubcarriers_Type = Unsigned32
_DocsIf31CmUsOfdmaChanNumActiveSubcarriers_Object = MibTableColumn
docsIf31CmUsOfdmaChanNumActiveSubcarriers = _DocsIf31CmUsOfdmaChanNumActiveSubcarriers_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 13, 1, 5),
    _DocsIf31CmUsOfdmaChanNumActiveSubcarriers_Type()
)
docsIf31CmUsOfdmaChanNumActiveSubcarriers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaChanNumActiveSubcarriers.setStatus("current")
_DocsIf31CmUsOfdmaChanSubcarrierSpacing_Type = SubcarrierSpacingType
_DocsIf31CmUsOfdmaChanSubcarrierSpacing_Object = MibTableColumn
docsIf31CmUsOfdmaChanSubcarrierSpacing = _DocsIf31CmUsOfdmaChanSubcarrierSpacing_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 13, 1, 6),
    _DocsIf31CmUsOfdmaChanSubcarrierSpacing_Type()
)
docsIf31CmUsOfdmaChanSubcarrierSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaChanSubcarrierSpacing.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaChanSubcarrierSpacing.setUnits("kHz")
_DocsIf31CmUsOfdmaChanCyclicPrefix_Type = UsOfdmaCyclicPrefix
_DocsIf31CmUsOfdmaChanCyclicPrefix_Object = MibTableColumn
docsIf31CmUsOfdmaChanCyclicPrefix = _DocsIf31CmUsOfdmaChanCyclicPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 13, 1, 7),
    _DocsIf31CmUsOfdmaChanCyclicPrefix_Type()
)
docsIf31CmUsOfdmaChanCyclicPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaChanCyclicPrefix.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaChanCyclicPrefix.setUnits("number of samples")
_DocsIf31CmUsOfdmaChanRollOffPeriod_Type = UsOfdmaRollOffPeriod
_DocsIf31CmUsOfdmaChanRollOffPeriod_Object = MibTableColumn
docsIf31CmUsOfdmaChanRollOffPeriod = _DocsIf31CmUsOfdmaChanRollOffPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 13, 1, 8),
    _DocsIf31CmUsOfdmaChanRollOffPeriod_Type()
)
docsIf31CmUsOfdmaChanRollOffPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaChanRollOffPeriod.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaChanRollOffPeriod.setUnits("number of samples")
_DocsIf31CmUsOfdmaChanNumSymbolsPerFrame_Type = Unsigned32
_DocsIf31CmUsOfdmaChanNumSymbolsPerFrame_Object = MibTableColumn
docsIf31CmUsOfdmaChanNumSymbolsPerFrame = _DocsIf31CmUsOfdmaChanNumSymbolsPerFrame_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 13, 1, 9),
    _DocsIf31CmUsOfdmaChanNumSymbolsPerFrame_Type()
)
docsIf31CmUsOfdmaChanNumSymbolsPerFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaChanNumSymbolsPerFrame.setStatus("current")
_DocsIf31CmUsOfdmaChanTxPower_Type = Unsigned32
_DocsIf31CmUsOfdmaChanTxPower_Object = MibTableColumn
docsIf31CmUsOfdmaChanTxPower = _DocsIf31CmUsOfdmaChanTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 13, 1, 10),
    _DocsIf31CmUsOfdmaChanTxPower_Type()
)
docsIf31CmUsOfdmaChanTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaChanTxPower.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaChanTxPower.setUnits("QuarterdBmV")
_DocsIf31CmUsOfdmaChanPreEqEnabled_Type = TruthValue
_DocsIf31CmUsOfdmaChanPreEqEnabled_Object = MibTableColumn
docsIf31CmUsOfdmaChanPreEqEnabled = _DocsIf31CmUsOfdmaChanPreEqEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 13, 1, 11),
    _DocsIf31CmUsOfdmaChanPreEqEnabled_Type()
)
docsIf31CmUsOfdmaChanPreEqEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaChanPreEqEnabled.setStatus("current")


class _DocsIf31CmUsOfdmaChanChannelId_Type(Unsigned32):
    """Custom type docsIf31CmUsOfdmaChanChannelId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsIf31CmUsOfdmaChanChannelId_Type.__name__ = "Unsigned32"
_DocsIf31CmUsOfdmaChanChannelId_Object = MibTableColumn
docsIf31CmUsOfdmaChanChannelId = _DocsIf31CmUsOfdmaChanChannelId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 13, 1, 12),
    _DocsIf31CmUsOfdmaChanChannelId_Type()
)
docsIf31CmUsOfdmaChanChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaChanChannelId.setStatus("current")
_DocsIf31CmUsOfdmaProfileStatsTable_Object = MibTable
docsIf31CmUsOfdmaProfileStatsTable = _DocsIf31CmUsOfdmaProfileStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 14)
)
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaProfileStatsTable.setStatus("current")
_DocsIf31CmUsOfdmaProfileStatsEntry_Object = MibTableRow
docsIf31CmUsOfdmaProfileStatsEntry = _DocsIf31CmUsOfdmaProfileStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 14, 1)
)
docsIf31CmUsOfdmaProfileStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF31-MIB", "docsIf31CmUsOfdmaProfileStatsIuc"),
)
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaProfileStatsEntry.setStatus("current")
_DocsIf31CmUsOfdmaProfileStatsIuc_Type = Unsigned32
_DocsIf31CmUsOfdmaProfileStatsIuc_Object = MibTableColumn
docsIf31CmUsOfdmaProfileStatsIuc = _DocsIf31CmUsOfdmaProfileStatsIuc_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 14, 1, 1),
    _DocsIf31CmUsOfdmaProfileStatsIuc_Type()
)
docsIf31CmUsOfdmaProfileStatsIuc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaProfileStatsIuc.setStatus("current")
_DocsIf31CmUsOfdmaProfileStatsOutOctets_Type = Counter64
_DocsIf31CmUsOfdmaProfileStatsOutOctets_Object = MibTableColumn
docsIf31CmUsOfdmaProfileStatsOutOctets = _DocsIf31CmUsOfdmaProfileStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 14, 1, 2),
    _DocsIf31CmUsOfdmaProfileStatsOutOctets_Type()
)
docsIf31CmUsOfdmaProfileStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaProfileStatsOutOctets.setStatus("current")
_DocsIf31CmUsOfdmaProfileStatsCtrDiscontinuityTime_Type = TimeStamp
_DocsIf31CmUsOfdmaProfileStatsCtrDiscontinuityTime_Object = MibTableColumn
docsIf31CmUsOfdmaProfileStatsCtrDiscontinuityTime = _DocsIf31CmUsOfdmaProfileStatsCtrDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 14, 1, 3),
    _DocsIf31CmUsOfdmaProfileStatsCtrDiscontinuityTime_Type()
)
docsIf31CmUsOfdmaProfileStatsCtrDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaProfileStatsCtrDiscontinuityTime.setStatus("current")
_DocsIf31CmUsOfdmaMinislotCfgStateTable_Object = MibTable
docsIf31CmUsOfdmaMinislotCfgStateTable = _DocsIf31CmUsOfdmaMinislotCfgStateTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 15)
)
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaMinislotCfgStateTable.setStatus("current")
_DocsIf31CmUsOfdmaMinislotCfgStateEntry_Object = MibTableRow
docsIf31CmUsOfdmaMinislotCfgStateEntry = _DocsIf31CmUsOfdmaMinislotCfgStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 15, 1)
)
docsIf31CmUsOfdmaMinislotCfgStateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF31-MIB", "docsIf31CmUsOfdmaProfileStatsIuc"),
    (0, "DOCS-IF31-MIB", "docsIf31CmUsOfdmaMinislotCfgStateStartMinislotNum"),
)
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaMinislotCfgStateEntry.setStatus("current")
_DocsIf31CmUsOfdmaMinislotCfgStateStartMinislotNum_Type = Unsigned32
_DocsIf31CmUsOfdmaMinislotCfgStateStartMinislotNum_Object = MibTableColumn
docsIf31CmUsOfdmaMinislotCfgStateStartMinislotNum = _DocsIf31CmUsOfdmaMinislotCfgStateStartMinislotNum_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 15, 1, 1),
    _DocsIf31CmUsOfdmaMinislotCfgStateStartMinislotNum_Type()
)
docsIf31CmUsOfdmaMinislotCfgStateStartMinislotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaMinislotCfgStateStartMinislotNum.setStatus("current")
_DocsIf31CmUsOfdmaMinislotCfgStateFirstSubcarrierId_Type = Unsigned32
_DocsIf31CmUsOfdmaMinislotCfgStateFirstSubcarrierId_Object = MibTableColumn
docsIf31CmUsOfdmaMinislotCfgStateFirstSubcarrierId = _DocsIf31CmUsOfdmaMinislotCfgStateFirstSubcarrierId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 15, 1, 2),
    _DocsIf31CmUsOfdmaMinislotCfgStateFirstSubcarrierId_Type()
)
docsIf31CmUsOfdmaMinislotCfgStateFirstSubcarrierId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaMinislotCfgStateFirstSubcarrierId.setStatus("current")
_DocsIf31CmUsOfdmaMinislotCfgStateNumConsecutiveMinislots_Type = Unsigned32
_DocsIf31CmUsOfdmaMinislotCfgStateNumConsecutiveMinislots_Object = MibTableColumn
docsIf31CmUsOfdmaMinislotCfgStateNumConsecutiveMinislots = _DocsIf31CmUsOfdmaMinislotCfgStateNumConsecutiveMinislots_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 15, 1, 3),
    _DocsIf31CmUsOfdmaMinislotCfgStateNumConsecutiveMinislots_Type()
)
docsIf31CmUsOfdmaMinislotCfgStateNumConsecutiveMinislots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaMinislotCfgStateNumConsecutiveMinislots.setStatus("current")
_DocsIf31CmUsOfdmaMinislotCfgStateMinislotPilotPattern_Type = Unsigned32
_DocsIf31CmUsOfdmaMinislotCfgStateMinislotPilotPattern_Object = MibTableColumn
docsIf31CmUsOfdmaMinislotCfgStateMinislotPilotPattern = _DocsIf31CmUsOfdmaMinislotCfgStateMinislotPilotPattern_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 15, 1, 4),
    _DocsIf31CmUsOfdmaMinislotCfgStateMinislotPilotPattern_Type()
)
docsIf31CmUsOfdmaMinislotCfgStateMinislotPilotPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaMinislotCfgStateMinislotPilotPattern.setStatus("current")
_DocsIf31CmUsOfdmaMinislotCfgStateDataSymbolModulation_Type = UsOfdmaModulationType
_DocsIf31CmUsOfdmaMinislotCfgStateDataSymbolModulation_Object = MibTableColumn
docsIf31CmUsOfdmaMinislotCfgStateDataSymbolModulation = _DocsIf31CmUsOfdmaMinislotCfgStateDataSymbolModulation_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 15, 1, 5),
    _DocsIf31CmUsOfdmaMinislotCfgStateDataSymbolModulation_Type()
)
docsIf31CmUsOfdmaMinislotCfgStateDataSymbolModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmUsOfdmaMinislotCfgStateDataSymbolModulation.setStatus("current")
_DocsIf31CmEmDlsStatsTable_Object = MibTable
docsIf31CmEmDlsStatsTable = _DocsIf31CmEmDlsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 16)
)
if mibBuilder.loadTexts:
    docsIf31CmEmDlsStatsTable.setStatus("current")
_DocsIf31CmEmDlsStatsEntry_Object = MibTableRow
docsIf31CmEmDlsStatsEntry = _DocsIf31CmEmDlsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 16, 1)
)
docsIf31CmEmDlsStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIf31CmEmDlsStatsEntry.setStatus("current")
_DocsIf31CmEmDlsStatsNumberTimesCrossedBelowUsEntryThrshlds_Type = Unsigned32
_DocsIf31CmEmDlsStatsNumberTimesCrossedBelowUsEntryThrshlds_Object = MibTableColumn
docsIf31CmEmDlsStatsNumberTimesCrossedBelowUsEntryThrshlds = _DocsIf31CmEmDlsStatsNumberTimesCrossedBelowUsEntryThrshlds_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 16, 1, 1),
    _DocsIf31CmEmDlsStatsNumberTimesCrossedBelowUsEntryThrshlds_Type()
)
docsIf31CmEmDlsStatsNumberTimesCrossedBelowUsEntryThrshlds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmEmDlsStatsNumberTimesCrossedBelowUsEntryThrshlds.setStatus("current")
_DocsIf31CmEmDlsStatsNumberTimesCrossedBelowDsEntryThrshlds_Type = Unsigned32
_DocsIf31CmEmDlsStatsNumberTimesCrossedBelowDsEntryThrshlds_Object = MibTableColumn
docsIf31CmEmDlsStatsNumberTimesCrossedBelowDsEntryThrshlds = _DocsIf31CmEmDlsStatsNumberTimesCrossedBelowDsEntryThrshlds_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 16, 1, 2),
    _DocsIf31CmEmDlsStatsNumberTimesCrossedBelowDsEntryThrshlds_Type()
)
docsIf31CmEmDlsStatsNumberTimesCrossedBelowDsEntryThrshlds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmEmDlsStatsNumberTimesCrossedBelowDsEntryThrshlds.setStatus("current")
_DocsIf31CmEmDlsStatsTotalDuration_Type = Unsigned32
_DocsIf31CmEmDlsStatsTotalDuration_Object = MibTableColumn
docsIf31CmEmDlsStatsTotalDuration = _DocsIf31CmEmDlsStatsTotalDuration_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 16, 1, 3),
    _DocsIf31CmEmDlsStatsTotalDuration_Type()
)
docsIf31CmEmDlsStatsTotalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmEmDlsStatsTotalDuration.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmEmDlsStatsTotalDuration.setUnits("seconds")
_DocsIf31CmEmDlsStatsTotalDurationBelowUsThrshlds_Type = Unsigned32
_DocsIf31CmEmDlsStatsTotalDurationBelowUsThrshlds_Object = MibTableColumn
docsIf31CmEmDlsStatsTotalDurationBelowUsThrshlds = _DocsIf31CmEmDlsStatsTotalDurationBelowUsThrshlds_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 16, 1, 4),
    _DocsIf31CmEmDlsStatsTotalDurationBelowUsThrshlds_Type()
)
docsIf31CmEmDlsStatsTotalDurationBelowUsThrshlds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmEmDlsStatsTotalDurationBelowUsThrshlds.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmEmDlsStatsTotalDurationBelowUsThrshlds.setUnits("seconds")
_DocsIf31CmEmDlsStatsTotalDurationBelowDsThrshlds_Type = Unsigned32
_DocsIf31CmEmDlsStatsTotalDurationBelowDsThrshlds_Object = MibTableColumn
docsIf31CmEmDlsStatsTotalDurationBelowDsThrshlds = _DocsIf31CmEmDlsStatsTotalDurationBelowDsThrshlds_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 16, 1, 5),
    _DocsIf31CmEmDlsStatsTotalDurationBelowDsThrshlds_Type()
)
docsIf31CmEmDlsStatsTotalDurationBelowDsThrshlds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmEmDlsStatsTotalDurationBelowDsThrshlds.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmEmDlsStatsTotalDurationBelowDsThrshlds.setUnits("seconds")
_DocsIf31CmEmDlsStatsTotalDurationBelowUsDsThrshlds_Type = Unsigned32
_DocsIf31CmEmDlsStatsTotalDurationBelowUsDsThrshlds_Object = MibTableColumn
docsIf31CmEmDlsStatsTotalDurationBelowUsDsThrshlds = _DocsIf31CmEmDlsStatsTotalDurationBelowUsDsThrshlds_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 16, 1, 6),
    _DocsIf31CmEmDlsStatsTotalDurationBelowUsDsThrshlds_Type()
)
docsIf31CmEmDlsStatsTotalDurationBelowUsDsThrshlds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmEmDlsStatsTotalDurationBelowUsDsThrshlds.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmEmDlsStatsTotalDurationBelowUsDsThrshlds.setUnits("seconds")
_DocsIf31CmEmDlsStatsNumSleepLatencyTriggers_Type = Counter32
_DocsIf31CmEmDlsStatsNumSleepLatencyTriggers_Object = MibTableColumn
docsIf31CmEmDlsStatsNumSleepLatencyTriggers = _DocsIf31CmEmDlsStatsNumSleepLatencyTriggers_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 16, 1, 7),
    _DocsIf31CmEmDlsStatsNumSleepLatencyTriggers_Type()
)
docsIf31CmEmDlsStatsNumSleepLatencyTriggers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmEmDlsStatsNumSleepLatencyTriggers.setStatus("current")
_DocsIf31CmEmDlsStatsNumSleepByteCtTriggers_Type = Counter32
_DocsIf31CmEmDlsStatsNumSleepByteCtTriggers_Object = MibTableColumn
docsIf31CmEmDlsStatsNumSleepByteCtTriggers = _DocsIf31CmEmDlsStatsNumSleepByteCtTriggers_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 16, 1, 8),
    _DocsIf31CmEmDlsStatsNumSleepByteCtTriggers_Type()
)
docsIf31CmEmDlsStatsNumSleepByteCtTriggers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmEmDlsStatsNumSleepByteCtTriggers.setStatus("current")
_DocsIf31CmEmDlsStatusTable_Object = MibTable
docsIf31CmEmDlsStatusTable = _DocsIf31CmEmDlsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 17)
)
if mibBuilder.loadTexts:
    docsIf31CmEmDlsStatusTable.setStatus("current")
_DocsIf31CmEmDlsStatusEntry_Object = MibTableRow
docsIf31CmEmDlsStatusEntry = _DocsIf31CmEmDlsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 17, 1)
)
docsIf31CmEmDlsStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIf31CmEmDlsStatusEntry.setStatus("current")
_DocsIf31CmEmDlsStatusAssignedEmIds_Type = EmIdList
_DocsIf31CmEmDlsStatusAssignedEmIds_Object = MibTableColumn
docsIf31CmEmDlsStatusAssignedEmIds = _DocsIf31CmEmDlsStatusAssignedEmIds_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 17, 1, 1),
    _DocsIf31CmEmDlsStatusAssignedEmIds_Type()
)
docsIf31CmEmDlsStatusAssignedEmIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmEmDlsStatusAssignedEmIds.setStatus("current")
_DocsIf31CmEmDlsStatusReceiveTimer_Type = Unsigned32
_DocsIf31CmEmDlsStatusReceiveTimer_Object = MibTableColumn
docsIf31CmEmDlsStatusReceiveTimer = _DocsIf31CmEmDlsStatusReceiveTimer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 17, 1, 2),
    _DocsIf31CmEmDlsStatusReceiveTimer_Type()
)
docsIf31CmEmDlsStatusReceiveTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmEmDlsStatusReceiveTimer.setStatus("current")


class _DocsIf31CmEmDlsStatusMaxSleepLatency_Type(Unsigned32):
    """Custom type docsIf31CmEmDlsStatusMaxSleepLatency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DocsIf31CmEmDlsStatusMaxSleepLatency_Type.__name__ = "Unsigned32"
_DocsIf31CmEmDlsStatusMaxSleepLatency_Object = MibTableColumn
docsIf31CmEmDlsStatusMaxSleepLatency = _DocsIf31CmEmDlsStatusMaxSleepLatency_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 17, 1, 3),
    _DocsIf31CmEmDlsStatusMaxSleepLatency_Type()
)
docsIf31CmEmDlsStatusMaxSleepLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmEmDlsStatusMaxSleepLatency.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmEmDlsStatusMaxSleepLatency.setUnits("milliseconds")


class _DocsIf31CmEmDlsStatusMaxSleepBytes_Type(Unsigned32):
    """Custom type docsIf31CmEmDlsStatusMaxSleepBytes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DocsIf31CmEmDlsStatusMaxSleepBytes_Type.__name__ = "Unsigned32"
_DocsIf31CmEmDlsStatusMaxSleepBytes_Object = MibTableColumn
docsIf31CmEmDlsStatusMaxSleepBytes = _DocsIf31CmEmDlsStatusMaxSleepBytes_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 17, 1, 4),
    _DocsIf31CmEmDlsStatusMaxSleepBytes_Type()
)
docsIf31CmEmDlsStatusMaxSleepBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmEmDlsStatusMaxSleepBytes.setStatus("current")
_DocsIf31CmSystemCfgState_ObjectIdentity = ObjectIdentity
docsIf31CmSystemCfgState = _DocsIf31CmSystemCfgState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 18)
)
_DocsIf31CmSystemCfgStateDiplexerCapability_Type = Unsigned32
_DocsIf31CmSystemCfgStateDiplexerCapability_Object = MibScalar
docsIf31CmSystemCfgStateDiplexerCapability = _DocsIf31CmSystemCfgStateDiplexerCapability_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 18, 1),
    _DocsIf31CmSystemCfgStateDiplexerCapability_Type()
)
docsIf31CmSystemCfgStateDiplexerCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmSystemCfgStateDiplexerCapability.setStatus("current")
_DocsIf31CmSystemCfgStateDiplexerCfgBandEdge_Type = Unsigned32
_DocsIf31CmSystemCfgStateDiplexerCfgBandEdge_Object = MibScalar
docsIf31CmSystemCfgStateDiplexerCfgBandEdge = _DocsIf31CmSystemCfgStateDiplexerCfgBandEdge_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 18, 2),
    _DocsIf31CmSystemCfgStateDiplexerCfgBandEdge_Type()
)
docsIf31CmSystemCfgStateDiplexerCfgBandEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmSystemCfgStateDiplexerCfgBandEdge.setStatus("current")
_DocsIf31CmSystemCfgStateDiplexerDsLowerCapability_Type = Unsigned32
_DocsIf31CmSystemCfgStateDiplexerDsLowerCapability_Object = MibScalar
docsIf31CmSystemCfgStateDiplexerDsLowerCapability = _DocsIf31CmSystemCfgStateDiplexerDsLowerCapability_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 18, 3),
    _DocsIf31CmSystemCfgStateDiplexerDsLowerCapability_Type()
)
docsIf31CmSystemCfgStateDiplexerDsLowerCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmSystemCfgStateDiplexerDsLowerCapability.setStatus("current")
_DocsIf31CmSystemCfgStateDiplexerCfgDsLowerBandEdge_Type = Unsigned32
_DocsIf31CmSystemCfgStateDiplexerCfgDsLowerBandEdge_Object = MibScalar
docsIf31CmSystemCfgStateDiplexerCfgDsLowerBandEdge = _DocsIf31CmSystemCfgStateDiplexerCfgDsLowerBandEdge_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 18, 4),
    _DocsIf31CmSystemCfgStateDiplexerCfgDsLowerBandEdge_Type()
)
docsIf31CmSystemCfgStateDiplexerCfgDsLowerBandEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmSystemCfgStateDiplexerCfgDsLowerBandEdge.setStatus("current")
_DocsIf31CmSystemCfgStateDiplexerDsUpperCapability_Type = Unsigned32
_DocsIf31CmSystemCfgStateDiplexerDsUpperCapability_Object = MibScalar
docsIf31CmSystemCfgStateDiplexerDsUpperCapability = _DocsIf31CmSystemCfgStateDiplexerDsUpperCapability_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 18, 5),
    _DocsIf31CmSystemCfgStateDiplexerDsUpperCapability_Type()
)
docsIf31CmSystemCfgStateDiplexerDsUpperCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmSystemCfgStateDiplexerDsUpperCapability.setStatus("current")
_DocsIf31CmSystemCfgStateDiplexerCfgDsUpperBandEdge_Type = Unsigned32
_DocsIf31CmSystemCfgStateDiplexerCfgDsUpperBandEdge_Object = MibScalar
docsIf31CmSystemCfgStateDiplexerCfgDsUpperBandEdge = _DocsIf31CmSystemCfgStateDiplexerCfgDsUpperBandEdge_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 18, 6),
    _DocsIf31CmSystemCfgStateDiplexerCfgDsUpperBandEdge_Type()
)
docsIf31CmSystemCfgStateDiplexerCfgDsUpperBandEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmSystemCfgStateDiplexerCfgDsUpperBandEdge.setStatus("current")
_DocsIf31CmtsDsOfdmChanTable_Object = MibTable
docsIf31CmtsDsOfdmChanTable = _DocsIf31CmtsDsOfdmChanTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 19)
)
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanTable.setStatus("current")
_DocsIf31CmtsDsOfdmChanEntry_Object = MibTableRow
docsIf31CmtsDsOfdmChanEntry = _DocsIf31CmtsDsOfdmChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 19, 1)
)
docsIf31CmtsDsOfdmChanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanEntry.setStatus("current")


class _DocsIf31CmtsDsOfdmChanChannelId_Type(Integer32):
    """Custom type docsIf31CmtsDsOfdmChanChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsIf31CmtsDsOfdmChanChannelId_Type.__name__ = "Integer32"
_DocsIf31CmtsDsOfdmChanChannelId_Object = MibTableColumn
docsIf31CmtsDsOfdmChanChannelId = _DocsIf31CmtsDsOfdmChanChannelId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 19, 1, 1),
    _DocsIf31CmtsDsOfdmChanChannelId_Type()
)
docsIf31CmtsDsOfdmChanChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanChannelId.setStatus("current")
_DocsIf31CmtsDsOfdmChanLowerBdryFreq_Type = Unsigned32
_DocsIf31CmtsDsOfdmChanLowerBdryFreq_Object = MibTableColumn
docsIf31CmtsDsOfdmChanLowerBdryFreq = _DocsIf31CmtsDsOfdmChanLowerBdryFreq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 19, 1, 2),
    _DocsIf31CmtsDsOfdmChanLowerBdryFreq_Type()
)
docsIf31CmtsDsOfdmChanLowerBdryFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanLowerBdryFreq.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanLowerBdryFreq.setUnits("Hz")
_DocsIf31CmtsDsOfdmChanUpperBdryFreq_Type = Unsigned32
_DocsIf31CmtsDsOfdmChanUpperBdryFreq_Object = MibTableColumn
docsIf31CmtsDsOfdmChanUpperBdryFreq = _DocsIf31CmtsDsOfdmChanUpperBdryFreq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 19, 1, 3),
    _DocsIf31CmtsDsOfdmChanUpperBdryFreq_Type()
)
docsIf31CmtsDsOfdmChanUpperBdryFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanUpperBdryFreq.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanUpperBdryFreq.setUnits("Hz")
_DocsIf31CmtsDsOfdmChanLowerBdryEncompSpectrum_Type = Unsigned32
_DocsIf31CmtsDsOfdmChanLowerBdryEncompSpectrum_Object = MibTableColumn
docsIf31CmtsDsOfdmChanLowerBdryEncompSpectrum = _DocsIf31CmtsDsOfdmChanLowerBdryEncompSpectrum_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 19, 1, 4),
    _DocsIf31CmtsDsOfdmChanLowerBdryEncompSpectrum_Type()
)
docsIf31CmtsDsOfdmChanLowerBdryEncompSpectrum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanLowerBdryEncompSpectrum.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanLowerBdryEncompSpectrum.setUnits("Hz")
_DocsIf31CmtsDsOfdmChanUpperBdryEncompSpectrum_Type = Unsigned32
_DocsIf31CmtsDsOfdmChanUpperBdryEncompSpectrum_Object = MibTableColumn
docsIf31CmtsDsOfdmChanUpperBdryEncompSpectrum = _DocsIf31CmtsDsOfdmChanUpperBdryEncompSpectrum_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 19, 1, 5),
    _DocsIf31CmtsDsOfdmChanUpperBdryEncompSpectrum_Type()
)
docsIf31CmtsDsOfdmChanUpperBdryEncompSpectrum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanUpperBdryEncompSpectrum.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanUpperBdryEncompSpectrum.setUnits("Hz")
_DocsIf31CmtsDsOfdmChanPlcFreq_Type = Unsigned32
_DocsIf31CmtsDsOfdmChanPlcFreq_Object = MibTableColumn
docsIf31CmtsDsOfdmChanPlcFreq = _DocsIf31CmtsDsOfdmChanPlcFreq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 19, 1, 6),
    _DocsIf31CmtsDsOfdmChanPlcFreq_Type()
)
docsIf31CmtsDsOfdmChanPlcFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanPlcFreq.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanPlcFreq.setUnits("Hz")
_DocsIf31CmtsDsOfdmChanSubcarrierZeroFreq_Type = Unsigned32
_DocsIf31CmtsDsOfdmChanSubcarrierZeroFreq_Object = MibTableColumn
docsIf31CmtsDsOfdmChanSubcarrierZeroFreq = _DocsIf31CmtsDsOfdmChanSubcarrierZeroFreq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 19, 1, 7),
    _DocsIf31CmtsDsOfdmChanSubcarrierZeroFreq_Type()
)
docsIf31CmtsDsOfdmChanSubcarrierZeroFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanSubcarrierZeroFreq.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanSubcarrierZeroFreq.setUnits("Hz")
_DocsIf31CmtsDsOfdmChanFirstActiveSubcarrierNum_Type = Unsigned32
_DocsIf31CmtsDsOfdmChanFirstActiveSubcarrierNum_Object = MibTableColumn
docsIf31CmtsDsOfdmChanFirstActiveSubcarrierNum = _DocsIf31CmtsDsOfdmChanFirstActiveSubcarrierNum_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 19, 1, 8),
    _DocsIf31CmtsDsOfdmChanFirstActiveSubcarrierNum_Type()
)
docsIf31CmtsDsOfdmChanFirstActiveSubcarrierNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanFirstActiveSubcarrierNum.setStatus("current")
_DocsIf31CmtsDsOfdmChanLastActiveSubcarrierNum_Type = Unsigned32
_DocsIf31CmtsDsOfdmChanLastActiveSubcarrierNum_Object = MibTableColumn
docsIf31CmtsDsOfdmChanLastActiveSubcarrierNum = _DocsIf31CmtsDsOfdmChanLastActiveSubcarrierNum_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 19, 1, 9),
    _DocsIf31CmtsDsOfdmChanLastActiveSubcarrierNum_Type()
)
docsIf31CmtsDsOfdmChanLastActiveSubcarrierNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanLastActiveSubcarrierNum.setStatus("current")
_DocsIf31CmtsDsOfdmChanNumActiveSubcarriers_Type = Unsigned32
_DocsIf31CmtsDsOfdmChanNumActiveSubcarriers_Object = MibTableColumn
docsIf31CmtsDsOfdmChanNumActiveSubcarriers = _DocsIf31CmtsDsOfdmChanNumActiveSubcarriers_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 19, 1, 10),
    _DocsIf31CmtsDsOfdmChanNumActiveSubcarriers_Type()
)
docsIf31CmtsDsOfdmChanNumActiveSubcarriers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanNumActiveSubcarriers.setStatus("current")
_DocsIf31CmtsDsOfdmChanSubcarrierSpacing_Type = SubcarrierSpacingType
_DocsIf31CmtsDsOfdmChanSubcarrierSpacing_Object = MibTableColumn
docsIf31CmtsDsOfdmChanSubcarrierSpacing = _DocsIf31CmtsDsOfdmChanSubcarrierSpacing_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 19, 1, 11),
    _DocsIf31CmtsDsOfdmChanSubcarrierSpacing_Type()
)
docsIf31CmtsDsOfdmChanSubcarrierSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanSubcarrierSpacing.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanSubcarrierSpacing.setUnits("kHz")
_DocsIf31CmtsDsOfdmChanLowerGuardbandWidth_Type = Unsigned32
_DocsIf31CmtsDsOfdmChanLowerGuardbandWidth_Object = MibTableColumn
docsIf31CmtsDsOfdmChanLowerGuardbandWidth = _DocsIf31CmtsDsOfdmChanLowerGuardbandWidth_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 19, 1, 12),
    _DocsIf31CmtsDsOfdmChanLowerGuardbandWidth_Type()
)
docsIf31CmtsDsOfdmChanLowerGuardbandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanLowerGuardbandWidth.setStatus("current")
_DocsIf31CmtsDsOfdmChanUpperGuardbandWidth_Type = Unsigned32
_DocsIf31CmtsDsOfdmChanUpperGuardbandWidth_Object = MibTableColumn
docsIf31CmtsDsOfdmChanUpperGuardbandWidth = _DocsIf31CmtsDsOfdmChanUpperGuardbandWidth_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 19, 1, 13),
    _DocsIf31CmtsDsOfdmChanUpperGuardbandWidth_Type()
)
docsIf31CmtsDsOfdmChanUpperGuardbandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanUpperGuardbandWidth.setStatus("current")
_DocsIf31CmtsDsOfdmChanCyclicPrefix_Type = DsOfdmCyclicPrefix
_DocsIf31CmtsDsOfdmChanCyclicPrefix_Object = MibTableColumn
docsIf31CmtsDsOfdmChanCyclicPrefix = _DocsIf31CmtsDsOfdmChanCyclicPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 19, 1, 14),
    _DocsIf31CmtsDsOfdmChanCyclicPrefix_Type()
)
docsIf31CmtsDsOfdmChanCyclicPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanCyclicPrefix.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanCyclicPrefix.setUnits("number of samples")
_DocsIf31CmtsDsOfdmChanRollOffPeriod_Type = DsOfdmRollOffPeriod
_DocsIf31CmtsDsOfdmChanRollOffPeriod_Object = MibTableColumn
docsIf31CmtsDsOfdmChanRollOffPeriod = _DocsIf31CmtsDsOfdmChanRollOffPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 19, 1, 15),
    _DocsIf31CmtsDsOfdmChanRollOffPeriod_Type()
)
docsIf31CmtsDsOfdmChanRollOffPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanRollOffPeriod.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanRollOffPeriod.setUnits("number of samples")
_DocsIf31CmtsDsOfdmChanTimeInterleaverDepth_Type = TimeInterleaverDepth
_DocsIf31CmtsDsOfdmChanTimeInterleaverDepth_Object = MibTableColumn
docsIf31CmtsDsOfdmChanTimeInterleaverDepth = _DocsIf31CmtsDsOfdmChanTimeInterleaverDepth_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 19, 1, 16),
    _DocsIf31CmtsDsOfdmChanTimeInterleaverDepth_Type()
)
docsIf31CmtsDsOfdmChanTimeInterleaverDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanTimeInterleaverDepth.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanTimeInterleaverDepth.setUnits("symbols")
_DocsIf31CmtsDsOfdmChanNumPilots_Type = Unsigned32
_DocsIf31CmtsDsOfdmChanNumPilots_Object = MibTableColumn
docsIf31CmtsDsOfdmChanNumPilots = _DocsIf31CmtsDsOfdmChanNumPilots_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 19, 1, 17),
    _DocsIf31CmtsDsOfdmChanNumPilots_Type()
)
docsIf31CmtsDsOfdmChanNumPilots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanNumPilots.setStatus("current")
_DocsIf31CmtsDsOfdmChanPilotScaleFactor_Type = Unsigned32
_DocsIf31CmtsDsOfdmChanPilotScaleFactor_Object = MibTableColumn
docsIf31CmtsDsOfdmChanPilotScaleFactor = _DocsIf31CmtsDsOfdmChanPilotScaleFactor_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 19, 1, 18),
    _DocsIf31CmtsDsOfdmChanPilotScaleFactor_Type()
)
docsIf31CmtsDsOfdmChanPilotScaleFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanPilotScaleFactor.setStatus("current")
_DocsIf31CmtsDsOfdmChanNcpModulation_Type = DsOfdmModulationType
_DocsIf31CmtsDsOfdmChanNcpModulation_Object = MibTableColumn
docsIf31CmtsDsOfdmChanNcpModulation = _DocsIf31CmtsDsOfdmChanNcpModulation_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 19, 1, 19),
    _DocsIf31CmtsDsOfdmChanNcpModulation_Type()
)
docsIf31CmtsDsOfdmChanNcpModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanNcpModulation.setStatus("current")


class _DocsIf31CmtsDsOfdmChanUtilization_Type(Unsigned32):
    """Custom type docsIf31CmtsDsOfdmChanUtilization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DocsIf31CmtsDsOfdmChanUtilization_Type.__name__ = "Unsigned32"
_DocsIf31CmtsDsOfdmChanUtilization_Object = MibTableColumn
docsIf31CmtsDsOfdmChanUtilization = _DocsIf31CmtsDsOfdmChanUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 19, 1, 20),
    _DocsIf31CmtsDsOfdmChanUtilization_Type()
)
docsIf31CmtsDsOfdmChanUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanUtilization.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanUtilization.setUnits("percent")
_DocsIf31CmtsDsOfdmProfileStatsTable_Object = MibTable
docsIf31CmtsDsOfdmProfileStatsTable = _DocsIf31CmtsDsOfdmProfileStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 20)
)
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmProfileStatsTable.setStatus("current")
_DocsIf31CmtsDsOfdmProfileStatsEntry_Object = MibTableRow
docsIf31CmtsDsOfdmProfileStatsEntry = _DocsIf31CmtsDsOfdmProfileStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 20, 1)
)
docsIf31CmtsDsOfdmProfileStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF31-MIB", "docsIf31CmtsDsOfdmProfileStatsProfileId"),
)
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmProfileStatsEntry.setStatus("current")


class _DocsIf31CmtsDsOfdmProfileStatsProfileId_Type(Unsigned32):
    """Custom type docsIf31CmtsDsOfdmProfileStatsProfileId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DocsIf31CmtsDsOfdmProfileStatsProfileId_Type.__name__ = "Unsigned32"
_DocsIf31CmtsDsOfdmProfileStatsProfileId_Object = MibTableColumn
docsIf31CmtsDsOfdmProfileStatsProfileId = _DocsIf31CmtsDsOfdmProfileStatsProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 20, 1, 1),
    _DocsIf31CmtsDsOfdmProfileStatsProfileId_Type()
)
docsIf31CmtsDsOfdmProfileStatsProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmProfileStatsProfileId.setStatus("current")


class _DocsIf31CmtsDsOfdmProfileStatsConfigChangeCt_Type(Unsigned32):
    """Custom type docsIf31CmtsDsOfdmProfileStatsConfigChangeCt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsIf31CmtsDsOfdmProfileStatsConfigChangeCt_Type.__name__ = "Unsigned32"
_DocsIf31CmtsDsOfdmProfileStatsConfigChangeCt_Object = MibTableColumn
docsIf31CmtsDsOfdmProfileStatsConfigChangeCt = _DocsIf31CmtsDsOfdmProfileStatsConfigChangeCt_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 20, 1, 2),
    _DocsIf31CmtsDsOfdmProfileStatsConfigChangeCt_Type()
)
docsIf31CmtsDsOfdmProfileStatsConfigChangeCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmProfileStatsConfigChangeCt.setStatus("current")
_DocsIf31CmtsDsOfdmProfileStatsFullChannelSpeed_Type = CounterBasedGauge64
_DocsIf31CmtsDsOfdmProfileStatsFullChannelSpeed_Object = MibTableColumn
docsIf31CmtsDsOfdmProfileStatsFullChannelSpeed = _DocsIf31CmtsDsOfdmProfileStatsFullChannelSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 20, 1, 3),
    _DocsIf31CmtsDsOfdmProfileStatsFullChannelSpeed_Type()
)
docsIf31CmtsDsOfdmProfileStatsFullChannelSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmProfileStatsFullChannelSpeed.setStatus("current")
_DocsIf31CmtsDsOfdmProfileStatsOutOctets_Type = Counter64
_DocsIf31CmtsDsOfdmProfileStatsOutOctets_Object = MibTableColumn
docsIf31CmtsDsOfdmProfileStatsOutOctets = _DocsIf31CmtsDsOfdmProfileStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 20, 1, 4),
    _DocsIf31CmtsDsOfdmProfileStatsOutOctets_Type()
)
docsIf31CmtsDsOfdmProfileStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmProfileStatsOutOctets.setStatus("current")
_DocsIf31CmtsDsOfdmProfileStatsOutUnicastOctets_Type = Counter64
_DocsIf31CmtsDsOfdmProfileStatsOutUnicastOctets_Object = MibTableColumn
docsIf31CmtsDsOfdmProfileStatsOutUnicastOctets = _DocsIf31CmtsDsOfdmProfileStatsOutUnicastOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 20, 1, 5),
    _DocsIf31CmtsDsOfdmProfileStatsOutUnicastOctets_Type()
)
docsIf31CmtsDsOfdmProfileStatsOutUnicastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmProfileStatsOutUnicastOctets.setStatus("current")
_DocsIf31CmtsDsOfdmProfileStatsOutMulticastOctets_Type = Counter64
_DocsIf31CmtsDsOfdmProfileStatsOutMulticastOctets_Object = MibTableColumn
docsIf31CmtsDsOfdmProfileStatsOutMulticastOctets = _DocsIf31CmtsDsOfdmProfileStatsOutMulticastOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 20, 1, 6),
    _DocsIf31CmtsDsOfdmProfileStatsOutMulticastOctets_Type()
)
docsIf31CmtsDsOfdmProfileStatsOutMulticastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmProfileStatsOutMulticastOctets.setStatus("current")
_DocsIf31CmtsDsOfdmProfileStatsOutFrames_Type = Counter64
_DocsIf31CmtsDsOfdmProfileStatsOutFrames_Object = MibTableColumn
docsIf31CmtsDsOfdmProfileStatsOutFrames = _DocsIf31CmtsDsOfdmProfileStatsOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 20, 1, 7),
    _DocsIf31CmtsDsOfdmProfileStatsOutFrames_Type()
)
docsIf31CmtsDsOfdmProfileStatsOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmProfileStatsOutFrames.setStatus("current")
_DocsIf31CmtsDsOfdmProfileStatsOutUnicastFrames_Type = Counter64
_DocsIf31CmtsDsOfdmProfileStatsOutUnicastFrames_Object = MibTableColumn
docsIf31CmtsDsOfdmProfileStatsOutUnicastFrames = _DocsIf31CmtsDsOfdmProfileStatsOutUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 20, 1, 8),
    _DocsIf31CmtsDsOfdmProfileStatsOutUnicastFrames_Type()
)
docsIf31CmtsDsOfdmProfileStatsOutUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmProfileStatsOutUnicastFrames.setStatus("current")
_DocsIf31CmtsDsOfdmProfileStatsOutMulticastFrames_Type = Counter64
_DocsIf31CmtsDsOfdmProfileStatsOutMulticastFrames_Object = MibTableColumn
docsIf31CmtsDsOfdmProfileStatsOutMulticastFrames = _DocsIf31CmtsDsOfdmProfileStatsOutMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 20, 1, 9),
    _DocsIf31CmtsDsOfdmProfileStatsOutMulticastFrames_Type()
)
docsIf31CmtsDsOfdmProfileStatsOutMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmProfileStatsOutMulticastFrames.setStatus("current")
_DocsIf31CmtsDsOfdmProfileStatsCtrDiscontinuityTime_Type = TimeStamp
_DocsIf31CmtsDsOfdmProfileStatsCtrDiscontinuityTime_Object = MibTableColumn
docsIf31CmtsDsOfdmProfileStatsCtrDiscontinuityTime = _DocsIf31CmtsDsOfdmProfileStatsCtrDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 20, 1, 10),
    _DocsIf31CmtsDsOfdmProfileStatsCtrDiscontinuityTime_Type()
)
docsIf31CmtsDsOfdmProfileStatsCtrDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmProfileStatsCtrDiscontinuityTime.setStatus("current")
_DocsIf31CmtsDsOfdmProfileStatsAssignedCmCt_Type = Unsigned32
_DocsIf31CmtsDsOfdmProfileStatsAssignedCmCt_Object = MibTableColumn
docsIf31CmtsDsOfdmProfileStatsAssignedCmCt = _DocsIf31CmtsDsOfdmProfileStatsAssignedCmCt_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 20, 1, 11),
    _DocsIf31CmtsDsOfdmProfileStatsAssignedCmCt_Type()
)
docsIf31CmtsDsOfdmProfileStatsAssignedCmCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmProfileStatsAssignedCmCt.setStatus("current")
_DocsIf31CmtsDsOfdmSubcarrierStatusTable_Object = MibTable
docsIf31CmtsDsOfdmSubcarrierStatusTable = _DocsIf31CmtsDsOfdmSubcarrierStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 21)
)
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmSubcarrierStatusTable.setStatus("current")
_DocsIf31CmtsDsOfdmSubcarrierStatusEntry_Object = MibTableRow
docsIf31CmtsDsOfdmSubcarrierStatusEntry = _DocsIf31CmtsDsOfdmSubcarrierStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 21, 1)
)
docsIf31CmtsDsOfdmSubcarrierStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF31-MIB", "docsIf31CmtsDsOfdmProfileStatsProfileId"),
    (0, "DOCS-IF31-MIB", "docsIf31CmtsDsOfdmSubcarrierStatusStartId"),
)
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmSubcarrierStatusEntry.setStatus("current")
_DocsIf31CmtsDsOfdmSubcarrierStatusStartId_Type = Unsigned32
_DocsIf31CmtsDsOfdmSubcarrierStatusStartId_Object = MibTableColumn
docsIf31CmtsDsOfdmSubcarrierStatusStartId = _DocsIf31CmtsDsOfdmSubcarrierStatusStartId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 21, 1, 1),
    _DocsIf31CmtsDsOfdmSubcarrierStatusStartId_Type()
)
docsIf31CmtsDsOfdmSubcarrierStatusStartId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmSubcarrierStatusStartId.setStatus("current")
_DocsIf31CmtsDsOfdmSubcarrierStatusEndId_Type = Unsigned32
_DocsIf31CmtsDsOfdmSubcarrierStatusEndId_Object = MibTableColumn
docsIf31CmtsDsOfdmSubcarrierStatusEndId = _DocsIf31CmtsDsOfdmSubcarrierStatusEndId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 21, 1, 2),
    _DocsIf31CmtsDsOfdmSubcarrierStatusEndId_Type()
)
docsIf31CmtsDsOfdmSubcarrierStatusEndId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmSubcarrierStatusEndId.setStatus("current")
_DocsIf31CmtsDsOfdmSubcarrierStatusMainModulation_Type = DsOfdmModulationType
_DocsIf31CmtsDsOfdmSubcarrierStatusMainModulation_Object = MibTableColumn
docsIf31CmtsDsOfdmSubcarrierStatusMainModulation = _DocsIf31CmtsDsOfdmSubcarrierStatusMainModulation_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 21, 1, 3),
    _DocsIf31CmtsDsOfdmSubcarrierStatusMainModulation_Type()
)
docsIf31CmtsDsOfdmSubcarrierStatusMainModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmSubcarrierStatusMainModulation.setStatus("current")
_DocsIf31CmtsDsOfdmSubcarrierStatusSkip_Type = TruthValue
_DocsIf31CmtsDsOfdmSubcarrierStatusSkip_Object = MibTableColumn
docsIf31CmtsDsOfdmSubcarrierStatusSkip = _DocsIf31CmtsDsOfdmSubcarrierStatusSkip_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 21, 1, 4),
    _DocsIf31CmtsDsOfdmSubcarrierStatusSkip_Type()
)
docsIf31CmtsDsOfdmSubcarrierStatusSkip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmSubcarrierStatusSkip.setStatus("current")
_DocsIf31CmtsDsOfdmSubcarrierStatusSkipModulation_Type = DsOfdmModulationType
_DocsIf31CmtsDsOfdmSubcarrierStatusSkipModulation_Object = MibTableColumn
docsIf31CmtsDsOfdmSubcarrierStatusSkipModulation = _DocsIf31CmtsDsOfdmSubcarrierStatusSkipModulation_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 21, 1, 5),
    _DocsIf31CmtsDsOfdmSubcarrierStatusSkipModulation_Type()
)
docsIf31CmtsDsOfdmSubcarrierStatusSkipModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmSubcarrierStatusSkipModulation.setStatus("current")
_DocsIf31CmtsDsOfdmChanPowerTable_Object = MibTable
docsIf31CmtsDsOfdmChanPowerTable = _DocsIf31CmtsDsOfdmChanPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 22)
)
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanPowerTable.setStatus("current")
_DocsIf31CmtsDsOfdmChanPowerEntry_Object = MibTableRow
docsIf31CmtsDsOfdmChanPowerEntry = _DocsIf31CmtsDsOfdmChanPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 22, 1)
)
docsIf31CmtsDsOfdmChanPowerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF31-MIB", "docsIf31CmtsDsOfdmChanPowerBandIndex"),
)
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanPowerEntry.setStatus("current")
_DocsIf31CmtsDsOfdmChanPowerBandIndex_Type = Unsigned32
_DocsIf31CmtsDsOfdmChanPowerBandIndex_Object = MibTableColumn
docsIf31CmtsDsOfdmChanPowerBandIndex = _DocsIf31CmtsDsOfdmChanPowerBandIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 22, 1, 1),
    _DocsIf31CmtsDsOfdmChanPowerBandIndex_Type()
)
docsIf31CmtsDsOfdmChanPowerBandIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanPowerBandIndex.setStatus("current")
_DocsIf31CmtsDsOfdmChanPowerCenterFrequency_Type = Unsigned32
_DocsIf31CmtsDsOfdmChanPowerCenterFrequency_Object = MibTableColumn
docsIf31CmtsDsOfdmChanPowerCenterFrequency = _DocsIf31CmtsDsOfdmChanPowerCenterFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 22, 1, 2),
    _DocsIf31CmtsDsOfdmChanPowerCenterFrequency_Type()
)
docsIf31CmtsDsOfdmChanPowerCenterFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanPowerCenterFrequency.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanPowerCenterFrequency.setUnits("Hz")
_DocsIf31CmtsDsOfdmChanPowerTxPower_Type = TenthdBmV
_DocsIf31CmtsDsOfdmChanPowerTxPower_Object = MibTableColumn
docsIf31CmtsDsOfdmChanPowerTxPower = _DocsIf31CmtsDsOfdmChanPowerTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 22, 1, 3),
    _DocsIf31CmtsDsOfdmChanPowerTxPower_Type()
)
docsIf31CmtsDsOfdmChanPowerTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanPowerTxPower.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmChanPowerTxPower.setUnits("TenthdBmV")
_DocsIf31CmtsUsOfdmaChanTable_Object = MibTable
docsIf31CmtsUsOfdmaChanTable = _DocsIf31CmtsUsOfdmaChanTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 23)
)
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanTable.setStatus("current")
_DocsIf31CmtsUsOfdmaChanEntry_Object = MibTableRow
docsIf31CmtsUsOfdmaChanEntry = _DocsIf31CmtsUsOfdmaChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 23, 1)
)
docsIf31CmtsUsOfdmaChanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanEntry.setStatus("current")
_DocsIf31CmtsUsOfdmaChanTemplateIndex_Type = Unsigned32
_DocsIf31CmtsUsOfdmaChanTemplateIndex_Object = MibTableColumn
docsIf31CmtsUsOfdmaChanTemplateIndex = _DocsIf31CmtsUsOfdmaChanTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 23, 1, 1),
    _DocsIf31CmtsUsOfdmaChanTemplateIndex_Type()
)
docsIf31CmtsUsOfdmaChanTemplateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanTemplateIndex.setStatus("current")


class _DocsIf31CmtsUsOfdmaChanConfigChangeCt_Type(Unsigned32):
    """Custom type docsIf31CmtsUsOfdmaChanConfigChangeCt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsIf31CmtsUsOfdmaChanConfigChangeCt_Type.__name__ = "Unsigned32"
_DocsIf31CmtsUsOfdmaChanConfigChangeCt_Object = MibTableColumn
docsIf31CmtsUsOfdmaChanConfigChangeCt = _DocsIf31CmtsUsOfdmaChanConfigChangeCt_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 23, 1, 2),
    _DocsIf31CmtsUsOfdmaChanConfigChangeCt_Type()
)
docsIf31CmtsUsOfdmaChanConfigChangeCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanConfigChangeCt.setStatus("current")
_DocsIf31CmtsUsOfdmaChanTargetRxPower_Type = TenthdBmV
_DocsIf31CmtsUsOfdmaChanTargetRxPower_Object = MibTableColumn
docsIf31CmtsUsOfdmaChanTargetRxPower = _DocsIf31CmtsUsOfdmaChanTargetRxPower_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 23, 1, 3),
    _DocsIf31CmtsUsOfdmaChanTargetRxPower_Type()
)
docsIf31CmtsUsOfdmaChanTargetRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanTargetRxPower.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanTargetRxPower.setUnits("TenthdBmV")
_DocsIf31CmtsUsOfdmaChanLowerBdryFreq_Type = Unsigned32
_DocsIf31CmtsUsOfdmaChanLowerBdryFreq_Object = MibTableColumn
docsIf31CmtsUsOfdmaChanLowerBdryFreq = _DocsIf31CmtsUsOfdmaChanLowerBdryFreq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 23, 1, 4),
    _DocsIf31CmtsUsOfdmaChanLowerBdryFreq_Type()
)
docsIf31CmtsUsOfdmaChanLowerBdryFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanLowerBdryFreq.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanLowerBdryFreq.setUnits("Hz")
_DocsIf31CmtsUsOfdmaChanUpperBdryFreq_Type = Unsigned32
_DocsIf31CmtsUsOfdmaChanUpperBdryFreq_Object = MibTableColumn
docsIf31CmtsUsOfdmaChanUpperBdryFreq = _DocsIf31CmtsUsOfdmaChanUpperBdryFreq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 23, 1, 5),
    _DocsIf31CmtsUsOfdmaChanUpperBdryFreq_Type()
)
docsIf31CmtsUsOfdmaChanUpperBdryFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanUpperBdryFreq.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanUpperBdryFreq.setUnits("Hz")
_DocsIf31CmtsUsOfdmaChanSubcarrierSpacing_Type = SubcarrierSpacingType
_DocsIf31CmtsUsOfdmaChanSubcarrierSpacing_Object = MibTableColumn
docsIf31CmtsUsOfdmaChanSubcarrierSpacing = _DocsIf31CmtsUsOfdmaChanSubcarrierSpacing_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 23, 1, 6),
    _DocsIf31CmtsUsOfdmaChanSubcarrierSpacing_Type()
)
docsIf31CmtsUsOfdmaChanSubcarrierSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanSubcarrierSpacing.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanSubcarrierSpacing.setUnits("kHz")
_DocsIf31CmtsUsOfdmaChanCyclicPrefix_Type = UsOfdmaCyclicPrefix
_DocsIf31CmtsUsOfdmaChanCyclicPrefix_Object = MibTableColumn
docsIf31CmtsUsOfdmaChanCyclicPrefix = _DocsIf31CmtsUsOfdmaChanCyclicPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 23, 1, 7),
    _DocsIf31CmtsUsOfdmaChanCyclicPrefix_Type()
)
docsIf31CmtsUsOfdmaChanCyclicPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanCyclicPrefix.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanCyclicPrefix.setUnits("number of samples")
_DocsIf31CmtsUsOfdmaChanNumSymbolsPerFrame_Type = Unsigned32
_DocsIf31CmtsUsOfdmaChanNumSymbolsPerFrame_Object = MibTableColumn
docsIf31CmtsUsOfdmaChanNumSymbolsPerFrame = _DocsIf31CmtsUsOfdmaChanNumSymbolsPerFrame_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 23, 1, 8),
    _DocsIf31CmtsUsOfdmaChanNumSymbolsPerFrame_Type()
)
docsIf31CmtsUsOfdmaChanNumSymbolsPerFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanNumSymbolsPerFrame.setStatus("current")
_DocsIf31CmtsUsOfdmaChanRollOffPeriod_Type = UsOfdmaRollOffPeriod
_DocsIf31CmtsUsOfdmaChanRollOffPeriod_Object = MibTableColumn
docsIf31CmtsUsOfdmaChanRollOffPeriod = _DocsIf31CmtsUsOfdmaChanRollOffPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 23, 1, 9),
    _DocsIf31CmtsUsOfdmaChanRollOffPeriod_Type()
)
docsIf31CmtsUsOfdmaChanRollOffPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanRollOffPeriod.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanRollOffPeriod.setUnits("number of samples")
_DocsIf31CmtsUsOfdmaChanPreEqEnable_Type = TruthValue
_DocsIf31CmtsUsOfdmaChanPreEqEnable_Object = MibTableColumn
docsIf31CmtsUsOfdmaChanPreEqEnable = _DocsIf31CmtsUsOfdmaChanPreEqEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 23, 1, 10),
    _DocsIf31CmtsUsOfdmaChanPreEqEnable_Type()
)
docsIf31CmtsUsOfdmaChanPreEqEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanPreEqEnable.setStatus("current")
_DocsIf31CmtsUsOfdmaChanFineRngGuardband_Type = Unsigned32
_DocsIf31CmtsUsOfdmaChanFineRngGuardband_Object = MibTableColumn
docsIf31CmtsUsOfdmaChanFineRngGuardband = _DocsIf31CmtsUsOfdmaChanFineRngGuardband_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 23, 1, 11),
    _DocsIf31CmtsUsOfdmaChanFineRngGuardband_Type()
)
docsIf31CmtsUsOfdmaChanFineRngGuardband.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanFineRngGuardband.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanFineRngGuardband.setUnits("Hz")
_DocsIf31CmtsUsOfdmaChanFineRngNumSubcarriers_Type = Unsigned32
_DocsIf31CmtsUsOfdmaChanFineRngNumSubcarriers_Object = MibTableColumn
docsIf31CmtsUsOfdmaChanFineRngNumSubcarriers = _DocsIf31CmtsUsOfdmaChanFineRngNumSubcarriers_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 23, 1, 12),
    _DocsIf31CmtsUsOfdmaChanFineRngNumSubcarriers_Type()
)
docsIf31CmtsUsOfdmaChanFineRngNumSubcarriers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanFineRngNumSubcarriers.setStatus("current")
_DocsIf31CmtsUsOfdmaChanFineRngPreambleLen_Type = Unsigned32
_DocsIf31CmtsUsOfdmaChanFineRngPreambleLen_Object = MibTableColumn
docsIf31CmtsUsOfdmaChanFineRngPreambleLen = _DocsIf31CmtsUsOfdmaChanFineRngPreambleLen_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 23, 1, 13),
    _DocsIf31CmtsUsOfdmaChanFineRngPreambleLen_Type()
)
docsIf31CmtsUsOfdmaChanFineRngPreambleLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanFineRngPreambleLen.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanFineRngPreambleLen.setUnits("bits")
_DocsIf31CmtsUsOfdmaChanInitRngGuardband_Type = Unsigned32
_DocsIf31CmtsUsOfdmaChanInitRngGuardband_Object = MibTableColumn
docsIf31CmtsUsOfdmaChanInitRngGuardband = _DocsIf31CmtsUsOfdmaChanInitRngGuardband_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 23, 1, 14),
    _DocsIf31CmtsUsOfdmaChanInitRngGuardband_Type()
)
docsIf31CmtsUsOfdmaChanInitRngGuardband.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanInitRngGuardband.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanInitRngGuardband.setUnits("Hz")
_DocsIf31CmtsUsOfdmaChanInitRngNumSubcarriers_Type = Unsigned32
_DocsIf31CmtsUsOfdmaChanInitRngNumSubcarriers_Object = MibTableColumn
docsIf31CmtsUsOfdmaChanInitRngNumSubcarriers = _DocsIf31CmtsUsOfdmaChanInitRngNumSubcarriers_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 23, 1, 15),
    _DocsIf31CmtsUsOfdmaChanInitRngNumSubcarriers_Type()
)
docsIf31CmtsUsOfdmaChanInitRngNumSubcarriers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanInitRngNumSubcarriers.setStatus("current")
_DocsIf31CmtsUsOfdmaChanInitRngPreambleLen_Type = Unsigned32
_DocsIf31CmtsUsOfdmaChanInitRngPreambleLen_Object = MibTableColumn
docsIf31CmtsUsOfdmaChanInitRngPreambleLen = _DocsIf31CmtsUsOfdmaChanInitRngPreambleLen_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 23, 1, 16),
    _DocsIf31CmtsUsOfdmaChanInitRngPreambleLen_Type()
)
docsIf31CmtsUsOfdmaChanInitRngPreambleLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanInitRngPreambleLen.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanInitRngPreambleLen.setUnits("bits")
_DocsIf31CmtsUsOfdmaChanProvAttribMask_Type = AttributeMask
_DocsIf31CmtsUsOfdmaChanProvAttribMask_Object = MibTableColumn
docsIf31CmtsUsOfdmaChanProvAttribMask = _DocsIf31CmtsUsOfdmaChanProvAttribMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 23, 1, 17),
    _DocsIf31CmtsUsOfdmaChanProvAttribMask_Type()
)
docsIf31CmtsUsOfdmaChanProvAttribMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanProvAttribMask.setStatus("current")


class _DocsIf31CmtsUsOfdmaChanTxBackoffStart_Type(Integer32):
    """Custom type docsIf31CmtsUsOfdmaChanTxBackoffStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_DocsIf31CmtsUsOfdmaChanTxBackoffStart_Type.__name__ = "Integer32"
_DocsIf31CmtsUsOfdmaChanTxBackoffStart_Object = MibTableColumn
docsIf31CmtsUsOfdmaChanTxBackoffStart = _DocsIf31CmtsUsOfdmaChanTxBackoffStart_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 23, 1, 18),
    _DocsIf31CmtsUsOfdmaChanTxBackoffStart_Type()
)
docsIf31CmtsUsOfdmaChanTxBackoffStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanTxBackoffStart.setStatus("current")


class _DocsIf31CmtsUsOfdmaChanTxBackoffEnd_Type(Integer32):
    """Custom type docsIf31CmtsUsOfdmaChanTxBackoffEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_DocsIf31CmtsUsOfdmaChanTxBackoffEnd_Type.__name__ = "Integer32"
_DocsIf31CmtsUsOfdmaChanTxBackoffEnd_Object = MibTableColumn
docsIf31CmtsUsOfdmaChanTxBackoffEnd = _DocsIf31CmtsUsOfdmaChanTxBackoffEnd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 23, 1, 19),
    _DocsIf31CmtsUsOfdmaChanTxBackoffEnd_Type()
)
docsIf31CmtsUsOfdmaChanTxBackoffEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanTxBackoffEnd.setStatus("current")


class _DocsIf31CmtsUsOfdmaChanRangingBackoffStart_Type(Integer32):
    """Custom type docsIf31CmtsUsOfdmaChanRangingBackoffStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_DocsIf31CmtsUsOfdmaChanRangingBackoffStart_Type.__name__ = "Integer32"
_DocsIf31CmtsUsOfdmaChanRangingBackoffStart_Object = MibTableColumn
docsIf31CmtsUsOfdmaChanRangingBackoffStart = _DocsIf31CmtsUsOfdmaChanRangingBackoffStart_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 23, 1, 20),
    _DocsIf31CmtsUsOfdmaChanRangingBackoffStart_Type()
)
docsIf31CmtsUsOfdmaChanRangingBackoffStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanRangingBackoffStart.setStatus("current")


class _DocsIf31CmtsUsOfdmaChanRangingBackoffEnd_Type(Integer32):
    """Custom type docsIf31CmtsUsOfdmaChanRangingBackoffEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_DocsIf31CmtsUsOfdmaChanRangingBackoffEnd_Type.__name__ = "Integer32"
_DocsIf31CmtsUsOfdmaChanRangingBackoffEnd_Object = MibTableColumn
docsIf31CmtsUsOfdmaChanRangingBackoffEnd = _DocsIf31CmtsUsOfdmaChanRangingBackoffEnd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 23, 1, 21),
    _DocsIf31CmtsUsOfdmaChanRangingBackoffEnd_Type()
)
docsIf31CmtsUsOfdmaChanRangingBackoffEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanRangingBackoffEnd.setStatus("current")


class _DocsIf31CmtsUsOfdmaChanUtilization_Type(Unsigned32):
    """Custom type docsIf31CmtsUsOfdmaChanUtilization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DocsIf31CmtsUsOfdmaChanUtilization_Type.__name__ = "Unsigned32"
_DocsIf31CmtsUsOfdmaChanUtilization_Object = MibTableColumn
docsIf31CmtsUsOfdmaChanUtilization = _DocsIf31CmtsUsOfdmaChanUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 23, 1, 22),
    _DocsIf31CmtsUsOfdmaChanUtilization_Type()
)
docsIf31CmtsUsOfdmaChanUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanUtilization.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanUtilization.setUnits("percent")
_DocsIf31CmtsUsOfdmaChanId_Type = Integer32
_DocsIf31CmtsUsOfdmaChanId_Object = MibTableColumn
docsIf31CmtsUsOfdmaChanId = _DocsIf31CmtsUsOfdmaChanId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 23, 1, 23),
    _DocsIf31CmtsUsOfdmaChanId_Type()
)
docsIf31CmtsUsOfdmaChanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaChanId.setStatus("current")
_DocsIf31CmtsUsOfdmaDataIucStatsTable_Object = MibTable
docsIf31CmtsUsOfdmaDataIucStatsTable = _DocsIf31CmtsUsOfdmaDataIucStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 24)
)
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaDataIucStatsTable.setStatus("current")
_DocsIf31CmtsUsOfdmaDataIucStatsEntry_Object = MibTableRow
docsIf31CmtsUsOfdmaDataIucStatsEntry = _DocsIf31CmtsUsOfdmaDataIucStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 24, 1)
)
docsIf31CmtsUsOfdmaDataIucStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaDataIucStatsDataIuc"),
)
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaDataIucStatsEntry.setStatus("current")
_DocsIf31CmtsUsOfdmaDataIucStatsDataIuc_Type = Unsigned32
_DocsIf31CmtsUsOfdmaDataIucStatsDataIuc_Object = MibTableColumn
docsIf31CmtsUsOfdmaDataIucStatsDataIuc = _DocsIf31CmtsUsOfdmaDataIucStatsDataIuc_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 24, 1, 1),
    _DocsIf31CmtsUsOfdmaDataIucStatsDataIuc_Type()
)
docsIf31CmtsUsOfdmaDataIucStatsDataIuc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaDataIucStatsDataIuc.setStatus("current")
_DocsIf31CmtsUsOfdmaDataIucStatsMinislotPilotPattern_Type = Unsigned32
_DocsIf31CmtsUsOfdmaDataIucStatsMinislotPilotPattern_Object = MibTableColumn
docsIf31CmtsUsOfdmaDataIucStatsMinislotPilotPattern = _DocsIf31CmtsUsOfdmaDataIucStatsMinislotPilotPattern_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 24, 1, 2),
    _DocsIf31CmtsUsOfdmaDataIucStatsMinislotPilotPattern_Type()
)
docsIf31CmtsUsOfdmaDataIucStatsMinislotPilotPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaDataIucStatsMinislotPilotPattern.setStatus("current")
_DocsIf31CmtsUsOfdmaDataIucStatsMinislotModulation_Type = UsOfdmaModulationType
_DocsIf31CmtsUsOfdmaDataIucStatsMinislotModulation_Object = MibTableColumn
docsIf31CmtsUsOfdmaDataIucStatsMinislotModulation = _DocsIf31CmtsUsOfdmaDataIucStatsMinislotModulation_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 24, 1, 3),
    _DocsIf31CmtsUsOfdmaDataIucStatsMinislotModulation_Type()
)
docsIf31CmtsUsOfdmaDataIucStatsMinislotModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaDataIucStatsMinislotModulation.setStatus("current")
_DocsIf31CmtsUsOfdmaDataIucStatsTotalCodewords_Type = Counter64
_DocsIf31CmtsUsOfdmaDataIucStatsTotalCodewords_Object = MibTableColumn
docsIf31CmtsUsOfdmaDataIucStatsTotalCodewords = _DocsIf31CmtsUsOfdmaDataIucStatsTotalCodewords_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 24, 1, 4),
    _DocsIf31CmtsUsOfdmaDataIucStatsTotalCodewords_Type()
)
docsIf31CmtsUsOfdmaDataIucStatsTotalCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaDataIucStatsTotalCodewords.setStatus("current")
_DocsIf31CmtsUsOfdmaDataIucStatsCorrectedCodewords_Type = Counter64
_DocsIf31CmtsUsOfdmaDataIucStatsCorrectedCodewords_Object = MibTableColumn
docsIf31CmtsUsOfdmaDataIucStatsCorrectedCodewords = _DocsIf31CmtsUsOfdmaDataIucStatsCorrectedCodewords_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 24, 1, 5),
    _DocsIf31CmtsUsOfdmaDataIucStatsCorrectedCodewords_Type()
)
docsIf31CmtsUsOfdmaDataIucStatsCorrectedCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaDataIucStatsCorrectedCodewords.setStatus("current")
_DocsIf31CmtsUsOfdmaDataIucStatsUnreliableCodewords_Type = Counter64
_DocsIf31CmtsUsOfdmaDataIucStatsUnreliableCodewords_Object = MibTableColumn
docsIf31CmtsUsOfdmaDataIucStatsUnreliableCodewords = _DocsIf31CmtsUsOfdmaDataIucStatsUnreliableCodewords_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 24, 1, 6),
    _DocsIf31CmtsUsOfdmaDataIucStatsUnreliableCodewords_Type()
)
docsIf31CmtsUsOfdmaDataIucStatsUnreliableCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaDataIucStatsUnreliableCodewords.setStatus("current")
_DocsIf31CmtsUsOfdmaDataIucStatsInOctets_Type = Counter64
_DocsIf31CmtsUsOfdmaDataIucStatsInOctets_Object = MibTableColumn
docsIf31CmtsUsOfdmaDataIucStatsInOctets = _DocsIf31CmtsUsOfdmaDataIucStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 24, 1, 7),
    _DocsIf31CmtsUsOfdmaDataIucStatsInOctets_Type()
)
docsIf31CmtsUsOfdmaDataIucStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaDataIucStatsInOctets.setStatus("current")
_DocsIf31CmtsUsOfdmaDataIucStatsCtrDiscontinuityTime_Type = TimeStamp
_DocsIf31CmtsUsOfdmaDataIucStatsCtrDiscontinuityTime_Object = MibTableColumn
docsIf31CmtsUsOfdmaDataIucStatsCtrDiscontinuityTime = _DocsIf31CmtsUsOfdmaDataIucStatsCtrDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 24, 1, 8),
    _DocsIf31CmtsUsOfdmaDataIucStatsCtrDiscontinuityTime_Type()
)
docsIf31CmtsUsOfdmaDataIucStatsCtrDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaDataIucStatsCtrDiscontinuityTime.setStatus("current")
_DocsIf31CmtsUsOfdmaDataIucStatsAssignedCmCt_Type = Unsigned32
_DocsIf31CmtsUsOfdmaDataIucStatsAssignedCmCt_Object = MibTableColumn
docsIf31CmtsUsOfdmaDataIucStatsAssignedCmCt = _DocsIf31CmtsUsOfdmaDataIucStatsAssignedCmCt_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 24, 1, 9),
    _DocsIf31CmtsUsOfdmaDataIucStatsAssignedCmCt_Type()
)
docsIf31CmtsUsOfdmaDataIucStatsAssignedCmCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaDataIucStatsAssignedCmCt.setStatus("current")
_DocsIf31CmtsUsOfdmaDataIucDetailStatusTable_Object = MibTable
docsIf31CmtsUsOfdmaDataIucDetailStatusTable = _DocsIf31CmtsUsOfdmaDataIucDetailStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 25)
)
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaDataIucDetailStatusTable.setStatus("current")
_DocsIf31CmtsUsOfdmaDataIucDetailStatusEntry_Object = MibTableRow
docsIf31CmtsUsOfdmaDataIucDetailStatusEntry = _DocsIf31CmtsUsOfdmaDataIucDetailStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 25, 1)
)
docsIf31CmtsUsOfdmaDataIucDetailStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaDataIucStatsDataIuc"),
    (0, "DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaDataIucDetailStatusLowerFreq"),
)
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaDataIucDetailStatusEntry.setStatus("current")
_DocsIf31CmtsUsOfdmaDataIucDetailStatusLowerFreq_Type = Unsigned32
_DocsIf31CmtsUsOfdmaDataIucDetailStatusLowerFreq_Object = MibTableColumn
docsIf31CmtsUsOfdmaDataIucDetailStatusLowerFreq = _DocsIf31CmtsUsOfdmaDataIucDetailStatusLowerFreq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 25, 1, 1),
    _DocsIf31CmtsUsOfdmaDataIucDetailStatusLowerFreq_Type()
)
docsIf31CmtsUsOfdmaDataIucDetailStatusLowerFreq.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaDataIucDetailStatusLowerFreq.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaDataIucDetailStatusLowerFreq.setUnits("Hz")
_DocsIf31CmtsUsOfdmaDataIucDetailStatusUpperFreq_Type = Unsigned32
_DocsIf31CmtsUsOfdmaDataIucDetailStatusUpperFreq_Object = MibTableColumn
docsIf31CmtsUsOfdmaDataIucDetailStatusUpperFreq = _DocsIf31CmtsUsOfdmaDataIucDetailStatusUpperFreq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 25, 1, 2),
    _DocsIf31CmtsUsOfdmaDataIucDetailStatusUpperFreq_Type()
)
docsIf31CmtsUsOfdmaDataIucDetailStatusUpperFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaDataIucDetailStatusUpperFreq.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaDataIucDetailStatusUpperFreq.setUnits("Hz")
_DocsIf31CmtsUsOfdmaDataIucDetailStatusMinislotPilotPattern_Type = Unsigned32
_DocsIf31CmtsUsOfdmaDataIucDetailStatusMinislotPilotPattern_Object = MibTableColumn
docsIf31CmtsUsOfdmaDataIucDetailStatusMinislotPilotPattern = _DocsIf31CmtsUsOfdmaDataIucDetailStatusMinislotPilotPattern_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 25, 1, 3),
    _DocsIf31CmtsUsOfdmaDataIucDetailStatusMinislotPilotPattern_Type()
)
docsIf31CmtsUsOfdmaDataIucDetailStatusMinislotPilotPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaDataIucDetailStatusMinislotPilotPattern.setStatus("current")
_DocsIf31CmtsUsOfdmaDataIucDetailStatusMinislotModulation_Type = UsOfdmaModulationType
_DocsIf31CmtsUsOfdmaDataIucDetailStatusMinislotModulation_Object = MibTableColumn
docsIf31CmtsUsOfdmaDataIucDetailStatusMinislotModulation = _DocsIf31CmtsUsOfdmaDataIucDetailStatusMinislotModulation_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 25, 1, 4),
    _DocsIf31CmtsUsOfdmaDataIucDetailStatusMinislotModulation_Type()
)
docsIf31CmtsUsOfdmaDataIucDetailStatusMinislotModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaDataIucDetailStatusMinislotModulation.setStatus("current")
_DocsIf31CmtsUsOfdmaRangingIucStatusTable_Object = MibTable
docsIf31CmtsUsOfdmaRangingIucStatusTable = _DocsIf31CmtsUsOfdmaRangingIucStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 26)
)
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaRangingIucStatusTable.setStatus("current")
_DocsIf31CmtsUsOfdmaRangingIucStatusEntry_Object = MibTableRow
docsIf31CmtsUsOfdmaRangingIucStatusEntry = _DocsIf31CmtsUsOfdmaRangingIucStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 26, 1)
)
docsIf31CmtsUsOfdmaRangingIucStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaRangingIucStatusIuc"),
)
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaRangingIucStatusEntry.setStatus("current")
_DocsIf31CmtsUsOfdmaRangingIucStatusIuc_Type = Unsigned32
_DocsIf31CmtsUsOfdmaRangingIucStatusIuc_Object = MibTableColumn
docsIf31CmtsUsOfdmaRangingIucStatusIuc = _DocsIf31CmtsUsOfdmaRangingIucStatusIuc_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 26, 1, 1),
    _DocsIf31CmtsUsOfdmaRangingIucStatusIuc_Type()
)
docsIf31CmtsUsOfdmaRangingIucStatusIuc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaRangingIucStatusIuc.setStatus("current")
_DocsIf31CmtsUsOfdmaRangingIucStatusGuardband_Type = Unsigned32
_DocsIf31CmtsUsOfdmaRangingIucStatusGuardband_Object = MibTableColumn
docsIf31CmtsUsOfdmaRangingIucStatusGuardband = _DocsIf31CmtsUsOfdmaRangingIucStatusGuardband_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 26, 1, 2),
    _DocsIf31CmtsUsOfdmaRangingIucStatusGuardband_Type()
)
docsIf31CmtsUsOfdmaRangingIucStatusGuardband.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaRangingIucStatusGuardband.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaRangingIucStatusGuardband.setUnits("Hz")
_DocsIf31CmtsUsOfdmaRangingIucStatusNumSubcarriers_Type = Unsigned32
_DocsIf31CmtsUsOfdmaRangingIucStatusNumSubcarriers_Object = MibTableColumn
docsIf31CmtsUsOfdmaRangingIucStatusNumSubcarriers = _DocsIf31CmtsUsOfdmaRangingIucStatusNumSubcarriers_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 26, 1, 3),
    _DocsIf31CmtsUsOfdmaRangingIucStatusNumSubcarriers_Type()
)
docsIf31CmtsUsOfdmaRangingIucStatusNumSubcarriers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaRangingIucStatusNumSubcarriers.setStatus("current")
_DocsIf31CmtsDsOfdmSubcarrierTypeTable_Object = MibTable
docsIf31CmtsDsOfdmSubcarrierTypeTable = _DocsIf31CmtsDsOfdmSubcarrierTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 27)
)
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmSubcarrierTypeTable.setStatus("current")
_DocsIf31CmtsDsOfdmSubcarrierTypeEntry_Object = MibTableRow
docsIf31CmtsDsOfdmSubcarrierTypeEntry = _DocsIf31CmtsDsOfdmSubcarrierTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 27, 1)
)
docsIf31CmtsDsOfdmSubcarrierTypeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF31-MIB", "docsIf31CmtsDsOfdmSubcarrierTypeStartSubcarrierId"),
)
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmSubcarrierTypeEntry.setStatus("current")
_DocsIf31CmtsDsOfdmSubcarrierTypeStartSubcarrierId_Type = Unsigned32
_DocsIf31CmtsDsOfdmSubcarrierTypeStartSubcarrierId_Object = MibTableColumn
docsIf31CmtsDsOfdmSubcarrierTypeStartSubcarrierId = _DocsIf31CmtsDsOfdmSubcarrierTypeStartSubcarrierId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 27, 1, 1),
    _DocsIf31CmtsDsOfdmSubcarrierTypeStartSubcarrierId_Type()
)
docsIf31CmtsDsOfdmSubcarrierTypeStartSubcarrierId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmSubcarrierTypeStartSubcarrierId.setStatus("current")
_DocsIf31CmtsDsOfdmSubcarrierTypeEndSubcarrierId_Type = Unsigned32
_DocsIf31CmtsDsOfdmSubcarrierTypeEndSubcarrierId_Object = MibTableColumn
docsIf31CmtsDsOfdmSubcarrierTypeEndSubcarrierId = _DocsIf31CmtsDsOfdmSubcarrierTypeEndSubcarrierId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 27, 1, 2),
    _DocsIf31CmtsDsOfdmSubcarrierTypeEndSubcarrierId_Type()
)
docsIf31CmtsDsOfdmSubcarrierTypeEndSubcarrierId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmSubcarrierTypeEndSubcarrierId.setStatus("current")


class _DocsIf31CmtsDsOfdmSubcarrierTypeSubcarrierType_Type(Integer32):
    """Custom type docsIf31CmtsDsOfdmSubcarrierTypeSubcarrierType based on Integer32"""
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
        *(("continuousPilot", 3),
          ("data", 1),
          ("excluded", 4),
          ("plc", 2))
    )


_DocsIf31CmtsDsOfdmSubcarrierTypeSubcarrierType_Type.__name__ = "Integer32"
_DocsIf31CmtsDsOfdmSubcarrierTypeSubcarrierType_Object = MibTableColumn
docsIf31CmtsDsOfdmSubcarrierTypeSubcarrierType = _DocsIf31CmtsDsOfdmSubcarrierTypeSubcarrierType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 27, 1, 3),
    _DocsIf31CmtsDsOfdmSubcarrierTypeSubcarrierType_Type()
)
docsIf31CmtsDsOfdmSubcarrierTypeSubcarrierType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsDsOfdmSubcarrierTypeSubcarrierType.setStatus("current")
_DocsIf31CmtsUsOfdmaSubcarrierTypeTable_Object = MibTable
docsIf31CmtsUsOfdmaSubcarrierTypeTable = _DocsIf31CmtsUsOfdmaSubcarrierTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 28)
)
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaSubcarrierTypeTable.setStatus("current")
_DocsIf31CmtsUsOfdmaSubcarrierTypeEntry_Object = MibTableRow
docsIf31CmtsUsOfdmaSubcarrierTypeEntry = _DocsIf31CmtsUsOfdmaSubcarrierTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 28, 1)
)
docsIf31CmtsUsOfdmaSubcarrierTypeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaSubcarrierTypeStartSubcarrierId"),
)
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaSubcarrierTypeEntry.setStatus("current")
_DocsIf31CmtsUsOfdmaSubcarrierTypeStartSubcarrierId_Type = Unsigned32
_DocsIf31CmtsUsOfdmaSubcarrierTypeStartSubcarrierId_Object = MibTableColumn
docsIf31CmtsUsOfdmaSubcarrierTypeStartSubcarrierId = _DocsIf31CmtsUsOfdmaSubcarrierTypeStartSubcarrierId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 28, 1, 1),
    _DocsIf31CmtsUsOfdmaSubcarrierTypeStartSubcarrierId_Type()
)
docsIf31CmtsUsOfdmaSubcarrierTypeStartSubcarrierId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaSubcarrierTypeStartSubcarrierId.setStatus("current")
_DocsIf31CmtsUsOfdmaSubcarrierTypeEndSubcarrierId_Type = Unsigned32
_DocsIf31CmtsUsOfdmaSubcarrierTypeEndSubcarrierId_Object = MibTableColumn
docsIf31CmtsUsOfdmaSubcarrierTypeEndSubcarrierId = _DocsIf31CmtsUsOfdmaSubcarrierTypeEndSubcarrierId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 28, 1, 2),
    _DocsIf31CmtsUsOfdmaSubcarrierTypeEndSubcarrierId_Type()
)
docsIf31CmtsUsOfdmaSubcarrierTypeEndSubcarrierId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaSubcarrierTypeEndSubcarrierId.setStatus("current")


class _DocsIf31CmtsUsOfdmaSubcarrierTypeSubcarrierType_Type(Integer32):
    """Custom type docsIf31CmtsUsOfdmaSubcarrierTypeSubcarrierType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("excluded", 2),
          ("unused", 3))
    )


_DocsIf31CmtsUsOfdmaSubcarrierTypeSubcarrierType_Type.__name__ = "Integer32"
_DocsIf31CmtsUsOfdmaSubcarrierTypeSubcarrierType_Object = MibTableColumn
docsIf31CmtsUsOfdmaSubcarrierTypeSubcarrierType = _DocsIf31CmtsUsOfdmaSubcarrierTypeSubcarrierType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 28, 1, 3),
    _DocsIf31CmtsUsOfdmaSubcarrierTypeSubcarrierType_Type()
)
docsIf31CmtsUsOfdmaSubcarrierTypeSubcarrierType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmtsUsOfdmaSubcarrierTypeSubcarrierType.setStatus("current")
_DocsIf31CmStatusTable_Object = MibTable
docsIf31CmStatusTable = _DocsIf31CmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 29)
)
if mibBuilder.loadTexts:
    docsIf31CmStatusTable.setStatus("current")
_DocsIf31CmStatusEntry_Object = MibTableRow
docsIf31CmStatusEntry = _DocsIf31CmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 29, 1)
)
docsIf31CmStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIf31CmStatusEntry.setStatus("current")
_DocsIf31CmStatusEmDlsOperStatus_Type = TruthValue
_DocsIf31CmStatusEmDlsOperStatus_Object = MibTableColumn
docsIf31CmStatusEmDlsOperStatus = _DocsIf31CmStatusEmDlsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 29, 1, 1),
    _DocsIf31CmStatusEmDlsOperStatus_Type()
)
docsIf31CmStatusEmDlsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmStatusEmDlsOperStatus.setStatus("current")
_DocsIf31CmEmDlsCfgTable_Object = MibTable
docsIf31CmEmDlsCfgTable = _DocsIf31CmEmDlsCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 30)
)
if mibBuilder.loadTexts:
    docsIf31CmEmDlsCfgTable.setStatus("current")
_DocsIf31CmEmDlsCfgEntry_Object = MibTableRow
docsIf31CmEmDlsCfgEntry = _DocsIf31CmEmDlsCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 30, 1)
)
docsIf31CmEmDlsCfgEntry.setIndexNames(
    (0, "DOCS-IF31-MIB", "docsIf31CmEmDlsCfgDirection"),
)
if mibBuilder.loadTexts:
    docsIf31CmEmDlsCfgEntry.setStatus("current")
_DocsIf31CmEmDlsCfgDirection_Type = IfDirection
_DocsIf31CmEmDlsCfgDirection_Object = MibTableColumn
docsIf31CmEmDlsCfgDirection = _DocsIf31CmEmDlsCfgDirection_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 30, 1, 1),
    _DocsIf31CmEmDlsCfgDirection_Type()
)
docsIf31CmEmDlsCfgDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf31CmEmDlsCfgDirection.setStatus("current")
_DocsIf31CmEmDlsCfgEntryBitrateThrshld_Type = Unsigned32
_DocsIf31CmEmDlsCfgEntryBitrateThrshld_Object = MibTableColumn
docsIf31CmEmDlsCfgEntryBitrateThrshld = _DocsIf31CmEmDlsCfgEntryBitrateThrshld_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 30, 1, 2),
    _DocsIf31CmEmDlsCfgEntryBitrateThrshld_Type()
)
docsIf31CmEmDlsCfgEntryBitrateThrshld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf31CmEmDlsCfgEntryBitrateThrshld.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmEmDlsCfgEntryBitrateThrshld.setUnits("bps")


class _DocsIf31CmEmDlsCfgEntryTimeThrshld_Type(Unsigned32):
    """Custom type docsIf31CmEmDlsCfgEntryTimeThrshld based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DocsIf31CmEmDlsCfgEntryTimeThrshld_Type.__name__ = "Unsigned32"
_DocsIf31CmEmDlsCfgEntryTimeThrshld_Object = MibTableColumn
docsIf31CmEmDlsCfgEntryTimeThrshld = _DocsIf31CmEmDlsCfgEntryTimeThrshld_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 30, 1, 3),
    _DocsIf31CmEmDlsCfgEntryTimeThrshld_Type()
)
docsIf31CmEmDlsCfgEntryTimeThrshld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf31CmEmDlsCfgEntryTimeThrshld.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmEmDlsCfgEntryTimeThrshld.setUnits("seconds")
_DocsIf31CmEmDlsCfgExitBitrateThrshld_Type = Unsigned32
_DocsIf31CmEmDlsCfgExitBitrateThrshld_Object = MibTableColumn
docsIf31CmEmDlsCfgExitBitrateThrshld = _DocsIf31CmEmDlsCfgExitBitrateThrshld_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 30, 1, 4),
    _DocsIf31CmEmDlsCfgExitBitrateThrshld_Type()
)
docsIf31CmEmDlsCfgExitBitrateThrshld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf31CmEmDlsCfgExitBitrateThrshld.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmEmDlsCfgExitBitrateThrshld.setUnits("bps")


class _DocsIf31CmEmDlsCfgExitTimeThrshld_Type(Unsigned32):
    """Custom type docsIf31CmEmDlsCfgExitTimeThrshld based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DocsIf31CmEmDlsCfgExitTimeThrshld_Type.__name__ = "Unsigned32"
_DocsIf31CmEmDlsCfgExitTimeThrshld_Object = MibTableColumn
docsIf31CmEmDlsCfgExitTimeThrshld = _DocsIf31CmEmDlsCfgExitTimeThrshld_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 30, 1, 5),
    _DocsIf31CmEmDlsCfgExitTimeThrshld_Type()
)
docsIf31CmEmDlsCfgExitTimeThrshld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf31CmEmDlsCfgExitTimeThrshld.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmEmDlsCfgExitTimeThrshld.setUnits("seconds")
_DocsIf31CmUsScQamChanTable_Object = MibTable
docsIf31CmUsScQamChanTable = _DocsIf31CmUsScQamChanTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 31)
)
if mibBuilder.loadTexts:
    docsIf31CmUsScQamChanTable.setStatus("current")
_DocsIf31CmUsScQamChanEntry_Object = MibTableRow
docsIf31CmUsScQamChanEntry = _DocsIf31CmUsScQamChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 31, 1)
)
if mibBuilder.loadTexts:
    docsIf31CmUsScQamChanEntry.setStatus("current")
_DocsIf31CmUsScQamChanTxPsd_Type = Unsigned32
_DocsIf31CmUsScQamChanTxPsd_Object = MibTableColumn
docsIf31CmUsScQamChanTxPsd = _DocsIf31CmUsScQamChanTxPsd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 1, 31, 1, 1),
    _DocsIf31CmUsScQamChanTxPsd_Type()
)
docsIf31CmUsScQamChanTxPsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf31CmUsScQamChanTxPsd.setStatus("current")
if mibBuilder.loadTexts:
    docsIf31CmUsScQamChanTxPsd.setUnits("QuarterdBmV")
_DocsIf31MibConformance_ObjectIdentity = ObjectIdentity
docsIf31MibConformance = _DocsIf31MibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 2)
)
_DocsIf31MibCompliances_ObjectIdentity = ObjectIdentity
docsIf31MibCompliances = _DocsIf31MibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 2, 1)
)
_DocsIf31MibGroups_ObjectIdentity = ObjectIdentity
docsIf31MibGroups = _DocsIf31MibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 2, 2)
)
docsIf3CmtsCmRegStatusEntry.registerAugmentions(
    ("DOCS-IF31-MIB",
     "docsIf31CmtsCmRegStatusEntry")
)
docsIf31CmtsCmRegStatusEntry.setIndexNames(*docsIf3CmtsCmRegStatusEntry.getIndexNames())
docsIfUpstreamChannelEntry.registerAugmentions(
    ("DOCS-IF31-MIB",
     "docsIf31CmUsScQamChanEntry")
)
docsIf31CmUsScQamChanEntry.setIndexNames(*docsIfUpstreamChannelEntry.getIndexNames())

# Managed Objects groups

docsIf31CmtsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 2, 2, 1)
)
docsIf31CmtsGroup.setObjects(
      *(("DOCS-IF31-MIB", "docsIf31DocsisBaseCapability"),
        ("DOCS-IF31-MIB", "docsIf31RxChStatusPrimaryDsIndicator"),
        ("DOCS-IF31-MIB", "docsIf31RxChStatusOfdmProfiles"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmRegStatusAssignedEmIds"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmRegStatusDsProfileIdList"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmRegStatusUsProfileIucList"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmRegStatusTcsPhigh"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmRegStatusTcsDrwTop"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmRegStatusMinUsableDsFreq"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmRegStatusMaxUsableDsFreq"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmRegStatusMaxUsableUsFreq"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmRegStatusPartialSvcState"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmRegStatusPartialChanState"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmUsOfdmaChannelRxPower"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmUsOfdmaChannelMeanRxMer"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmUsOfdmaChannelStdDevRxMer"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmUsOfdmaChannelRxMerThreshold"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmUsOfdmaChannelThresholdRxMerValue"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmUsOfdmaChannelThresholdRxMerHighestFreq"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmUsOfdmaChannelMicroreflections"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmUsOfdmaChannelHighResolutionTimingOffset"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmUsOfdmaChannelIsMuted"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmUsOfdmaChannelRangingStatus"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmUsOfdmaChannelCurPartialSvcReasonCode"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmUsOfdmaChannelLastPartialSvcTime"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmUsOfdmaChannelLastPartialSvcReasonCode"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmUsOfdmaChannelNumPartialSvcIncidents"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmUsOfdmaProfileTotalCodewords"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmUsOfdmaProfileCorrectedCodewords"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmUsOfdmaProfileUnreliableCodewords"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmDsOfdmChannelCurPartialSvcReasonCode"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmDsOfdmChannelLastPartialSvcTime"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmDsOfdmChannelLastPartialSvcReasonCode"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmDsOfdmChannelNumPartialSvcIncidents"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmDsOfdmChannelNumPartialChanIncidents"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmDsOfdmProfilePartialChanReasonCode"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmDsOfdmProfileLastPartialChanTime"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmDsOfdmProfileLastPartialChanReasonCode"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmEmStatsEm1x1ModeTotalDuration"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmEmStatsDlsModeTotalDuration"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmEmStatsLastDlsTime"),
        ("DOCS-IF31-MIB", "docsIf31CmtsCmEmStatsDlsWakeupEvents"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmChanChannelId"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmChanLowerBdryFreq"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmChanUpperBdryFreq"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmChanLowerBdryEncompSpectrum"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmChanUpperBdryEncompSpectrum"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmChanPlcFreq"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmChanSubcarrierZeroFreq"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmChanFirstActiveSubcarrierNum"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmChanLastActiveSubcarrierNum"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmChanNumActiveSubcarriers"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmChanSubcarrierSpacing"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmChanLowerGuardbandWidth"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmChanUpperGuardbandWidth"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmChanCyclicPrefix"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmChanRollOffPeriod"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmChanTimeInterleaverDepth"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmChanNumPilots"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmChanPilotScaleFactor"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmChanNcpModulation"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmChanUtilization"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmProfileStatsConfigChangeCt"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmProfileStatsFullChannelSpeed"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmProfileStatsOutOctets"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmProfileStatsOutUnicastOctets"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmProfileStatsOutMulticastOctets"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmProfileStatsOutFrames"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmProfileStatsOutUnicastFrames"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmProfileStatsOutMulticastFrames"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmProfileStatsCtrDiscontinuityTime"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmProfileStatsAssignedCmCt"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmSubcarrierStatusEndId"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmSubcarrierStatusMainModulation"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmSubcarrierStatusSkip"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmSubcarrierStatusSkipModulation"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmChanPowerCenterFrequency"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmChanPowerTxPower"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaChanTemplateIndex"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaChanConfigChangeCt"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaChanTargetRxPower"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaChanLowerBdryFreq"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaChanUpperBdryFreq"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaChanSubcarrierSpacing"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaChanCyclicPrefix"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaChanNumSymbolsPerFrame"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaChanRollOffPeriod"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaChanPreEqEnable"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaChanFineRngGuardband"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaChanFineRngNumSubcarriers"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaChanFineRngPreambleLen"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaChanInitRngGuardband"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaChanInitRngNumSubcarriers"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaChanInitRngPreambleLen"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaChanProvAttribMask"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaChanTxBackoffStart"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaChanTxBackoffEnd"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaChanRangingBackoffStart"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaChanRangingBackoffEnd"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaChanUtilization"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaChanId"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaDataIucStatsMinislotPilotPattern"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaDataIucStatsMinislotModulation"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaDataIucStatsTotalCodewords"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaDataIucStatsCorrectedCodewords"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaDataIucStatsUnreliableCodewords"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaDataIucStatsInOctets"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaDataIucStatsCtrDiscontinuityTime"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaDataIucStatsAssignedCmCt"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaDataIucDetailStatusUpperFreq"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaDataIucDetailStatusMinislotPilotPattern"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaDataIucDetailStatusMinislotModulation"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaRangingIucStatusGuardband"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaRangingIucStatusNumSubcarriers"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmSubcarrierTypeEndSubcarrierId"),
        ("DOCS-IF31-MIB", "docsIf31CmtsDsOfdmSubcarrierTypeSubcarrierType"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaSubcarrierTypeEndSubcarrierId"),
        ("DOCS-IF31-MIB", "docsIf31CmtsUsOfdmaSubcarrierTypeSubcarrierType"))
)
if mibBuilder.loadTexts:
    docsIf31CmtsGroup.setStatus("current")

docsIf31CmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 2, 2, 2)
)
docsIf31CmGroup.setObjects(
      *(("DOCS-IF31-MIB", "docsIf31DocsisBaseCapability"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmChanChannelId"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmChanChanIndicator"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmChanSubcarrierZeroFreq"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmChanFirstActiveSubcarrierNum"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmChanLastActiveSubcarrierNum"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmChanNumActiveSubcarriers"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmChanSubcarrierSpacing"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmChanCyclicPrefix"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmChanRollOffPeriod"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmChanPlcFreq"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmChanNumPilots"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmChanTimeInterleaverDepth"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmChanPlcTotalCodewords"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmChanPlcUnreliableCodewords"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmChanNcpTotalFields"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmChanNcpFieldCrcFailures"),
        ("DOCS-IF31-MIB", "docsIf31CmEmDlsStatsNumberTimesCrossedBelowUsEntryThrshlds"),
        ("DOCS-IF31-MIB", "docsIf31CmEmDlsStatsNumberTimesCrossedBelowDsEntryThrshlds"),
        ("DOCS-IF31-MIB", "docsIf31CmEmDlsStatsTotalDuration"),
        ("DOCS-IF31-MIB", "docsIf31CmEmDlsStatsTotalDurationBelowUsThrshlds"),
        ("DOCS-IF31-MIB", "docsIf31CmEmDlsStatsTotalDurationBelowDsThrshlds"),
        ("DOCS-IF31-MIB", "docsIf31CmEmDlsStatsTotalDurationBelowUsDsThrshlds"),
        ("DOCS-IF31-MIB", "docsIf31CmEmDlsStatsNumSleepLatencyTriggers"),
        ("DOCS-IF31-MIB", "docsIf31CmEmDlsStatsNumSleepByteCtTriggers"),
        ("DOCS-IF31-MIB", "docsIf31CmEmDlsStatusAssignedEmIds"),
        ("DOCS-IF31-MIB", "docsIf31CmEmDlsStatusReceiveTimer"),
        ("DOCS-IF31-MIB", "docsIf31CmEmDlsStatusMaxSleepLatency"),
        ("DOCS-IF31-MIB", "docsIf31CmEmDlsStatusMaxSleepBytes"),
        ("DOCS-IF31-MIB", "docsIf31CmSystemCfgStateDiplexerCapability"),
        ("DOCS-IF31-MIB", "docsIf31CmSystemCfgStateDiplexerCfgBandEdge"),
        ("DOCS-IF31-MIB", "docsIf31CmSystemCfgStateDiplexerDsLowerCapability"),
        ("DOCS-IF31-MIB", "docsIf31CmSystemCfgStateDiplexerCfgDsLowerBandEdge"),
        ("DOCS-IF31-MIB", "docsIf31CmSystemCfgStateDiplexerDsUpperCapability"),
        ("DOCS-IF31-MIB", "docsIf31CmSystemCfgStateDiplexerCfgDsUpperBandEdge"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmProfileStatsConfigChangeCt"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmProfileStatsTotalCodewords"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmProfileStatsCorrectedCodewords"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmProfileStatsUncorrectableCodewords"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmProfileStatsInOctets"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmProfileStatsInUnicastOctets"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmProfileStatsInMulticastOctets"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmProfileStatsInFrames"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmProfileStatsInUnicastFrames"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmProfileStatsInMulticastFrames"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmProfileStatsInFrameCrcFailures"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmProfileStatsCtrDiscontinuityTime"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmChannelPowerCenterFrequency"),
        ("DOCS-IF31-MIB", "docsIf31CmDsOfdmChannelPowerRxPower"),
        ("DOCS-IF31-MIB", "docsIf31CmStatusOfdmaUsT3Timeouts"),
        ("DOCS-IF31-MIB", "docsIf31CmStatusOfdmaUsT4Timeouts"),
        ("DOCS-IF31-MIB", "docsIf31CmStatusOfdmaUsRangingAborteds"),
        ("DOCS-IF31-MIB", "docsIf31CmStatusOfdmaUsT3Exceededs"),
        ("DOCS-IF31-MIB", "docsIf31CmStatusOfdmaUsIsMuted"),
        ("DOCS-IF31-MIB", "docsIf31CmStatusOfdmaUsRangingStatus"),
        ("DOCS-IF31-MIB", "docsIf31CmUsOfdmaChanConfigChangeCt"),
        ("DOCS-IF31-MIB", "docsIf31CmUsOfdmaChanSubcarrierZeroFreq"),
        ("DOCS-IF31-MIB", "docsIf31CmUsOfdmaChanFirstActiveSubcarrierNum"),
        ("DOCS-IF31-MIB", "docsIf31CmUsOfdmaChanLastActiveSubcarrierNum"),
        ("DOCS-IF31-MIB", "docsIf31CmUsOfdmaChanNumActiveSubcarriers"),
        ("DOCS-IF31-MIB", "docsIf31CmUsOfdmaChanSubcarrierSpacing"),
        ("DOCS-IF31-MIB", "docsIf31CmUsOfdmaChanCyclicPrefix"),
        ("DOCS-IF31-MIB", "docsIf31CmUsOfdmaChanRollOffPeriod"),
        ("DOCS-IF31-MIB", "docsIf31CmUsOfdmaChanNumSymbolsPerFrame"),
        ("DOCS-IF31-MIB", "docsIf31CmUsOfdmaChanTxPower"),
        ("DOCS-IF31-MIB", "docsIf31CmUsOfdmaChanPreEqEnabled"),
        ("DOCS-IF31-MIB", "docsIf31CmUsOfdmaChanChannelId"),
        ("DOCS-IF31-MIB", "docsIf31CmUsOfdmaProfileStatsOutOctets"),
        ("DOCS-IF31-MIB", "docsIf31CmUsOfdmaProfileStatsCtrDiscontinuityTime"),
        ("DOCS-IF31-MIB", "docsIf31CmUsOfdmaMinislotCfgStateFirstSubcarrierId"),
        ("DOCS-IF31-MIB", "docsIf31CmUsOfdmaMinislotCfgStateNumConsecutiveMinislots"),
        ("DOCS-IF31-MIB", "docsIf31CmUsOfdmaMinislotCfgStateMinislotPilotPattern"),
        ("DOCS-IF31-MIB", "docsIf31CmUsOfdmaMinislotCfgStateDataSymbolModulation"),
        ("DOCS-IF31-MIB", "docsIf31CmStatusEmDlsOperStatus"),
        ("DOCS-IF31-MIB", "docsIf31CmEmDlsCfgExitBitrateThrshld"),
        ("DOCS-IF31-MIB", "docsIf31CmEmDlsCfgEntryTimeThrshld"),
        ("DOCS-IF31-MIB", "docsIf31CmEmDlsCfgEntryBitrateThrshld"),
        ("DOCS-IF31-MIB", "docsIf31CmEmDlsCfgExitTimeThrshld"),
        ("DOCS-IF31-MIB", "docsIf31CmUsScQamChanTxPsd"))
)
if mibBuilder.loadTexts:
    docsIf31CmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

docsIf31CmtsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 2, 1, 1)
)
if mibBuilder.loadTexts:
    docsIf31CmtsCompliance.setStatus(
        "current"
    )

docsIf31CmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 28, 2, 1, 2)
)
if mibBuilder.loadTexts:
    docsIf31CmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-IF31-MIB",
    **{"ClabsDocsisVersion": ClabsDocsisVersion,
       "EmIdList": EmIdList,
       "SubcarrierSpacingType": SubcarrierSpacingType,
       "PrimaryDsIndicatorType": PrimaryDsIndicatorType,
       "OfdmProfiles": OfdmProfiles,
       "DsOfdmCyclicPrefix": DsOfdmCyclicPrefix,
       "UsOfdmaCyclicPrefix": UsOfdmaCyclicPrefix,
       "DsOfdmRollOffPeriod": DsOfdmRollOffPeriod,
       "UsOfdmaRollOffPeriod": UsOfdmaRollOffPeriod,
       "TimeInterleaverDepth": TimeInterleaverDepth,
       "DsOfdmModulationType": DsOfdmModulationType,
       "UsOfdmaModulationType": UsOfdmaModulationType,
       "PartialChannelType": PartialChannelType,
       "PartialServiceType": PartialServiceType,
       "PartialChanReasonType": PartialChanReasonType,
       "PartialSvcReasonType": PartialSvcReasonType,
       "HundredthdBmV": HundredthdBmV,
       "HundredthdB": HundredthdB,
       "docsIf31Mib": docsIf31Mib,
       "docsIf31Notifications": docsIf31Notifications,
       "docsIf31MibObjects": docsIf31MibObjects,
       "docsIf31DocsisBaseCapability": docsIf31DocsisBaseCapability,
       "docsIf31RxChStatusTable": docsIf31RxChStatusTable,
       "docsIf31RxChStatusEntry": docsIf31RxChStatusEntry,
       "docsIf31RxChStatusPrimaryDsIndicator": docsIf31RxChStatusPrimaryDsIndicator,
       "docsIf31RxChStatusOfdmProfiles": docsIf31RxChStatusOfdmProfiles,
       "docsIf31CmtsCmRegStatusTable": docsIf31CmtsCmRegStatusTable,
       "docsIf31CmtsCmRegStatusEntry": docsIf31CmtsCmRegStatusEntry,
       "docsIf31CmtsCmRegStatusAssignedEmIds": docsIf31CmtsCmRegStatusAssignedEmIds,
       "docsIf31CmtsCmRegStatusDsProfileIdList": docsIf31CmtsCmRegStatusDsProfileIdList,
       "docsIf31CmtsCmRegStatusUsProfileIucList": docsIf31CmtsCmRegStatusUsProfileIucList,
       "docsIf31CmtsCmRegStatusTcsPhigh": docsIf31CmtsCmRegStatusTcsPhigh,
       "docsIf31CmtsCmRegStatusTcsDrwTop": docsIf31CmtsCmRegStatusTcsDrwTop,
       "docsIf31CmtsCmRegStatusMinUsableDsFreq": docsIf31CmtsCmRegStatusMinUsableDsFreq,
       "docsIf31CmtsCmRegStatusMaxUsableDsFreq": docsIf31CmtsCmRegStatusMaxUsableDsFreq,
       "docsIf31CmtsCmRegStatusMaxUsableUsFreq": docsIf31CmtsCmRegStatusMaxUsableUsFreq,
       "docsIf31CmtsCmRegStatusPartialSvcState": docsIf31CmtsCmRegStatusPartialSvcState,
       "docsIf31CmtsCmRegStatusPartialChanState": docsIf31CmtsCmRegStatusPartialChanState,
       "docsIf31CmtsCmUsOfdmaChannelStatusTable": docsIf31CmtsCmUsOfdmaChannelStatusTable,
       "docsIf31CmtsCmUsOfdmaChannelStatusEntry": docsIf31CmtsCmUsOfdmaChannelStatusEntry,
       "docsIf31CmtsCmUsOfdmaChannelRxPower": docsIf31CmtsCmUsOfdmaChannelRxPower,
       "docsIf31CmtsCmUsOfdmaChannelMeanRxMer": docsIf31CmtsCmUsOfdmaChannelMeanRxMer,
       "docsIf31CmtsCmUsOfdmaChannelStdDevRxMer": docsIf31CmtsCmUsOfdmaChannelStdDevRxMer,
       "docsIf31CmtsCmUsOfdmaChannelRxMerThreshold": docsIf31CmtsCmUsOfdmaChannelRxMerThreshold,
       "docsIf31CmtsCmUsOfdmaChannelThresholdRxMerValue": docsIf31CmtsCmUsOfdmaChannelThresholdRxMerValue,
       "docsIf31CmtsCmUsOfdmaChannelThresholdRxMerHighestFreq": docsIf31CmtsCmUsOfdmaChannelThresholdRxMerHighestFreq,
       "docsIf31CmtsCmUsOfdmaChannelMicroreflections": docsIf31CmtsCmUsOfdmaChannelMicroreflections,
       "docsIf31CmtsCmUsOfdmaChannelHighResolutionTimingOffset": docsIf31CmtsCmUsOfdmaChannelHighResolutionTimingOffset,
       "docsIf31CmtsCmUsOfdmaChannelIsMuted": docsIf31CmtsCmUsOfdmaChannelIsMuted,
       "docsIf31CmtsCmUsOfdmaChannelRangingStatus": docsIf31CmtsCmUsOfdmaChannelRangingStatus,
       "docsIf31CmtsCmUsOfdmaChannelCurPartialSvcReasonCode": docsIf31CmtsCmUsOfdmaChannelCurPartialSvcReasonCode,
       "docsIf31CmtsCmUsOfdmaChannelLastPartialSvcTime": docsIf31CmtsCmUsOfdmaChannelLastPartialSvcTime,
       "docsIf31CmtsCmUsOfdmaChannelLastPartialSvcReasonCode": docsIf31CmtsCmUsOfdmaChannelLastPartialSvcReasonCode,
       "docsIf31CmtsCmUsOfdmaChannelNumPartialSvcIncidents": docsIf31CmtsCmUsOfdmaChannelNumPartialSvcIncidents,
       "docsIf31CmtsCmUsOfdmaProfileStatusTable": docsIf31CmtsCmUsOfdmaProfileStatusTable,
       "docsIf31CmtsCmUsOfdmaProfileStatusEntry": docsIf31CmtsCmUsOfdmaProfileStatusEntry,
       "docsIf31CmtsCmUsOfdmaProfileTotalCodewords": docsIf31CmtsCmUsOfdmaProfileTotalCodewords,
       "docsIf31CmtsCmUsOfdmaProfileCorrectedCodewords": docsIf31CmtsCmUsOfdmaProfileCorrectedCodewords,
       "docsIf31CmtsCmUsOfdmaProfileUnreliableCodewords": docsIf31CmtsCmUsOfdmaProfileUnreliableCodewords,
       "docsIf31CmtsCmDsOfdmChannelStatusTable": docsIf31CmtsCmDsOfdmChannelStatusTable,
       "docsIf31CmtsCmDsOfdmChannelStatusEntry": docsIf31CmtsCmDsOfdmChannelStatusEntry,
       "docsIf31CmtsCmDsOfdmChannelCurPartialSvcReasonCode": docsIf31CmtsCmDsOfdmChannelCurPartialSvcReasonCode,
       "docsIf31CmtsCmDsOfdmChannelLastPartialSvcTime": docsIf31CmtsCmDsOfdmChannelLastPartialSvcTime,
       "docsIf31CmtsCmDsOfdmChannelLastPartialSvcReasonCode": docsIf31CmtsCmDsOfdmChannelLastPartialSvcReasonCode,
       "docsIf31CmtsCmDsOfdmChannelNumPartialSvcIncidents": docsIf31CmtsCmDsOfdmChannelNumPartialSvcIncidents,
       "docsIf31CmtsCmDsOfdmChannelNumPartialChanIncidents": docsIf31CmtsCmDsOfdmChannelNumPartialChanIncidents,
       "docsIf31CmtsCmDsOfdmProfileStatusTable": docsIf31CmtsCmDsOfdmProfileStatusTable,
       "docsIf31CmtsCmDsOfdmProfileStatusEntry": docsIf31CmtsCmDsOfdmProfileStatusEntry,
       "docsIf31CmtsCmDsOfdmProfilePartialChanReasonCode": docsIf31CmtsCmDsOfdmProfilePartialChanReasonCode,
       "docsIf31CmtsCmDsOfdmProfileLastPartialChanTime": docsIf31CmtsCmDsOfdmProfileLastPartialChanTime,
       "docsIf31CmtsCmDsOfdmProfileLastPartialChanReasonCode": docsIf31CmtsCmDsOfdmProfileLastPartialChanReasonCode,
       "docsIf31CmtsCmEmStatsTable": docsIf31CmtsCmEmStatsTable,
       "docsIf31CmtsCmEmStatsEntry": docsIf31CmtsCmEmStatsEntry,
       "docsIf31CmtsCmEmStatsEm1x1ModeTotalDuration": docsIf31CmtsCmEmStatsEm1x1ModeTotalDuration,
       "docsIf31CmtsCmEmStatsDlsModeTotalDuration": docsIf31CmtsCmEmStatsDlsModeTotalDuration,
       "docsIf31CmtsCmEmStatsLastDlsTime": docsIf31CmtsCmEmStatsLastDlsTime,
       "docsIf31CmtsCmEmStatsDlsWakeupEvents": docsIf31CmtsCmEmStatsDlsWakeupEvents,
       "docsIf31CmDsOfdmChanTable": docsIf31CmDsOfdmChanTable,
       "docsIf31CmDsOfdmChanEntry": docsIf31CmDsOfdmChanEntry,
       "docsIf31CmDsOfdmChanChannelId": docsIf31CmDsOfdmChanChannelId,
       "docsIf31CmDsOfdmChanChanIndicator": docsIf31CmDsOfdmChanChanIndicator,
       "docsIf31CmDsOfdmChanSubcarrierZeroFreq": docsIf31CmDsOfdmChanSubcarrierZeroFreq,
       "docsIf31CmDsOfdmChanFirstActiveSubcarrierNum": docsIf31CmDsOfdmChanFirstActiveSubcarrierNum,
       "docsIf31CmDsOfdmChanLastActiveSubcarrierNum": docsIf31CmDsOfdmChanLastActiveSubcarrierNum,
       "docsIf31CmDsOfdmChanNumActiveSubcarriers": docsIf31CmDsOfdmChanNumActiveSubcarriers,
       "docsIf31CmDsOfdmChanSubcarrierSpacing": docsIf31CmDsOfdmChanSubcarrierSpacing,
       "docsIf31CmDsOfdmChanCyclicPrefix": docsIf31CmDsOfdmChanCyclicPrefix,
       "docsIf31CmDsOfdmChanRollOffPeriod": docsIf31CmDsOfdmChanRollOffPeriod,
       "docsIf31CmDsOfdmChanPlcFreq": docsIf31CmDsOfdmChanPlcFreq,
       "docsIf31CmDsOfdmChanNumPilots": docsIf31CmDsOfdmChanNumPilots,
       "docsIf31CmDsOfdmChanTimeInterleaverDepth": docsIf31CmDsOfdmChanTimeInterleaverDepth,
       "docsIf31CmDsOfdmChanPlcTotalCodewords": docsIf31CmDsOfdmChanPlcTotalCodewords,
       "docsIf31CmDsOfdmChanPlcUnreliableCodewords": docsIf31CmDsOfdmChanPlcUnreliableCodewords,
       "docsIf31CmDsOfdmChanNcpTotalFields": docsIf31CmDsOfdmChanNcpTotalFields,
       "docsIf31CmDsOfdmChanNcpFieldCrcFailures": docsIf31CmDsOfdmChanNcpFieldCrcFailures,
       "docsIf31CmDsOfdmProfileStatsTable": docsIf31CmDsOfdmProfileStatsTable,
       "docsIf31CmDsOfdmProfileStatsEntry": docsIf31CmDsOfdmProfileStatsEntry,
       "docsIf31CmDsOfdmProfileStatsProfileId": docsIf31CmDsOfdmProfileStatsProfileId,
       "docsIf31CmDsOfdmProfileStatsConfigChangeCt": docsIf31CmDsOfdmProfileStatsConfigChangeCt,
       "docsIf31CmDsOfdmProfileStatsTotalCodewords": docsIf31CmDsOfdmProfileStatsTotalCodewords,
       "docsIf31CmDsOfdmProfileStatsCorrectedCodewords": docsIf31CmDsOfdmProfileStatsCorrectedCodewords,
       "docsIf31CmDsOfdmProfileStatsUncorrectableCodewords": docsIf31CmDsOfdmProfileStatsUncorrectableCodewords,
       "docsIf31CmDsOfdmProfileStatsInOctets": docsIf31CmDsOfdmProfileStatsInOctets,
       "docsIf31CmDsOfdmProfileStatsInUnicastOctets": docsIf31CmDsOfdmProfileStatsInUnicastOctets,
       "docsIf31CmDsOfdmProfileStatsInMulticastOctets": docsIf31CmDsOfdmProfileStatsInMulticastOctets,
       "docsIf31CmDsOfdmProfileStatsInFrames": docsIf31CmDsOfdmProfileStatsInFrames,
       "docsIf31CmDsOfdmProfileStatsInUnicastFrames": docsIf31CmDsOfdmProfileStatsInUnicastFrames,
       "docsIf31CmDsOfdmProfileStatsInMulticastFrames": docsIf31CmDsOfdmProfileStatsInMulticastFrames,
       "docsIf31CmDsOfdmProfileStatsInFrameCrcFailures": docsIf31CmDsOfdmProfileStatsInFrameCrcFailures,
       "docsIf31CmDsOfdmProfileStatsCtrDiscontinuityTime": docsIf31CmDsOfdmProfileStatsCtrDiscontinuityTime,
       "docsIf31CmDsOfdmChannelPowerTable": docsIf31CmDsOfdmChannelPowerTable,
       "docsIf31CmDsOfdmChannelPowerEntry": docsIf31CmDsOfdmChannelPowerEntry,
       "docsIf31CmDsOfdmChannelBandIndex": docsIf31CmDsOfdmChannelBandIndex,
       "docsIf31CmDsOfdmChannelPowerCenterFrequency": docsIf31CmDsOfdmChannelPowerCenterFrequency,
       "docsIf31CmDsOfdmChannelPowerRxPower": docsIf31CmDsOfdmChannelPowerRxPower,
       "docsIf31CmStatusOfdmaUsTable": docsIf31CmStatusOfdmaUsTable,
       "docsIf31CmStatusOfdmaUsEntry": docsIf31CmStatusOfdmaUsEntry,
       "docsIf31CmStatusOfdmaUsT3Timeouts": docsIf31CmStatusOfdmaUsT3Timeouts,
       "docsIf31CmStatusOfdmaUsT4Timeouts": docsIf31CmStatusOfdmaUsT4Timeouts,
       "docsIf31CmStatusOfdmaUsRangingAborteds": docsIf31CmStatusOfdmaUsRangingAborteds,
       "docsIf31CmStatusOfdmaUsT3Exceededs": docsIf31CmStatusOfdmaUsT3Exceededs,
       "docsIf31CmStatusOfdmaUsIsMuted": docsIf31CmStatusOfdmaUsIsMuted,
       "docsIf31CmStatusOfdmaUsRangingStatus": docsIf31CmStatusOfdmaUsRangingStatus,
       "docsIf31CmUsOfdmaChanTable": docsIf31CmUsOfdmaChanTable,
       "docsIf31CmUsOfdmaChanEntry": docsIf31CmUsOfdmaChanEntry,
       "docsIf31CmUsOfdmaChanConfigChangeCt": docsIf31CmUsOfdmaChanConfigChangeCt,
       "docsIf31CmUsOfdmaChanSubcarrierZeroFreq": docsIf31CmUsOfdmaChanSubcarrierZeroFreq,
       "docsIf31CmUsOfdmaChanFirstActiveSubcarrierNum": docsIf31CmUsOfdmaChanFirstActiveSubcarrierNum,
       "docsIf31CmUsOfdmaChanLastActiveSubcarrierNum": docsIf31CmUsOfdmaChanLastActiveSubcarrierNum,
       "docsIf31CmUsOfdmaChanNumActiveSubcarriers": docsIf31CmUsOfdmaChanNumActiveSubcarriers,
       "docsIf31CmUsOfdmaChanSubcarrierSpacing": docsIf31CmUsOfdmaChanSubcarrierSpacing,
       "docsIf31CmUsOfdmaChanCyclicPrefix": docsIf31CmUsOfdmaChanCyclicPrefix,
       "docsIf31CmUsOfdmaChanRollOffPeriod": docsIf31CmUsOfdmaChanRollOffPeriod,
       "docsIf31CmUsOfdmaChanNumSymbolsPerFrame": docsIf31CmUsOfdmaChanNumSymbolsPerFrame,
       "docsIf31CmUsOfdmaChanTxPower": docsIf31CmUsOfdmaChanTxPower,
       "docsIf31CmUsOfdmaChanPreEqEnabled": docsIf31CmUsOfdmaChanPreEqEnabled,
       "docsIf31CmUsOfdmaChanChannelId": docsIf31CmUsOfdmaChanChannelId,
       "docsIf31CmUsOfdmaProfileStatsTable": docsIf31CmUsOfdmaProfileStatsTable,
       "docsIf31CmUsOfdmaProfileStatsEntry": docsIf31CmUsOfdmaProfileStatsEntry,
       "docsIf31CmUsOfdmaProfileStatsIuc": docsIf31CmUsOfdmaProfileStatsIuc,
       "docsIf31CmUsOfdmaProfileStatsOutOctets": docsIf31CmUsOfdmaProfileStatsOutOctets,
       "docsIf31CmUsOfdmaProfileStatsCtrDiscontinuityTime": docsIf31CmUsOfdmaProfileStatsCtrDiscontinuityTime,
       "docsIf31CmUsOfdmaMinislotCfgStateTable": docsIf31CmUsOfdmaMinislotCfgStateTable,
       "docsIf31CmUsOfdmaMinislotCfgStateEntry": docsIf31CmUsOfdmaMinislotCfgStateEntry,
       "docsIf31CmUsOfdmaMinislotCfgStateStartMinislotNum": docsIf31CmUsOfdmaMinislotCfgStateStartMinislotNum,
       "docsIf31CmUsOfdmaMinislotCfgStateFirstSubcarrierId": docsIf31CmUsOfdmaMinislotCfgStateFirstSubcarrierId,
       "docsIf31CmUsOfdmaMinislotCfgStateNumConsecutiveMinislots": docsIf31CmUsOfdmaMinislotCfgStateNumConsecutiveMinislots,
       "docsIf31CmUsOfdmaMinislotCfgStateMinislotPilotPattern": docsIf31CmUsOfdmaMinislotCfgStateMinislotPilotPattern,
       "docsIf31CmUsOfdmaMinislotCfgStateDataSymbolModulation": docsIf31CmUsOfdmaMinislotCfgStateDataSymbolModulation,
       "docsIf31CmEmDlsStatsTable": docsIf31CmEmDlsStatsTable,
       "docsIf31CmEmDlsStatsEntry": docsIf31CmEmDlsStatsEntry,
       "docsIf31CmEmDlsStatsNumberTimesCrossedBelowUsEntryThrshlds": docsIf31CmEmDlsStatsNumberTimesCrossedBelowUsEntryThrshlds,
       "docsIf31CmEmDlsStatsNumberTimesCrossedBelowDsEntryThrshlds": docsIf31CmEmDlsStatsNumberTimesCrossedBelowDsEntryThrshlds,
       "docsIf31CmEmDlsStatsTotalDuration": docsIf31CmEmDlsStatsTotalDuration,
       "docsIf31CmEmDlsStatsTotalDurationBelowUsThrshlds": docsIf31CmEmDlsStatsTotalDurationBelowUsThrshlds,
       "docsIf31CmEmDlsStatsTotalDurationBelowDsThrshlds": docsIf31CmEmDlsStatsTotalDurationBelowDsThrshlds,
       "docsIf31CmEmDlsStatsTotalDurationBelowUsDsThrshlds": docsIf31CmEmDlsStatsTotalDurationBelowUsDsThrshlds,
       "docsIf31CmEmDlsStatsNumSleepLatencyTriggers": docsIf31CmEmDlsStatsNumSleepLatencyTriggers,
       "docsIf31CmEmDlsStatsNumSleepByteCtTriggers": docsIf31CmEmDlsStatsNumSleepByteCtTriggers,
       "docsIf31CmEmDlsStatusTable": docsIf31CmEmDlsStatusTable,
       "docsIf31CmEmDlsStatusEntry": docsIf31CmEmDlsStatusEntry,
       "docsIf31CmEmDlsStatusAssignedEmIds": docsIf31CmEmDlsStatusAssignedEmIds,
       "docsIf31CmEmDlsStatusReceiveTimer": docsIf31CmEmDlsStatusReceiveTimer,
       "docsIf31CmEmDlsStatusMaxSleepLatency": docsIf31CmEmDlsStatusMaxSleepLatency,
       "docsIf31CmEmDlsStatusMaxSleepBytes": docsIf31CmEmDlsStatusMaxSleepBytes,
       "docsIf31CmSystemCfgState": docsIf31CmSystemCfgState,
       "docsIf31CmSystemCfgStateDiplexerCapability": docsIf31CmSystemCfgStateDiplexerCapability,
       "docsIf31CmSystemCfgStateDiplexerCfgBandEdge": docsIf31CmSystemCfgStateDiplexerCfgBandEdge,
       "docsIf31CmSystemCfgStateDiplexerDsLowerCapability": docsIf31CmSystemCfgStateDiplexerDsLowerCapability,
       "docsIf31CmSystemCfgStateDiplexerCfgDsLowerBandEdge": docsIf31CmSystemCfgStateDiplexerCfgDsLowerBandEdge,
       "docsIf31CmSystemCfgStateDiplexerDsUpperCapability": docsIf31CmSystemCfgStateDiplexerDsUpperCapability,
       "docsIf31CmSystemCfgStateDiplexerCfgDsUpperBandEdge": docsIf31CmSystemCfgStateDiplexerCfgDsUpperBandEdge,
       "docsIf31CmtsDsOfdmChanTable": docsIf31CmtsDsOfdmChanTable,
       "docsIf31CmtsDsOfdmChanEntry": docsIf31CmtsDsOfdmChanEntry,
       "docsIf31CmtsDsOfdmChanChannelId": docsIf31CmtsDsOfdmChanChannelId,
       "docsIf31CmtsDsOfdmChanLowerBdryFreq": docsIf31CmtsDsOfdmChanLowerBdryFreq,
       "docsIf31CmtsDsOfdmChanUpperBdryFreq": docsIf31CmtsDsOfdmChanUpperBdryFreq,
       "docsIf31CmtsDsOfdmChanLowerBdryEncompSpectrum": docsIf31CmtsDsOfdmChanLowerBdryEncompSpectrum,
       "docsIf31CmtsDsOfdmChanUpperBdryEncompSpectrum": docsIf31CmtsDsOfdmChanUpperBdryEncompSpectrum,
       "docsIf31CmtsDsOfdmChanPlcFreq": docsIf31CmtsDsOfdmChanPlcFreq,
       "docsIf31CmtsDsOfdmChanSubcarrierZeroFreq": docsIf31CmtsDsOfdmChanSubcarrierZeroFreq,
       "docsIf31CmtsDsOfdmChanFirstActiveSubcarrierNum": docsIf31CmtsDsOfdmChanFirstActiveSubcarrierNum,
       "docsIf31CmtsDsOfdmChanLastActiveSubcarrierNum": docsIf31CmtsDsOfdmChanLastActiveSubcarrierNum,
       "docsIf31CmtsDsOfdmChanNumActiveSubcarriers": docsIf31CmtsDsOfdmChanNumActiveSubcarriers,
       "docsIf31CmtsDsOfdmChanSubcarrierSpacing": docsIf31CmtsDsOfdmChanSubcarrierSpacing,
       "docsIf31CmtsDsOfdmChanLowerGuardbandWidth": docsIf31CmtsDsOfdmChanLowerGuardbandWidth,
       "docsIf31CmtsDsOfdmChanUpperGuardbandWidth": docsIf31CmtsDsOfdmChanUpperGuardbandWidth,
       "docsIf31CmtsDsOfdmChanCyclicPrefix": docsIf31CmtsDsOfdmChanCyclicPrefix,
       "docsIf31CmtsDsOfdmChanRollOffPeriod": docsIf31CmtsDsOfdmChanRollOffPeriod,
       "docsIf31CmtsDsOfdmChanTimeInterleaverDepth": docsIf31CmtsDsOfdmChanTimeInterleaverDepth,
       "docsIf31CmtsDsOfdmChanNumPilots": docsIf31CmtsDsOfdmChanNumPilots,
       "docsIf31CmtsDsOfdmChanPilotScaleFactor": docsIf31CmtsDsOfdmChanPilotScaleFactor,
       "docsIf31CmtsDsOfdmChanNcpModulation": docsIf31CmtsDsOfdmChanNcpModulation,
       "docsIf31CmtsDsOfdmChanUtilization": docsIf31CmtsDsOfdmChanUtilization,
       "docsIf31CmtsDsOfdmProfileStatsTable": docsIf31CmtsDsOfdmProfileStatsTable,
       "docsIf31CmtsDsOfdmProfileStatsEntry": docsIf31CmtsDsOfdmProfileStatsEntry,
       "docsIf31CmtsDsOfdmProfileStatsProfileId": docsIf31CmtsDsOfdmProfileStatsProfileId,
       "docsIf31CmtsDsOfdmProfileStatsConfigChangeCt": docsIf31CmtsDsOfdmProfileStatsConfigChangeCt,
       "docsIf31CmtsDsOfdmProfileStatsFullChannelSpeed": docsIf31CmtsDsOfdmProfileStatsFullChannelSpeed,
       "docsIf31CmtsDsOfdmProfileStatsOutOctets": docsIf31CmtsDsOfdmProfileStatsOutOctets,
       "docsIf31CmtsDsOfdmProfileStatsOutUnicastOctets": docsIf31CmtsDsOfdmProfileStatsOutUnicastOctets,
       "docsIf31CmtsDsOfdmProfileStatsOutMulticastOctets": docsIf31CmtsDsOfdmProfileStatsOutMulticastOctets,
       "docsIf31CmtsDsOfdmProfileStatsOutFrames": docsIf31CmtsDsOfdmProfileStatsOutFrames,
       "docsIf31CmtsDsOfdmProfileStatsOutUnicastFrames": docsIf31CmtsDsOfdmProfileStatsOutUnicastFrames,
       "docsIf31CmtsDsOfdmProfileStatsOutMulticastFrames": docsIf31CmtsDsOfdmProfileStatsOutMulticastFrames,
       "docsIf31CmtsDsOfdmProfileStatsCtrDiscontinuityTime": docsIf31CmtsDsOfdmProfileStatsCtrDiscontinuityTime,
       "docsIf31CmtsDsOfdmProfileStatsAssignedCmCt": docsIf31CmtsDsOfdmProfileStatsAssignedCmCt,
       "docsIf31CmtsDsOfdmSubcarrierStatusTable": docsIf31CmtsDsOfdmSubcarrierStatusTable,
       "docsIf31CmtsDsOfdmSubcarrierStatusEntry": docsIf31CmtsDsOfdmSubcarrierStatusEntry,
       "docsIf31CmtsDsOfdmSubcarrierStatusStartId": docsIf31CmtsDsOfdmSubcarrierStatusStartId,
       "docsIf31CmtsDsOfdmSubcarrierStatusEndId": docsIf31CmtsDsOfdmSubcarrierStatusEndId,
       "docsIf31CmtsDsOfdmSubcarrierStatusMainModulation": docsIf31CmtsDsOfdmSubcarrierStatusMainModulation,
       "docsIf31CmtsDsOfdmSubcarrierStatusSkip": docsIf31CmtsDsOfdmSubcarrierStatusSkip,
       "docsIf31CmtsDsOfdmSubcarrierStatusSkipModulation": docsIf31CmtsDsOfdmSubcarrierStatusSkipModulation,
       "docsIf31CmtsDsOfdmChanPowerTable": docsIf31CmtsDsOfdmChanPowerTable,
       "docsIf31CmtsDsOfdmChanPowerEntry": docsIf31CmtsDsOfdmChanPowerEntry,
       "docsIf31CmtsDsOfdmChanPowerBandIndex": docsIf31CmtsDsOfdmChanPowerBandIndex,
       "docsIf31CmtsDsOfdmChanPowerCenterFrequency": docsIf31CmtsDsOfdmChanPowerCenterFrequency,
       "docsIf31CmtsDsOfdmChanPowerTxPower": docsIf31CmtsDsOfdmChanPowerTxPower,
       "docsIf31CmtsUsOfdmaChanTable": docsIf31CmtsUsOfdmaChanTable,
       "docsIf31CmtsUsOfdmaChanEntry": docsIf31CmtsUsOfdmaChanEntry,
       "docsIf31CmtsUsOfdmaChanTemplateIndex": docsIf31CmtsUsOfdmaChanTemplateIndex,
       "docsIf31CmtsUsOfdmaChanConfigChangeCt": docsIf31CmtsUsOfdmaChanConfigChangeCt,
       "docsIf31CmtsUsOfdmaChanTargetRxPower": docsIf31CmtsUsOfdmaChanTargetRxPower,
       "docsIf31CmtsUsOfdmaChanLowerBdryFreq": docsIf31CmtsUsOfdmaChanLowerBdryFreq,
       "docsIf31CmtsUsOfdmaChanUpperBdryFreq": docsIf31CmtsUsOfdmaChanUpperBdryFreq,
       "docsIf31CmtsUsOfdmaChanSubcarrierSpacing": docsIf31CmtsUsOfdmaChanSubcarrierSpacing,
       "docsIf31CmtsUsOfdmaChanCyclicPrefix": docsIf31CmtsUsOfdmaChanCyclicPrefix,
       "docsIf31CmtsUsOfdmaChanNumSymbolsPerFrame": docsIf31CmtsUsOfdmaChanNumSymbolsPerFrame,
       "docsIf31CmtsUsOfdmaChanRollOffPeriod": docsIf31CmtsUsOfdmaChanRollOffPeriod,
       "docsIf31CmtsUsOfdmaChanPreEqEnable": docsIf31CmtsUsOfdmaChanPreEqEnable,
       "docsIf31CmtsUsOfdmaChanFineRngGuardband": docsIf31CmtsUsOfdmaChanFineRngGuardband,
       "docsIf31CmtsUsOfdmaChanFineRngNumSubcarriers": docsIf31CmtsUsOfdmaChanFineRngNumSubcarriers,
       "docsIf31CmtsUsOfdmaChanFineRngPreambleLen": docsIf31CmtsUsOfdmaChanFineRngPreambleLen,
       "docsIf31CmtsUsOfdmaChanInitRngGuardband": docsIf31CmtsUsOfdmaChanInitRngGuardband,
       "docsIf31CmtsUsOfdmaChanInitRngNumSubcarriers": docsIf31CmtsUsOfdmaChanInitRngNumSubcarriers,
       "docsIf31CmtsUsOfdmaChanInitRngPreambleLen": docsIf31CmtsUsOfdmaChanInitRngPreambleLen,
       "docsIf31CmtsUsOfdmaChanProvAttribMask": docsIf31CmtsUsOfdmaChanProvAttribMask,
       "docsIf31CmtsUsOfdmaChanTxBackoffStart": docsIf31CmtsUsOfdmaChanTxBackoffStart,
       "docsIf31CmtsUsOfdmaChanTxBackoffEnd": docsIf31CmtsUsOfdmaChanTxBackoffEnd,
       "docsIf31CmtsUsOfdmaChanRangingBackoffStart": docsIf31CmtsUsOfdmaChanRangingBackoffStart,
       "docsIf31CmtsUsOfdmaChanRangingBackoffEnd": docsIf31CmtsUsOfdmaChanRangingBackoffEnd,
       "docsIf31CmtsUsOfdmaChanUtilization": docsIf31CmtsUsOfdmaChanUtilization,
       "docsIf31CmtsUsOfdmaChanId": docsIf31CmtsUsOfdmaChanId,
       "docsIf31CmtsUsOfdmaDataIucStatsTable": docsIf31CmtsUsOfdmaDataIucStatsTable,
       "docsIf31CmtsUsOfdmaDataIucStatsEntry": docsIf31CmtsUsOfdmaDataIucStatsEntry,
       "docsIf31CmtsUsOfdmaDataIucStatsDataIuc": docsIf31CmtsUsOfdmaDataIucStatsDataIuc,
       "docsIf31CmtsUsOfdmaDataIucStatsMinislotPilotPattern": docsIf31CmtsUsOfdmaDataIucStatsMinislotPilotPattern,
       "docsIf31CmtsUsOfdmaDataIucStatsMinislotModulation": docsIf31CmtsUsOfdmaDataIucStatsMinislotModulation,
       "docsIf31CmtsUsOfdmaDataIucStatsTotalCodewords": docsIf31CmtsUsOfdmaDataIucStatsTotalCodewords,
       "docsIf31CmtsUsOfdmaDataIucStatsCorrectedCodewords": docsIf31CmtsUsOfdmaDataIucStatsCorrectedCodewords,
       "docsIf31CmtsUsOfdmaDataIucStatsUnreliableCodewords": docsIf31CmtsUsOfdmaDataIucStatsUnreliableCodewords,
       "docsIf31CmtsUsOfdmaDataIucStatsInOctets": docsIf31CmtsUsOfdmaDataIucStatsInOctets,
       "docsIf31CmtsUsOfdmaDataIucStatsCtrDiscontinuityTime": docsIf31CmtsUsOfdmaDataIucStatsCtrDiscontinuityTime,
       "docsIf31CmtsUsOfdmaDataIucStatsAssignedCmCt": docsIf31CmtsUsOfdmaDataIucStatsAssignedCmCt,
       "docsIf31CmtsUsOfdmaDataIucDetailStatusTable": docsIf31CmtsUsOfdmaDataIucDetailStatusTable,
       "docsIf31CmtsUsOfdmaDataIucDetailStatusEntry": docsIf31CmtsUsOfdmaDataIucDetailStatusEntry,
       "docsIf31CmtsUsOfdmaDataIucDetailStatusLowerFreq": docsIf31CmtsUsOfdmaDataIucDetailStatusLowerFreq,
       "docsIf31CmtsUsOfdmaDataIucDetailStatusUpperFreq": docsIf31CmtsUsOfdmaDataIucDetailStatusUpperFreq,
       "docsIf31CmtsUsOfdmaDataIucDetailStatusMinislotPilotPattern": docsIf31CmtsUsOfdmaDataIucDetailStatusMinislotPilotPattern,
       "docsIf31CmtsUsOfdmaDataIucDetailStatusMinislotModulation": docsIf31CmtsUsOfdmaDataIucDetailStatusMinislotModulation,
       "docsIf31CmtsUsOfdmaRangingIucStatusTable": docsIf31CmtsUsOfdmaRangingIucStatusTable,
       "docsIf31CmtsUsOfdmaRangingIucStatusEntry": docsIf31CmtsUsOfdmaRangingIucStatusEntry,
       "docsIf31CmtsUsOfdmaRangingIucStatusIuc": docsIf31CmtsUsOfdmaRangingIucStatusIuc,
       "docsIf31CmtsUsOfdmaRangingIucStatusGuardband": docsIf31CmtsUsOfdmaRangingIucStatusGuardband,
       "docsIf31CmtsUsOfdmaRangingIucStatusNumSubcarriers": docsIf31CmtsUsOfdmaRangingIucStatusNumSubcarriers,
       "docsIf31CmtsDsOfdmSubcarrierTypeTable": docsIf31CmtsDsOfdmSubcarrierTypeTable,
       "docsIf31CmtsDsOfdmSubcarrierTypeEntry": docsIf31CmtsDsOfdmSubcarrierTypeEntry,
       "docsIf31CmtsDsOfdmSubcarrierTypeStartSubcarrierId": docsIf31CmtsDsOfdmSubcarrierTypeStartSubcarrierId,
       "docsIf31CmtsDsOfdmSubcarrierTypeEndSubcarrierId": docsIf31CmtsDsOfdmSubcarrierTypeEndSubcarrierId,
       "docsIf31CmtsDsOfdmSubcarrierTypeSubcarrierType": docsIf31CmtsDsOfdmSubcarrierTypeSubcarrierType,
       "docsIf31CmtsUsOfdmaSubcarrierTypeTable": docsIf31CmtsUsOfdmaSubcarrierTypeTable,
       "docsIf31CmtsUsOfdmaSubcarrierTypeEntry": docsIf31CmtsUsOfdmaSubcarrierTypeEntry,
       "docsIf31CmtsUsOfdmaSubcarrierTypeStartSubcarrierId": docsIf31CmtsUsOfdmaSubcarrierTypeStartSubcarrierId,
       "docsIf31CmtsUsOfdmaSubcarrierTypeEndSubcarrierId": docsIf31CmtsUsOfdmaSubcarrierTypeEndSubcarrierId,
       "docsIf31CmtsUsOfdmaSubcarrierTypeSubcarrierType": docsIf31CmtsUsOfdmaSubcarrierTypeSubcarrierType,
       "docsIf31CmStatusTable": docsIf31CmStatusTable,
       "docsIf31CmStatusEntry": docsIf31CmStatusEntry,
       "docsIf31CmStatusEmDlsOperStatus": docsIf31CmStatusEmDlsOperStatus,
       "docsIf31CmEmDlsCfgTable": docsIf31CmEmDlsCfgTable,
       "docsIf31CmEmDlsCfgEntry": docsIf31CmEmDlsCfgEntry,
       "docsIf31CmEmDlsCfgDirection": docsIf31CmEmDlsCfgDirection,
       "docsIf31CmEmDlsCfgEntryBitrateThrshld": docsIf31CmEmDlsCfgEntryBitrateThrshld,
       "docsIf31CmEmDlsCfgEntryTimeThrshld": docsIf31CmEmDlsCfgEntryTimeThrshld,
       "docsIf31CmEmDlsCfgExitBitrateThrshld": docsIf31CmEmDlsCfgExitBitrateThrshld,
       "docsIf31CmEmDlsCfgExitTimeThrshld": docsIf31CmEmDlsCfgExitTimeThrshld,
       "docsIf31CmUsScQamChanTable": docsIf31CmUsScQamChanTable,
       "docsIf31CmUsScQamChanEntry": docsIf31CmUsScQamChanEntry,
       "docsIf31CmUsScQamChanTxPsd": docsIf31CmUsScQamChanTxPsd,
       "docsIf31MibConformance": docsIf31MibConformance,
       "docsIf31MibCompliances": docsIf31MibCompliances,
       "docsIf31CmtsCompliance": docsIf31CmtsCompliance,
       "docsIf31CmCompliance": docsIf31CmCompliance,
       "docsIf31MibGroups": docsIf31MibGroups,
       "docsIf31CmtsGroup": docsIf31CmtsGroup,
       "docsIf31CmGroup": docsIf31CmGroup}
)
