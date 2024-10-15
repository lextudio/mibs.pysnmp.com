# SNMP MIB module (IEEE8021-SPB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-SPB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:56 2024
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

(ieee8021BridgeBasePort,) = mibBuilder.importSymbols(
    "IEEE8021-BRIDGE-MIB",
    "ieee8021BridgeBasePort")

(dot1agCfmMaIndex,
 dot1agCfmMdIndex,
 dot1agCfmMepEntry) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "dot1agCfmMaIndex",
    "dot1agCfmMdIndex",
    "dot1agCfmMepEntry")

(IEEE8021BridgePortNumber,
 IEEE8021PbbIngressEgress,
 IEEE8021PbbServiceIdentifier,
 IEEE8021PbbTeEsp,
 ieee802dot1mibs) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021BridgePortNumber",
    "IEEE8021PbbIngressEgress",
    "IEEE8021PbbServiceIdentifier",
    "IEEE8021PbbTeEsp",
    "ieee802dot1mibs")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(VlanId,
 VlanIdOrAny,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIdOrAny",
    "VlanIdOrNone")

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

ieee8021SpbMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 26)
)
ieee8021SpbMib.setRevisions(
        ("2018-06-28 00:00",
         "2015-06-23 00:00",
         "2013-05-13 00:00",
         "2012-02-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IEEE8021SpbAreaAddress(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class IEEE8021SpbEctAlgorithm(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x-"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class IEEE8021SpbMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )



class IEEE8021SpbEctMode(Integer32, TextualConvention):
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
        *(("disabled", 1),
          ("spbm", 2),
          ("spbv", 3))
    )



class IEEE8021SpbDigestConvention(Integer32, TextualConvention):
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
        *(("loopFreeBoth", 2),
          ("loopFreeMcastOnly", 3),
          ("off", 1))
    )



class IEEE8021SpbLinkMetric(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )



class IEEE8021SpbAdjState(Integer32, TextualConvention):
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )



class IEEE8021SpbmSPsourceId(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class IEEE8021SpbDigest(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )



class IEEE8021SpbMCID(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(51, 51),
    )



class IEEE8021SpbBridgePriority(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



class IEEE8021SpbMTID(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class IEEE8021SpbServiceIdentifierOrAny(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(255, 16777215),
    )



# MIB Managed Objects in the order of their OIDs

_Ieee8021SpbObjects_ObjectIdentity = ObjectIdentity
ieee8021SpbObjects = _Ieee8021SpbObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 26, 1)
)
_Ieee8021SpbSys_ObjectIdentity = ObjectIdentity
ieee8021SpbSys = _Ieee8021SpbSys_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 1)
)
_Ieee8021SpbSysAreaAddress_Type = IEEE8021SpbAreaAddress
_Ieee8021SpbSysAreaAddress_Object = MibScalar
ieee8021SpbSysAreaAddress = _Ieee8021SpbSysAreaAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 1, 1),
    _Ieee8021SpbSysAreaAddress_Type()
)
ieee8021SpbSysAreaAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021SpbSysAreaAddress.setStatus("current")
_Ieee8021SpbSysId_Type = MacAddress
_Ieee8021SpbSysId_Object = MibScalar
ieee8021SpbSysId = _Ieee8021SpbSysId_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 1, 2),
    _Ieee8021SpbSysId_Type()
)
ieee8021SpbSysId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021SpbSysId.setStatus("current")
_Ieee8021SpbSysControlAddr_Type = MacAddress
_Ieee8021SpbSysControlAddr_Object = MibScalar
ieee8021SpbSysControlAddr = _Ieee8021SpbSysControlAddr_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 1, 3),
    _Ieee8021SpbSysControlAddr_Type()
)
ieee8021SpbSysControlAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021SpbSysControlAddr.setStatus("current")


class _Ieee8021SpbSysName_Type(SnmpAdminString):
    """Custom type ieee8021SpbSysName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Ieee8021SpbSysName_Type.__name__ = "SnmpAdminString"
_Ieee8021SpbSysName_Object = MibScalar
ieee8021SpbSysName = _Ieee8021SpbSysName_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 1, 4),
    _Ieee8021SpbSysName_Type()
)
ieee8021SpbSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbSysName.setStatus("current")
_Ieee8021SpbSysBridgePriority_Type = IEEE8021SpbBridgePriority
_Ieee8021SpbSysBridgePriority_Object = MibScalar
ieee8021SpbSysBridgePriority = _Ieee8021SpbSysBridgePriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 1, 5),
    _Ieee8021SpbSysBridgePriority_Type()
)
ieee8021SpbSysBridgePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbSysBridgePriority.setStatus("current")
_Ieee8021SpbmSysSPSourceId_Type = IEEE8021SpbmSPsourceId
_Ieee8021SpbmSysSPSourceId_Object = MibScalar
ieee8021SpbmSysSPSourceId = _Ieee8021SpbmSysSPSourceId_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 1, 6),
    _Ieee8021SpbmSysSPSourceId_Type()
)
ieee8021SpbmSysSPSourceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021SpbmSysSPSourceId.setStatus("current")


class _Ieee8021SpbvSysMode_Type(IEEE8021SpbMode):
    """Custom type ieee8021SpbvSysMode based on IEEE8021SpbMode"""


_Ieee8021SpbvSysMode_Object = MibScalar
ieee8021SpbvSysMode = _Ieee8021SpbvSysMode_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 1, 7),
    _Ieee8021SpbvSysMode_Type()
)
ieee8021SpbvSysMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021SpbvSysMode.setStatus("current")


class _Ieee8021SpbmSysMode_Type(IEEE8021SpbMode):
    """Custom type ieee8021SpbmSysMode based on IEEE8021SpbMode"""


_Ieee8021SpbmSysMode_Object = MibScalar
ieee8021SpbmSysMode = _Ieee8021SpbmSysMode_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 1, 8),
    _Ieee8021SpbmSysMode_Type()
)
ieee8021SpbmSysMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021SpbmSysMode.setStatus("current")


class _Ieee8021SpbSysDigestConvention_Type(IEEE8021SpbDigestConvention):
    """Custom type ieee8021SpbSysDigestConvention based on IEEE8021SpbDigestConvention"""


_Ieee8021SpbSysDigestConvention_Object = MibScalar
ieee8021SpbSysDigestConvention = _Ieee8021SpbSysDigestConvention_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 1, 9),
    _Ieee8021SpbSysDigestConvention_Type()
)
ieee8021SpbSysDigestConvention.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021SpbSysDigestConvention.setStatus("current")
_Ieee8021SpbMtidStaticTable_Object = MibTable
ieee8021SpbMtidStaticTable = _Ieee8021SpbMtidStaticTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 2)
)
if mibBuilder.loadTexts:
    ieee8021SpbMtidStaticTable.setStatus("current")
_Ieee8021SpbMtidStaticTableEntry_Object = MibTableRow
ieee8021SpbMtidStaticTableEntry = _Ieee8021SpbMtidStaticTableEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 2, 1)
)
ieee8021SpbMtidStaticTableEntry.setIndexNames(
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbMtidStaticEntryMtid"),
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbTopIx"),
)
if mibBuilder.loadTexts:
    ieee8021SpbMtidStaticTableEntry.setStatus("current")
_Ieee8021SpbMtidStaticEntryMtid_Type = IEEE8021SpbMTID
_Ieee8021SpbMtidStaticEntryMtid_Object = MibTableColumn
ieee8021SpbMtidStaticEntryMtid = _Ieee8021SpbMtidStaticEntryMtid_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 2, 1, 1),
    _Ieee8021SpbMtidStaticEntryMtid_Type()
)
ieee8021SpbMtidStaticEntryMtid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbMtidStaticEntryMtid.setStatus("current")


class _Ieee8021SpbMTidStaticEntryMtidOverload_Type(TruthValue):
    """Custom type ieee8021SpbMTidStaticEntryMtidOverload based on TruthValue"""


_Ieee8021SpbMTidStaticEntryMtidOverload_Object = MibTableColumn
ieee8021SpbMTidStaticEntryMtidOverload = _Ieee8021SpbMTidStaticEntryMtidOverload_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 2, 1, 2),
    _Ieee8021SpbMTidStaticEntryMtidOverload_Type()
)
ieee8021SpbMTidStaticEntryMtidOverload.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021SpbMTidStaticEntryMtidOverload.setStatus("current")
_Ieee8021SpbMtidStaticEntryRowStatus_Type = RowStatus
_Ieee8021SpbMtidStaticEntryRowStatus_Object = MibTableColumn
ieee8021SpbMtidStaticEntryRowStatus = _Ieee8021SpbMtidStaticEntryRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 2, 1, 3),
    _Ieee8021SpbMtidStaticEntryRowStatus_Type()
)
ieee8021SpbMtidStaticEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021SpbMtidStaticEntryRowStatus.setStatus("current")
_Ieee8021SpbTopIx_Type = IEEE8021SpbMTID
_Ieee8021SpbTopIx_Object = MibTableColumn
ieee8021SpbTopIx = _Ieee8021SpbTopIx_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 2, 1, 4),
    _Ieee8021SpbTopIx_Type()
)
ieee8021SpbTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbTopIx.setStatus("current")
_Ieee8021SpbTopIxDynamicTable_Object = MibTable
ieee8021SpbTopIxDynamicTable = _Ieee8021SpbTopIxDynamicTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 3)
)
if mibBuilder.loadTexts:
    ieee8021SpbTopIxDynamicTable.setStatus("current")
_Ieee8021SpbTopIxDynamicTableEntry_Object = MibTableRow
ieee8021SpbTopIxDynamicTableEntry = _Ieee8021SpbTopIxDynamicTableEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 3, 1)
)
ieee8021SpbTopIxDynamicTableEntry.setIndexNames(
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbTopIxDynamicEntryTopIx"),
)
if mibBuilder.loadTexts:
    ieee8021SpbTopIxDynamicTableEntry.setStatus("current")
_Ieee8021SpbTopIxDynamicEntryTopIx_Type = IEEE8021SpbMTID
_Ieee8021SpbTopIxDynamicEntryTopIx_Object = MibTableColumn
ieee8021SpbTopIxDynamicEntryTopIx = _Ieee8021SpbTopIxDynamicEntryTopIx_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 3, 1, 1),
    _Ieee8021SpbTopIxDynamicEntryTopIx_Type()
)
ieee8021SpbTopIxDynamicEntryTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbTopIxDynamicEntryTopIx.setStatus("current")
_Ieee8021SpbTopIxDynamicEntryAgreeDigest_Type = IEEE8021SpbDigest
_Ieee8021SpbTopIxDynamicEntryAgreeDigest_Object = MibTableColumn
ieee8021SpbTopIxDynamicEntryAgreeDigest = _Ieee8021SpbTopIxDynamicEntryAgreeDigest_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 3, 1, 2),
    _Ieee8021SpbTopIxDynamicEntryAgreeDigest_Type()
)
ieee8021SpbTopIxDynamicEntryAgreeDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbTopIxDynamicEntryAgreeDigest.setStatus("current")
_Ieee8021SpbTopIxDynamicEntryMCID_Type = IEEE8021SpbMCID
_Ieee8021SpbTopIxDynamicEntryMCID_Object = MibTableColumn
ieee8021SpbTopIxDynamicEntryMCID = _Ieee8021SpbTopIxDynamicEntryMCID_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 3, 1, 3),
    _Ieee8021SpbTopIxDynamicEntryMCID_Type()
)
ieee8021SpbTopIxDynamicEntryMCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbTopIxDynamicEntryMCID.setStatus("current")
_Ieee8021SpbTopIxDynamicEntryAuxMCID_Type = IEEE8021SpbMCID
_Ieee8021SpbTopIxDynamicEntryAuxMCID_Object = MibTableColumn
ieee8021SpbTopIxDynamicEntryAuxMCID = _Ieee8021SpbTopIxDynamicEntryAuxMCID_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 3, 1, 4),
    _Ieee8021SpbTopIxDynamicEntryAuxMCID_Type()
)
ieee8021SpbTopIxDynamicEntryAuxMCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbTopIxDynamicEntryAuxMCID.setStatus("current")
_Ieee8021SpbEctStaticTable_Object = MibTable
ieee8021SpbEctStaticTable = _Ieee8021SpbEctStaticTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 4)
)
if mibBuilder.loadTexts:
    ieee8021SpbEctStaticTable.setStatus("current")
_Ieee8021SpbEctStaticTableEntry_Object = MibTableRow
ieee8021SpbEctStaticTableEntry = _Ieee8021SpbEctStaticTableEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 4, 1)
)
ieee8021SpbEctStaticTableEntry.setIndexNames(
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbEctStaticEntryTopIx"),
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbEctStaticEntryBaseVid"),
)
if mibBuilder.loadTexts:
    ieee8021SpbEctStaticTableEntry.setStatus("current")
_Ieee8021SpbEctStaticEntryTopIx_Type = IEEE8021SpbMTID
_Ieee8021SpbEctStaticEntryTopIx_Object = MibTableColumn
ieee8021SpbEctStaticEntryTopIx = _Ieee8021SpbEctStaticEntryTopIx_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 4, 1, 1),
    _Ieee8021SpbEctStaticEntryTopIx_Type()
)
ieee8021SpbEctStaticEntryTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbEctStaticEntryTopIx.setStatus("current")
_Ieee8021SpbEctStaticEntryBaseVid_Type = VlanIdOrAny
_Ieee8021SpbEctStaticEntryBaseVid_Object = MibTableColumn
ieee8021SpbEctStaticEntryBaseVid = _Ieee8021SpbEctStaticEntryBaseVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 4, 1, 2),
    _Ieee8021SpbEctStaticEntryBaseVid_Type()
)
ieee8021SpbEctStaticEntryBaseVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbEctStaticEntryBaseVid.setStatus("current")


class _Ieee8021SpbEctStaticEntryEctAlgorithm_Type(IEEE8021SpbEctAlgorithm):
    """Custom type ieee8021SpbEctStaticEntryEctAlgorithm based on IEEE8021SpbEctAlgorithm"""
    defaultValue = OctetString("00-80-c2-01")


_Ieee8021SpbEctStaticEntryEctAlgorithm_Object = MibTableColumn
ieee8021SpbEctStaticEntryEctAlgorithm = _Ieee8021SpbEctStaticEntryEctAlgorithm_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 4, 1, 3),
    _Ieee8021SpbEctStaticEntryEctAlgorithm_Type()
)
ieee8021SpbEctStaticEntryEctAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021SpbEctStaticEntryEctAlgorithm.setStatus("current")
_Ieee8021SpbvEctStaticEntrySpvid_Type = VlanIdOrNone
_Ieee8021SpbvEctStaticEntrySpvid_Object = MibTableColumn
ieee8021SpbvEctStaticEntrySpvid = _Ieee8021SpbvEctStaticEntrySpvid_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 4, 1, 4),
    _Ieee8021SpbvEctStaticEntrySpvid_Type()
)
ieee8021SpbvEctStaticEntrySpvid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021SpbvEctStaticEntrySpvid.setStatus("current")
_Ieee8021SpbEctStaticEntryRowStatus_Type = RowStatus
_Ieee8021SpbEctStaticEntryRowStatus_Object = MibTableColumn
ieee8021SpbEctStaticEntryRowStatus = _Ieee8021SpbEctStaticEntryRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 4, 1, 5),
    _Ieee8021SpbEctStaticEntryRowStatus_Type()
)
ieee8021SpbEctStaticEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021SpbEctStaticEntryRowStatus.setStatus("current")
_Ieee8021SpbEctDynamicTable_Object = MibTable
ieee8021SpbEctDynamicTable = _Ieee8021SpbEctDynamicTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 5)
)
if mibBuilder.loadTexts:
    ieee8021SpbEctDynamicTable.setStatus("current")
_Ieee8021SpbEctDynamicTableEntry_Object = MibTableRow
ieee8021SpbEctDynamicTableEntry = _Ieee8021SpbEctDynamicTableEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 5, 1)
)
ieee8021SpbEctDynamicTableEntry.setIndexNames(
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicEntryTopIx"),
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicEntryBaseVid"),
)
if mibBuilder.loadTexts:
    ieee8021SpbEctDynamicTableEntry.setStatus("current")
_Ieee8021SpbEctDynamicEntryTopIx_Type = IEEE8021SpbMTID
_Ieee8021SpbEctDynamicEntryTopIx_Object = MibTableColumn
ieee8021SpbEctDynamicEntryTopIx = _Ieee8021SpbEctDynamicEntryTopIx_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 5, 1, 1),
    _Ieee8021SpbEctDynamicEntryTopIx_Type()
)
ieee8021SpbEctDynamicEntryTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbEctDynamicEntryTopIx.setStatus("current")
_Ieee8021SpbEctDynamicEntryBaseVid_Type = VlanId
_Ieee8021SpbEctDynamicEntryBaseVid_Object = MibTableColumn
ieee8021SpbEctDynamicEntryBaseVid = _Ieee8021SpbEctDynamicEntryBaseVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 5, 1, 2),
    _Ieee8021SpbEctDynamicEntryBaseVid_Type()
)
ieee8021SpbEctDynamicEntryBaseVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbEctDynamicEntryBaseVid.setStatus("current")
_Ieee8021SpbEctDynamicEntryMode_Type = IEEE8021SpbEctMode
_Ieee8021SpbEctDynamicEntryMode_Object = MibTableColumn
ieee8021SpbEctDynamicEntryMode = _Ieee8021SpbEctDynamicEntryMode_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 5, 1, 3),
    _Ieee8021SpbEctDynamicEntryMode_Type()
)
ieee8021SpbEctDynamicEntryMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbEctDynamicEntryMode.setStatus("current")
_Ieee8021SpbEctDynamicEntryLocalUse_Type = TruthValue
_Ieee8021SpbEctDynamicEntryLocalUse_Object = MibTableColumn
ieee8021SpbEctDynamicEntryLocalUse = _Ieee8021SpbEctDynamicEntryLocalUse_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 5, 1, 4),
    _Ieee8021SpbEctDynamicEntryLocalUse_Type()
)
ieee8021SpbEctDynamicEntryLocalUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbEctDynamicEntryLocalUse.setStatus("current")
_Ieee8021SpbEctDynamicEntryRemoteUse_Type = TruthValue
_Ieee8021SpbEctDynamicEntryRemoteUse_Object = MibTableColumn
ieee8021SpbEctDynamicEntryRemoteUse = _Ieee8021SpbEctDynamicEntryRemoteUse_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 5, 1, 5),
    _Ieee8021SpbEctDynamicEntryRemoteUse_Type()
)
ieee8021SpbEctDynamicEntryRemoteUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbEctDynamicEntryRemoteUse.setStatus("current")
_Ieee8021SpbEctDynamicEntryIngressCheckDiscards_Type = Unsigned32
_Ieee8021SpbEctDynamicEntryIngressCheckDiscards_Object = MibTableColumn
ieee8021SpbEctDynamicEntryIngressCheckDiscards = _Ieee8021SpbEctDynamicEntryIngressCheckDiscards_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 5, 1, 6),
    _Ieee8021SpbEctDynamicEntryIngressCheckDiscards_Type()
)
ieee8021SpbEctDynamicEntryIngressCheckDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbEctDynamicEntryIngressCheckDiscards.setStatus("current")
_Ieee8021SpbAdjStaticTable_Object = MibTable
ieee8021SpbAdjStaticTable = _Ieee8021SpbAdjStaticTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 6)
)
if mibBuilder.loadTexts:
    ieee8021SpbAdjStaticTable.setStatus("current")
_Ieee8021SpbAdjStaticTableEntry_Object = MibTableRow
ieee8021SpbAdjStaticTableEntry = _Ieee8021SpbAdjStaticTableEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 6, 1)
)
ieee8021SpbAdjStaticTableEntry.setIndexNames(
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbAdjStaticEntryTopIx"),
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbAdjStaticEntryIfIndex"),
)
if mibBuilder.loadTexts:
    ieee8021SpbAdjStaticTableEntry.setStatus("current")
_Ieee8021SpbAdjStaticEntryTopIx_Type = IEEE8021SpbMTID
_Ieee8021SpbAdjStaticEntryTopIx_Object = MibTableColumn
ieee8021SpbAdjStaticEntryTopIx = _Ieee8021SpbAdjStaticEntryTopIx_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 6, 1, 1),
    _Ieee8021SpbAdjStaticEntryTopIx_Type()
)
ieee8021SpbAdjStaticEntryTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbAdjStaticEntryTopIx.setStatus("current")
_Ieee8021SpbAdjStaticEntryIfIndex_Type = InterfaceIndexOrZero
_Ieee8021SpbAdjStaticEntryIfIndex_Object = MibTableColumn
ieee8021SpbAdjStaticEntryIfIndex = _Ieee8021SpbAdjStaticEntryIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 6, 1, 2),
    _Ieee8021SpbAdjStaticEntryIfIndex_Type()
)
ieee8021SpbAdjStaticEntryIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbAdjStaticEntryIfIndex.setStatus("current")
_Ieee8021SpbAdjStaticEntryMetric_Type = IEEE8021SpbLinkMetric
_Ieee8021SpbAdjStaticEntryMetric_Object = MibTableColumn
ieee8021SpbAdjStaticEntryMetric = _Ieee8021SpbAdjStaticEntryMetric_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 6, 1, 3),
    _Ieee8021SpbAdjStaticEntryMetric_Type()
)
ieee8021SpbAdjStaticEntryMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021SpbAdjStaticEntryMetric.setStatus("current")
_Ieee8021SpbAdjStaticEntryIfAdminState_Type = IEEE8021SpbAdjState
_Ieee8021SpbAdjStaticEntryIfAdminState_Object = MibTableColumn
ieee8021SpbAdjStaticEntryIfAdminState = _Ieee8021SpbAdjStaticEntryIfAdminState_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 6, 1, 4),
    _Ieee8021SpbAdjStaticEntryIfAdminState_Type()
)
ieee8021SpbAdjStaticEntryIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021SpbAdjStaticEntryIfAdminState.setStatus("current")
_Ieee8021SpbAdjStaticEntryRowStatus_Type = RowStatus
_Ieee8021SpbAdjStaticEntryRowStatus_Object = MibTableColumn
ieee8021SpbAdjStaticEntryRowStatus = _Ieee8021SpbAdjStaticEntryRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 6, 1, 5),
    _Ieee8021SpbAdjStaticEntryRowStatus_Type()
)
ieee8021SpbAdjStaticEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021SpbAdjStaticEntryRowStatus.setStatus("current")
_Ieee8021SpbAdjDynamicTable_Object = MibTable
ieee8021SpbAdjDynamicTable = _Ieee8021SpbAdjDynamicTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 7)
)
if mibBuilder.loadTexts:
    ieee8021SpbAdjDynamicTable.setStatus("current")
_Ieee8021SpbAdjDynamicTableEntry_Object = MibTableRow
ieee8021SpbAdjDynamicTableEntry = _Ieee8021SpbAdjDynamicTableEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1)
)
ieee8021SpbAdjDynamicTableEntry.setIndexNames(
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryTopIx"),
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryIfIndex"),
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerSysId"),
)
if mibBuilder.loadTexts:
    ieee8021SpbAdjDynamicTableEntry.setStatus("current")
_Ieee8021SpbAdjDynamicEntryTopIx_Type = IEEE8021SpbMTID
_Ieee8021SpbAdjDynamicEntryTopIx_Object = MibTableColumn
ieee8021SpbAdjDynamicEntryTopIx = _Ieee8021SpbAdjDynamicEntryTopIx_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1, 1),
    _Ieee8021SpbAdjDynamicEntryTopIx_Type()
)
ieee8021SpbAdjDynamicEntryTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbAdjDynamicEntryTopIx.setStatus("current")
_Ieee8021SpbAdjDynamicEntryIfIndex_Type = InterfaceIndexOrZero
_Ieee8021SpbAdjDynamicEntryIfIndex_Object = MibTableColumn
ieee8021SpbAdjDynamicEntryIfIndex = _Ieee8021SpbAdjDynamicEntryIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1, 2),
    _Ieee8021SpbAdjDynamicEntryIfIndex_Type()
)
ieee8021SpbAdjDynamicEntryIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbAdjDynamicEntryIfIndex.setStatus("current")
_Ieee8021SpbAdjDynamicEntryPeerSysId_Type = MacAddress
_Ieee8021SpbAdjDynamicEntryPeerSysId_Object = MibTableColumn
ieee8021SpbAdjDynamicEntryPeerSysId = _Ieee8021SpbAdjDynamicEntryPeerSysId_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1, 3),
    _Ieee8021SpbAdjDynamicEntryPeerSysId_Type()
)
ieee8021SpbAdjDynamicEntryPeerSysId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbAdjDynamicEntryPeerSysId.setStatus("current")
_Ieee8021SpbAdjDynamicEntryPort_Type = IEEE8021BridgePortNumber
_Ieee8021SpbAdjDynamicEntryPort_Object = MibTableColumn
ieee8021SpbAdjDynamicEntryPort = _Ieee8021SpbAdjDynamicEntryPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1, 4),
    _Ieee8021SpbAdjDynamicEntryPort_Type()
)
ieee8021SpbAdjDynamicEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbAdjDynamicEntryPort.setStatus("current")
_Ieee8021SpbAdjDynamicEntryIfOperState_Type = IEEE8021SpbAdjState
_Ieee8021SpbAdjDynamicEntryIfOperState_Object = MibTableColumn
ieee8021SpbAdjDynamicEntryIfOperState = _Ieee8021SpbAdjDynamicEntryIfOperState_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1, 5),
    _Ieee8021SpbAdjDynamicEntryIfOperState_Type()
)
ieee8021SpbAdjDynamicEntryIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbAdjDynamicEntryIfOperState.setStatus("current")


class _Ieee8021SpbAdjDynamicEntryPeerSysName_Type(SnmpAdminString):
    """Custom type ieee8021SpbAdjDynamicEntryPeerSysName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Ieee8021SpbAdjDynamicEntryPeerSysName_Type.__name__ = "SnmpAdminString"
_Ieee8021SpbAdjDynamicEntryPeerSysName_Object = MibTableColumn
ieee8021SpbAdjDynamicEntryPeerSysName = _Ieee8021SpbAdjDynamicEntryPeerSysName_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1, 6),
    _Ieee8021SpbAdjDynamicEntryPeerSysName_Type()
)
ieee8021SpbAdjDynamicEntryPeerSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbAdjDynamicEntryPeerSysName.setStatus("current")
_Ieee8021SpbAdjDynamicEntryPeerAgreeDigest_Type = IEEE8021SpbDigest
_Ieee8021SpbAdjDynamicEntryPeerAgreeDigest_Object = MibTableColumn
ieee8021SpbAdjDynamicEntryPeerAgreeDigest = _Ieee8021SpbAdjDynamicEntryPeerAgreeDigest_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1, 7),
    _Ieee8021SpbAdjDynamicEntryPeerAgreeDigest_Type()
)
ieee8021SpbAdjDynamicEntryPeerAgreeDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbAdjDynamicEntryPeerAgreeDigest.setStatus("current")
_Ieee8021SpbAdjDynamicEntryPeerMCID_Type = IEEE8021SpbMCID
_Ieee8021SpbAdjDynamicEntryPeerMCID_Object = MibTableColumn
ieee8021SpbAdjDynamicEntryPeerMCID = _Ieee8021SpbAdjDynamicEntryPeerMCID_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1, 8),
    _Ieee8021SpbAdjDynamicEntryPeerMCID_Type()
)
ieee8021SpbAdjDynamicEntryPeerMCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbAdjDynamicEntryPeerMCID.setStatus("current")
_Ieee8021SpbAdjDynamicEntryPeerAuxMCID_Type = IEEE8021SpbMCID
_Ieee8021SpbAdjDynamicEntryPeerAuxMCID_Object = MibTableColumn
ieee8021SpbAdjDynamicEntryPeerAuxMCID = _Ieee8021SpbAdjDynamicEntryPeerAuxMCID_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1, 9),
    _Ieee8021SpbAdjDynamicEntryPeerAuxMCID_Type()
)
ieee8021SpbAdjDynamicEntryPeerAuxMCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbAdjDynamicEntryPeerAuxMCID.setStatus("current")
_Ieee8021SpbAdjDynamicEntryLocalCircuitID_Type = Unsigned32
_Ieee8021SpbAdjDynamicEntryLocalCircuitID_Object = MibTableColumn
ieee8021SpbAdjDynamicEntryLocalCircuitID = _Ieee8021SpbAdjDynamicEntryLocalCircuitID_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1, 10),
    _Ieee8021SpbAdjDynamicEntryLocalCircuitID_Type()
)
ieee8021SpbAdjDynamicEntryLocalCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbAdjDynamicEntryLocalCircuitID.setStatus("current")
_Ieee8021SpbAdjDynamicEntryPeerLocalCircuitID_Type = Unsigned32
_Ieee8021SpbAdjDynamicEntryPeerLocalCircuitID_Object = MibTableColumn
ieee8021SpbAdjDynamicEntryPeerLocalCircuitID = _Ieee8021SpbAdjDynamicEntryPeerLocalCircuitID_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1, 11),
    _Ieee8021SpbAdjDynamicEntryPeerLocalCircuitID_Type()
)
ieee8021SpbAdjDynamicEntryPeerLocalCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbAdjDynamicEntryPeerLocalCircuitID.setStatus("current")
_Ieee8021SpbAdjDynamicEntryPortIdentifier_Type = Unsigned32
_Ieee8021SpbAdjDynamicEntryPortIdentifier_Object = MibTableColumn
ieee8021SpbAdjDynamicEntryPortIdentifier = _Ieee8021SpbAdjDynamicEntryPortIdentifier_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1, 12),
    _Ieee8021SpbAdjDynamicEntryPortIdentifier_Type()
)
ieee8021SpbAdjDynamicEntryPortIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbAdjDynamicEntryPortIdentifier.setStatus("current")
_Ieee8021SpbAdjDynamicEntryPeerPortIdentifier_Type = Unsigned32
_Ieee8021SpbAdjDynamicEntryPeerPortIdentifier_Object = MibTableColumn
ieee8021SpbAdjDynamicEntryPeerPortIdentifier = _Ieee8021SpbAdjDynamicEntryPeerPortIdentifier_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1, 13),
    _Ieee8021SpbAdjDynamicEntryPeerPortIdentifier_Type()
)
ieee8021SpbAdjDynamicEntryPeerPortIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbAdjDynamicEntryPeerPortIdentifier.setStatus("current")
_Ieee8021SpbAdjDynamicEntryIsisCircIndex_Type = Unsigned32
_Ieee8021SpbAdjDynamicEntryIsisCircIndex_Object = MibTableColumn
ieee8021SpbAdjDynamicEntryIsisCircIndex = _Ieee8021SpbAdjDynamicEntryIsisCircIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1, 14),
    _Ieee8021SpbAdjDynamicEntryIsisCircIndex_Type()
)
ieee8021SpbAdjDynamicEntryIsisCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbAdjDynamicEntryIsisCircIndex.setStatus("current")
_Ieee8021SpbTopNodeTable_Object = MibTable
ieee8021SpbTopNodeTable = _Ieee8021SpbTopNodeTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 8)
)
if mibBuilder.loadTexts:
    ieee8021SpbTopNodeTable.setStatus("current")
_Ieee8021SpbTopNodeTableEntry_Object = MibTableRow
ieee8021SpbTopNodeTableEntry = _Ieee8021SpbTopNodeTableEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 8, 1)
)
ieee8021SpbTopNodeTableEntry.setIndexNames(
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbTopNodeEntryTopIx"),
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbTopNodeEntrySysId"),
)
if mibBuilder.loadTexts:
    ieee8021SpbTopNodeTableEntry.setStatus("current")
_Ieee8021SpbTopNodeEntryTopIx_Type = IEEE8021SpbMTID
_Ieee8021SpbTopNodeEntryTopIx_Object = MibTableColumn
ieee8021SpbTopNodeEntryTopIx = _Ieee8021SpbTopNodeEntryTopIx_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 8, 1, 1),
    _Ieee8021SpbTopNodeEntryTopIx_Type()
)
ieee8021SpbTopNodeEntryTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbTopNodeEntryTopIx.setStatus("current")
_Ieee8021SpbTopNodeEntrySysId_Type = MacAddress
_Ieee8021SpbTopNodeEntrySysId_Object = MibTableColumn
ieee8021SpbTopNodeEntrySysId = _Ieee8021SpbTopNodeEntrySysId_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 8, 1, 2),
    _Ieee8021SpbTopNodeEntrySysId_Type()
)
ieee8021SpbTopNodeEntrySysId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbTopNodeEntrySysId.setStatus("current")
_Ieee8021SpbTopNodeEntryBridgePriority_Type = IEEE8021SpbBridgePriority
_Ieee8021SpbTopNodeEntryBridgePriority_Object = MibTableColumn
ieee8021SpbTopNodeEntryBridgePriority = _Ieee8021SpbTopNodeEntryBridgePriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 8, 1, 3),
    _Ieee8021SpbTopNodeEntryBridgePriority_Type()
)
ieee8021SpbTopNodeEntryBridgePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbTopNodeEntryBridgePriority.setStatus("current")
_Ieee8021SpbmTopNodeEntrySPsourceID_Type = IEEE8021SpbmSPsourceId
_Ieee8021SpbmTopNodeEntrySPsourceID_Object = MibTableColumn
ieee8021SpbmTopNodeEntrySPsourceID = _Ieee8021SpbmTopNodeEntrySPsourceID_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 8, 1, 4),
    _Ieee8021SpbmTopNodeEntrySPsourceID_Type()
)
ieee8021SpbmTopNodeEntrySPsourceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbmTopNodeEntrySPsourceID.setStatus("current")


class _Ieee8021SpbTopNodeEntrySysName_Type(SnmpAdminString):
    """Custom type ieee8021SpbTopNodeEntrySysName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Ieee8021SpbTopNodeEntrySysName_Type.__name__ = "SnmpAdminString"
_Ieee8021SpbTopNodeEntrySysName_Object = MibTableColumn
ieee8021SpbTopNodeEntrySysName = _Ieee8021SpbTopNodeEntrySysName_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 8, 1, 5),
    _Ieee8021SpbTopNodeEntrySysName_Type()
)
ieee8021SpbTopNodeEntrySysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbTopNodeEntrySysName.setStatus("current")
_Ieee8021SpbTopEctTable_Object = MibTable
ieee8021SpbTopEctTable = _Ieee8021SpbTopEctTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 9)
)
if mibBuilder.loadTexts:
    ieee8021SpbTopEctTable.setStatus("current")
_Ieee8021SpbTopEctTableEntry_Object = MibTableRow
ieee8021SpbTopEctTableEntry = _Ieee8021SpbTopEctTableEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 9, 1)
)
ieee8021SpbTopEctTableEntry.setIndexNames(
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbTopEctEntryTopIx"),
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbTopEctEntrySysId"),
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbTopEctEntryBaseVid"),
)
if mibBuilder.loadTexts:
    ieee8021SpbTopEctTableEntry.setStatus("current")
_Ieee8021SpbTopEctEntryTopIx_Type = IEEE8021SpbMTID
_Ieee8021SpbTopEctEntryTopIx_Object = MibTableColumn
ieee8021SpbTopEctEntryTopIx = _Ieee8021SpbTopEctEntryTopIx_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 9, 1, 1),
    _Ieee8021SpbTopEctEntryTopIx_Type()
)
ieee8021SpbTopEctEntryTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbTopEctEntryTopIx.setStatus("current")
_Ieee8021SpbTopEctEntrySysId_Type = MacAddress
_Ieee8021SpbTopEctEntrySysId_Object = MibTableColumn
ieee8021SpbTopEctEntrySysId = _Ieee8021SpbTopEctEntrySysId_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 9, 1, 2),
    _Ieee8021SpbTopEctEntrySysId_Type()
)
ieee8021SpbTopEctEntrySysId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbTopEctEntrySysId.setStatus("current")
_Ieee8021SpbTopEctEntryBaseVid_Type = VlanIdOrAny
_Ieee8021SpbTopEctEntryBaseVid_Object = MibTableColumn
ieee8021SpbTopEctEntryBaseVid = _Ieee8021SpbTopEctEntryBaseVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 9, 1, 3),
    _Ieee8021SpbTopEctEntryBaseVid_Type()
)
ieee8021SpbTopEctEntryBaseVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbTopEctEntryBaseVid.setStatus("current")
_Ieee8021SpbTopEctEntryEctAlgorithm_Type = IEEE8021SpbEctAlgorithm
_Ieee8021SpbTopEctEntryEctAlgorithm_Object = MibTableColumn
ieee8021SpbTopEctEntryEctAlgorithm = _Ieee8021SpbTopEctEntryEctAlgorithm_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 9, 1, 4),
    _Ieee8021SpbTopEctEntryEctAlgorithm_Type()
)
ieee8021SpbTopEctEntryEctAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbTopEctEntryEctAlgorithm.setStatus("current")
_Ieee8021SpbTopEctEntryMode_Type = IEEE8021SpbEctMode
_Ieee8021SpbTopEctEntryMode_Object = MibTableColumn
ieee8021SpbTopEctEntryMode = _Ieee8021SpbTopEctEntryMode_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 9, 1, 5),
    _Ieee8021SpbTopEctEntryMode_Type()
)
ieee8021SpbTopEctEntryMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbTopEctEntryMode.setStatus("current")
_Ieee8021SpbvTopEctSysMode_Type = IEEE8021SpbMode
_Ieee8021SpbvTopEctSysMode_Object = MibTableColumn
ieee8021SpbvTopEctSysMode = _Ieee8021SpbvTopEctSysMode_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 9, 1, 6),
    _Ieee8021SpbvTopEctSysMode_Type()
)
ieee8021SpbvTopEctSysMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbvTopEctSysMode.setStatus("current")
_Ieee8021SpbvTopEctEntrySpvid_Type = VlanIdOrNone
_Ieee8021SpbvTopEctEntrySpvid_Object = MibTableColumn
ieee8021SpbvTopEctEntrySpvid = _Ieee8021SpbvTopEctEntrySpvid_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 9, 1, 7),
    _Ieee8021SpbvTopEctEntrySpvid_Type()
)
ieee8021SpbvTopEctEntrySpvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbvTopEctEntrySpvid.setStatus("current")
_Ieee8021SpbTopEctEntryLocalUse_Type = TruthValue
_Ieee8021SpbTopEctEntryLocalUse_Object = MibTableColumn
ieee8021SpbTopEctEntryLocalUse = _Ieee8021SpbTopEctEntryLocalUse_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 9, 1, 8),
    _Ieee8021SpbTopEctEntryLocalUse_Type()
)
ieee8021SpbTopEctEntryLocalUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbTopEctEntryLocalUse.setStatus("current")
_Ieee8021SpbTopEdgeTable_Object = MibTable
ieee8021SpbTopEdgeTable = _Ieee8021SpbTopEdgeTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 10)
)
if mibBuilder.loadTexts:
    ieee8021SpbTopEdgeTable.setStatus("current")
_Ieee8021SpbTopEdgeTableEntry_Object = MibTableRow
ieee8021SpbTopEdgeTableEntry = _Ieee8021SpbTopEdgeTableEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 10, 1)
)
ieee8021SpbTopEdgeTableEntry.setIndexNames(
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbTopEdgeEntryTopIx"),
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbTopEdgeEntrySysIdNear"),
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbTopEdgeEntrySysIdFar"),
)
if mibBuilder.loadTexts:
    ieee8021SpbTopEdgeTableEntry.setStatus("current")
_Ieee8021SpbTopEdgeEntryTopIx_Type = IEEE8021SpbMTID
_Ieee8021SpbTopEdgeEntryTopIx_Object = MibTableColumn
ieee8021SpbTopEdgeEntryTopIx = _Ieee8021SpbTopEdgeEntryTopIx_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 10, 1, 1),
    _Ieee8021SpbTopEdgeEntryTopIx_Type()
)
ieee8021SpbTopEdgeEntryTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbTopEdgeEntryTopIx.setStatus("current")
_Ieee8021SpbTopEdgeEntrySysIdNear_Type = MacAddress
_Ieee8021SpbTopEdgeEntrySysIdNear_Object = MibTableColumn
ieee8021SpbTopEdgeEntrySysIdNear = _Ieee8021SpbTopEdgeEntrySysIdNear_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 10, 1, 2),
    _Ieee8021SpbTopEdgeEntrySysIdNear_Type()
)
ieee8021SpbTopEdgeEntrySysIdNear.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbTopEdgeEntrySysIdNear.setStatus("current")
_Ieee8021SpbTopEdgeEntrySysIdFar_Type = MacAddress
_Ieee8021SpbTopEdgeEntrySysIdFar_Object = MibTableColumn
ieee8021SpbTopEdgeEntrySysIdFar = _Ieee8021SpbTopEdgeEntrySysIdFar_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 10, 1, 3),
    _Ieee8021SpbTopEdgeEntrySysIdFar_Type()
)
ieee8021SpbTopEdgeEntrySysIdFar.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbTopEdgeEntrySysIdFar.setStatus("current")
_Ieee8021SpbTopEdgeEntryMetricNear2Far_Type = IEEE8021SpbLinkMetric
_Ieee8021SpbTopEdgeEntryMetricNear2Far_Object = MibTableColumn
ieee8021SpbTopEdgeEntryMetricNear2Far = _Ieee8021SpbTopEdgeEntryMetricNear2Far_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 10, 1, 4),
    _Ieee8021SpbTopEdgeEntryMetricNear2Far_Type()
)
ieee8021SpbTopEdgeEntryMetricNear2Far.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbTopEdgeEntryMetricNear2Far.setStatus("current")
_Ieee8021SpbTopEdgeEntryMetricFar2Near_Type = IEEE8021SpbLinkMetric
_Ieee8021SpbTopEdgeEntryMetricFar2Near_Object = MibTableColumn
ieee8021SpbTopEdgeEntryMetricFar2Near = _Ieee8021SpbTopEdgeEntryMetricFar2Near_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 10, 1, 5),
    _Ieee8021SpbTopEdgeEntryMetricFar2Near_Type()
)
ieee8021SpbTopEdgeEntryMetricFar2Near.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbTopEdgeEntryMetricFar2Near.setStatus("current")
_Ieee8021SpbmTopSrvTable_Object = MibTable
ieee8021SpbmTopSrvTable = _Ieee8021SpbmTopSrvTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 11)
)
if mibBuilder.loadTexts:
    ieee8021SpbmTopSrvTable.setStatus("current")
_Ieee8021SpbmTopSrvTableEntry_Object = MibTableRow
ieee8021SpbmTopSrvTableEntry = _Ieee8021SpbmTopSrvTableEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 11, 1)
)
ieee8021SpbmTopSrvTableEntry.setIndexNames(
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbmTopSrvEntryTopIx"),
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbmTopSrvEntrySysId"),
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbmTopSrvEntryIsid"),
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbmTopSrvEntryBaseVid"),
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbmTopSrvEntryMac"),
)
if mibBuilder.loadTexts:
    ieee8021SpbmTopSrvTableEntry.setStatus("current")
_Ieee8021SpbmTopSrvEntryTopIx_Type = IEEE8021SpbMTID
_Ieee8021SpbmTopSrvEntryTopIx_Object = MibTableColumn
ieee8021SpbmTopSrvEntryTopIx = _Ieee8021SpbmTopSrvEntryTopIx_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 11, 1, 1),
    _Ieee8021SpbmTopSrvEntryTopIx_Type()
)
ieee8021SpbmTopSrvEntryTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbmTopSrvEntryTopIx.setStatus("current")
_Ieee8021SpbmTopSrvEntrySysId_Type = MacAddress
_Ieee8021SpbmTopSrvEntrySysId_Object = MibTableColumn
ieee8021SpbmTopSrvEntrySysId = _Ieee8021SpbmTopSrvEntrySysId_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 11, 1, 2),
    _Ieee8021SpbmTopSrvEntrySysId_Type()
)
ieee8021SpbmTopSrvEntrySysId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbmTopSrvEntrySysId.setStatus("current")
_Ieee8021SpbmTopSrvEntryIsid_Type = IEEE8021SpbServiceIdentifierOrAny
_Ieee8021SpbmTopSrvEntryIsid_Object = MibTableColumn
ieee8021SpbmTopSrvEntryIsid = _Ieee8021SpbmTopSrvEntryIsid_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 11, 1, 3),
    _Ieee8021SpbmTopSrvEntryIsid_Type()
)
ieee8021SpbmTopSrvEntryIsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbmTopSrvEntryIsid.setStatus("current")
_Ieee8021SpbmTopSrvEntryBaseVid_Type = VlanIdOrAny
_Ieee8021SpbmTopSrvEntryBaseVid_Object = MibTableColumn
ieee8021SpbmTopSrvEntryBaseVid = _Ieee8021SpbmTopSrvEntryBaseVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 11, 1, 4),
    _Ieee8021SpbmTopSrvEntryBaseVid_Type()
)
ieee8021SpbmTopSrvEntryBaseVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbmTopSrvEntryBaseVid.setStatus("current")
_Ieee8021SpbmTopSrvEntryMac_Type = MacAddress
_Ieee8021SpbmTopSrvEntryMac_Object = MibTableColumn
ieee8021SpbmTopSrvEntryMac = _Ieee8021SpbmTopSrvEntryMac_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 11, 1, 5),
    _Ieee8021SpbmTopSrvEntryMac_Type()
)
ieee8021SpbmTopSrvEntryMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbmTopSrvEntryMac.setStatus("current")
_Ieee8021SpbmTopSrvEntryIsidFlags_Type = IEEE8021PbbIngressEgress
_Ieee8021SpbmTopSrvEntryIsidFlags_Object = MibTableColumn
ieee8021SpbmTopSrvEntryIsidFlags = _Ieee8021SpbmTopSrvEntryIsidFlags_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 11, 1, 6),
    _Ieee8021SpbmTopSrvEntryIsidFlags_Type()
)
ieee8021SpbmTopSrvEntryIsidFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbmTopSrvEntryIsidFlags.setStatus("current")
_Ieee8021SpbvTopSrvTable_Object = MibTable
ieee8021SpbvTopSrvTable = _Ieee8021SpbvTopSrvTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 12)
)
if mibBuilder.loadTexts:
    ieee8021SpbvTopSrvTable.setStatus("current")
_Ieee8021SpbvTopSrvTableEntry_Object = MibTableRow
ieee8021SpbvTopSrvTableEntry = _Ieee8021SpbvTopSrvTableEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 12, 1)
)
ieee8021SpbvTopSrvTableEntry.setIndexNames(
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbvTopSrvEntryTopIx"),
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbvTopSrvEntrySysId"),
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbvTopSrvEntryMMac"),
)
if mibBuilder.loadTexts:
    ieee8021SpbvTopSrvTableEntry.setStatus("current")
_Ieee8021SpbvTopSrvEntryTopIx_Type = IEEE8021SpbMTID
_Ieee8021SpbvTopSrvEntryTopIx_Object = MibTableColumn
ieee8021SpbvTopSrvEntryTopIx = _Ieee8021SpbvTopSrvEntryTopIx_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 12, 1, 1),
    _Ieee8021SpbvTopSrvEntryTopIx_Type()
)
ieee8021SpbvTopSrvEntryTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbvTopSrvEntryTopIx.setStatus("current")
_Ieee8021SpbvTopSrvEntrySysId_Type = MacAddress
_Ieee8021SpbvTopSrvEntrySysId_Object = MibTableColumn
ieee8021SpbvTopSrvEntrySysId = _Ieee8021SpbvTopSrvEntrySysId_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 12, 1, 2),
    _Ieee8021SpbvTopSrvEntrySysId_Type()
)
ieee8021SpbvTopSrvEntrySysId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbvTopSrvEntrySysId.setStatus("current")
_Ieee8021SpbvTopSrvEntryMMac_Type = MacAddress
_Ieee8021SpbvTopSrvEntryMMac_Object = MibTableColumn
ieee8021SpbvTopSrvEntryMMac = _Ieee8021SpbvTopSrvEntryMMac_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 12, 1, 3),
    _Ieee8021SpbvTopSrvEntryMMac_Type()
)
ieee8021SpbvTopSrvEntryMMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbvTopSrvEntryMMac.setStatus("current")
_Ieee8021SpbvTopSrvEntryBaseVid_Type = VlanId
_Ieee8021SpbvTopSrvEntryBaseVid_Object = MibTableColumn
ieee8021SpbvTopSrvEntryBaseVid = _Ieee8021SpbvTopSrvEntryBaseVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 12, 1, 4),
    _Ieee8021SpbvTopSrvEntryBaseVid_Type()
)
ieee8021SpbvTopSrvEntryBaseVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbvTopSrvEntryBaseVid.setStatus("current")
_Ieee8021SpbvTopSrvEntryMMacFlags_Type = IEEE8021PbbIngressEgress
_Ieee8021SpbvTopSrvEntryMMacFlags_Object = MibTableColumn
ieee8021SpbvTopSrvEntryMMacFlags = _Ieee8021SpbvTopSrvEntryMMacFlags_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 12, 1, 5),
    _Ieee8021SpbvTopSrvEntryMMacFlags_Type()
)
ieee8021SpbvTopSrvEntryMMacFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpbvTopSrvEntryMMacFlags.setStatus("current")
_Ieee8021SpbmBsiStaticTable_Object = MibTable
ieee8021SpbmBsiStaticTable = _Ieee8021SpbmBsiStaticTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 13)
)
if mibBuilder.loadTexts:
    ieee8021SpbmBsiStaticTable.setStatus("current")
_Ieee8021SpbmBsiStaticEntry_Object = MibTableRow
ieee8021SpbmBsiStaticEntry = _Ieee8021SpbmBsiStaticEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 13, 1)
)
ieee8021SpbmBsiStaticEntry.setIndexNames(
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbTopIx"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbmBsiStaticEntryIsid"),
    (0, "IEEE8021-SPB-MIB", "ieee8021SpbmBsiStaticEntryBaseVid"),
)
if mibBuilder.loadTexts:
    ieee8021SpbmBsiStaticEntry.setStatus("current")
_Ieee8021SpbmBsiStaticEntryIsid_Type = IEEE8021PbbServiceIdentifier
_Ieee8021SpbmBsiStaticEntryIsid_Object = MibTableColumn
ieee8021SpbmBsiStaticEntryIsid = _Ieee8021SpbmBsiStaticEntryIsid_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 13, 1, 1),
    _Ieee8021SpbmBsiStaticEntryIsid_Type()
)
ieee8021SpbmBsiStaticEntryIsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbmBsiStaticEntryIsid.setStatus("current")
_Ieee8021SpbmBsiStaticEntryBaseVid_Type = VlanId
_Ieee8021SpbmBsiStaticEntryBaseVid_Object = MibTableColumn
ieee8021SpbmBsiStaticEntryBaseVid = _Ieee8021SpbmBsiStaticEntryBaseVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 13, 1, 2),
    _Ieee8021SpbmBsiStaticEntryBaseVid_Type()
)
ieee8021SpbmBsiStaticEntryBaseVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpbmBsiStaticEntryBaseVid.setStatus("current")
_Ieee8021SpbmBsiStaticEntryTBit_Type = TruthValue
_Ieee8021SpbmBsiStaticEntryTBit_Object = MibTableColumn
ieee8021SpbmBsiStaticEntryTBit = _Ieee8021SpbmBsiStaticEntryTBit_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 13, 1, 3),
    _Ieee8021SpbmBsiStaticEntryTBit_Type()
)
ieee8021SpbmBsiStaticEntryTBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021SpbmBsiStaticEntryTBit.setStatus("current")
_Ieee8021SpbmBsiStaticEntryRBit_Type = TruthValue
_Ieee8021SpbmBsiStaticEntryRBit_Object = MibTableColumn
ieee8021SpbmBsiStaticEntryRBit = _Ieee8021SpbmBsiStaticEntryRBit_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 13, 1, 4),
    _Ieee8021SpbmBsiStaticEntryRBit_Type()
)
ieee8021SpbmBsiStaticEntryRBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021SpbmBsiStaticEntryRBit.setStatus("current")
_Ieee8021SpbmBsiStaticEntryTsBit_Type = TruthValue
_Ieee8021SpbmBsiStaticEntryTsBit_Object = MibTableColumn
ieee8021SpbmBsiStaticEntryTsBit = _Ieee8021SpbmBsiStaticEntryTsBit_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 13, 1, 5),
    _Ieee8021SpbmBsiStaticEntryTsBit_Type()
)
ieee8021SpbmBsiStaticEntryTsBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021SpbmBsiStaticEntryTsBit.setStatus("current")


class _Ieee8021SpbmBsiStaticEntryTieBreakMask_Type(Integer32):
    """Custom type ieee8021SpbmBsiStaticEntryTieBreakMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Ieee8021SpbmBsiStaticEntryTieBreakMask_Type.__name__ = "Integer32"
_Ieee8021SpbmBsiStaticEntryTieBreakMask_Object = MibTableColumn
ieee8021SpbmBsiStaticEntryTieBreakMask = _Ieee8021SpbmBsiStaticEntryTieBreakMask_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 13, 1, 6),
    _Ieee8021SpbmBsiStaticEntryTieBreakMask_Type()
)
ieee8021SpbmBsiStaticEntryTieBreakMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021SpbmBsiStaticEntryTieBreakMask.setStatus("current")
_Ieee8021SpbmBsiStaticEntryRowStatus_Type = RowStatus
_Ieee8021SpbmBsiStaticEntryRowStatus_Object = MibTableColumn
ieee8021SpbmBsiStaticEntryRowStatus = _Ieee8021SpbmBsiStaticEntryRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 13, 1, 7),
    _Ieee8021SpbmBsiStaticEntryRowStatus_Type()
)
ieee8021SpbmBsiStaticEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021SpbmBsiStaticEntryRowStatus.setStatus("current")
_Dot1agCfmMepSpbmTable_Object = MibTable
dot1agCfmMepSpbmTable = _Dot1agCfmMepSpbmTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 14)
)
if mibBuilder.loadTexts:
    dot1agCfmMepSpbmTable.setStatus("current")
_Dot1agCfmMepSpbmEntry_Object = MibTableRow
dot1agCfmMepSpbmEntry = _Dot1agCfmMepSpbmEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 14, 1)
)
if mibBuilder.loadTexts:
    dot1agCfmMepSpbmEntry.setStatus("current")
_Dot1agCfmMepTransmitLbmSpbmDA_Type = MacAddress
_Dot1agCfmMepTransmitLbmSpbmDA_Object = MibTableColumn
dot1agCfmMepTransmitLbmSpbmDA = _Dot1agCfmMepTransmitLbmSpbmDA_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 14, 1, 1),
    _Dot1agCfmMepTransmitLbmSpbmDA_Type()
)
dot1agCfmMepTransmitLbmSpbmDA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLbmSpbmDA.setStatus("current")
_Dot1agCfmMepTransmitLtmSpbmDA_Type = MacAddress
_Dot1agCfmMepTransmitLtmSpbmDA_Object = MibTableColumn
dot1agCfmMepTransmitLtmSpbmDA = _Dot1agCfmMepTransmitLtmSpbmDA_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 14, 1, 2),
    _Dot1agCfmMepTransmitLtmSpbmDA_Type()
)
dot1agCfmMepTransmitLtmSpbmDA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepTransmitLtmSpbmDA.setStatus("current")
_Dot1agCfmMepSpbmEspTable_Object = MibTable
dot1agCfmMepSpbmEspTable = _Dot1agCfmMepSpbmEspTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 15)
)
if mibBuilder.loadTexts:
    dot1agCfmMepSpbmEspTable.setStatus("current")
_Dot1agCfmMepSpbmEspEntry_Object = MibTableRow
dot1agCfmMepSpbmEspEntry = _Dot1agCfmMepSpbmEspEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 15, 1)
)
dot1agCfmMepSpbmEspEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-SPB-MIB", "dot1agCfmMepSpbmEspIndex"),
)
if mibBuilder.loadTexts:
    dot1agCfmMepSpbmEspEntry.setStatus("current")


class _Dot1agCfmMepSpbmEspIndex_Type(Unsigned32):
    """Custom type dot1agCfmMepSpbmEspIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot1agCfmMepSpbmEspIndex_Type.__name__ = "Unsigned32"
_Dot1agCfmMepSpbmEspIndex_Object = MibTableColumn
dot1agCfmMepSpbmEspIndex = _Dot1agCfmMepSpbmEspIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 15, 1, 1),
    _Dot1agCfmMepSpbmEspIndex_Type()
)
dot1agCfmMepSpbmEspIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1agCfmMepSpbmEspIndex.setStatus("current")
_Dot1agCfmMepSpbmEspEsp_Type = IEEE8021PbbTeEsp
_Dot1agCfmMepSpbmEspEsp_Object = MibTableColumn
dot1agCfmMepSpbmEspEsp = _Dot1agCfmMepSpbmEspEsp_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 15, 1, 2),
    _Dot1agCfmMepSpbmEspEsp_Type()
)
dot1agCfmMepSpbmEspEsp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepSpbmEspEsp.setStatus("current")
_Dot1agCfmMepSpbmEspRowStatus_Type = RowStatus
_Dot1agCfmMepSpbmEspRowStatus_Object = MibTableColumn
dot1agCfmMepSpbmEspRowStatus = _Dot1agCfmMepSpbmEspRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 1, 15, 1, 3),
    _Dot1agCfmMepSpbmEspRowStatus_Type()
)
dot1agCfmMepSpbmEspRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agCfmMepSpbmEspRowStatus.setStatus("current")
_Ieee8021SpbConformance_ObjectIdentity = ObjectIdentity
ieee8021SpbConformance = _Ieee8021SpbConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 26, 2)
)
_Ieee8021SpbGroups_ObjectIdentity = ObjectIdentity
ieee8021SpbGroups = _Ieee8021SpbGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 1)
)
_Ieee8021SpbCompliances_ObjectIdentity = ObjectIdentity
ieee8021SpbCompliances = _Ieee8021SpbCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 2)
)
_Ieee8021PcrObjects_ObjectIdentity = ObjectIdentity
ieee8021PcrObjects = _Ieee8021PcrObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 26, 3)
)
_Ieee8021PcrEctStaticTable_Object = MibTable
ieee8021PcrEctStaticTable = _Ieee8021PcrEctStaticTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 3, 1)
)
if mibBuilder.loadTexts:
    ieee8021PcrEctStaticTable.setStatus("current")
_Ieee8021PcrEctStaticTableEntry_Object = MibTableRow
ieee8021PcrEctStaticTableEntry = _Ieee8021PcrEctStaticTableEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 3, 1, 1)
)
ieee8021PcrEctStaticTableEntry.setIndexNames(
    (0, "IEEE8021-SPB-MIB", "ieee8021PcrEctStaticEntryTopIx"),
    (0, "IEEE8021-SPB-MIB", "ieee8021PcrEctStaticEntryBaseVid"),
)
if mibBuilder.loadTexts:
    ieee8021PcrEctStaticTableEntry.setStatus("current")
_Ieee8021PcrEctStaticEntryTopIx_Type = IEEE8021SpbMTID
_Ieee8021PcrEctStaticEntryTopIx_Object = MibTableColumn
ieee8021PcrEctStaticEntryTopIx = _Ieee8021PcrEctStaticEntryTopIx_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 3, 1, 1, 1),
    _Ieee8021PcrEctStaticEntryTopIx_Type()
)
ieee8021PcrEctStaticEntryTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PcrEctStaticEntryTopIx.setStatus("current")
_Ieee8021PcrEctStaticEntryBaseVid_Type = VlanIdOrAny
_Ieee8021PcrEctStaticEntryBaseVid_Object = MibTableColumn
ieee8021PcrEctStaticEntryBaseVid = _Ieee8021PcrEctStaticEntryBaseVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 3, 1, 1, 2),
    _Ieee8021PcrEctStaticEntryBaseVid_Type()
)
ieee8021PcrEctStaticEntryBaseVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PcrEctStaticEntryBaseVid.setStatus("current")
_Ieee8021PcrEctStaticEntryMrtBlueVid_Type = VlanIdOrNone
_Ieee8021PcrEctStaticEntryMrtBlueVid_Object = MibTableColumn
ieee8021PcrEctStaticEntryMrtBlueVid = _Ieee8021PcrEctStaticEntryMrtBlueVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 3, 1, 1, 3),
    _Ieee8021PcrEctStaticEntryMrtBlueVid_Type()
)
ieee8021PcrEctStaticEntryMrtBlueVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PcrEctStaticEntryMrtBlueVid.setStatus("current")
_Ieee8021PcrEctStaticEntryMrtRedVid_Type = VlanIdOrNone
_Ieee8021PcrEctStaticEntryMrtRedVid_Object = MibTableColumn
ieee8021PcrEctStaticEntryMrtRedVid = _Ieee8021PcrEctStaticEntryMrtRedVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 3, 1, 1, 4),
    _Ieee8021PcrEctStaticEntryMrtRedVid_Type()
)
ieee8021PcrEctStaticEntryMrtRedVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PcrEctStaticEntryMrtRedVid.setStatus("current")
_Ieee8021PcrEctStaticEntryRowStatus_Type = RowStatus
_Ieee8021PcrEctStaticEntryRowStatus_Object = MibTableColumn
ieee8021PcrEctStaticEntryRowStatus = _Ieee8021PcrEctStaticEntryRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 3, 1, 1, 5),
    _Ieee8021PcrEctStaticEntryRowStatus_Type()
)
ieee8021PcrEctStaticEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PcrEctStaticEntryRowStatus.setStatus("current")
_Ieee8021PcrTopEctTable_Object = MibTable
ieee8021PcrTopEctTable = _Ieee8021PcrTopEctTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 3, 2)
)
if mibBuilder.loadTexts:
    ieee8021PcrTopEctTable.setStatus("current")
_Ieee8021PcrTopEctTableEntry_Object = MibTableRow
ieee8021PcrTopEctTableEntry = _Ieee8021PcrTopEctTableEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 3, 2, 1)
)
ieee8021PcrTopEctTableEntry.setIndexNames(
    (0, "IEEE8021-SPB-MIB", "ieee8021PcrTopEctEntryTopIx"),
    (0, "IEEE8021-SPB-MIB", "ieee8021PcrTopEctEntrySysId"),
    (0, "IEEE8021-SPB-MIB", "ieee8021PcrTopEctEntryBaseVid"),
)
if mibBuilder.loadTexts:
    ieee8021PcrTopEctTableEntry.setStatus("current")
_Ieee8021PcrTopEctEntryTopIx_Type = IEEE8021SpbMTID
_Ieee8021PcrTopEctEntryTopIx_Object = MibTableColumn
ieee8021PcrTopEctEntryTopIx = _Ieee8021PcrTopEctEntryTopIx_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 3, 2, 1, 1),
    _Ieee8021PcrTopEctEntryTopIx_Type()
)
ieee8021PcrTopEctEntryTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PcrTopEctEntryTopIx.setStatus("current")
_Ieee8021PcrTopEctEntrySysId_Type = MacAddress
_Ieee8021PcrTopEctEntrySysId_Object = MibTableColumn
ieee8021PcrTopEctEntrySysId = _Ieee8021PcrTopEctEntrySysId_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 3, 2, 1, 2),
    _Ieee8021PcrTopEctEntrySysId_Type()
)
ieee8021PcrTopEctEntrySysId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PcrTopEctEntrySysId.setStatus("current")
_Ieee8021PcrTopEctEntryBaseVid_Type = VlanIdOrAny
_Ieee8021PcrTopEctEntryBaseVid_Object = MibTableColumn
ieee8021PcrTopEctEntryBaseVid = _Ieee8021PcrTopEctEntryBaseVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 3, 2, 1, 3),
    _Ieee8021PcrTopEctEntryBaseVid_Type()
)
ieee8021PcrTopEctEntryBaseVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PcrTopEctEntryBaseVid.setStatus("current")
_Ieee8021PcrTopEctEntryMode_Type = IEEE8021SpbEctMode
_Ieee8021PcrTopEctEntryMode_Object = MibTableColumn
ieee8021PcrTopEctEntryMode = _Ieee8021PcrTopEctEntryMode_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 3, 2, 1, 4),
    _Ieee8021PcrTopEctEntryMode_Type()
)
ieee8021PcrTopEctEntryMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PcrTopEctEntryMode.setStatus("current")
_Ieee8021PcrTopEctEntryMrtBlueVid_Type = VlanIdOrNone
_Ieee8021PcrTopEctEntryMrtBlueVid_Object = MibTableColumn
ieee8021PcrTopEctEntryMrtBlueVid = _Ieee8021PcrTopEctEntryMrtBlueVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 3, 2, 1, 5),
    _Ieee8021PcrTopEctEntryMrtBlueVid_Type()
)
ieee8021PcrTopEctEntryMrtBlueVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PcrTopEctEntryMrtBlueVid.setStatus("current")
_Ieee8021PcrTopEctEntryMrtRedVid_Type = VlanIdOrNone
_Ieee8021PcrTopEctEntryMrtRedVid_Object = MibTableColumn
ieee8021PcrTopEctEntryMrtRedVid = _Ieee8021PcrTopEctEntryMrtRedVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 26, 3, 2, 1, 6),
    _Ieee8021PcrTopEctEntryMrtRedVid_Type()
)
ieee8021PcrTopEctEntryMrtRedVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PcrTopEctEntryMrtRedVid.setStatus("current")
_Ieee8021PcrConformance_ObjectIdentity = ObjectIdentity
ieee8021PcrConformance = _Ieee8021PcrConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 26, 4)
)
_Ieee8021PcrGroups_ObjectIdentity = ObjectIdentity
ieee8021PcrGroups = _Ieee8021PcrGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 26, 4, 1)
)
_Ieee8021PcrCompliances_ObjectIdentity = ObjectIdentity
ieee8021PcrCompliances = _Ieee8021PcrCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 26, 4, 2)
)
dot1agCfmMepEntry.registerAugmentions(
    ("IEEE8021-SPB-MIB",
     "dot1agCfmMepSpbmEntry")
)
dot1agCfmMepSpbmEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())

# Managed Objects groups

ieee8021SpbSysGroupSPBM = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 1)
)
ieee8021SpbSysGroupSPBM.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbSysAreaAddress"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbSysId"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbSysControlAddr"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbSysName"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbSysBridgePriority"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbmSysSPSourceId"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbmSysMode"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbSysDigestConvention"))
)
if mibBuilder.loadTexts:
    ieee8021SpbSysGroupSPBM.setStatus("current")

ieee8021SpbMtidStaticTableGroupSPBM = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 2)
)
ieee8021SpbMtidStaticTableGroupSPBM.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbMTidStaticEntryMtidOverload"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbMtidStaticEntryRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021SpbMtidStaticTableGroupSPBM.setStatus("current")

ieee8021SpbTopIxDynamicTableGroupSPBM = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 3)
)
ieee8021SpbTopIxDynamicTableGroupSPBM.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbTopIxDynamicEntryAgreeDigest"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbTopIxDynamicEntryMCID"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbTopIxDynamicEntryAuxMCID"))
)
if mibBuilder.loadTexts:
    ieee8021SpbTopIxDynamicTableGroupSPBM.setStatus("current")

ieee8021SpbEctStaticTableGroupSPBM = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 4)
)
ieee8021SpbEctStaticTableGroupSPBM.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbEctStaticEntryEctAlgorithm"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbEctStaticEntryRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021SpbEctStaticTableGroupSPBM.setStatus("current")

ieee8021SpbEctDynamicTableGroupSPBM = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 5)
)
ieee8021SpbEctDynamicTableGroupSPBM.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicEntryMode"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicEntryLocalUse"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicEntryRemoteUse"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicEntryIngressCheckDiscards"))
)
if mibBuilder.loadTexts:
    ieee8021SpbEctDynamicTableGroupSPBM.setStatus("current")

ieee8021SpbAdjStaticTableGroupSPBM = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 6)
)
ieee8021SpbAdjStaticTableGroupSPBM.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbAdjStaticEntryMetric"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjStaticEntryIfAdminState"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjStaticEntryRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021SpbAdjStaticTableGroupSPBM.setStatus("current")

ieee8021SpbAdjDynamicTableGroupSPBM = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 7)
)
ieee8021SpbAdjDynamicTableGroupSPBM.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPort"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryIfOperState"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerSysName"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerAgreeDigest"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerMCID"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerAuxMCID"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryLocalCircuitID"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerLocalCircuitID"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPortIdentifier"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerPortIdentifier"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryIsisCircIndex"))
)
if mibBuilder.loadTexts:
    ieee8021SpbAdjDynamicTableGroupSPBM.setStatus("current")

ieee8021SpbTopNodeTableGroupSPBM = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 8)
)
ieee8021SpbTopNodeTableGroupSPBM.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbTopNodeEntryBridgePriority"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbmTopNodeEntrySPsourceID"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbTopNodeEntrySysName"))
)
if mibBuilder.loadTexts:
    ieee8021SpbTopNodeTableGroupSPBM.setStatus("current")

ieee8021SpbTopEctTableGroupSPBM = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 9)
)
ieee8021SpbTopEctTableGroupSPBM.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbTopEctEntryEctAlgorithm"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbTopEctEntryMode"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbTopEctEntryLocalUse"))
)
if mibBuilder.loadTexts:
    ieee8021SpbTopEctTableGroupSPBM.setStatus("current")

ieee8021SpbTopEdgeTableGroupSPBM = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 10)
)
ieee8021SpbTopEdgeTableGroupSPBM.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbTopEdgeEntryMetricNear2Far"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbTopEdgeEntryMetricFar2Near"))
)
if mibBuilder.loadTexts:
    ieee8021SpbTopEdgeTableGroupSPBM.setStatus("current")

ieee8021SpbmTopSrvTableGroupSPBM = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 11)
)
ieee8021SpbmTopSrvTableGroupSPBM.setObjects(
    ("IEEE8021-SPB-MIB", "ieee8021SpbmTopSrvEntryIsidFlags")
)
if mibBuilder.loadTexts:
    ieee8021SpbmTopSrvTableGroupSPBM.setStatus("current")

ieee8021SpbSysGroupSPBV = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 12)
)
ieee8021SpbSysGroupSPBV.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbSysAreaAddress"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbSysId"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbSysControlAddr"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbSysName"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbSysBridgePriority"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbvSysMode"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbSysDigestConvention"))
)
if mibBuilder.loadTexts:
    ieee8021SpbSysGroupSPBV.setStatus("current")

ieee8021SpbMtidStaticTableGroupSPBV = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 13)
)
ieee8021SpbMtidStaticTableGroupSPBV.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbMTidStaticEntryMtidOverload"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbMtidStaticEntryRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021SpbMtidStaticTableGroupSPBV.setStatus("current")

ieee8021SpbTopIxDynamicTableGroupSPBV = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 14)
)
ieee8021SpbTopIxDynamicTableGroupSPBV.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbTopIxDynamicEntryAgreeDigest"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbTopIxDynamicEntryMCID"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbTopIxDynamicEntryAuxMCID"))
)
if mibBuilder.loadTexts:
    ieee8021SpbTopIxDynamicTableGroupSPBV.setStatus("current")

ieee8021SpbEctStaticTableGroupSPBV = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 15)
)
ieee8021SpbEctStaticTableGroupSPBV.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbEctStaticEntryEctAlgorithm"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbvEctStaticEntrySpvid"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbEctStaticEntryRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021SpbEctStaticTableGroupSPBV.setStatus("current")

ieee8021SpbEctDynamicTableGroupSPBV = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 16)
)
ieee8021SpbEctDynamicTableGroupSPBV.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicEntryMode"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicEntryLocalUse"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicEntryRemoteUse"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicEntryIngressCheckDiscards"))
)
if mibBuilder.loadTexts:
    ieee8021SpbEctDynamicTableGroupSPBV.setStatus("current")

ieee8021SpbAdjStaticTableGroupSPBV = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 17)
)
ieee8021SpbAdjStaticTableGroupSPBV.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbAdjStaticEntryMetric"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjStaticEntryIfAdminState"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjStaticEntryRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021SpbAdjStaticTableGroupSPBV.setStatus("current")

ieee8021SpbAdjDynamicTableGroupSPBV = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 18)
)
ieee8021SpbAdjDynamicTableGroupSPBV.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPort"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryIfOperState"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerSysName"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerAgreeDigest"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerMCID"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerAuxMCID"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryLocalCircuitID"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerLocalCircuitID"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPortIdentifier"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerPortIdentifier"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryIsisCircIndex"))
)
if mibBuilder.loadTexts:
    ieee8021SpbAdjDynamicTableGroupSPBV.setStatus("current")

ieee8021SpbTopNodeTableGroupSPBV = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 19)
)
ieee8021SpbTopNodeTableGroupSPBV.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbTopNodeEntryBridgePriority"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbTopNodeEntrySysName"))
)
if mibBuilder.loadTexts:
    ieee8021SpbTopNodeTableGroupSPBV.setStatus("current")

ieee8021SpbTopEctTableGroupSPBV = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 20)
)
ieee8021SpbTopEctTableGroupSPBV.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbTopEctEntryEctAlgorithm"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbTopEctEntryMode"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbvTopEctSysMode"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbvTopEctEntrySpvid"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbTopEctEntryLocalUse"))
)
if mibBuilder.loadTexts:
    ieee8021SpbTopEctTableGroupSPBV.setStatus("current")

ieee8021SpbTopEdgeTableGroupSPBV = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 21)
)
ieee8021SpbTopEdgeTableGroupSPBV.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbTopEdgeEntryMetricNear2Far"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbTopEdgeEntryMetricFar2Near"))
)
if mibBuilder.loadTexts:
    ieee8021SpbTopEdgeTableGroupSPBV.setStatus("current")

ieee8021SpbvTopSrvTableGroupSPBV = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 22)
)
ieee8021SpbvTopSrvTableGroupSPBV.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbvTopSrvEntryBaseVid"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbvTopSrvEntryMMacFlags"))
)
if mibBuilder.loadTexts:
    ieee8021SpbvTopSrvTableGroupSPBV.setStatus("current")

ieee8021SpbmBsiStaticTableGroupSPBM = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 23)
)
ieee8021SpbmBsiStaticTableGroupSPBM.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbmBsiStaticEntryTBit"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbmBsiStaticEntryRBit"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbmBsiStaticEntryTsBit"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbmBsiStaticEntryTieBreakMask"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbmBsiStaticEntryRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021SpbmBsiStaticTableGroupSPBM.setStatus("current")

dot1agCfmMepSpbmTableGroupSPBM = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 24)
)
dot1agCfmMepSpbmTableGroupSPBM.setObjects(
      *(("IEEE8021-SPB-MIB", "dot1agCfmMepTransmitLbmSpbmDA"),
        ("IEEE8021-SPB-MIB", "dot1agCfmMepTransmitLtmSpbmDA"))
)
if mibBuilder.loadTexts:
    dot1agCfmMepSpbmTableGroupSPBM.setStatus("current")

dot1agCfmMepSpbmEspTableGroupSPBM = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 25)
)
dot1agCfmMepSpbmEspTableGroupSPBM.setObjects(
      *(("IEEE8021-SPB-MIB", "dot1agCfmMepSpbmEspEsp"),
        ("IEEE8021-SPB-MIB", "dot1agCfmMepSpbmEspRowStatus"))
)
if mibBuilder.loadTexts:
    dot1agCfmMepSpbmEspTableGroupSPBM.setStatus("current")

ieee8021PcrSysGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 4, 1, 1)
)
ieee8021PcrSysGroup.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbSysAreaAddress"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbSysId"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbSysControlAddr"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbSysName"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbSysBridgePriority"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbmSysSPSourceId"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbmSysMode"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbvSysMode"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbSysDigestConvention"))
)
if mibBuilder.loadTexts:
    ieee8021PcrSysGroup.setStatus("current")

ieee8021PcrMtidStaticTableGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 4, 1, 2)
)
ieee8021PcrMtidStaticTableGroup.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbMTidStaticEntryMtidOverload"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbMtidStaticEntryRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021PcrMtidStaticTableGroup.setStatus("current")

ieee8021PcrTopIxDynamicTableGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 4, 1, 3)
)
ieee8021PcrTopIxDynamicTableGroup.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbTopIxDynamicEntryAgreeDigest"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbTopIxDynamicEntryMCID"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbTopIxDynamicEntryAuxMCID"))
)
if mibBuilder.loadTexts:
    ieee8021PcrTopIxDynamicTableGroup.setStatus("current")

ieee8021PcrEctStaticTableGroupMAC = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 4, 1, 4)
)
ieee8021PcrEctStaticTableGroupMAC.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbEctStaticEntryEctAlgorithm"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbEctStaticEntryRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021PcrEctStaticTableGroupMAC.setStatus("current")

ieee8021PcrEctStaticTableGroupVID = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 4, 1, 5)
)
ieee8021PcrEctStaticTableGroupVID.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbEctStaticEntryEctAlgorithm"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbvEctStaticEntrySpvid"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbEctStaticEntryRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021PcrEctStaticTableGroupVID.setStatus("current")

ieee8021PcrEctStaticTableGroupMrt = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 4, 1, 6)
)
ieee8021PcrEctStaticTableGroupMrt.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021PcrEctStaticEntryMrtBlueVid"),
        ("IEEE8021-SPB-MIB", "ieee8021PcrEctStaticEntryMrtRedVid"),
        ("IEEE8021-SPB-MIB", "ieee8021PcrEctStaticEntryRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021PcrEctStaticTableGroupMrt.setStatus("current")

ieee8021PcrEctDynamicTableGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 4, 1, 7)
)
ieee8021PcrEctDynamicTableGroup.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicEntryMode"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicEntryLocalUse"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicEntryRemoteUse"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicEntryIngressCheckDiscards"))
)
if mibBuilder.loadTexts:
    ieee8021PcrEctDynamicTableGroup.setStatus("current")

ieee8021PcrAdjStaticTableGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 4, 1, 8)
)
ieee8021PcrAdjStaticTableGroup.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbAdjStaticEntryMetric"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjStaticEntryIfAdminState"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjStaticEntryRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021PcrAdjStaticTableGroup.setStatus("current")

ieee8021PcrAdjDynamicTableGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 4, 1, 9)
)
ieee8021PcrAdjDynamicTableGroup.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPort"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryIfOperState"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerSysName"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerAgreeDigest"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerMCID"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerAuxMCID"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryLocalCircuitID"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerLocalCircuitID"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPortIdentifier"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerPortIdentifier"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryIsisCircIndex"))
)
if mibBuilder.loadTexts:
    ieee8021PcrAdjDynamicTableGroup.setStatus("current")

ieee8021PcrTopNodeTableGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 4, 1, 10)
)
ieee8021PcrTopNodeTableGroup.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbTopNodeEntryBridgePriority"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbmTopNodeEntrySPsourceID"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbTopNodeEntrySysName"))
)
if mibBuilder.loadTexts:
    ieee8021PcrTopNodeTableGroup.setStatus("current")

ieee8021PcrTopEctTableGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 4, 1, 11)
)
ieee8021PcrTopEctTableGroup.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021PcrTopEctEntryMode"),
        ("IEEE8021-SPB-MIB", "ieee8021PcrTopEctEntryMrtBlueVid"),
        ("IEEE8021-SPB-MIB", "ieee8021PcrTopEctEntryMrtRedVid"))
)
if mibBuilder.loadTexts:
    ieee8021PcrTopEctTableGroup.setStatus("current")

ieee8021PcrTopEdgeTableGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 4, 1, 12)
)
ieee8021PcrTopEdgeTableGroup.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbTopEdgeEntryMetricNear2Far"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbTopEdgeEntryMetricFar2Near"))
)
if mibBuilder.loadTexts:
    ieee8021PcrTopEdgeTableGroup.setStatus("current")

ieee8021PcrTopSrvTableGroupVid = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 26, 4, 1, 13)
)
ieee8021PcrTopSrvTableGroupVid.setObjects(
      *(("IEEE8021-SPB-MIB", "ieee8021SpbvTopSrvEntryBaseVid"),
        ("IEEE8021-SPB-MIB", "ieee8021SpbvTopSrvEntryMMacFlags"))
)
if mibBuilder.loadTexts:
    ieee8021PcrTopSrvTableGroupVid.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021SpbComplianceSPBM = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ieee8021SpbComplianceSPBM.setStatus(
        "current"
    )

ieee8021SpbComplianceSPBV = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 26, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ieee8021SpbComplianceSPBV.setStatus(
        "current"
    )

ieee8021PcrCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 26, 4, 2, 1)
)
if mibBuilder.loadTexts:
    ieee8021PcrCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-SPB-MIB",
    **{"IEEE8021SpbAreaAddress": IEEE8021SpbAreaAddress,
       "IEEE8021SpbEctAlgorithm": IEEE8021SpbEctAlgorithm,
       "IEEE8021SpbMode": IEEE8021SpbMode,
       "IEEE8021SpbEctMode": IEEE8021SpbEctMode,
       "IEEE8021SpbDigestConvention": IEEE8021SpbDigestConvention,
       "IEEE8021SpbLinkMetric": IEEE8021SpbLinkMetric,
       "IEEE8021SpbAdjState": IEEE8021SpbAdjState,
       "IEEE8021SpbmSPsourceId": IEEE8021SpbmSPsourceId,
       "IEEE8021SpbDigest": IEEE8021SpbDigest,
       "IEEE8021SpbMCID": IEEE8021SpbMCID,
       "IEEE8021SpbBridgePriority": IEEE8021SpbBridgePriority,
       "IEEE8021SpbMTID": IEEE8021SpbMTID,
       "IEEE8021SpbServiceIdentifierOrAny": IEEE8021SpbServiceIdentifierOrAny,
       "ieee8021SpbMib": ieee8021SpbMib,
       "ieee8021SpbObjects": ieee8021SpbObjects,
       "ieee8021SpbSys": ieee8021SpbSys,
       "ieee8021SpbSysAreaAddress": ieee8021SpbSysAreaAddress,
       "ieee8021SpbSysId": ieee8021SpbSysId,
       "ieee8021SpbSysControlAddr": ieee8021SpbSysControlAddr,
       "ieee8021SpbSysName": ieee8021SpbSysName,
       "ieee8021SpbSysBridgePriority": ieee8021SpbSysBridgePriority,
       "ieee8021SpbmSysSPSourceId": ieee8021SpbmSysSPSourceId,
       "ieee8021SpbvSysMode": ieee8021SpbvSysMode,
       "ieee8021SpbmSysMode": ieee8021SpbmSysMode,
       "ieee8021SpbSysDigestConvention": ieee8021SpbSysDigestConvention,
       "ieee8021SpbMtidStaticTable": ieee8021SpbMtidStaticTable,
       "ieee8021SpbMtidStaticTableEntry": ieee8021SpbMtidStaticTableEntry,
       "ieee8021SpbMtidStaticEntryMtid": ieee8021SpbMtidStaticEntryMtid,
       "ieee8021SpbMTidStaticEntryMtidOverload": ieee8021SpbMTidStaticEntryMtidOverload,
       "ieee8021SpbMtidStaticEntryRowStatus": ieee8021SpbMtidStaticEntryRowStatus,
       "ieee8021SpbTopIx": ieee8021SpbTopIx,
       "ieee8021SpbTopIxDynamicTable": ieee8021SpbTopIxDynamicTable,
       "ieee8021SpbTopIxDynamicTableEntry": ieee8021SpbTopIxDynamicTableEntry,
       "ieee8021SpbTopIxDynamicEntryTopIx": ieee8021SpbTopIxDynamicEntryTopIx,
       "ieee8021SpbTopIxDynamicEntryAgreeDigest": ieee8021SpbTopIxDynamicEntryAgreeDigest,
       "ieee8021SpbTopIxDynamicEntryMCID": ieee8021SpbTopIxDynamicEntryMCID,
       "ieee8021SpbTopIxDynamicEntryAuxMCID": ieee8021SpbTopIxDynamicEntryAuxMCID,
       "ieee8021SpbEctStaticTable": ieee8021SpbEctStaticTable,
       "ieee8021SpbEctStaticTableEntry": ieee8021SpbEctStaticTableEntry,
       "ieee8021SpbEctStaticEntryTopIx": ieee8021SpbEctStaticEntryTopIx,
       "ieee8021SpbEctStaticEntryBaseVid": ieee8021SpbEctStaticEntryBaseVid,
       "ieee8021SpbEctStaticEntryEctAlgorithm": ieee8021SpbEctStaticEntryEctAlgorithm,
       "ieee8021SpbvEctStaticEntrySpvid": ieee8021SpbvEctStaticEntrySpvid,
       "ieee8021SpbEctStaticEntryRowStatus": ieee8021SpbEctStaticEntryRowStatus,
       "ieee8021SpbEctDynamicTable": ieee8021SpbEctDynamicTable,
       "ieee8021SpbEctDynamicTableEntry": ieee8021SpbEctDynamicTableEntry,
       "ieee8021SpbEctDynamicEntryTopIx": ieee8021SpbEctDynamicEntryTopIx,
       "ieee8021SpbEctDynamicEntryBaseVid": ieee8021SpbEctDynamicEntryBaseVid,
       "ieee8021SpbEctDynamicEntryMode": ieee8021SpbEctDynamicEntryMode,
       "ieee8021SpbEctDynamicEntryLocalUse": ieee8021SpbEctDynamicEntryLocalUse,
       "ieee8021SpbEctDynamicEntryRemoteUse": ieee8021SpbEctDynamicEntryRemoteUse,
       "ieee8021SpbEctDynamicEntryIngressCheckDiscards": ieee8021SpbEctDynamicEntryIngressCheckDiscards,
       "ieee8021SpbAdjStaticTable": ieee8021SpbAdjStaticTable,
       "ieee8021SpbAdjStaticTableEntry": ieee8021SpbAdjStaticTableEntry,
       "ieee8021SpbAdjStaticEntryTopIx": ieee8021SpbAdjStaticEntryTopIx,
       "ieee8021SpbAdjStaticEntryIfIndex": ieee8021SpbAdjStaticEntryIfIndex,
       "ieee8021SpbAdjStaticEntryMetric": ieee8021SpbAdjStaticEntryMetric,
       "ieee8021SpbAdjStaticEntryIfAdminState": ieee8021SpbAdjStaticEntryIfAdminState,
       "ieee8021SpbAdjStaticEntryRowStatus": ieee8021SpbAdjStaticEntryRowStatus,
       "ieee8021SpbAdjDynamicTable": ieee8021SpbAdjDynamicTable,
       "ieee8021SpbAdjDynamicTableEntry": ieee8021SpbAdjDynamicTableEntry,
       "ieee8021SpbAdjDynamicEntryTopIx": ieee8021SpbAdjDynamicEntryTopIx,
       "ieee8021SpbAdjDynamicEntryIfIndex": ieee8021SpbAdjDynamicEntryIfIndex,
       "ieee8021SpbAdjDynamicEntryPeerSysId": ieee8021SpbAdjDynamicEntryPeerSysId,
       "ieee8021SpbAdjDynamicEntryPort": ieee8021SpbAdjDynamicEntryPort,
       "ieee8021SpbAdjDynamicEntryIfOperState": ieee8021SpbAdjDynamicEntryIfOperState,
       "ieee8021SpbAdjDynamicEntryPeerSysName": ieee8021SpbAdjDynamicEntryPeerSysName,
       "ieee8021SpbAdjDynamicEntryPeerAgreeDigest": ieee8021SpbAdjDynamicEntryPeerAgreeDigest,
       "ieee8021SpbAdjDynamicEntryPeerMCID": ieee8021SpbAdjDynamicEntryPeerMCID,
       "ieee8021SpbAdjDynamicEntryPeerAuxMCID": ieee8021SpbAdjDynamicEntryPeerAuxMCID,
       "ieee8021SpbAdjDynamicEntryLocalCircuitID": ieee8021SpbAdjDynamicEntryLocalCircuitID,
       "ieee8021SpbAdjDynamicEntryPeerLocalCircuitID": ieee8021SpbAdjDynamicEntryPeerLocalCircuitID,
       "ieee8021SpbAdjDynamicEntryPortIdentifier": ieee8021SpbAdjDynamicEntryPortIdentifier,
       "ieee8021SpbAdjDynamicEntryPeerPortIdentifier": ieee8021SpbAdjDynamicEntryPeerPortIdentifier,
       "ieee8021SpbAdjDynamicEntryIsisCircIndex": ieee8021SpbAdjDynamicEntryIsisCircIndex,
       "ieee8021SpbTopNodeTable": ieee8021SpbTopNodeTable,
       "ieee8021SpbTopNodeTableEntry": ieee8021SpbTopNodeTableEntry,
       "ieee8021SpbTopNodeEntryTopIx": ieee8021SpbTopNodeEntryTopIx,
       "ieee8021SpbTopNodeEntrySysId": ieee8021SpbTopNodeEntrySysId,
       "ieee8021SpbTopNodeEntryBridgePriority": ieee8021SpbTopNodeEntryBridgePriority,
       "ieee8021SpbmTopNodeEntrySPsourceID": ieee8021SpbmTopNodeEntrySPsourceID,
       "ieee8021SpbTopNodeEntrySysName": ieee8021SpbTopNodeEntrySysName,
       "ieee8021SpbTopEctTable": ieee8021SpbTopEctTable,
       "ieee8021SpbTopEctTableEntry": ieee8021SpbTopEctTableEntry,
       "ieee8021SpbTopEctEntryTopIx": ieee8021SpbTopEctEntryTopIx,
       "ieee8021SpbTopEctEntrySysId": ieee8021SpbTopEctEntrySysId,
       "ieee8021SpbTopEctEntryBaseVid": ieee8021SpbTopEctEntryBaseVid,
       "ieee8021SpbTopEctEntryEctAlgorithm": ieee8021SpbTopEctEntryEctAlgorithm,
       "ieee8021SpbTopEctEntryMode": ieee8021SpbTopEctEntryMode,
       "ieee8021SpbvTopEctSysMode": ieee8021SpbvTopEctSysMode,
       "ieee8021SpbvTopEctEntrySpvid": ieee8021SpbvTopEctEntrySpvid,
       "ieee8021SpbTopEctEntryLocalUse": ieee8021SpbTopEctEntryLocalUse,
       "ieee8021SpbTopEdgeTable": ieee8021SpbTopEdgeTable,
       "ieee8021SpbTopEdgeTableEntry": ieee8021SpbTopEdgeTableEntry,
       "ieee8021SpbTopEdgeEntryTopIx": ieee8021SpbTopEdgeEntryTopIx,
       "ieee8021SpbTopEdgeEntrySysIdNear": ieee8021SpbTopEdgeEntrySysIdNear,
       "ieee8021SpbTopEdgeEntrySysIdFar": ieee8021SpbTopEdgeEntrySysIdFar,
       "ieee8021SpbTopEdgeEntryMetricNear2Far": ieee8021SpbTopEdgeEntryMetricNear2Far,
       "ieee8021SpbTopEdgeEntryMetricFar2Near": ieee8021SpbTopEdgeEntryMetricFar2Near,
       "ieee8021SpbmTopSrvTable": ieee8021SpbmTopSrvTable,
       "ieee8021SpbmTopSrvTableEntry": ieee8021SpbmTopSrvTableEntry,
       "ieee8021SpbmTopSrvEntryTopIx": ieee8021SpbmTopSrvEntryTopIx,
       "ieee8021SpbmTopSrvEntrySysId": ieee8021SpbmTopSrvEntrySysId,
       "ieee8021SpbmTopSrvEntryIsid": ieee8021SpbmTopSrvEntryIsid,
       "ieee8021SpbmTopSrvEntryBaseVid": ieee8021SpbmTopSrvEntryBaseVid,
       "ieee8021SpbmTopSrvEntryMac": ieee8021SpbmTopSrvEntryMac,
       "ieee8021SpbmTopSrvEntryIsidFlags": ieee8021SpbmTopSrvEntryIsidFlags,
       "ieee8021SpbvTopSrvTable": ieee8021SpbvTopSrvTable,
       "ieee8021SpbvTopSrvTableEntry": ieee8021SpbvTopSrvTableEntry,
       "ieee8021SpbvTopSrvEntryTopIx": ieee8021SpbvTopSrvEntryTopIx,
       "ieee8021SpbvTopSrvEntrySysId": ieee8021SpbvTopSrvEntrySysId,
       "ieee8021SpbvTopSrvEntryMMac": ieee8021SpbvTopSrvEntryMMac,
       "ieee8021SpbvTopSrvEntryBaseVid": ieee8021SpbvTopSrvEntryBaseVid,
       "ieee8021SpbvTopSrvEntryMMacFlags": ieee8021SpbvTopSrvEntryMMacFlags,
       "ieee8021SpbmBsiStaticTable": ieee8021SpbmBsiStaticTable,
       "ieee8021SpbmBsiStaticEntry": ieee8021SpbmBsiStaticEntry,
       "ieee8021SpbmBsiStaticEntryIsid": ieee8021SpbmBsiStaticEntryIsid,
       "ieee8021SpbmBsiStaticEntryBaseVid": ieee8021SpbmBsiStaticEntryBaseVid,
       "ieee8021SpbmBsiStaticEntryTBit": ieee8021SpbmBsiStaticEntryTBit,
       "ieee8021SpbmBsiStaticEntryRBit": ieee8021SpbmBsiStaticEntryRBit,
       "ieee8021SpbmBsiStaticEntryTsBit": ieee8021SpbmBsiStaticEntryTsBit,
       "ieee8021SpbmBsiStaticEntryTieBreakMask": ieee8021SpbmBsiStaticEntryTieBreakMask,
       "ieee8021SpbmBsiStaticEntryRowStatus": ieee8021SpbmBsiStaticEntryRowStatus,
       "dot1agCfmMepSpbmTable": dot1agCfmMepSpbmTable,
       "dot1agCfmMepSpbmEntry": dot1agCfmMepSpbmEntry,
       "dot1agCfmMepTransmitLbmSpbmDA": dot1agCfmMepTransmitLbmSpbmDA,
       "dot1agCfmMepTransmitLtmSpbmDA": dot1agCfmMepTransmitLtmSpbmDA,
       "dot1agCfmMepSpbmEspTable": dot1agCfmMepSpbmEspTable,
       "dot1agCfmMepSpbmEspEntry": dot1agCfmMepSpbmEspEntry,
       "dot1agCfmMepSpbmEspIndex": dot1agCfmMepSpbmEspIndex,
       "dot1agCfmMepSpbmEspEsp": dot1agCfmMepSpbmEspEsp,
       "dot1agCfmMepSpbmEspRowStatus": dot1agCfmMepSpbmEspRowStatus,
       "ieee8021SpbConformance": ieee8021SpbConformance,
       "ieee8021SpbGroups": ieee8021SpbGroups,
       "ieee8021SpbSysGroupSPBM": ieee8021SpbSysGroupSPBM,
       "ieee8021SpbMtidStaticTableGroupSPBM": ieee8021SpbMtidStaticTableGroupSPBM,
       "ieee8021SpbTopIxDynamicTableGroupSPBM": ieee8021SpbTopIxDynamicTableGroupSPBM,
       "ieee8021SpbEctStaticTableGroupSPBM": ieee8021SpbEctStaticTableGroupSPBM,
       "ieee8021SpbEctDynamicTableGroupSPBM": ieee8021SpbEctDynamicTableGroupSPBM,
       "ieee8021SpbAdjStaticTableGroupSPBM": ieee8021SpbAdjStaticTableGroupSPBM,
       "ieee8021SpbAdjDynamicTableGroupSPBM": ieee8021SpbAdjDynamicTableGroupSPBM,
       "ieee8021SpbTopNodeTableGroupSPBM": ieee8021SpbTopNodeTableGroupSPBM,
       "ieee8021SpbTopEctTableGroupSPBM": ieee8021SpbTopEctTableGroupSPBM,
       "ieee8021SpbTopEdgeTableGroupSPBM": ieee8021SpbTopEdgeTableGroupSPBM,
       "ieee8021SpbmTopSrvTableGroupSPBM": ieee8021SpbmTopSrvTableGroupSPBM,
       "ieee8021SpbSysGroupSPBV": ieee8021SpbSysGroupSPBV,
       "ieee8021SpbMtidStaticTableGroupSPBV": ieee8021SpbMtidStaticTableGroupSPBV,
       "ieee8021SpbTopIxDynamicTableGroupSPBV": ieee8021SpbTopIxDynamicTableGroupSPBV,
       "ieee8021SpbEctStaticTableGroupSPBV": ieee8021SpbEctStaticTableGroupSPBV,
       "ieee8021SpbEctDynamicTableGroupSPBV": ieee8021SpbEctDynamicTableGroupSPBV,
       "ieee8021SpbAdjStaticTableGroupSPBV": ieee8021SpbAdjStaticTableGroupSPBV,
       "ieee8021SpbAdjDynamicTableGroupSPBV": ieee8021SpbAdjDynamicTableGroupSPBV,
       "ieee8021SpbTopNodeTableGroupSPBV": ieee8021SpbTopNodeTableGroupSPBV,
       "ieee8021SpbTopEctTableGroupSPBV": ieee8021SpbTopEctTableGroupSPBV,
       "ieee8021SpbTopEdgeTableGroupSPBV": ieee8021SpbTopEdgeTableGroupSPBV,
       "ieee8021SpbvTopSrvTableGroupSPBV": ieee8021SpbvTopSrvTableGroupSPBV,
       "ieee8021SpbmBsiStaticTableGroupSPBM": ieee8021SpbmBsiStaticTableGroupSPBM,
       "dot1agCfmMepSpbmTableGroupSPBM": dot1agCfmMepSpbmTableGroupSPBM,
       "dot1agCfmMepSpbmEspTableGroupSPBM": dot1agCfmMepSpbmEspTableGroupSPBM,
       "ieee8021SpbCompliances": ieee8021SpbCompliances,
       "ieee8021SpbComplianceSPBM": ieee8021SpbComplianceSPBM,
       "ieee8021SpbComplianceSPBV": ieee8021SpbComplianceSPBV,
       "ieee8021PcrObjects": ieee8021PcrObjects,
       "ieee8021PcrEctStaticTable": ieee8021PcrEctStaticTable,
       "ieee8021PcrEctStaticTableEntry": ieee8021PcrEctStaticTableEntry,
       "ieee8021PcrEctStaticEntryTopIx": ieee8021PcrEctStaticEntryTopIx,
       "ieee8021PcrEctStaticEntryBaseVid": ieee8021PcrEctStaticEntryBaseVid,
       "ieee8021PcrEctStaticEntryMrtBlueVid": ieee8021PcrEctStaticEntryMrtBlueVid,
       "ieee8021PcrEctStaticEntryMrtRedVid": ieee8021PcrEctStaticEntryMrtRedVid,
       "ieee8021PcrEctStaticEntryRowStatus": ieee8021PcrEctStaticEntryRowStatus,
       "ieee8021PcrTopEctTable": ieee8021PcrTopEctTable,
       "ieee8021PcrTopEctTableEntry": ieee8021PcrTopEctTableEntry,
       "ieee8021PcrTopEctEntryTopIx": ieee8021PcrTopEctEntryTopIx,
       "ieee8021PcrTopEctEntrySysId": ieee8021PcrTopEctEntrySysId,
       "ieee8021PcrTopEctEntryBaseVid": ieee8021PcrTopEctEntryBaseVid,
       "ieee8021PcrTopEctEntryMode": ieee8021PcrTopEctEntryMode,
       "ieee8021PcrTopEctEntryMrtBlueVid": ieee8021PcrTopEctEntryMrtBlueVid,
       "ieee8021PcrTopEctEntryMrtRedVid": ieee8021PcrTopEctEntryMrtRedVid,
       "ieee8021PcrConformance": ieee8021PcrConformance,
       "ieee8021PcrGroups": ieee8021PcrGroups,
       "ieee8021PcrSysGroup": ieee8021PcrSysGroup,
       "ieee8021PcrMtidStaticTableGroup": ieee8021PcrMtidStaticTableGroup,
       "ieee8021PcrTopIxDynamicTableGroup": ieee8021PcrTopIxDynamicTableGroup,
       "ieee8021PcrEctStaticTableGroupMAC": ieee8021PcrEctStaticTableGroupMAC,
       "ieee8021PcrEctStaticTableGroupVID": ieee8021PcrEctStaticTableGroupVID,
       "ieee8021PcrEctStaticTableGroupMrt": ieee8021PcrEctStaticTableGroupMrt,
       "ieee8021PcrEctDynamicTableGroup": ieee8021PcrEctDynamicTableGroup,
       "ieee8021PcrAdjStaticTableGroup": ieee8021PcrAdjStaticTableGroup,
       "ieee8021PcrAdjDynamicTableGroup": ieee8021PcrAdjDynamicTableGroup,
       "ieee8021PcrTopNodeTableGroup": ieee8021PcrTopNodeTableGroup,
       "ieee8021PcrTopEctTableGroup": ieee8021PcrTopEctTableGroup,
       "ieee8021PcrTopEdgeTableGroup": ieee8021PcrTopEdgeTableGroup,
       "ieee8021PcrTopSrvTableGroupVid": ieee8021PcrTopSrvTableGroupVid,
       "ieee8021PcrCompliances": ieee8021PcrCompliances,
       "ieee8021PcrCompliance": ieee8021PcrCompliance}
)
