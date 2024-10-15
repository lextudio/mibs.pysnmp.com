# SNMP MIB module (CISCO-LWAPP-MESH-LINKTEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-MESH-LINKTEST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:41 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoLwappMeshLinkTestMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 606)
)
ciscoLwappMeshLinkTestMIB.setRevisions(
        ("2010-09-30 00:00",
         "2007-02-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappMeshLinkTestMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappMeshLinkTestMIBNotifs = _CiscoLwappMeshLinkTestMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 0)
)
_CiscoLwappMeshLinkTestMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappMeshLinkTestMIBObjects = _CiscoLwappMeshLinkTestMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1)
)
_CiscoLwappMeshLinkTestConfig_ObjectIdentity = ObjectIdentity
ciscoLwappMeshLinkTestConfig = _CiscoLwappMeshLinkTestConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 1)
)


class _ClMeshLtPurgeTime_Type(Unsigned32):
    """Custom type clMeshLtPurgeTime based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 1800),
    )


_ClMeshLtPurgeTime_Type.__name__ = "Unsigned32"
_ClMeshLtPurgeTime_Object = MibScalar
clMeshLtPurgeTime = _ClMeshLtPurgeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 1, 1),
    _ClMeshLtPurgeTime_Type()
)
clMeshLtPurgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshLtPurgeTime.setStatus("current")
if mibBuilder.loadTexts:
    clMeshLtPurgeTime.setUnits("seconds")
_CiscoLwappMeshLinkTestRun_ObjectIdentity = ObjectIdentity
ciscoLwappMeshLinkTestRun = _CiscoLwappMeshLinkTestRun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 2)
)
_ClMeshLtTable_Object = MibTable
clMeshLtTable = _ClMeshLtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 2, 1)
)
if mibBuilder.loadTexts:
    clMeshLtTable.setStatus("current")
_ClMeshLtEntry_Object = MibTableRow
clMeshLtEntry = _ClMeshLtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 2, 1, 1)
)
clMeshLtEntry.setIndexNames(
    (0, "CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtIndex"),
)
if mibBuilder.loadTexts:
    clMeshLtEntry.setStatus("current")


class _ClMeshLtIndex_Type(Unsigned32):
    """Custom type clMeshLtIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ClMeshLtIndex_Type.__name__ = "Unsigned32"
_ClMeshLtIndex_Object = MibTableColumn
clMeshLtIndex = _ClMeshLtIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 2, 1, 1, 1),
    _ClMeshLtIndex_Type()
)
clMeshLtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clMeshLtIndex.setStatus("current")
_ClMeshLtSrcMacAddress_Type = MacAddress
_ClMeshLtSrcMacAddress_Object = MibTableColumn
clMeshLtSrcMacAddress = _ClMeshLtSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 2, 1, 1, 2),
    _ClMeshLtSrcMacAddress_Type()
)
clMeshLtSrcMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clMeshLtSrcMacAddress.setStatus("current")
_ClMeshLtDestMacAddress_Type = MacAddress
_ClMeshLtDestMacAddress_Object = MibTableColumn
clMeshLtDestMacAddress = _ClMeshLtDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 2, 1, 1, 3),
    _ClMeshLtDestMacAddress_Type()
)
clMeshLtDestMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clMeshLtDestMacAddress.setStatus("current")
_ClMeshLtDataRate_Type = Unsigned32
_ClMeshLtDataRate_Object = MibTableColumn
clMeshLtDataRate = _ClMeshLtDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 2, 1, 1, 4),
    _ClMeshLtDataRate_Type()
)
clMeshLtDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clMeshLtDataRate.setStatus("deprecated")
if mibBuilder.loadTexts:
    clMeshLtDataRate.setUnits("Mbps")


class _ClMeshLtPktsPerSec_Type(Unsigned32):
    """Custom type clMeshLtPktsPerSec based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3000),
    )


_ClMeshLtPktsPerSec_Type.__name__ = "Unsigned32"
_ClMeshLtPktsPerSec_Object = MibTableColumn
clMeshLtPktsPerSec = _ClMeshLtPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 2, 1, 1, 5),
    _ClMeshLtPktsPerSec_Type()
)
clMeshLtPktsPerSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clMeshLtPktsPerSec.setStatus("current")
if mibBuilder.loadTexts:
    clMeshLtPktsPerSec.setUnits("packets")


class _ClMeshLtPktSize_Type(Unsigned32):
    """Custom type clMeshLtPktSize based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1500),
    )


_ClMeshLtPktSize_Type.__name__ = "Unsigned32"
_ClMeshLtPktSize_Object = MibTableColumn
clMeshLtPktSize = _ClMeshLtPktSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 2, 1, 1, 6),
    _ClMeshLtPktSize_Type()
)
clMeshLtPktSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clMeshLtPktSize.setStatus("current")
if mibBuilder.loadTexts:
    clMeshLtPktSize.setUnits("bytes")


class _ClMeshLtDuration_Type(Unsigned32):
    """Custom type clMeshLtDuration based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 60),
    )


_ClMeshLtDuration_Type.__name__ = "Unsigned32"
_ClMeshLtDuration_Object = MibTableColumn
clMeshLtDuration = _ClMeshLtDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 2, 1, 1, 7),
    _ClMeshLtDuration_Type()
)
clMeshLtDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clMeshLtDuration.setStatus("current")
if mibBuilder.loadTexts:
    clMeshLtDuration.setUnits("seconds")
_ClMeshLtRowStatus_Type = RowStatus
_ClMeshLtRowStatus_Object = MibTableColumn
clMeshLtRowStatus = _ClMeshLtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 2, 1, 1, 8),
    _ClMeshLtRowStatus_Type()
)
clMeshLtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clMeshLtRowStatus.setStatus("current")


class _ClMeshLtDataRateValue_Type(Integer32):
    """Custom type clMeshLtDataRateValue based on Integer32"""
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
              29)
        )
    )
    namedValues = NamedValues(
        *(("htMcs0", 14),
          ("htMcs1", 15),
          ("htMcs10", 24),
          ("htMcs11", 25),
          ("htMcs12", 26),
          ("htMcs13", 27),
          ("htMcs14", 28),
          ("htMcs15", 29),
          ("htMcs2", 16),
          ("htMcs3", 17),
          ("htMcs4", 18),
          ("htMcs5", 19),
          ("htMcs6", 20),
          ("htMcs7", 21),
          ("htMcs8", 22),
          ("htMcs9", 23),
          ("mbps1", 1),
          ("mbps108", 13),
          ("mbps11", 6),
          ("mbps12", 7),
          ("mbps18", 8),
          ("mbps2", 2),
          ("mbps24", 9),
          ("mbps36", 10),
          ("mbps48", 11),
          ("mbps54", 12),
          ("mbps5point5", 3),
          ("mbps6", 4),
          ("mbps9", 5))
    )


_ClMeshLtDataRateValue_Type.__name__ = "Integer32"
_ClMeshLtDataRateValue_Object = MibTableColumn
clMeshLtDataRateValue = _ClMeshLtDataRateValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 2, 1, 1, 9),
    _ClMeshLtDataRateValue_Type()
)
clMeshLtDataRateValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clMeshLtDataRateValue.setStatus("current")
_CiscoLwappMeshLinkTestStatus_ObjectIdentity = ObjectIdentity
ciscoLwappMeshLinkTestStatus = _CiscoLwappMeshLinkTestStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 3)
)
_ClMeshLtResultsTable_Object = MibTable
clMeshLtResultsTable = _ClMeshLtResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 3, 1)
)
if mibBuilder.loadTexts:
    clMeshLtResultsTable.setStatus("current")
_ClMeshLtResultsEntry_Object = MibTableRow
clMeshLtResultsEntry = _ClMeshLtResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 3, 1, 1)
)
clMeshLtResultsEntry.setIndexNames(
    (0, "CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtIndex"),
)
if mibBuilder.loadTexts:
    clMeshLtResultsEntry.setStatus("current")
_ClMeshLtTxPkts_Type = Counter32
_ClMeshLtTxPkts_Object = MibTableColumn
clMeshLtTxPkts = _ClMeshLtTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 3, 1, 1, 1),
    _ClMeshLtTxPkts_Type()
)
clMeshLtTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshLtTxPkts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshLtTxPkts.setUnits("packets")
_ClMeshLtRxPkts_Type = Counter32
_ClMeshLtRxPkts_Object = MibTableColumn
clMeshLtRxPkts = _ClMeshLtRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 3, 1, 1, 2),
    _ClMeshLtRxPkts_Type()
)
clMeshLtRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshLtRxPkts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshLtRxPkts.setUnits("packets")
_ClMeshLtRxGoodPkts_Type = Counter32
_ClMeshLtRxGoodPkts_Object = MibTableColumn
clMeshLtRxGoodPkts = _ClMeshLtRxGoodPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 3, 1, 1, 3),
    _ClMeshLtRxGoodPkts_Type()
)
clMeshLtRxGoodPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshLtRxGoodPkts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshLtRxGoodPkts.setUnits("packets")
_ClMeshLtRxDupPkts_Type = Counter32
_ClMeshLtRxDupPkts_Object = MibTableColumn
clMeshLtRxDupPkts = _ClMeshLtRxDupPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 3, 1, 1, 4),
    _ClMeshLtRxDupPkts_Type()
)
clMeshLtRxDupPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshLtRxDupPkts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshLtRxDupPkts.setUnits("packets")
_ClMeshLtRxShortPkts_Type = Counter32
_ClMeshLtRxShortPkts_Object = MibTableColumn
clMeshLtRxShortPkts = _ClMeshLtRxShortPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 3, 1, 1, 5),
    _ClMeshLtRxShortPkts_Type()
)
clMeshLtRxShortPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshLtRxShortPkts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshLtRxShortPkts.setUnits("packets")
_ClMeshLtRxBigPkts_Type = Counter32
_ClMeshLtRxBigPkts_Object = MibTableColumn
clMeshLtRxBigPkts = _ClMeshLtRxBigPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 3, 1, 1, 6),
    _ClMeshLtRxBigPkts_Type()
)
clMeshLtRxBigPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshLtRxBigPkts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshLtRxBigPkts.setUnits("packets")
_ClMeshLtRxPhyErrPkts_Type = Counter32
_ClMeshLtRxPhyErrPkts_Object = MibTableColumn
clMeshLtRxPhyErrPkts = _ClMeshLtRxPhyErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 3, 1, 1, 7),
    _ClMeshLtRxPhyErrPkts_Type()
)
clMeshLtRxPhyErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshLtRxPhyErrPkts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshLtRxPhyErrPkts.setUnits("packets")
_ClMeshLtRxCRCErrPkts_Type = Counter32
_ClMeshLtRxCRCErrPkts_Object = MibTableColumn
clMeshLtRxCRCErrPkts = _ClMeshLtRxCRCErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 3, 1, 1, 8),
    _ClMeshLtRxCRCErrPkts_Type()
)
clMeshLtRxCRCErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshLtRxCRCErrPkts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshLtRxCRCErrPkts.setUnits("packets")
_ClMeshLtRxSeqErrPkts_Type = Counter32
_ClMeshLtRxSeqErrPkts_Object = MibTableColumn
clMeshLtRxSeqErrPkts = _ClMeshLtRxSeqErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 3, 1, 1, 9),
    _ClMeshLtRxSeqErrPkts_Type()
)
clMeshLtRxSeqErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshLtRxSeqErrPkts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshLtRxSeqErrPkts.setUnits("packets")
_ClMeshLtRxAvgSNR_Type = Integer32
_ClMeshLtRxAvgSNR_Object = MibTableColumn
clMeshLtRxAvgSNR = _ClMeshLtRxAvgSNR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 3, 1, 1, 10),
    _ClMeshLtRxAvgSNR_Type()
)
clMeshLtRxAvgSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshLtRxAvgSNR.setStatus("current")
if mibBuilder.loadTexts:
    clMeshLtRxAvgSNR.setUnits("dB")
_ClMeshLtRxHighestSNR_Type = Integer32
_ClMeshLtRxHighestSNR_Object = MibTableColumn
clMeshLtRxHighestSNR = _ClMeshLtRxHighestSNR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 3, 1, 1, 11),
    _ClMeshLtRxHighestSNR_Type()
)
clMeshLtRxHighestSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshLtRxHighestSNR.setStatus("current")
if mibBuilder.loadTexts:
    clMeshLtRxHighestSNR.setUnits("dB")
_ClMeshLtRxLowestSNR_Type = Integer32
_ClMeshLtRxLowestSNR_Object = MibTableColumn
clMeshLtRxLowestSNR = _ClMeshLtRxLowestSNR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 3, 1, 1, 12),
    _ClMeshLtRxLowestSNR_Type()
)
clMeshLtRxLowestSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshLtRxLowestSNR.setStatus("current")
if mibBuilder.loadTexts:
    clMeshLtRxLowestSNR.setUnits("dB")
_ClMeshLtRxAvgNoiseFloor_Type = Integer32
_ClMeshLtRxAvgNoiseFloor_Object = MibTableColumn
clMeshLtRxAvgNoiseFloor = _ClMeshLtRxAvgNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 3, 1, 1, 13),
    _ClMeshLtRxAvgNoiseFloor_Type()
)
clMeshLtRxAvgNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshLtRxAvgNoiseFloor.setStatus("current")
if mibBuilder.loadTexts:
    clMeshLtRxAvgNoiseFloor.setUnits("dB")
_ClMeshLtRxHighestNoiseFloor_Type = Integer32
_ClMeshLtRxHighestNoiseFloor_Object = MibTableColumn
clMeshLtRxHighestNoiseFloor = _ClMeshLtRxHighestNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 3, 1, 1, 14),
    _ClMeshLtRxHighestNoiseFloor_Type()
)
clMeshLtRxHighestNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshLtRxHighestNoiseFloor.setStatus("current")
if mibBuilder.loadTexts:
    clMeshLtRxHighestNoiseFloor.setUnits("dB")
_ClMeshLtRxLowestNoiseFloor_Type = Integer32
_ClMeshLtRxLowestNoiseFloor_Object = MibTableColumn
clMeshLtRxLowestNoiseFloor = _ClMeshLtRxLowestNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 3, 1, 1, 15),
    _ClMeshLtRxLowestNoiseFloor_Type()
)
clMeshLtRxLowestNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshLtRxLowestNoiseFloor.setStatus("current")
if mibBuilder.loadTexts:
    clMeshLtRxLowestNoiseFloor.setUnits("dB")
_ClMeshLtRxAvgRSSI_Type = Integer32
_ClMeshLtRxAvgRSSI_Object = MibTableColumn
clMeshLtRxAvgRSSI = _ClMeshLtRxAvgRSSI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 3, 1, 1, 16),
    _ClMeshLtRxAvgRSSI_Type()
)
clMeshLtRxAvgRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshLtRxAvgRSSI.setStatus("current")
if mibBuilder.loadTexts:
    clMeshLtRxAvgRSSI.setUnits("dBm")
_ClMeshLtRxHighestRSSI_Type = Integer32
_ClMeshLtRxHighestRSSI_Object = MibTableColumn
clMeshLtRxHighestRSSI = _ClMeshLtRxHighestRSSI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 3, 1, 1, 17),
    _ClMeshLtRxHighestRSSI_Type()
)
clMeshLtRxHighestRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshLtRxHighestRSSI.setStatus("current")
if mibBuilder.loadTexts:
    clMeshLtRxHighestRSSI.setUnits("dBm")
_ClMeshLtRxLowestRSSI_Type = Integer32
_ClMeshLtRxLowestRSSI_Object = MibTableColumn
clMeshLtRxLowestRSSI = _ClMeshLtRxLowestRSSI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 3, 1, 1, 18),
    _ClMeshLtRxLowestRSSI_Type()
)
clMeshLtRxLowestRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshLtRxLowestRSSI.setStatus("current")
if mibBuilder.loadTexts:
    clMeshLtRxLowestRSSI.setUnits("dBm")


class _ClMeshLtStatus_Type(Integer32):
    """Custom type clMeshLtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clMeshLtStatusFailed", 1),
          ("clMeshLtStatusInProgress", 2),
          ("clMeshLtStatusSuccess", 3))
    )


_ClMeshLtStatus_Type.__name__ = "Integer32"
_ClMeshLtStatus_Object = MibTableColumn
clMeshLtStatus = _ClMeshLtStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 1, 3, 1, 1, 19),
    _ClMeshLtStatus_Type()
)
clMeshLtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshLtStatus.setStatus("current")
_CiscoLwappMeshLinkTestMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappMeshLinkTestMIBConform = _CiscoLwappMeshLinkTestMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 2)
)
_CiscoLwappMeshLinkTestMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappMeshLinkTestMIBCompliances = _CiscoLwappMeshLinkTestMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 2, 1)
)
_CiscoLwappMeshLinkTestMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappMeshLinkTestMIBGroups = _CiscoLwappMeshLinkTestMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 2, 2)
)

# Managed Objects groups

ciscoLwappMeshLinkTestConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 2, 2, 1)
)
ciscoLwappMeshLinkTestConfigGroup.setObjects(
    ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtPurgeTime")
)
if mibBuilder.loadTexts:
    ciscoLwappMeshLinkTestConfigGroup.setStatus("current")

ciscoLwappMeshLinkTestRunGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 2, 2, 2)
)
ciscoLwappMeshLinkTestRunGroup.setObjects(
      *(("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtSrcMacAddress"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtDestMacAddress"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtDataRate"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtPktsPerSec"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtPktSize"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtDuration"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRowStatus"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtTxPkts"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxPkts"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxGoodPkts"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxDupPkts"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxShortPkts"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxBigPkts"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxPhyErrPkts"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxCRCErrPkts"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxSeqErrPkts"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxAvgSNR"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxHighestSNR"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxLowestSNR"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxAvgNoiseFloor"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxHighestNoiseFloor"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxLowestNoiseFloor"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxAvgRSSI"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxHighestRSSI"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxLowestRSSI"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshLinkTestRunGroup.setStatus("deprecated")

ciscoLwappMeshLinkTestRunGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 2, 2, 3)
)
ciscoLwappMeshLinkTestRunGroupRev1.setObjects(
      *(("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtSrcMacAddress"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtDestMacAddress"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtDataRateValue"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtPktsPerSec"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtPktSize"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtDuration"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRowStatus"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtTxPkts"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxPkts"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxGoodPkts"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxDupPkts"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxShortPkts"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxBigPkts"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxPhyErrPkts"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxCRCErrPkts"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxSeqErrPkts"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxAvgSNR"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxHighestSNR"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxLowestSNR"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxAvgNoiseFloor"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxHighestNoiseFloor"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxLowestNoiseFloor"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxAvgRSSI"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxHighestRSSI"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtRxLowestRSSI"),
        ("CISCO-LWAPP-MESH-LINKTEST-MIB", "clMeshLtStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshLinkTestRunGroupRev1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappMeshLinkTestMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappMeshLinkTestMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappMeshLinkTestMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 606, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappMeshLinkTestMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-MESH-LINKTEST-MIB",
    **{"ciscoLwappMeshLinkTestMIB": ciscoLwappMeshLinkTestMIB,
       "ciscoLwappMeshLinkTestMIBNotifs": ciscoLwappMeshLinkTestMIBNotifs,
       "ciscoLwappMeshLinkTestMIBObjects": ciscoLwappMeshLinkTestMIBObjects,
       "ciscoLwappMeshLinkTestConfig": ciscoLwappMeshLinkTestConfig,
       "clMeshLtPurgeTime": clMeshLtPurgeTime,
       "ciscoLwappMeshLinkTestRun": ciscoLwappMeshLinkTestRun,
       "clMeshLtTable": clMeshLtTable,
       "clMeshLtEntry": clMeshLtEntry,
       "clMeshLtIndex": clMeshLtIndex,
       "clMeshLtSrcMacAddress": clMeshLtSrcMacAddress,
       "clMeshLtDestMacAddress": clMeshLtDestMacAddress,
       "clMeshLtDataRate": clMeshLtDataRate,
       "clMeshLtPktsPerSec": clMeshLtPktsPerSec,
       "clMeshLtPktSize": clMeshLtPktSize,
       "clMeshLtDuration": clMeshLtDuration,
       "clMeshLtRowStatus": clMeshLtRowStatus,
       "clMeshLtDataRateValue": clMeshLtDataRateValue,
       "ciscoLwappMeshLinkTestStatus": ciscoLwappMeshLinkTestStatus,
       "clMeshLtResultsTable": clMeshLtResultsTable,
       "clMeshLtResultsEntry": clMeshLtResultsEntry,
       "clMeshLtTxPkts": clMeshLtTxPkts,
       "clMeshLtRxPkts": clMeshLtRxPkts,
       "clMeshLtRxGoodPkts": clMeshLtRxGoodPkts,
       "clMeshLtRxDupPkts": clMeshLtRxDupPkts,
       "clMeshLtRxShortPkts": clMeshLtRxShortPkts,
       "clMeshLtRxBigPkts": clMeshLtRxBigPkts,
       "clMeshLtRxPhyErrPkts": clMeshLtRxPhyErrPkts,
       "clMeshLtRxCRCErrPkts": clMeshLtRxCRCErrPkts,
       "clMeshLtRxSeqErrPkts": clMeshLtRxSeqErrPkts,
       "clMeshLtRxAvgSNR": clMeshLtRxAvgSNR,
       "clMeshLtRxHighestSNR": clMeshLtRxHighestSNR,
       "clMeshLtRxLowestSNR": clMeshLtRxLowestSNR,
       "clMeshLtRxAvgNoiseFloor": clMeshLtRxAvgNoiseFloor,
       "clMeshLtRxHighestNoiseFloor": clMeshLtRxHighestNoiseFloor,
       "clMeshLtRxLowestNoiseFloor": clMeshLtRxLowestNoiseFloor,
       "clMeshLtRxAvgRSSI": clMeshLtRxAvgRSSI,
       "clMeshLtRxHighestRSSI": clMeshLtRxHighestRSSI,
       "clMeshLtRxLowestRSSI": clMeshLtRxLowestRSSI,
       "clMeshLtStatus": clMeshLtStatus,
       "ciscoLwappMeshLinkTestMIBConform": ciscoLwappMeshLinkTestMIBConform,
       "ciscoLwappMeshLinkTestMIBCompliances": ciscoLwappMeshLinkTestMIBCompliances,
       "ciscoLwappMeshLinkTestMIBCompliance": ciscoLwappMeshLinkTestMIBCompliance,
       "ciscoLwappMeshLinkTestMIBComplianceRev1": ciscoLwappMeshLinkTestMIBComplianceRev1,
       "ciscoLwappMeshLinkTestMIBGroups": ciscoLwappMeshLinkTestMIBGroups,
       "ciscoLwappMeshLinkTestConfigGroup": ciscoLwappMeshLinkTestConfigGroup,
       "ciscoLwappMeshLinkTestRunGroup": ciscoLwappMeshLinkTestRunGroup,
       "ciscoLwappMeshLinkTestRunGroupRev1": ciscoLwappMeshLinkTestRunGroupRev1}
)
