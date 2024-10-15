# SNMP MIB module (CISCO-FCS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FCS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:26 2024
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

(FcGs3RejectReasonCode,) = mibBuilder.importSymbols(
    "CISCO-NS-MIB",
    "FcGs3RejectReasonCode")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(DomainIdOrZero,
 FcAddressId,
 FcNameId,
 FcPortModuleTypes,
 FcPortTxTypes,
 FcPortTypes,
 VsanIndex) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "DomainIdOrZero",
    "FcAddressId",
    "FcNameId",
    "FcPortModuleTypes",
    "FcPortTxTypes",
    "FcPortTypes",
    "VsanIndex")

(ListIndex,
 ListIndexOrZero,
 TimeIntervalSec) = mibBuilder.importSymbols(
    "CISCO-TC",
    "ListIndex",
    "ListIndexOrZero",
    "TimeIntervalSec")

(vsanIndex,) = mibBuilder.importSymbols(
    "CISCO-VSAN-MIB",
    "vsanIndex")

(FcList,) = mibBuilder.importSymbols(
    "CISCO-ZS-MIB",
    "FcList")

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
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoFcsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 297)
)
ciscoFcsMIB.setRevisions(
        ("2004-02-19 00:00",
         "2003-08-20 00:00",
         "2002-12-18 00:00",
         "2002-10-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CreatedBy(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createdByMgmt", 1),
          ("learnedviaGS3", 2))
    )



class FcIeType(Integer32, TextualConvention):
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
        *(("bridge", 5),
          ("hub", 4),
          ("other", 2),
          ("switch", 3),
          ("unknown", 1))
    )



class FcPortState(Integer32, TextualConvention):
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
        *(("fault", 5),
          ("offline", 3),
          ("online", 2),
          ("other", 6),
          ("testing", 4),
          ("unknown", 1))
    )



class FcPlatformType(Integer32, TextualConvention):
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("converter", 4),
          ("gateway", 3),
          ("host", 8),
          ("hostBusAdapter", 5),
          ("module", 10),
          ("other", 2),
          ("storageAccessDev", 12),
          ("storageDevice", 7),
          ("storageSubSys", 9),
          ("swDriver", 11),
          ("swProxyAgent", 6),
          ("unknown", 1))
    )



class FcFcsRejReasonExplanation(Integer32, TextualConvention):
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("attPortNameListNotAvailable", 14),
          ("domainIdNotAvailable", 5),
          ("fabNameNotAvailable", 7),
          ("ieInfoListNotAvailable", 10),
          ("ieListNotAvailable", 3),
          ("ieTypeNotAvailable", 4),
          ("ielogNameNotAvailable", 8),
          ("invNameIdForIEOrPort", 2),
          ("mgmtAddrListNotAvailable", 9),
          ("mgmtIdNotAvailable", 6),
          ("noAdditionalExplanation", 1),
          ("phyPortNumNotAvailable", 13),
          ("platformNameAlreadyExists", 18),
          ("platformNameNoExist", 17),
          ("platformNodeNameAlreadyExists", 20),
          ("platformNodeNameNoExists", 19),
          ("portListNotAvailable", 11),
          ("portStateNotAvailable", 15),
          ("portTypeNotAvailable", 12),
          ("unableToRegIELogName", 16))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoFcsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFcsMIBObjects = _CiscoFcsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1)
)
_FcsConfiguration_ObjectIdentity = ObjectIdentity
fcsConfiguration = _FcsConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1)
)
_FcsVsanDiscoverySpinLock_Type = TestAndIncr
_FcsVsanDiscoverySpinLock_Object = MibScalar
fcsVsanDiscoverySpinLock = _FcsVsanDiscoverySpinLock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 1),
    _FcsVsanDiscoverySpinLock_Type()
)
fcsVsanDiscoverySpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcsVsanDiscoverySpinLock.setStatus("current")


class _FcsVsanDiscoveryName_Type(SnmpAdminString):
    """Custom type fcsVsanDiscoveryName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FcsVsanDiscoveryName_Type.__name__ = "SnmpAdminString"
_FcsVsanDiscoveryName_Object = MibScalar
fcsVsanDiscoveryName = _FcsVsanDiscoveryName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 2),
    _FcsVsanDiscoveryName_Type()
)
fcsVsanDiscoveryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcsVsanDiscoveryName.setStatus("current")
_FcsVsanDiscoveryList2k_Type = FcList
_FcsVsanDiscoveryList2k_Object = MibScalar
fcsVsanDiscoveryList2k = _FcsVsanDiscoveryList2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 3),
    _FcsVsanDiscoveryList2k_Type()
)
fcsVsanDiscoveryList2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcsVsanDiscoveryList2k.setStatus("current")
_FcsVsanDiscoveryList4k_Type = FcList
_FcsVsanDiscoveryList4k_Object = MibScalar
fcsVsanDiscoveryList4k = _FcsVsanDiscoveryList4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 4),
    _FcsVsanDiscoveryList4k_Type()
)
fcsVsanDiscoveryList4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcsVsanDiscoveryList4k.setStatus("current")


class _FcsStartDiscovery_Type(Integer32):
    """Custom type fcsStartDiscovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 2),
          ("startDiscovery", 1))
    )


_FcsStartDiscovery_Type.__name__ = "Integer32"
_FcsStartDiscovery_Object = MibScalar
fcsStartDiscovery = _FcsStartDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 5),
    _FcsStartDiscovery_Type()
)
fcsStartDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcsStartDiscovery.setStatus("current")
_FcsDiscoveryStatusTable_Object = MibTable
fcsDiscoveryStatusTable = _FcsDiscoveryStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 6)
)
if mibBuilder.loadTexts:
    fcsDiscoveryStatusTable.setStatus("current")
_FcsDiscoveryStatusEntry_Object = MibTableRow
fcsDiscoveryStatusEntry = _FcsDiscoveryStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 6, 1)
)
fcsDiscoveryStatusEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    fcsDiscoveryStatusEntry.setStatus("current")


class _FcsDiscoveryStatus_Type(Integer32):
    """Custom type fcsDiscoveryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("completed", 2),
          ("databaseInvalid", 3),
          ("inProgress", 1))
    )


_FcsDiscoveryStatus_Type.__name__ = "Integer32"
_FcsDiscoveryStatus_Object = MibTableColumn
fcsDiscoveryStatus = _FcsDiscoveryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 6, 1, 1),
    _FcsDiscoveryStatus_Type()
)
fcsDiscoveryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsDiscoveryStatus.setStatus("current")
_FcsDiscoveryCompleteTime_Type = TimeStamp
_FcsDiscoveryCompleteTime_Object = MibTableColumn
fcsDiscoveryCompleteTime = _FcsDiscoveryCompleteTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 6, 1, 2),
    _FcsDiscoveryCompleteTime_Type()
)
fcsDiscoveryCompleteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsDiscoveryCompleteTime.setStatus("current")


class _FcsVsanDiscoveryTimeOut_Type(TimeIntervalSec):
    """Custom type fcsVsanDiscoveryTimeOut based on TimeIntervalSec"""
    defaultValue = 900

    subtypeSpec = TimeIntervalSec.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1800),
    )


_FcsVsanDiscoveryTimeOut_Type.__name__ = "TimeIntervalSec"
_FcsVsanDiscoveryTimeOut_Object = MibScalar
fcsVsanDiscoveryTimeOut = _FcsVsanDiscoveryTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 7),
    _FcsVsanDiscoveryTimeOut_Type()
)
fcsVsanDiscoveryTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcsVsanDiscoveryTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    fcsVsanDiscoveryTimeOut.setUnits("seconds")
_FcsDiscoveryInvalidateCache2k_Type = FcList
_FcsDiscoveryInvalidateCache2k_Object = MibScalar
fcsDiscoveryInvalidateCache2k = _FcsDiscoveryInvalidateCache2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 8),
    _FcsDiscoveryInvalidateCache2k_Type()
)
fcsDiscoveryInvalidateCache2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcsDiscoveryInvalidateCache2k.setStatus("current")
_FcsDiscoveryInvalidateCache4k_Type = FcList
_FcsDiscoveryInvalidateCache4k_Object = MibScalar
fcsDiscoveryInvalidateCache4k = _FcsDiscoveryInvalidateCache4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 9),
    _FcsDiscoveryInvalidateCache4k_Type()
)
fcsDiscoveryInvalidateCache4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcsDiscoveryInvalidateCache4k.setStatus("current")


class _FcsIeNumber_Type(Integer32):
    """Custom type fcsIeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 489472),
    )


_FcsIeNumber_Type.__name__ = "Integer32"
_FcsIeNumber_Object = MibScalar
fcsIeNumber = _FcsIeNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 10),
    _FcsIeNumber_Type()
)
fcsIeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsIeNumber.setStatus("current")
_FcsIeTable_Object = MibTable
fcsIeTable = _FcsIeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 11)
)
if mibBuilder.loadTexts:
    fcsIeTable.setStatus("current")
_FcsIeEntry_Object = MibTableRow
fcsIeEntry = _FcsIeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 11, 1)
)
fcsIeEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-FCS-MIB", "fcsIeName"),
)
if mibBuilder.loadTexts:
    fcsIeEntry.setStatus("current")
_FcsIeName_Type = FcNameId
_FcsIeName_Object = MibTableColumn
fcsIeName = _FcsIeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 11, 1, 1),
    _FcsIeName_Type()
)
fcsIeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcsIeName.setStatus("current")
_FcsIeType_Type = FcIeType
_FcsIeType_Object = MibTableColumn
fcsIeType = _FcsIeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 11, 1, 2),
    _FcsIeType_Type()
)
fcsIeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsIeType.setStatus("current")
_FcsIeDomainId_Type = DomainIdOrZero
_FcsIeDomainId_Object = MibTableColumn
fcsIeDomainId = _FcsIeDomainId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 11, 1, 3),
    _FcsIeDomainId_Type()
)
fcsIeDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsIeDomainId.setStatus("current")


class _FcsIeMgmtId_Type(FcAddressId):
    """Custom type fcsIeMgmtId based on FcAddressId"""
    defaultHexValue = "000000"


_FcsIeMgmtId_Object = MibTableColumn
fcsIeMgmtId = _FcsIeMgmtId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 11, 1, 4),
    _FcsIeMgmtId_Type()
)
fcsIeMgmtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsIeMgmtId.setStatus("current")


class _FcsIeFabricName_Type(FcNameId):
    """Custom type fcsIeFabricName based on FcNameId"""
    defaultHexValue = "0000000000000000"


_FcsIeFabricName_Object = MibTableColumn
fcsIeFabricName = _FcsIeFabricName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 11, 1, 5),
    _FcsIeFabricName_Type()
)
fcsIeFabricName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsIeFabricName.setStatus("current")


class _FcsIeLogicalName_Type(OctetString):
    """Custom type fcsIeLogicalName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FcsIeLogicalName_Type.__name__ = "OctetString"
_FcsIeLogicalName_Object = MibTableColumn
fcsIeLogicalName = _FcsIeLogicalName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 11, 1, 6),
    _FcsIeLogicalName_Type()
)
fcsIeLogicalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsIeLogicalName.setStatus("current")
_FcsIeMgmtAddrListIndex_Type = ListIndexOrZero
_FcsIeMgmtAddrListIndex_Object = MibTableColumn
fcsIeMgmtAddrListIndex = _FcsIeMgmtAddrListIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 11, 1, 7),
    _FcsIeMgmtAddrListIndex_Type()
)
fcsIeMgmtAddrListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsIeMgmtAddrListIndex.setStatus("current")


class _FcsIeInfoList_Type(OctetString):
    """Custom type fcsIeInfoList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FcsIeInfoList_Type.__name__ = "OctetString"
_FcsIeInfoList_Object = MibTableColumn
fcsIeInfoList = _FcsIeInfoList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 11, 1, 8),
    _FcsIeInfoList_Type()
)
fcsIeInfoList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsIeInfoList.setStatus("current")
_FcsIePortListIndex_Type = ListIndexOrZero
_FcsIePortListIndex_Object = MibTableColumn
fcsIePortListIndex = _FcsIePortListIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 11, 1, 9),
    _FcsIePortListIndex_Type()
)
fcsIePortListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsIePortListIndex.setStatus("current")
_FcsMgmtAddrListTable_Object = MibTable
fcsMgmtAddrListTable = _FcsMgmtAddrListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 12)
)
if mibBuilder.loadTexts:
    fcsMgmtAddrListTable.setStatus("current")
_FcsMgmtAddrListEntry_Object = MibTableRow
fcsMgmtAddrListEntry = _FcsMgmtAddrListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 12, 1)
)
fcsMgmtAddrListEntry.setIndexNames(
    (0, "CISCO-FCS-MIB", "fcsMgmtAddrListIndex"),
    (0, "CISCO-FCS-MIB", "fcsMgmtAddrIndex"),
)
if mibBuilder.loadTexts:
    fcsMgmtAddrListEntry.setStatus("current")


class _FcsMgmtAddrListIndex_Type(ListIndex):
    """Custom type fcsMgmtAddrListIndex based on ListIndex"""
    subtypeSpec = ListIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FcsMgmtAddrListIndex_Type.__name__ = "ListIndex"
_FcsMgmtAddrListIndex_Object = MibTableColumn
fcsMgmtAddrListIndex = _FcsMgmtAddrListIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 12, 1, 1),
    _FcsMgmtAddrListIndex_Type()
)
fcsMgmtAddrListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcsMgmtAddrListIndex.setStatus("current")


class _FcsMgmtAddrIndex_Type(Unsigned32):
    """Custom type fcsMgmtAddrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FcsMgmtAddrIndex_Type.__name__ = "Unsigned32"
_FcsMgmtAddrIndex_Object = MibTableColumn
fcsMgmtAddrIndex = _FcsMgmtAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 12, 1, 2),
    _FcsMgmtAddrIndex_Type()
)
fcsMgmtAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcsMgmtAddrIndex.setStatus("current")


class _FcsMgmtAddr_Type(OctetString):
    """Custom type fcsMgmtAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FcsMgmtAddr_Type.__name__ = "OctetString"
_FcsMgmtAddr_Object = MibTableColumn
fcsMgmtAddr = _FcsMgmtAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 12, 1, 3),
    _FcsMgmtAddr_Type()
)
fcsMgmtAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcsMgmtAddr.setStatus("current")
_FcsMgmtAddrConfigSource_Type = CreatedBy
_FcsMgmtAddrConfigSource_Object = MibTableColumn
fcsMgmtAddrConfigSource = _FcsMgmtAddrConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 12, 1, 4),
    _FcsMgmtAddrConfigSource_Type()
)
fcsMgmtAddrConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsMgmtAddrConfigSource.setStatus("current")
_FcsMgmtAddrRowStatus_Type = RowStatus
_FcsMgmtAddrRowStatus_Object = MibTableColumn
fcsMgmtAddrRowStatus = _FcsMgmtAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 12, 1, 5),
    _FcsMgmtAddrRowStatus_Type()
)
fcsMgmtAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcsMgmtAddrRowStatus.setStatus("current")
_FcsPortListTable_Object = MibTable
fcsPortListTable = _FcsPortListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 13)
)
if mibBuilder.loadTexts:
    fcsPortListTable.setStatus("current")
_FcsPortListEntry_Object = MibTableRow
fcsPortListEntry = _FcsPortListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 13, 1)
)
fcsPortListEntry.setIndexNames(
    (0, "CISCO-FCS-MIB", "fcsPortListIndex"),
    (0, "CISCO-FCS-MIB", "fcsPortName"),
)
if mibBuilder.loadTexts:
    fcsPortListEntry.setStatus("current")


class _FcsPortListIndex_Type(ListIndex):
    """Custom type fcsPortListIndex based on ListIndex"""
    subtypeSpec = ListIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FcsPortListIndex_Type.__name__ = "ListIndex"
_FcsPortListIndex_Object = MibTableColumn
fcsPortListIndex = _FcsPortListIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 13, 1, 1),
    _FcsPortListIndex_Type()
)
fcsPortListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsPortListIndex.setStatus("current")


class _FcsPortNumber_Type(Integer32):
    """Custom type fcsPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FcsPortNumber_Type.__name__ = "Integer32"
_FcsPortNumber_Object = MibScalar
fcsPortNumber = _FcsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 14),
    _FcsPortNumber_Type()
)
fcsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsPortNumber.setStatus("current")
_FcsPortTable_Object = MibTable
fcsPortTable = _FcsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 15)
)
if mibBuilder.loadTexts:
    fcsPortTable.setStatus("current")
_FcsPortEntry_Object = MibTableRow
fcsPortEntry = _FcsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 15, 1)
)
fcsPortEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-FCS-MIB", "fcsPortName"),
)
if mibBuilder.loadTexts:
    fcsPortEntry.setStatus("current")
_FcsPortName_Type = FcNameId
_FcsPortName_Object = MibTableColumn
fcsPortName = _FcsPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 15, 1, 1),
    _FcsPortName_Type()
)
fcsPortName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcsPortName.setStatus("current")
_FcsPortType_Type = FcPortTypes
_FcsPortType_Object = MibTableColumn
fcsPortType = _FcsPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 15, 1, 2),
    _FcsPortType_Type()
)
fcsPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsPortType.setStatus("current")
_FcsPortTXType_Type = FcPortTxTypes
_FcsPortTXType_Object = MibTableColumn
fcsPortTXType = _FcsPortTXType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 15, 1, 3),
    _FcsPortTXType_Type()
)
fcsPortTXType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsPortTXType.setStatus("current")
_FcsPortModuleType_Type = FcPortModuleTypes
_FcsPortModuleType_Object = MibTableColumn
fcsPortModuleType = _FcsPortModuleType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 15, 1, 4),
    _FcsPortModuleType_Type()
)
fcsPortModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsPortModuleType.setStatus("current")


class _FcsPortPhyPortNum_Type(Integer32):
    """Custom type fcsPortPhyPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FcsPortPhyPortNum_Type.__name__ = "Integer32"
_FcsPortPhyPortNum_Object = MibTableColumn
fcsPortPhyPortNum = _FcsPortPhyPortNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 15, 1, 5),
    _FcsPortPhyPortNum_Type()
)
fcsPortPhyPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsPortPhyPortNum.setStatus("current")
_FcsPortAttachPortNameIndex_Type = ListIndexOrZero
_FcsPortAttachPortNameIndex_Object = MibTableColumn
fcsPortAttachPortNameIndex = _FcsPortAttachPortNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 15, 1, 6),
    _FcsPortAttachPortNameIndex_Type()
)
fcsPortAttachPortNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsPortAttachPortNameIndex.setStatus("current")
_FcsPortState_Type = FcPortState
_FcsPortState_Object = MibTableColumn
fcsPortState = _FcsPortState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 15, 1, 7),
    _FcsPortState_Type()
)
fcsPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsPortState.setStatus("current")
_FcsAttachPortNameListTable_Object = MibTable
fcsAttachPortNameListTable = _FcsAttachPortNameListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 16)
)
if mibBuilder.loadTexts:
    fcsAttachPortNameListTable.setStatus("current")
_FcsAttachPortNameListEntry_Object = MibTableRow
fcsAttachPortNameListEntry = _FcsAttachPortNameListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 16, 1)
)
fcsAttachPortNameListEntry.setIndexNames(
    (0, "CISCO-FCS-MIB", "fcsAttachPortNameListIndex"),
    (0, "CISCO-FCS-MIB", "fcsAttachPortName"),
)
if mibBuilder.loadTexts:
    fcsAttachPortNameListEntry.setStatus("current")


class _FcsAttachPortNameListIndex_Type(ListIndex):
    """Custom type fcsAttachPortNameListIndex based on ListIndex"""
    subtypeSpec = ListIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FcsAttachPortNameListIndex_Type.__name__ = "ListIndex"
_FcsAttachPortNameListIndex_Object = MibTableColumn
fcsAttachPortNameListIndex = _FcsAttachPortNameListIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 16, 1, 1),
    _FcsAttachPortNameListIndex_Type()
)
fcsAttachPortNameListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcsAttachPortNameListIndex.setStatus("current")


class _FcsAttachPortName_Type(OctetString):
    """Custom type fcsAttachPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_FcsAttachPortName_Type.__name__ = "OctetString"
_FcsAttachPortName_Object = MibTableColumn
fcsAttachPortName = _FcsAttachPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 16, 1, 2),
    _FcsAttachPortName_Type()
)
fcsAttachPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsAttachPortName.setStatus("current")


class _FcsPlatformNumber_Type(Integer32):
    """Custom type fcsPlatformNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FcsPlatformNumber_Type.__name__ = "Integer32"
_FcsPlatformNumber_Object = MibScalar
fcsPlatformNumber = _FcsPlatformNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 17),
    _FcsPlatformNumber_Type()
)
fcsPlatformNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsPlatformNumber.setStatus("current")
_FcsPlatformTable_Object = MibTable
fcsPlatformTable = _FcsPlatformTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 18)
)
if mibBuilder.loadTexts:
    fcsPlatformTable.setStatus("current")
_FcsPlatformEntry_Object = MibTableRow
fcsPlatformEntry = _FcsPlatformEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 18, 1)
)
fcsPlatformEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-FCS-MIB", "fcsPlatformIndex"),
)
if mibBuilder.loadTexts:
    fcsPlatformEntry.setStatus("current")


class _FcsPlatformIndex_Type(Unsigned32):
    """Custom type fcsPlatformIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FcsPlatformIndex_Type.__name__ = "Unsigned32"
_FcsPlatformIndex_Object = MibTableColumn
fcsPlatformIndex = _FcsPlatformIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 18, 1, 1),
    _FcsPlatformIndex_Type()
)
fcsPlatformIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcsPlatformIndex.setStatus("current")


class _FcsPlatformName_Type(OctetString):
    """Custom type fcsPlatformName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FcsPlatformName_Type.__name__ = "OctetString"
_FcsPlatformName_Object = MibTableColumn
fcsPlatformName = _FcsPlatformName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 18, 1, 2),
    _FcsPlatformName_Type()
)
fcsPlatformName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcsPlatformName.setStatus("current")
_FcsPlatformType_Type = FcPlatformType
_FcsPlatformType_Object = MibTableColumn
fcsPlatformType = _FcsPlatformType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 18, 1, 3),
    _FcsPlatformType_Type()
)
fcsPlatformType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcsPlatformType.setStatus("current")
_FcsPlatformNodeNameListIndex_Type = ListIndexOrZero
_FcsPlatformNodeNameListIndex_Object = MibTableColumn
fcsPlatformNodeNameListIndex = _FcsPlatformNodeNameListIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 18, 1, 4),
    _FcsPlatformNodeNameListIndex_Type()
)
fcsPlatformNodeNameListIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcsPlatformNodeNameListIndex.setStatus("current")
_FcsPlatformMgmtAddrListIndex_Type = ListIndexOrZero
_FcsPlatformMgmtAddrListIndex_Object = MibTableColumn
fcsPlatformMgmtAddrListIndex = _FcsPlatformMgmtAddrListIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 18, 1, 5),
    _FcsPlatformMgmtAddrListIndex_Type()
)
fcsPlatformMgmtAddrListIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcsPlatformMgmtAddrListIndex.setStatus("current")
_FcsPlatformConfigSource_Type = CreatedBy
_FcsPlatformConfigSource_Object = MibTableColumn
fcsPlatformConfigSource = _FcsPlatformConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 18, 1, 6),
    _FcsPlatformConfigSource_Type()
)
fcsPlatformConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsPlatformConfigSource.setStatus("current")


class _FcsPlatformValidation_Type(Integer32):
    """Custom type fcsPlatformValidation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 2),
          ("validate", 1))
    )


_FcsPlatformValidation_Type.__name__ = "Integer32"
_FcsPlatformValidation_Object = MibTableColumn
fcsPlatformValidation = _FcsPlatformValidation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 18, 1, 7),
    _FcsPlatformValidation_Type()
)
fcsPlatformValidation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcsPlatformValidation.setStatus("current")


class _FcsPlatformValidationResult_Type(Integer32):
    """Custom type fcsPlatformValidationResult based on Integer32"""
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
        *(("failure", 5),
          ("inProgress", 2),
          ("nameInvalid", 3),
          ("nodeInvalid", 4),
          ("success", 1))
    )


_FcsPlatformValidationResult_Type.__name__ = "Integer32"
_FcsPlatformValidationResult_Object = MibTableColumn
fcsPlatformValidationResult = _FcsPlatformValidationResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 18, 1, 8),
    _FcsPlatformValidationResult_Type()
)
fcsPlatformValidationResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsPlatformValidationResult.setStatus("current")
_FcsPlatformRowStatus_Type = RowStatus
_FcsPlatformRowStatus_Object = MibTableColumn
fcsPlatformRowStatus = _FcsPlatformRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 18, 1, 9),
    _FcsPlatformRowStatus_Type()
)
fcsPlatformRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcsPlatformRowStatus.setStatus("current")
_FcsNodeNameListTable_Object = MibTable
fcsNodeNameListTable = _FcsNodeNameListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 19)
)
if mibBuilder.loadTexts:
    fcsNodeNameListTable.setStatus("current")
_FcsNodeNameListEntry_Object = MibTableRow
fcsNodeNameListEntry = _FcsNodeNameListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 19, 1)
)
fcsNodeNameListEntry.setIndexNames(
    (0, "CISCO-FCS-MIB", "fcsNodeNameListIndex"),
    (0, "CISCO-FCS-MIB", "fcsNodeName"),
)
if mibBuilder.loadTexts:
    fcsNodeNameListEntry.setStatus("current")


class _FcsNodeNameListIndex_Type(ListIndex):
    """Custom type fcsNodeNameListIndex based on ListIndex"""
    subtypeSpec = ListIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FcsNodeNameListIndex_Type.__name__ = "ListIndex"
_FcsNodeNameListIndex_Object = MibTableColumn
fcsNodeNameListIndex = _FcsNodeNameListIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 19, 1, 1),
    _FcsNodeNameListIndex_Type()
)
fcsNodeNameListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcsNodeNameListIndex.setStatus("current")
_FcsNodeName_Type = FcNameId
_FcsNodeName_Object = MibTableColumn
fcsNodeName = _FcsNodeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 19, 1, 2),
    _FcsNodeName_Type()
)
fcsNodeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcsNodeName.setStatus("current")
_FcsNodeNameConfigSource_Type = CreatedBy
_FcsNodeNameConfigSource_Object = MibTableColumn
fcsNodeNameConfigSource = _FcsNodeNameConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 19, 1, 3),
    _FcsNodeNameConfigSource_Type()
)
fcsNodeNameConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsNodeNameConfigSource.setStatus("current")
_FcsNodeNameRowStatus_Type = RowStatus
_FcsNodeNameRowStatus_Object = MibTableColumn
fcsNodeNameRowStatus = _FcsNodeNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 19, 1, 4),
    _FcsNodeNameRowStatus_Type()
)
fcsNodeNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcsNodeNameRowStatus.setStatus("current")


class _FcsReqRejNotifyEnable_Type(TruthValue):
    """Custom type fcsReqRejNotifyEnable based on TruthValue"""


_FcsReqRejNotifyEnable_Object = MibScalar
fcsReqRejNotifyEnable = _FcsReqRejNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 20),
    _FcsReqRejNotifyEnable_Type()
)
fcsReqRejNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcsReqRejNotifyEnable.setStatus("current")


class _FcsDiscoveryCompleteNotifyEnable_Type(TruthValue):
    """Custom type fcsDiscoveryCompleteNotifyEnable based on TruthValue"""


_FcsDiscoveryCompleteNotifyEnable_Object = MibScalar
fcsDiscoveryCompleteNotifyEnable = _FcsDiscoveryCompleteNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 1, 21),
    _FcsDiscoveryCompleteNotifyEnable_Type()
)
fcsDiscoveryCompleteNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcsDiscoveryCompleteNotifyEnable.setStatus("current")
_FcsStats_ObjectIdentity = ObjectIdentity
fcsStats = _FcsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 2)
)
_FcsTotalRejects_Type = Counter32
_FcsTotalRejects_Object = MibScalar
fcsTotalRejects = _FcsTotalRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 2, 1),
    _FcsTotalRejects_Type()
)
fcsTotalRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsTotalRejects.setStatus("current")
_FcsStatsTable_Object = MibTable
fcsStatsTable = _FcsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fcsStatsTable.setStatus("current")
_FcsStatsEntry_Object = MibTableRow
fcsStatsEntry = _FcsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 2, 2, 1)
)
fcsStatsEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    fcsStatsEntry.setStatus("current")
_FcsRxGetReqs_Type = Counter32
_FcsRxGetReqs_Object = MibTableColumn
fcsRxGetReqs = _FcsRxGetReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 2, 2, 1, 1),
    _FcsRxGetReqs_Type()
)
fcsRxGetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsRxGetReqs.setStatus("current")
_FcsTxGetReqs_Type = Counter32
_FcsTxGetReqs_Object = MibTableColumn
fcsTxGetReqs = _FcsTxGetReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 2, 2, 1, 2),
    _FcsTxGetReqs_Type()
)
fcsTxGetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsTxGetReqs.setStatus("current")
_FcsRxRegReqs_Type = Counter32
_FcsRxRegReqs_Object = MibTableColumn
fcsRxRegReqs = _FcsRxRegReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 2, 2, 1, 3),
    _FcsRxRegReqs_Type()
)
fcsRxRegReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsRxRegReqs.setStatus("current")
_FcsTxRegReqs_Type = Counter32
_FcsTxRegReqs_Object = MibTableColumn
fcsTxRegReqs = _FcsTxRegReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 2, 2, 1, 4),
    _FcsTxRegReqs_Type()
)
fcsTxRegReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsTxRegReqs.setStatus("current")
_FcsRxDeregReqs_Type = Counter32
_FcsRxDeregReqs_Object = MibTableColumn
fcsRxDeregReqs = _FcsRxDeregReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 2, 2, 1, 5),
    _FcsRxDeregReqs_Type()
)
fcsRxDeregReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsRxDeregReqs.setStatus("current")
_FcsTxDeregReqs_Type = Counter32
_FcsTxDeregReqs_Object = MibTableColumn
fcsTxDeregReqs = _FcsTxDeregReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 2, 2, 1, 6),
    _FcsTxDeregReqs_Type()
)
fcsTxDeregReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsTxDeregReqs.setStatus("current")
_FcsTxRscns_Type = Counter32
_FcsTxRscns_Object = MibTableColumn
fcsTxRscns = _FcsTxRscns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 2, 2, 1, 7),
    _FcsTxRscns_Type()
)
fcsTxRscns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsTxRscns.setStatus("current")
_FcsRxRscns_Type = Counter32
_FcsRxRscns_Object = MibTableColumn
fcsRxRscns = _FcsRxRscns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 2, 2, 1, 8),
    _FcsRxRscns_Type()
)
fcsRxRscns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsRxRscns.setStatus("current")
_FcsRejects_Type = Counter32
_FcsRejects_Object = MibTableColumn
fcsRejects = _FcsRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 2, 2, 1, 9),
    _FcsRejects_Type()
)
fcsRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsRejects.setStatus("current")
_FcsInformation_ObjectIdentity = ObjectIdentity
fcsInformation = _FcsInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 3)
)
_FcsRejReasonCode_Type = FcGs3RejectReasonCode
_FcsRejReasonCode_Object = MibScalar
fcsRejReasonCode = _FcsRejReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 3, 1),
    _FcsRejReasonCode_Type()
)
fcsRejReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsRejReasonCode.setStatus("current")
_FcsRejReasonCodeExplanation_Type = FcFcsRejReasonExplanation
_FcsRejReasonCodeExplanation_Object = MibScalar
fcsRejReasonCodeExplanation = _FcsRejReasonCodeExplanation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 3, 2),
    _FcsRejReasonCodeExplanation_Type()
)
fcsRejReasonCodeExplanation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcsRejReasonCodeExplanation.setStatus("current")
_FcsMgmtAddrChangeVsanIndex_Type = VsanIndex
_FcsMgmtAddrChangeVsanIndex_Object = MibScalar
fcsMgmtAddrChangeVsanIndex = _FcsMgmtAddrChangeVsanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 3, 3),
    _FcsMgmtAddrChangeVsanIndex_Type()
)
fcsMgmtAddrChangeVsanIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fcsMgmtAddrChangeVsanIndex.setStatus("current")
_FcsMgmtAddrChangeIeName_Type = FcNameId
_FcsMgmtAddrChangeIeName_Object = MibScalar
fcsMgmtAddrChangeIeName = _FcsMgmtAddrChangeIeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 3, 4),
    _FcsMgmtAddrChangeIeName_Type()
)
fcsMgmtAddrChangeIeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fcsMgmtAddrChangeIeName.setStatus("current")
_FcsNotification_ObjectIdentity = ObjectIdentity
fcsNotification = _FcsNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 4)
)
_FcsNotifications_ObjectIdentity = ObjectIdentity
fcsNotifications = _FcsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 4, 0)
)
_FcsMIBConformance_ObjectIdentity = ObjectIdentity
fcsMIBConformance = _FcsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 2)
)
_FcsMIBCompliances_ObjectIdentity = ObjectIdentity
fcsMIBCompliances = _FcsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 2, 1)
)
_FcsMIBGroups_ObjectIdentity = ObjectIdentity
fcsMIBGroups = _FcsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 2, 2)
)

# Managed Objects groups

fcsConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 2, 2, 1)
)
fcsConfigurationGroup.setObjects(
      *(("CISCO-FCS-MIB", "fcsVsanDiscoverySpinLock"),
        ("CISCO-FCS-MIB", "fcsVsanDiscoveryName"),
        ("CISCO-FCS-MIB", "fcsVsanDiscoveryList2k"),
        ("CISCO-FCS-MIB", "fcsVsanDiscoveryList4k"),
        ("CISCO-FCS-MIB", "fcsStartDiscovery"),
        ("CISCO-FCS-MIB", "fcsDiscoveryStatus"),
        ("CISCO-FCS-MIB", "fcsDiscoveryCompleteTime"),
        ("CISCO-FCS-MIB", "fcsVsanDiscoveryTimeOut"),
        ("CISCO-FCS-MIB", "fcsDiscoveryInvalidateCache2k"),
        ("CISCO-FCS-MIB", "fcsDiscoveryInvalidateCache4k"),
        ("CISCO-FCS-MIB", "fcsIeNumber"),
        ("CISCO-FCS-MIB", "fcsIeType"),
        ("CISCO-FCS-MIB", "fcsIeDomainId"),
        ("CISCO-FCS-MIB", "fcsIeMgmtId"),
        ("CISCO-FCS-MIB", "fcsIeFabricName"),
        ("CISCO-FCS-MIB", "fcsIeLogicalName"),
        ("CISCO-FCS-MIB", "fcsIeMgmtAddrListIndex"),
        ("CISCO-FCS-MIB", "fcsIeInfoList"),
        ("CISCO-FCS-MIB", "fcsIePortListIndex"),
        ("CISCO-FCS-MIB", "fcsMgmtAddr"),
        ("CISCO-FCS-MIB", "fcsMgmtAddrConfigSource"),
        ("CISCO-FCS-MIB", "fcsMgmtAddrRowStatus"),
        ("CISCO-FCS-MIB", "fcsPortListIndex"),
        ("CISCO-FCS-MIB", "fcsPortNumber"),
        ("CISCO-FCS-MIB", "fcsPortType"),
        ("CISCO-FCS-MIB", "fcsPortTXType"),
        ("CISCO-FCS-MIB", "fcsPortModuleType"),
        ("CISCO-FCS-MIB", "fcsPortPhyPortNum"),
        ("CISCO-FCS-MIB", "fcsPortAttachPortNameIndex"),
        ("CISCO-FCS-MIB", "fcsPortState"),
        ("CISCO-FCS-MIB", "fcsAttachPortName"),
        ("CISCO-FCS-MIB", "fcsPlatformNumber"),
        ("CISCO-FCS-MIB", "fcsPlatformName"),
        ("CISCO-FCS-MIB", "fcsPlatformType"),
        ("CISCO-FCS-MIB", "fcsPlatformNodeNameListIndex"),
        ("CISCO-FCS-MIB", "fcsPlatformMgmtAddrListIndex"),
        ("CISCO-FCS-MIB", "fcsPlatformConfigSource"),
        ("CISCO-FCS-MIB", "fcsPlatformValidation"),
        ("CISCO-FCS-MIB", "fcsPlatformValidationResult"),
        ("CISCO-FCS-MIB", "fcsPlatformRowStatus"),
        ("CISCO-FCS-MIB", "fcsNodeNameConfigSource"),
        ("CISCO-FCS-MIB", "fcsNodeNameRowStatus"))
)
if mibBuilder.loadTexts:
    fcsConfigurationGroup.setStatus("current")

fcsStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 2, 2, 2)
)
fcsStatisticsGroup.setObjects(
      *(("CISCO-FCS-MIB", "fcsTotalRejects"),
        ("CISCO-FCS-MIB", "fcsRxGetReqs"),
        ("CISCO-FCS-MIB", "fcsTxGetReqs"),
        ("CISCO-FCS-MIB", "fcsRxRegReqs"),
        ("CISCO-FCS-MIB", "fcsTxRegReqs"),
        ("CISCO-FCS-MIB", "fcsRxDeregReqs"),
        ("CISCO-FCS-MIB", "fcsTxDeregReqs"),
        ("CISCO-FCS-MIB", "fcsTxRscns"),
        ("CISCO-FCS-MIB", "fcsRxRscns"),
        ("CISCO-FCS-MIB", "fcsRejects"))
)
if mibBuilder.loadTexts:
    fcsStatisticsGroup.setStatus("current")

fcsNotificationControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 2, 2, 3)
)
fcsNotificationControlGroup.setObjects(
      *(("CISCO-FCS-MIB", "fcsReqRejNotifyEnable"),
        ("CISCO-FCS-MIB", "fcsRejReasonCode"),
        ("CISCO-FCS-MIB", "fcsRejReasonCodeExplanation"),
        ("CISCO-FCS-MIB", "fcsDiscoveryCompleteNotifyEnable"))
)
if mibBuilder.loadTexts:
    fcsNotificationControlGroup.setStatus("deprecated")

fcsNotificationControlGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 2, 2, 6)
)
fcsNotificationControlGroupRev1.setObjects(
      *(("CISCO-FCS-MIB", "fcsReqRejNotifyEnable"),
        ("CISCO-FCS-MIB", "fcsRejReasonCode"),
        ("CISCO-FCS-MIB", "fcsRejReasonCodeExplanation"),
        ("CISCO-FCS-MIB", "fcsDiscoveryCompleteNotifyEnable"),
        ("CISCO-FCS-MIB", "fcsMgmtAddrChangeVsanIndex"),
        ("CISCO-FCS-MIB", "fcsMgmtAddrChangeIeName"))
)
if mibBuilder.loadTexts:
    fcsNotificationControlGroupRev1.setStatus("current")


# Notification objects

fcsReqRejNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 4, 0, 1)
)
fcsReqRejNotify.setObjects(
      *(("CISCO-FCS-MIB", "fcsRejReasonCode"),
        ("CISCO-FCS-MIB", "fcsRejReasonCodeExplanation"))
)
if mibBuilder.loadTexts:
    fcsReqRejNotify.setStatus(
        "current"
    )

fcsDiscoveryCompleteNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 4, 0, 2)
)
fcsDiscoveryCompleteNotify.setObjects(
    ("CISCO-FCS-MIB", "fcsVsanDiscoveryName")
)
if mibBuilder.loadTexts:
    fcsDiscoveryCompleteNotify.setStatus(
        "current"
    )

fcsMgmtAddrChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 1, 4, 0, 3)
)
fcsMgmtAddrChangeNotify.setObjects(
      *(("CISCO-FCS-MIB", "fcsMgmtAddrChangeVsanIndex"),
        ("CISCO-FCS-MIB", "fcsMgmtAddrChangeIeName"))
)
if mibBuilder.loadTexts:
    fcsMgmtAddrChangeNotify.setStatus(
        "current"
    )


# Notifications groups

fcsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 2, 2, 4)
)
fcsNotificationGroup.setObjects(
      *(("CISCO-FCS-MIB", "fcsReqRejNotify"),
        ("CISCO-FCS-MIB", "fcsDiscoveryCompleteNotify"))
)
if mibBuilder.loadTexts:
    fcsNotificationGroup.setStatus(
        "deprecated"
    )

fcsNotificationGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 2, 2, 5)
)
fcsNotificationGroupRev1.setObjects(
      *(("CISCO-FCS-MIB", "fcsReqRejNotify"),
        ("CISCO-FCS-MIB", "fcsDiscoveryCompleteNotify"),
        ("CISCO-FCS-MIB", "fcsMgmtAddrChangeNotify"))
)
if mibBuilder.loadTexts:
    fcsNotificationGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fcsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fcsMIBCompliance.setStatus(
        "deprecated"
    )

fcsMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 297, 2, 1, 2)
)
if mibBuilder.loadTexts:
    fcsMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FCS-MIB",
    **{"CreatedBy": CreatedBy,
       "FcIeType": FcIeType,
       "FcPortState": FcPortState,
       "FcPlatformType": FcPlatformType,
       "FcFcsRejReasonExplanation": FcFcsRejReasonExplanation,
       "ciscoFcsMIB": ciscoFcsMIB,
       "ciscoFcsMIBObjects": ciscoFcsMIBObjects,
       "fcsConfiguration": fcsConfiguration,
       "fcsVsanDiscoverySpinLock": fcsVsanDiscoverySpinLock,
       "fcsVsanDiscoveryName": fcsVsanDiscoveryName,
       "fcsVsanDiscoveryList2k": fcsVsanDiscoveryList2k,
       "fcsVsanDiscoveryList4k": fcsVsanDiscoveryList4k,
       "fcsStartDiscovery": fcsStartDiscovery,
       "fcsDiscoveryStatusTable": fcsDiscoveryStatusTable,
       "fcsDiscoveryStatusEntry": fcsDiscoveryStatusEntry,
       "fcsDiscoveryStatus": fcsDiscoveryStatus,
       "fcsDiscoveryCompleteTime": fcsDiscoveryCompleteTime,
       "fcsVsanDiscoveryTimeOut": fcsVsanDiscoveryTimeOut,
       "fcsDiscoveryInvalidateCache2k": fcsDiscoveryInvalidateCache2k,
       "fcsDiscoveryInvalidateCache4k": fcsDiscoveryInvalidateCache4k,
       "fcsIeNumber": fcsIeNumber,
       "fcsIeTable": fcsIeTable,
       "fcsIeEntry": fcsIeEntry,
       "fcsIeName": fcsIeName,
       "fcsIeType": fcsIeType,
       "fcsIeDomainId": fcsIeDomainId,
       "fcsIeMgmtId": fcsIeMgmtId,
       "fcsIeFabricName": fcsIeFabricName,
       "fcsIeLogicalName": fcsIeLogicalName,
       "fcsIeMgmtAddrListIndex": fcsIeMgmtAddrListIndex,
       "fcsIeInfoList": fcsIeInfoList,
       "fcsIePortListIndex": fcsIePortListIndex,
       "fcsMgmtAddrListTable": fcsMgmtAddrListTable,
       "fcsMgmtAddrListEntry": fcsMgmtAddrListEntry,
       "fcsMgmtAddrListIndex": fcsMgmtAddrListIndex,
       "fcsMgmtAddrIndex": fcsMgmtAddrIndex,
       "fcsMgmtAddr": fcsMgmtAddr,
       "fcsMgmtAddrConfigSource": fcsMgmtAddrConfigSource,
       "fcsMgmtAddrRowStatus": fcsMgmtAddrRowStatus,
       "fcsPortListTable": fcsPortListTable,
       "fcsPortListEntry": fcsPortListEntry,
       "fcsPortListIndex": fcsPortListIndex,
       "fcsPortNumber": fcsPortNumber,
       "fcsPortTable": fcsPortTable,
       "fcsPortEntry": fcsPortEntry,
       "fcsPortName": fcsPortName,
       "fcsPortType": fcsPortType,
       "fcsPortTXType": fcsPortTXType,
       "fcsPortModuleType": fcsPortModuleType,
       "fcsPortPhyPortNum": fcsPortPhyPortNum,
       "fcsPortAttachPortNameIndex": fcsPortAttachPortNameIndex,
       "fcsPortState": fcsPortState,
       "fcsAttachPortNameListTable": fcsAttachPortNameListTable,
       "fcsAttachPortNameListEntry": fcsAttachPortNameListEntry,
       "fcsAttachPortNameListIndex": fcsAttachPortNameListIndex,
       "fcsAttachPortName": fcsAttachPortName,
       "fcsPlatformNumber": fcsPlatformNumber,
       "fcsPlatformTable": fcsPlatformTable,
       "fcsPlatformEntry": fcsPlatformEntry,
       "fcsPlatformIndex": fcsPlatformIndex,
       "fcsPlatformName": fcsPlatformName,
       "fcsPlatformType": fcsPlatformType,
       "fcsPlatformNodeNameListIndex": fcsPlatformNodeNameListIndex,
       "fcsPlatformMgmtAddrListIndex": fcsPlatformMgmtAddrListIndex,
       "fcsPlatformConfigSource": fcsPlatformConfigSource,
       "fcsPlatformValidation": fcsPlatformValidation,
       "fcsPlatformValidationResult": fcsPlatformValidationResult,
       "fcsPlatformRowStatus": fcsPlatformRowStatus,
       "fcsNodeNameListTable": fcsNodeNameListTable,
       "fcsNodeNameListEntry": fcsNodeNameListEntry,
       "fcsNodeNameListIndex": fcsNodeNameListIndex,
       "fcsNodeName": fcsNodeName,
       "fcsNodeNameConfigSource": fcsNodeNameConfigSource,
       "fcsNodeNameRowStatus": fcsNodeNameRowStatus,
       "fcsReqRejNotifyEnable": fcsReqRejNotifyEnable,
       "fcsDiscoveryCompleteNotifyEnable": fcsDiscoveryCompleteNotifyEnable,
       "fcsStats": fcsStats,
       "fcsTotalRejects": fcsTotalRejects,
       "fcsStatsTable": fcsStatsTable,
       "fcsStatsEntry": fcsStatsEntry,
       "fcsRxGetReqs": fcsRxGetReqs,
       "fcsTxGetReqs": fcsTxGetReqs,
       "fcsRxRegReqs": fcsRxRegReqs,
       "fcsTxRegReqs": fcsTxRegReqs,
       "fcsRxDeregReqs": fcsRxDeregReqs,
       "fcsTxDeregReqs": fcsTxDeregReqs,
       "fcsTxRscns": fcsTxRscns,
       "fcsRxRscns": fcsRxRscns,
       "fcsRejects": fcsRejects,
       "fcsInformation": fcsInformation,
       "fcsRejReasonCode": fcsRejReasonCode,
       "fcsRejReasonCodeExplanation": fcsRejReasonCodeExplanation,
       "fcsMgmtAddrChangeVsanIndex": fcsMgmtAddrChangeVsanIndex,
       "fcsMgmtAddrChangeIeName": fcsMgmtAddrChangeIeName,
       "fcsNotification": fcsNotification,
       "fcsNotifications": fcsNotifications,
       "fcsReqRejNotify": fcsReqRejNotify,
       "fcsDiscoveryCompleteNotify": fcsDiscoveryCompleteNotify,
       "fcsMgmtAddrChangeNotify": fcsMgmtAddrChangeNotify,
       "fcsMIBConformance": fcsMIBConformance,
       "fcsMIBCompliances": fcsMIBCompliances,
       "fcsMIBCompliance": fcsMIBCompliance,
       "fcsMIBComplianceRev1": fcsMIBComplianceRev1,
       "fcsMIBGroups": fcsMIBGroups,
       "fcsConfigurationGroup": fcsConfigurationGroup,
       "fcsStatisticsGroup": fcsStatisticsGroup,
       "fcsNotificationControlGroup": fcsNotificationControlGroup,
       "fcsNotificationGroup": fcsNotificationGroup,
       "fcsNotificationGroupRev1": fcsNotificationGroupRev1,
       "fcsNotificationControlGroupRev1": fcsNotificationControlGroupRev1}
)
