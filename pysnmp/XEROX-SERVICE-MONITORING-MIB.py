"""SNMP MIB module (XEROX-SERVICE-MONITORING-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-SERVICE-MONITORING-MIB
Produced by pysmi-1.3.3 at Sun Mar 10 06:00:43 2024
On host MacBook-Pro.local platform Darwin version 23.4.0 by user lextm
Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]
"""
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

(hrDeviceIndex,
 ProductID) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "hrDeviceIndex",
    "ProductID")

(NotificationGroup,
 ModuleCompliance,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "NotificationGroup",
    "ModuleCompliance",
    "ObjectGroup")

(TimeTicks,
 Gauge32,
 Integer32,
 IpAddress,
 Bits,
 Counter32,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 NotificationType,
 ModuleIdentity,
 Counter64,
 MibIdentifier,
 Unsigned32,
 iso,
 ObjectIdentity) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "TimeTicks",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "Bits",
    "Counter32",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "ModuleIdentity",
    "Counter64",
    "MibIdentifier",
    "Unsigned32",
    "iso",
    "ObjectIdentity")

(RowStatus,
 DisplayString,
 DateAndTime,
 TruthValue,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "RowStatus",
    "DisplayString",
    "DateAndTime",
    "TruthValue",
    "TextualConvention")

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")

(XcmCommsMgmtState,
 XcmCommsMgmtConditions,
 XcmCommsStackExtProtocol) = mibBuilder.importSymbols(
    "XEROX-COMMS-ENGINE-TC",
    "XcmCommsMgmtState",
    "XcmCommsMgmtConditions",
    "XcmCommsStackExtProtocol")

(Ordinal32,
 XcmGenSNMPv2ErrorStatus,
 zeroDotZero,
 XcmFixedLocaleDisplayString,
 Cardinal32) = mibBuilder.importSymbols(
    "XEROX-GENERAL-TC",
    "Ordinal32",
    "XcmGenSNMPv2ErrorStatus",
    "zeroDotZero",
    "XcmFixedLocaleDisplayString",
    "Cardinal32")

(XcmHrDpaConditions,
 XcmHrDpaAvailability,
 XcmHrDpaState,
 XcmHrDevDetailUnitClass) = mibBuilder.importSymbols(
    "XEROX-HOST-RESOURCES-EXT-TC",
    "XcmHrDpaConditions",
    "XcmHrDpaAvailability",
    "XcmHrDpaState",
    "XcmHrDevDetailUnitClass")

(XcmSvcMonServiceMgmtOperation,
 XcmSvcMonGroupSupport,
 XcmSvcMonServiceDetailClass,
 XcmSvcMonServiceMgmtData,
 XcmSvcMonServiceDetailType,
 XcmSvcMonServiceType) = mibBuilder.importSymbols(
    "XEROX-SERVICE-MONITORING-TC",
    "XcmSvcMonServiceMgmtOperation",
    "XcmSvcMonGroupSupport",
    "XcmSvcMonServiceDetailClass",
    "XcmSvcMonServiceMgmtData",
    "XcmSvcMonServiceDetailType",
    "XcmSvcMonServiceType")


# MODULE-IDENTITY

xcmSvcMonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XcmSvcMonZeroDummy_ObjectIdentity = ObjectIdentity
xcmSvcMonZeroDummy = _XcmSvcMonZeroDummy_ObjectIdentity(
    (0, 0, 74)
)
_XcmSvcMonGeneral_ObjectIdentity = ObjectIdentity
xcmSvcMonGeneral = _XcmSvcMonGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 1)
)
_XcmSvcMonGeneralTable_Object = MibTable
xcmSvcMonGeneralTable = _XcmSvcMonGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 1, 2)
)
if mibBuilder.loadTexts:
    xcmSvcMonGeneralTable.setStatus("current")
_XcmSvcMonGeneralEntry_Object = MibTableRow
xcmSvcMonGeneralEntry = _XcmSvcMonGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 1, 2, 1)
)
xcmSvcMonGeneralEntry.setIndexNames(
    (0, "XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonGeneralIndex"),
)
if mibBuilder.loadTexts:
    xcmSvcMonGeneralEntry.setStatus("current")
_XcmSvcMonGeneralIndex_Type = Ordinal32
_XcmSvcMonGeneralIndex_Object = MibTableColumn
xcmSvcMonGeneralIndex = _XcmSvcMonGeneralIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 1, 2, 1, 1),
    _XcmSvcMonGeneralIndex_Type()
)
xcmSvcMonGeneralIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmSvcMonGeneralIndex.setStatus("current")
_XcmSvcMonGeneralRowStatus_Type = RowStatus
_XcmSvcMonGeneralRowStatus_Object = MibTableColumn
xcmSvcMonGeneralRowStatus = _XcmSvcMonGeneralRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 1, 2, 1, 2),
    _XcmSvcMonGeneralRowStatus_Type()
)
xcmSvcMonGeneralRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonGeneralRowStatus.setStatus("current")


class _XcmSvcMonGeneralVersionID_Type(ProductID):
    """Custom type xcmSvcMonGeneralVersionID based on ProductID"""
    defaultValue = "(0, 0)"


_XcmSvcMonGeneralVersionID_Object = MibTableColumn
xcmSvcMonGeneralVersionID = _XcmSvcMonGeneralVersionID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 1, 2, 1, 3),
    _XcmSvcMonGeneralVersionID_Type()
)
xcmSvcMonGeneralVersionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonGeneralVersionID.setStatus("current")


class _XcmSvcMonGeneralVersionDate_Type(DateAndTime):
    """Custom type xcmSvcMonGeneralVersionDate based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmSvcMonGeneralVersionDate_Object = MibTableColumn
xcmSvcMonGeneralVersionDate = _XcmSvcMonGeneralVersionDate_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 1, 2, 1, 4),
    _XcmSvcMonGeneralVersionDate_Type()
)
xcmSvcMonGeneralVersionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonGeneralVersionDate.setStatus("current")


class _XcmSvcMonGeneralGroupSupport_Type(XcmSvcMonGroupSupport):
    """Custom type xcmSvcMonGeneralGroupSupport based on XcmSvcMonGroupSupport"""
    defaultValue = 1


_XcmSvcMonGeneralGroupSupport_Object = MibTableColumn
xcmSvcMonGeneralGroupSupport = _XcmSvcMonGeneralGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 1, 2, 1, 5),
    _XcmSvcMonGeneralGroupSupport_Type()
)
xcmSvcMonGeneralGroupSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonGeneralGroupSupport.setStatus("current")
_XcmSvcMonGeneralCreateSupport_Type = XcmSvcMonGroupSupport
_XcmSvcMonGeneralCreateSupport_Object = MibTableColumn
xcmSvcMonGeneralCreateSupport = _XcmSvcMonGeneralCreateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 1, 2, 1, 6),
    _XcmSvcMonGeneralCreateSupport_Type()
)
xcmSvcMonGeneralCreateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonGeneralCreateSupport.setStatus("current")
_XcmSvcMonGeneralUpdateSupport_Type = XcmSvcMonGroupSupport
_XcmSvcMonGeneralUpdateSupport_Object = MibTableColumn
xcmSvcMonGeneralUpdateSupport = _XcmSvcMonGeneralUpdateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 1, 2, 1, 7),
    _XcmSvcMonGeneralUpdateSupport_Type()
)
xcmSvcMonGeneralUpdateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonGeneralUpdateSupport.setStatus("current")
_XcmSvcMonMIBConformance_ObjectIdentity = ObjectIdentity
xcmSvcMonMIBConformance = _XcmSvcMonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 2)
)
_XcmSvcMonMIBGroups_ObjectIdentity = ObjectIdentity
xcmSvcMonMIBGroups = _XcmSvcMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 2, 2)
)
_XcmSvcMonQueue_ObjectIdentity = ObjectIdentity
xcmSvcMonQueue = _XcmSvcMonQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 3)
)
_XcmSvcMonQueueTable_Object = MibTable
xcmSvcMonQueueTable = _XcmSvcMonQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 3, 2)
)
if mibBuilder.loadTexts:
    xcmSvcMonQueueTable.setStatus("current")
_XcmSvcMonQueueEntry_Object = MibTableRow
xcmSvcMonQueueEntry = _XcmSvcMonQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 3, 2, 1)
)
xcmSvcMonQueueEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueIndex"),
)
if mibBuilder.loadTexts:
    xcmSvcMonQueueEntry.setStatus("current")
_XcmSvcMonQueueIndex_Type = Ordinal32
_XcmSvcMonQueueIndex_Object = MibTableColumn
xcmSvcMonQueueIndex = _XcmSvcMonQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 3, 2, 1, 1),
    _XcmSvcMonQueueIndex_Type()
)
xcmSvcMonQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonQueueIndex.setStatus("current")
_XcmSvcMonQueueRowStatus_Type = RowStatus
_XcmSvcMonQueueRowStatus_Object = MibTableColumn
xcmSvcMonQueueRowStatus = _XcmSvcMonQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 3, 2, 1, 2),
    _XcmSvcMonQueueRowStatus_Type()
)
xcmSvcMonQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonQueueRowStatus.setStatus("current")


class _XcmSvcMonQueueDomain_Type(XcmCommsStackExtProtocol):
    """Custom type xcmSvcMonQueueDomain based on XcmCommsStackExtProtocol"""


_XcmSvcMonQueueDomain_Object = MibTableColumn
xcmSvcMonQueueDomain = _XcmSvcMonQueueDomain_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 3, 2, 1, 3),
    _XcmSvcMonQueueDomain_Type()
)
xcmSvcMonQueueDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonQueueDomain.setStatus("current")


class _XcmSvcMonQueuePath_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmSvcMonQueuePath based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmSvcMonQueuePath_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmSvcMonQueuePath_Object = MibTableColumn
xcmSvcMonQueuePath = _XcmSvcMonQueuePath_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 3, 2, 1, 4),
    _XcmSvcMonQueuePath_Type()
)
xcmSvcMonQueuePath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonQueuePath.setStatus("current")


class _XcmSvcMonQueueName_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmSvcMonQueueName based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmSvcMonQueueName_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmSvcMonQueueName_Object = MibTableColumn
xcmSvcMonQueueName = _XcmSvcMonQueueName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 3, 2, 1, 5),
    _XcmSvcMonQueueName_Type()
)
xcmSvcMonQueueName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonQueueName.setStatus("current")


class _XcmSvcMonQueueOnSystem_Type(TruthValue):
    """Custom type xcmSvcMonQueueOnSystem based on TruthValue"""


_XcmSvcMonQueueOnSystem_Object = MibTableColumn
xcmSvcMonQueueOnSystem = _XcmSvcMonQueueOnSystem_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 3, 2, 1, 6),
    _XcmSvcMonQueueOnSystem_Type()
)
xcmSvcMonQueueOnSystem.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonQueueOnSystem.setStatus("current")
_XcmSvcMonQueueExt_ObjectIdentity = ObjectIdentity
xcmSvcMonQueueExt = _XcmSvcMonQueueExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4)
)
_XcmSvcMonQueueExtV1EventOID_ObjectIdentity = ObjectIdentity
xcmSvcMonQueueExtV1EventOID = _XcmSvcMonQueueExtV1EventOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 1)
)
if mibBuilder.loadTexts:
    xcmSvcMonQueueExtV1EventOID.setStatus("current")
_XcmSvcMonQueueExtV2EventPrefix_ObjectIdentity = ObjectIdentity
xcmSvcMonQueueExtV2EventPrefix = _XcmSvcMonQueueExtV2EventPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 1, 0)
)
_XcmSvcMonQueueExtTable_Object = MibTable
xcmSvcMonQueueExtTable = _XcmSvcMonQueueExtTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 2)
)
if mibBuilder.loadTexts:
    xcmSvcMonQueueExtTable.setStatus("current")
_XcmSvcMonQueueExtEntry_Object = MibTableRow
xcmSvcMonQueueExtEntry = _XcmSvcMonQueueExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 2, 1)
)
xcmSvcMonQueueEntry.registerAugmentions(
    ("XEROX-SERVICE-MONITORING-MIB",
     "xcmSvcMonQueueExtEntry")
)
xcmSvcMonQueueExtEntry.setIndexNames(*xcmSvcMonQueueEntry.getIndexNames())
if mibBuilder.loadTexts:
    xcmSvcMonQueueExtEntry.setStatus("current")
_XcmSvcMonQueueRoutingIndex_Type = Cardinal32
_XcmSvcMonQueueRoutingIndex_Object = MibTableColumn
xcmSvcMonQueueRoutingIndex = _XcmSvcMonQueueRoutingIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 2, 1, 1),
    _XcmSvcMonQueueRoutingIndex_Type()
)
xcmSvcMonQueueRoutingIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonQueueRoutingIndex.setStatus("current")


class _XcmSvcMonQueueState_Type(XcmCommsMgmtState):
    """Custom type xcmSvcMonQueueState based on XcmCommsMgmtState"""


_XcmSvcMonQueueState_Object = MibTableColumn
xcmSvcMonQueueState = _XcmSvcMonQueueState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 2, 1, 2),
    _XcmSvcMonQueueState_Type()
)
xcmSvcMonQueueState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonQueueState.setStatus("current")
_XcmSvcMonQueueConditions_Type = XcmCommsMgmtConditions
_XcmSvcMonQueueConditions_Object = MibTableColumn
xcmSvcMonQueueConditions = _XcmSvcMonQueueConditions_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 2, 1, 3),
    _XcmSvcMonQueueConditions_Type()
)
xcmSvcMonQueueConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonQueueConditions.setStatus("current")
_XcmSvcMonQueueFaultCount_Type = Counter32
_XcmSvcMonQueueFaultCount_Object = MibTableColumn
xcmSvcMonQueueFaultCount = _XcmSvcMonQueueFaultCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 2, 1, 4),
    _XcmSvcMonQueueFaultCount_Type()
)
xcmSvcMonQueueFaultCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonQueueFaultCount.setStatus("current")
_XcmSvcMonQueueFaultCode_Type = Integer32
_XcmSvcMonQueueFaultCode_Object = MibTableColumn
xcmSvcMonQueueFaultCode = _XcmSvcMonQueueFaultCode_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 2, 1, 5),
    _XcmSvcMonQueueFaultCode_Type()
)
xcmSvcMonQueueFaultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonQueueFaultCode.setStatus("current")


class _XcmSvcMonQueueFaultString_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmSvcMonQueueFaultString based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmSvcMonQueueFaultString_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmSvcMonQueueFaultString_Object = MibTableColumn
xcmSvcMonQueueFaultString = _XcmSvcMonQueueFaultString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 2, 1, 6),
    _XcmSvcMonQueueFaultString_Type()
)
xcmSvcMonQueueFaultString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonQueueFaultString.setStatus("current")


class _XcmSvcMonQueueRowCreateDate_Type(DateAndTime):
    """Custom type xcmSvcMonQueueRowCreateDate based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmSvcMonQueueRowCreateDate_Object = MibTableColumn
xcmSvcMonQueueRowCreateDate = _XcmSvcMonQueueRowCreateDate_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 2, 1, 7),
    _XcmSvcMonQueueRowCreateDate_Type()
)
xcmSvcMonQueueRowCreateDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonQueueRowCreateDate.setStatus("current")
_XcmSvcMonQueueRowTotalJobs_Type = Counter32
_XcmSvcMonQueueRowTotalJobs_Object = MibTableColumn
xcmSvcMonQueueRowTotalJobs = _XcmSvcMonQueueRowTotalJobs_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 2, 1, 8),
    _XcmSvcMonQueueRowTotalJobs_Type()
)
xcmSvcMonQueueRowTotalJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonQueueRowTotalJobs.setStatus("current")


class _XcmSvcMonQueueLastConnectDate_Type(DateAndTime):
    """Custom type xcmSvcMonQueueLastConnectDate based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmSvcMonQueueLastConnectDate_Object = MibTableColumn
xcmSvcMonQueueLastConnectDate = _XcmSvcMonQueueLastConnectDate_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 2, 1, 9),
    _XcmSvcMonQueueLastConnectDate_Type()
)
xcmSvcMonQueueLastConnectDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonQueueLastConnectDate.setStatus("current")
_XcmSvcMonQueueLastConnectJobs_Type = Counter32
_XcmSvcMonQueueLastConnectJobs_Object = MibTableColumn
xcmSvcMonQueueLastConnectJobs = _XcmSvcMonQueueLastConnectJobs_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 2, 1, 10),
    _XcmSvcMonQueueLastConnectJobs_Type()
)
xcmSvcMonQueueLastConnectJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonQueueLastConnectJobs.setStatus("current")
_XcmSvcMonService_ObjectIdentity = ObjectIdentity
xcmSvcMonService = _XcmSvcMonService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5)
)
_XcmSvcMonServiceV1EventOID_ObjectIdentity = ObjectIdentity
xcmSvcMonServiceV1EventOID = _XcmSvcMonServiceV1EventOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 1)
)
if mibBuilder.loadTexts:
    xcmSvcMonServiceV1EventOID.setStatus("current")
_XcmSvcMonServiceV2EventPrefix_ObjectIdentity = ObjectIdentity
xcmSvcMonServiceV2EventPrefix = _XcmSvcMonServiceV2EventPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 1, 0)
)
_XcmSvcMonServiceTable_Object = MibTable
xcmSvcMonServiceTable = _XcmSvcMonServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2)
)
if mibBuilder.loadTexts:
    xcmSvcMonServiceTable.setStatus("current")
_XcmSvcMonServiceEntry_Object = MibTableRow
xcmSvcMonServiceEntry = _XcmSvcMonServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1)
)
xcmSvcMonServiceEntry.setIndexNames(
    (0, "XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceIndex"),
)
if mibBuilder.loadTexts:
    xcmSvcMonServiceEntry.setStatus("current")
_XcmSvcMonServiceIndex_Type = Ordinal32
_XcmSvcMonServiceIndex_Object = MibTableColumn
xcmSvcMonServiceIndex = _XcmSvcMonServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 1),
    _XcmSvcMonServiceIndex_Type()
)
xcmSvcMonServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonServiceIndex.setStatus("current")
_XcmSvcMonServiceRowStatus_Type = RowStatus
_XcmSvcMonServiceRowStatus_Object = MibTableColumn
xcmSvcMonServiceRowStatus = _XcmSvcMonServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 2),
    _XcmSvcMonServiceRowStatus_Type()
)
xcmSvcMonServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceRowStatus.setStatus("current")


class _XcmSvcMonServiceName_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmSvcMonServiceName based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmSvcMonServiceName_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmSvcMonServiceName_Object = MibTableColumn
xcmSvcMonServiceName = _XcmSvcMonServiceName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 3),
    _XcmSvcMonServiceName_Type()
)
xcmSvcMonServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceName.setStatus("current")


class _XcmSvcMonServiceCurrentState_Type(XcmHrDpaState):
    """Custom type xcmSvcMonServiceCurrentState based on XcmHrDpaState"""


_XcmSvcMonServiceCurrentState_Object = MibTableColumn
xcmSvcMonServiceCurrentState = _XcmSvcMonServiceCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 4),
    _XcmSvcMonServiceCurrentState_Type()
)
xcmSvcMonServiceCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonServiceCurrentState.setStatus("current")


class _XcmSvcMonServicePreviousState_Type(XcmHrDpaState):
    """Custom type xcmSvcMonServicePreviousState based on XcmHrDpaState"""


_XcmSvcMonServicePreviousState_Object = MibTableColumn
xcmSvcMonServicePreviousState = _XcmSvcMonServicePreviousState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 5),
    _XcmSvcMonServicePreviousState_Type()
)
xcmSvcMonServicePreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonServicePreviousState.setStatus("current")
_XcmSvcMonServiceConditions_Type = XcmHrDpaConditions
_XcmSvcMonServiceConditions_Object = MibTableColumn
xcmSvcMonServiceConditions = _XcmSvcMonServiceConditions_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 6),
    _XcmSvcMonServiceConditions_Type()
)
xcmSvcMonServiceConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonServiceConditions.setStatus("current")


class _XcmSvcMonServiceAvailability_Type(XcmHrDpaAvailability):
    """Custom type xcmSvcMonServiceAvailability based on XcmHrDpaAvailability"""


_XcmSvcMonServiceAvailability_Object = MibTableColumn
xcmSvcMonServiceAvailability = _XcmSvcMonServiceAvailability_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 7),
    _XcmSvcMonServiceAvailability_Type()
)
xcmSvcMonServiceAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonServiceAvailability.setStatus("current")
_XcmSvcMonServicePhysicalDevice_Type = Cardinal32
_XcmSvcMonServicePhysicalDevice_Object = MibTableColumn
xcmSvcMonServicePhysicalDevice = _XcmSvcMonServicePhysicalDevice_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 8),
    _XcmSvcMonServicePhysicalDevice_Type()
)
xcmSvcMonServicePhysicalDevice.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServicePhysicalDevice.setStatus("current")
_XcmSvcMonServiceLogicalDevice_Type = Cardinal32
_XcmSvcMonServiceLogicalDevice_Object = MibTableColumn
xcmSvcMonServiceLogicalDevice = _XcmSvcMonServiceLogicalDevice_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 9),
    _XcmSvcMonServiceLogicalDevice_Type()
)
xcmSvcMonServiceLogicalDevice.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceLogicalDevice.setStatus("current")
_XcmSvcMonServiceExternalDevice_Type = Cardinal32
_XcmSvcMonServiceExternalDevice_Object = MibTableColumn
xcmSvcMonServiceExternalDevice = _XcmSvcMonServiceExternalDevice_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 10),
    _XcmSvcMonServiceExternalDevice_Type()
)
xcmSvcMonServiceExternalDevice.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceExternalDevice.setStatus("current")
_XcmSvcMonServiceSWRun_Type = Cardinal32
_XcmSvcMonServiceSWRun_Object = MibTableColumn
xcmSvcMonServiceSWRun = _XcmSvcMonServiceSWRun_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 11),
    _XcmSvcMonServiceSWRun_Type()
)
xcmSvcMonServiceSWRun.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceSWRun.setStatus("current")
_XcmSvcMonServiceSWInstalled_Type = Cardinal32
_XcmSvcMonServiceSWInstalled_Object = MibTableColumn
xcmSvcMonServiceSWInstalled = _XcmSvcMonServiceSWInstalled_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 12),
    _XcmSvcMonServiceSWInstalled_Type()
)
xcmSvcMonServiceSWInstalled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceSWInstalled.setStatus("current")
_XcmSvcMonServiceStorage_Type = Cardinal32
_XcmSvcMonServiceStorage_Object = MibTableColumn
xcmSvcMonServiceStorage = _XcmSvcMonServiceStorage_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 13),
    _XcmSvcMonServiceStorage_Type()
)
xcmSvcMonServiceStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceStorage.setStatus("current")


class _XcmSvcMonServicePriority_Type(Integer32):
    """Custom type xcmSvcMonServicePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XcmSvcMonServicePriority_Type.__name__ = "Integer32"
_XcmSvcMonServicePriority_Object = MibTableColumn
xcmSvcMonServicePriority = _XcmSvcMonServicePriority_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 14),
    _XcmSvcMonServicePriority_Type()
)
xcmSvcMonServicePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServicePriority.setStatus("current")


class _XcmSvcMonServiceType_Type(XcmSvcMonServiceType):
    """Custom type xcmSvcMonServiceType based on XcmSvcMonServiceType"""


_XcmSvcMonServiceType_Object = MibTableColumn
xcmSvcMonServiceType = _XcmSvcMonServiceType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 15),
    _XcmSvcMonServiceType_Type()
)
xcmSvcMonServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceType.setStatus("current")


class _XcmSvcMonServiceStateDetail_Type(OctetString):
    """Custom type xcmSvcMonServiceStateDetail based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_XcmSvcMonServiceStateDetail_Type.__name__ = "OctetString"
_XcmSvcMonServiceStateDetail_Object = MibTableColumn
xcmSvcMonServiceStateDetail = _XcmSvcMonServiceStateDetail_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 16),
    _XcmSvcMonServiceStateDetail_Type()
)
xcmSvcMonServiceStateDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonServiceStateDetail.setStatus("current")
_XcmSvcMonServiceDetail_ObjectIdentity = ObjectIdentity
xcmSvcMonServiceDetail = _XcmSvcMonServiceDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 6)
)
_XcmSvcMonServiceDetailTable_Object = MibTable
xcmSvcMonServiceDetailTable = _XcmSvcMonServiceDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 6, 2)
)
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailTable.setStatus("current")
_XcmSvcMonServiceDetailEntry_Object = MibTableRow
xcmSvcMonServiceDetailEntry = _XcmSvcMonServiceDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 6, 2, 1)
)
xcmSvcMonServiceDetailEntry.setIndexNames(
    (0, "XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceIndex"),
    (0, "XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceDetailClass"),
    (0, "XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceDetailType"),
    (0, "XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceDetailIndex"),
)
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailEntry.setStatus("current")
_XcmSvcMonServiceDetailClass_Type = XcmSvcMonServiceDetailClass
_XcmSvcMonServiceDetailClass_Object = MibTableColumn
xcmSvcMonServiceDetailClass = _XcmSvcMonServiceDetailClass_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 6, 2, 1, 1),
    _XcmSvcMonServiceDetailClass_Type()
)
xcmSvcMonServiceDetailClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailClass.setStatus("current")
_XcmSvcMonServiceDetailType_Type = XcmSvcMonServiceDetailType
_XcmSvcMonServiceDetailType_Object = MibTableColumn
xcmSvcMonServiceDetailType = _XcmSvcMonServiceDetailType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 6, 2, 1, 2),
    _XcmSvcMonServiceDetailType_Type()
)
xcmSvcMonServiceDetailType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailType.setStatus("current")
_XcmSvcMonServiceDetailIndex_Type = Ordinal32
_XcmSvcMonServiceDetailIndex_Object = MibTableColumn
xcmSvcMonServiceDetailIndex = _XcmSvcMonServiceDetailIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 6, 2, 1, 3),
    _XcmSvcMonServiceDetailIndex_Type()
)
xcmSvcMonServiceDetailIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailIndex.setStatus("current")
_XcmSvcMonServiceDetailRowStatus_Type = RowStatus
_XcmSvcMonServiceDetailRowStatus_Object = MibTableColumn
xcmSvcMonServiceDetailRowStatus = _XcmSvcMonServiceDetailRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 6, 2, 1, 4),
    _XcmSvcMonServiceDetailRowStatus_Type()
)
xcmSvcMonServiceDetailRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailRowStatus.setStatus("current")


class _XcmSvcMonServiceDetailUnitClass_Type(XcmHrDevDetailUnitClass):
    """Custom type xcmSvcMonServiceDetailUnitClass based on XcmHrDevDetailUnitClass"""


_XcmSvcMonServiceDetailUnitClass_Object = MibTableColumn
xcmSvcMonServiceDetailUnitClass = _XcmSvcMonServiceDetailUnitClass_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 6, 2, 1, 5),
    _XcmSvcMonServiceDetailUnitClass_Type()
)
xcmSvcMonServiceDetailUnitClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailUnitClass.setStatus("current")
_XcmSvcMonServiceDetailUnit_Type = Cardinal32
_XcmSvcMonServiceDetailUnit_Object = MibTableColumn
xcmSvcMonServiceDetailUnit = _XcmSvcMonServiceDetailUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 6, 2, 1, 6),
    _XcmSvcMonServiceDetailUnit_Type()
)
xcmSvcMonServiceDetailUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailUnit.setStatus("current")
_XcmSvcMonServiceDetailInteger_Type = Integer32
_XcmSvcMonServiceDetailInteger_Object = MibTableColumn
xcmSvcMonServiceDetailInteger = _XcmSvcMonServiceDetailInteger_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 6, 2, 1, 7),
    _XcmSvcMonServiceDetailInteger_Type()
)
xcmSvcMonServiceDetailInteger.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailInteger.setStatus("current")


class _XcmSvcMonServiceDetailOID_Type(ObjectIdentifier):
    """Custom type xcmSvcMonServiceDetailOID based on ObjectIdentifier"""
    defaultValue = "(0, 0)"


_XcmSvcMonServiceDetailOID_Object = MibTableColumn
xcmSvcMonServiceDetailOID = _XcmSvcMonServiceDetailOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 6, 2, 1, 8),
    _XcmSvcMonServiceDetailOID_Type()
)
xcmSvcMonServiceDetailOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailOID.setStatus("current")


class _XcmSvcMonServiceDetailString_Type(OctetString):
    """Custom type xcmSvcMonServiceDetailString based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmSvcMonServiceDetailString_Type.__name__ = "OctetString"
_XcmSvcMonServiceDetailString_Object = MibTableColumn
xcmSvcMonServiceDetailString = _XcmSvcMonServiceDetailString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 6, 2, 1, 9),
    _XcmSvcMonServiceDetailString_Type()
)
xcmSvcMonServiceDetailString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailString.setStatus("current")
_XcmSvcMonServiceMgmt_ObjectIdentity = ObjectIdentity
xcmSvcMonServiceMgmt = _XcmSvcMonServiceMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 7)
)
_XcmSvcMonServiceMgmtV1EventOID_ObjectIdentity = ObjectIdentity
xcmSvcMonServiceMgmtV1EventOID = _XcmSvcMonServiceMgmtV1EventOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 7, 1)
)
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtV1EventOID.setStatus("current")
_XcmSvcMonServiceMgmtV2EventPrefix_ObjectIdentity = ObjectIdentity
xcmSvcMonServiceMgmtV2EventPrefix = _XcmSvcMonServiceMgmtV2EventPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 7, 1, 0)
)
_XcmSvcMonServiceMgmtTable_Object = MibTable
xcmSvcMonServiceMgmtTable = _XcmSvcMonServiceMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 7, 2)
)
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtTable.setStatus("current")
_XcmSvcMonServiceMgmtEntry_Object = MibTableRow
xcmSvcMonServiceMgmtEntry = _XcmSvcMonServiceMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 7, 2, 1)
)
xcmSvcMonServiceEntry.registerAugmentions(
    ("XEROX-SERVICE-MONITORING-MIB",
     "xcmSvcMonServiceMgmtEntry")
)
xcmSvcMonServiceMgmtEntry.setIndexNames(*xcmSvcMonServiceEntry.getIndexNames())
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtEntry.setStatus("current")
_XcmSvcMonServiceMgmtOperation_Type = XcmSvcMonServiceMgmtOperation
_XcmSvcMonServiceMgmtOperation_Object = MibTableColumn
xcmSvcMonServiceMgmtOperation = _XcmSvcMonServiceMgmtOperation_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 7, 2, 1, 1),
    _XcmSvcMonServiceMgmtOperation_Type()
)
xcmSvcMonServiceMgmtOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtOperation.setStatus("current")


class _XcmSvcMonServiceMgmtData_Type(XcmSvcMonServiceMgmtData):
    """Custom type xcmSvcMonServiceMgmtData based on XcmSvcMonServiceMgmtData"""
    defaultHexValue = ""

    subtypeSpec = XcmSvcMonServiceMgmtData.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmSvcMonServiceMgmtData_Type.__name__ = "XcmSvcMonServiceMgmtData"
_XcmSvcMonServiceMgmtData_Object = MibTableColumn
xcmSvcMonServiceMgmtData = _XcmSvcMonServiceMgmtData_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 7, 2, 1, 2),
    _XcmSvcMonServiceMgmtData_Type()
)
xcmSvcMonServiceMgmtData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtData.setStatus("current")
_XcmSvcMonServiceMgmtStatus_Type = XcmGenSNMPv2ErrorStatus
_XcmSvcMonServiceMgmtStatus_Object = MibTableColumn
xcmSvcMonServiceMgmtStatus = _XcmSvcMonServiceMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 7, 2, 1, 3),
    _XcmSvcMonServiceMgmtStatus_Type()
)
xcmSvcMonServiceMgmtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtStatus.setStatus("current")


class _XcmSvcMonServiceMgmtInProgress_Type(TruthValue):
    """Custom type xcmSvcMonServiceMgmtInProgress based on TruthValue"""


_XcmSvcMonServiceMgmtInProgress_Object = MibTableColumn
xcmSvcMonServiceMgmtInProgress = _XcmSvcMonServiceMgmtInProgress_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 7, 2, 1, 4),
    _XcmSvcMonServiceMgmtInProgress_Type()
)
xcmSvcMonServiceMgmtInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtInProgress.setStatus("current")
_XcmSvcMonServiceMgmtRowStatus_Type = RowStatus
_XcmSvcMonServiceMgmtRowStatus_Object = MibTableColumn
xcmSvcMonServiceMgmtRowStatus = _XcmSvcMonServiceMgmtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 7, 2, 1, 5),
    _XcmSvcMonServiceMgmtRowStatus_Type()
)
xcmSvcMonServiceMgmtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtRowStatus.setStatus("current")


class _XcmSvcMonServiceMgmtUserPassword_Type(OctetString):
    """Custom type xcmSvcMonServiceMgmtUserPassword based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmSvcMonServiceMgmtUserPassword_Type.__name__ = "OctetString"
_XcmSvcMonServiceMgmtUserPassword_Object = MibTableColumn
xcmSvcMonServiceMgmtUserPassword = _XcmSvcMonServiceMgmtUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 7, 2, 1, 6),
    _XcmSvcMonServiceMgmtUserPassword_Type()
)
xcmSvcMonServiceMgmtUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtUserPassword.setStatus("current")


class _XcmSvcMonServiceMgmtOperatorPassword_Type(OctetString):
    """Custom type xcmSvcMonServiceMgmtOperatorPassword based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmSvcMonServiceMgmtOperatorPassword_Type.__name__ = "OctetString"
_XcmSvcMonServiceMgmtOperatorPassword_Object = MibTableColumn
xcmSvcMonServiceMgmtOperatorPassword = _XcmSvcMonServiceMgmtOperatorPassword_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 7, 2, 1, 7),
    _XcmSvcMonServiceMgmtOperatorPassword_Type()
)
xcmSvcMonServiceMgmtOperatorPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtOperatorPassword.setStatus("current")


class _XcmSvcMonServiceMgmtAdminPassword_Type(OctetString):
    """Custom type xcmSvcMonServiceMgmtAdminPassword based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmSvcMonServiceMgmtAdminPassword_Type.__name__ = "OctetString"
_XcmSvcMonServiceMgmtAdminPassword_Object = MibTableColumn
xcmSvcMonServiceMgmtAdminPassword = _XcmSvcMonServiceMgmtAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 7, 2, 1, 8),
    _XcmSvcMonServiceMgmtAdminPassword_Type()
)
xcmSvcMonServiceMgmtAdminPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtAdminPassword.setStatus("current")

# Managed Objects groups

xcmSvcMonGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 2, 2, 1)
)
xcmSvcMonGeneralGroup.setObjects(
      *(("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonGeneralRowStatus"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonGeneralVersionID"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonGeneralVersionDate"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonGeneralGroupSupport"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonGeneralCreateSupport"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonGeneralUpdateSupport"))
)
if mibBuilder.loadTexts:
    xcmSvcMonGeneralGroup.setStatus("current")

xcmSvcMonQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 2, 2, 3)
)
xcmSvcMonQueueGroup.setObjects(
      *(("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueIndex"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueRowStatus"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueDomain"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueuePath"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueName"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueOnSystem"))
)
if mibBuilder.loadTexts:
    xcmSvcMonQueueGroup.setStatus("current")

xcmSvcMonQueueExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 2, 2, 4)
)
xcmSvcMonQueueExtGroup.setObjects(
      *(("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueRoutingIndex"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueState"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueConditions"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueFaultCount"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueFaultCode"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueFaultString"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueRowCreateDate"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueRowTotalJobs"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueLastConnectDate"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueLastConnectJobs"))
)
if mibBuilder.loadTexts:
    xcmSvcMonQueueExtGroup.setStatus("current")

xcmSvcMonServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 2, 2, 5)
)
xcmSvcMonServiceGroup.setObjects(
      *(("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceIndex"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceRowStatus"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceName"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceCurrentState"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServicePreviousState"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceConditions"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceAvailability"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServicePhysicalDevice"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceLogicalDevice"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceExternalDevice"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceSWRun"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceSWInstalled"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceStorage"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServicePriority"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceType"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceStateDetail"))
)
if mibBuilder.loadTexts:
    xcmSvcMonServiceGroup.setStatus("current")

xcmSvcMonServiceDetailGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 2, 2, 6)
)
xcmSvcMonServiceDetailGroup.setObjects(
      *(("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceDetailRowStatus"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceDetailUnitClass"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceDetailUnit"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceDetailInteger"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceDetailOID"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceDetailString"))
)
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailGroup.setStatus("current")

xcmSvcMonServiceMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 2, 2, 7)
)
xcmSvcMonServiceMgmtGroup.setObjects(
      *(("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceMgmtOperation"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceMgmtData"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceMgmtStatus"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceMgmtInProgress"))
)
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtGroup.setStatus("current")


# Notification objects

xcmSvcMonQueueExtV2Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 1, 0, 1)
)
xcmSvcMonQueueExtV2Event.setObjects(
      *(("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueIndex"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueOnSystem"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueState"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueConditions"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueFaultCount"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueFaultCode"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueFaultString"))
)
if mibBuilder.loadTexts:
    xcmSvcMonQueueExtV2Event.setStatus(
        "current"
    )

xcmSvcMonServiceV2Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 1, 0, 1)
)
xcmSvcMonServiceV2Event.setObjects(
      *(("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceIndex"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceCurrentState"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServicePreviousState"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceConditions"))
)
if mibBuilder.loadTexts:
    xcmSvcMonServiceV2Event.setStatus(
        "current"
    )

xcmSvcMonServiceMgmtV2Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 7, 1, 0, 1)
)
xcmSvcMonServiceMgmtV2Event.setObjects(
      *(("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceIndex"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceMgmtOperation"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceMgmtStatus"))
)
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtV2Event.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

xcmSvcMonMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 2, 3)
)
if mibBuilder.loadTexts:
    xcmSvcMonMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-SERVICE-MONITORING-MIB",
    **{"xcmSvcMonZeroDummy": xcmSvcMonZeroDummy,
       "xcmSvcMonMIB": xcmSvcMonMIB,
       "xcmSvcMonGeneral": xcmSvcMonGeneral,
       "xcmSvcMonGeneralTable": xcmSvcMonGeneralTable,
       "xcmSvcMonGeneralEntry": xcmSvcMonGeneralEntry,
       "xcmSvcMonGeneralIndex": xcmSvcMonGeneralIndex,
       "xcmSvcMonGeneralRowStatus": xcmSvcMonGeneralRowStatus,
       "xcmSvcMonGeneralVersionID": xcmSvcMonGeneralVersionID,
       "xcmSvcMonGeneralVersionDate": xcmSvcMonGeneralVersionDate,
       "xcmSvcMonGeneralGroupSupport": xcmSvcMonGeneralGroupSupport,
       "xcmSvcMonGeneralCreateSupport": xcmSvcMonGeneralCreateSupport,
       "xcmSvcMonGeneralUpdateSupport": xcmSvcMonGeneralUpdateSupport,
       "xcmSvcMonMIBConformance": xcmSvcMonMIBConformance,
       "xcmSvcMonMIBGroups": xcmSvcMonMIBGroups,
       "xcmSvcMonGeneralGroup": xcmSvcMonGeneralGroup,
       "xcmSvcMonQueueGroup": xcmSvcMonQueueGroup,
       "xcmSvcMonQueueExtGroup": xcmSvcMonQueueExtGroup,
       "xcmSvcMonServiceGroup": xcmSvcMonServiceGroup,
       "xcmSvcMonServiceDetailGroup": xcmSvcMonServiceDetailGroup,
       "xcmSvcMonServiceMgmtGroup": xcmSvcMonServiceMgmtGroup,
       "xcmSvcMonMIBCompliance": xcmSvcMonMIBCompliance,
       "xcmSvcMonQueue": xcmSvcMonQueue,
       "xcmSvcMonQueueTable": xcmSvcMonQueueTable,
       "xcmSvcMonQueueEntry": xcmSvcMonQueueEntry,
       "xcmSvcMonQueueIndex": xcmSvcMonQueueIndex,
       "xcmSvcMonQueueRowStatus": xcmSvcMonQueueRowStatus,
       "xcmSvcMonQueueDomain": xcmSvcMonQueueDomain,
       "xcmSvcMonQueuePath": xcmSvcMonQueuePath,
       "xcmSvcMonQueueName": xcmSvcMonQueueName,
       "xcmSvcMonQueueOnSystem": xcmSvcMonQueueOnSystem,
       "xcmSvcMonQueueExt": xcmSvcMonQueueExt,
       "xcmSvcMonQueueExtV1EventOID": xcmSvcMonQueueExtV1EventOID,
       "xcmSvcMonQueueExtV2EventPrefix": xcmSvcMonQueueExtV2EventPrefix,
       "xcmSvcMonQueueExtV2Event": xcmSvcMonQueueExtV2Event,
       "xcmSvcMonQueueExtTable": xcmSvcMonQueueExtTable,
       "xcmSvcMonQueueExtEntry": xcmSvcMonQueueExtEntry,
       "xcmSvcMonQueueRoutingIndex": xcmSvcMonQueueRoutingIndex,
       "xcmSvcMonQueueState": xcmSvcMonQueueState,
       "xcmSvcMonQueueConditions": xcmSvcMonQueueConditions,
       "xcmSvcMonQueueFaultCount": xcmSvcMonQueueFaultCount,
       "xcmSvcMonQueueFaultCode": xcmSvcMonQueueFaultCode,
       "xcmSvcMonQueueFaultString": xcmSvcMonQueueFaultString,
       "xcmSvcMonQueueRowCreateDate": xcmSvcMonQueueRowCreateDate,
       "xcmSvcMonQueueRowTotalJobs": xcmSvcMonQueueRowTotalJobs,
       "xcmSvcMonQueueLastConnectDate": xcmSvcMonQueueLastConnectDate,
       "xcmSvcMonQueueLastConnectJobs": xcmSvcMonQueueLastConnectJobs,
       "xcmSvcMonService": xcmSvcMonService,
       "xcmSvcMonServiceV1EventOID": xcmSvcMonServiceV1EventOID,
       "xcmSvcMonServiceV2EventPrefix": xcmSvcMonServiceV2EventPrefix,
       "xcmSvcMonServiceV2Event": xcmSvcMonServiceV2Event,
       "xcmSvcMonServiceTable": xcmSvcMonServiceTable,
       "xcmSvcMonServiceEntry": xcmSvcMonServiceEntry,
       "xcmSvcMonServiceIndex": xcmSvcMonServiceIndex,
       "xcmSvcMonServiceRowStatus": xcmSvcMonServiceRowStatus,
       "xcmSvcMonServiceName": xcmSvcMonServiceName,
       "xcmSvcMonServiceCurrentState": xcmSvcMonServiceCurrentState,
       "xcmSvcMonServicePreviousState": xcmSvcMonServicePreviousState,
       "xcmSvcMonServiceConditions": xcmSvcMonServiceConditions,
       "xcmSvcMonServiceAvailability": xcmSvcMonServiceAvailability,
       "xcmSvcMonServicePhysicalDevice": xcmSvcMonServicePhysicalDevice,
       "xcmSvcMonServiceLogicalDevice": xcmSvcMonServiceLogicalDevice,
       "xcmSvcMonServiceExternalDevice": xcmSvcMonServiceExternalDevice,
       "xcmSvcMonServiceSWRun": xcmSvcMonServiceSWRun,
       "xcmSvcMonServiceSWInstalled": xcmSvcMonServiceSWInstalled,
       "xcmSvcMonServiceStorage": xcmSvcMonServiceStorage,
       "xcmSvcMonServicePriority": xcmSvcMonServicePriority,
       "xcmSvcMonServiceType": xcmSvcMonServiceType,
       "xcmSvcMonServiceStateDetail": xcmSvcMonServiceStateDetail,
       "xcmSvcMonServiceDetail": xcmSvcMonServiceDetail,
       "xcmSvcMonServiceDetailTable": xcmSvcMonServiceDetailTable,
       "xcmSvcMonServiceDetailEntry": xcmSvcMonServiceDetailEntry,
       "xcmSvcMonServiceDetailClass": xcmSvcMonServiceDetailClass,
       "xcmSvcMonServiceDetailType": xcmSvcMonServiceDetailType,
       "xcmSvcMonServiceDetailIndex": xcmSvcMonServiceDetailIndex,
       "xcmSvcMonServiceDetailRowStatus": xcmSvcMonServiceDetailRowStatus,
       "xcmSvcMonServiceDetailUnitClass": xcmSvcMonServiceDetailUnitClass,
       "xcmSvcMonServiceDetailUnit": xcmSvcMonServiceDetailUnit,
       "xcmSvcMonServiceDetailInteger": xcmSvcMonServiceDetailInteger,
       "xcmSvcMonServiceDetailOID": xcmSvcMonServiceDetailOID,
       "xcmSvcMonServiceDetailString": xcmSvcMonServiceDetailString,
       "xcmSvcMonServiceMgmt": xcmSvcMonServiceMgmt,
       "xcmSvcMonServiceMgmtV1EventOID": xcmSvcMonServiceMgmtV1EventOID,
       "xcmSvcMonServiceMgmtV2EventPrefix": xcmSvcMonServiceMgmtV2EventPrefix,
       "xcmSvcMonServiceMgmtV2Event": xcmSvcMonServiceMgmtV2Event,
       "xcmSvcMonServiceMgmtTable": xcmSvcMonServiceMgmtTable,
       "xcmSvcMonServiceMgmtEntry": xcmSvcMonServiceMgmtEntry,
       "xcmSvcMonServiceMgmtOperation": xcmSvcMonServiceMgmtOperation,
       "xcmSvcMonServiceMgmtData": xcmSvcMonServiceMgmtData,
       "xcmSvcMonServiceMgmtStatus": xcmSvcMonServiceMgmtStatus,
       "xcmSvcMonServiceMgmtInProgress": xcmSvcMonServiceMgmtInProgress,
       "xcmSvcMonServiceMgmtRowStatus": xcmSvcMonServiceMgmtRowStatus,
       "xcmSvcMonServiceMgmtUserPassword": xcmSvcMonServiceMgmtUserPassword,
       "xcmSvcMonServiceMgmtOperatorPassword": xcmSvcMonServiceMgmtOperatorPassword,
       "xcmSvcMonServiceMgmtAdminPassword": xcmSvcMonServiceMgmtAdminPassword}
)
