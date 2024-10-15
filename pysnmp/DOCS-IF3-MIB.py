# SNMP MIB module (DOCS-IF3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOCS-IF3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:25 2024
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

(docsDevEvId,
 docsDevEvLastTime,
 docsDevEvLevel,
 docsDevEvText) = mibBuilder.importSymbols(
    "DOCS-CABLE-DEVICE-MIB",
    "docsDevEvId",
    "docsDevEvLastTime",
    "docsDevEvLevel",
    "docsDevEvText")

(DocsEqualizerData,
 DocsisQosVersion,
 DocsisUpstreamType,
 TenthdB,
 TenthdBmV) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "DocsEqualizerData",
    "DocsisQosVersion",
    "DocsisUpstreamType",
    "TenthdB",
    "TenthdBmV")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

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

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

docsIf3Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20)
)
docsIf3Mib.setRevisions(
        ("2017-06-15 00:00",
         "2016-08-04 00:00",
         "2016-05-05 00:00",
         "2015-05-20 00:00",
         "2015-04-08 00:00",
         "2013-11-19 00:00",
         "2013-04-04 00:00",
         "2012-11-13 00:00",
         "2012-08-09 00:00",
         "2011-02-10 00:00",
         "2010-06-11 00:00",
         "2010-01-15 00:00",
         "2009-05-29 00:00",
         "2009-01-21 00:00",
         "2008-05-22 00:00",
         "2008-02-15 00:00",
         "2007-12-06 00:00",
         "2007-08-03 00:00",
         "2007-05-18 00:00",
         "2007-02-23 00:00",
         "2006-12-07 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CmRegState(Integer32, TextualConvention):
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
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("accessDenied", 13),
          ("bpiInit", 19),
          ("configFileDownloadComplete", 10),
          ("dhcpv4Complete", 7),
          ("dhcpv4InProgress", 15),
          ("dhcpv6Complete", 17),
          ("dhcpv6InProgress", 16),
          ("dsTopologyResolutionInProgress", 21),
          ("eaeInProgress", 14),
          ("forwardingDisabled", 20),
          ("notReady", 2),
          ("notSynchronized", 3),
          ("operational", 12),
          ("other", 1),
          ("phySynchronized", 4),
          ("rangingComplete", 6),
          ("rangingInProgress", 22),
          ("registrationComplete", 11),
          ("registrationInProgress", 18),
          ("rfMuteAll", 23),
          ("securityEstablished", 9),
          ("todEstablished", 8),
          ("usParametersAcquired", 5))
    )



class CmtsCmRegState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("bpiInit", 9),
          ("configFileDownloadComplete", 15),
          ("dhcpv4Complete", 5),
          ("dhcpv6Complete", 13),
          ("forwardingDisabled", 17),
          ("initialRanging", 2),
          ("operational", 8),
          ("other", 1),
          ("rangingAutoAdjComplete", 4),
          ("registrationComplete", 6),
          ("rfMuteAll", 18),
          ("startConfigFileDownload", 14),
          ("startDhcpv4", 11),
          ("startDhcpv6", 12),
          ("startEae", 10),
          ("startRegistration", 16))
    )



class ScdmaSelectionString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )



class AmplitudeData(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(2, 4116),
    )



class SpectrumAnalysisWindowFunction(Integer32, TextualConvention):
    status = "current"
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
        *(("blackmanHarris", 2),
          ("chebyshev", 7),
          ("flatTop", 5),
          ("gaussian", 6),
          ("hamming", 4),
          ("hann", 1),
          ("other", 0),
          ("rectangular", 3))
    )



class Tlv8(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(2, 255),
    )



class ChId(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class ChSetId(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class ChannelList(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d,"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class AttributeMask(Bits, TextualConvention):
    status = "current"


class AttrAggrRuleMask(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class RcpId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )



class Dsid(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )



class RangingState(Integer32, TextualConvention):
    status = "current"
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
        *(("aborted", 2),
          ("continue", 5),
          ("other", 1),
          ("retriesExceeded", 3),
          ("success", 4),
          ("timeoutT4", 6))
    )



class IfDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 1),
          ("upstream", 2))
    )



# MIB Managed Objects in the order of their OIDs

_DocsIf3Notifications_ObjectIdentity = ObjectIdentity
docsIf3Notifications = _DocsIf3Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 0)
)
_DocsIf3MibObjects_ObjectIdentity = ObjectIdentity
docsIf3MibObjects = _DocsIf3MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1)
)
_DocsIf3CmStatusTable_Object = MibTable
docsIf3CmStatusTable = _DocsIf3CmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 1)
)
if mibBuilder.loadTexts:
    docsIf3CmStatusTable.setStatus("current")
_DocsIf3CmStatusEntry_Object = MibTableRow
docsIf3CmStatusEntry = _DocsIf3CmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 1, 1)
)
docsIf3CmStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIf3CmStatusEntry.setStatus("current")
_DocsIf3CmStatusValue_Type = CmRegState
_DocsIf3CmStatusValue_Object = MibTableColumn
docsIf3CmStatusValue = _DocsIf3CmStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 1, 1, 1),
    _DocsIf3CmStatusValue_Type()
)
docsIf3CmStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmStatusValue.setStatus("current")


class _DocsIf3CmStatusCode_Type(OctetString):
    """Custom type docsIf3CmStatusCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 5),
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(7, 7),
    )


_DocsIf3CmStatusCode_Type.__name__ = "OctetString"
_DocsIf3CmStatusCode_Object = MibTableColumn
docsIf3CmStatusCode = _DocsIf3CmStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 1, 1, 2),
    _DocsIf3CmStatusCode_Type()
)
docsIf3CmStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmStatusCode.setStatus("current")
_DocsIf3CmStatusResets_Type = Counter32
_DocsIf3CmStatusResets_Object = MibTableColumn
docsIf3CmStatusResets = _DocsIf3CmStatusResets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 1, 1, 3),
    _DocsIf3CmStatusResets_Type()
)
docsIf3CmStatusResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmStatusResets.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmStatusResets.setUnits("resets")
_DocsIf3CmStatusLostSyncs_Type = Counter32
_DocsIf3CmStatusLostSyncs_Object = MibTableColumn
docsIf3CmStatusLostSyncs = _DocsIf3CmStatusLostSyncs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 1, 1, 4),
    _DocsIf3CmStatusLostSyncs_Type()
)
docsIf3CmStatusLostSyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmStatusLostSyncs.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmStatusLostSyncs.setUnits("messages")
_DocsIf3CmStatusInvalidMaps_Type = Counter32
_DocsIf3CmStatusInvalidMaps_Object = MibTableColumn
docsIf3CmStatusInvalidMaps = _DocsIf3CmStatusInvalidMaps_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 1, 1, 5),
    _DocsIf3CmStatusInvalidMaps_Type()
)
docsIf3CmStatusInvalidMaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmStatusInvalidMaps.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmStatusInvalidMaps.setUnits("maps")
_DocsIf3CmStatusInvalidUcds_Type = Counter32
_DocsIf3CmStatusInvalidUcds_Object = MibTableColumn
docsIf3CmStatusInvalidUcds = _DocsIf3CmStatusInvalidUcds_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 1, 1, 6),
    _DocsIf3CmStatusInvalidUcds_Type()
)
docsIf3CmStatusInvalidUcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmStatusInvalidUcds.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmStatusInvalidUcds.setUnits("messages")
_DocsIf3CmStatusInvalidRangingRsps_Type = Counter32
_DocsIf3CmStatusInvalidRangingRsps_Object = MibTableColumn
docsIf3CmStatusInvalidRangingRsps = _DocsIf3CmStatusInvalidRangingRsps_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 1, 1, 7),
    _DocsIf3CmStatusInvalidRangingRsps_Type()
)
docsIf3CmStatusInvalidRangingRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmStatusInvalidRangingRsps.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmStatusInvalidRangingRsps.setUnits("messages")
_DocsIf3CmStatusInvalidRegRsps_Type = Counter32
_DocsIf3CmStatusInvalidRegRsps_Object = MibTableColumn
docsIf3CmStatusInvalidRegRsps = _DocsIf3CmStatusInvalidRegRsps_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 1, 1, 8),
    _DocsIf3CmStatusInvalidRegRsps_Type()
)
docsIf3CmStatusInvalidRegRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmStatusInvalidRegRsps.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmStatusInvalidRegRsps.setUnits("messages")
_DocsIf3CmStatusT1Timeouts_Type = Counter32
_DocsIf3CmStatusT1Timeouts_Object = MibTableColumn
docsIf3CmStatusT1Timeouts = _DocsIf3CmStatusT1Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 1, 1, 9),
    _DocsIf3CmStatusT1Timeouts_Type()
)
docsIf3CmStatusT1Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmStatusT1Timeouts.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmStatusT1Timeouts.setUnits("timeouts")
_DocsIf3CmStatusT2Timeouts_Type = Counter32
_DocsIf3CmStatusT2Timeouts_Object = MibTableColumn
docsIf3CmStatusT2Timeouts = _DocsIf3CmStatusT2Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 1, 1, 10),
    _DocsIf3CmStatusT2Timeouts_Type()
)
docsIf3CmStatusT2Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmStatusT2Timeouts.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmStatusT2Timeouts.setUnits("timeouts")
_DocsIf3CmStatusUCCsSuccesses_Type = Counter32
_DocsIf3CmStatusUCCsSuccesses_Object = MibTableColumn
docsIf3CmStatusUCCsSuccesses = _DocsIf3CmStatusUCCsSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 1, 1, 11),
    _DocsIf3CmStatusUCCsSuccesses_Type()
)
docsIf3CmStatusUCCsSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmStatusUCCsSuccesses.setStatus("obsolete")
if mibBuilder.loadTexts:
    docsIf3CmStatusUCCsSuccesses.setUnits("attempts")
_DocsIf3CmStatusUCCFails_Type = Counter32
_DocsIf3CmStatusUCCFails_Object = MibTableColumn
docsIf3CmStatusUCCFails = _DocsIf3CmStatusUCCFails_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 1, 1, 12),
    _DocsIf3CmStatusUCCFails_Type()
)
docsIf3CmStatusUCCFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmStatusUCCFails.setStatus("obsolete")
if mibBuilder.loadTexts:
    docsIf3CmStatusUCCFails.setUnits("attempts")
_DocsIf3CmStatusEnergyMgt1x1OperStatus_Type = TruthValue
_DocsIf3CmStatusEnergyMgt1x1OperStatus_Object = MibTableColumn
docsIf3CmStatusEnergyMgt1x1OperStatus = _DocsIf3CmStatusEnergyMgt1x1OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 1, 1, 13),
    _DocsIf3CmStatusEnergyMgt1x1OperStatus_Type()
)
docsIf3CmStatusEnergyMgt1x1OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmStatusEnergyMgt1x1OperStatus.setStatus("current")
_DocsIf3CmStatusUsTable_Object = MibTable
docsIf3CmStatusUsTable = _DocsIf3CmStatusUsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 2)
)
if mibBuilder.loadTexts:
    docsIf3CmStatusUsTable.setStatus("current")
_DocsIf3CmStatusUsEntry_Object = MibTableRow
docsIf3CmStatusUsEntry = _DocsIf3CmStatusUsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 2, 1)
)
docsIf3CmStatusUsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIf3CmStatusUsEntry.setStatus("current")
_DocsIf3CmStatusUsTxPower_Type = TenthdBmV
_DocsIf3CmStatusUsTxPower_Object = MibTableColumn
docsIf3CmStatusUsTxPower = _DocsIf3CmStatusUsTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 2, 1, 1),
    _DocsIf3CmStatusUsTxPower_Type()
)
docsIf3CmStatusUsTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmStatusUsTxPower.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmStatusUsTxPower.setUnits("TenthdBmV")
_DocsIf3CmStatusUsT3Timeouts_Type = Counter32
_DocsIf3CmStatusUsT3Timeouts_Object = MibTableColumn
docsIf3CmStatusUsT3Timeouts = _DocsIf3CmStatusUsT3Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 2, 1, 2),
    _DocsIf3CmStatusUsT3Timeouts_Type()
)
docsIf3CmStatusUsT3Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmStatusUsT3Timeouts.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmStatusUsT3Timeouts.setUnits("timeouts")
_DocsIf3CmStatusUsT4Timeouts_Type = Counter32
_DocsIf3CmStatusUsT4Timeouts_Object = MibTableColumn
docsIf3CmStatusUsT4Timeouts = _DocsIf3CmStatusUsT4Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 2, 1, 3),
    _DocsIf3CmStatusUsT4Timeouts_Type()
)
docsIf3CmStatusUsT4Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmStatusUsT4Timeouts.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmStatusUsT4Timeouts.setUnits("timeouts")
_DocsIf3CmStatusUsRangingAborteds_Type = Counter32
_DocsIf3CmStatusUsRangingAborteds_Object = MibTableColumn
docsIf3CmStatusUsRangingAborteds = _DocsIf3CmStatusUsRangingAborteds_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 2, 1, 4),
    _DocsIf3CmStatusUsRangingAborteds_Type()
)
docsIf3CmStatusUsRangingAborteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmStatusUsRangingAborteds.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmStatusUsRangingAborteds.setUnits("attempts")
_DocsIf3CmStatusUsModulationType_Type = DocsisUpstreamType
_DocsIf3CmStatusUsModulationType_Object = MibTableColumn
docsIf3CmStatusUsModulationType = _DocsIf3CmStatusUsModulationType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 2, 1, 5),
    _DocsIf3CmStatusUsModulationType_Type()
)
docsIf3CmStatusUsModulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmStatusUsModulationType.setStatus("current")
_DocsIf3CmStatusUsEqData_Type = DocsEqualizerData
_DocsIf3CmStatusUsEqData_Object = MibTableColumn
docsIf3CmStatusUsEqData = _DocsIf3CmStatusUsEqData_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 2, 1, 6),
    _DocsIf3CmStatusUsEqData_Type()
)
docsIf3CmStatusUsEqData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmStatusUsEqData.setStatus("current")
_DocsIf3CmStatusUsT3Exceededs_Type = Counter32
_DocsIf3CmStatusUsT3Exceededs_Object = MibTableColumn
docsIf3CmStatusUsT3Exceededs = _DocsIf3CmStatusUsT3Exceededs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 2, 1, 7),
    _DocsIf3CmStatusUsT3Exceededs_Type()
)
docsIf3CmStatusUsT3Exceededs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmStatusUsT3Exceededs.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmStatusUsT3Exceededs.setUnits("timeouts")
_DocsIf3CmStatusUsIsMuted_Type = TruthValue
_DocsIf3CmStatusUsIsMuted_Object = MibTableColumn
docsIf3CmStatusUsIsMuted = _DocsIf3CmStatusUsIsMuted_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 2, 1, 8),
    _DocsIf3CmStatusUsIsMuted_Type()
)
docsIf3CmStatusUsIsMuted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmStatusUsIsMuted.setStatus("current")
_DocsIf3CmStatusUsRangingStatus_Type = RangingState
_DocsIf3CmStatusUsRangingStatus_Object = MibTableColumn
docsIf3CmStatusUsRangingStatus = _DocsIf3CmStatusUsRangingStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 2, 1, 9),
    _DocsIf3CmStatusUsRangingStatus_Type()
)
docsIf3CmStatusUsRangingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmStatusUsRangingStatus.setStatus("current")
_DocsIf3CmtsCmRegStatusTable_Object = MibTable
docsIf3CmtsCmRegStatusTable = _DocsIf3CmtsCmRegStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 3)
)
if mibBuilder.loadTexts:
    docsIf3CmtsCmRegStatusTable.setStatus("current")
_DocsIf3CmtsCmRegStatusEntry_Object = MibTableRow
docsIf3CmtsCmRegStatusEntry = _DocsIf3CmtsCmRegStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 3, 1)
)
docsIf3CmtsCmRegStatusEntry.setIndexNames(
    (0, "DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusId"),
)
if mibBuilder.loadTexts:
    docsIf3CmtsCmRegStatusEntry.setStatus("current")


class _DocsIf3CmtsCmRegStatusId_Type(Unsigned32):
    """Custom type docsIf3CmtsCmRegStatusId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsIf3CmtsCmRegStatusId_Type.__name__ = "Unsigned32"
_DocsIf3CmtsCmRegStatusId_Object = MibTableColumn
docsIf3CmtsCmRegStatusId = _DocsIf3CmtsCmRegStatusId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 3, 1, 1),
    _DocsIf3CmtsCmRegStatusId_Type()
)
docsIf3CmtsCmRegStatusId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf3CmtsCmRegStatusId.setStatus("current")
_DocsIf3CmtsCmRegStatusMacAddr_Type = MacAddress
_DocsIf3CmtsCmRegStatusMacAddr_Object = MibTableColumn
docsIf3CmtsCmRegStatusMacAddr = _DocsIf3CmtsCmRegStatusMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 3, 1, 2),
    _DocsIf3CmtsCmRegStatusMacAddr_Type()
)
docsIf3CmtsCmRegStatusMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsCmRegStatusMacAddr.setStatus("current")
_DocsIf3CmtsCmRegStatusIPv6Addr_Type = InetAddressIPv6
_DocsIf3CmtsCmRegStatusIPv6Addr_Object = MibTableColumn
docsIf3CmtsCmRegStatusIPv6Addr = _DocsIf3CmtsCmRegStatusIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 3, 1, 3),
    _DocsIf3CmtsCmRegStatusIPv6Addr_Type()
)
docsIf3CmtsCmRegStatusIPv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsCmRegStatusIPv6Addr.setStatus("current")
_DocsIf3CmtsCmRegStatusIPv6LinkLocal_Type = InetAddressIPv6
_DocsIf3CmtsCmRegStatusIPv6LinkLocal_Object = MibTableColumn
docsIf3CmtsCmRegStatusIPv6LinkLocal = _DocsIf3CmtsCmRegStatusIPv6LinkLocal_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 3, 1, 4),
    _DocsIf3CmtsCmRegStatusIPv6LinkLocal_Type()
)
docsIf3CmtsCmRegStatusIPv6LinkLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsCmRegStatusIPv6LinkLocal.setStatus("current")
_DocsIf3CmtsCmRegStatusIPv4Addr_Type = InetAddressIPv4
_DocsIf3CmtsCmRegStatusIPv4Addr_Object = MibTableColumn
docsIf3CmtsCmRegStatusIPv4Addr = _DocsIf3CmtsCmRegStatusIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 3, 1, 5),
    _DocsIf3CmtsCmRegStatusIPv4Addr_Type()
)
docsIf3CmtsCmRegStatusIPv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsCmRegStatusIPv4Addr.setStatus("current")
_DocsIf3CmtsCmRegStatusValue_Type = CmtsCmRegState
_DocsIf3CmtsCmRegStatusValue_Object = MibTableColumn
docsIf3CmtsCmRegStatusValue = _DocsIf3CmtsCmRegStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 3, 1, 6),
    _DocsIf3CmtsCmRegStatusValue_Type()
)
docsIf3CmtsCmRegStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsCmRegStatusValue.setStatus("current")
_DocsIf3CmtsCmRegStatusMdIfIndex_Type = InterfaceIndexOrZero
_DocsIf3CmtsCmRegStatusMdIfIndex_Object = MibTableColumn
docsIf3CmtsCmRegStatusMdIfIndex = _DocsIf3CmtsCmRegStatusMdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 3, 1, 7),
    _DocsIf3CmtsCmRegStatusMdIfIndex_Type()
)
docsIf3CmtsCmRegStatusMdIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsCmRegStatusMdIfIndex.setStatus("current")
_DocsIf3CmtsCmRegStatusMdCmSgId_Type = Unsigned32
_DocsIf3CmtsCmRegStatusMdCmSgId_Object = MibTableColumn
docsIf3CmtsCmRegStatusMdCmSgId = _DocsIf3CmtsCmRegStatusMdCmSgId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 3, 1, 8),
    _DocsIf3CmtsCmRegStatusMdCmSgId_Type()
)
docsIf3CmtsCmRegStatusMdCmSgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsCmRegStatusMdCmSgId.setStatus("current")
_DocsIf3CmtsCmRegStatusRcpId_Type = RcpId
_DocsIf3CmtsCmRegStatusRcpId_Object = MibTableColumn
docsIf3CmtsCmRegStatusRcpId = _DocsIf3CmtsCmRegStatusRcpId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 3, 1, 9),
    _DocsIf3CmtsCmRegStatusRcpId_Type()
)
docsIf3CmtsCmRegStatusRcpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsCmRegStatusRcpId.setStatus("current")
_DocsIf3CmtsCmRegStatusRccStatusId_Type = Unsigned32
_DocsIf3CmtsCmRegStatusRccStatusId_Object = MibTableColumn
docsIf3CmtsCmRegStatusRccStatusId = _DocsIf3CmtsCmRegStatusRccStatusId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 3, 1, 10),
    _DocsIf3CmtsCmRegStatusRccStatusId_Type()
)
docsIf3CmtsCmRegStatusRccStatusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsCmRegStatusRccStatusId.setStatus("current")
_DocsIf3CmtsCmRegStatusRcsId_Type = ChSetId
_DocsIf3CmtsCmRegStatusRcsId_Object = MibTableColumn
docsIf3CmtsCmRegStatusRcsId = _DocsIf3CmtsCmRegStatusRcsId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 3, 1, 11),
    _DocsIf3CmtsCmRegStatusRcsId_Type()
)
docsIf3CmtsCmRegStatusRcsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsCmRegStatusRcsId.setStatus("current")
_DocsIf3CmtsCmRegStatusTcsId_Type = ChSetId
_DocsIf3CmtsCmRegStatusTcsId_Object = MibTableColumn
docsIf3CmtsCmRegStatusTcsId = _DocsIf3CmtsCmRegStatusTcsId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 3, 1, 12),
    _DocsIf3CmtsCmRegStatusTcsId_Type()
)
docsIf3CmtsCmRegStatusTcsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsCmRegStatusTcsId.setStatus("current")
_DocsIf3CmtsCmRegStatusQosVersion_Type = DocsisQosVersion
_DocsIf3CmtsCmRegStatusQosVersion_Object = MibTableColumn
docsIf3CmtsCmRegStatusQosVersion = _DocsIf3CmtsCmRegStatusQosVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 3, 1, 13),
    _DocsIf3CmtsCmRegStatusQosVersion_Type()
)
docsIf3CmtsCmRegStatusQosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsCmRegStatusQosVersion.setStatus("current")
_DocsIf3CmtsCmRegStatusLastRegTime_Type = DateAndTime
_DocsIf3CmtsCmRegStatusLastRegTime_Object = MibTableColumn
docsIf3CmtsCmRegStatusLastRegTime = _DocsIf3CmtsCmRegStatusLastRegTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 3, 1, 14),
    _DocsIf3CmtsCmRegStatusLastRegTime_Type()
)
docsIf3CmtsCmRegStatusLastRegTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsCmRegStatusLastRegTime.setStatus("current")
_DocsIf3CmtsCmRegStatusAddrResolutionReqs_Type = Counter32
_DocsIf3CmtsCmRegStatusAddrResolutionReqs_Object = MibTableColumn
docsIf3CmtsCmRegStatusAddrResolutionReqs = _DocsIf3CmtsCmRegStatusAddrResolutionReqs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 3, 1, 15),
    _DocsIf3CmtsCmRegStatusAddrResolutionReqs_Type()
)
docsIf3CmtsCmRegStatusAddrResolutionReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsCmRegStatusAddrResolutionReqs.setStatus("current")


class _DocsIf3CmtsCmRegStatusEnergyMgtEnabled_Type(Bits):
    """Custom type docsIf3CmtsCmRegStatusEnergyMgtEnabled based on Bits"""
    namedValues = NamedValues(
        *(("dlsMode", 1),
          ("em1x1Mode", 0))
    )

_DocsIf3CmtsCmRegStatusEnergyMgtEnabled_Type.__name__ = "Bits"
_DocsIf3CmtsCmRegStatusEnergyMgtEnabled_Object = MibTableColumn
docsIf3CmtsCmRegStatusEnergyMgtEnabled = _DocsIf3CmtsCmRegStatusEnergyMgtEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 3, 1, 16),
    _DocsIf3CmtsCmRegStatusEnergyMgtEnabled_Type()
)
docsIf3CmtsCmRegStatusEnergyMgtEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsCmRegStatusEnergyMgtEnabled.setStatus("current")


class _DocsIf3CmtsCmRegStatusEnergyMgtOperStatus_Type(Bits):
    """Custom type docsIf3CmtsCmRegStatusEnergyMgtOperStatus based on Bits"""
    namedValues = NamedValues(
        *(("dlsMode", 1),
          ("em1x1Mode", 0))
    )

_DocsIf3CmtsCmRegStatusEnergyMgtOperStatus_Type.__name__ = "Bits"
_DocsIf3CmtsCmRegStatusEnergyMgtOperStatus_Object = MibTableColumn
docsIf3CmtsCmRegStatusEnergyMgtOperStatus = _DocsIf3CmtsCmRegStatusEnergyMgtOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 3, 1, 17),
    _DocsIf3CmtsCmRegStatusEnergyMgtOperStatus_Type()
)
docsIf3CmtsCmRegStatusEnergyMgtOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsCmRegStatusEnergyMgtOperStatus.setStatus("current")
_DocsIf3CmtsCmUsStatusTable_Object = MibTable
docsIf3CmtsCmUsStatusTable = _DocsIf3CmtsCmUsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 4)
)
if mibBuilder.loadTexts:
    docsIf3CmtsCmUsStatusTable.setStatus("current")
_DocsIf3CmtsCmUsStatusEntry_Object = MibTableRow
docsIf3CmtsCmUsStatusEntry = _DocsIf3CmtsCmUsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 4, 1)
)
docsIf3CmtsCmUsStatusEntry.setIndexNames(
    (0, "DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusId"),
    (0, "DOCS-IF3-MIB", "docsIf3CmtsCmUsStatusChIfIndex"),
)
if mibBuilder.loadTexts:
    docsIf3CmtsCmUsStatusEntry.setStatus("current")
_DocsIf3CmtsCmUsStatusChIfIndex_Type = InterfaceIndex
_DocsIf3CmtsCmUsStatusChIfIndex_Object = MibTableColumn
docsIf3CmtsCmUsStatusChIfIndex = _DocsIf3CmtsCmUsStatusChIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 4, 1, 1),
    _DocsIf3CmtsCmUsStatusChIfIndex_Type()
)
docsIf3CmtsCmUsStatusChIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf3CmtsCmUsStatusChIfIndex.setStatus("current")
_DocsIf3CmtsCmUsStatusModulationType_Type = DocsisUpstreamType
_DocsIf3CmtsCmUsStatusModulationType_Object = MibTableColumn
docsIf3CmtsCmUsStatusModulationType = _DocsIf3CmtsCmUsStatusModulationType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 4, 1, 2),
    _DocsIf3CmtsCmUsStatusModulationType_Type()
)
docsIf3CmtsCmUsStatusModulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsCmUsStatusModulationType.setStatus("current")
_DocsIf3CmtsCmUsStatusRxPower_Type = TenthdBmV
_DocsIf3CmtsCmUsStatusRxPower_Object = MibTableColumn
docsIf3CmtsCmUsStatusRxPower = _DocsIf3CmtsCmUsStatusRxPower_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 4, 1, 3),
    _DocsIf3CmtsCmUsStatusRxPower_Type()
)
docsIf3CmtsCmUsStatusRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsCmUsStatusRxPower.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmtsCmUsStatusRxPower.setUnits("TenthdBmV")
_DocsIf3CmtsCmUsStatusSignalNoise_Type = TenthdB
_DocsIf3CmtsCmUsStatusSignalNoise_Object = MibTableColumn
docsIf3CmtsCmUsStatusSignalNoise = _DocsIf3CmtsCmUsStatusSignalNoise_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 4, 1, 4),
    _DocsIf3CmtsCmUsStatusSignalNoise_Type()
)
docsIf3CmtsCmUsStatusSignalNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsCmUsStatusSignalNoise.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmtsCmUsStatusSignalNoise.setUnits("TenthdB")


class _DocsIf3CmtsCmUsStatusMicroreflections_Type(Unsigned32):
    """Custom type docsIf3CmtsCmUsStatusMicroreflections based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsIf3CmtsCmUsStatusMicroreflections_Type.__name__ = "Unsigned32"
_DocsIf3CmtsCmUsStatusMicroreflections_Object = MibTableColumn
docsIf3CmtsCmUsStatusMicroreflections = _DocsIf3CmtsCmUsStatusMicroreflections_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 4, 1, 5),
    _DocsIf3CmtsCmUsStatusMicroreflections_Type()
)
docsIf3CmtsCmUsStatusMicroreflections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsCmUsStatusMicroreflections.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmtsCmUsStatusMicroreflections.setUnits("-dBc")
_DocsIf3CmtsCmUsStatusEqData_Type = DocsEqualizerData
_DocsIf3CmtsCmUsStatusEqData_Object = MibTableColumn
docsIf3CmtsCmUsStatusEqData = _DocsIf3CmtsCmUsStatusEqData_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 4, 1, 6),
    _DocsIf3CmtsCmUsStatusEqData_Type()
)
docsIf3CmtsCmUsStatusEqData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsCmUsStatusEqData.setStatus("current")
_DocsIf3CmtsCmUsStatusUnerroreds_Type = Counter32
_DocsIf3CmtsCmUsStatusUnerroreds_Object = MibTableColumn
docsIf3CmtsCmUsStatusUnerroreds = _DocsIf3CmtsCmUsStatusUnerroreds_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 4, 1, 7),
    _DocsIf3CmtsCmUsStatusUnerroreds_Type()
)
docsIf3CmtsCmUsStatusUnerroreds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsCmUsStatusUnerroreds.setStatus("current")
_DocsIf3CmtsCmUsStatusCorrecteds_Type = Counter32
_DocsIf3CmtsCmUsStatusCorrecteds_Object = MibTableColumn
docsIf3CmtsCmUsStatusCorrecteds = _DocsIf3CmtsCmUsStatusCorrecteds_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 4, 1, 8),
    _DocsIf3CmtsCmUsStatusCorrecteds_Type()
)
docsIf3CmtsCmUsStatusCorrecteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsCmUsStatusCorrecteds.setStatus("current")
_DocsIf3CmtsCmUsStatusUncorrectables_Type = Counter32
_DocsIf3CmtsCmUsStatusUncorrectables_Object = MibTableColumn
docsIf3CmtsCmUsStatusUncorrectables = _DocsIf3CmtsCmUsStatusUncorrectables_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 4, 1, 9),
    _DocsIf3CmtsCmUsStatusUncorrectables_Type()
)
docsIf3CmtsCmUsStatusUncorrectables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsCmUsStatusUncorrectables.setStatus("current")
_DocsIf3CmtsCmUsStatusHighResolutionTimingOffset_Type = Integer32
_DocsIf3CmtsCmUsStatusHighResolutionTimingOffset_Object = MibTableColumn
docsIf3CmtsCmUsStatusHighResolutionTimingOffset = _DocsIf3CmtsCmUsStatusHighResolutionTimingOffset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 4, 1, 10),
    _DocsIf3CmtsCmUsStatusHighResolutionTimingOffset_Type()
)
docsIf3CmtsCmUsStatusHighResolutionTimingOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsCmUsStatusHighResolutionTimingOffset.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmtsCmUsStatusHighResolutionTimingOffset.setUnits("time tick/(64*256)")
_DocsIf3CmtsCmUsStatusIsMuted_Type = TruthValue
_DocsIf3CmtsCmUsStatusIsMuted_Object = MibTableColumn
docsIf3CmtsCmUsStatusIsMuted = _DocsIf3CmtsCmUsStatusIsMuted_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 4, 1, 11),
    _DocsIf3CmtsCmUsStatusIsMuted_Type()
)
docsIf3CmtsCmUsStatusIsMuted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsCmUsStatusIsMuted.setStatus("current")
_DocsIf3CmtsCmUsStatusRangingStatus_Type = RangingState
_DocsIf3CmtsCmUsStatusRangingStatus_Object = MibTableColumn
docsIf3CmtsCmUsStatusRangingStatus = _DocsIf3CmtsCmUsStatusRangingStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 4, 1, 12),
    _DocsIf3CmtsCmUsStatusRangingStatus_Type()
)
docsIf3CmtsCmUsStatusRangingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsCmUsStatusRangingStatus.setStatus("current")
_DocsIf3MdChCfgTable_Object = MibTable
docsIf3MdChCfgTable = _DocsIf3MdChCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 5)
)
if mibBuilder.loadTexts:
    docsIf3MdChCfgTable.setStatus("current")
_DocsIf3MdChCfgEntry_Object = MibTableRow
docsIf3MdChCfgEntry = _DocsIf3MdChCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 5, 1)
)
docsIf3MdChCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF3-MIB", "docsIf3MdChCfgChIfIndex"),
)
if mibBuilder.loadTexts:
    docsIf3MdChCfgEntry.setStatus("current")
_DocsIf3MdChCfgChIfIndex_Type = InterfaceIndex
_DocsIf3MdChCfgChIfIndex_Object = MibTableColumn
docsIf3MdChCfgChIfIndex = _DocsIf3MdChCfgChIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 5, 1, 1),
    _DocsIf3MdChCfgChIfIndex_Type()
)
docsIf3MdChCfgChIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf3MdChCfgChIfIndex.setStatus("current")
_DocsIf3MdChCfgIsPriCapableDs_Type = TruthValue
_DocsIf3MdChCfgIsPriCapableDs_Object = MibTableColumn
docsIf3MdChCfgIsPriCapableDs = _DocsIf3MdChCfgIsPriCapableDs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 5, 1, 2),
    _DocsIf3MdChCfgIsPriCapableDs_Type()
)
docsIf3MdChCfgIsPriCapableDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIf3MdChCfgIsPriCapableDs.setStatus("current")


class _DocsIf3MdChCfgChId_Type(ChId):
    """Custom type docsIf3MdChCfgChId based on ChId"""
    subtypeSpec = ChId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DocsIf3MdChCfgChId_Type.__name__ = "ChId"
_DocsIf3MdChCfgChId_Object = MibTableColumn
docsIf3MdChCfgChId = _DocsIf3MdChCfgChId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 5, 1, 3),
    _DocsIf3MdChCfgChId_Type()
)
docsIf3MdChCfgChId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIf3MdChCfgChId.setStatus("current")


class _DocsIf3MdChCfgSfProvAttrMask_Type(AttributeMask):
    """Custom type docsIf3MdChCfgSfProvAttrMask based on AttributeMask"""
    defaultHexValue = "00000000"


_DocsIf3MdChCfgSfProvAttrMask_Object = MibTableColumn
docsIf3MdChCfgSfProvAttrMask = _DocsIf3MdChCfgSfProvAttrMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 5, 1, 4),
    _DocsIf3MdChCfgSfProvAttrMask_Type()
)
docsIf3MdChCfgSfProvAttrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIf3MdChCfgSfProvAttrMask.setStatus("current")
_DocsIf3MdChCfgRowStatus_Type = RowStatus
_DocsIf3MdChCfgRowStatus_Object = MibTableColumn
docsIf3MdChCfgRowStatus = _DocsIf3MdChCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 5, 1, 5),
    _DocsIf3MdChCfgRowStatus_Type()
)
docsIf3MdChCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIf3MdChCfgRowStatus.setStatus("current")
_DocsIf3RccCfgTable_Object = MibTable
docsIf3RccCfgTable = _DocsIf3RccCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 6)
)
if mibBuilder.loadTexts:
    docsIf3RccCfgTable.setStatus("obsolete")
_DocsIf3RccCfgEntry_Object = MibTableRow
docsIf3RccCfgEntry = _DocsIf3RccCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 6, 1)
)
docsIf3RccCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF3-MIB", "docsIf3RccCfgRcpId"),
    (0, "DOCS-IF3-MIB", "docsIf3RccCfgRccCfgId"),
)
if mibBuilder.loadTexts:
    docsIf3RccCfgEntry.setStatus("obsolete")
_DocsIf3RccCfgRcpId_Type = RcpId
_DocsIf3RccCfgRcpId_Object = MibTableColumn
docsIf3RccCfgRcpId = _DocsIf3RccCfgRcpId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 6, 1, 1),
    _DocsIf3RccCfgRcpId_Type()
)
docsIf3RccCfgRcpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf3RccCfgRcpId.setStatus("obsolete")


class _DocsIf3RccCfgRccCfgId_Type(Unsigned32):
    """Custom type docsIf3RccCfgRccCfgId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsIf3RccCfgRccCfgId_Type.__name__ = "Unsigned32"
_DocsIf3RccCfgRccCfgId_Object = MibTableColumn
docsIf3RccCfgRccCfgId = _DocsIf3RccCfgRccCfgId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 6, 1, 2),
    _DocsIf3RccCfgRccCfgId_Type()
)
docsIf3RccCfgRccCfgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf3RccCfgRccCfgId.setStatus("obsolete")


class _DocsIf3RccCfgVendorSpecific_Type(OctetString):
    """Custom type docsIf3RccCfgVendorSpecific based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 252),
    )


_DocsIf3RccCfgVendorSpecific_Type.__name__ = "OctetString"
_DocsIf3RccCfgVendorSpecific_Object = MibTableColumn
docsIf3RccCfgVendorSpecific = _DocsIf3RccCfgVendorSpecific_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 6, 1, 3),
    _DocsIf3RccCfgVendorSpecific_Type()
)
docsIf3RccCfgVendorSpecific.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIf3RccCfgVendorSpecific.setStatus("obsolete")


class _DocsIf3RccCfgDescription_Type(SnmpAdminString):
    """Custom type docsIf3RccCfgDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DocsIf3RccCfgDescription_Type.__name__ = "SnmpAdminString"
_DocsIf3RccCfgDescription_Object = MibTableColumn
docsIf3RccCfgDescription = _DocsIf3RccCfgDescription_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 6, 1, 4),
    _DocsIf3RccCfgDescription_Type()
)
docsIf3RccCfgDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIf3RccCfgDescription.setStatus("obsolete")
_DocsIf3RccCfgRowStatus_Type = RowStatus
_DocsIf3RccCfgRowStatus_Object = MibTableColumn
docsIf3RccCfgRowStatus = _DocsIf3RccCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 6, 1, 5),
    _DocsIf3RccCfgRowStatus_Type()
)
docsIf3RccCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIf3RccCfgRowStatus.setStatus("obsolete")
_DocsIf3RccStatusTable_Object = MibTable
docsIf3RccStatusTable = _DocsIf3RccStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 7)
)
if mibBuilder.loadTexts:
    docsIf3RccStatusTable.setStatus("current")
_DocsIf3RccStatusEntry_Object = MibTableRow
docsIf3RccStatusEntry = _DocsIf3RccStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 7, 1)
)
docsIf3RccStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF3-MIB", "docsIf3RccStatusRcpId"),
    (0, "DOCS-IF3-MIB", "docsIf3RccStatusRccStatusId"),
)
if mibBuilder.loadTexts:
    docsIf3RccStatusEntry.setStatus("current")
_DocsIf3RccStatusRcpId_Type = RcpId
_DocsIf3RccStatusRcpId_Object = MibTableColumn
docsIf3RccStatusRcpId = _DocsIf3RccStatusRcpId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 7, 1, 1),
    _DocsIf3RccStatusRcpId_Type()
)
docsIf3RccStatusRcpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf3RccStatusRcpId.setStatus("current")


class _DocsIf3RccStatusRccStatusId_Type(Unsigned32):
    """Custom type docsIf3RccStatusRccStatusId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsIf3RccStatusRccStatusId_Type.__name__ = "Unsigned32"
_DocsIf3RccStatusRccStatusId_Object = MibTableColumn
docsIf3RccStatusRccStatusId = _DocsIf3RccStatusRccStatusId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 7, 1, 2),
    _DocsIf3RccStatusRccStatusId_Type()
)
docsIf3RccStatusRccStatusId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf3RccStatusRccStatusId.setStatus("current")


class _DocsIf3RccStatusRccCfgId_Type(Unsigned32):
    """Custom type docsIf3RccStatusRccCfgId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsIf3RccStatusRccCfgId_Type.__name__ = "Unsigned32"
_DocsIf3RccStatusRccCfgId_Object = MibTableColumn
docsIf3RccStatusRccCfgId = _DocsIf3RccStatusRccCfgId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 7, 1, 3),
    _DocsIf3RccStatusRccCfgId_Type()
)
docsIf3RccStatusRccCfgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3RccStatusRccCfgId.setStatus("current")


class _DocsIf3RccStatusValidityCode_Type(Integer32):
    """Custom type docsIf3RccStatusValidityCode based on Integer32"""
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
        *(("duplicateDs", 7),
          ("invalid", 3),
          ("missingPrimaryDs", 5),
          ("multiplePrimaryDs", 6),
          ("other", 1),
          ("valid", 2),
          ("wrongConnectivity", 9),
          ("wrongFrequencyRange", 8),
          ("wrongPrimaryDs", 4))
    )


_DocsIf3RccStatusValidityCode_Type.__name__ = "Integer32"
_DocsIf3RccStatusValidityCode_Object = MibTableColumn
docsIf3RccStatusValidityCode = _DocsIf3RccStatusValidityCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 7, 1, 4),
    _DocsIf3RccStatusValidityCode_Type()
)
docsIf3RccStatusValidityCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3RccStatusValidityCode.setStatus("current")
_DocsIf3RccStatusValidityCodeText_Type = SnmpAdminString
_DocsIf3RccStatusValidityCodeText_Object = MibTableColumn
docsIf3RccStatusValidityCodeText = _DocsIf3RccStatusValidityCodeText_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 7, 1, 5),
    _DocsIf3RccStatusValidityCodeText_Type()
)
docsIf3RccStatusValidityCodeText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3RccStatusValidityCodeText.setStatus("current")
_DocsIf3RxChCfgTable_Object = MibTable
docsIf3RxChCfgTable = _DocsIf3RxChCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 8)
)
if mibBuilder.loadTexts:
    docsIf3RxChCfgTable.setStatus("obsolete")
_DocsIf3RxChCfgEntry_Object = MibTableRow
docsIf3RxChCfgEntry = _DocsIf3RxChCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 8, 1)
)
docsIf3RxChCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF3-MIB", "docsIf3RccCfgRcpId"),
    (0, "DOCS-IF3-MIB", "docsIf3RccCfgRccCfgId"),
    (0, "DOCS-IF3-MIB", "docsIf3RxChCfgRcId"),
)
if mibBuilder.loadTexts:
    docsIf3RxChCfgEntry.setStatus("obsolete")


class _DocsIf3RxChCfgRcId_Type(Unsigned32):
    """Custom type docsIf3RxChCfgRcId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DocsIf3RxChCfgRcId_Type.__name__ = "Unsigned32"
_DocsIf3RxChCfgRcId_Object = MibTableColumn
docsIf3RxChCfgRcId = _DocsIf3RxChCfgRcId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 8, 1, 1),
    _DocsIf3RxChCfgRcId_Type()
)
docsIf3RxChCfgRcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf3RxChCfgRcId.setStatus("obsolete")
_DocsIf3RxChCfgChIfIndex_Type = InterfaceIndex
_DocsIf3RxChCfgChIfIndex_Object = MibTableColumn
docsIf3RxChCfgChIfIndex = _DocsIf3RxChCfgChIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 8, 1, 2),
    _DocsIf3RxChCfgChIfIndex_Type()
)
docsIf3RxChCfgChIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIf3RxChCfgChIfIndex.setStatus("obsolete")


class _DocsIf3RxChCfgPrimaryDsIndicator_Type(TruthValue):
    """Custom type docsIf3RxChCfgPrimaryDsIndicator based on TruthValue"""


_DocsIf3RxChCfgPrimaryDsIndicator_Object = MibTableColumn
docsIf3RxChCfgPrimaryDsIndicator = _DocsIf3RxChCfgPrimaryDsIndicator_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 8, 1, 3),
    _DocsIf3RxChCfgPrimaryDsIndicator_Type()
)
docsIf3RxChCfgPrimaryDsIndicator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIf3RxChCfgPrimaryDsIndicator.setStatus("obsolete")


class _DocsIf3RxChCfgRcRmConnectivityId_Type(Unsigned32):
    """Custom type docsIf3RxChCfgRcRmConnectivityId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsIf3RxChCfgRcRmConnectivityId_Type.__name__ = "Unsigned32"
_DocsIf3RxChCfgRcRmConnectivityId_Object = MibTableColumn
docsIf3RxChCfgRcRmConnectivityId = _DocsIf3RxChCfgRcRmConnectivityId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 8, 1, 4),
    _DocsIf3RxChCfgRcRmConnectivityId_Type()
)
docsIf3RxChCfgRcRmConnectivityId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIf3RxChCfgRcRmConnectivityId.setStatus("obsolete")
_DocsIf3RxChCfgRowStatus_Type = RowStatus
_DocsIf3RxChCfgRowStatus_Object = MibTableColumn
docsIf3RxChCfgRowStatus = _DocsIf3RxChCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 8, 1, 5),
    _DocsIf3RxChCfgRowStatus_Type()
)
docsIf3RxChCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIf3RxChCfgRowStatus.setStatus("obsolete")
_DocsIf3RxChStatusTable_Object = MibTable
docsIf3RxChStatusTable = _DocsIf3RxChStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 9)
)
if mibBuilder.loadTexts:
    docsIf3RxChStatusTable.setStatus("current")
_DocsIf3RxChStatusEntry_Object = MibTableRow
docsIf3RxChStatusEntry = _DocsIf3RxChStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 9, 1)
)
docsIf3RxChStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF3-MIB", "docsIf3RccStatusRcpId"),
    (0, "DOCS-IF3-MIB", "docsIf3RccStatusRccStatusId"),
    (0, "DOCS-IF3-MIB", "docsIf3RxChStatusRcId"),
)
if mibBuilder.loadTexts:
    docsIf3RxChStatusEntry.setStatus("current")


class _DocsIf3RxChStatusRcId_Type(Unsigned32):
    """Custom type docsIf3RxChStatusRcId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DocsIf3RxChStatusRcId_Type.__name__ = "Unsigned32"
_DocsIf3RxChStatusRcId_Object = MibTableColumn
docsIf3RxChStatusRcId = _DocsIf3RxChStatusRcId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 9, 1, 1),
    _DocsIf3RxChStatusRcId_Type()
)
docsIf3RxChStatusRcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf3RxChStatusRcId.setStatus("current")
_DocsIf3RxChStatusChIfIndex_Type = InterfaceIndex
_DocsIf3RxChStatusChIfIndex_Object = MibTableColumn
docsIf3RxChStatusChIfIndex = _DocsIf3RxChStatusChIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 9, 1, 2),
    _DocsIf3RxChStatusChIfIndex_Type()
)
docsIf3RxChStatusChIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3RxChStatusChIfIndex.setStatus("current")
_DocsIf3RxChStatusPrimaryDsIndicator_Type = TruthValue
_DocsIf3RxChStatusPrimaryDsIndicator_Object = MibTableColumn
docsIf3RxChStatusPrimaryDsIndicator = _DocsIf3RxChStatusPrimaryDsIndicator_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 9, 1, 3),
    _DocsIf3RxChStatusPrimaryDsIndicator_Type()
)
docsIf3RxChStatusPrimaryDsIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3RxChStatusPrimaryDsIndicator.setStatus("current")


class _DocsIf3RxChStatusRcRmConnectivityId_Type(Unsigned32):
    """Custom type docsIf3RxChStatusRcRmConnectivityId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsIf3RxChStatusRcRmConnectivityId_Type.__name__ = "Unsigned32"
_DocsIf3RxChStatusRcRmConnectivityId_Object = MibTableColumn
docsIf3RxChStatusRcRmConnectivityId = _DocsIf3RxChStatusRcRmConnectivityId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 9, 1, 4),
    _DocsIf3RxChStatusRcRmConnectivityId_Type()
)
docsIf3RxChStatusRcRmConnectivityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3RxChStatusRcRmConnectivityId.setStatus("current")
_DocsIf3RxModuleCfgTable_Object = MibTable
docsIf3RxModuleCfgTable = _DocsIf3RxModuleCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 10)
)
if mibBuilder.loadTexts:
    docsIf3RxModuleCfgTable.setStatus("obsolete")
_DocsIf3RxModuleCfgEntry_Object = MibTableRow
docsIf3RxModuleCfgEntry = _DocsIf3RxModuleCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 10, 1)
)
docsIf3RxModuleCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF3-MIB", "docsIf3RccCfgRcpId"),
    (0, "DOCS-IF3-MIB", "docsIf3RccCfgRccCfgId"),
    (0, "DOCS-IF3-MIB", "docsIf3RxModuleCfgRmId"),
)
if mibBuilder.loadTexts:
    docsIf3RxModuleCfgEntry.setStatus("obsolete")


class _DocsIf3RxModuleCfgRmId_Type(Unsigned32):
    """Custom type docsIf3RxModuleCfgRmId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DocsIf3RxModuleCfgRmId_Type.__name__ = "Unsigned32"
_DocsIf3RxModuleCfgRmId_Object = MibTableColumn
docsIf3RxModuleCfgRmId = _DocsIf3RxModuleCfgRmId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 10, 1, 1),
    _DocsIf3RxModuleCfgRmId_Type()
)
docsIf3RxModuleCfgRmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf3RxModuleCfgRmId.setStatus("obsolete")


class _DocsIf3RxModuleCfgRmRmConnectivityId_Type(Unsigned32):
    """Custom type docsIf3RxModuleCfgRmRmConnectivityId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsIf3RxModuleCfgRmRmConnectivityId_Type.__name__ = "Unsigned32"
_DocsIf3RxModuleCfgRmRmConnectivityId_Object = MibTableColumn
docsIf3RxModuleCfgRmRmConnectivityId = _DocsIf3RxModuleCfgRmRmConnectivityId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 10, 1, 2),
    _DocsIf3RxModuleCfgRmRmConnectivityId_Type()
)
docsIf3RxModuleCfgRmRmConnectivityId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIf3RxModuleCfgRmRmConnectivityId.setStatus("obsolete")
_DocsIf3RxModuleCfgFirstCenterFrequency_Type = Unsigned32
_DocsIf3RxModuleCfgFirstCenterFrequency_Object = MibTableColumn
docsIf3RxModuleCfgFirstCenterFrequency = _DocsIf3RxModuleCfgFirstCenterFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 10, 1, 3),
    _DocsIf3RxModuleCfgFirstCenterFrequency_Type()
)
docsIf3RxModuleCfgFirstCenterFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIf3RxModuleCfgFirstCenterFrequency.setStatus("obsolete")
if mibBuilder.loadTexts:
    docsIf3RxModuleCfgFirstCenterFrequency.setUnits("Hz")
_DocsIf3RxModuleCfgRowStatus_Type = RowStatus
_DocsIf3RxModuleCfgRowStatus_Object = MibTableColumn
docsIf3RxModuleCfgRowStatus = _DocsIf3RxModuleCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 10, 1, 4),
    _DocsIf3RxModuleCfgRowStatus_Type()
)
docsIf3RxModuleCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIf3RxModuleCfgRowStatus.setStatus("obsolete")
_DocsIf3RxModuleStatusTable_Object = MibTable
docsIf3RxModuleStatusTable = _DocsIf3RxModuleStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 11)
)
if mibBuilder.loadTexts:
    docsIf3RxModuleStatusTable.setStatus("current")
_DocsIf3RxModuleStatusEntry_Object = MibTableRow
docsIf3RxModuleStatusEntry = _DocsIf3RxModuleStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 11, 1)
)
docsIf3RxModuleStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF3-MIB", "docsIf3RccStatusRcpId"),
    (0, "DOCS-IF3-MIB", "docsIf3RccStatusRccStatusId"),
    (0, "DOCS-IF3-MIB", "docsIf3RxModuleStatusRmId"),
)
if mibBuilder.loadTexts:
    docsIf3RxModuleStatusEntry.setStatus("current")


class _DocsIf3RxModuleStatusRmId_Type(Unsigned32):
    """Custom type docsIf3RxModuleStatusRmId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DocsIf3RxModuleStatusRmId_Type.__name__ = "Unsigned32"
_DocsIf3RxModuleStatusRmId_Object = MibTableColumn
docsIf3RxModuleStatusRmId = _DocsIf3RxModuleStatusRmId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 11, 1, 1),
    _DocsIf3RxModuleStatusRmId_Type()
)
docsIf3RxModuleStatusRmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf3RxModuleStatusRmId.setStatus("current")


class _DocsIf3RxModuleStatusRmRmConnectivityId_Type(Unsigned32):
    """Custom type docsIf3RxModuleStatusRmRmConnectivityId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsIf3RxModuleStatusRmRmConnectivityId_Type.__name__ = "Unsigned32"
_DocsIf3RxModuleStatusRmRmConnectivityId_Object = MibTableColumn
docsIf3RxModuleStatusRmRmConnectivityId = _DocsIf3RxModuleStatusRmRmConnectivityId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 11, 1, 2),
    _DocsIf3RxModuleStatusRmRmConnectivityId_Type()
)
docsIf3RxModuleStatusRmRmConnectivityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3RxModuleStatusRmRmConnectivityId.setStatus("current")
_DocsIf3RxModuleStatusFirstCenterFrequency_Type = Unsigned32
_DocsIf3RxModuleStatusFirstCenterFrequency_Object = MibTableColumn
docsIf3RxModuleStatusFirstCenterFrequency = _DocsIf3RxModuleStatusFirstCenterFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 11, 1, 3),
    _DocsIf3RxModuleStatusFirstCenterFrequency_Type()
)
docsIf3RxModuleStatusFirstCenterFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3RxModuleStatusFirstCenterFrequency.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3RxModuleStatusFirstCenterFrequency.setUnits("Hz")
_DocsIf3MdNodeStatusTable_Object = MibTable
docsIf3MdNodeStatusTable = _DocsIf3MdNodeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 12)
)
if mibBuilder.loadTexts:
    docsIf3MdNodeStatusTable.setStatus("current")
_DocsIf3MdNodeStatusEntry_Object = MibTableRow
docsIf3MdNodeStatusEntry = _DocsIf3MdNodeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 12, 1)
)
docsIf3MdNodeStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF3-MIB", "docsIf3MdNodeStatusNodeName"),
    (0, "DOCS-IF3-MIB", "docsIf3MdNodeStatusMdCmSgId"),
)
if mibBuilder.loadTexts:
    docsIf3MdNodeStatusEntry.setStatus("current")


class _DocsIf3MdNodeStatusNodeName_Type(NodeName):
    """Custom type docsIf3MdNodeStatusNodeName based on NodeName"""
    subtypeSpec = NodeName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_DocsIf3MdNodeStatusNodeName_Type.__name__ = "NodeName"
_DocsIf3MdNodeStatusNodeName_Object = MibTableColumn
docsIf3MdNodeStatusNodeName = _DocsIf3MdNodeStatusNodeName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 12, 1, 1),
    _DocsIf3MdNodeStatusNodeName_Type()
)
docsIf3MdNodeStatusNodeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf3MdNodeStatusNodeName.setStatus("current")


class _DocsIf3MdNodeStatusMdCmSgId_Type(Unsigned32):
    """Custom type docsIf3MdNodeStatusMdCmSgId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsIf3MdNodeStatusMdCmSgId_Type.__name__ = "Unsigned32"
_DocsIf3MdNodeStatusMdCmSgId_Object = MibTableColumn
docsIf3MdNodeStatusMdCmSgId = _DocsIf3MdNodeStatusMdCmSgId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 12, 1, 2),
    _DocsIf3MdNodeStatusMdCmSgId_Type()
)
docsIf3MdNodeStatusMdCmSgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf3MdNodeStatusMdCmSgId.setStatus("current")


class _DocsIf3MdNodeStatusMdDsSgId_Type(Unsigned32):
    """Custom type docsIf3MdNodeStatusMdDsSgId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DocsIf3MdNodeStatusMdDsSgId_Type.__name__ = "Unsigned32"
_DocsIf3MdNodeStatusMdDsSgId_Object = MibTableColumn
docsIf3MdNodeStatusMdDsSgId = _DocsIf3MdNodeStatusMdDsSgId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 12, 1, 3),
    _DocsIf3MdNodeStatusMdDsSgId_Type()
)
docsIf3MdNodeStatusMdDsSgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3MdNodeStatusMdDsSgId.setStatus("current")


class _DocsIf3MdNodeStatusMdUsSgId_Type(Unsigned32):
    """Custom type docsIf3MdNodeStatusMdUsSgId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DocsIf3MdNodeStatusMdUsSgId_Type.__name__ = "Unsigned32"
_DocsIf3MdNodeStatusMdUsSgId_Object = MibTableColumn
docsIf3MdNodeStatusMdUsSgId = _DocsIf3MdNodeStatusMdUsSgId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 12, 1, 4),
    _DocsIf3MdNodeStatusMdUsSgId_Type()
)
docsIf3MdNodeStatusMdUsSgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3MdNodeStatusMdUsSgId.setStatus("current")
_DocsIf3MdDsSgStatusTable_Object = MibTable
docsIf3MdDsSgStatusTable = _DocsIf3MdDsSgStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 13)
)
if mibBuilder.loadTexts:
    docsIf3MdDsSgStatusTable.setStatus("current")
_DocsIf3MdDsSgStatusEntry_Object = MibTableRow
docsIf3MdDsSgStatusEntry = _DocsIf3MdDsSgStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 13, 1)
)
docsIf3MdDsSgStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF3-MIB", "docsIf3MdDsSgStatusMdDsSgId"),
)
if mibBuilder.loadTexts:
    docsIf3MdDsSgStatusEntry.setStatus("current")


class _DocsIf3MdDsSgStatusMdDsSgId_Type(Unsigned32):
    """Custom type docsIf3MdDsSgStatusMdDsSgId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DocsIf3MdDsSgStatusMdDsSgId_Type.__name__ = "Unsigned32"
_DocsIf3MdDsSgStatusMdDsSgId_Object = MibTableColumn
docsIf3MdDsSgStatusMdDsSgId = _DocsIf3MdDsSgStatusMdDsSgId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 13, 1, 1),
    _DocsIf3MdDsSgStatusMdDsSgId_Type()
)
docsIf3MdDsSgStatusMdDsSgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf3MdDsSgStatusMdDsSgId.setStatus("current")
_DocsIf3MdDsSgStatusChSetId_Type = ChSetId
_DocsIf3MdDsSgStatusChSetId_Object = MibTableColumn
docsIf3MdDsSgStatusChSetId = _DocsIf3MdDsSgStatusChSetId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 13, 1, 2),
    _DocsIf3MdDsSgStatusChSetId_Type()
)
docsIf3MdDsSgStatusChSetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3MdDsSgStatusChSetId.setStatus("current")
_DocsIf3MdUsSgStatusTable_Object = MibTable
docsIf3MdUsSgStatusTable = _DocsIf3MdUsSgStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 14)
)
if mibBuilder.loadTexts:
    docsIf3MdUsSgStatusTable.setStatus("current")
_DocsIf3MdUsSgStatusEntry_Object = MibTableRow
docsIf3MdUsSgStatusEntry = _DocsIf3MdUsSgStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 14, 1)
)
docsIf3MdUsSgStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF3-MIB", "docsIf3MdUsSgStatusMdUsSgId"),
)
if mibBuilder.loadTexts:
    docsIf3MdUsSgStatusEntry.setStatus("current")


class _DocsIf3MdUsSgStatusMdUsSgId_Type(Unsigned32):
    """Custom type docsIf3MdUsSgStatusMdUsSgId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DocsIf3MdUsSgStatusMdUsSgId_Type.__name__ = "Unsigned32"
_DocsIf3MdUsSgStatusMdUsSgId_Object = MibTableColumn
docsIf3MdUsSgStatusMdUsSgId = _DocsIf3MdUsSgStatusMdUsSgId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 14, 1, 1),
    _DocsIf3MdUsSgStatusMdUsSgId_Type()
)
docsIf3MdUsSgStatusMdUsSgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf3MdUsSgStatusMdUsSgId.setStatus("current")
_DocsIf3MdUsSgStatusChSetId_Type = ChSetId
_DocsIf3MdUsSgStatusChSetId_Object = MibTableColumn
docsIf3MdUsSgStatusChSetId = _DocsIf3MdUsSgStatusChSetId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 14, 1, 2),
    _DocsIf3MdUsSgStatusChSetId_Type()
)
docsIf3MdUsSgStatusChSetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3MdUsSgStatusChSetId.setStatus("current")
_DocsIf3MdUsToDsChMappingTable_Object = MibTable
docsIf3MdUsToDsChMappingTable = _DocsIf3MdUsToDsChMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 15)
)
if mibBuilder.loadTexts:
    docsIf3MdUsToDsChMappingTable.setStatus("current")
_DocsIf3MdUsToDsChMappingEntry_Object = MibTableRow
docsIf3MdUsToDsChMappingEntry = _DocsIf3MdUsToDsChMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 15, 1)
)
docsIf3MdUsToDsChMappingEntry.setIndexNames(
    (0, "DOCS-IF3-MIB", "docsIf3MdUsToDsChMappingUsIfIndex"),
    (0, "DOCS-IF3-MIB", "docsIf3MdUsToDsChMappingDsIfIndex"),
    (0, "DOCS-IF3-MIB", "docsIf3MdUsToDsChMappingMdIfIndex"),
)
if mibBuilder.loadTexts:
    docsIf3MdUsToDsChMappingEntry.setStatus("current")
_DocsIf3MdUsToDsChMappingUsIfIndex_Type = InterfaceIndex
_DocsIf3MdUsToDsChMappingUsIfIndex_Object = MibTableColumn
docsIf3MdUsToDsChMappingUsIfIndex = _DocsIf3MdUsToDsChMappingUsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 15, 1, 1),
    _DocsIf3MdUsToDsChMappingUsIfIndex_Type()
)
docsIf3MdUsToDsChMappingUsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf3MdUsToDsChMappingUsIfIndex.setStatus("current")
_DocsIf3MdUsToDsChMappingDsIfIndex_Type = InterfaceIndex
_DocsIf3MdUsToDsChMappingDsIfIndex_Object = MibTableColumn
docsIf3MdUsToDsChMappingDsIfIndex = _DocsIf3MdUsToDsChMappingDsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 15, 1, 2),
    _DocsIf3MdUsToDsChMappingDsIfIndex_Type()
)
docsIf3MdUsToDsChMappingDsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf3MdUsToDsChMappingDsIfIndex.setStatus("current")
_DocsIf3MdUsToDsChMappingMdIfIndex_Type = InterfaceIndex
_DocsIf3MdUsToDsChMappingMdIfIndex_Object = MibTableColumn
docsIf3MdUsToDsChMappingMdIfIndex = _DocsIf3MdUsToDsChMappingMdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 15, 1, 3),
    _DocsIf3MdUsToDsChMappingMdIfIndex_Type()
)
docsIf3MdUsToDsChMappingMdIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3MdUsToDsChMappingMdIfIndex.setStatus("current")
_DocsIf3MdCfgTable_Object = MibTable
docsIf3MdCfgTable = _DocsIf3MdCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 16)
)
if mibBuilder.loadTexts:
    docsIf3MdCfgTable.setStatus("current")
_DocsIf3MdCfgEntry_Object = MibTableRow
docsIf3MdCfgEntry = _DocsIf3MdCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 16, 1)
)
docsIf3MdCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIf3MdCfgEntry.setStatus("current")


class _DocsIf3MdCfgMddInterval_Type(Unsigned32):
    """Custom type docsIf3MdCfgMddInterval based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_DocsIf3MdCfgMddInterval_Type.__name__ = "Unsigned32"
_DocsIf3MdCfgMddInterval_Object = MibTableColumn
docsIf3MdCfgMddInterval = _DocsIf3MdCfgMddInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 16, 1, 1),
    _DocsIf3MdCfgMddInterval_Type()
)
docsIf3MdCfgMddInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3MdCfgMddInterval.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3MdCfgMddInterval.setUnits("milliseconds")


class _DocsIf3MdCfgIpProvMode_Type(Integer32):
    """Custom type docsIf3MdCfgIpProvMode based on Integer32"""
    defaultValue = 1

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
        *(("alternate", 2),
          ("dualStack", 3),
          ("ipv4Only", 0),
          ("ipv6Only", 1))
    )


_DocsIf3MdCfgIpProvMode_Type.__name__ = "Integer32"
_DocsIf3MdCfgIpProvMode_Object = MibTableColumn
docsIf3MdCfgIpProvMode = _DocsIf3MdCfgIpProvMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 16, 1, 2),
    _DocsIf3MdCfgIpProvMode_Type()
)
docsIf3MdCfgIpProvMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3MdCfgIpProvMode.setStatus("current")


class _DocsIf3MdCfgCmStatusEvCtlEnabled_Type(TruthValue):
    """Custom type docsIf3MdCfgCmStatusEvCtlEnabled based on TruthValue"""


_DocsIf3MdCfgCmStatusEvCtlEnabled_Object = MibTableColumn
docsIf3MdCfgCmStatusEvCtlEnabled = _DocsIf3MdCfgCmStatusEvCtlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 16, 1, 3),
    _DocsIf3MdCfgCmStatusEvCtlEnabled_Type()
)
docsIf3MdCfgCmStatusEvCtlEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3MdCfgCmStatusEvCtlEnabled.setStatus("current")


class _DocsIf3MdCfgUsFreqRange_Type(Integer32):
    """Custom type docsIf3MdCfgUsFreqRange based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("extended", 1),
          ("standard", 0))
    )


_DocsIf3MdCfgUsFreqRange_Type.__name__ = "Integer32"
_DocsIf3MdCfgUsFreqRange_Object = MibTableColumn
docsIf3MdCfgUsFreqRange = _DocsIf3MdCfgUsFreqRange_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 16, 1, 4),
    _DocsIf3MdCfgUsFreqRange_Type()
)
docsIf3MdCfgUsFreqRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3MdCfgUsFreqRange.setStatus("current")


class _DocsIf3MdCfgMcastDsidFwdEnabled_Type(TruthValue):
    """Custom type docsIf3MdCfgMcastDsidFwdEnabled based on TruthValue"""


_DocsIf3MdCfgMcastDsidFwdEnabled_Object = MibTableColumn
docsIf3MdCfgMcastDsidFwdEnabled = _DocsIf3MdCfgMcastDsidFwdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 16, 1, 5),
    _DocsIf3MdCfgMcastDsidFwdEnabled_Type()
)
docsIf3MdCfgMcastDsidFwdEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3MdCfgMcastDsidFwdEnabled.setStatus("current")


class _DocsIf3MdCfgMultRxChModeEnabled_Type(TruthValue):
    """Custom type docsIf3MdCfgMultRxChModeEnabled based on TruthValue"""


_DocsIf3MdCfgMultRxChModeEnabled_Object = MibTableColumn
docsIf3MdCfgMultRxChModeEnabled = _DocsIf3MdCfgMultRxChModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 16, 1, 6),
    _DocsIf3MdCfgMultRxChModeEnabled_Type()
)
docsIf3MdCfgMultRxChModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3MdCfgMultRxChModeEnabled.setStatus("current")


class _DocsIf3MdCfgMultTxChModeEnabled_Type(TruthValue):
    """Custom type docsIf3MdCfgMultTxChModeEnabled based on TruthValue"""


_DocsIf3MdCfgMultTxChModeEnabled_Object = MibTableColumn
docsIf3MdCfgMultTxChModeEnabled = _DocsIf3MdCfgMultTxChModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 16, 1, 7),
    _DocsIf3MdCfgMultTxChModeEnabled_Type()
)
docsIf3MdCfgMultTxChModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3MdCfgMultTxChModeEnabled.setStatus("current")


class _DocsIf3MdCfgEarlyAuthEncrCtrl_Type(Integer32):
    """Custom type docsIf3MdCfgEarlyAuthEncrCtrl based on Integer32"""
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
        *(("disableEae", 1),
          ("enableEaeCapabilityBasedEnforcement", 3),
          ("enableEaeRangingBasedEnforcement", 2),
          ("enableEaeTotalEnforcement", 4))
    )


_DocsIf3MdCfgEarlyAuthEncrCtrl_Type.__name__ = "Integer32"
_DocsIf3MdCfgEarlyAuthEncrCtrl_Object = MibTableColumn
docsIf3MdCfgEarlyAuthEncrCtrl = _DocsIf3MdCfgEarlyAuthEncrCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 16, 1, 8),
    _DocsIf3MdCfgEarlyAuthEncrCtrl_Type()
)
docsIf3MdCfgEarlyAuthEncrCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3MdCfgEarlyAuthEncrCtrl.setStatus("current")


class _DocsIf3MdCfgTftpProxyEnabled_Type(TruthValue):
    """Custom type docsIf3MdCfgTftpProxyEnabled based on TruthValue"""


_DocsIf3MdCfgTftpProxyEnabled_Object = MibTableColumn
docsIf3MdCfgTftpProxyEnabled = _DocsIf3MdCfgTftpProxyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 16, 1, 9),
    _DocsIf3MdCfgTftpProxyEnabled_Type()
)
docsIf3MdCfgTftpProxyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3MdCfgTftpProxyEnabled.setStatus("current")


class _DocsIf3MdCfgSrcAddrVerifEnabled_Type(TruthValue):
    """Custom type docsIf3MdCfgSrcAddrVerifEnabled based on TruthValue"""


_DocsIf3MdCfgSrcAddrVerifEnabled_Object = MibTableColumn
docsIf3MdCfgSrcAddrVerifEnabled = _DocsIf3MdCfgSrcAddrVerifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 16, 1, 10),
    _DocsIf3MdCfgSrcAddrVerifEnabled_Type()
)
docsIf3MdCfgSrcAddrVerifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3MdCfgSrcAddrVerifEnabled.setStatus("current")


class _DocsIf3MdCfgDownChannelAnnex_Type(Integer32):
    """Custom type docsIf3MdCfgDownChannelAnnex based on Integer32"""
    defaultValue = 1

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
        *(("annexA", 3),
          ("annexB", 4),
          ("annexC", 5),
          ("other", 2),
          ("unknown", 1))
    )


_DocsIf3MdCfgDownChannelAnnex_Type.__name__ = "Integer32"
_DocsIf3MdCfgDownChannelAnnex_Object = MibTableColumn
docsIf3MdCfgDownChannelAnnex = _DocsIf3MdCfgDownChannelAnnex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 16, 1, 11),
    _DocsIf3MdCfgDownChannelAnnex_Type()
)
docsIf3MdCfgDownChannelAnnex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3MdCfgDownChannelAnnex.setStatus("current")


class _DocsIf3MdCfgCmUdcEnabled_Type(TruthValue):
    """Custom type docsIf3MdCfgCmUdcEnabled based on TruthValue"""


_DocsIf3MdCfgCmUdcEnabled_Object = MibTableColumn
docsIf3MdCfgCmUdcEnabled = _DocsIf3MdCfgCmUdcEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 16, 1, 12),
    _DocsIf3MdCfgCmUdcEnabled_Type()
)
docsIf3MdCfgCmUdcEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3MdCfgCmUdcEnabled.setStatus("current")


class _DocsIf3MdCfgSendUdcRulesEnabled_Type(TruthValue):
    """Custom type docsIf3MdCfgSendUdcRulesEnabled based on TruthValue"""


_DocsIf3MdCfgSendUdcRulesEnabled_Object = MibTableColumn
docsIf3MdCfgSendUdcRulesEnabled = _DocsIf3MdCfgSendUdcRulesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 16, 1, 13),
    _DocsIf3MdCfgSendUdcRulesEnabled_Type()
)
docsIf3MdCfgSendUdcRulesEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3MdCfgSendUdcRulesEnabled.setStatus("current")
_DocsIf3MdCfgServiceTypeIdList_Type = SnmpTagList
_DocsIf3MdCfgServiceTypeIdList_Object = MibTableColumn
docsIf3MdCfgServiceTypeIdList = _DocsIf3MdCfgServiceTypeIdList_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 16, 1, 14),
    _DocsIf3MdCfgServiceTypeIdList_Type()
)
docsIf3MdCfgServiceTypeIdList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3MdCfgServiceTypeIdList.setStatus("current")


class _DocsIf3MdCfgBpi2EnforceCtrl_Type(Integer32):
    """Custom type docsIf3MdCfgBpi2EnforceCtrl based on Integer32"""
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
        *(("disable", 0),
          ("qosCfgFile", 3),
          ("qosCfgFileWithBpi2AndCapabPrivSupportEnabled", 1),
          ("qosCfgFileWithBpi2Enabled", 2),
          ("total", 4))
    )


_DocsIf3MdCfgBpi2EnforceCtrl_Type.__name__ = "Integer32"
_DocsIf3MdCfgBpi2EnforceCtrl_Object = MibTableColumn
docsIf3MdCfgBpi2EnforceCtrl = _DocsIf3MdCfgBpi2EnforceCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 16, 1, 15),
    _DocsIf3MdCfgBpi2EnforceCtrl_Type()
)
docsIf3MdCfgBpi2EnforceCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3MdCfgBpi2EnforceCtrl.setStatus("current")


class _DocsIf3MdCfgEnergyMgt1x1Enabled_Type(TruthValue):
    """Custom type docsIf3MdCfgEnergyMgt1x1Enabled based on TruthValue"""


_DocsIf3MdCfgEnergyMgt1x1Enabled_Object = MibTableColumn
docsIf3MdCfgEnergyMgt1x1Enabled = _DocsIf3MdCfgEnergyMgt1x1Enabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 16, 1, 16),
    _DocsIf3MdCfgEnergyMgt1x1Enabled_Type()
)
docsIf3MdCfgEnergyMgt1x1Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3MdCfgEnergyMgt1x1Enabled.setStatus("current")
_DocsIf3BondingGrpCfgTable_Object = MibTable
docsIf3BondingGrpCfgTable = _DocsIf3BondingGrpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 17)
)
if mibBuilder.loadTexts:
    docsIf3BondingGrpCfgTable.setStatus("current")
_DocsIf3BondingGrpCfgEntry_Object = MibTableRow
docsIf3BondingGrpCfgEntry = _DocsIf3BondingGrpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 17, 1)
)
docsIf3BondingGrpCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF3-MIB", "docsIf3BondingGrpCfgDir"),
    (0, "DOCS-IF3-MIB", "docsIf3BondingGrpCfgCfgId"),
)
if mibBuilder.loadTexts:
    docsIf3BondingGrpCfgEntry.setStatus("current")
_DocsIf3BondingGrpCfgDir_Type = IfDirection
_DocsIf3BondingGrpCfgDir_Object = MibTableColumn
docsIf3BondingGrpCfgDir = _DocsIf3BondingGrpCfgDir_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 17, 1, 1),
    _DocsIf3BondingGrpCfgDir_Type()
)
docsIf3BondingGrpCfgDir.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf3BondingGrpCfgDir.setStatus("current")


class _DocsIf3BondingGrpCfgCfgId_Type(Unsigned32):
    """Custom type docsIf3BondingGrpCfgCfgId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DocsIf3BondingGrpCfgCfgId_Type.__name__ = "Unsigned32"
_DocsIf3BondingGrpCfgCfgId_Object = MibTableColumn
docsIf3BondingGrpCfgCfgId = _DocsIf3BondingGrpCfgCfgId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 17, 1, 2),
    _DocsIf3BondingGrpCfgCfgId_Type()
)
docsIf3BondingGrpCfgCfgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf3BondingGrpCfgCfgId.setStatus("current")


class _DocsIf3BondingGrpCfgChList_Type(ChannelList):
    """Custom type docsIf3BondingGrpCfgChList based on ChannelList"""
    subtypeSpec = ChannelList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_DocsIf3BondingGrpCfgChList_Type.__name__ = "ChannelList"
_DocsIf3BondingGrpCfgChList_Object = MibTableColumn
docsIf3BondingGrpCfgChList = _DocsIf3BondingGrpCfgChList_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 17, 1, 3),
    _DocsIf3BondingGrpCfgChList_Type()
)
docsIf3BondingGrpCfgChList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIf3BondingGrpCfgChList.setStatus("current")


class _DocsIf3BondingGrpCfgSfProvAttrMask_Type(AttributeMask):
    """Custom type docsIf3BondingGrpCfgSfProvAttrMask based on AttributeMask"""
    defaultHexValue = "80000000"


_DocsIf3BondingGrpCfgSfProvAttrMask_Object = MibTableColumn
docsIf3BondingGrpCfgSfProvAttrMask = _DocsIf3BondingGrpCfgSfProvAttrMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 17, 1, 4),
    _DocsIf3BondingGrpCfgSfProvAttrMask_Type()
)
docsIf3BondingGrpCfgSfProvAttrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIf3BondingGrpCfgSfProvAttrMask.setStatus("current")


class _DocsIf3BondingGrpCfgDsidReseqWaitTime_Type(Unsigned32):
    """Custom type docsIf3BondingGrpCfgDsidReseqWaitTime based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 180),
        ValueRangeConstraint(255, 255),
    )


_DocsIf3BondingGrpCfgDsidReseqWaitTime_Type.__name__ = "Unsigned32"
_DocsIf3BondingGrpCfgDsidReseqWaitTime_Object = MibTableColumn
docsIf3BondingGrpCfgDsidReseqWaitTime = _DocsIf3BondingGrpCfgDsidReseqWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 17, 1, 5),
    _DocsIf3BondingGrpCfgDsidReseqWaitTime_Type()
)
docsIf3BondingGrpCfgDsidReseqWaitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIf3BondingGrpCfgDsidReseqWaitTime.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3BondingGrpCfgDsidReseqWaitTime.setUnits("hundredMicroseconds")


class _DocsIf3BondingGrpCfgDsidReseqWarnThrshld_Type(Unsigned32):
    """Custom type docsIf3BondingGrpCfgDsidReseqWarnThrshld based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 179),
        ValueRangeConstraint(255, 255),
    )


_DocsIf3BondingGrpCfgDsidReseqWarnThrshld_Type.__name__ = "Unsigned32"
_DocsIf3BondingGrpCfgDsidReseqWarnThrshld_Object = MibTableColumn
docsIf3BondingGrpCfgDsidReseqWarnThrshld = _DocsIf3BondingGrpCfgDsidReseqWarnThrshld_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 17, 1, 6),
    _DocsIf3BondingGrpCfgDsidReseqWarnThrshld_Type()
)
docsIf3BondingGrpCfgDsidReseqWarnThrshld.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIf3BondingGrpCfgDsidReseqWarnThrshld.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3BondingGrpCfgDsidReseqWarnThrshld.setUnits("hundredMicroseconds")
_DocsIf3BondingGrpCfgRowStatus_Type = RowStatus
_DocsIf3BondingGrpCfgRowStatus_Object = MibTableColumn
docsIf3BondingGrpCfgRowStatus = _DocsIf3BondingGrpCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 17, 1, 7),
    _DocsIf3BondingGrpCfgRowStatus_Type()
)
docsIf3BondingGrpCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIf3BondingGrpCfgRowStatus.setStatus("current")
_DocsIf3DsBondingGrpStatusTable_Object = MibTable
docsIf3DsBondingGrpStatusTable = _DocsIf3DsBondingGrpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 18)
)
if mibBuilder.loadTexts:
    docsIf3DsBondingGrpStatusTable.setStatus("current")
_DocsIf3DsBondingGrpStatusEntry_Object = MibTableRow
docsIf3DsBondingGrpStatusEntry = _DocsIf3DsBondingGrpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 18, 1)
)
docsIf3DsBondingGrpStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF3-MIB", "docsIf3DsBondingGrpStatusChSetId"),
)
if mibBuilder.loadTexts:
    docsIf3DsBondingGrpStatusEntry.setStatus("current")
_DocsIf3DsBondingGrpStatusChSetId_Type = ChSetId
_DocsIf3DsBondingGrpStatusChSetId_Object = MibTableColumn
docsIf3DsBondingGrpStatusChSetId = _DocsIf3DsBondingGrpStatusChSetId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 18, 1, 1),
    _DocsIf3DsBondingGrpStatusChSetId_Type()
)
docsIf3DsBondingGrpStatusChSetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf3DsBondingGrpStatusChSetId.setStatus("current")


class _DocsIf3DsBondingGrpStatusMdDsSgId_Type(Unsigned32):
    """Custom type docsIf3DsBondingGrpStatusMdDsSgId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsIf3DsBondingGrpStatusMdDsSgId_Type.__name__ = "Unsigned32"
_DocsIf3DsBondingGrpStatusMdDsSgId_Object = MibTableColumn
docsIf3DsBondingGrpStatusMdDsSgId = _DocsIf3DsBondingGrpStatusMdDsSgId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 18, 1, 2),
    _DocsIf3DsBondingGrpStatusMdDsSgId_Type()
)
docsIf3DsBondingGrpStatusMdDsSgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3DsBondingGrpStatusMdDsSgId.setStatus("current")


class _DocsIf3DsBondingGrpStatusCfgId_Type(Unsigned32):
    """Custom type docsIf3DsBondingGrpStatusCfgId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsIf3DsBondingGrpStatusCfgId_Type.__name__ = "Unsigned32"
_DocsIf3DsBondingGrpStatusCfgId_Object = MibTableColumn
docsIf3DsBondingGrpStatusCfgId = _DocsIf3DsBondingGrpStatusCfgId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 18, 1, 3),
    _DocsIf3DsBondingGrpStatusCfgId_Type()
)
docsIf3DsBondingGrpStatusCfgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3DsBondingGrpStatusCfgId.setStatus("current")
_DocsIf3UsBondingGrpStatusTable_Object = MibTable
docsIf3UsBondingGrpStatusTable = _DocsIf3UsBondingGrpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 19)
)
if mibBuilder.loadTexts:
    docsIf3UsBondingGrpStatusTable.setStatus("current")
_DocsIf3UsBondingGrpStatusEntry_Object = MibTableRow
docsIf3UsBondingGrpStatusEntry = _DocsIf3UsBondingGrpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 19, 1)
)
docsIf3UsBondingGrpStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF3-MIB", "docsIf3UsBondingGrpStatusChSetId"),
)
if mibBuilder.loadTexts:
    docsIf3UsBondingGrpStatusEntry.setStatus("current")
_DocsIf3UsBondingGrpStatusChSetId_Type = ChSetId
_DocsIf3UsBondingGrpStatusChSetId_Object = MibTableColumn
docsIf3UsBondingGrpStatusChSetId = _DocsIf3UsBondingGrpStatusChSetId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 19, 1, 1),
    _DocsIf3UsBondingGrpStatusChSetId_Type()
)
docsIf3UsBondingGrpStatusChSetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf3UsBondingGrpStatusChSetId.setStatus("current")


class _DocsIf3UsBondingGrpStatusMdUsSgId_Type(Unsigned32):
    """Custom type docsIf3UsBondingGrpStatusMdUsSgId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsIf3UsBondingGrpStatusMdUsSgId_Type.__name__ = "Unsigned32"
_DocsIf3UsBondingGrpStatusMdUsSgId_Object = MibTableColumn
docsIf3UsBondingGrpStatusMdUsSgId = _DocsIf3UsBondingGrpStatusMdUsSgId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 19, 1, 2),
    _DocsIf3UsBondingGrpStatusMdUsSgId_Type()
)
docsIf3UsBondingGrpStatusMdUsSgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3UsBondingGrpStatusMdUsSgId.setStatus("current")


class _DocsIf3UsBondingGrpStatusCfgId_Type(Unsigned32):
    """Custom type docsIf3UsBondingGrpStatusCfgId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsIf3UsBondingGrpStatusCfgId_Type.__name__ = "Unsigned32"
_DocsIf3UsBondingGrpStatusCfgId_Object = MibTableColumn
docsIf3UsBondingGrpStatusCfgId = _DocsIf3UsBondingGrpStatusCfgId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 19, 1, 3),
    _DocsIf3UsBondingGrpStatusCfgId_Type()
)
docsIf3UsBondingGrpStatusCfgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3UsBondingGrpStatusCfgId.setStatus("current")
_DocsIf3UsChExtTable_Object = MibTable
docsIf3UsChExtTable = _DocsIf3UsChExtTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 20)
)
if mibBuilder.loadTexts:
    docsIf3UsChExtTable.setStatus("current")
_DocsIf3UsChExtEntry_Object = MibTableRow
docsIf3UsChExtEntry = _DocsIf3UsChExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 20, 1)
)
docsIf3UsChExtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIf3UsChExtEntry.setStatus("current")


class _DocsIf3UsChExtSacCodeHoppingSelectionMode_Type(Integer32):
    """Custom type docsIf3UsChExtSacCodeHoppingSelectionMode based on Integer32"""
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
        *(("none", 0),
          ("sac1CodeHoppingMode1", 2),
          ("sac1NoCodeHopping", 1),
          ("sac2CodeHoppingMode2", 3),
          ("sac2NoCodeHopping", 4))
    )


_DocsIf3UsChExtSacCodeHoppingSelectionMode_Type.__name__ = "Integer32"
_DocsIf3UsChExtSacCodeHoppingSelectionMode_Object = MibTableColumn
docsIf3UsChExtSacCodeHoppingSelectionMode = _DocsIf3UsChExtSacCodeHoppingSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 20, 1, 1),
    _DocsIf3UsChExtSacCodeHoppingSelectionMode_Type()
)
docsIf3UsChExtSacCodeHoppingSelectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3UsChExtSacCodeHoppingSelectionMode.setStatus("current")
_DocsIf3UsChExtScdmaSelectionStringActiveCodes_Type = ScdmaSelectionString
_DocsIf3UsChExtScdmaSelectionStringActiveCodes_Object = MibTableColumn
docsIf3UsChExtScdmaSelectionStringActiveCodes = _DocsIf3UsChExtScdmaSelectionStringActiveCodes_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 20, 1, 2),
    _DocsIf3UsChExtScdmaSelectionStringActiveCodes_Type()
)
docsIf3UsChExtScdmaSelectionStringActiveCodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3UsChExtScdmaSelectionStringActiveCodes.setStatus("current")
_DocsIf3CmCapabilities_ObjectIdentity = ObjectIdentity
docsIf3CmCapabilities = _DocsIf3CmCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 21)
)
_DocsIf3CmCapabilitiesReq_Type = Tlv8
_DocsIf3CmCapabilitiesReq_Object = MibScalar
docsIf3CmCapabilitiesReq = _DocsIf3CmCapabilitiesReq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 21, 1),
    _DocsIf3CmCapabilitiesReq_Type()
)
docsIf3CmCapabilitiesReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmCapabilitiesReq.setStatus("current")
_DocsIf3CmCapabilitiesRsp_Type = Tlv8
_DocsIf3CmCapabilitiesRsp_Object = MibScalar
docsIf3CmCapabilitiesRsp = _DocsIf3CmCapabilitiesRsp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 21, 2),
    _DocsIf3CmCapabilitiesRsp_Type()
)
docsIf3CmCapabilitiesRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmCapabilitiesRsp.setStatus("current")
_DocsIf3UsChSetTable_Object = MibTable
docsIf3UsChSetTable = _DocsIf3UsChSetTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 22)
)
if mibBuilder.loadTexts:
    docsIf3UsChSetTable.setStatus("current")
_DocsIf3UsChSetEntry_Object = MibTableRow
docsIf3UsChSetEntry = _DocsIf3UsChSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 22, 1)
)
docsIf3UsChSetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF3-MIB", "docsIf3UsChSetId"),
)
if mibBuilder.loadTexts:
    docsIf3UsChSetEntry.setStatus("current")
_DocsIf3UsChSetId_Type = ChSetId
_DocsIf3UsChSetId_Object = MibTableColumn
docsIf3UsChSetId = _DocsIf3UsChSetId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 22, 1, 1),
    _DocsIf3UsChSetId_Type()
)
docsIf3UsChSetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf3UsChSetId.setStatus("current")


class _DocsIf3UsChSetChList_Type(ChannelList):
    """Custom type docsIf3UsChSetChList based on ChannelList"""
    subtypeSpec = ChannelList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(2, 255),
    )


_DocsIf3UsChSetChList_Type.__name__ = "ChannelList"
_DocsIf3UsChSetChList_Object = MibTableColumn
docsIf3UsChSetChList = _DocsIf3UsChSetChList_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 22, 1, 2),
    _DocsIf3UsChSetChList_Type()
)
docsIf3UsChSetChList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3UsChSetChList.setStatus("current")
_DocsIf3DsChSetTable_Object = MibTable
docsIf3DsChSetTable = _DocsIf3DsChSetTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 23)
)
if mibBuilder.loadTexts:
    docsIf3DsChSetTable.setStatus("current")
_DocsIf3DsChSetEntry_Object = MibTableRow
docsIf3DsChSetEntry = _DocsIf3DsChSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 23, 1)
)
docsIf3DsChSetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF3-MIB", "docsIf3DsChSetId"),
)
if mibBuilder.loadTexts:
    docsIf3DsChSetEntry.setStatus("current")
_DocsIf3DsChSetId_Type = ChSetId
_DocsIf3DsChSetId_Object = MibTableColumn
docsIf3DsChSetId = _DocsIf3DsChSetId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 23, 1, 1),
    _DocsIf3DsChSetId_Type()
)
docsIf3DsChSetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf3DsChSetId.setStatus("current")


class _DocsIf3DsChSetChList_Type(ChannelList):
    """Custom type docsIf3DsChSetChList based on ChannelList"""
    subtypeSpec = ChannelList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(2, 255),
    )


_DocsIf3DsChSetChList_Type.__name__ = "ChannelList"
_DocsIf3DsChSetChList_Object = MibTableColumn
docsIf3DsChSetChList = _DocsIf3DsChSetChList_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 23, 1, 2),
    _DocsIf3DsChSetChList_Type()
)
docsIf3DsChSetChList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3DsChSetChList.setStatus("current")
_DocsIf3SignalQualityExtTable_Object = MibTable
docsIf3SignalQualityExtTable = _DocsIf3SignalQualityExtTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 24)
)
if mibBuilder.loadTexts:
    docsIf3SignalQualityExtTable.setStatus("current")
_DocsIf3SignalQualityExtEntry_Object = MibTableRow
docsIf3SignalQualityExtEntry = _DocsIf3SignalQualityExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 24, 1)
)
docsIf3SignalQualityExtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIf3SignalQualityExtEntry.setStatus("current")


class _DocsIf3SignalQualityExtRxMER_Type(TenthdB):
    """Custom type docsIf3SignalQualityExtRxMER based on TenthdB"""
    subtypeSpec = TenthdB.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_DocsIf3SignalQualityExtRxMER_Type.__name__ = "TenthdB"
_DocsIf3SignalQualityExtRxMER_Object = MibTableColumn
docsIf3SignalQualityExtRxMER = _DocsIf3SignalQualityExtRxMER_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 24, 1, 1),
    _DocsIf3SignalQualityExtRxMER_Type()
)
docsIf3SignalQualityExtRxMER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3SignalQualityExtRxMER.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3SignalQualityExtRxMER.setUnits("TenthdB")
_DocsIf3SignalQualityExtRxMerSamples_Type = Unsigned32
_DocsIf3SignalQualityExtRxMerSamples_Object = MibTableColumn
docsIf3SignalQualityExtRxMerSamples = _DocsIf3SignalQualityExtRxMerSamples_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 24, 1, 2),
    _DocsIf3SignalQualityExtRxMerSamples_Type()
)
docsIf3SignalQualityExtRxMerSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3SignalQualityExtRxMerSamples.setStatus("current")
_DocsIf3CmtsSignalQualityExtTable_Object = MibTable
docsIf3CmtsSignalQualityExtTable = _DocsIf3CmtsSignalQualityExtTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 25)
)
if mibBuilder.loadTexts:
    docsIf3CmtsSignalQualityExtTable.setStatus("current")
_DocsIf3CmtsSignalQualityExtEntry_Object = MibTableRow
docsIf3CmtsSignalQualityExtEntry = _DocsIf3CmtsSignalQualityExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 25, 1)
)
docsIf3CmtsSignalQualityExtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIf3CmtsSignalQualityExtEntry.setStatus("current")
_DocsIf3CmtsSignalQualityExtCNIR_Type = TenthdB
_DocsIf3CmtsSignalQualityExtCNIR_Object = MibTableColumn
docsIf3CmtsSignalQualityExtCNIR = _DocsIf3CmtsSignalQualityExtCNIR_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 25, 1, 1),
    _DocsIf3CmtsSignalQualityExtCNIR_Type()
)
docsIf3CmtsSignalQualityExtCNIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsSignalQualityExtCNIR.setStatus("current")
_DocsIf3CmtsSignalQualityExtExpectedRxSignalPower_Type = TenthdBmV
_DocsIf3CmtsSignalQualityExtExpectedRxSignalPower_Object = MibTableColumn
docsIf3CmtsSignalQualityExtExpectedRxSignalPower = _DocsIf3CmtsSignalQualityExtExpectedRxSignalPower_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 25, 1, 2),
    _DocsIf3CmtsSignalQualityExtExpectedRxSignalPower_Type()
)
docsIf3CmtsSignalQualityExtExpectedRxSignalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsSignalQualityExtExpectedRxSignalPower.setStatus("current")
_DocsIf3CmtsSpectrumAnalysisMeasTable_Object = MibTable
docsIf3CmtsSpectrumAnalysisMeasTable = _DocsIf3CmtsSpectrumAnalysisMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 26)
)
if mibBuilder.loadTexts:
    docsIf3CmtsSpectrumAnalysisMeasTable.setStatus("current")
_DocsIf3CmtsSpectrumAnalysisMeasEntry_Object = MibTableRow
docsIf3CmtsSpectrumAnalysisMeasEntry = _DocsIf3CmtsSpectrumAnalysisMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 26, 1)
)
docsIf3CmtsSpectrumAnalysisMeasEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIf3CmtsSpectrumAnalysisMeasEntry.setStatus("current")
_DocsIf3CmtsSpectrumAnalysisMeasAmplitudeData_Type = AmplitudeData
_DocsIf3CmtsSpectrumAnalysisMeasAmplitudeData_Object = MibTableColumn
docsIf3CmtsSpectrumAnalysisMeasAmplitudeData = _DocsIf3CmtsSpectrumAnalysisMeasAmplitudeData_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 26, 1, 1),
    _DocsIf3CmtsSpectrumAnalysisMeasAmplitudeData_Type()
)
docsIf3CmtsSpectrumAnalysisMeasAmplitudeData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsSpectrumAnalysisMeasAmplitudeData.setStatus("current")
_DocsIf3CmtsSpectrumAnalysisMeasTimeInterval_Type = Unsigned32
_DocsIf3CmtsSpectrumAnalysisMeasTimeInterval_Object = MibTableColumn
docsIf3CmtsSpectrumAnalysisMeasTimeInterval = _DocsIf3CmtsSpectrumAnalysisMeasTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 26, 1, 2),
    _DocsIf3CmtsSpectrumAnalysisMeasTimeInterval_Type()
)
docsIf3CmtsSpectrumAnalysisMeasTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsSpectrumAnalysisMeasTimeInterval.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmtsSpectrumAnalysisMeasTimeInterval.setUnits("milliseconds")
_DocsIf3CmtsSpectrumAnalysisMeasRowStatus_Type = RowStatus
_DocsIf3CmtsSpectrumAnalysisMeasRowStatus_Object = MibTableColumn
docsIf3CmtsSpectrumAnalysisMeasRowStatus = _DocsIf3CmtsSpectrumAnalysisMeasRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 26, 1, 3),
    _DocsIf3CmtsSpectrumAnalysisMeasRowStatus_Type()
)
docsIf3CmtsSpectrumAnalysisMeasRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIf3CmtsSpectrumAnalysisMeasRowStatus.setStatus("current")
_DocsIf3CmtsCmCtrl_ObjectIdentity = ObjectIdentity
docsIf3CmtsCmCtrl = _DocsIf3CmtsCmCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 27)
)


class _DocsIf3CmtsCmCtrlCmdMacAddr_Type(MacAddress):
    """Custom type docsIf3CmtsCmCtrlCmdMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_DocsIf3CmtsCmCtrlCmdMacAddr_Object = MibScalar
docsIf3CmtsCmCtrlCmdMacAddr = _DocsIf3CmtsCmCtrlCmdMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 27, 1),
    _DocsIf3CmtsCmCtrlCmdMacAddr_Type()
)
docsIf3CmtsCmCtrlCmdMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3CmtsCmCtrlCmdMacAddr.setStatus("current")


class _DocsIf3CmtsCmCtrlCmdMuteUsChId_Type(ChId):
    """Custom type docsIf3CmtsCmCtrlCmdMuteUsChId based on ChId"""
    defaultValue = 0


_DocsIf3CmtsCmCtrlCmdMuteUsChId_Object = MibScalar
docsIf3CmtsCmCtrlCmdMuteUsChId = _DocsIf3CmtsCmCtrlCmdMuteUsChId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 27, 2),
    _DocsIf3CmtsCmCtrlCmdMuteUsChId_Type()
)
docsIf3CmtsCmCtrlCmdMuteUsChId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3CmtsCmCtrlCmdMuteUsChId.setStatus("current")


class _DocsIf3CmtsCmCtrlCmdMuteInterval_Type(Unsigned32):
    """Custom type docsIf3CmtsCmCtrlCmdMuteInterval based on Unsigned32"""
    defaultValue = 1


_DocsIf3CmtsCmCtrlCmdMuteInterval_Object = MibScalar
docsIf3CmtsCmCtrlCmdMuteInterval = _DocsIf3CmtsCmCtrlCmdMuteInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 27, 3),
    _DocsIf3CmtsCmCtrlCmdMuteInterval_Type()
)
docsIf3CmtsCmCtrlCmdMuteInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3CmtsCmCtrlCmdMuteInterval.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmtsCmCtrlCmdMuteInterval.setUnits("milliseconds")


class _DocsIf3CmtsCmCtrlCmdDisableForwarding_Type(TruthValue):
    """Custom type docsIf3CmtsCmCtrlCmdDisableForwarding based on TruthValue"""


_DocsIf3CmtsCmCtrlCmdDisableForwarding_Object = MibScalar
docsIf3CmtsCmCtrlCmdDisableForwarding = _DocsIf3CmtsCmCtrlCmdDisableForwarding_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 27, 4),
    _DocsIf3CmtsCmCtrlCmdDisableForwarding_Type()
)
docsIf3CmtsCmCtrlCmdDisableForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3CmtsCmCtrlCmdDisableForwarding.setStatus("current")


class _DocsIf3CmtsCmCtrlCmdCommit_Type(Integer32):
    """Custom type docsIf3CmtsCmCtrlCmdCommit based on Integer32"""
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
        *(("cmReinit", 2),
          ("disableForwarding", 3),
          ("mute", 1))
    )


_DocsIf3CmtsCmCtrlCmdCommit_Type.__name__ = "Integer32"
_DocsIf3CmtsCmCtrlCmdCommit_Object = MibScalar
docsIf3CmtsCmCtrlCmdCommit = _DocsIf3CmtsCmCtrlCmdCommit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 27, 5),
    _DocsIf3CmtsCmCtrlCmdCommit_Type()
)
docsIf3CmtsCmCtrlCmdCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3CmtsCmCtrlCmdCommit.setStatus("current")
_DocsIf3CmDpvStatsTable_Object = MibTable
docsIf3CmDpvStatsTable = _DocsIf3CmDpvStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 28)
)
if mibBuilder.loadTexts:
    docsIf3CmDpvStatsTable.setStatus("current")
_DocsIf3CmDpvStatsEntry_Object = MibTableRow
docsIf3CmDpvStatsEntry = _DocsIf3CmDpvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 28, 1)
)
docsIf3CmDpvStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF3-MIB", "docsIf3CmDpvStatsGrpId"),
)
if mibBuilder.loadTexts:
    docsIf3CmDpvStatsEntry.setStatus("current")


class _DocsIf3CmDpvStatsGrpId_Type(Unsigned32):
    """Custom type docsIf3CmDpvStatsGrpId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DocsIf3CmDpvStatsGrpId_Type.__name__ = "Unsigned32"
_DocsIf3CmDpvStatsGrpId_Object = MibTableColumn
docsIf3CmDpvStatsGrpId = _DocsIf3CmDpvStatsGrpId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 28, 1, 1),
    _DocsIf3CmDpvStatsGrpId_Type()
)
docsIf3CmDpvStatsGrpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf3CmDpvStatsGrpId.setStatus("current")
_DocsIf3CmDpvStatsLastMeasLatency_Type = Unsigned32
_DocsIf3CmDpvStatsLastMeasLatency_Object = MibTableColumn
docsIf3CmDpvStatsLastMeasLatency = _DocsIf3CmDpvStatsLastMeasLatency_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 28, 1, 2),
    _DocsIf3CmDpvStatsLastMeasLatency_Type()
)
docsIf3CmDpvStatsLastMeasLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmDpvStatsLastMeasLatency.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmDpvStatsLastMeasLatency.setUnits("nanoseconds")
_DocsIf3CmDpvStatsLastMeasTime_Type = DateAndTime
_DocsIf3CmDpvStatsLastMeasTime_Object = MibTableColumn
docsIf3CmDpvStatsLastMeasTime = _DocsIf3CmDpvStatsLastMeasTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 28, 1, 3),
    _DocsIf3CmDpvStatsLastMeasTime_Type()
)
docsIf3CmDpvStatsLastMeasTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmDpvStatsLastMeasTime.setStatus("current")
_DocsIf3CmDpvStatsMinLatency_Type = Unsigned32
_DocsIf3CmDpvStatsMinLatency_Object = MibTableColumn
docsIf3CmDpvStatsMinLatency = _DocsIf3CmDpvStatsMinLatency_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 28, 1, 4),
    _DocsIf3CmDpvStatsMinLatency_Type()
)
docsIf3CmDpvStatsMinLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmDpvStatsMinLatency.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmDpvStatsMinLatency.setUnits("nanoseconds")
_DocsIf3CmDpvStatsMaxLatency_Type = Unsigned32
_DocsIf3CmDpvStatsMaxLatency_Object = MibTableColumn
docsIf3CmDpvStatsMaxLatency = _DocsIf3CmDpvStatsMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 28, 1, 5),
    _DocsIf3CmDpvStatsMaxLatency_Type()
)
docsIf3CmDpvStatsMaxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmDpvStatsMaxLatency.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmDpvStatsMaxLatency.setUnits("nanoseconds")
_DocsIf3CmDpvStatsAvgLatency_Type = Unsigned32
_DocsIf3CmDpvStatsAvgLatency_Object = MibTableColumn
docsIf3CmDpvStatsAvgLatency = _DocsIf3CmDpvStatsAvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 28, 1, 6),
    _DocsIf3CmDpvStatsAvgLatency_Type()
)
docsIf3CmDpvStatsAvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmDpvStatsAvgLatency.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmDpvStatsAvgLatency.setUnits("nanoseconds")
_DocsIf3CmDpvStatsNumMeas_Type = Unsigned32
_DocsIf3CmDpvStatsNumMeas_Object = MibTableColumn
docsIf3CmDpvStatsNumMeas = _DocsIf3CmDpvStatsNumMeas_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 28, 1, 7),
    _DocsIf3CmDpvStatsNumMeas_Type()
)
docsIf3CmDpvStatsNumMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmDpvStatsNumMeas.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmDpvStatsNumMeas.setUnits("measurements")
_DocsIf3CmDpvStatsLastClearTime_Type = DateAndTime
_DocsIf3CmDpvStatsLastClearTime_Object = MibTableColumn
docsIf3CmDpvStatsLastClearTime = _DocsIf3CmDpvStatsLastClearTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 28, 1, 8),
    _DocsIf3CmDpvStatsLastClearTime_Type()
)
docsIf3CmDpvStatsLastClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmDpvStatsLastClearTime.setStatus("current")
_DocsIf3CmEventCtrlTable_Object = MibTable
docsIf3CmEventCtrlTable = _DocsIf3CmEventCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 29)
)
if mibBuilder.loadTexts:
    docsIf3CmEventCtrlTable.setStatus("current")
_DocsIf3CmEventCtrlEntry_Object = MibTableRow
docsIf3CmEventCtrlEntry = _DocsIf3CmEventCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 29, 1)
)
docsIf3CmEventCtrlEntry.setIndexNames(
    (0, "DOCS-IF3-MIB", "docsIf3CmEventCtrlEventId"),
)
if mibBuilder.loadTexts:
    docsIf3CmEventCtrlEntry.setStatus("current")
_DocsIf3CmEventCtrlEventId_Type = Unsigned32
_DocsIf3CmEventCtrlEventId_Object = MibTableColumn
docsIf3CmEventCtrlEventId = _DocsIf3CmEventCtrlEventId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 29, 1, 1),
    _DocsIf3CmEventCtrlEventId_Type()
)
docsIf3CmEventCtrlEventId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf3CmEventCtrlEventId.setStatus("current")
_DocsIf3CmEventCtrlStatus_Type = RowStatus
_DocsIf3CmEventCtrlStatus_Object = MibTableColumn
docsIf3CmEventCtrlStatus = _DocsIf3CmEventCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 29, 1, 2),
    _DocsIf3CmEventCtrlStatus_Type()
)
docsIf3CmEventCtrlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIf3CmEventCtrlStatus.setStatus("current")
_DocsIf3CmtsEventCtrlTable_Object = MibTable
docsIf3CmtsEventCtrlTable = _DocsIf3CmtsEventCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 30)
)
if mibBuilder.loadTexts:
    docsIf3CmtsEventCtrlTable.setStatus("current")
_DocsIf3CmtsEventCtrlEntry_Object = MibTableRow
docsIf3CmtsEventCtrlEntry = _DocsIf3CmtsEventCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 30, 1)
)
docsIf3CmtsEventCtrlEntry.setIndexNames(
    (0, "DOCS-IF3-MIB", "docsIf3CmtsEventCtrlEventId"),
)
if mibBuilder.loadTexts:
    docsIf3CmtsEventCtrlEntry.setStatus("current")
_DocsIf3CmtsEventCtrlEventId_Type = Unsigned32
_DocsIf3CmtsEventCtrlEventId_Object = MibTableColumn
docsIf3CmtsEventCtrlEventId = _DocsIf3CmtsEventCtrlEventId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 30, 1, 1),
    _DocsIf3CmtsEventCtrlEventId_Type()
)
docsIf3CmtsEventCtrlEventId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf3CmtsEventCtrlEventId.setStatus("current")
_DocsIf3CmtsEventCtrlStatus_Type = RowStatus
_DocsIf3CmtsEventCtrlStatus_Object = MibTableColumn
docsIf3CmtsEventCtrlStatus = _DocsIf3CmtsEventCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 30, 1, 2),
    _DocsIf3CmtsEventCtrlStatus_Type()
)
docsIf3CmtsEventCtrlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIf3CmtsEventCtrlStatus.setStatus("current")
_DocsIf3CmMdCfgTable_Object = MibTable
docsIf3CmMdCfgTable = _DocsIf3CmMdCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 31)
)
if mibBuilder.loadTexts:
    docsIf3CmMdCfgTable.setStatus("current")
_DocsIf3CmMdCfgEntry_Object = MibTableRow
docsIf3CmMdCfgEntry = _DocsIf3CmMdCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 31, 1)
)
docsIf3CmMdCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIf3CmMdCfgEntry.setStatus("current")


class _DocsIf3CmMdCfgIpProvMode_Type(Integer32):
    """Custom type docsIf3CmMdCfgIpProvMode based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("honorMdd", 4),
          ("ipv4Only", 0),
          ("ipv6Only", 1))
    )


_DocsIf3CmMdCfgIpProvMode_Type.__name__ = "Integer32"
_DocsIf3CmMdCfgIpProvMode_Object = MibTableColumn
docsIf3CmMdCfgIpProvMode = _DocsIf3CmMdCfgIpProvMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 31, 1, 1),
    _DocsIf3CmMdCfgIpProvMode_Type()
)
docsIf3CmMdCfgIpProvMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3CmMdCfgIpProvMode.setStatus("current")


class _DocsIf3CmMdCfgIpProvModeResetOnChange_Type(TruthValue):
    """Custom type docsIf3CmMdCfgIpProvModeResetOnChange based on TruthValue"""


_DocsIf3CmMdCfgIpProvModeResetOnChange_Object = MibTableColumn
docsIf3CmMdCfgIpProvModeResetOnChange = _DocsIf3CmMdCfgIpProvModeResetOnChange_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 31, 1, 2),
    _DocsIf3CmMdCfgIpProvModeResetOnChange_Type()
)
docsIf3CmMdCfgIpProvModeResetOnChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3CmMdCfgIpProvModeResetOnChange.setStatus("current")


class _DocsIf3CmMdCfgIpProvModeResetOnChangeHoldOffTimer_Type(Unsigned32):
    """Custom type docsIf3CmMdCfgIpProvModeResetOnChangeHoldOffTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_DocsIf3CmMdCfgIpProvModeResetOnChangeHoldOffTimer_Type.__name__ = "Unsigned32"
_DocsIf3CmMdCfgIpProvModeResetOnChangeHoldOffTimer_Object = MibTableColumn
docsIf3CmMdCfgIpProvModeResetOnChangeHoldOffTimer = _DocsIf3CmMdCfgIpProvModeResetOnChangeHoldOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 31, 1, 3),
    _DocsIf3CmMdCfgIpProvModeResetOnChangeHoldOffTimer_Type()
)
docsIf3CmMdCfgIpProvModeResetOnChangeHoldOffTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3CmMdCfgIpProvModeResetOnChangeHoldOffTimer.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmMdCfgIpProvModeResetOnChangeHoldOffTimer.setUnits("seconds")


class _DocsIf3CmMdCfgIpProvModeStorageType_Type(StorageType):
    """Custom type docsIf3CmMdCfgIpProvModeStorageType based on StorageType"""


_DocsIf3CmMdCfgIpProvModeStorageType_Object = MibTableColumn
docsIf3CmMdCfgIpProvModeStorageType = _DocsIf3CmMdCfgIpProvModeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 31, 1, 4),
    _DocsIf3CmMdCfgIpProvModeStorageType_Type()
)
docsIf3CmMdCfgIpProvModeStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3CmMdCfgIpProvModeStorageType.setStatus("current")
_DocsIf3CmEnergyMgtCfg_ObjectIdentity = ObjectIdentity
docsIf3CmEnergyMgtCfg = _DocsIf3CmEnergyMgtCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 32)
)


class _DocsIf3CmEnergyMgtCfgFeatureEnabled_Type(Bits):
    """Custom type docsIf3CmEnergyMgtCfgFeatureEnabled based on Bits"""
    namedValues = NamedValues(
        *(("dls", 1),
          ("em1x1Feature", 0))
    )

_DocsIf3CmEnergyMgtCfgFeatureEnabled_Type.__name__ = "Bits"
_DocsIf3CmEnergyMgtCfgFeatureEnabled_Object = MibScalar
docsIf3CmEnergyMgtCfgFeatureEnabled = _DocsIf3CmEnergyMgtCfgFeatureEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 32, 1),
    _DocsIf3CmEnergyMgtCfgFeatureEnabled_Type()
)
docsIf3CmEnergyMgtCfgFeatureEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmEnergyMgtCfgFeatureEnabled.setStatus("current")


class _DocsIf3CmEnergyMgtCfgCyclePeriod_Type(Unsigned32):
    """Custom type docsIf3CmEnergyMgtCfgCyclePeriod based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsIf3CmEnergyMgtCfgCyclePeriod_Type.__name__ = "Unsigned32"
_DocsIf3CmEnergyMgtCfgCyclePeriod_Object = MibScalar
docsIf3CmEnergyMgtCfgCyclePeriod = _DocsIf3CmEnergyMgtCfgCyclePeriod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 32, 2),
    _DocsIf3CmEnergyMgtCfgCyclePeriod_Type()
)
docsIf3CmEnergyMgtCfgCyclePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmEnergyMgtCfgCyclePeriod.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmEnergyMgtCfgCyclePeriod.setUnits("seconds")
_DocsIf3CmEnergyMgt1x1CfgTable_Object = MibTable
docsIf3CmEnergyMgt1x1CfgTable = _DocsIf3CmEnergyMgt1x1CfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 33)
)
if mibBuilder.loadTexts:
    docsIf3CmEnergyMgt1x1CfgTable.setStatus("current")
_DocsIf3CmEnergyMgt1x1CfgEntry_Object = MibTableRow
docsIf3CmEnergyMgt1x1CfgEntry = _DocsIf3CmEnergyMgt1x1CfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 33, 1)
)
docsIf3CmEnergyMgt1x1CfgEntry.setIndexNames(
    (0, "DOCS-IF3-MIB", "docsIf3CmEnergyMgt1x1CfgDirection"),
)
if mibBuilder.loadTexts:
    docsIf3CmEnergyMgt1x1CfgEntry.setStatus("current")
_DocsIf3CmEnergyMgt1x1CfgDirection_Type = IfDirection
_DocsIf3CmEnergyMgt1x1CfgDirection_Object = MibTableColumn
docsIf3CmEnergyMgt1x1CfgDirection = _DocsIf3CmEnergyMgt1x1CfgDirection_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 33, 1, 1),
    _DocsIf3CmEnergyMgt1x1CfgDirection_Type()
)
docsIf3CmEnergyMgt1x1CfgDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf3CmEnergyMgt1x1CfgDirection.setStatus("current")
_DocsIf3CmEnergyMgt1x1CfgEntryBitrateThrshld_Type = Unsigned32
_DocsIf3CmEnergyMgt1x1CfgEntryBitrateThrshld_Object = MibTableColumn
docsIf3CmEnergyMgt1x1CfgEntryBitrateThrshld = _DocsIf3CmEnergyMgt1x1CfgEntryBitrateThrshld_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 33, 1, 2),
    _DocsIf3CmEnergyMgt1x1CfgEntryBitrateThrshld_Type()
)
docsIf3CmEnergyMgt1x1CfgEntryBitrateThrshld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3CmEnergyMgt1x1CfgEntryBitrateThrshld.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmEnergyMgt1x1CfgEntryBitrateThrshld.setUnits("bps")


class _DocsIf3CmEnergyMgt1x1CfgEntryTimeThrshld_Type(Unsigned32):
    """Custom type docsIf3CmEnergyMgt1x1CfgEntryTimeThrshld based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DocsIf3CmEnergyMgt1x1CfgEntryTimeThrshld_Type.__name__ = "Unsigned32"
_DocsIf3CmEnergyMgt1x1CfgEntryTimeThrshld_Object = MibTableColumn
docsIf3CmEnergyMgt1x1CfgEntryTimeThrshld = _DocsIf3CmEnergyMgt1x1CfgEntryTimeThrshld_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 33, 1, 3),
    _DocsIf3CmEnergyMgt1x1CfgEntryTimeThrshld_Type()
)
docsIf3CmEnergyMgt1x1CfgEntryTimeThrshld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3CmEnergyMgt1x1CfgEntryTimeThrshld.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmEnergyMgt1x1CfgEntryTimeThrshld.setUnits("seconds")
_DocsIf3CmEnergyMgt1x1CfgExitBitrateThrshld_Type = Unsigned32
_DocsIf3CmEnergyMgt1x1CfgExitBitrateThrshld_Object = MibTableColumn
docsIf3CmEnergyMgt1x1CfgExitBitrateThrshld = _DocsIf3CmEnergyMgt1x1CfgExitBitrateThrshld_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 33, 1, 4),
    _DocsIf3CmEnergyMgt1x1CfgExitBitrateThrshld_Type()
)
docsIf3CmEnergyMgt1x1CfgExitBitrateThrshld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3CmEnergyMgt1x1CfgExitBitrateThrshld.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmEnergyMgt1x1CfgExitBitrateThrshld.setUnits("bps")


class _DocsIf3CmEnergyMgt1x1CfgExitTimeThrshld_Type(Unsigned32):
    """Custom type docsIf3CmEnergyMgt1x1CfgExitTimeThrshld based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DocsIf3CmEnergyMgt1x1CfgExitTimeThrshld_Type.__name__ = "Unsigned32"
_DocsIf3CmEnergyMgt1x1CfgExitTimeThrshld_Object = MibTableColumn
docsIf3CmEnergyMgt1x1CfgExitTimeThrshld = _DocsIf3CmEnergyMgt1x1CfgExitTimeThrshld_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 33, 1, 5),
    _DocsIf3CmEnergyMgt1x1CfgExitTimeThrshld_Type()
)
docsIf3CmEnergyMgt1x1CfgExitTimeThrshld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3CmEnergyMgt1x1CfgExitTimeThrshld.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmEnergyMgt1x1CfgExitTimeThrshld.setUnits("seconds")
_DocsIf3CmSpectrumAnalysisCtrlCmd_ObjectIdentity = ObjectIdentity
docsIf3CmSpectrumAnalysisCtrlCmd = _DocsIf3CmSpectrumAnalysisCtrlCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 34)
)


class _DocsIf3CmSpectrumAnalysisCtrlCmdEnable_Type(TruthValue):
    """Custom type docsIf3CmSpectrumAnalysisCtrlCmdEnable based on TruthValue"""


_DocsIf3CmSpectrumAnalysisCtrlCmdEnable_Object = MibScalar
docsIf3CmSpectrumAnalysisCtrlCmdEnable = _DocsIf3CmSpectrumAnalysisCtrlCmdEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 34, 1),
    _DocsIf3CmSpectrumAnalysisCtrlCmdEnable_Type()
)
docsIf3CmSpectrumAnalysisCtrlCmdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3CmSpectrumAnalysisCtrlCmdEnable.setStatus("current")


class _DocsIf3CmSpectrumAnalysisCtrlCmdInactivityTimeout_Type(Integer32):
    """Custom type docsIf3CmSpectrumAnalysisCtrlCmdInactivityTimeout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_DocsIf3CmSpectrumAnalysisCtrlCmdInactivityTimeout_Type.__name__ = "Integer32"
_DocsIf3CmSpectrumAnalysisCtrlCmdInactivityTimeout_Object = MibScalar
docsIf3CmSpectrumAnalysisCtrlCmdInactivityTimeout = _DocsIf3CmSpectrumAnalysisCtrlCmdInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 34, 2),
    _DocsIf3CmSpectrumAnalysisCtrlCmdInactivityTimeout_Type()
)
docsIf3CmSpectrumAnalysisCtrlCmdInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3CmSpectrumAnalysisCtrlCmdInactivityTimeout.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmSpectrumAnalysisCtrlCmdInactivityTimeout.setUnits("seconds")


class _DocsIf3CmSpectrumAnalysisCtrlCmdFirstSegmentCenterFrequency_Type(Unsigned32):
    """Custom type docsIf3CmSpectrumAnalysisCtrlCmdFirstSegmentCenterFrequency based on Unsigned32"""
    defaultValue = 93000000


_DocsIf3CmSpectrumAnalysisCtrlCmdFirstSegmentCenterFrequency_Object = MibScalar
docsIf3CmSpectrumAnalysisCtrlCmdFirstSegmentCenterFrequency = _DocsIf3CmSpectrumAnalysisCtrlCmdFirstSegmentCenterFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 34, 3),
    _DocsIf3CmSpectrumAnalysisCtrlCmdFirstSegmentCenterFrequency_Type()
)
docsIf3CmSpectrumAnalysisCtrlCmdFirstSegmentCenterFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3CmSpectrumAnalysisCtrlCmdFirstSegmentCenterFrequency.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmSpectrumAnalysisCtrlCmdFirstSegmentCenterFrequency.setUnits("Hz")


class _DocsIf3CmSpectrumAnalysisCtrlCmdLastSegmentCenterFrequency_Type(Unsigned32):
    """Custom type docsIf3CmSpectrumAnalysisCtrlCmdLastSegmentCenterFrequency based on Unsigned32"""
    defaultValue = 993000000


_DocsIf3CmSpectrumAnalysisCtrlCmdLastSegmentCenterFrequency_Object = MibScalar
docsIf3CmSpectrumAnalysisCtrlCmdLastSegmentCenterFrequency = _DocsIf3CmSpectrumAnalysisCtrlCmdLastSegmentCenterFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 34, 4),
    _DocsIf3CmSpectrumAnalysisCtrlCmdLastSegmentCenterFrequency_Type()
)
docsIf3CmSpectrumAnalysisCtrlCmdLastSegmentCenterFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3CmSpectrumAnalysisCtrlCmdLastSegmentCenterFrequency.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmSpectrumAnalysisCtrlCmdLastSegmentCenterFrequency.setUnits("Hz")


class _DocsIf3CmSpectrumAnalysisCtrlCmdSegmentFrequencySpan_Type(Unsigned32):
    """Custom type docsIf3CmSpectrumAnalysisCtrlCmdSegmentFrequencySpan based on Unsigned32"""
    defaultValue = 7500000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000000, 900000000),
    )


_DocsIf3CmSpectrumAnalysisCtrlCmdSegmentFrequencySpan_Type.__name__ = "Unsigned32"
_DocsIf3CmSpectrumAnalysisCtrlCmdSegmentFrequencySpan_Object = MibScalar
docsIf3CmSpectrumAnalysisCtrlCmdSegmentFrequencySpan = _DocsIf3CmSpectrumAnalysisCtrlCmdSegmentFrequencySpan_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 34, 5),
    _DocsIf3CmSpectrumAnalysisCtrlCmdSegmentFrequencySpan_Type()
)
docsIf3CmSpectrumAnalysisCtrlCmdSegmentFrequencySpan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3CmSpectrumAnalysisCtrlCmdSegmentFrequencySpan.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmSpectrumAnalysisCtrlCmdSegmentFrequencySpan.setUnits("Hz")


class _DocsIf3CmSpectrumAnalysisCtrlCmdNumBinsPerSegment_Type(Unsigned32):
    """Custom type docsIf3CmSpectrumAnalysisCtrlCmdNumBinsPerSegment based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2048),
    )


_DocsIf3CmSpectrumAnalysisCtrlCmdNumBinsPerSegment_Type.__name__ = "Unsigned32"
_DocsIf3CmSpectrumAnalysisCtrlCmdNumBinsPerSegment_Object = MibScalar
docsIf3CmSpectrumAnalysisCtrlCmdNumBinsPerSegment = _DocsIf3CmSpectrumAnalysisCtrlCmdNumBinsPerSegment_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 34, 6),
    _DocsIf3CmSpectrumAnalysisCtrlCmdNumBinsPerSegment_Type()
)
docsIf3CmSpectrumAnalysisCtrlCmdNumBinsPerSegment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3CmSpectrumAnalysisCtrlCmdNumBinsPerSegment.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmSpectrumAnalysisCtrlCmdNumBinsPerSegment.setUnits("bins-per-segment")


class _DocsIf3CmSpectrumAnalysisCtrlCmdEquivalentNoiseBandwidth_Type(Unsigned32):
    """Custom type docsIf3CmSpectrumAnalysisCtrlCmdEquivalentNoiseBandwidth based on Unsigned32"""
    defaultValue = 150

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_DocsIf3CmSpectrumAnalysisCtrlCmdEquivalentNoiseBandwidth_Type.__name__ = "Unsigned32"
_DocsIf3CmSpectrumAnalysisCtrlCmdEquivalentNoiseBandwidth_Object = MibScalar
docsIf3CmSpectrumAnalysisCtrlCmdEquivalentNoiseBandwidth = _DocsIf3CmSpectrumAnalysisCtrlCmdEquivalentNoiseBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 34, 7),
    _DocsIf3CmSpectrumAnalysisCtrlCmdEquivalentNoiseBandwidth_Type()
)
docsIf3CmSpectrumAnalysisCtrlCmdEquivalentNoiseBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3CmSpectrumAnalysisCtrlCmdEquivalentNoiseBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmSpectrumAnalysisCtrlCmdEquivalentNoiseBandwidth.setUnits("hundredthsbin")
_DocsIf3CmSpectrumAnalysisCtrlCmdWindowFunction_Type = SpectrumAnalysisWindowFunction
_DocsIf3CmSpectrumAnalysisCtrlCmdWindowFunction_Object = MibScalar
docsIf3CmSpectrumAnalysisCtrlCmdWindowFunction = _DocsIf3CmSpectrumAnalysisCtrlCmdWindowFunction_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 34, 8),
    _DocsIf3CmSpectrumAnalysisCtrlCmdWindowFunction_Type()
)
docsIf3CmSpectrumAnalysisCtrlCmdWindowFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3CmSpectrumAnalysisCtrlCmdWindowFunction.setStatus("current")


class _DocsIf3CmSpectrumAnalysisCtrlCmdNumberOfAverages_Type(Unsigned32):
    """Custom type docsIf3CmSpectrumAnalysisCtrlCmdNumberOfAverages based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_DocsIf3CmSpectrumAnalysisCtrlCmdNumberOfAverages_Type.__name__ = "Unsigned32"
_DocsIf3CmSpectrumAnalysisCtrlCmdNumberOfAverages_Object = MibScalar
docsIf3CmSpectrumAnalysisCtrlCmdNumberOfAverages = _DocsIf3CmSpectrumAnalysisCtrlCmdNumberOfAverages_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 34, 9),
    _DocsIf3CmSpectrumAnalysisCtrlCmdNumberOfAverages_Type()
)
docsIf3CmSpectrumAnalysisCtrlCmdNumberOfAverages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIf3CmSpectrumAnalysisCtrlCmdNumberOfAverages.setStatus("current")
_DocsIf3CmSpectrumAnalysisMeasTable_Object = MibTable
docsIf3CmSpectrumAnalysisMeasTable = _DocsIf3CmSpectrumAnalysisMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 35)
)
if mibBuilder.loadTexts:
    docsIf3CmSpectrumAnalysisMeasTable.setStatus("current")
_DocsIf3CmSpectrumAnalysisMeasEntry_Object = MibTableRow
docsIf3CmSpectrumAnalysisMeasEntry = _DocsIf3CmSpectrumAnalysisMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 35, 1)
)
docsIf3CmSpectrumAnalysisMeasEntry.setIndexNames(
    (0, "DOCS-IF3-MIB", "docsIf3CmSpectrumAnalysisMeasFrequency"),
)
if mibBuilder.loadTexts:
    docsIf3CmSpectrumAnalysisMeasEntry.setStatus("current")
_DocsIf3CmSpectrumAnalysisMeasFrequency_Type = Integer32
_DocsIf3CmSpectrumAnalysisMeasFrequency_Object = MibTableColumn
docsIf3CmSpectrumAnalysisMeasFrequency = _DocsIf3CmSpectrumAnalysisMeasFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 35, 1, 1),
    _DocsIf3CmSpectrumAnalysisMeasFrequency_Type()
)
docsIf3CmSpectrumAnalysisMeasFrequency.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIf3CmSpectrumAnalysisMeasFrequency.setStatus("current")
_DocsIf3CmSpectrumAnalysisMeasAmplitudeData_Type = AmplitudeData
_DocsIf3CmSpectrumAnalysisMeasAmplitudeData_Object = MibTableColumn
docsIf3CmSpectrumAnalysisMeasAmplitudeData = _DocsIf3CmSpectrumAnalysisMeasAmplitudeData_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 35, 1, 2),
    _DocsIf3CmSpectrumAnalysisMeasAmplitudeData_Type()
)
docsIf3CmSpectrumAnalysisMeasAmplitudeData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmSpectrumAnalysisMeasAmplitudeData.setStatus("current")
_DocsIf3CmSpectrumAnalysisMeasTotalSegmentPower_Type = TenthdB
_DocsIf3CmSpectrumAnalysisMeasTotalSegmentPower_Object = MibTableColumn
docsIf3CmSpectrumAnalysisMeasTotalSegmentPower = _DocsIf3CmSpectrumAnalysisMeasTotalSegmentPower_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 35, 1, 3),
    _DocsIf3CmSpectrumAnalysisMeasTotalSegmentPower_Type()
)
docsIf3CmSpectrumAnalysisMeasTotalSegmentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmSpectrumAnalysisMeasTotalSegmentPower.setStatus("current")
_DocsIf3CmtsCmEmStatsTable_Object = MibTable
docsIf3CmtsCmEmStatsTable = _DocsIf3CmtsCmEmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 36)
)
if mibBuilder.loadTexts:
    docsIf3CmtsCmEmStatsTable.setStatus("current")
_DocsIf3CmtsCmEmStatsEntry_Object = MibTableRow
docsIf3CmtsCmEmStatsEntry = _DocsIf3CmtsCmEmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 36, 1)
)
docsIf3CmtsCmEmStatsEntry.setIndexNames(
    (0, "DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusId"),
)
if mibBuilder.loadTexts:
    docsIf3CmtsCmEmStatsEntry.setStatus("current")
_DocsIf3CmtsCmEmStatsEm1x1ModeTotalDuration_Type = Unsigned32
_DocsIf3CmtsCmEmStatsEm1x1ModeTotalDuration_Object = MibTableColumn
docsIf3CmtsCmEmStatsEm1x1ModeTotalDuration = _DocsIf3CmtsCmEmStatsEm1x1ModeTotalDuration_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 36, 1, 1),
    _DocsIf3CmtsCmEmStatsEm1x1ModeTotalDuration_Type()
)
docsIf3CmtsCmEmStatsEm1x1ModeTotalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmtsCmEmStatsEm1x1ModeTotalDuration.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmtsCmEmStatsEm1x1ModeTotalDuration.setUnits("seconds")
_DocsIf3CmEm1x1StatsTable_Object = MibTable
docsIf3CmEm1x1StatsTable = _DocsIf3CmEm1x1StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 37)
)
if mibBuilder.loadTexts:
    docsIf3CmEm1x1StatsTable.setStatus("current")
_DocsIf3CmEm1x1StatsEntry_Object = MibTableRow
docsIf3CmEm1x1StatsEntry = _DocsIf3CmEm1x1StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 37, 1)
)
docsIf3CmEm1x1StatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIf3CmEm1x1StatsEntry.setStatus("current")
_DocsIf3CmEm1x1StatsNumberTimesCrossedBelowUsEntryThrshlds_Type = Unsigned32
_DocsIf3CmEm1x1StatsNumberTimesCrossedBelowUsEntryThrshlds_Object = MibTableColumn
docsIf3CmEm1x1StatsNumberTimesCrossedBelowUsEntryThrshlds = _DocsIf3CmEm1x1StatsNumberTimesCrossedBelowUsEntryThrshlds_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 37, 1, 1),
    _DocsIf3CmEm1x1StatsNumberTimesCrossedBelowUsEntryThrshlds_Type()
)
docsIf3CmEm1x1StatsNumberTimesCrossedBelowUsEntryThrshlds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmEm1x1StatsNumberTimesCrossedBelowUsEntryThrshlds.setStatus("current")
_DocsIf3CmEm1x1StatsNumberTimesCrossedBelowDsEntryThrshlds_Type = Unsigned32
_DocsIf3CmEm1x1StatsNumberTimesCrossedBelowDsEntryThrshlds_Object = MibTableColumn
docsIf3CmEm1x1StatsNumberTimesCrossedBelowDsEntryThrshlds = _DocsIf3CmEm1x1StatsNumberTimesCrossedBelowDsEntryThrshlds_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 37, 1, 2),
    _DocsIf3CmEm1x1StatsNumberTimesCrossedBelowDsEntryThrshlds_Type()
)
docsIf3CmEm1x1StatsNumberTimesCrossedBelowDsEntryThrshlds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmEm1x1StatsNumberTimesCrossedBelowDsEntryThrshlds.setStatus("current")
_DocsIf3CmEm1x1StatsTotalDuration_Type = Unsigned32
_DocsIf3CmEm1x1StatsTotalDuration_Object = MibTableColumn
docsIf3CmEm1x1StatsTotalDuration = _DocsIf3CmEm1x1StatsTotalDuration_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 37, 1, 3),
    _DocsIf3CmEm1x1StatsTotalDuration_Type()
)
docsIf3CmEm1x1StatsTotalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmEm1x1StatsTotalDuration.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmEm1x1StatsTotalDuration.setUnits("seconds")
_DocsIf3CmEm1x1StatsTotalDurationBelowUsThrshlds_Type = Unsigned32
_DocsIf3CmEm1x1StatsTotalDurationBelowUsThrshlds_Object = MibTableColumn
docsIf3CmEm1x1StatsTotalDurationBelowUsThrshlds = _DocsIf3CmEm1x1StatsTotalDurationBelowUsThrshlds_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 37, 1, 4),
    _DocsIf3CmEm1x1StatsTotalDurationBelowUsThrshlds_Type()
)
docsIf3CmEm1x1StatsTotalDurationBelowUsThrshlds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmEm1x1StatsTotalDurationBelowUsThrshlds.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmEm1x1StatsTotalDurationBelowUsThrshlds.setUnits("seconds")
_DocsIf3CmEm1x1StatsTotalDurationBelowDsThrshlds_Type = Unsigned32
_DocsIf3CmEm1x1StatsTotalDurationBelowDsThrshlds_Object = MibTableColumn
docsIf3CmEm1x1StatsTotalDurationBelowDsThrshlds = _DocsIf3CmEm1x1StatsTotalDurationBelowDsThrshlds_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 37, 1, 5),
    _DocsIf3CmEm1x1StatsTotalDurationBelowDsThrshlds_Type()
)
docsIf3CmEm1x1StatsTotalDurationBelowDsThrshlds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmEm1x1StatsTotalDurationBelowDsThrshlds.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmEm1x1StatsTotalDurationBelowDsThrshlds.setUnits("seconds")
_DocsIf3CmEm1x1StatsTotalDurationBelowUsDsThrshlds_Type = Unsigned32
_DocsIf3CmEm1x1StatsTotalDurationBelowUsDsThrshlds_Object = MibTableColumn
docsIf3CmEm1x1StatsTotalDurationBelowUsDsThrshlds = _DocsIf3CmEm1x1StatsTotalDurationBelowUsDsThrshlds_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 1, 37, 1, 6),
    _DocsIf3CmEm1x1StatsTotalDurationBelowUsDsThrshlds_Type()
)
docsIf3CmEm1x1StatsTotalDurationBelowUsDsThrshlds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIf3CmEm1x1StatsTotalDurationBelowUsDsThrshlds.setStatus("current")
if mibBuilder.loadTexts:
    docsIf3CmEm1x1StatsTotalDurationBelowUsDsThrshlds.setUnits("seconds")
_DocsIf3MibConformance_ObjectIdentity = ObjectIdentity
docsIf3MibConformance = _DocsIf3MibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 2)
)
_DocsIf3MibCompliances_ObjectIdentity = ObjectIdentity
docsIf3MibCompliances = _DocsIf3MibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 2, 1)
)
_DocsIf3MibGroups_ObjectIdentity = ObjectIdentity
docsIf3MibGroups = _DocsIf3MibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 2, 2)
)

# Managed Objects groups

docsIf3CmtsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 2, 2, 1)
)
docsIf3CmtsGroup.setObjects(
      *(("DOCS-IF3-MIB", "docsIf3SignalQualityExtRxMER"),
        ("DOCS-IF3-MIB", "docsIf3SignalQualityExtRxMerSamples"),
        ("DOCS-IF3-MIB", "docsIf3MdNodeStatusMdDsSgId"),
        ("DOCS-IF3-MIB", "docsIf3MdNodeStatusMdUsSgId"),
        ("DOCS-IF3-MIB", "docsIf3MdDsSgStatusChSetId"),
        ("DOCS-IF3-MIB", "docsIf3MdUsSgStatusChSetId"),
        ("DOCS-IF3-MIB", "docsIf3CmtsSignalQualityExtCNIR"),
        ("DOCS-IF3-MIB", "docsIf3CmtsSignalQualityExtExpectedRxSignalPower"),
        ("DOCS-IF3-MIB", "docsIf3CmtsSpectrumAnalysisMeasAmplitudeData"),
        ("DOCS-IF3-MIB", "docsIf3CmtsSpectrumAnalysisMeasTimeInterval"),
        ("DOCS-IF3-MIB", "docsIf3CmtsSpectrumAnalysisMeasRowStatus"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusMacAddr"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusIPv6Addr"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusIPv6LinkLocal"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusIPv4Addr"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusValue"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusMdIfIndex"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusMdCmSgId"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusRcpId"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusRccStatusId"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusRcsId"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusTcsId"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusQosVersion"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusLastRegTime"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusAddrResolutionReqs"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusEnergyMgtEnabled"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusEnergyMgtOperStatus"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmUsStatusModulationType"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmUsStatusRxPower"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmUsStatusSignalNoise"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmUsStatusMicroreflections"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmUsStatusEqData"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmUsStatusUnerroreds"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmUsStatusCorrecteds"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmUsStatusUncorrectables"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmUsStatusHighResolutionTimingOffset"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmUsStatusIsMuted"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmUsStatusRangingStatus"),
        ("DOCS-IF3-MIB", "docsIf3UsChExtSacCodeHoppingSelectionMode"),
        ("DOCS-IF3-MIB", "docsIf3UsChExtScdmaSelectionStringActiveCodes"),
        ("DOCS-IF3-MIB", "docsIf3MdCfgMddInterval"),
        ("DOCS-IF3-MIB", "docsIf3MdCfgIpProvMode"),
        ("DOCS-IF3-MIB", "docsIf3MdCfgCmStatusEvCtlEnabled"),
        ("DOCS-IF3-MIB", "docsIf3MdCfgUsFreqRange"),
        ("DOCS-IF3-MIB", "docsIf3MdCfgMcastDsidFwdEnabled"),
        ("DOCS-IF3-MIB", "docsIf3MdCfgMultRxChModeEnabled"),
        ("DOCS-IF3-MIB", "docsIf3MdCfgMultTxChModeEnabled"),
        ("DOCS-IF3-MIB", "docsIf3MdCfgEarlyAuthEncrCtrl"),
        ("DOCS-IF3-MIB", "docsIf3MdCfgTftpProxyEnabled"),
        ("DOCS-IF3-MIB", "docsIf3MdCfgSrcAddrVerifEnabled"),
        ("DOCS-IF3-MIB", "docsIf3MdCfgDownChannelAnnex"),
        ("DOCS-IF3-MIB", "docsIf3MdCfgCmUdcEnabled"),
        ("DOCS-IF3-MIB", "docsIf3MdCfgSendUdcRulesEnabled"),
        ("DOCS-IF3-MIB", "docsIf3MdCfgServiceTypeIdList"),
        ("DOCS-IF3-MIB", "docsIf3MdCfgBpi2EnforceCtrl"),
        ("DOCS-IF3-MIB", "docsIf3MdCfgEnergyMgt1x1Enabled"),
        ("DOCS-IF3-MIB", "docsIf3MdChCfgIsPriCapableDs"),
        ("DOCS-IF3-MIB", "docsIf3MdChCfgChId"),
        ("DOCS-IF3-MIB", "docsIf3MdChCfgSfProvAttrMask"),
        ("DOCS-IF3-MIB", "docsIf3MdChCfgRowStatus"),
        ("DOCS-IF3-MIB", "docsIf3MdUsToDsChMappingMdIfIndex"),
        ("DOCS-IF3-MIB", "docsIf3DsChSetChList"),
        ("DOCS-IF3-MIB", "docsIf3UsChSetChList"),
        ("DOCS-IF3-MIB", "docsIf3BondingGrpCfgChList"),
        ("DOCS-IF3-MIB", "docsIf3BondingGrpCfgSfProvAttrMask"),
        ("DOCS-IF3-MIB", "docsIf3BondingGrpCfgDsidReseqWaitTime"),
        ("DOCS-IF3-MIB", "docsIf3BondingGrpCfgDsidReseqWarnThrshld"),
        ("DOCS-IF3-MIB", "docsIf3BondingGrpCfgRowStatus"),
        ("DOCS-IF3-MIB", "docsIf3DsBondingGrpStatusMdDsSgId"),
        ("DOCS-IF3-MIB", "docsIf3DsBondingGrpStatusCfgId"),
        ("DOCS-IF3-MIB", "docsIf3UsBondingGrpStatusMdUsSgId"),
        ("DOCS-IF3-MIB", "docsIf3UsBondingGrpStatusCfgId"),
        ("DOCS-IF3-MIB", "docsIf3RccStatusRccCfgId"),
        ("DOCS-IF3-MIB", "docsIf3RccStatusValidityCode"),
        ("DOCS-IF3-MIB", "docsIf3RccStatusValidityCodeText"),
        ("DOCS-IF3-MIB", "docsIf3RxChStatusChIfIndex"),
        ("DOCS-IF3-MIB", "docsIf3RxChStatusPrimaryDsIndicator"),
        ("DOCS-IF3-MIB", "docsIf3RxChStatusRcRmConnectivityId"),
        ("DOCS-IF3-MIB", "docsIf3RxModuleStatusRmRmConnectivityId"),
        ("DOCS-IF3-MIB", "docsIf3RxModuleStatusFirstCenterFrequency"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmCtrlCmdMacAddr"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmCtrlCmdMuteUsChId"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmCtrlCmdMuteInterval"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmCtrlCmdDisableForwarding"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmCtrlCmdCommit"),
        ("DOCS-IF3-MIB", "docsIf3CmtsEventCtrlStatus"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmEmStatsEm1x1ModeTotalDuration"))
)
if mibBuilder.loadTexts:
    docsIf3CmtsGroup.setStatus("current")

docsIf3CmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 2, 2, 2)
)
docsIf3CmGroup.setObjects(
      *(("DOCS-IF3-MIB", "docsIf3SignalQualityExtRxMER"),
        ("DOCS-IF3-MIB", "docsIf3SignalQualityExtRxMerSamples"),
        ("DOCS-IF3-MIB", "docsIf3CmStatusValue"),
        ("DOCS-IF3-MIB", "docsIf3CmStatusCode"),
        ("DOCS-IF3-MIB", "docsIf3CmStatusResets"),
        ("DOCS-IF3-MIB", "docsIf3CmStatusLostSyncs"),
        ("DOCS-IF3-MIB", "docsIf3CmStatusInvalidMaps"),
        ("DOCS-IF3-MIB", "docsIf3CmStatusInvalidUcds"),
        ("DOCS-IF3-MIB", "docsIf3CmStatusInvalidRangingRsps"),
        ("DOCS-IF3-MIB", "docsIf3CmStatusInvalidRegRsps"),
        ("DOCS-IF3-MIB", "docsIf3CmStatusT1Timeouts"),
        ("DOCS-IF3-MIB", "docsIf3CmStatusT2Timeouts"),
        ("DOCS-IF3-MIB", "docsIf3CmStatusEnergyMgt1x1OperStatus"),
        ("DOCS-IF3-MIB", "docsIf3CmStatusUsTxPower"),
        ("DOCS-IF3-MIB", "docsIf3CmStatusUsT3Timeouts"),
        ("DOCS-IF3-MIB", "docsIf3CmStatusUsT4Timeouts"),
        ("DOCS-IF3-MIB", "docsIf3CmStatusUsRangingAborteds"),
        ("DOCS-IF3-MIB", "docsIf3CmStatusUsModulationType"),
        ("DOCS-IF3-MIB", "docsIf3CmStatusUsEqData"),
        ("DOCS-IF3-MIB", "docsIf3CmStatusUsT3Exceededs"),
        ("DOCS-IF3-MIB", "docsIf3CmStatusUsIsMuted"),
        ("DOCS-IF3-MIB", "docsIf3CmStatusUsRangingStatus"),
        ("DOCS-IF3-MIB", "docsIf3CmCapabilitiesReq"),
        ("DOCS-IF3-MIB", "docsIf3CmCapabilitiesRsp"),
        ("DOCS-IF3-MIB", "docsIf3UsChExtSacCodeHoppingSelectionMode"),
        ("DOCS-IF3-MIB", "docsIf3UsChExtScdmaSelectionStringActiveCodes"),
        ("DOCS-IF3-MIB", "docsIf3RxChStatusChIfIndex"),
        ("DOCS-IF3-MIB", "docsIf3RxChStatusPrimaryDsIndicator"),
        ("DOCS-IF3-MIB", "docsIf3RxChStatusRcRmConnectivityId"),
        ("DOCS-IF3-MIB", "docsIf3RxModuleStatusRmRmConnectivityId"),
        ("DOCS-IF3-MIB", "docsIf3RxModuleStatusFirstCenterFrequency"),
        ("DOCS-IF3-MIB", "docsIf3CmDpvStatsLastMeasLatency"),
        ("DOCS-IF3-MIB", "docsIf3CmDpvStatsLastMeasTime"),
        ("DOCS-IF3-MIB", "docsIf3CmDpvStatsMinLatency"),
        ("DOCS-IF3-MIB", "docsIf3CmDpvStatsMaxLatency"),
        ("DOCS-IF3-MIB", "docsIf3CmDpvStatsAvgLatency"),
        ("DOCS-IF3-MIB", "docsIf3CmDpvStatsNumMeas"),
        ("DOCS-IF3-MIB", "docsIf3CmDpvStatsLastClearTime"),
        ("DOCS-IF3-MIB", "docsIf3CmEventCtrlStatus"),
        ("DOCS-IF3-MIB", "docsIf3CmMdCfgIpProvMode"),
        ("DOCS-IF3-MIB", "docsIf3CmMdCfgIpProvModeResetOnChange"),
        ("DOCS-IF3-MIB", "docsIf3CmMdCfgIpProvModeResetOnChangeHoldOffTimer"),
        ("DOCS-IF3-MIB", "docsIf3CmMdCfgIpProvModeStorageType"),
        ("DOCS-IF3-MIB", "docsIf3CmEnergyMgtCfgFeatureEnabled"),
        ("DOCS-IF3-MIB", "docsIf3CmEnergyMgtCfgCyclePeriod"),
        ("DOCS-IF3-MIB", "docsIf3CmEnergyMgt1x1CfgDirection"),
        ("DOCS-IF3-MIB", "docsIf3CmEnergyMgt1x1CfgEntryBitrateThrshld"),
        ("DOCS-IF3-MIB", "docsIf3CmEnergyMgt1x1CfgEntryTimeThrshld"),
        ("DOCS-IF3-MIB", "docsIf3CmEnergyMgt1x1CfgExitBitrateThrshld"),
        ("DOCS-IF3-MIB", "docsIf3CmEnergyMgt1x1CfgExitTimeThrshld"),
        ("DOCS-IF3-MIB", "docsIf3CmSpectrumAnalysisCtrlCmdEnable"),
        ("DOCS-IF3-MIB", "docsIf3CmSpectrumAnalysisCtrlCmdInactivityTimeout"),
        ("DOCS-IF3-MIB", "docsIf3CmSpectrumAnalysisCtrlCmdFirstSegmentCenterFrequency"),
        ("DOCS-IF3-MIB", "docsIf3CmSpectrumAnalysisCtrlCmdLastSegmentCenterFrequency"),
        ("DOCS-IF3-MIB", "docsIf3CmSpectrumAnalysisCtrlCmdSegmentFrequencySpan"),
        ("DOCS-IF3-MIB", "docsIf3CmSpectrumAnalysisCtrlCmdNumBinsPerSegment"),
        ("DOCS-IF3-MIB", "docsIf3CmSpectrumAnalysisCtrlCmdEquivalentNoiseBandwidth"),
        ("DOCS-IF3-MIB", "docsIf3CmSpectrumAnalysisCtrlCmdWindowFunction"),
        ("DOCS-IF3-MIB", "docsIf3CmSpectrumAnalysisCtrlCmdNumberOfAverages"),
        ("DOCS-IF3-MIB", "docsIf3CmSpectrumAnalysisMeasAmplitudeData"),
        ("DOCS-IF3-MIB", "docsIf3CmSpectrumAnalysisMeasTotalSegmentPower"),
        ("DOCS-IF3-MIB", "docsIf3CmEm1x1StatsNumberTimesCrossedBelowUsEntryThrshlds"),
        ("DOCS-IF3-MIB", "docsIf3CmEm1x1StatsNumberTimesCrossedBelowDsEntryThrshlds"),
        ("DOCS-IF3-MIB", "docsIf3CmEm1x1StatsTotalDuration"),
        ("DOCS-IF3-MIB", "docsIf3CmEm1x1StatsTotalDurationBelowUsThrshlds"),
        ("DOCS-IF3-MIB", "docsIf3CmEm1x1StatsTotalDurationBelowDsThrshlds"),
        ("DOCS-IF3-MIB", "docsIf3CmEm1x1StatsTotalDurationBelowUsDsThrshlds"))
)
if mibBuilder.loadTexts:
    docsIf3CmGroup.setStatus("current")

docsIf3ObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 2, 2, 5)
)
docsIf3ObsoleteGroup.setObjects(
      *(("DOCS-IF3-MIB", "docsIf3RccCfgVendorSpecific"),
        ("DOCS-IF3-MIB", "docsIf3RccCfgDescription"),
        ("DOCS-IF3-MIB", "docsIf3RccCfgRowStatus"),
        ("DOCS-IF3-MIB", "docsIf3RxChCfgChIfIndex"),
        ("DOCS-IF3-MIB", "docsIf3RxChCfgPrimaryDsIndicator"),
        ("DOCS-IF3-MIB", "docsIf3RxChCfgRcRmConnectivityId"),
        ("DOCS-IF3-MIB", "docsIf3RxChCfgRowStatus"),
        ("DOCS-IF3-MIB", "docsIf3RxModuleCfgRmRmConnectivityId"),
        ("DOCS-IF3-MIB", "docsIf3RxModuleCfgFirstCenterFrequency"),
        ("DOCS-IF3-MIB", "docsIf3RxModuleCfgRowStatus"),
        ("DOCS-IF3-MIB", "docsIf3CmStatusUCCsSuccesses"),
        ("DOCS-IF3-MIB", "docsIf3CmStatusUCCFails"))
)
if mibBuilder.loadTexts:
    docsIf3ObsoleteGroup.setStatus("obsolete")


# Notification objects

docsIf3CmtsEventNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 0, 1)
)
docsIf3CmtsEventNotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvLastTime"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    docsIf3CmtsEventNotif.setStatus(
        "current"
    )

docsIf3CmEventNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 0, 2)
)
docsIf3CmEventNotif.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvLastTime"))
)
if mibBuilder.loadTexts:
    docsIf3CmEventNotif.setStatus(
        "current"
    )


# Notifications groups

docsIf3CmtsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 2, 2, 3)
)
docsIf3CmtsNotificationGroup.setObjects(
    ("DOCS-IF3-MIB", "docsIf3CmtsEventNotif")
)
if mibBuilder.loadTexts:
    docsIf3CmtsNotificationGroup.setStatus(
        "current"
    )

docsIf3CmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 2, 2, 4)
)
docsIf3CmNotificationGroup.setObjects(
    ("DOCS-IF3-MIB", "docsIf3CmEventNotif")
)
if mibBuilder.loadTexts:
    docsIf3CmNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

docsIf3CmtsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 2, 1, 1)
)
if mibBuilder.loadTexts:
    docsIf3CmtsCompliance.setStatus(
        "current"
    )

docsIf3CmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 20, 2, 1, 2)
)
if mibBuilder.loadTexts:
    docsIf3CmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-IF3-MIB",
    **{"CmRegState": CmRegState,
       "CmtsCmRegState": CmtsCmRegState,
       "ScdmaSelectionString": ScdmaSelectionString,
       "AmplitudeData": AmplitudeData,
       "SpectrumAnalysisWindowFunction": SpectrumAnalysisWindowFunction,
       "Tlv8": Tlv8,
       "ChId": ChId,
       "ChSetId": ChSetId,
       "ChannelList": ChannelList,
       "AttributeMask": AttributeMask,
       "AttrAggrRuleMask": AttrAggrRuleMask,
       "RcpId": RcpId,
       "Dsid": Dsid,
       "RangingState": RangingState,
       "IfDirection": IfDirection,
       "docsIf3Mib": docsIf3Mib,
       "docsIf3Notifications": docsIf3Notifications,
       "docsIf3CmtsEventNotif": docsIf3CmtsEventNotif,
       "docsIf3CmEventNotif": docsIf3CmEventNotif,
       "docsIf3MibObjects": docsIf3MibObjects,
       "docsIf3CmStatusTable": docsIf3CmStatusTable,
       "docsIf3CmStatusEntry": docsIf3CmStatusEntry,
       "docsIf3CmStatusValue": docsIf3CmStatusValue,
       "docsIf3CmStatusCode": docsIf3CmStatusCode,
       "docsIf3CmStatusResets": docsIf3CmStatusResets,
       "docsIf3CmStatusLostSyncs": docsIf3CmStatusLostSyncs,
       "docsIf3CmStatusInvalidMaps": docsIf3CmStatusInvalidMaps,
       "docsIf3CmStatusInvalidUcds": docsIf3CmStatusInvalidUcds,
       "docsIf3CmStatusInvalidRangingRsps": docsIf3CmStatusInvalidRangingRsps,
       "docsIf3CmStatusInvalidRegRsps": docsIf3CmStatusInvalidRegRsps,
       "docsIf3CmStatusT1Timeouts": docsIf3CmStatusT1Timeouts,
       "docsIf3CmStatusT2Timeouts": docsIf3CmStatusT2Timeouts,
       "docsIf3CmStatusUCCsSuccesses": docsIf3CmStatusUCCsSuccesses,
       "docsIf3CmStatusUCCFails": docsIf3CmStatusUCCFails,
       "docsIf3CmStatusEnergyMgt1x1OperStatus": docsIf3CmStatusEnergyMgt1x1OperStatus,
       "docsIf3CmStatusUsTable": docsIf3CmStatusUsTable,
       "docsIf3CmStatusUsEntry": docsIf3CmStatusUsEntry,
       "docsIf3CmStatusUsTxPower": docsIf3CmStatusUsTxPower,
       "docsIf3CmStatusUsT3Timeouts": docsIf3CmStatusUsT3Timeouts,
       "docsIf3CmStatusUsT4Timeouts": docsIf3CmStatusUsT4Timeouts,
       "docsIf3CmStatusUsRangingAborteds": docsIf3CmStatusUsRangingAborteds,
       "docsIf3CmStatusUsModulationType": docsIf3CmStatusUsModulationType,
       "docsIf3CmStatusUsEqData": docsIf3CmStatusUsEqData,
       "docsIf3CmStatusUsT3Exceededs": docsIf3CmStatusUsT3Exceededs,
       "docsIf3CmStatusUsIsMuted": docsIf3CmStatusUsIsMuted,
       "docsIf3CmStatusUsRangingStatus": docsIf3CmStatusUsRangingStatus,
       "docsIf3CmtsCmRegStatusTable": docsIf3CmtsCmRegStatusTable,
       "docsIf3CmtsCmRegStatusEntry": docsIf3CmtsCmRegStatusEntry,
       "docsIf3CmtsCmRegStatusId": docsIf3CmtsCmRegStatusId,
       "docsIf3CmtsCmRegStatusMacAddr": docsIf3CmtsCmRegStatusMacAddr,
       "docsIf3CmtsCmRegStatusIPv6Addr": docsIf3CmtsCmRegStatusIPv6Addr,
       "docsIf3CmtsCmRegStatusIPv6LinkLocal": docsIf3CmtsCmRegStatusIPv6LinkLocal,
       "docsIf3CmtsCmRegStatusIPv4Addr": docsIf3CmtsCmRegStatusIPv4Addr,
       "docsIf3CmtsCmRegStatusValue": docsIf3CmtsCmRegStatusValue,
       "docsIf3CmtsCmRegStatusMdIfIndex": docsIf3CmtsCmRegStatusMdIfIndex,
       "docsIf3CmtsCmRegStatusMdCmSgId": docsIf3CmtsCmRegStatusMdCmSgId,
       "docsIf3CmtsCmRegStatusRcpId": docsIf3CmtsCmRegStatusRcpId,
       "docsIf3CmtsCmRegStatusRccStatusId": docsIf3CmtsCmRegStatusRccStatusId,
       "docsIf3CmtsCmRegStatusRcsId": docsIf3CmtsCmRegStatusRcsId,
       "docsIf3CmtsCmRegStatusTcsId": docsIf3CmtsCmRegStatusTcsId,
       "docsIf3CmtsCmRegStatusQosVersion": docsIf3CmtsCmRegStatusQosVersion,
       "docsIf3CmtsCmRegStatusLastRegTime": docsIf3CmtsCmRegStatusLastRegTime,
       "docsIf3CmtsCmRegStatusAddrResolutionReqs": docsIf3CmtsCmRegStatusAddrResolutionReqs,
       "docsIf3CmtsCmRegStatusEnergyMgtEnabled": docsIf3CmtsCmRegStatusEnergyMgtEnabled,
       "docsIf3CmtsCmRegStatusEnergyMgtOperStatus": docsIf3CmtsCmRegStatusEnergyMgtOperStatus,
       "docsIf3CmtsCmUsStatusTable": docsIf3CmtsCmUsStatusTable,
       "docsIf3CmtsCmUsStatusEntry": docsIf3CmtsCmUsStatusEntry,
       "docsIf3CmtsCmUsStatusChIfIndex": docsIf3CmtsCmUsStatusChIfIndex,
       "docsIf3CmtsCmUsStatusModulationType": docsIf3CmtsCmUsStatusModulationType,
       "docsIf3CmtsCmUsStatusRxPower": docsIf3CmtsCmUsStatusRxPower,
       "docsIf3CmtsCmUsStatusSignalNoise": docsIf3CmtsCmUsStatusSignalNoise,
       "docsIf3CmtsCmUsStatusMicroreflections": docsIf3CmtsCmUsStatusMicroreflections,
       "docsIf3CmtsCmUsStatusEqData": docsIf3CmtsCmUsStatusEqData,
       "docsIf3CmtsCmUsStatusUnerroreds": docsIf3CmtsCmUsStatusUnerroreds,
       "docsIf3CmtsCmUsStatusCorrecteds": docsIf3CmtsCmUsStatusCorrecteds,
       "docsIf3CmtsCmUsStatusUncorrectables": docsIf3CmtsCmUsStatusUncorrectables,
       "docsIf3CmtsCmUsStatusHighResolutionTimingOffset": docsIf3CmtsCmUsStatusHighResolutionTimingOffset,
       "docsIf3CmtsCmUsStatusIsMuted": docsIf3CmtsCmUsStatusIsMuted,
       "docsIf3CmtsCmUsStatusRangingStatus": docsIf3CmtsCmUsStatusRangingStatus,
       "docsIf3MdChCfgTable": docsIf3MdChCfgTable,
       "docsIf3MdChCfgEntry": docsIf3MdChCfgEntry,
       "docsIf3MdChCfgChIfIndex": docsIf3MdChCfgChIfIndex,
       "docsIf3MdChCfgIsPriCapableDs": docsIf3MdChCfgIsPriCapableDs,
       "docsIf3MdChCfgChId": docsIf3MdChCfgChId,
       "docsIf3MdChCfgSfProvAttrMask": docsIf3MdChCfgSfProvAttrMask,
       "docsIf3MdChCfgRowStatus": docsIf3MdChCfgRowStatus,
       "docsIf3RccCfgTable": docsIf3RccCfgTable,
       "docsIf3RccCfgEntry": docsIf3RccCfgEntry,
       "docsIf3RccCfgRcpId": docsIf3RccCfgRcpId,
       "docsIf3RccCfgRccCfgId": docsIf3RccCfgRccCfgId,
       "docsIf3RccCfgVendorSpecific": docsIf3RccCfgVendorSpecific,
       "docsIf3RccCfgDescription": docsIf3RccCfgDescription,
       "docsIf3RccCfgRowStatus": docsIf3RccCfgRowStatus,
       "docsIf3RccStatusTable": docsIf3RccStatusTable,
       "docsIf3RccStatusEntry": docsIf3RccStatusEntry,
       "docsIf3RccStatusRcpId": docsIf3RccStatusRcpId,
       "docsIf3RccStatusRccStatusId": docsIf3RccStatusRccStatusId,
       "docsIf3RccStatusRccCfgId": docsIf3RccStatusRccCfgId,
       "docsIf3RccStatusValidityCode": docsIf3RccStatusValidityCode,
       "docsIf3RccStatusValidityCodeText": docsIf3RccStatusValidityCodeText,
       "docsIf3RxChCfgTable": docsIf3RxChCfgTable,
       "docsIf3RxChCfgEntry": docsIf3RxChCfgEntry,
       "docsIf3RxChCfgRcId": docsIf3RxChCfgRcId,
       "docsIf3RxChCfgChIfIndex": docsIf3RxChCfgChIfIndex,
       "docsIf3RxChCfgPrimaryDsIndicator": docsIf3RxChCfgPrimaryDsIndicator,
       "docsIf3RxChCfgRcRmConnectivityId": docsIf3RxChCfgRcRmConnectivityId,
       "docsIf3RxChCfgRowStatus": docsIf3RxChCfgRowStatus,
       "docsIf3RxChStatusTable": docsIf3RxChStatusTable,
       "docsIf3RxChStatusEntry": docsIf3RxChStatusEntry,
       "docsIf3RxChStatusRcId": docsIf3RxChStatusRcId,
       "docsIf3RxChStatusChIfIndex": docsIf3RxChStatusChIfIndex,
       "docsIf3RxChStatusPrimaryDsIndicator": docsIf3RxChStatusPrimaryDsIndicator,
       "docsIf3RxChStatusRcRmConnectivityId": docsIf3RxChStatusRcRmConnectivityId,
       "docsIf3RxModuleCfgTable": docsIf3RxModuleCfgTable,
       "docsIf3RxModuleCfgEntry": docsIf3RxModuleCfgEntry,
       "docsIf3RxModuleCfgRmId": docsIf3RxModuleCfgRmId,
       "docsIf3RxModuleCfgRmRmConnectivityId": docsIf3RxModuleCfgRmRmConnectivityId,
       "docsIf3RxModuleCfgFirstCenterFrequency": docsIf3RxModuleCfgFirstCenterFrequency,
       "docsIf3RxModuleCfgRowStatus": docsIf3RxModuleCfgRowStatus,
       "docsIf3RxModuleStatusTable": docsIf3RxModuleStatusTable,
       "docsIf3RxModuleStatusEntry": docsIf3RxModuleStatusEntry,
       "docsIf3RxModuleStatusRmId": docsIf3RxModuleStatusRmId,
       "docsIf3RxModuleStatusRmRmConnectivityId": docsIf3RxModuleStatusRmRmConnectivityId,
       "docsIf3RxModuleStatusFirstCenterFrequency": docsIf3RxModuleStatusFirstCenterFrequency,
       "docsIf3MdNodeStatusTable": docsIf3MdNodeStatusTable,
       "docsIf3MdNodeStatusEntry": docsIf3MdNodeStatusEntry,
       "docsIf3MdNodeStatusNodeName": docsIf3MdNodeStatusNodeName,
       "docsIf3MdNodeStatusMdCmSgId": docsIf3MdNodeStatusMdCmSgId,
       "docsIf3MdNodeStatusMdDsSgId": docsIf3MdNodeStatusMdDsSgId,
       "docsIf3MdNodeStatusMdUsSgId": docsIf3MdNodeStatusMdUsSgId,
       "docsIf3MdDsSgStatusTable": docsIf3MdDsSgStatusTable,
       "docsIf3MdDsSgStatusEntry": docsIf3MdDsSgStatusEntry,
       "docsIf3MdDsSgStatusMdDsSgId": docsIf3MdDsSgStatusMdDsSgId,
       "docsIf3MdDsSgStatusChSetId": docsIf3MdDsSgStatusChSetId,
       "docsIf3MdUsSgStatusTable": docsIf3MdUsSgStatusTable,
       "docsIf3MdUsSgStatusEntry": docsIf3MdUsSgStatusEntry,
       "docsIf3MdUsSgStatusMdUsSgId": docsIf3MdUsSgStatusMdUsSgId,
       "docsIf3MdUsSgStatusChSetId": docsIf3MdUsSgStatusChSetId,
       "docsIf3MdUsToDsChMappingTable": docsIf3MdUsToDsChMappingTable,
       "docsIf3MdUsToDsChMappingEntry": docsIf3MdUsToDsChMappingEntry,
       "docsIf3MdUsToDsChMappingUsIfIndex": docsIf3MdUsToDsChMappingUsIfIndex,
       "docsIf3MdUsToDsChMappingDsIfIndex": docsIf3MdUsToDsChMappingDsIfIndex,
       "docsIf3MdUsToDsChMappingMdIfIndex": docsIf3MdUsToDsChMappingMdIfIndex,
       "docsIf3MdCfgTable": docsIf3MdCfgTable,
       "docsIf3MdCfgEntry": docsIf3MdCfgEntry,
       "docsIf3MdCfgMddInterval": docsIf3MdCfgMddInterval,
       "docsIf3MdCfgIpProvMode": docsIf3MdCfgIpProvMode,
       "docsIf3MdCfgCmStatusEvCtlEnabled": docsIf3MdCfgCmStatusEvCtlEnabled,
       "docsIf3MdCfgUsFreqRange": docsIf3MdCfgUsFreqRange,
       "docsIf3MdCfgMcastDsidFwdEnabled": docsIf3MdCfgMcastDsidFwdEnabled,
       "docsIf3MdCfgMultRxChModeEnabled": docsIf3MdCfgMultRxChModeEnabled,
       "docsIf3MdCfgMultTxChModeEnabled": docsIf3MdCfgMultTxChModeEnabled,
       "docsIf3MdCfgEarlyAuthEncrCtrl": docsIf3MdCfgEarlyAuthEncrCtrl,
       "docsIf3MdCfgTftpProxyEnabled": docsIf3MdCfgTftpProxyEnabled,
       "docsIf3MdCfgSrcAddrVerifEnabled": docsIf3MdCfgSrcAddrVerifEnabled,
       "docsIf3MdCfgDownChannelAnnex": docsIf3MdCfgDownChannelAnnex,
       "docsIf3MdCfgCmUdcEnabled": docsIf3MdCfgCmUdcEnabled,
       "docsIf3MdCfgSendUdcRulesEnabled": docsIf3MdCfgSendUdcRulesEnabled,
       "docsIf3MdCfgServiceTypeIdList": docsIf3MdCfgServiceTypeIdList,
       "docsIf3MdCfgBpi2EnforceCtrl": docsIf3MdCfgBpi2EnforceCtrl,
       "docsIf3MdCfgEnergyMgt1x1Enabled": docsIf3MdCfgEnergyMgt1x1Enabled,
       "docsIf3BondingGrpCfgTable": docsIf3BondingGrpCfgTable,
       "docsIf3BondingGrpCfgEntry": docsIf3BondingGrpCfgEntry,
       "docsIf3BondingGrpCfgDir": docsIf3BondingGrpCfgDir,
       "docsIf3BondingGrpCfgCfgId": docsIf3BondingGrpCfgCfgId,
       "docsIf3BondingGrpCfgChList": docsIf3BondingGrpCfgChList,
       "docsIf3BondingGrpCfgSfProvAttrMask": docsIf3BondingGrpCfgSfProvAttrMask,
       "docsIf3BondingGrpCfgDsidReseqWaitTime": docsIf3BondingGrpCfgDsidReseqWaitTime,
       "docsIf3BondingGrpCfgDsidReseqWarnThrshld": docsIf3BondingGrpCfgDsidReseqWarnThrshld,
       "docsIf3BondingGrpCfgRowStatus": docsIf3BondingGrpCfgRowStatus,
       "docsIf3DsBondingGrpStatusTable": docsIf3DsBondingGrpStatusTable,
       "docsIf3DsBondingGrpStatusEntry": docsIf3DsBondingGrpStatusEntry,
       "docsIf3DsBondingGrpStatusChSetId": docsIf3DsBondingGrpStatusChSetId,
       "docsIf3DsBondingGrpStatusMdDsSgId": docsIf3DsBondingGrpStatusMdDsSgId,
       "docsIf3DsBondingGrpStatusCfgId": docsIf3DsBondingGrpStatusCfgId,
       "docsIf3UsBondingGrpStatusTable": docsIf3UsBondingGrpStatusTable,
       "docsIf3UsBondingGrpStatusEntry": docsIf3UsBondingGrpStatusEntry,
       "docsIf3UsBondingGrpStatusChSetId": docsIf3UsBondingGrpStatusChSetId,
       "docsIf3UsBondingGrpStatusMdUsSgId": docsIf3UsBondingGrpStatusMdUsSgId,
       "docsIf3UsBondingGrpStatusCfgId": docsIf3UsBondingGrpStatusCfgId,
       "docsIf3UsChExtTable": docsIf3UsChExtTable,
       "docsIf3UsChExtEntry": docsIf3UsChExtEntry,
       "docsIf3UsChExtSacCodeHoppingSelectionMode": docsIf3UsChExtSacCodeHoppingSelectionMode,
       "docsIf3UsChExtScdmaSelectionStringActiveCodes": docsIf3UsChExtScdmaSelectionStringActiveCodes,
       "docsIf3CmCapabilities": docsIf3CmCapabilities,
       "docsIf3CmCapabilitiesReq": docsIf3CmCapabilitiesReq,
       "docsIf3CmCapabilitiesRsp": docsIf3CmCapabilitiesRsp,
       "docsIf3UsChSetTable": docsIf3UsChSetTable,
       "docsIf3UsChSetEntry": docsIf3UsChSetEntry,
       "docsIf3UsChSetId": docsIf3UsChSetId,
       "docsIf3UsChSetChList": docsIf3UsChSetChList,
       "docsIf3DsChSetTable": docsIf3DsChSetTable,
       "docsIf3DsChSetEntry": docsIf3DsChSetEntry,
       "docsIf3DsChSetId": docsIf3DsChSetId,
       "docsIf3DsChSetChList": docsIf3DsChSetChList,
       "docsIf3SignalQualityExtTable": docsIf3SignalQualityExtTable,
       "docsIf3SignalQualityExtEntry": docsIf3SignalQualityExtEntry,
       "docsIf3SignalQualityExtRxMER": docsIf3SignalQualityExtRxMER,
       "docsIf3SignalQualityExtRxMerSamples": docsIf3SignalQualityExtRxMerSamples,
       "docsIf3CmtsSignalQualityExtTable": docsIf3CmtsSignalQualityExtTable,
       "docsIf3CmtsSignalQualityExtEntry": docsIf3CmtsSignalQualityExtEntry,
       "docsIf3CmtsSignalQualityExtCNIR": docsIf3CmtsSignalQualityExtCNIR,
       "docsIf3CmtsSignalQualityExtExpectedRxSignalPower": docsIf3CmtsSignalQualityExtExpectedRxSignalPower,
       "docsIf3CmtsSpectrumAnalysisMeasTable": docsIf3CmtsSpectrumAnalysisMeasTable,
       "docsIf3CmtsSpectrumAnalysisMeasEntry": docsIf3CmtsSpectrumAnalysisMeasEntry,
       "docsIf3CmtsSpectrumAnalysisMeasAmplitudeData": docsIf3CmtsSpectrumAnalysisMeasAmplitudeData,
       "docsIf3CmtsSpectrumAnalysisMeasTimeInterval": docsIf3CmtsSpectrumAnalysisMeasTimeInterval,
       "docsIf3CmtsSpectrumAnalysisMeasRowStatus": docsIf3CmtsSpectrumAnalysisMeasRowStatus,
       "docsIf3CmtsCmCtrl": docsIf3CmtsCmCtrl,
       "docsIf3CmtsCmCtrlCmdMacAddr": docsIf3CmtsCmCtrlCmdMacAddr,
       "docsIf3CmtsCmCtrlCmdMuteUsChId": docsIf3CmtsCmCtrlCmdMuteUsChId,
       "docsIf3CmtsCmCtrlCmdMuteInterval": docsIf3CmtsCmCtrlCmdMuteInterval,
       "docsIf3CmtsCmCtrlCmdDisableForwarding": docsIf3CmtsCmCtrlCmdDisableForwarding,
       "docsIf3CmtsCmCtrlCmdCommit": docsIf3CmtsCmCtrlCmdCommit,
       "docsIf3CmDpvStatsTable": docsIf3CmDpvStatsTable,
       "docsIf3CmDpvStatsEntry": docsIf3CmDpvStatsEntry,
       "docsIf3CmDpvStatsGrpId": docsIf3CmDpvStatsGrpId,
       "docsIf3CmDpvStatsLastMeasLatency": docsIf3CmDpvStatsLastMeasLatency,
       "docsIf3CmDpvStatsLastMeasTime": docsIf3CmDpvStatsLastMeasTime,
       "docsIf3CmDpvStatsMinLatency": docsIf3CmDpvStatsMinLatency,
       "docsIf3CmDpvStatsMaxLatency": docsIf3CmDpvStatsMaxLatency,
       "docsIf3CmDpvStatsAvgLatency": docsIf3CmDpvStatsAvgLatency,
       "docsIf3CmDpvStatsNumMeas": docsIf3CmDpvStatsNumMeas,
       "docsIf3CmDpvStatsLastClearTime": docsIf3CmDpvStatsLastClearTime,
       "docsIf3CmEventCtrlTable": docsIf3CmEventCtrlTable,
       "docsIf3CmEventCtrlEntry": docsIf3CmEventCtrlEntry,
       "docsIf3CmEventCtrlEventId": docsIf3CmEventCtrlEventId,
       "docsIf3CmEventCtrlStatus": docsIf3CmEventCtrlStatus,
       "docsIf3CmtsEventCtrlTable": docsIf3CmtsEventCtrlTable,
       "docsIf3CmtsEventCtrlEntry": docsIf3CmtsEventCtrlEntry,
       "docsIf3CmtsEventCtrlEventId": docsIf3CmtsEventCtrlEventId,
       "docsIf3CmtsEventCtrlStatus": docsIf3CmtsEventCtrlStatus,
       "docsIf3CmMdCfgTable": docsIf3CmMdCfgTable,
       "docsIf3CmMdCfgEntry": docsIf3CmMdCfgEntry,
       "docsIf3CmMdCfgIpProvMode": docsIf3CmMdCfgIpProvMode,
       "docsIf3CmMdCfgIpProvModeResetOnChange": docsIf3CmMdCfgIpProvModeResetOnChange,
       "docsIf3CmMdCfgIpProvModeResetOnChangeHoldOffTimer": docsIf3CmMdCfgIpProvModeResetOnChangeHoldOffTimer,
       "docsIf3CmMdCfgIpProvModeStorageType": docsIf3CmMdCfgIpProvModeStorageType,
       "docsIf3CmEnergyMgtCfg": docsIf3CmEnergyMgtCfg,
       "docsIf3CmEnergyMgtCfgFeatureEnabled": docsIf3CmEnergyMgtCfgFeatureEnabled,
       "docsIf3CmEnergyMgtCfgCyclePeriod": docsIf3CmEnergyMgtCfgCyclePeriod,
       "docsIf3CmEnergyMgt1x1CfgTable": docsIf3CmEnergyMgt1x1CfgTable,
       "docsIf3CmEnergyMgt1x1CfgEntry": docsIf3CmEnergyMgt1x1CfgEntry,
       "docsIf3CmEnergyMgt1x1CfgDirection": docsIf3CmEnergyMgt1x1CfgDirection,
       "docsIf3CmEnergyMgt1x1CfgEntryBitrateThrshld": docsIf3CmEnergyMgt1x1CfgEntryBitrateThrshld,
       "docsIf3CmEnergyMgt1x1CfgEntryTimeThrshld": docsIf3CmEnergyMgt1x1CfgEntryTimeThrshld,
       "docsIf3CmEnergyMgt1x1CfgExitBitrateThrshld": docsIf3CmEnergyMgt1x1CfgExitBitrateThrshld,
       "docsIf3CmEnergyMgt1x1CfgExitTimeThrshld": docsIf3CmEnergyMgt1x1CfgExitTimeThrshld,
       "docsIf3CmSpectrumAnalysisCtrlCmd": docsIf3CmSpectrumAnalysisCtrlCmd,
       "docsIf3CmSpectrumAnalysisCtrlCmdEnable": docsIf3CmSpectrumAnalysisCtrlCmdEnable,
       "docsIf3CmSpectrumAnalysisCtrlCmdInactivityTimeout": docsIf3CmSpectrumAnalysisCtrlCmdInactivityTimeout,
       "docsIf3CmSpectrumAnalysisCtrlCmdFirstSegmentCenterFrequency": docsIf3CmSpectrumAnalysisCtrlCmdFirstSegmentCenterFrequency,
       "docsIf3CmSpectrumAnalysisCtrlCmdLastSegmentCenterFrequency": docsIf3CmSpectrumAnalysisCtrlCmdLastSegmentCenterFrequency,
       "docsIf3CmSpectrumAnalysisCtrlCmdSegmentFrequencySpan": docsIf3CmSpectrumAnalysisCtrlCmdSegmentFrequencySpan,
       "docsIf3CmSpectrumAnalysisCtrlCmdNumBinsPerSegment": docsIf3CmSpectrumAnalysisCtrlCmdNumBinsPerSegment,
       "docsIf3CmSpectrumAnalysisCtrlCmdEquivalentNoiseBandwidth": docsIf3CmSpectrumAnalysisCtrlCmdEquivalentNoiseBandwidth,
       "docsIf3CmSpectrumAnalysisCtrlCmdWindowFunction": docsIf3CmSpectrumAnalysisCtrlCmdWindowFunction,
       "docsIf3CmSpectrumAnalysisCtrlCmdNumberOfAverages": docsIf3CmSpectrumAnalysisCtrlCmdNumberOfAverages,
       "docsIf3CmSpectrumAnalysisMeasTable": docsIf3CmSpectrumAnalysisMeasTable,
       "docsIf3CmSpectrumAnalysisMeasEntry": docsIf3CmSpectrumAnalysisMeasEntry,
       "docsIf3CmSpectrumAnalysisMeasFrequency": docsIf3CmSpectrumAnalysisMeasFrequency,
       "docsIf3CmSpectrumAnalysisMeasAmplitudeData": docsIf3CmSpectrumAnalysisMeasAmplitudeData,
       "docsIf3CmSpectrumAnalysisMeasTotalSegmentPower": docsIf3CmSpectrumAnalysisMeasTotalSegmentPower,
       "docsIf3CmtsCmEmStatsTable": docsIf3CmtsCmEmStatsTable,
       "docsIf3CmtsCmEmStatsEntry": docsIf3CmtsCmEmStatsEntry,
       "docsIf3CmtsCmEmStatsEm1x1ModeTotalDuration": docsIf3CmtsCmEmStatsEm1x1ModeTotalDuration,
       "docsIf3CmEm1x1StatsTable": docsIf3CmEm1x1StatsTable,
       "docsIf3CmEm1x1StatsEntry": docsIf3CmEm1x1StatsEntry,
       "docsIf3CmEm1x1StatsNumberTimesCrossedBelowUsEntryThrshlds": docsIf3CmEm1x1StatsNumberTimesCrossedBelowUsEntryThrshlds,
       "docsIf3CmEm1x1StatsNumberTimesCrossedBelowDsEntryThrshlds": docsIf3CmEm1x1StatsNumberTimesCrossedBelowDsEntryThrshlds,
       "docsIf3CmEm1x1StatsTotalDuration": docsIf3CmEm1x1StatsTotalDuration,
       "docsIf3CmEm1x1StatsTotalDurationBelowUsThrshlds": docsIf3CmEm1x1StatsTotalDurationBelowUsThrshlds,
       "docsIf3CmEm1x1StatsTotalDurationBelowDsThrshlds": docsIf3CmEm1x1StatsTotalDurationBelowDsThrshlds,
       "docsIf3CmEm1x1StatsTotalDurationBelowUsDsThrshlds": docsIf3CmEm1x1StatsTotalDurationBelowUsDsThrshlds,
       "docsIf3MibConformance": docsIf3MibConformance,
       "docsIf3MibCompliances": docsIf3MibCompliances,
       "docsIf3CmtsCompliance": docsIf3CmtsCompliance,
       "docsIf3CmCompliance": docsIf3CmCompliance,
       "docsIf3MibGroups": docsIf3MibGroups,
       "docsIf3CmtsGroup": docsIf3CmtsGroup,
       "docsIf3CmGroup": docsIf3CmGroup,
       "docsIf3CmtsNotificationGroup": docsIf3CmtsNotificationGroup,
       "docsIf3CmNotificationGroup": docsIf3CmNotificationGroup,
       "docsIf3ObsoleteGroup": docsIf3ObsoleteGroup}
)
