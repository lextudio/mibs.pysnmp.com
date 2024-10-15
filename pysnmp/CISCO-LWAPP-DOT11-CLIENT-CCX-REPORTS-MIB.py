# SNMP MIB module (CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:24 2024
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

(cldcClientMacAddress,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-DOT11-CLIENT-MIB",
    "cldcClientMacAddress")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappDot11ClientRmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 767)
)
ciscoLwappDot11ClientRmMIB.setRevisions(
        ("2010-12-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoLwappCcxRmReqStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 3),
          ("inProgress", 1),
          ("success", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoLwapDot11ClientRmMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwapDot11ClientRmMIBNotifs = _CiscoLwapDot11ClientRmMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 0)
)
_CiscoLwappDot11ClientRmMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappDot11ClientRmMIBObjects = _CiscoLwappDot11ClientRmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1)
)
_CldccrRmReq_ObjectIdentity = ObjectIdentity
cldccrRmReq = _CldccrRmReq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 1)
)
_CldccrRmReqTable_Object = MibTable
cldccrRmReqTable = _CldccrRmReqTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cldccrRmReqTable.setStatus("current")
_CldccrRmReqEntry_Object = MibTableRow
cldccrRmReqEntry = _CldccrRmReqEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 1, 1, 1)
)
cldccrRmReqEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldccrRmReqEntry.setStatus("current")


class _CldccrRmReqReportType_Type(Bits):
    """Custom type cldccrRmReqReportType based on Bits"""
    namedValues = NamedValues(
        *(("beaconReport", 2),
          ("channelLoadReport", 0),
          ("frameReport", 3),
          ("histogramReport", 1))
    )

_CldccrRmReqReportType_Type.__name__ = "Bits"
_CldccrRmReqReportType_Object = MibTableColumn
cldccrRmReqReportType = _CldccrRmReqReportType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 1, 1, 1, 1),
    _CldccrRmReqReportType_Type()
)
cldccrRmReqReportType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldccrRmReqReportType.setStatus("current")
_CldccrRmInitiateReq_Type = TruthValue
_CldccrRmInitiateReq_Object = MibTableColumn
cldccrRmInitiateReq = _CldccrRmInitiateReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 1, 1, 1, 2),
    _CldccrRmInitiateReq_Type()
)
cldccrRmInitiateReq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldccrRmInitiateReq.setStatus("current")


class _CldccrRmReqNumIterations_Type(Integer32):
    """Custom type cldccrRmReqNumIterations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_CldccrRmReqNumIterations_Type.__name__ = "Integer32"
_CldccrRmReqNumIterations_Object = MibTableColumn
cldccrRmReqNumIterations = _CldccrRmReqNumIterations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 1, 1, 1, 3),
    _CldccrRmReqNumIterations_Type()
)
cldccrRmReqNumIterations.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldccrRmReqNumIterations.setStatus("current")


class _CldccrRmReqMeasDuration_Type(Unsigned32):
    """Custom type cldccrRmReqMeasDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 32400),
    )


_CldccrRmReqMeasDuration_Type.__name__ = "Unsigned32"
_CldccrRmReqMeasDuration_Object = MibTableColumn
cldccrRmReqMeasDuration = _CldccrRmReqMeasDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 1, 1, 1, 4),
    _CldccrRmReqMeasDuration_Type()
)
cldccrRmReqMeasDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldccrRmReqMeasDuration.setStatus("current")
_CldccrRmReqRowStatus_Type = RowStatus
_CldccrRmReqRowStatus_Object = MibTableColumn
cldccrRmReqRowStatus = _CldccrRmReqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 1, 1, 1, 5),
    _CldccrRmReqRowStatus_Type()
)
cldccrRmReqRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldccrRmReqRowStatus.setStatus("current")
_CldccrRmResp_ObjectIdentity = ObjectIdentity
cldccrRmResp = _CldccrRmResp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2)
)
_CldccrRmHistRepTable_Object = MibTable
cldccrRmHistRepTable = _CldccrRmHistRepTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cldccrRmHistRepTable.setStatus("current")
_CldccrRmHistRepEntry_Object = MibTableRow
cldccrRmHistRepEntry = _CldccrRmHistRepEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 1, 1)
)
cldccrRmHistRepEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmHistIndex"),
)
if mibBuilder.loadTexts:
    cldccrRmHistRepEntry.setStatus("current")


class _CldccrRmHistIndex_Type(Unsigned32):
    """Custom type cldccrRmHistIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28),
    )


_CldccrRmHistIndex_Type.__name__ = "Unsigned32"
_CldccrRmHistIndex_Object = MibTableColumn
cldccrRmHistIndex = _CldccrRmHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 1, 1, 1),
    _CldccrRmHistIndex_Type()
)
cldccrRmHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldccrRmHistIndex.setStatus("current")
_CldccrRmHistRepChannelNumber_Type = Unsigned32
_CldccrRmHistRepChannelNumber_Object = MibTableColumn
cldccrRmHistRepChannelNumber = _CldccrRmHistRepChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 1, 1, 2),
    _CldccrRmHistRepChannelNumber_Type()
)
cldccrRmHistRepChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccrRmHistRepChannelNumber.setStatus("current")
_CldccrRmHistRepTimeStamp_Type = OctetString
_CldccrRmHistRepTimeStamp_Object = MibTableColumn
cldccrRmHistRepTimeStamp = _CldccrRmHistRepTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 1, 1, 3),
    _CldccrRmHistRepTimeStamp_Type()
)
cldccrRmHistRepTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccrRmHistRepTimeStamp.setStatus("current")
_CldccrRmHistRepRPIDensity0_Type = Unsigned32
_CldccrRmHistRepRPIDensity0_Object = MibTableColumn
cldccrRmHistRepRPIDensity0 = _CldccrRmHistRepRPIDensity0_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 1, 1, 4),
    _CldccrRmHistRepRPIDensity0_Type()
)
cldccrRmHistRepRPIDensity0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccrRmHistRepRPIDensity0.setStatus("current")
_CldccrRmHistRepRPIDensity1_Type = Unsigned32
_CldccrRmHistRepRPIDensity1_Object = MibTableColumn
cldccrRmHistRepRPIDensity1 = _CldccrRmHistRepRPIDensity1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 1, 1, 5),
    _CldccrRmHistRepRPIDensity1_Type()
)
cldccrRmHistRepRPIDensity1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccrRmHistRepRPIDensity1.setStatus("current")
_CldccrRmHistRepRPIDensity2_Type = Unsigned32
_CldccrRmHistRepRPIDensity2_Object = MibTableColumn
cldccrRmHistRepRPIDensity2 = _CldccrRmHistRepRPIDensity2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 1, 1, 6),
    _CldccrRmHistRepRPIDensity2_Type()
)
cldccrRmHistRepRPIDensity2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccrRmHistRepRPIDensity2.setStatus("current")
_CldccrRmHistRepRPIDensity3_Type = Unsigned32
_CldccrRmHistRepRPIDensity3_Object = MibTableColumn
cldccrRmHistRepRPIDensity3 = _CldccrRmHistRepRPIDensity3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 1, 1, 7),
    _CldccrRmHistRepRPIDensity3_Type()
)
cldccrRmHistRepRPIDensity3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccrRmHistRepRPIDensity3.setStatus("current")
_CldccrRmHistRepRPIDensity4_Type = Unsigned32
_CldccrRmHistRepRPIDensity4_Object = MibTableColumn
cldccrRmHistRepRPIDensity4 = _CldccrRmHistRepRPIDensity4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 1, 1, 8),
    _CldccrRmHistRepRPIDensity4_Type()
)
cldccrRmHistRepRPIDensity4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccrRmHistRepRPIDensity4.setStatus("current")
_CldccrRmHistRepRPIDensity5_Type = Unsigned32
_CldccrRmHistRepRPIDensity5_Object = MibTableColumn
cldccrRmHistRepRPIDensity5 = _CldccrRmHistRepRPIDensity5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 1, 1, 9),
    _CldccrRmHistRepRPIDensity5_Type()
)
cldccrRmHistRepRPIDensity5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccrRmHistRepRPIDensity5.setStatus("current")
_CldccrRmHistRepRPIDensity6_Type = Unsigned32
_CldccrRmHistRepRPIDensity6_Object = MibTableColumn
cldccrRmHistRepRPIDensity6 = _CldccrRmHistRepRPIDensity6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 1, 1, 10),
    _CldccrRmHistRepRPIDensity6_Type()
)
cldccrRmHistRepRPIDensity6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccrRmHistRepRPIDensity6.setStatus("current")
_CldccrRmHistRepRPIDensity7_Type = Unsigned32
_CldccrRmHistRepRPIDensity7_Object = MibTableColumn
cldccrRmHistRepRPIDensity7 = _CldccrRmHistRepRPIDensity7_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 1, 1, 11),
    _CldccrRmHistRepRPIDensity7_Type()
)
cldccrRmHistRepRPIDensity7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccrRmHistRepRPIDensity7.setStatus("current")
_CldccrRmBeaconRepTable_Object = MibTable
cldccrRmBeaconRepTable = _CldccrRmBeaconRepTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cldccrRmBeaconRepTable.setStatus("current")
_CldccrRmBeaconRepEntry_Object = MibTableRow
cldccrRmBeaconRepEntry = _CldccrRmBeaconRepEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 2, 1)
)
cldccrRmBeaconRepEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmBeaconIndex"),
)
if mibBuilder.loadTexts:
    cldccrRmBeaconRepEntry.setStatus("current")


class _CldccrRmBeaconIndex_Type(Unsigned32):
    """Custom type cldccrRmBeaconIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28),
    )


_CldccrRmBeaconIndex_Type.__name__ = "Unsigned32"
_CldccrRmBeaconIndex_Object = MibTableColumn
cldccrRmBeaconIndex = _CldccrRmBeaconIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 2, 1, 1),
    _CldccrRmBeaconIndex_Type()
)
cldccrRmBeaconIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldccrRmBeaconIndex.setStatus("current")
_CldccrRmBeaconRptChannelNumber_Type = Unsigned32
_CldccrRmBeaconRptChannelNumber_Object = MibTableColumn
cldccrRmBeaconRptChannelNumber = _CldccrRmBeaconRptChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 2, 1, 2),
    _CldccrRmBeaconRptChannelNumber_Type()
)
cldccrRmBeaconRptChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccrRmBeaconRptChannelNumber.setStatus("current")
_CldccrRmBeaconRptTimeStamp_Type = OctetString
_CldccrRmBeaconRptTimeStamp_Object = MibTableColumn
cldccrRmBeaconRptTimeStamp = _CldccrRmBeaconRptTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 2, 1, 3),
    _CldccrRmBeaconRptTimeStamp_Type()
)
cldccrRmBeaconRptTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccrRmBeaconRptTimeStamp.setStatus("current")


class _CldccrRmBeaconRptPhyType_Type(Integer32):
    """Custom type cldccrRmBeaconRptPhyType based on Integer32"""
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
        *(("dss", 2),
          ("erp", 6),
          ("fh", 1),
          ("highDataRateDss", 5),
          ("ofdm", 4),
          ("unused", 3))
    )


_CldccrRmBeaconRptPhyType_Type.__name__ = "Integer32"
_CldccrRmBeaconRptPhyType_Object = MibTableColumn
cldccrRmBeaconRptPhyType = _CldccrRmBeaconRptPhyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 2, 1, 4),
    _CldccrRmBeaconRptPhyType_Type()
)
cldccrRmBeaconRptPhyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccrRmBeaconRptPhyType.setStatus("current")


class _CldccrRmBeaconRptReceivedPower_Type(Unsigned32):
    """Custom type cldccrRmBeaconRptReceivedPower based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_CldccrRmBeaconRptReceivedPower_Type.__name__ = "Unsigned32"
_CldccrRmBeaconRptReceivedPower_Object = MibTableColumn
cldccrRmBeaconRptReceivedPower = _CldccrRmBeaconRptReceivedPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 2, 1, 5),
    _CldccrRmBeaconRptReceivedPower_Type()
)
cldccrRmBeaconRptReceivedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccrRmBeaconRptReceivedPower.setStatus("current")
_CldccrRmBeaconRptBSSID_Type = MacAddress
_CldccrRmBeaconRptBSSID_Object = MibTableColumn
cldccrRmBeaconRptBSSID = _CldccrRmBeaconRptBSSID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 2, 1, 6),
    _CldccrRmBeaconRptBSSID_Type()
)
cldccrRmBeaconRptBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccrRmBeaconRptBSSID.setStatus("current")


class _CldccrRmBeaconRptParentTsf_Type(OctetString):
    """Custom type cldccrRmBeaconRptParentTsf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_CldccrRmBeaconRptParentTsf_Type.__name__ = "OctetString"
_CldccrRmBeaconRptParentTsf_Object = MibTableColumn
cldccrRmBeaconRptParentTsf = _CldccrRmBeaconRptParentTsf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 2, 1, 7),
    _CldccrRmBeaconRptParentTsf_Type()
)
cldccrRmBeaconRptParentTsf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccrRmBeaconRptParentTsf.setStatus("current")


class _CldccrRmBeaconRptTargetTsf_Type(OctetString):
    """Custom type cldccrRmBeaconRptTargetTsf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_CldccrRmBeaconRptTargetTsf_Type.__name__ = "OctetString"
_CldccrRmBeaconRptTargetTsf_Object = MibTableColumn
cldccrRmBeaconRptTargetTsf = _CldccrRmBeaconRptTargetTsf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 2, 1, 8),
    _CldccrRmBeaconRptTargetTsf_Type()
)
cldccrRmBeaconRptTargetTsf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccrRmBeaconRptTargetTsf.setStatus("current")
_CldccrRmBeaconRptInterval_Type = Unsigned32
_CldccrRmBeaconRptInterval_Object = MibTableColumn
cldccrRmBeaconRptInterval = _CldccrRmBeaconRptInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 2, 1, 9),
    _CldccrRmBeaconRptInterval_Type()
)
cldccrRmBeaconRptInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccrRmBeaconRptInterval.setStatus("current")
_CldccrRmBeaconRptCapInfo_Type = Unsigned32
_CldccrRmBeaconRptCapInfo_Object = MibTableColumn
cldccrRmBeaconRptCapInfo = _CldccrRmBeaconRptCapInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 2, 1, 10),
    _CldccrRmBeaconRptCapInfo_Type()
)
cldccrRmBeaconRptCapInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccrRmBeaconRptCapInfo.setStatus("current")
_CldccRmChannelLoadReportTable_Object = MibTable
cldccRmChannelLoadReportTable = _CldccRmChannelLoadReportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cldccRmChannelLoadReportTable.setStatus("current")
_CldccRmChannelLoadReportEntry_Object = MibTableRow
cldccRmChannelLoadReportEntry = _CldccRmChannelLoadReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 3, 1)
)
cldccRmChannelLoadReportEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccRmChannelLoadReportIndex"),
)
if mibBuilder.loadTexts:
    cldccRmChannelLoadReportEntry.setStatus("current")
_CldccRmChannelLoadReportIndex_Type = Unsigned32
_CldccRmChannelLoadReportIndex_Object = MibTableColumn
cldccRmChannelLoadReportIndex = _CldccRmChannelLoadReportIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 3, 1, 1),
    _CldccRmChannelLoadReportIndex_Type()
)
cldccRmChannelLoadReportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldccRmChannelLoadReportIndex.setStatus("current")
_CldccRmChannelLoadReportChannelNumber_Type = Unsigned32
_CldccRmChannelLoadReportChannelNumber_Object = MibTableColumn
cldccRmChannelLoadReportChannelNumber = _CldccRmChannelLoadReportChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 3, 1, 2),
    _CldccRmChannelLoadReportChannelNumber_Type()
)
cldccRmChannelLoadReportChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccRmChannelLoadReportChannelNumber.setStatus("current")
_CldccRmChannelLoadReportTimeStamp_Type = OctetString
_CldccRmChannelLoadReportTimeStamp_Object = MibTableColumn
cldccRmChannelLoadReportTimeStamp = _CldccRmChannelLoadReportTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 3, 1, 3),
    _CldccRmChannelLoadReportTimeStamp_Type()
)
cldccRmChannelLoadReportTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccRmChannelLoadReportTimeStamp.setStatus("current")
_CldccRmChannelLoadReportCCABusyFraction_Type = Unsigned32
_CldccRmChannelLoadReportCCABusyFraction_Object = MibTableColumn
cldccRmChannelLoadReportCCABusyFraction = _CldccRmChannelLoadReportCCABusyFraction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 3, 1, 4),
    _CldccRmChannelLoadReportCCABusyFraction_Type()
)
cldccRmChannelLoadReportCCABusyFraction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccRmChannelLoadReportCCABusyFraction.setStatus("current")
_CldccRmFrameReportTable_Object = MibTable
cldccRmFrameReportTable = _CldccRmFrameReportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cldccRmFrameReportTable.setStatus("current")
_CldccRmFrameReportEntry_Object = MibTableRow
cldccRmFrameReportEntry = _CldccRmFrameReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 4, 1)
)
cldccRmFrameReportEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccRmFrameReportElemIndex"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccRmFrameReportSubElemIndex"),
)
if mibBuilder.loadTexts:
    cldccRmFrameReportEntry.setStatus("current")
_CldccRmFrameReportElemIndex_Type = Unsigned32
_CldccRmFrameReportElemIndex_Object = MibTableColumn
cldccRmFrameReportElemIndex = _CldccRmFrameReportElemIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 4, 1, 1),
    _CldccRmFrameReportElemIndex_Type()
)
cldccRmFrameReportElemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldccRmFrameReportElemIndex.setStatus("current")
_CldccRmFrameReportSubElemIndex_Type = Unsigned32
_CldccRmFrameReportSubElemIndex_Object = MibTableColumn
cldccRmFrameReportSubElemIndex = _CldccRmFrameReportSubElemIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 4, 1, 2),
    _CldccRmFrameReportSubElemIndex_Type()
)
cldccRmFrameReportSubElemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldccRmFrameReportSubElemIndex.setStatus("current")
_CldccRmFrameReportChanNumber_Type = Unsigned32
_CldccRmFrameReportChanNumber_Object = MibTableColumn
cldccRmFrameReportChanNumber = _CldccRmFrameReportChanNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 4, 1, 3),
    _CldccRmFrameReportChanNumber_Type()
)
cldccRmFrameReportChanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccRmFrameReportChanNumber.setStatus("current")
_CldccRmFrameReportTimeStamp_Type = OctetString
_CldccRmFrameReportTimeStamp_Object = MibTableColumn
cldccRmFrameReportTimeStamp = _CldccRmFrameReportTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 4, 1, 4),
    _CldccRmFrameReportTimeStamp_Type()
)
cldccRmFrameReportTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccRmFrameReportTimeStamp.setStatus("current")
_CldccRmFrameReportTransmitAddr_Type = MacAddress
_CldccRmFrameReportTransmitAddr_Object = MibTableColumn
cldccRmFrameReportTransmitAddr = _CldccRmFrameReportTransmitAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 4, 1, 5),
    _CldccRmFrameReportTransmitAddr_Type()
)
cldccRmFrameReportTransmitAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccRmFrameReportTransmitAddr.setStatus("current")
_CldccRmFrameReportBssid_Type = MacAddress
_CldccRmFrameReportBssid_Object = MibTableColumn
cldccRmFrameReportBssid = _CldccRmFrameReportBssid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 4, 1, 6),
    _CldccRmFrameReportBssid_Type()
)
cldccRmFrameReportBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccRmFrameReportBssid.setStatus("current")


class _CldccRmFrameReportRecvSigPower_Type(Unsigned32):
    """Custom type cldccRmFrameReportRecvSigPower based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_CldccRmFrameReportRecvSigPower_Type.__name__ = "Unsigned32"
_CldccRmFrameReportRecvSigPower_Object = MibTableColumn
cldccRmFrameReportRecvSigPower = _CldccRmFrameReportRecvSigPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 4, 1, 7),
    _CldccRmFrameReportRecvSigPower_Type()
)
cldccRmFrameReportRecvSigPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccRmFrameReportRecvSigPower.setStatus("current")


class _CldccRmFrameReportFrameCount_Type(Unsigned32):
    """Custom type cldccRmFrameReportFrameCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_CldccRmFrameReportFrameCount_Type.__name__ = "Unsigned32"
_CldccRmFrameReportFrameCount_Object = MibTableColumn
cldccRmFrameReportFrameCount = _CldccRmFrameReportFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 4, 1, 8),
    _CldccRmFrameReportFrameCount_Type()
)
cldccRmFrameReportFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccRmFrameReportFrameCount.setStatus("current")
_CldccrRmReqStatus_ObjectIdentity = ObjectIdentity
cldccrRmReqStatus = _CldccrRmReqStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 3)
)
_CldccrRmReqStatusTable_Object = MibTable
cldccrRmReqStatusTable = _CldccrRmReqStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cldccrRmReqStatusTable.setStatus("current")
_CldccrRmReqStatusEntry_Object = MibTableRow
cldccrRmReqStatusEntry = _CldccrRmReqStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 3, 1, 1)
)
cldccrRmReqStatusEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldccrRmReqStatusEntry.setStatus("current")
_CldccrRmFrameReqStatus_Type = CiscoLwappCcxRmReqStatus
_CldccrRmFrameReqStatus_Object = MibTableColumn
cldccrRmFrameReqStatus = _CldccrRmFrameReqStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 3, 1, 1, 1),
    _CldccrRmFrameReqStatus_Type()
)
cldccrRmFrameReqStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccrRmFrameReqStatus.setStatus("current")
_CldccrRmHistogramReqStatus_Type = CiscoLwappCcxRmReqStatus
_CldccrRmHistogramReqStatus_Object = MibTableColumn
cldccrRmHistogramReqStatus = _CldccrRmHistogramReqStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 3, 1, 1, 2),
    _CldccrRmHistogramReqStatus_Type()
)
cldccrRmHistogramReqStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccrRmHistogramReqStatus.setStatus("current")
_CldccrRmBeaconReqStatus_Type = CiscoLwappCcxRmReqStatus
_CldccrRmBeaconReqStatus_Object = MibTableColumn
cldccrRmBeaconReqStatus = _CldccrRmBeaconReqStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 3, 1, 1, 3),
    _CldccrRmBeaconReqStatus_Type()
)
cldccrRmBeaconReqStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccrRmBeaconReqStatus.setStatus("current")
_CldccrRmChanLoadReqStatus_Type = CiscoLwappCcxRmReqStatus
_CldccrRmChanLoadReqStatus_Object = MibTableColumn
cldccrRmChanLoadReqStatus = _CldccrRmChanLoadReqStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 3, 1, 1, 4),
    _CldccrRmChanLoadReqStatus_Type()
)
cldccrRmChanLoadReqStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccrRmChanLoadReqStatus.setStatus("current")
_CiscoLwappDot11ClientRmMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappDot11ClientRmMIBConform = _CiscoLwappDot11ClientRmMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 2)
)
_CiscoLwappDot11ClientRmMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappDot11ClientRmMIBCompliances = _CiscoLwappDot11ClientRmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 2, 1)
)
_CiscoLwappDot11ClientRmMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappDot11ClientRmMIBGroups = _CiscoLwappDot11ClientRmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 2, 2)
)

# Managed Objects groups

ciscoLwappDot11ClientRmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 2, 2, 1)
)
ciscoLwappDot11ClientRmConfigGroup.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmReqReportType"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmInitiateReq"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmReqNumIterations"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmReqMeasDuration"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmReqRowStatus"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmHistRepChannelNumber"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmHistRepTimeStamp"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmHistRepRPIDensity0"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmHistRepRPIDensity1"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmHistRepRPIDensity2"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmHistRepRPIDensity3"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmHistRepRPIDensity4"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmHistRepRPIDensity5"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmHistRepRPIDensity6"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmHistRepRPIDensity7"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmBeaconRptChannelNumber"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmBeaconRptTimeStamp"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmBeaconRptPhyType"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmBeaconRptReceivedPower"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmBeaconRptBSSID"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmBeaconRptParentTsf"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmBeaconRptTargetTsf"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmBeaconRptInterval"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmBeaconRptCapInfo"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccRmChannelLoadReportChannelNumber"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccRmChannelLoadReportTimeStamp"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccRmChannelLoadReportCCABusyFraction"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccRmFrameReportChanNumber"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccRmFrameReportTimeStamp"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccRmFrameReportTransmitAddr"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccRmFrameReportBssid"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccRmFrameReportRecvSigPower"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccRmFrameReportFrameCount"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmFrameReqStatus"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmHistogramReqStatus"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmBeaconReqStatus"),
        ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmChanLoadReqStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientRmConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappDot11ClientRmMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 767, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientRmMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB",
    **{"CiscoLwappCcxRmReqStatus": CiscoLwappCcxRmReqStatus,
       "ciscoLwappDot11ClientRmMIB": ciscoLwappDot11ClientRmMIB,
       "ciscoLwapDot11ClientRmMIBNotifs": ciscoLwapDot11ClientRmMIBNotifs,
       "ciscoLwappDot11ClientRmMIBObjects": ciscoLwappDot11ClientRmMIBObjects,
       "cldccrRmReq": cldccrRmReq,
       "cldccrRmReqTable": cldccrRmReqTable,
       "cldccrRmReqEntry": cldccrRmReqEntry,
       "cldccrRmReqReportType": cldccrRmReqReportType,
       "cldccrRmInitiateReq": cldccrRmInitiateReq,
       "cldccrRmReqNumIterations": cldccrRmReqNumIterations,
       "cldccrRmReqMeasDuration": cldccrRmReqMeasDuration,
       "cldccrRmReqRowStatus": cldccrRmReqRowStatus,
       "cldccrRmResp": cldccrRmResp,
       "cldccrRmHistRepTable": cldccrRmHistRepTable,
       "cldccrRmHistRepEntry": cldccrRmHistRepEntry,
       "cldccrRmHistIndex": cldccrRmHistIndex,
       "cldccrRmHistRepChannelNumber": cldccrRmHistRepChannelNumber,
       "cldccrRmHistRepTimeStamp": cldccrRmHistRepTimeStamp,
       "cldccrRmHistRepRPIDensity0": cldccrRmHistRepRPIDensity0,
       "cldccrRmHistRepRPIDensity1": cldccrRmHistRepRPIDensity1,
       "cldccrRmHistRepRPIDensity2": cldccrRmHistRepRPIDensity2,
       "cldccrRmHistRepRPIDensity3": cldccrRmHistRepRPIDensity3,
       "cldccrRmHistRepRPIDensity4": cldccrRmHistRepRPIDensity4,
       "cldccrRmHistRepRPIDensity5": cldccrRmHistRepRPIDensity5,
       "cldccrRmHistRepRPIDensity6": cldccrRmHistRepRPIDensity6,
       "cldccrRmHistRepRPIDensity7": cldccrRmHistRepRPIDensity7,
       "cldccrRmBeaconRepTable": cldccrRmBeaconRepTable,
       "cldccrRmBeaconRepEntry": cldccrRmBeaconRepEntry,
       "cldccrRmBeaconIndex": cldccrRmBeaconIndex,
       "cldccrRmBeaconRptChannelNumber": cldccrRmBeaconRptChannelNumber,
       "cldccrRmBeaconRptTimeStamp": cldccrRmBeaconRptTimeStamp,
       "cldccrRmBeaconRptPhyType": cldccrRmBeaconRptPhyType,
       "cldccrRmBeaconRptReceivedPower": cldccrRmBeaconRptReceivedPower,
       "cldccrRmBeaconRptBSSID": cldccrRmBeaconRptBSSID,
       "cldccrRmBeaconRptParentTsf": cldccrRmBeaconRptParentTsf,
       "cldccrRmBeaconRptTargetTsf": cldccrRmBeaconRptTargetTsf,
       "cldccrRmBeaconRptInterval": cldccrRmBeaconRptInterval,
       "cldccrRmBeaconRptCapInfo": cldccrRmBeaconRptCapInfo,
       "cldccRmChannelLoadReportTable": cldccRmChannelLoadReportTable,
       "cldccRmChannelLoadReportEntry": cldccRmChannelLoadReportEntry,
       "cldccRmChannelLoadReportIndex": cldccRmChannelLoadReportIndex,
       "cldccRmChannelLoadReportChannelNumber": cldccRmChannelLoadReportChannelNumber,
       "cldccRmChannelLoadReportTimeStamp": cldccRmChannelLoadReportTimeStamp,
       "cldccRmChannelLoadReportCCABusyFraction": cldccRmChannelLoadReportCCABusyFraction,
       "cldccRmFrameReportTable": cldccRmFrameReportTable,
       "cldccRmFrameReportEntry": cldccRmFrameReportEntry,
       "cldccRmFrameReportElemIndex": cldccRmFrameReportElemIndex,
       "cldccRmFrameReportSubElemIndex": cldccRmFrameReportSubElemIndex,
       "cldccRmFrameReportChanNumber": cldccRmFrameReportChanNumber,
       "cldccRmFrameReportTimeStamp": cldccRmFrameReportTimeStamp,
       "cldccRmFrameReportTransmitAddr": cldccRmFrameReportTransmitAddr,
       "cldccRmFrameReportBssid": cldccRmFrameReportBssid,
       "cldccRmFrameReportRecvSigPower": cldccRmFrameReportRecvSigPower,
       "cldccRmFrameReportFrameCount": cldccRmFrameReportFrameCount,
       "cldccrRmReqStatus": cldccrRmReqStatus,
       "cldccrRmReqStatusTable": cldccrRmReqStatusTable,
       "cldccrRmReqStatusEntry": cldccrRmReqStatusEntry,
       "cldccrRmFrameReqStatus": cldccrRmFrameReqStatus,
       "cldccrRmHistogramReqStatus": cldccrRmHistogramReqStatus,
       "cldccrRmBeaconReqStatus": cldccrRmBeaconReqStatus,
       "cldccrRmChanLoadReqStatus": cldccrRmChanLoadReqStatus,
       "ciscoLwappDot11ClientRmMIBConform": ciscoLwappDot11ClientRmMIBConform,
       "ciscoLwappDot11ClientRmMIBCompliances": ciscoLwappDot11ClientRmMIBCompliances,
       "ciscoLwappDot11ClientRmMibCompliance": ciscoLwappDot11ClientRmMibCompliance,
       "ciscoLwappDot11ClientRmMIBGroups": ciscoLwappDot11ClientRmMIBGroups,
       "ciscoLwappDot11ClientRmConfigGroup": ciscoLwappDot11ClientRmConfigGroup}
)
