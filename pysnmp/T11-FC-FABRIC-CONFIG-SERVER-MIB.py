# SNMP MIB module (T11-FC-FABRIC-CONFIG-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/T11-FC-FABRIC-CONFIG-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:28 2024
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

(FcAddressIdOrZero,
 FcDomainIdOrZero,
 FcNameIdOrZero,
 FcPortType,
 fcmInstanceIndex,
 fcmSwitchIndex) = mibBuilder.importSymbols(
    "FC-MGMT-MIB",
    "FcAddressIdOrZero",
    "FcDomainIdOrZero",
    "FcNameIdOrZero",
    "FcPortType",
    "fcmInstanceIndex",
    "fcmSwitchIndex")

(URLString,) = mibBuilder.importSymbols(
    "NETWORK-SERVICES-MIB",
    "URLString")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(t11FamLocalSwitchWwn,) = mibBuilder.importSymbols(
    "T11-FC-FABRIC-ADDR-MGR-MIB",
    "t11FamLocalSwitchWwn")

(T11NsGs4RejectReasonCode,) = mibBuilder.importSymbols(
    "T11-FC-NAME-SERVER-MIB",
    "T11NsGs4RejectReasonCode")

(T11FabricIndex,) = mibBuilder.importSymbols(
    "T11-TC-MIB",
    "T11FabricIndex")


# MODULE-IDENTITY

t11FcFabricConfigServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 162)
)
t11FcFabricConfigServerMIB.setRevisions(
        ("2007-06-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class T11FcListIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class T11FcListIndexPointerOrZero(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class T11FcIeType(Integer32, TextualConvention):
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



class T11FcPortState(Integer32, TextualConvention):
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
        *(("fault", 6),
          ("offline", 4),
          ("online", 3),
          ("other", 2),
          ("testing", 5),
          ("unknown", 1))
    )



class T11FcPortTxType(Integer32, TextualConvention):
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
        *(("electrical", 6),
          ("longwave1310nm", 5),
          ("longwave1550nm", 4),
          ("other", 2),
          ("shortwave850nm", 3),
          ("tenGbaseEr1550", 9),
          ("tenGbaseEw1550", 13),
          ("tenGbaseLr1310", 8),
          ("tenGbaseLw1310", 12),
          ("tenGbaseLx1300", 10),
          ("tenGbaseSr850", 7),
          ("tenGbaseSw850", 11),
          ("unknown", 1))
    )



class T11FcsRejectReasonExplanation(Integer32, TextualConvention):
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
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("attPortNameListNotAvailable", 14),
          ("attributesMissing", 26),
          ("domainIdNotAvailable", 5),
          ("fabNameNotAvailable", 7),
          ("ieInfoListNotAvailable", 10),
          ("ieListNotAvailable", 3),
          ("ieTypeNotAvailable", 4),
          ("ielogNameNotAvailable", 8),
          ("invNameIdForIEOrPort", 2),
          ("invalidAttribBlockLength", 25),
          ("invalidDeviceNameLength", 23),
          ("mgmtAddrListNotAvailable", 9),
          ("mgmtIdNotAvailable", 6),
          ("multipleAttributes", 24),
          ("noAdditionalExplanation", 1),
          ("noEntriesInLunMap", 22),
          ("phyPortNumNotAvailable", 13),
          ("platformNameAlreadyExists", 18),
          ("platformNameNoExist", 17),
          ("platformNodeNameAlreadyExists", 20),
          ("platformNodeNameNoExists", 19),
          ("portListNotAvailable", 11),
          ("portStateNotAvailable", 15),
          ("portTypeNotAvailable", 12),
          ("resourceUnavailable", 21),
          ("unableToRegIELogName", 16))
    )



# MIB Managed Objects in the order of their OIDs

_T11FcsNotifications_ObjectIdentity = ObjectIdentity
t11FcsNotifications = _T11FcsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 162, 0)
)
_T11FcsMIBObjects_ObjectIdentity = ObjectIdentity
t11FcsMIBObjects = _T11FcsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 162, 1)
)
_T11FcsDiscovery_ObjectIdentity = ObjectIdentity
t11FcsDiscovery = _T11FcsDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 162, 1, 1)
)
_T11FcsFabricDiscoveryTable_Object = MibTable
t11FcsFabricDiscoveryTable = _T11FcsFabricDiscoveryTable_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 1, 1)
)
if mibBuilder.loadTexts:
    t11FcsFabricDiscoveryTable.setStatus("current")
_T11FcsFabricDiscoveryEntry_Object = MibTableRow
t11FcsFabricDiscoveryEntry = _T11FcsFabricDiscoveryEntry_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 1, 1, 1)
)
t11FcsFabricDiscoveryEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
)
if mibBuilder.loadTexts:
    t11FcsFabricDiscoveryEntry.setStatus("current")
_T11FcsFabricDiscoveryRangeLow_Type = T11FabricIndex
_T11FcsFabricDiscoveryRangeLow_Object = MibTableColumn
t11FcsFabricDiscoveryRangeLow = _T11FcsFabricDiscoveryRangeLow_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 1, 1, 1, 1),
    _T11FcsFabricDiscoveryRangeLow_Type()
)
t11FcsFabricDiscoveryRangeLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcsFabricDiscoveryRangeLow.setStatus("current")
_T11FcsFabricDiscoveryRangeHigh_Type = T11FabricIndex
_T11FcsFabricDiscoveryRangeHigh_Object = MibTableColumn
t11FcsFabricDiscoveryRangeHigh = _T11FcsFabricDiscoveryRangeHigh_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 1, 1, 1, 2),
    _T11FcsFabricDiscoveryRangeHigh_Type()
)
t11FcsFabricDiscoveryRangeHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcsFabricDiscoveryRangeHigh.setStatus("current")


class _T11FcsFabricDiscoveryStart_Type(Integer32):
    """Custom type t11FcsFabricDiscoveryStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 2),
          ("start", 1))
    )


_T11FcsFabricDiscoveryStart_Type.__name__ = "Integer32"
_T11FcsFabricDiscoveryStart_Object = MibTableColumn
t11FcsFabricDiscoveryStart = _T11FcsFabricDiscoveryStart_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 1, 1, 1, 3),
    _T11FcsFabricDiscoveryStart_Type()
)
t11FcsFabricDiscoveryStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcsFabricDiscoveryStart.setStatus("current")


class _T11FcsFabricDiscoveryTimeOut_Type(Unsigned32):
    """Custom type t11FcsFabricDiscoveryTimeOut based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 86400),
    )


_T11FcsFabricDiscoveryTimeOut_Type.__name__ = "Unsigned32"
_T11FcsFabricDiscoveryTimeOut_Object = MibTableColumn
t11FcsFabricDiscoveryTimeOut = _T11FcsFabricDiscoveryTimeOut_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 1, 1, 1, 4),
    _T11FcsFabricDiscoveryTimeOut_Type()
)
t11FcsFabricDiscoveryTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcsFabricDiscoveryTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    t11FcsFabricDiscoveryTimeOut.setUnits("Seconds")
_T11FcsDiscoveryStateTable_Object = MibTable
t11FcsDiscoveryStateTable = _T11FcsDiscoveryStateTable_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 1, 2)
)
if mibBuilder.loadTexts:
    t11FcsDiscoveryStateTable.setStatus("current")
_T11FcsDiscoveryStateEntry_Object = MibTableRow
t11FcsDiscoveryStateEntry = _T11FcsDiscoveryStateEntry_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 1, 2, 1)
)
t11FcsDiscoveryStateEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsFabricIndex"),
)
if mibBuilder.loadTexts:
    t11FcsDiscoveryStateEntry.setStatus("current")
_T11FcsFabricIndex_Type = T11FabricIndex
_T11FcsFabricIndex_Object = MibTableColumn
t11FcsFabricIndex = _T11FcsFabricIndex_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 1, 2, 1, 1),
    _T11FcsFabricIndex_Type()
)
t11FcsFabricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcsFabricIndex.setStatus("current")


class _T11FcsDiscoveryStatus_Type(Integer32):
    """Custom type t11FcsDiscoveryStatus based on Integer32"""
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
          ("inProgress", 1),
          ("localOnly", 3))
    )


_T11FcsDiscoveryStatus_Type.__name__ = "Integer32"
_T11FcsDiscoveryStatus_Object = MibTableColumn
t11FcsDiscoveryStatus = _T11FcsDiscoveryStatus_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 1, 2, 1, 2),
    _T11FcsDiscoveryStatus_Type()
)
t11FcsDiscoveryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcsDiscoveryStatus.setStatus("current")
_T11FcsDiscoveryCompleteTime_Type = TimeStamp
_T11FcsDiscoveryCompleteTime_Object = MibTableColumn
t11FcsDiscoveryCompleteTime = _T11FcsDiscoveryCompleteTime_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 1, 2, 1, 3),
    _T11FcsDiscoveryCompleteTime_Type()
)
t11FcsDiscoveryCompleteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsDiscoveryCompleteTime.setStatus("current")
_T11FcsDiscoveredConfig_ObjectIdentity = ObjectIdentity
t11FcsDiscoveredConfig = _T11FcsDiscoveredConfig_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 162, 1, 2)
)
_T11FcsIeTable_Object = MibTable
t11FcsIeTable = _T11FcsIeTable_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 1)
)
if mibBuilder.loadTexts:
    t11FcsIeTable.setStatus("current")
_T11FcsIeEntry_Object = MibTableRow
t11FcsIeEntry = _T11FcsIeEntry_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 1, 1)
)
t11FcsIeEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsFabricIndex"),
    (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsIeName"),
)
if mibBuilder.loadTexts:
    t11FcsIeEntry.setStatus("current")


class _T11FcsIeName_Type(FcNameIdOrZero):
    """Custom type t11FcsIeName based on FcNameIdOrZero"""
    subtypeSpec = FcNameIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
    )


_T11FcsIeName_Type.__name__ = "FcNameIdOrZero"
_T11FcsIeName_Object = MibTableColumn
t11FcsIeName = _T11FcsIeName_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 1, 1, 1),
    _T11FcsIeName_Type()
)
t11FcsIeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcsIeName.setStatus("current")
_T11FcsIeType_Type = T11FcIeType
_T11FcsIeType_Object = MibTableColumn
t11FcsIeType = _T11FcsIeType_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 1, 1, 2),
    _T11FcsIeType_Type()
)
t11FcsIeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsIeType.setStatus("current")
_T11FcsIeDomainId_Type = FcDomainIdOrZero
_T11FcsIeDomainId_Object = MibTableColumn
t11FcsIeDomainId = _T11FcsIeDomainId_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 1, 1, 3),
    _T11FcsIeDomainId_Type()
)
t11FcsIeDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsIeDomainId.setStatus("current")


class _T11FcsIeMgmtId_Type(FcAddressIdOrZero):
    """Custom type t11FcsIeMgmtId based on FcAddressIdOrZero"""
    defaultHexValue = "000000"


_T11FcsIeMgmtId_Object = MibTableColumn
t11FcsIeMgmtId = _T11FcsIeMgmtId_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 1, 1, 4),
    _T11FcsIeMgmtId_Type()
)
t11FcsIeMgmtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsIeMgmtId.setStatus("current")


class _T11FcsIeFabricName_Type(FcNameIdOrZero):
    """Custom type t11FcsIeFabricName based on FcNameIdOrZero"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = FcNameIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
    )


_T11FcsIeFabricName_Type.__name__ = "FcNameIdOrZero"
_T11FcsIeFabricName_Object = MibTableColumn
t11FcsIeFabricName = _T11FcsIeFabricName_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 1, 1, 5),
    _T11FcsIeFabricName_Type()
)
t11FcsIeFabricName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsIeFabricName.setStatus("current")


class _T11FcsIeLogicalName_Type(OctetString):
    """Custom type t11FcsIeLogicalName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_T11FcsIeLogicalName_Type.__name__ = "OctetString"
_T11FcsIeLogicalName_Object = MibTableColumn
t11FcsIeLogicalName = _T11FcsIeLogicalName_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 1, 1, 6),
    _T11FcsIeLogicalName_Type()
)
t11FcsIeLogicalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsIeLogicalName.setStatus("current")
_T11FcsIeMgmtAddrListIndex_Type = T11FcListIndexPointerOrZero
_T11FcsIeMgmtAddrListIndex_Object = MibTableColumn
t11FcsIeMgmtAddrListIndex = _T11FcsIeMgmtAddrListIndex_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 1, 1, 7),
    _T11FcsIeMgmtAddrListIndex_Type()
)
t11FcsIeMgmtAddrListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsIeMgmtAddrListIndex.setStatus("current")


class _T11FcsIeInfoList_Type(OctetString):
    """Custom type t11FcsIeInfoList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 252),
    )


_T11FcsIeInfoList_Type.__name__ = "OctetString"
_T11FcsIeInfoList_Object = MibTableColumn
t11FcsIeInfoList = _T11FcsIeInfoList_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 1, 1, 8),
    _T11FcsIeInfoList_Type()
)
t11FcsIeInfoList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsIeInfoList.setStatus("current")
_T11FcsMgmtAddrListTable_Object = MibTable
t11FcsMgmtAddrListTable = _T11FcsMgmtAddrListTable_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 2)
)
if mibBuilder.loadTexts:
    t11FcsMgmtAddrListTable.setStatus("current")
_T11FcsMgmtAddrListEntry_Object = MibTableRow
t11FcsMgmtAddrListEntry = _T11FcsMgmtAddrListEntry_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 2, 1)
)
t11FcsMgmtAddrListEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsMgmtAddrListIndex"),
    (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsMgmtAddrIndex"),
)
if mibBuilder.loadTexts:
    t11FcsMgmtAddrListEntry.setStatus("current")
_T11FcsMgmtAddrListIndex_Type = T11FcListIndex
_T11FcsMgmtAddrListIndex_Object = MibTableColumn
t11FcsMgmtAddrListIndex = _T11FcsMgmtAddrListIndex_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 2, 1, 1),
    _T11FcsMgmtAddrListIndex_Type()
)
t11FcsMgmtAddrListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcsMgmtAddrListIndex.setStatus("current")


class _T11FcsMgmtAddrIndex_Type(Unsigned32):
    """Custom type t11FcsMgmtAddrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcsMgmtAddrIndex_Type.__name__ = "Unsigned32"
_T11FcsMgmtAddrIndex_Object = MibTableColumn
t11FcsMgmtAddrIndex = _T11FcsMgmtAddrIndex_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 2, 1, 2),
    _T11FcsMgmtAddrIndex_Type()
)
t11FcsMgmtAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcsMgmtAddrIndex.setStatus("current")
_T11FcsMgmtAddr_Type = URLString
_T11FcsMgmtAddr_Object = MibTableColumn
t11FcsMgmtAddr = _T11FcsMgmtAddr_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 2, 1, 3),
    _T11FcsMgmtAddr_Type()
)
t11FcsMgmtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsMgmtAddr.setStatus("current")
_T11FcsPortTable_Object = MibTable
t11FcsPortTable = _T11FcsPortTable_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 4)
)
if mibBuilder.loadTexts:
    t11FcsPortTable.setStatus("current")
_T11FcsPortEntry_Object = MibTableRow
t11FcsPortEntry = _T11FcsPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 4, 1)
)
t11FcsPortEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsFabricIndex"),
    (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsIeName"),
    (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPortName"),
)
if mibBuilder.loadTexts:
    t11FcsPortEntry.setStatus("current")


class _T11FcsPortName_Type(FcNameIdOrZero):
    """Custom type t11FcsPortName based on FcNameIdOrZero"""
    subtypeSpec = FcNameIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
    )


_T11FcsPortName_Type.__name__ = "FcNameIdOrZero"
_T11FcsPortName_Object = MibTableColumn
t11FcsPortName = _T11FcsPortName_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 4, 1, 1),
    _T11FcsPortName_Type()
)
t11FcsPortName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcsPortName.setStatus("current")
_T11FcsPortType_Type = FcPortType
_T11FcsPortType_Object = MibTableColumn
t11FcsPortType = _T11FcsPortType_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 4, 1, 2),
    _T11FcsPortType_Type()
)
t11FcsPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsPortType.setStatus("current")
_T11FcsPortTxType_Type = T11FcPortTxType
_T11FcsPortTxType_Object = MibTableColumn
t11FcsPortTxType = _T11FcsPortTxType_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 4, 1, 3),
    _T11FcsPortTxType_Type()
)
t11FcsPortTxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsPortTxType.setStatus("current")


class _T11FcsPortModuleType_Type(Unsigned32):
    """Custom type t11FcsPortModuleType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_T11FcsPortModuleType_Type.__name__ = "Unsigned32"
_T11FcsPortModuleType_Object = MibTableColumn
t11FcsPortModuleType = _T11FcsPortModuleType_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 4, 1, 4),
    _T11FcsPortModuleType_Type()
)
t11FcsPortModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsPortModuleType.setStatus("current")
_T11FcsPortPhyPortNum_Type = Unsigned32
_T11FcsPortPhyPortNum_Object = MibTableColumn
t11FcsPortPhyPortNum = _T11FcsPortPhyPortNum_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 4, 1, 5),
    _T11FcsPortPhyPortNum_Type()
)
t11FcsPortPhyPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsPortPhyPortNum.setStatus("current")
_T11FcsPortAttachPortNameIndex_Type = T11FcListIndexPointerOrZero
_T11FcsPortAttachPortNameIndex_Object = MibTableColumn
t11FcsPortAttachPortNameIndex = _T11FcsPortAttachPortNameIndex_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 4, 1, 6),
    _T11FcsPortAttachPortNameIndex_Type()
)
t11FcsPortAttachPortNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsPortAttachPortNameIndex.setStatus("current")
_T11FcsPortState_Type = T11FcPortState
_T11FcsPortState_Object = MibTableColumn
t11FcsPortState = _T11FcsPortState_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 4, 1, 7),
    _T11FcsPortState_Type()
)
t11FcsPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsPortState.setStatus("current")


class _T11FcsPortSpeedCapab_Type(OctetString):
    """Custom type t11FcsPortSpeedCapab based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_T11FcsPortSpeedCapab_Type.__name__ = "OctetString"
_T11FcsPortSpeedCapab_Object = MibTableColumn
t11FcsPortSpeedCapab = _T11FcsPortSpeedCapab_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 4, 1, 8),
    _T11FcsPortSpeedCapab_Type()
)
t11FcsPortSpeedCapab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsPortSpeedCapab.setStatus("current")


class _T11FcsPortOperSpeed_Type(OctetString):
    """Custom type t11FcsPortOperSpeed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_T11FcsPortOperSpeed_Type.__name__ = "OctetString"
_T11FcsPortOperSpeed_Object = MibTableColumn
t11FcsPortOperSpeed = _T11FcsPortOperSpeed_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 4, 1, 9),
    _T11FcsPortOperSpeed_Type()
)
t11FcsPortOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsPortOperSpeed.setStatus("current")


class _T11FcsPortZoningEnfStatus_Type(OctetString):
    """Custom type t11FcsPortZoningEnfStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_T11FcsPortZoningEnfStatus_Type.__name__ = "OctetString"
_T11FcsPortZoningEnfStatus_Object = MibTableColumn
t11FcsPortZoningEnfStatus = _T11FcsPortZoningEnfStatus_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 4, 1, 10),
    _T11FcsPortZoningEnfStatus_Type()
)
t11FcsPortZoningEnfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsPortZoningEnfStatus.setStatus("current")
_T11FcsAttachPortNameListTable_Object = MibTable
t11FcsAttachPortNameListTable = _T11FcsAttachPortNameListTable_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 5)
)
if mibBuilder.loadTexts:
    t11FcsAttachPortNameListTable.setStatus("current")
_T11FcsAttachPortNameListEntry_Object = MibTableRow
t11FcsAttachPortNameListEntry = _T11FcsAttachPortNameListEntry_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 5, 1)
)
t11FcsAttachPortNameListEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsAttachPortNameListIndex"),
    (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsAttachPortName"),
)
if mibBuilder.loadTexts:
    t11FcsAttachPortNameListEntry.setStatus("current")
_T11FcsAttachPortNameListIndex_Type = T11FcListIndex
_T11FcsAttachPortNameListIndex_Object = MibTableColumn
t11FcsAttachPortNameListIndex = _T11FcsAttachPortNameListIndex_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 5, 1, 1),
    _T11FcsAttachPortNameListIndex_Type()
)
t11FcsAttachPortNameListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcsAttachPortNameListIndex.setStatus("current")


class _T11FcsAttachPortName_Type(OctetString):
    """Custom type t11FcsAttachPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_T11FcsAttachPortName_Type.__name__ = "OctetString"
_T11FcsAttachPortName_Object = MibTableColumn
t11FcsAttachPortName = _T11FcsAttachPortName_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 5, 1, 2),
    _T11FcsAttachPortName_Type()
)
t11FcsAttachPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsAttachPortName.setStatus("current")
_T11FcsPlatformTable_Object = MibTable
t11FcsPlatformTable = _T11FcsPlatformTable_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 6)
)
if mibBuilder.loadTexts:
    t11FcsPlatformTable.setStatus("current")
_T11FcsPlatformEntry_Object = MibTableRow
t11FcsPlatformEntry = _T11FcsPlatformEntry_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1)
)
t11FcsPlatformEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsFabricIndex"),
    (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformIndex"),
)
if mibBuilder.loadTexts:
    t11FcsPlatformEntry.setStatus("current")


class _T11FcsPlatformIndex_Type(Unsigned32):
    """Custom type t11FcsPlatformIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcsPlatformIndex_Type.__name__ = "Unsigned32"
_T11FcsPlatformIndex_Object = MibTableColumn
t11FcsPlatformIndex = _T11FcsPlatformIndex_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 1),
    _T11FcsPlatformIndex_Type()
)
t11FcsPlatformIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcsPlatformIndex.setStatus("current")


class _T11FcsPlatformName_Type(OctetString):
    """Custom type t11FcsPlatformName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_T11FcsPlatformName_Type.__name__ = "OctetString"
_T11FcsPlatformName_Object = MibTableColumn
t11FcsPlatformName = _T11FcsPlatformName_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 2),
    _T11FcsPlatformName_Type()
)
t11FcsPlatformName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsPlatformName.setStatus("current")


class _T11FcsPlatformType_Type(OctetString):
    """Custom type t11FcsPlatformType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_T11FcsPlatformType_Type.__name__ = "OctetString"
_T11FcsPlatformType_Object = MibTableColumn
t11FcsPlatformType = _T11FcsPlatformType_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 3),
    _T11FcsPlatformType_Type()
)
t11FcsPlatformType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsPlatformType.setStatus("current")
_T11FcsPlatformNodeNameListIndex_Type = T11FcListIndexPointerOrZero
_T11FcsPlatformNodeNameListIndex_Object = MibTableColumn
t11FcsPlatformNodeNameListIndex = _T11FcsPlatformNodeNameListIndex_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 4),
    _T11FcsPlatformNodeNameListIndex_Type()
)
t11FcsPlatformNodeNameListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsPlatformNodeNameListIndex.setStatus("current")
_T11FcsPlatformMgmtAddrListIndex_Type = T11FcListIndexPointerOrZero
_T11FcsPlatformMgmtAddrListIndex_Object = MibTableColumn
t11FcsPlatformMgmtAddrListIndex = _T11FcsPlatformMgmtAddrListIndex_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 5),
    _T11FcsPlatformMgmtAddrListIndex_Type()
)
t11FcsPlatformMgmtAddrListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsPlatformMgmtAddrListIndex.setStatus("current")


class _T11FcsPlatformVendorId_Type(SnmpAdminString):
    """Custom type t11FcsPlatformVendorId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(12, 12),
    )


_T11FcsPlatformVendorId_Type.__name__ = "SnmpAdminString"
_T11FcsPlatformVendorId_Object = MibTableColumn
t11FcsPlatformVendorId = _T11FcsPlatformVendorId_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 6),
    _T11FcsPlatformVendorId_Type()
)
t11FcsPlatformVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsPlatformVendorId.setStatus("current")


class _T11FcsPlatformProductId_Type(SnmpAdminString):
    """Custom type t11FcsPlatformProductId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(20, 20),
    )


_T11FcsPlatformProductId_Type.__name__ = "SnmpAdminString"
_T11FcsPlatformProductId_Object = MibTableColumn
t11FcsPlatformProductId = _T11FcsPlatformProductId_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 7),
    _T11FcsPlatformProductId_Type()
)
t11FcsPlatformProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsPlatformProductId.setStatus("current")


class _T11FcsPlatformProductRevLevel_Type(SnmpAdminString):
    """Custom type t11FcsPlatformProductRevLevel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 32),
    )


_T11FcsPlatformProductRevLevel_Type.__name__ = "SnmpAdminString"
_T11FcsPlatformProductRevLevel_Object = MibTableColumn
t11FcsPlatformProductRevLevel = _T11FcsPlatformProductRevLevel_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 8),
    _T11FcsPlatformProductRevLevel_Type()
)
t11FcsPlatformProductRevLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsPlatformProductRevLevel.setStatus("current")


class _T11FcsPlatformDescription_Type(SnmpAdminString):
    """Custom type t11FcsPlatformDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 128),
    )


_T11FcsPlatformDescription_Type.__name__ = "SnmpAdminString"
_T11FcsPlatformDescription_Object = MibTableColumn
t11FcsPlatformDescription = _T11FcsPlatformDescription_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 9),
    _T11FcsPlatformDescription_Type()
)
t11FcsPlatformDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsPlatformDescription.setStatus("current")


class _T11FcsPlatformLabel_Type(SnmpAdminString):
    """Custom type t11FcsPlatformLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 64),
    )


_T11FcsPlatformLabel_Type.__name__ = "SnmpAdminString"
_T11FcsPlatformLabel_Object = MibTableColumn
t11FcsPlatformLabel = _T11FcsPlatformLabel_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 10),
    _T11FcsPlatformLabel_Type()
)
t11FcsPlatformLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsPlatformLabel.setStatus("current")


class _T11FcsPlatformLocation_Type(SnmpAdminString):
    """Custom type t11FcsPlatformLocation based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 128),
    )


_T11FcsPlatformLocation_Type.__name__ = "SnmpAdminString"
_T11FcsPlatformLocation_Object = MibTableColumn
t11FcsPlatformLocation = _T11FcsPlatformLocation_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 11),
    _T11FcsPlatformLocation_Type()
)
t11FcsPlatformLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsPlatformLocation.setStatus("current")


class _T11FcsPlatformSystemID_Type(SnmpAdminString):
    """Custom type t11FcsPlatformSystemID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 64),
    )


_T11FcsPlatformSystemID_Type.__name__ = "SnmpAdminString"
_T11FcsPlatformSystemID_Object = MibTableColumn
t11FcsPlatformSystemID = _T11FcsPlatformSystemID_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 12),
    _T11FcsPlatformSystemID_Type()
)
t11FcsPlatformSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsPlatformSystemID.setStatus("current")
_T11FcsPlatformSysMgmtAddr_Type = T11FcListIndexPointerOrZero
_T11FcsPlatformSysMgmtAddr_Object = MibTableColumn
t11FcsPlatformSysMgmtAddr = _T11FcsPlatformSysMgmtAddr_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 13),
    _T11FcsPlatformSysMgmtAddr_Type()
)
t11FcsPlatformSysMgmtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsPlatformSysMgmtAddr.setStatus("current")


class _T11FcsPlatformClusterId_Type(SnmpAdminString):
    """Custom type t11FcsPlatformClusterId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 64),
    )


_T11FcsPlatformClusterId_Type.__name__ = "SnmpAdminString"
_T11FcsPlatformClusterId_Object = MibTableColumn
t11FcsPlatformClusterId = _T11FcsPlatformClusterId_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 14),
    _T11FcsPlatformClusterId_Type()
)
t11FcsPlatformClusterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsPlatformClusterId.setStatus("current")
_T11FcsPlatformClusterMgmtAddr_Type = T11FcListIndexPointerOrZero
_T11FcsPlatformClusterMgmtAddr_Object = MibTableColumn
t11FcsPlatformClusterMgmtAddr = _T11FcsPlatformClusterMgmtAddr_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 15),
    _T11FcsPlatformClusterMgmtAddr_Type()
)
t11FcsPlatformClusterMgmtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsPlatformClusterMgmtAddr.setStatus("current")


class _T11FcsPlatformFC4Types_Type(OctetString):
    """Custom type t11FcsPlatformFC4Types based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(32, 32),
    )


_T11FcsPlatformFC4Types_Type.__name__ = "OctetString"
_T11FcsPlatformFC4Types_Object = MibTableColumn
t11FcsPlatformFC4Types = _T11FcsPlatformFC4Types_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 16),
    _T11FcsPlatformFC4Types_Type()
)
t11FcsPlatformFC4Types.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsPlatformFC4Types.setStatus("current")
_T11FcsNodeNameListTable_Object = MibTable
t11FcsNodeNameListTable = _T11FcsNodeNameListTable_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 7)
)
if mibBuilder.loadTexts:
    t11FcsNodeNameListTable.setStatus("current")
_T11FcsNodeNameListEntry_Object = MibTableRow
t11FcsNodeNameListEntry = _T11FcsNodeNameListEntry_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 7, 1)
)
t11FcsNodeNameListEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsNodeNameListIndex"),
    (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsNodeName"),
)
if mibBuilder.loadTexts:
    t11FcsNodeNameListEntry.setStatus("current")
_T11FcsNodeNameListIndex_Type = T11FcListIndex
_T11FcsNodeNameListIndex_Object = MibTableColumn
t11FcsNodeNameListIndex = _T11FcsNodeNameListIndex_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 7, 1, 1),
    _T11FcsNodeNameListIndex_Type()
)
t11FcsNodeNameListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcsNodeNameListIndex.setStatus("current")


class _T11FcsNodeName_Type(FcNameIdOrZero):
    """Custom type t11FcsNodeName based on FcNameIdOrZero"""
    subtypeSpec = FcNameIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
    )


_T11FcsNodeName_Type.__name__ = "FcNameIdOrZero"
_T11FcsNodeName_Object = MibTableColumn
t11FcsNodeName = _T11FcsNodeName_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 2, 7, 1, 2),
    _T11FcsNodeName_Type()
)
t11FcsNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsNodeName.setStatus("current")
_T11FcsStats_ObjectIdentity = ObjectIdentity
t11FcsStats = _T11FcsStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 162, 1, 3)
)
_T11FcsStatsTable_Object = MibTable
t11FcsStatsTable = _T11FcsStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 3, 1)
)
if mibBuilder.loadTexts:
    t11FcsStatsTable.setStatus("current")
_T11FcsStatsEntry_Object = MibTableRow
t11FcsStatsEntry = _T11FcsStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 3, 1, 1)
)
t11FcsStatsEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsFabricIndex"),
)
if mibBuilder.loadTexts:
    t11FcsStatsEntry.setStatus("current")
_T11FcsInGetReqs_Type = Counter32
_T11FcsInGetReqs_Object = MibTableColumn
t11FcsInGetReqs = _T11FcsInGetReqs_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 3, 1, 1, 1),
    _T11FcsInGetReqs_Type()
)
t11FcsInGetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsInGetReqs.setStatus("current")
_T11FcsOutGetReqs_Type = Counter32
_T11FcsOutGetReqs_Object = MibTableColumn
t11FcsOutGetReqs = _T11FcsOutGetReqs_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 3, 1, 1, 2),
    _T11FcsOutGetReqs_Type()
)
t11FcsOutGetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsOutGetReqs.setStatus("current")
_T11FcsInRegReqs_Type = Counter32
_T11FcsInRegReqs_Object = MibTableColumn
t11FcsInRegReqs = _T11FcsInRegReqs_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 3, 1, 1, 3),
    _T11FcsInRegReqs_Type()
)
t11FcsInRegReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsInRegReqs.setStatus("current")
_T11FcsOutRegReqs_Type = Counter32
_T11FcsOutRegReqs_Object = MibTableColumn
t11FcsOutRegReqs = _T11FcsOutRegReqs_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 3, 1, 1, 4),
    _T11FcsOutRegReqs_Type()
)
t11FcsOutRegReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsOutRegReqs.setStatus("current")
_T11FcsInDeregReqs_Type = Counter32
_T11FcsInDeregReqs_Object = MibTableColumn
t11FcsInDeregReqs = _T11FcsInDeregReqs_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 3, 1, 1, 5),
    _T11FcsInDeregReqs_Type()
)
t11FcsInDeregReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsInDeregReqs.setStatus("current")
_T11FcsOutDeregReqs_Type = Counter32
_T11FcsOutDeregReqs_Object = MibTableColumn
t11FcsOutDeregReqs = _T11FcsOutDeregReqs_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 3, 1, 1, 6),
    _T11FcsOutDeregReqs_Type()
)
t11FcsOutDeregReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsOutDeregReqs.setStatus("current")
_T11FcsRejects_Type = Counter32
_T11FcsRejects_Object = MibTableColumn
t11FcsRejects = _T11FcsRejects_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 3, 1, 1, 7),
    _T11FcsRejects_Type()
)
t11FcsRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsRejects.setStatus("current")
_T11FcsNotificationInfo_ObjectIdentity = ObjectIdentity
t11FcsNotificationInfo = _T11FcsNotificationInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 162, 1, 4)
)
_T11FcsNotifyControlTable_Object = MibTable
t11FcsNotifyControlTable = _T11FcsNotifyControlTable_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 4, 1)
)
if mibBuilder.loadTexts:
    t11FcsNotifyControlTable.setStatus("current")
_T11FcsNotifyControlEntry_Object = MibTableRow
t11FcsNotifyControlEntry = _T11FcsNotifyControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 4, 1, 1)
)
t11FcsNotifyControlEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsFabricIndex"),
)
if mibBuilder.loadTexts:
    t11FcsNotifyControlEntry.setStatus("current")


class _T11FcsReqRejectNotifyEnable_Type(TruthValue):
    """Custom type t11FcsReqRejectNotifyEnable based on TruthValue"""


_T11FcsReqRejectNotifyEnable_Object = MibTableColumn
t11FcsReqRejectNotifyEnable = _T11FcsReqRejectNotifyEnable_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 4, 1, 1, 1),
    _T11FcsReqRejectNotifyEnable_Type()
)
t11FcsReqRejectNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcsReqRejectNotifyEnable.setStatus("current")


class _T11FcsDiscoveryCompNotifyEnable_Type(TruthValue):
    """Custom type t11FcsDiscoveryCompNotifyEnable based on TruthValue"""


_T11FcsDiscoveryCompNotifyEnable_Object = MibTableColumn
t11FcsDiscoveryCompNotifyEnable = _T11FcsDiscoveryCompNotifyEnable_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 4, 1, 1, 2),
    _T11FcsDiscoveryCompNotifyEnable_Type()
)
t11FcsDiscoveryCompNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcsDiscoveryCompNotifyEnable.setStatus("current")


class _T11FcsMgmtAddrChangeNotifyEnable_Type(TruthValue):
    """Custom type t11FcsMgmtAddrChangeNotifyEnable based on TruthValue"""


_T11FcsMgmtAddrChangeNotifyEnable_Object = MibTableColumn
t11FcsMgmtAddrChangeNotifyEnable = _T11FcsMgmtAddrChangeNotifyEnable_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 4, 1, 1, 3),
    _T11FcsMgmtAddrChangeNotifyEnable_Type()
)
t11FcsMgmtAddrChangeNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcsMgmtAddrChangeNotifyEnable.setStatus("current")


class _T11FcsRejectCtCommandString_Type(OctetString):
    """Custom type t11FcsRejectCtCommandString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_T11FcsRejectCtCommandString_Type.__name__ = "OctetString"
_T11FcsRejectCtCommandString_Object = MibTableColumn
t11FcsRejectCtCommandString = _T11FcsRejectCtCommandString_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 4, 1, 1, 4),
    _T11FcsRejectCtCommandString_Type()
)
t11FcsRejectCtCommandString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsRejectCtCommandString.setStatus("current")
_T11FcsRejectRequestSource_Type = FcNameIdOrZero
_T11FcsRejectRequestSource_Object = MibTableColumn
t11FcsRejectRequestSource = _T11FcsRejectRequestSource_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 4, 1, 1, 5),
    _T11FcsRejectRequestSource_Type()
)
t11FcsRejectRequestSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsRejectRequestSource.setStatus("current")
_T11FcsRejectReasonCode_Type = T11NsGs4RejectReasonCode
_T11FcsRejectReasonCode_Object = MibTableColumn
t11FcsRejectReasonCode = _T11FcsRejectReasonCode_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 4, 1, 1, 6),
    _T11FcsRejectReasonCode_Type()
)
t11FcsRejectReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsRejectReasonCode.setStatus("current")
_T11FcsRejectReasonCodeExp_Type = T11FcsRejectReasonExplanation
_T11FcsRejectReasonCodeExp_Object = MibTableColumn
t11FcsRejectReasonCodeExp = _T11FcsRejectReasonCodeExp_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 4, 1, 1, 7),
    _T11FcsRejectReasonCodeExp_Type()
)
t11FcsRejectReasonCodeExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsRejectReasonCodeExp.setStatus("current")


class _T11FcsRejectReasonVendorCode_Type(OctetString):
    """Custom type t11FcsRejectReasonVendorCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_T11FcsRejectReasonVendorCode_Type.__name__ = "OctetString"
_T11FcsRejectReasonVendorCode_Object = MibTableColumn
t11FcsRejectReasonVendorCode = _T11FcsRejectReasonVendorCode_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 4, 1, 1, 8),
    _T11FcsRejectReasonVendorCode_Type()
)
t11FcsRejectReasonVendorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcsRejectReasonVendorCode.setStatus("current")
_T11FcsMgmtAddrChangeFabricIndex_Type = T11FabricIndex
_T11FcsMgmtAddrChangeFabricIndex_Object = MibScalar
t11FcsMgmtAddrChangeFabricIndex = _T11FcsMgmtAddrChangeFabricIndex_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 4, 2),
    _T11FcsMgmtAddrChangeFabricIndex_Type()
)
t11FcsMgmtAddrChangeFabricIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    t11FcsMgmtAddrChangeFabricIndex.setStatus("current")
_T11FcsMgmtAddrChangeIeName_Type = FcNameIdOrZero
_T11FcsMgmtAddrChangeIeName_Object = MibScalar
t11FcsMgmtAddrChangeIeName = _T11FcsMgmtAddrChangeIeName_Object(
    (1, 3, 6, 1, 2, 1, 162, 1, 4, 3),
    _T11FcsMgmtAddrChangeIeName_Type()
)
t11FcsMgmtAddrChangeIeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    t11FcsMgmtAddrChangeIeName.setStatus("current")
_T11FcsMIBConformance_ObjectIdentity = ObjectIdentity
t11FcsMIBConformance = _T11FcsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 162, 2)
)
_T11FcsMIBCompliances_ObjectIdentity = ObjectIdentity
t11FcsMIBCompliances = _T11FcsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 162, 2, 1)
)
_T11FcsMIBGroups_ObjectIdentity = ObjectIdentity
t11FcsMIBGroups = _T11FcsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 162, 2, 2)
)

# Managed Objects groups

t11FcsDiscoveryControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 162, 2, 2, 1)
)
t11FcsDiscoveryControlGroup.setObjects(
      *(("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsFabricDiscoveryRangeLow"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsFabricDiscoveryRangeHigh"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsFabricDiscoveryStart"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsFabricDiscoveryTimeOut"))
)
if mibBuilder.loadTexts:
    t11FcsDiscoveryControlGroup.setStatus("current")

t11FcsDiscoveryStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 162, 2, 2, 2)
)
t11FcsDiscoveryStatusGroup.setObjects(
      *(("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsDiscoveryStatus"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsDiscoveryCompleteTime"))
)
if mibBuilder.loadTexts:
    t11FcsDiscoveryStatusGroup.setStatus("current")

t11FcsDiscoveredConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 162, 2, 2, 3)
)
t11FcsDiscoveredConfigGroup.setObjects(
      *(("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsIeType"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsIeDomainId"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsIeMgmtId"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsIeFabricName"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsIeLogicalName"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsIeMgmtAddrListIndex"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsIeInfoList"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsMgmtAddr"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPortType"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPortTxType"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPortModuleType"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPortPhyPortNum"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPortAttachPortNameIndex"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPortState"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPortSpeedCapab"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPortOperSpeed"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPortZoningEnfStatus"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsAttachPortName"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformName"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformType"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformNodeNameListIndex"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformMgmtAddrListIndex"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformVendorId"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformProductId"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformProductRevLevel"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformDescription"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformLabel"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformLocation"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformSystemID"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformSysMgmtAddr"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformClusterId"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformClusterMgmtAddr"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformFC4Types"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsNodeName"))
)
if mibBuilder.loadTexts:
    t11FcsDiscoveredConfigGroup.setStatus("current")

t11FcsStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 162, 2, 2, 4)
)
t11FcsStatisticsGroup.setObjects(
      *(("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsInGetReqs"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsOutGetReqs"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsInRegReqs"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsOutRegReqs"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsInDeregReqs"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsOutDeregReqs"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsRejects"))
)
if mibBuilder.loadTexts:
    t11FcsStatisticsGroup.setStatus("current")

t11FcsNotificationInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 162, 2, 2, 5)
)
t11FcsNotificationInfoGroup.setObjects(
      *(("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsReqRejectNotifyEnable"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsDiscoveryCompNotifyEnable"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsMgmtAddrChangeNotifyEnable"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsRejectCtCommandString"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsRejectRequestSource"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsRejectReasonCode"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsRejectReasonCodeExp"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsRejectReasonVendorCode"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsMgmtAddrChangeFabricIndex"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsMgmtAddrChangeIeName"))
)
if mibBuilder.loadTexts:
    t11FcsNotificationInfoGroup.setStatus("current")


# Notification objects

t11FcsRqRejectNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 162, 0, 1)
)
t11FcsRqRejectNotification.setObjects(
      *(("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamLocalSwitchWwn"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsRejectReasonCode"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsRejectReasonCodeExp"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsRejectReasonVendorCode"))
)
if mibBuilder.loadTexts:
    t11FcsRqRejectNotification.setStatus(
        "current"
    )

t11FcsDiscoveryCompleteNotify = NotificationType(
    (1, 3, 6, 1, 2, 1, 162, 0, 2)
)
t11FcsDiscoveryCompleteNotify.setObjects(
    ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsFabricDiscoveryRangeLow")
)
if mibBuilder.loadTexts:
    t11FcsDiscoveryCompleteNotify.setStatus(
        "current"
    )

t11FcsMgmtAddrChangeNotify = NotificationType(
    (1, 3, 6, 1, 2, 1, 162, 0, 3)
)
t11FcsMgmtAddrChangeNotify.setObjects(
      *(("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsMgmtAddrChangeFabricIndex"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsMgmtAddrChangeIeName"))
)
if mibBuilder.loadTexts:
    t11FcsMgmtAddrChangeNotify.setStatus(
        "current"
    )


# Notifications groups

t11FcsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 162, 2, 2, 6)
)
t11FcsNotificationGroup.setObjects(
      *(("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsRqRejectNotification"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsDiscoveryCompleteNotify"),
        ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsMgmtAddrChangeNotify"))
)
if mibBuilder.loadTexts:
    t11FcsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

t11FcsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 162, 2, 1, 1)
)
if mibBuilder.loadTexts:
    t11FcsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "T11-FC-FABRIC-CONFIG-SERVER-MIB",
    **{"T11FcListIndex": T11FcListIndex,
       "T11FcListIndexPointerOrZero": T11FcListIndexPointerOrZero,
       "T11FcIeType": T11FcIeType,
       "T11FcPortState": T11FcPortState,
       "T11FcPortTxType": T11FcPortTxType,
       "T11FcsRejectReasonExplanation": T11FcsRejectReasonExplanation,
       "t11FcFabricConfigServerMIB": t11FcFabricConfigServerMIB,
       "t11FcsNotifications": t11FcsNotifications,
       "t11FcsRqRejectNotification": t11FcsRqRejectNotification,
       "t11FcsDiscoveryCompleteNotify": t11FcsDiscoveryCompleteNotify,
       "t11FcsMgmtAddrChangeNotify": t11FcsMgmtAddrChangeNotify,
       "t11FcsMIBObjects": t11FcsMIBObjects,
       "t11FcsDiscovery": t11FcsDiscovery,
       "t11FcsFabricDiscoveryTable": t11FcsFabricDiscoveryTable,
       "t11FcsFabricDiscoveryEntry": t11FcsFabricDiscoveryEntry,
       "t11FcsFabricDiscoveryRangeLow": t11FcsFabricDiscoveryRangeLow,
       "t11FcsFabricDiscoveryRangeHigh": t11FcsFabricDiscoveryRangeHigh,
       "t11FcsFabricDiscoveryStart": t11FcsFabricDiscoveryStart,
       "t11FcsFabricDiscoveryTimeOut": t11FcsFabricDiscoveryTimeOut,
       "t11FcsDiscoveryStateTable": t11FcsDiscoveryStateTable,
       "t11FcsDiscoveryStateEntry": t11FcsDiscoveryStateEntry,
       "t11FcsFabricIndex": t11FcsFabricIndex,
       "t11FcsDiscoveryStatus": t11FcsDiscoveryStatus,
       "t11FcsDiscoveryCompleteTime": t11FcsDiscoveryCompleteTime,
       "t11FcsDiscoveredConfig": t11FcsDiscoveredConfig,
       "t11FcsIeTable": t11FcsIeTable,
       "t11FcsIeEntry": t11FcsIeEntry,
       "t11FcsIeName": t11FcsIeName,
       "t11FcsIeType": t11FcsIeType,
       "t11FcsIeDomainId": t11FcsIeDomainId,
       "t11FcsIeMgmtId": t11FcsIeMgmtId,
       "t11FcsIeFabricName": t11FcsIeFabricName,
       "t11FcsIeLogicalName": t11FcsIeLogicalName,
       "t11FcsIeMgmtAddrListIndex": t11FcsIeMgmtAddrListIndex,
       "t11FcsIeInfoList": t11FcsIeInfoList,
       "t11FcsMgmtAddrListTable": t11FcsMgmtAddrListTable,
       "t11FcsMgmtAddrListEntry": t11FcsMgmtAddrListEntry,
       "t11FcsMgmtAddrListIndex": t11FcsMgmtAddrListIndex,
       "t11FcsMgmtAddrIndex": t11FcsMgmtAddrIndex,
       "t11FcsMgmtAddr": t11FcsMgmtAddr,
       "t11FcsPortTable": t11FcsPortTable,
       "t11FcsPortEntry": t11FcsPortEntry,
       "t11FcsPortName": t11FcsPortName,
       "t11FcsPortType": t11FcsPortType,
       "t11FcsPortTxType": t11FcsPortTxType,
       "t11FcsPortModuleType": t11FcsPortModuleType,
       "t11FcsPortPhyPortNum": t11FcsPortPhyPortNum,
       "t11FcsPortAttachPortNameIndex": t11FcsPortAttachPortNameIndex,
       "t11FcsPortState": t11FcsPortState,
       "t11FcsPortSpeedCapab": t11FcsPortSpeedCapab,
       "t11FcsPortOperSpeed": t11FcsPortOperSpeed,
       "t11FcsPortZoningEnfStatus": t11FcsPortZoningEnfStatus,
       "t11FcsAttachPortNameListTable": t11FcsAttachPortNameListTable,
       "t11FcsAttachPortNameListEntry": t11FcsAttachPortNameListEntry,
       "t11FcsAttachPortNameListIndex": t11FcsAttachPortNameListIndex,
       "t11FcsAttachPortName": t11FcsAttachPortName,
       "t11FcsPlatformTable": t11FcsPlatformTable,
       "t11FcsPlatformEntry": t11FcsPlatformEntry,
       "t11FcsPlatformIndex": t11FcsPlatformIndex,
       "t11FcsPlatformName": t11FcsPlatformName,
       "t11FcsPlatformType": t11FcsPlatformType,
       "t11FcsPlatformNodeNameListIndex": t11FcsPlatformNodeNameListIndex,
       "t11FcsPlatformMgmtAddrListIndex": t11FcsPlatformMgmtAddrListIndex,
       "t11FcsPlatformVendorId": t11FcsPlatformVendorId,
       "t11FcsPlatformProductId": t11FcsPlatformProductId,
       "t11FcsPlatformProductRevLevel": t11FcsPlatformProductRevLevel,
       "t11FcsPlatformDescription": t11FcsPlatformDescription,
       "t11FcsPlatformLabel": t11FcsPlatformLabel,
       "t11FcsPlatformLocation": t11FcsPlatformLocation,
       "t11FcsPlatformSystemID": t11FcsPlatformSystemID,
       "t11FcsPlatformSysMgmtAddr": t11FcsPlatformSysMgmtAddr,
       "t11FcsPlatformClusterId": t11FcsPlatformClusterId,
       "t11FcsPlatformClusterMgmtAddr": t11FcsPlatformClusterMgmtAddr,
       "t11FcsPlatformFC4Types": t11FcsPlatformFC4Types,
       "t11FcsNodeNameListTable": t11FcsNodeNameListTable,
       "t11FcsNodeNameListEntry": t11FcsNodeNameListEntry,
       "t11FcsNodeNameListIndex": t11FcsNodeNameListIndex,
       "t11FcsNodeName": t11FcsNodeName,
       "t11FcsStats": t11FcsStats,
       "t11FcsStatsTable": t11FcsStatsTable,
       "t11FcsStatsEntry": t11FcsStatsEntry,
       "t11FcsInGetReqs": t11FcsInGetReqs,
       "t11FcsOutGetReqs": t11FcsOutGetReqs,
       "t11FcsInRegReqs": t11FcsInRegReqs,
       "t11FcsOutRegReqs": t11FcsOutRegReqs,
       "t11FcsInDeregReqs": t11FcsInDeregReqs,
       "t11FcsOutDeregReqs": t11FcsOutDeregReqs,
       "t11FcsRejects": t11FcsRejects,
       "t11FcsNotificationInfo": t11FcsNotificationInfo,
       "t11FcsNotifyControlTable": t11FcsNotifyControlTable,
       "t11FcsNotifyControlEntry": t11FcsNotifyControlEntry,
       "t11FcsReqRejectNotifyEnable": t11FcsReqRejectNotifyEnable,
       "t11FcsDiscoveryCompNotifyEnable": t11FcsDiscoveryCompNotifyEnable,
       "t11FcsMgmtAddrChangeNotifyEnable": t11FcsMgmtAddrChangeNotifyEnable,
       "t11FcsRejectCtCommandString": t11FcsRejectCtCommandString,
       "t11FcsRejectRequestSource": t11FcsRejectRequestSource,
       "t11FcsRejectReasonCode": t11FcsRejectReasonCode,
       "t11FcsRejectReasonCodeExp": t11FcsRejectReasonCodeExp,
       "t11FcsRejectReasonVendorCode": t11FcsRejectReasonVendorCode,
       "t11FcsMgmtAddrChangeFabricIndex": t11FcsMgmtAddrChangeFabricIndex,
       "t11FcsMgmtAddrChangeIeName": t11FcsMgmtAddrChangeIeName,
       "t11FcsMIBConformance": t11FcsMIBConformance,
       "t11FcsMIBCompliances": t11FcsMIBCompliances,
       "t11FcsMIBCompliance": t11FcsMIBCompliance,
       "t11FcsMIBGroups": t11FcsMIBGroups,
       "t11FcsDiscoveryControlGroup": t11FcsDiscoveryControlGroup,
       "t11FcsDiscoveryStatusGroup": t11FcsDiscoveryStatusGroup,
       "t11FcsDiscoveredConfigGroup": t11FcsDiscoveredConfigGroup,
       "t11FcsStatisticsGroup": t11FcsStatisticsGroup,
       "t11FcsNotificationInfoGroup": t11FcsNotificationInfoGroup,
       "t11FcsNotificationGroup": t11FcsNotificationGroup}
)
