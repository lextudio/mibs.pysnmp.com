# SNMP MIB module (CISCO-GGSN-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-GGSN-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:51 2024
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

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cggsnQosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 241)
)
cggsnQosMIB.setRevisions(
        ("2008-12-17 00:00",
         "2006-09-11 00:00",
         "2005-03-21 17:00",
         "2003-11-27 13:00",
         "2002-04-18 14:00",
         "2001-12-06 13:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UmtsQosTrafficClass(Integer32, TextualConvention):
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
        *(("background", 4),
          ("conversational", 1),
          ("interactive", 3),
          ("streaming", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CggsnQosMIBObjects_ObjectIdentity = ObjectIdentity
cggsnQosMIBObjects = _CggsnQosMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1)
)
_CggsnQosGeneralConfig_ObjectIdentity = ObjectIdentity
cggsnQosGeneralConfig = _CggsnQosGeneralConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 1)
)


class _CggsnQosMappingMethod_Type(Integer32):
    """Custom type cggsnQosMappingMethod based on Integer32"""
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
        *(("canonical", 2),
          ("delay", 3),
          ("none", 1),
          ("umts", 4))
    )


_CggsnQosMappingMethod_Type.__name__ = "Integer32"
_CggsnQosMappingMethod_Object = MibScalar
cggsnQosMappingMethod = _CggsnQosMappingMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 1, 1),
    _CggsnQosMappingMethod_Type()
)
cggsnQosMappingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cggsnQosMappingMethod.setStatus("current")
_CggsnQosClassIpTosMapTable_Object = MibTable
cggsnQosClassIpTosMapTable = _CggsnQosClassIpTosMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cggsnQosClassIpTosMapTable.setStatus("current")
_CggsnQosClassIpTosMapEntry_Object = MibTableRow
cggsnQosClassIpTosMapEntry = _CggsnQosClassIpTosMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 1, 2, 1)
)
cggsnQosClassIpTosMapEntry.setIndexNames(
    (0, "CISCO-GGSN-QOS-MIB", "cggsnQosClass"),
)
if mibBuilder.loadTexts:
    cggsnQosClassIpTosMapEntry.setStatus("current")


class _CggsnQosClass_Type(Integer32):
    """Custom type cggsnQosClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CggsnQosClass_Type.__name__ = "Integer32"
_CggsnQosClass_Object = MibTableColumn
cggsnQosClass = _CggsnQosClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 1, 2, 1, 1),
    _CggsnQosClass_Type()
)
cggsnQosClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cggsnQosClass.setStatus("current")


class _CggsnQosMappedIpTos_Type(Integer32):
    """Custom type cggsnQosMappedIpTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_CggsnQosMappedIpTos_Type.__name__ = "Integer32"
_CggsnQosMappedIpTos_Object = MibTableColumn
cggsnQosMappedIpTos = _CggsnQosMappedIpTos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 1, 2, 1, 2),
    _CggsnQosMappedIpTos_Type()
)
cggsnQosMappedIpTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cggsnQosMappedIpTos.setStatus("current")
_CggsnQosCurrentPdps_Type = Gauge32
_CggsnQosCurrentPdps_Object = MibTableColumn
cggsnQosCurrentPdps = _CggsnQosCurrentPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 1, 2, 1, 3),
    _CggsnQosCurrentPdps_Type()
)
cggsnQosCurrentPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cggsnQosCurrentPdps.setStatus("current")
_CggsnQosCanonicalQos_ObjectIdentity = ObjectIdentity
cggsnQosCanonicalQos = _CggsnQosCanonicalQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 2)
)


class _CggsnQosTotalBandwidthResrc_Type(Unsigned32):
    """Custom type cggsnQosTotalBandwidthResrc based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CggsnQosTotalBandwidthResrc_Type.__name__ = "Unsigned32"
_CggsnQosTotalBandwidthResrc_Object = MibScalar
cggsnQosTotalBandwidthResrc = _CggsnQosTotalBandwidthResrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 2, 1),
    _CggsnQosTotalBandwidthResrc_Type()
)
cggsnQosTotalBandwidthResrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cggsnQosTotalBandwidthResrc.setStatus("current")
if mibBuilder.loadTexts:
    cggsnQosTotalBandwidthResrc.setUnits("bits/sec")
_CggsnQosCurrentUsedBandwidth_Type = Gauge32
_CggsnQosCurrentUsedBandwidth_Object = MibScalar
cggsnQosCurrentUsedBandwidth = _CggsnQosCurrentUsedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 2, 2),
    _CggsnQosCurrentUsedBandwidth_Type()
)
cggsnQosCurrentUsedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cggsnQosCurrentUsedBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cggsnQosCurrentUsedBandwidth.setUnits("bits/sec")


class _CggsnQosPremiumMtDeviationFactor_Type(Unsigned32):
    """Custom type cggsnQosPremiumMtDeviationFactor based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CggsnQosPremiumMtDeviationFactor_Type.__name__ = "Unsigned32"
_CggsnQosPremiumMtDeviationFactor_Object = MibScalar
cggsnQosPremiumMtDeviationFactor = _CggsnQosPremiumMtDeviationFactor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 2, 3),
    _CggsnQosPremiumMtDeviationFactor_Type()
)
cggsnQosPremiumMtDeviationFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cggsnQosPremiumMtDeviationFactor.setStatus("current")


class _CggsnQosBestEffrtBandWidthFactor_Type(Unsigned32):
    """Custom type cggsnQosBestEffrtBandWidthFactor based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000000),
    )


_CggsnQosBestEffrtBandWidthFactor_Type.__name__ = "Unsigned32"
_CggsnQosBestEffrtBandWidthFactor_Object = MibScalar
cggsnQosBestEffrtBandWidthFactor = _CggsnQosBestEffrtBandWidthFactor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 2, 4),
    _CggsnQosBestEffrtBandWidthFactor_Type()
)
cggsnQosBestEffrtBandWidthFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cggsnQosBestEffrtBandWidthFactor.setStatus("current")
if mibBuilder.loadTexts:
    cggsnQosBestEffrtBandWidthFactor.setUnits("bits/sec")
_CggsnQosPremiumMeanThroughput_Type = Gauge32
_CggsnQosPremiumMeanThroughput_Object = MibScalar
cggsnQosPremiumMeanThroughput = _CggsnQosPremiumMeanThroughput_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 2, 5),
    _CggsnQosPremiumMeanThroughput_Type()
)
cggsnQosPremiumMeanThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cggsnQosPremiumMeanThroughput.setStatus("current")
if mibBuilder.loadTexts:
    cggsnQosPremiumMeanThroughput.setUnits("bytes/sec")
_CggsnQosNormalMeanThroughput_Type = Gauge32
_CggsnQosNormalMeanThroughput_Object = MibScalar
cggsnQosNormalMeanThroughput = _CggsnQosNormalMeanThroughput_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 2, 6),
    _CggsnQosNormalMeanThroughput_Type()
)
cggsnQosNormalMeanThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cggsnQosNormalMeanThroughput.setStatus("current")
if mibBuilder.loadTexts:
    cggsnQosNormalMeanThroughput.setUnits("bytes/sec")
_CggsnQosBestEffortMeanThroughput_Type = Gauge32
_CggsnQosBestEffortMeanThroughput_Object = MibScalar
cggsnQosBestEffortMeanThroughput = _CggsnQosBestEffortMeanThroughput_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 2, 7),
    _CggsnQosBestEffortMeanThroughput_Type()
)
cggsnQosBestEffortMeanThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cggsnQosBestEffortMeanThroughput.setStatus("current")
if mibBuilder.loadTexts:
    cggsnQosBestEffortMeanThroughput.setUnits("bytes/sec")
_CggsnQosUmtsQos_ObjectIdentity = ObjectIdentity
cggsnQosUmtsQos = _CggsnQosUmtsQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3)
)
_CggsnQosTrafficClassPhbTable_Object = MibTable
cggsnQosTrafficClassPhbTable = _CggsnQosTrafficClassPhbTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cggsnQosTrafficClassPhbTable.setStatus("current")
_CggsnQosTrafficClassPhbEntry_Object = MibTableRow
cggsnQosTrafficClassPhbEntry = _CggsnQosTrafficClassPhbEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 1, 1)
)
cggsnQosTrafficClassPhbEntry.setIndexNames(
    (0, "CISCO-GGSN-QOS-MIB", "cggsnQosUmtsTrafficClass"),
)
if mibBuilder.loadTexts:
    cggsnQosTrafficClassPhbEntry.setStatus("current")


class _CggsnQosUmtsTrafficClass_Type(Integer32):
    """Custom type cggsnQosUmtsTrafficClass based on Integer32"""
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
        *(("background", 5),
          ("conversational", 2),
          ("interactive", 4),
          ("signalling", 1),
          ("streaming", 3))
    )


_CggsnQosUmtsTrafficClass_Type.__name__ = "Integer32"
_CggsnQosUmtsTrafficClass_Object = MibTableColumn
cggsnQosUmtsTrafficClass = _CggsnQosUmtsTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 1, 1, 1),
    _CggsnQosUmtsTrafficClass_Type()
)
cggsnQosUmtsTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cggsnQosUmtsTrafficClass.setStatus("current")


class _CggsnQosUmtsDiffServPhbgroup_Type(Integer32):
    """Custom type cggsnQosUmtsDiffServPhbgroup based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("afClass1", 3),
          ("afClass2", 4),
          ("afClass3", 5),
          ("afClass4", 6),
          ("bestEffort", 7),
          ("efClass", 2),
          ("signallingClass", 1))
    )


_CggsnQosUmtsDiffServPhbgroup_Type.__name__ = "Integer32"
_CggsnQosUmtsDiffServPhbgroup_Object = MibTableColumn
cggsnQosUmtsDiffServPhbgroup = _CggsnQosUmtsDiffServPhbgroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 1, 1, 2),
    _CggsnQosUmtsDiffServPhbgroup_Type()
)
cggsnQosUmtsDiffServPhbgroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cggsnQosUmtsDiffServPhbgroup.setStatus("current")
_CggsnQosUmtsPdps_Type = Gauge32
_CggsnQosUmtsPdps_Object = MibTableColumn
cggsnQosUmtsPdps = _CggsnQosUmtsPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 1, 1, 3),
    _CggsnQosUmtsPdps_Type()
)
cggsnQosUmtsPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cggsnQosUmtsPdps.setStatus("current")
_CggsnQosPhbToDscpMapTable_Object = MibTable
cggsnQosPhbToDscpMapTable = _CggsnQosPhbToDscpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cggsnQosPhbToDscpMapTable.setStatus("current")
_CggsnQosPhbToDscpMapEntry_Object = MibTableRow
cggsnQosPhbToDscpMapEntry = _CggsnQosPhbToDscpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 2, 1)
)
cggsnQosPhbToDscpMapEntry.setIndexNames(
    (0, "CISCO-GGSN-QOS-MIB", "cggsnQosDiffServPhb"),
)
if mibBuilder.loadTexts:
    cggsnQosPhbToDscpMapEntry.setStatus("current")


class _CggsnQosDiffServPhb_Type(Integer32):
    """Custom type cggsnQosDiffServPhb based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("afClass1High", 5),
          ("afClass1Low", 3),
          ("afClass1Medium", 4),
          ("afClass2High", 8),
          ("afClass2Low", 6),
          ("afClass2Medium", 7),
          ("afClass3High", 11),
          ("afClass3Low", 9),
          ("afClass3Medium", 10),
          ("afClass4High", 14),
          ("afClass4Low", 12),
          ("afClass4Medium", 13),
          ("bestEffort", 15),
          ("efClass", 2),
          ("signallingClass", 1))
    )


_CggsnQosDiffServPhb_Type.__name__ = "Integer32"
_CggsnQosDiffServPhb_Object = MibTableColumn
cggsnQosDiffServPhb = _CggsnQosDiffServPhb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 2, 1, 1),
    _CggsnQosDiffServPhb_Type()
)
cggsnQosDiffServPhb.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cggsnQosDiffServPhb.setStatus("current")


class _CggsnQosDscp_Type(Integer32):
    """Custom type cggsnQosDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CggsnQosDscp_Type.__name__ = "Integer32"
_CggsnQosDscp_Object = MibTableColumn
cggsnQosDscp = _CggsnQosDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 2, 1, 2),
    _CggsnQosDscp_Type()
)
cggsnQosDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cggsnQosDscp.setStatus("current")


class _CggsnQosUmtsDscpUnmodified_Type(Integer32):
    """Custom type cggsnQosUmtsDscpUnmodified based on Integer32"""
    defaultValue = 4

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
        *(("all", 3),
          ("down", 2),
          ("none", 4),
          ("up", 1))
    )


_CggsnQosUmtsDscpUnmodified_Type.__name__ = "Integer32"
_CggsnQosUmtsDscpUnmodified_Object = MibScalar
cggsnQosUmtsDscpUnmodified = _CggsnQosUmtsDscpUnmodified_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 3),
    _CggsnQosUmtsDscpUnmodified_Type()
)
cggsnQosUmtsDscpUnmodified.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cggsnQosUmtsDscpUnmodified.setStatus("current")
_CggsnQosUmtsCac_ObjectIdentity = ObjectIdentity
cggsnQosUmtsCac = _CggsnQosUmtsCac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4)
)


class _CggsnUmtsQosMapImsSigTrafClass_Type(UmtsQosTrafficClass):
    """Custom type cggsnUmtsQosMapImsSigTrafClass based on UmtsQosTrafficClass"""


_CggsnUmtsQosMapImsSigTrafClass_Object = MibScalar
cggsnUmtsQosMapImsSigTrafClass = _CggsnUmtsQosMapImsSigTrafClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 1),
    _CggsnUmtsQosMapImsSigTrafClass_Type()
)
cggsnUmtsQosMapImsSigTrafClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cggsnUmtsQosMapImsSigTrafClass.setStatus("deprecated")


class _CggsnUmtsQosMapImsSigTrafHandPri_Type(Integer32):
    """Custom type cggsnUmtsQosMapImsSigTrafHandPri based on Integer32"""
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
        *(("priority1", 1),
          ("priority2", 2),
          ("priority3", 3))
    )


_CggsnUmtsQosMapImsSigTrafHandPri_Type.__name__ = "Integer32"
_CggsnUmtsQosMapImsSigTrafHandPri_Object = MibScalar
cggsnUmtsQosMapImsSigTrafHandPri = _CggsnUmtsQosMapImsSigTrafHandPri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 2),
    _CggsnUmtsQosMapImsSigTrafHandPri_Type()
)
cggsnUmtsQosMapImsSigTrafHandPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cggsnUmtsQosMapImsSigTrafHandPri.setStatus("deprecated")
_CggsnUmtsQosCacPolicyTable_Object = MibTable
cggsnUmtsQosCacPolicyTable = _CggsnUmtsQosCacPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 3)
)
if mibBuilder.loadTexts:
    cggsnUmtsQosCacPolicyTable.setStatus("current")
_CggsnUmtsQosCacPolicyEntry_Object = MibTableRow
cggsnUmtsQosCacPolicyEntry = _CggsnUmtsQosCacPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 3, 1)
)
cggsnUmtsQosCacPolicyEntry.setIndexNames(
    (0, "CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacPolicyName"),
)
if mibBuilder.loadTexts:
    cggsnUmtsQosCacPolicyEntry.setStatus("current")


class _CggsnUmtsQosCacPolicyName_Type(SnmpAdminString):
    """Custom type cggsnUmtsQosCacPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_CggsnUmtsQosCacPolicyName_Type.__name__ = "SnmpAdminString"
_CggsnUmtsQosCacPolicyName_Object = MibTableColumn
cggsnUmtsQosCacPolicyName = _CggsnUmtsQosCacPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 3, 1, 1),
    _CggsnUmtsQosCacPolicyName_Type()
)
cggsnUmtsQosCacPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cggsnUmtsQosCacPolicyName.setStatus("current")
_CggsnUmtsQosCacRowStatus_Type = RowStatus
_CggsnUmtsQosCacRowStatus_Object = MibTableColumn
cggsnUmtsQosCacRowStatus = _CggsnUmtsQosCacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 3, 1, 2),
    _CggsnUmtsQosCacRowStatus_Type()
)
cggsnUmtsQosCacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cggsnUmtsQosCacRowStatus.setStatus("current")


class _CggsnUmtsQosCacMaxPdp_Type(Unsigned32):
    """Custom type cggsnUmtsQosCacMaxPdp based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CggsnUmtsQosCacMaxPdp_Type.__name__ = "Unsigned32"
_CggsnUmtsQosCacMaxPdp_Object = MibTableColumn
cggsnUmtsQosCacMaxPdp = _CggsnUmtsQosCacMaxPdp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 3, 1, 3),
    _CggsnUmtsQosCacMaxPdp_Type()
)
cggsnUmtsQosCacMaxPdp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cggsnUmtsQosCacMaxPdp.setStatus("current")


class _CggsnUmtsQosCacPdpThreshold_Type(Unsigned32):
    """Custom type cggsnUmtsQosCacPdpThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CggsnUmtsQosCacPdpThreshold_Type.__name__ = "Unsigned32"
_CggsnUmtsQosCacPdpThreshold_Object = MibTableColumn
cggsnUmtsQosCacPdpThreshold = _CggsnUmtsQosCacPdpThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 3, 1, 4),
    _CggsnUmtsQosCacPdpThreshold_Type()
)
cggsnUmtsQosCacPdpThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cggsnUmtsQosCacPdpThreshold.setStatus("current")
_CggsnUmtsQosCacMaxTrafficClass_Type = UmtsQosTrafficClass
_CggsnUmtsQosCacMaxTrafficClass_Object = MibTableColumn
cggsnUmtsQosCacMaxTrafficClass = _CggsnUmtsQosCacMaxTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 3, 1, 5),
    _CggsnUmtsQosCacMaxTrafficClass_Type()
)
cggsnUmtsQosCacMaxTrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cggsnUmtsQosCacMaxTrafficClass.setStatus("current")


class _CggsnUmtsQosCacMaxTrafHandPrio_Type(Integer32):
    """Custom type cggsnUmtsQosCacMaxTrafHandPrio based on Integer32"""
    defaultValue = 0

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
        *(("none", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3))
    )


_CggsnUmtsQosCacMaxTrafHandPrio_Type.__name__ = "Integer32"
_CggsnUmtsQosCacMaxTrafHandPrio_Object = MibTableColumn
cggsnUmtsQosCacMaxTrafHandPrio = _CggsnUmtsQosCacMaxTrafHandPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 3, 1, 6),
    _CggsnUmtsQosCacMaxTrafHandPrio_Type()
)
cggsnUmtsQosCacMaxTrafHandPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cggsnUmtsQosCacMaxTrafHandPrio.setStatus("current")


class _CggsnUmtsQosCacMaxThruPut_Type(Unsigned32):
    """Custom type cggsnUmtsQosCacMaxThruPut based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CggsnUmtsQosCacMaxThruPut_Type.__name__ = "Unsigned32"
_CggsnUmtsQosCacMaxThruPut_Object = MibTableColumn
cggsnUmtsQosCacMaxThruPut = _CggsnUmtsQosCacMaxThruPut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 3, 1, 7),
    _CggsnUmtsQosCacMaxThruPut_Type()
)
cggsnUmtsQosCacMaxThruPut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cggsnUmtsQosCacMaxThruPut.setStatus("current")


class _CggsnUmtsQosCacMaxThruPutReject_Type(TruthValue):
    """Custom type cggsnUmtsQosCacMaxThruPutReject based on TruthValue"""


_CggsnUmtsQosCacMaxThruPutReject_Object = MibTableColumn
cggsnUmtsQosCacMaxThruPutReject = _CggsnUmtsQosCacMaxThruPutReject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 3, 1, 8),
    _CggsnUmtsQosCacMaxThruPutReject_Type()
)
cggsnUmtsQosCacMaxThruPutReject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cggsnUmtsQosCacMaxThruPutReject.setStatus("current")


class _CggsnUmtsQosCacMaxDelayClass_Type(Integer32):
    """Custom type cggsnUmtsQosCacMaxDelayClass based on Integer32"""
    defaultValue = 0

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
        *(("delayClass1", 1),
          ("delayClass2", 2),
          ("delayClass3", 3),
          ("delayClass4", 4),
          ("none", 0))
    )


_CggsnUmtsQosCacMaxDelayClass_Type.__name__ = "Integer32"
_CggsnUmtsQosCacMaxDelayClass_Object = MibTableColumn
cggsnUmtsQosCacMaxDelayClass = _CggsnUmtsQosCacMaxDelayClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 3, 1, 9),
    _CggsnUmtsQosCacMaxDelayClass_Type()
)
cggsnUmtsQosCacMaxDelayClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cggsnUmtsQosCacMaxDelayClass.setStatus("current")


class _CggsnUmtsQosCacMaxDelayClassRej_Type(TruthValue):
    """Custom type cggsnUmtsQosCacMaxDelayClassRej based on TruthValue"""


_CggsnUmtsQosCacMaxDelayClassRej_Object = MibTableColumn
cggsnUmtsQosCacMaxDelayClassRej = _CggsnUmtsQosCacMaxDelayClassRej_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 3, 1, 10),
    _CggsnUmtsQosCacMaxDelayClassRej_Type()
)
cggsnUmtsQosCacMaxDelayClassRej.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cggsnUmtsQosCacMaxDelayClassRej.setStatus("current")
_CggsnUmtsQosCacTcTable_Object = MibTable
cggsnUmtsQosCacTcTable = _CggsnUmtsQosCacTcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 4)
)
if mibBuilder.loadTexts:
    cggsnUmtsQosCacTcTable.setStatus("current")
_CggsnUmtsQosCacTcEntry_Object = MibTableRow
cggsnUmtsQosCacTcEntry = _CggsnUmtsQosCacTcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 4, 1)
)
cggsnUmtsQosCacTcEntry.setIndexNames(
    (0, "CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacPolicyName"),
    (0, "CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacTcTrafClass"),
    (0, "CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacTcBitRateType"),
    (0, "CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacTcDirection"),
)
if mibBuilder.loadTexts:
    cggsnUmtsQosCacTcEntry.setStatus("current")
_CggsnUmtsQosCacTcTrafClass_Type = UmtsQosTrafficClass
_CggsnUmtsQosCacTcTrafClass_Object = MibTableColumn
cggsnUmtsQosCacTcTrafClass = _CggsnUmtsQosCacTcTrafClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 4, 1, 1),
    _CggsnUmtsQosCacTcTrafClass_Type()
)
cggsnUmtsQosCacTcTrafClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cggsnUmtsQosCacTcTrafClass.setStatus("current")


class _CggsnUmtsQosCacTcBitRateType_Type(Integer32):
    """Custom type cggsnUmtsQosCacTcBitRateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("guaranteed", 2),
          ("maximum", 1))
    )


_CggsnUmtsQosCacTcBitRateType_Type.__name__ = "Integer32"
_CggsnUmtsQosCacTcBitRateType_Object = MibTableColumn
cggsnUmtsQosCacTcBitRateType = _CggsnUmtsQosCacTcBitRateType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 4, 1, 2),
    _CggsnUmtsQosCacTcBitRateType_Type()
)
cggsnUmtsQosCacTcBitRateType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cggsnUmtsQosCacTcBitRateType.setStatus("current")


class _CggsnUmtsQosCacTcDirection_Type(Integer32):
    """Custom type cggsnUmtsQosCacTcDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downlink", 2),
          ("uplink", 1))
    )


_CggsnUmtsQosCacTcDirection_Type.__name__ = "Integer32"
_CggsnUmtsQosCacTcDirection_Object = MibTableColumn
cggsnUmtsQosCacTcDirection = _CggsnUmtsQosCacTcDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 4, 1, 3),
    _CggsnUmtsQosCacTcDirection_Type()
)
cggsnUmtsQosCacTcDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cggsnUmtsQosCacTcDirection.setStatus("current")
_CggsnUmtsQosCacTcRowStatus_Type = RowStatus
_CggsnUmtsQosCacTcRowStatus_Object = MibTableColumn
cggsnUmtsQosCacTcRowStatus = _CggsnUmtsQosCacTcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 4, 1, 4),
    _CggsnUmtsQosCacTcRowStatus_Type()
)
cggsnUmtsQosCacTcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cggsnUmtsQosCacTcRowStatus.setStatus("current")


class _CggsnUmtsQosCacTcBitRate_Type(Integer32):
    """Custom type cggsnUmtsQosCacTcBitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16000),
    )


_CggsnUmtsQosCacTcBitRate_Type.__name__ = "Integer32"
_CggsnUmtsQosCacTcBitRate_Object = MibTableColumn
cggsnUmtsQosCacTcBitRate = _CggsnUmtsQosCacTcBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 4, 1, 5),
    _CggsnUmtsQosCacTcBitRate_Type()
)
cggsnUmtsQosCacTcBitRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cggsnUmtsQosCacTcBitRate.setStatus("deprecated")
if mibBuilder.loadTexts:
    cggsnUmtsQosCacTcBitRate.setUnits("Kbps")


class _CggsnUmtsQosCacTcReject_Type(TruthValue):
    """Custom type cggsnUmtsQosCacTcReject based on TruthValue"""


_CggsnUmtsQosCacTcReject_Object = MibTableColumn
cggsnUmtsQosCacTcReject = _CggsnUmtsQosCacTcReject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 4, 1, 6),
    _CggsnUmtsQosCacTcReject_Type()
)
cggsnUmtsQosCacTcReject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cggsnUmtsQosCacTcReject.setStatus("current")


class _CggsnUmtsQosCacTcRevBitRate_Type(Unsigned32):
    """Custom type cggsnUmtsQosCacTcRevBitRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256000),
    )


_CggsnUmtsQosCacTcRevBitRate_Type.__name__ = "Unsigned32"
_CggsnUmtsQosCacTcRevBitRate_Object = MibTableColumn
cggsnUmtsQosCacTcRevBitRate = _CggsnUmtsQosCacTcRevBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 4, 1, 7),
    _CggsnUmtsQosCacTcRevBitRate_Type()
)
cggsnUmtsQosCacTcRevBitRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cggsnUmtsQosCacTcRevBitRate.setStatus("current")
if mibBuilder.loadTexts:
    cggsnUmtsQosCacTcRevBitRate.setUnits("Kbps")
_CggsnUmtsQosCacBWPoolTable_Object = MibTable
cggsnUmtsQosCacBWPoolTable = _CggsnUmtsQosCacBWPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 5)
)
if mibBuilder.loadTexts:
    cggsnUmtsQosCacBWPoolTable.setStatus("current")
_CggsnUmtsQosCacBWPoolEntry_Object = MibTableRow
cggsnUmtsQosCacBWPoolEntry = _CggsnUmtsQosCacBWPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 5, 1)
)
cggsnUmtsQosCacBWPoolEntry.setIndexNames(
    (0, "CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacBWPoolName"),
)
if mibBuilder.loadTexts:
    cggsnUmtsQosCacBWPoolEntry.setStatus("current")


class _CggsnUmtsQosCacBWPoolName_Type(SnmpAdminString):
    """Custom type cggsnUmtsQosCacBWPoolName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_CggsnUmtsQosCacBWPoolName_Type.__name__ = "SnmpAdminString"
_CggsnUmtsQosCacBWPoolName_Object = MibTableColumn
cggsnUmtsQosCacBWPoolName = _CggsnUmtsQosCacBWPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 5, 1, 1),
    _CggsnUmtsQosCacBWPoolName_Type()
)
cggsnUmtsQosCacBWPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cggsnUmtsQosCacBWPoolName.setStatus("current")
_CggsnUmtsQosCacBWPoolRowStatus_Type = RowStatus
_CggsnUmtsQosCacBWPoolRowStatus_Object = MibTableColumn
cggsnUmtsQosCacBWPoolRowStatus = _CggsnUmtsQosCacBWPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 5, 1, 2),
    _CggsnUmtsQosCacBWPoolRowStatus_Type()
)
cggsnUmtsQosCacBWPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cggsnUmtsQosCacBWPoolRowStatus.setStatus("current")


class _CggsnUmtsQosCacBWPoolBWVal_Type(Unsigned32):
    """Custom type cggsnUmtsQosCacBWPoolBWVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CggsnUmtsQosCacBWPoolBWVal_Type.__name__ = "Unsigned32"
_CggsnUmtsQosCacBWPoolBWVal_Object = MibTableColumn
cggsnUmtsQosCacBWPoolBWVal = _CggsnUmtsQosCacBWPoolBWVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 5, 1, 3),
    _CggsnUmtsQosCacBWPoolBWVal_Type()
)
cggsnUmtsQosCacBWPoolBWVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cggsnUmtsQosCacBWPoolBWVal.setStatus("current")
if mibBuilder.loadTexts:
    cggsnUmtsQosCacBWPoolBWVal.setUnits("Kbps")
_CggsnQosBWPoolTrafClassTable_Object = MibTable
cggsnQosBWPoolTrafClassTable = _CggsnQosBWPoolTrafClassTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 6)
)
if mibBuilder.loadTexts:
    cggsnQosBWPoolTrafClassTable.setStatus("current")
_CggsnQosBWPoolTrafClassEntry_Object = MibTableRow
cggsnQosBWPoolTrafClassEntry = _CggsnQosBWPoolTrafClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 6, 1)
)
cggsnQosBWPoolTrafClassEntry.setIndexNames(
    (0, "CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacBWPoolName"),
    (0, "CISCO-GGSN-QOS-MIB", "cggsnQosBWPoolTrafClass"),
)
if mibBuilder.loadTexts:
    cggsnQosBWPoolTrafClassEntry.setStatus("current")
_CggsnQosBWPoolTrafClass_Type = UmtsQosTrafficClass
_CggsnQosBWPoolTrafClass_Object = MibTableColumn
cggsnQosBWPoolTrafClass = _CggsnQosBWPoolTrafClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 6, 1, 1),
    _CggsnQosBWPoolTrafClass_Type()
)
cggsnQosBWPoolTrafClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cggsnQosBWPoolTrafClass.setStatus("current")
_CggsnQosBWPoolTrafClassRowStatus_Type = RowStatus
_CggsnQosBWPoolTrafClassRowStatus_Object = MibTableColumn
cggsnQosBWPoolTrafClassRowStatus = _CggsnQosBWPoolTrafClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 6, 1, 2),
    _CggsnQosBWPoolTrafClassRowStatus_Type()
)
cggsnQosBWPoolTrafClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cggsnQosBWPoolTrafClassRowStatus.setStatus("current")


class _CggsnQosBWPoolTrafClassPercent_Type(TruthValue):
    """Custom type cggsnQosBWPoolTrafClassPercent based on TruthValue"""


_CggsnQosBWPoolTrafClassPercent_Object = MibTableColumn
cggsnQosBWPoolTrafClassPercent = _CggsnQosBWPoolTrafClassPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 6, 1, 3),
    _CggsnQosBWPoolTrafClassPercent_Type()
)
cggsnQosBWPoolTrafClassPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cggsnQosBWPoolTrafClassPercent.setStatus("current")


class _CggsnQosBWPoolTrafClassPerVal_Type(Integer32):
    """Custom type cggsnQosBWPoolTrafClassPerVal based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CggsnQosBWPoolTrafClassPerVal_Type.__name__ = "Integer32"
_CggsnQosBWPoolTrafClassPerVal_Object = MibTableColumn
cggsnQosBWPoolTrafClassPerVal = _CggsnQosBWPoolTrafClassPerVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 6, 1, 4),
    _CggsnQosBWPoolTrafClassPerVal_Type()
)
cggsnQosBWPoolTrafClassPerVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cggsnQosBWPoolTrafClassPerVal.setStatus("current")


class _CggsnQosBWPoolTrafClassAbsVal_Type(Unsigned32):
    """Custom type cggsnQosBWPoolTrafClassAbsVal based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CggsnQosBWPoolTrafClassAbsVal_Type.__name__ = "Unsigned32"
_CggsnQosBWPoolTrafClassAbsVal_Object = MibTableColumn
cggsnQosBWPoolTrafClassAbsVal = _CggsnQosBWPoolTrafClassAbsVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 6, 1, 5),
    _CggsnQosBWPoolTrafClassAbsVal_Type()
)
cggsnQosBWPoolTrafClassAbsVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cggsnQosBWPoolTrafClassAbsVal.setStatus("current")


class _CggsnQosBWPoolTrafClassAvailBw_Type(Unsigned32):
    """Custom type cggsnQosBWPoolTrafClassAvailBw based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CggsnQosBWPoolTrafClassAvailBw_Type.__name__ = "Unsigned32"
_CggsnQosBWPoolTrafClassAvailBw_Object = MibTableColumn
cggsnQosBWPoolTrafClassAvailBw = _CggsnQosBWPoolTrafClassAvailBw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 1, 3, 4, 6, 1, 6),
    _CggsnQosBWPoolTrafClassAvailBw_Type()
)
cggsnQosBWPoolTrafClassAvailBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cggsnQosBWPoolTrafClassAvailBw.setStatus("current")
_CggsnQosMIBConformances_ObjectIdentity = ObjectIdentity
cggsnQosMIBConformances = _CggsnQosMIBConformances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 2)
)
_CggsnQosMIBCompliances_ObjectIdentity = ObjectIdentity
cggsnQosMIBCompliances = _CggsnQosMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 2, 1)
)
_CggsnQosMIBGroups_ObjectIdentity = ObjectIdentity
cggsnQosMIBGroups = _CggsnQosMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 2, 2)
)

# Managed Objects groups

cggsnQosGeneralConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 2, 2, 1)
)
cggsnQosGeneralConfigGroup.setObjects(
      *(("CISCO-GGSN-QOS-MIB", "cggsnQosMappingMethod"),
        ("CISCO-GGSN-QOS-MIB", "cggsnQosMappedIpTos"),
        ("CISCO-GGSN-QOS-MIB", "cggsnQosCurrentPdps"))
)
if mibBuilder.loadTexts:
    cggsnQosGeneralConfigGroup.setStatus("current")

cggsnQosCanonicalQosGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 2, 2, 2)
)
cggsnQosCanonicalQosGroup.setObjects(
      *(("CISCO-GGSN-QOS-MIB", "cggsnQosTotalBandwidthResrc"),
        ("CISCO-GGSN-QOS-MIB", "cggsnQosCurrentUsedBandwidth"),
        ("CISCO-GGSN-QOS-MIB", "cggsnQosPremiumMtDeviationFactor"),
        ("CISCO-GGSN-QOS-MIB", "cggsnQosBestEffrtBandWidthFactor"),
        ("CISCO-GGSN-QOS-MIB", "cggsnQosPremiumMeanThroughput"),
        ("CISCO-GGSN-QOS-MIB", "cggsnQosNormalMeanThroughput"),
        ("CISCO-GGSN-QOS-MIB", "cggsnQosBestEffortMeanThroughput"))
)
if mibBuilder.loadTexts:
    cggsnQosCanonicalQosGroup.setStatus("current")

cggsnQosUmtsQosGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 2, 2, 3)
)
cggsnQosUmtsQosGroup.setObjects(
      *(("CISCO-GGSN-QOS-MIB", "cggsnQosUmtsDiffServPhbgroup"),
        ("CISCO-GGSN-QOS-MIB", "cggsnQosUmtsPdps"),
        ("CISCO-GGSN-QOS-MIB", "cggsnQosDscp"),
        ("CISCO-GGSN-QOS-MIB", "cggsnQosUmtsDscpUnmodified"))
)
if mibBuilder.loadTexts:
    cggsnQosUmtsQosGroup.setStatus("current")

cggsnQosUmtsCacGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 2, 2, 4)
)
cggsnQosUmtsCacGroup.setObjects(
      *(("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosMapImsSigTrafClass"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosMapImsSigTrafHandPri"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacRowStatus"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacMaxPdp"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacPdpThreshold"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacMaxTrafficClass"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacMaxTrafHandPrio"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacMaxThruPut"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacMaxThruPutReject"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacMaxDelayClass"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacMaxDelayClassRej"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacTcRowStatus"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacTcBitRate"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacTcReject"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacBWPoolRowStatus"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacBWPoolBWVal"),
        ("CISCO-GGSN-QOS-MIB", "cggsnQosBWPoolTrafClassRowStatus"),
        ("CISCO-GGSN-QOS-MIB", "cggsnQosBWPoolTrafClassPercent"),
        ("CISCO-GGSN-QOS-MIB", "cggsnQosBWPoolTrafClassPerVal"),
        ("CISCO-GGSN-QOS-MIB", "cggsnQosBWPoolTrafClassAbsVal"),
        ("CISCO-GGSN-QOS-MIB", "cggsnQosBWPoolTrafClassAvailBw"))
)
if mibBuilder.loadTexts:
    cggsnQosUmtsCacGroup.setStatus("deprecated")

cggsnQosUmtsCacGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 2, 2, 5)
)
cggsnQosUmtsCacGroupRev1.setObjects(
      *(("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacRowStatus"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacMaxPdp"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacPdpThreshold"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacMaxTrafficClass"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacMaxTrafHandPrio"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacMaxThruPut"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacMaxThruPutReject"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacMaxDelayClass"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacMaxDelayClassRej"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacTcRowStatus"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacTcBitRate"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacTcReject"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacBWPoolRowStatus"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacBWPoolBWVal"),
        ("CISCO-GGSN-QOS-MIB", "cggsnQosBWPoolTrafClassRowStatus"),
        ("CISCO-GGSN-QOS-MIB", "cggsnQosBWPoolTrafClassPercent"),
        ("CISCO-GGSN-QOS-MIB", "cggsnQosBWPoolTrafClassPerVal"),
        ("CISCO-GGSN-QOS-MIB", "cggsnQosBWPoolTrafClassAbsVal"),
        ("CISCO-GGSN-QOS-MIB", "cggsnQosBWPoolTrafClassAvailBw"))
)
if mibBuilder.loadTexts:
    cggsnQosUmtsCacGroupRev1.setStatus("deprecated")

cggsnQosUmtsCacGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 2, 2, 6)
)
cggsnQosUmtsCacGroupRev2.setObjects(
      *(("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacRowStatus"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacMaxPdp"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacPdpThreshold"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacMaxTrafficClass"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacMaxTrafHandPrio"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacMaxThruPut"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacMaxThruPutReject"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacMaxDelayClass"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacMaxDelayClassRej"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacTcRowStatus"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacTcReject"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacTcRevBitRate"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacBWPoolRowStatus"),
        ("CISCO-GGSN-QOS-MIB", "cggsnUmtsQosCacBWPoolBWVal"),
        ("CISCO-GGSN-QOS-MIB", "cggsnQosBWPoolTrafClassRowStatus"),
        ("CISCO-GGSN-QOS-MIB", "cggsnQosBWPoolTrafClassPercent"),
        ("CISCO-GGSN-QOS-MIB", "cggsnQosBWPoolTrafClassPerVal"),
        ("CISCO-GGSN-QOS-MIB", "cggsnQosBWPoolTrafClassAbsVal"),
        ("CISCO-GGSN-QOS-MIB", "cggsnQosBWPoolTrafClassAvailBw"))
)
if mibBuilder.loadTexts:
    cggsnQosUmtsCacGroupRev2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cggsnQosMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cggsnQosMIBCompliance.setStatus(
        "obsolete"
    )

cggsnQosMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cggsnQosMIBComplianceRev1.setStatus(
        "deprecated"
    )

cggsnQosMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cggsnQosMIBComplianceRev2.setStatus(
        "deprecated"
    )

cggsnQosMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 2, 1, 4)
)
if mibBuilder.loadTexts:
    cggsnQosMIBComplianceRev3.setStatus(
        "deprecated"
    )

cggsnQosMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 241, 2, 1, 5)
)
if mibBuilder.loadTexts:
    cggsnQosMIBComplianceRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-GGSN-QOS-MIB",
    **{"UmtsQosTrafficClass": UmtsQosTrafficClass,
       "cggsnQosMIB": cggsnQosMIB,
       "cggsnQosMIBObjects": cggsnQosMIBObjects,
       "cggsnQosGeneralConfig": cggsnQosGeneralConfig,
       "cggsnQosMappingMethod": cggsnQosMappingMethod,
       "cggsnQosClassIpTosMapTable": cggsnQosClassIpTosMapTable,
       "cggsnQosClassIpTosMapEntry": cggsnQosClassIpTosMapEntry,
       "cggsnQosClass": cggsnQosClass,
       "cggsnQosMappedIpTos": cggsnQosMappedIpTos,
       "cggsnQosCurrentPdps": cggsnQosCurrentPdps,
       "cggsnQosCanonicalQos": cggsnQosCanonicalQos,
       "cggsnQosTotalBandwidthResrc": cggsnQosTotalBandwidthResrc,
       "cggsnQosCurrentUsedBandwidth": cggsnQosCurrentUsedBandwidth,
       "cggsnQosPremiumMtDeviationFactor": cggsnQosPremiumMtDeviationFactor,
       "cggsnQosBestEffrtBandWidthFactor": cggsnQosBestEffrtBandWidthFactor,
       "cggsnQosPremiumMeanThroughput": cggsnQosPremiumMeanThroughput,
       "cggsnQosNormalMeanThroughput": cggsnQosNormalMeanThroughput,
       "cggsnQosBestEffortMeanThroughput": cggsnQosBestEffortMeanThroughput,
       "cggsnQosUmtsQos": cggsnQosUmtsQos,
       "cggsnQosTrafficClassPhbTable": cggsnQosTrafficClassPhbTable,
       "cggsnQosTrafficClassPhbEntry": cggsnQosTrafficClassPhbEntry,
       "cggsnQosUmtsTrafficClass": cggsnQosUmtsTrafficClass,
       "cggsnQosUmtsDiffServPhbgroup": cggsnQosUmtsDiffServPhbgroup,
       "cggsnQosUmtsPdps": cggsnQosUmtsPdps,
       "cggsnQosPhbToDscpMapTable": cggsnQosPhbToDscpMapTable,
       "cggsnQosPhbToDscpMapEntry": cggsnQosPhbToDscpMapEntry,
       "cggsnQosDiffServPhb": cggsnQosDiffServPhb,
       "cggsnQosDscp": cggsnQosDscp,
       "cggsnQosUmtsDscpUnmodified": cggsnQosUmtsDscpUnmodified,
       "cggsnQosUmtsCac": cggsnQosUmtsCac,
       "cggsnUmtsQosMapImsSigTrafClass": cggsnUmtsQosMapImsSigTrafClass,
       "cggsnUmtsQosMapImsSigTrafHandPri": cggsnUmtsQosMapImsSigTrafHandPri,
       "cggsnUmtsQosCacPolicyTable": cggsnUmtsQosCacPolicyTable,
       "cggsnUmtsQosCacPolicyEntry": cggsnUmtsQosCacPolicyEntry,
       "cggsnUmtsQosCacPolicyName": cggsnUmtsQosCacPolicyName,
       "cggsnUmtsQosCacRowStatus": cggsnUmtsQosCacRowStatus,
       "cggsnUmtsQosCacMaxPdp": cggsnUmtsQosCacMaxPdp,
       "cggsnUmtsQosCacPdpThreshold": cggsnUmtsQosCacPdpThreshold,
       "cggsnUmtsQosCacMaxTrafficClass": cggsnUmtsQosCacMaxTrafficClass,
       "cggsnUmtsQosCacMaxTrafHandPrio": cggsnUmtsQosCacMaxTrafHandPrio,
       "cggsnUmtsQosCacMaxThruPut": cggsnUmtsQosCacMaxThruPut,
       "cggsnUmtsQosCacMaxThruPutReject": cggsnUmtsQosCacMaxThruPutReject,
       "cggsnUmtsQosCacMaxDelayClass": cggsnUmtsQosCacMaxDelayClass,
       "cggsnUmtsQosCacMaxDelayClassRej": cggsnUmtsQosCacMaxDelayClassRej,
       "cggsnUmtsQosCacTcTable": cggsnUmtsQosCacTcTable,
       "cggsnUmtsQosCacTcEntry": cggsnUmtsQosCacTcEntry,
       "cggsnUmtsQosCacTcTrafClass": cggsnUmtsQosCacTcTrafClass,
       "cggsnUmtsQosCacTcBitRateType": cggsnUmtsQosCacTcBitRateType,
       "cggsnUmtsQosCacTcDirection": cggsnUmtsQosCacTcDirection,
       "cggsnUmtsQosCacTcRowStatus": cggsnUmtsQosCacTcRowStatus,
       "cggsnUmtsQosCacTcBitRate": cggsnUmtsQosCacTcBitRate,
       "cggsnUmtsQosCacTcReject": cggsnUmtsQosCacTcReject,
       "cggsnUmtsQosCacTcRevBitRate": cggsnUmtsQosCacTcRevBitRate,
       "cggsnUmtsQosCacBWPoolTable": cggsnUmtsQosCacBWPoolTable,
       "cggsnUmtsQosCacBWPoolEntry": cggsnUmtsQosCacBWPoolEntry,
       "cggsnUmtsQosCacBWPoolName": cggsnUmtsQosCacBWPoolName,
       "cggsnUmtsQosCacBWPoolRowStatus": cggsnUmtsQosCacBWPoolRowStatus,
       "cggsnUmtsQosCacBWPoolBWVal": cggsnUmtsQosCacBWPoolBWVal,
       "cggsnQosBWPoolTrafClassTable": cggsnQosBWPoolTrafClassTable,
       "cggsnQosBWPoolTrafClassEntry": cggsnQosBWPoolTrafClassEntry,
       "cggsnQosBWPoolTrafClass": cggsnQosBWPoolTrafClass,
       "cggsnQosBWPoolTrafClassRowStatus": cggsnQosBWPoolTrafClassRowStatus,
       "cggsnQosBWPoolTrafClassPercent": cggsnQosBWPoolTrafClassPercent,
       "cggsnQosBWPoolTrafClassPerVal": cggsnQosBWPoolTrafClassPerVal,
       "cggsnQosBWPoolTrafClassAbsVal": cggsnQosBWPoolTrafClassAbsVal,
       "cggsnQosBWPoolTrafClassAvailBw": cggsnQosBWPoolTrafClassAvailBw,
       "cggsnQosMIBConformances": cggsnQosMIBConformances,
       "cggsnQosMIBCompliances": cggsnQosMIBCompliances,
       "cggsnQosMIBCompliance": cggsnQosMIBCompliance,
       "cggsnQosMIBComplianceRev1": cggsnQosMIBComplianceRev1,
       "cggsnQosMIBComplianceRev2": cggsnQosMIBComplianceRev2,
       "cggsnQosMIBComplianceRev3": cggsnQosMIBComplianceRev3,
       "cggsnQosMIBComplianceRev4": cggsnQosMIBComplianceRev4,
       "cggsnQosMIBGroups": cggsnQosMIBGroups,
       "cggsnQosGeneralConfigGroup": cggsnQosGeneralConfigGroup,
       "cggsnQosCanonicalQosGroup": cggsnQosCanonicalQosGroup,
       "cggsnQosUmtsQosGroup": cggsnQosUmtsQosGroup,
       "cggsnQosUmtsCacGroup": cggsnQosUmtsCacGroup,
       "cggsnQosUmtsCacGroupRev1": cggsnQosUmtsCacGroupRev1,
       "cggsnQosUmtsCacGroupRev2": cggsnQosUmtsCacGroupRev2}
)
