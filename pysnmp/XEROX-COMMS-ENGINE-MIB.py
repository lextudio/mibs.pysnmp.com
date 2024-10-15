# SNMP MIB module (XEROX-COMMS-ENGINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-COMMS-ENGINE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:16 2024
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

(ProductID,
 hrDeviceIndex) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "ProductID",
    "hrDeviceIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")

(XcmCommsAddressExtFanout,
 XcmCommsAddressExtForm,
 XcmCommsAddressExtScope,
 XcmCommsEngineGroupSupport,
 XcmCommsMgmtCommandData,
 XcmCommsMgmtCommandRequest,
 XcmCommsMgmtConditions,
 XcmCommsMgmtState,
 XcmCommsStackExtLayer,
 XcmCommsStackExtProtocol,
 XcmCommsStackExtPurpose,
 XcmCommsStackExtRole,
 XcmCommsStackExtSuite,
 XcmCommsStackExtSuiteVersion,
 XcmCommsStackPosition) = mibBuilder.importSymbols(
    "XEROX-COMMS-ENGINE-TC",
    "XcmCommsAddressExtFanout",
    "XcmCommsAddressExtForm",
    "XcmCommsAddressExtScope",
    "XcmCommsEngineGroupSupport",
    "XcmCommsMgmtCommandData",
    "XcmCommsMgmtCommandRequest",
    "XcmCommsMgmtConditions",
    "XcmCommsMgmtState",
    "XcmCommsStackExtLayer",
    "XcmCommsStackExtProtocol",
    "XcmCommsStackExtPurpose",
    "XcmCommsStackExtRole",
    "XcmCommsStackExtSuite",
    "XcmCommsStackExtSuiteVersion",
    "XcmCommsStackPosition")

(Cardinal32,
 Ordinal32,
 XcmFixedLocaleDisplayString,
 XcmGenSNMPv2ErrorStatus,
 zeroDotZero) = mibBuilder.importSymbols(
    "XEROX-GENERAL-TC",
    "Cardinal32",
    "Ordinal32",
    "XcmFixedLocaleDisplayString",
    "XcmGenSNMPv2ErrorStatus",
    "zeroDotZero")

(XcmHrDevTrafficUnit,) = mibBuilder.importSymbols(
    "XEROX-HOST-RESOURCES-EXT-TC",
    "XcmHrDevTrafficUnit")


# MODULE-IDENTITY

xcmCommsEngineMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XcmCommsEngineZeroDummy_ObjectIdentity = ObjectIdentity
xcmCommsEngineZeroDummy = _XcmCommsEngineZeroDummy_ObjectIdentity(
    (0, 0, 61)
)
_XcmCommsEngineMIBConformance_ObjectIdentity = ObjectIdentity
xcmCommsEngineMIBConformance = _XcmCommsEngineMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2)
)
_XcmCommsEngineMIBGroups_ObjectIdentity = ObjectIdentity
xcmCommsEngineMIBGroups = _XcmCommsEngineMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 2)
)
_XcmCommsEngine_ObjectIdentity = ObjectIdentity
xcmCommsEngine = _XcmCommsEngine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 3)
)
_XcmCommsEngineTable_Object = MibTable
xcmCommsEngineTable = _XcmCommsEngineTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 3, 2)
)
if mibBuilder.loadTexts:
    xcmCommsEngineTable.setStatus("current")
_XcmCommsEngineEntry_Object = MibTableRow
xcmCommsEngineEntry = _XcmCommsEngineEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 3, 2, 1)
)
xcmCommsEngineEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsEngineEntry.setStatus("current")
_XcmCommsEngineRowStatus_Type = RowStatus
_XcmCommsEngineRowStatus_Object = MibTableColumn
xcmCommsEngineRowStatus = _XcmCommsEngineRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 3, 2, 1, 1),
    _XcmCommsEngineRowStatus_Type()
)
xcmCommsEngineRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineRowStatus.setStatus("current")


class _XcmCommsEngineName_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmCommsEngineName based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmCommsEngineName_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmCommsEngineName_Object = MibTableColumn
xcmCommsEngineName = _XcmCommsEngineName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 3, 2, 1, 2),
    _XcmCommsEngineName_Type()
)
xcmCommsEngineName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineName.setStatus("current")


class _XcmCommsEngineStackLast_Type(Cardinal32):
    """Custom type xcmCommsEngineStackLast based on Cardinal32"""
    defaultValue = 0


_XcmCommsEngineStackLast_Object = MibTableColumn
xcmCommsEngineStackLast = _XcmCommsEngineStackLast_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 3, 2, 1, 3),
    _XcmCommsEngineStackLast_Type()
)
xcmCommsEngineStackLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineStackLast.setStatus("current")


class _XcmCommsEngineMuxLast_Type(Cardinal32):
    """Custom type xcmCommsEngineMuxLast based on Cardinal32"""
    defaultValue = 0


_XcmCommsEngineMuxLast_Object = MibTableColumn
xcmCommsEngineMuxLast = _XcmCommsEngineMuxLast_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 3, 2, 1, 4),
    _XcmCommsEngineMuxLast_Type()
)
xcmCommsEngineMuxLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineMuxLast.setStatus("current")


class _XcmCommsEngineAddressLast_Type(Cardinal32):
    """Custom type xcmCommsEngineAddressLast based on Cardinal32"""
    defaultValue = 0


_XcmCommsEngineAddressLast_Object = MibTableColumn
xcmCommsEngineAddressLast = _XcmCommsEngineAddressLast_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 3, 2, 1, 6),
    _XcmCommsEngineAddressLast_Type()
)
xcmCommsEngineAddressLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineAddressLast.setStatus("current")


class _XcmCommsEngineMgmtLast_Type(Cardinal32):
    """Custom type xcmCommsEngineMgmtLast based on Cardinal32"""
    defaultValue = 0


_XcmCommsEngineMgmtLast_Object = MibTableColumn
xcmCommsEngineMgmtLast = _XcmCommsEngineMgmtLast_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 3, 2, 1, 7),
    _XcmCommsEngineMgmtLast_Type()
)
xcmCommsEngineMgmtLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineMgmtLast.setStatus("current")


class _XcmCommsEngineGroupSupport_Type(XcmCommsEngineGroupSupport):
    """Custom type xcmCommsEngineGroupSupport based on XcmCommsEngineGroupSupport"""
    defaultValue = 1


_XcmCommsEngineGroupSupport_Object = MibTableColumn
xcmCommsEngineGroupSupport = _XcmCommsEngineGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 3, 2, 1, 8),
    _XcmCommsEngineGroupSupport_Type()
)
xcmCommsEngineGroupSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineGroupSupport.setStatus("current")


class _XcmCommsEngineCreateSupport_Type(XcmCommsEngineGroupSupport):
    """Custom type xcmCommsEngineCreateSupport based on XcmCommsEngineGroupSupport"""
    defaultValue = 0


_XcmCommsEngineCreateSupport_Object = MibTableColumn
xcmCommsEngineCreateSupport = _XcmCommsEngineCreateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 3, 2, 1, 9),
    _XcmCommsEngineCreateSupport_Type()
)
xcmCommsEngineCreateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineCreateSupport.setStatus("current")


class _XcmCommsEngineUpdateSupport_Type(XcmCommsEngineGroupSupport):
    """Custom type xcmCommsEngineUpdateSupport based on XcmCommsEngineGroupSupport"""
    defaultValue = 0


_XcmCommsEngineUpdateSupport_Object = MibTableColumn
xcmCommsEngineUpdateSupport = _XcmCommsEngineUpdateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 3, 2, 1, 10),
    _XcmCommsEngineUpdateSupport_Type()
)
xcmCommsEngineUpdateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineUpdateSupport.setStatus("current")
_XcmCommsEngineExt_ObjectIdentity = ObjectIdentity
xcmCommsEngineExt = _XcmCommsEngineExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 4)
)
_XcmCommsEngineExtTable_Object = MibTable
xcmCommsEngineExtTable = _XcmCommsEngineExtTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 4, 2)
)
if mibBuilder.loadTexts:
    xcmCommsEngineExtTable.setStatus("current")
_XcmCommsEngineExtEntry_Object = MibTableRow
xcmCommsEngineExtEntry = _XcmCommsEngineExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 4, 2, 1)
)
xcmCommsEngineExtEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsEngineExtEntry.setStatus("current")
_XcmCommsEngineExtRowStatus_Type = RowStatus
_XcmCommsEngineExtRowStatus_Object = MibTableColumn
xcmCommsEngineExtRowStatus = _XcmCommsEngineExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 4, 2, 1, 1),
    _XcmCommsEngineExtRowStatus_Type()
)
xcmCommsEngineExtRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineExtRowStatus.setStatus("current")


class _XcmCommsEngineExtState_Type(XcmCommsMgmtState):
    """Custom type xcmCommsEngineExtState based on XcmCommsMgmtState"""


_XcmCommsEngineExtState_Object = MibTableColumn
xcmCommsEngineExtState = _XcmCommsEngineExtState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 4, 2, 1, 2),
    _XcmCommsEngineExtState_Type()
)
xcmCommsEngineExtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineExtState.setStatus("current")


class _XcmCommsEngineExtConditions_Type(XcmCommsMgmtConditions):
    """Custom type xcmCommsEngineExtConditions based on XcmCommsMgmtConditions"""
    defaultValue = 0


_XcmCommsEngineExtConditions_Object = MibTableColumn
xcmCommsEngineExtConditions = _XcmCommsEngineExtConditions_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 4, 2, 1, 4),
    _XcmCommsEngineExtConditions_Type()
)
xcmCommsEngineExtConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineExtConditions.setStatus("current")


class _XcmCommsEngineExtVersionID_Type(ProductID):
    """Custom type xcmCommsEngineExtVersionID based on ProductID"""
    defaultValue = (0, 0)


_XcmCommsEngineExtVersionID_Object = MibTableColumn
xcmCommsEngineExtVersionID = _XcmCommsEngineExtVersionID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 4, 2, 1, 5),
    _XcmCommsEngineExtVersionID_Type()
)
xcmCommsEngineExtVersionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineExtVersionID.setStatus("current")


class _XcmCommsEngineExtVersionDate_Type(DateAndTime):
    """Custom type xcmCommsEngineExtVersionDate based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmCommsEngineExtVersionDate_Object = MibTableColumn
xcmCommsEngineExtVersionDate = _XcmCommsEngineExtVersionDate_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 4, 2, 1, 6),
    _XcmCommsEngineExtVersionDate_Type()
)
xcmCommsEngineExtVersionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineExtVersionDate.setStatus("current")


class _XcmCommsEngineExtMgmtIndex_Type(Cardinal32):
    """Custom type xcmCommsEngineExtMgmtIndex based on Cardinal32"""
    defaultValue = 0


_XcmCommsEngineExtMgmtIndex_Object = MibTableColumn
xcmCommsEngineExtMgmtIndex = _XcmCommsEngineExtMgmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 4, 2, 1, 7),
    _XcmCommsEngineExtMgmtIndex_Type()
)
xcmCommsEngineExtMgmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineExtMgmtIndex.setStatus("current")


class _XcmCommsEngineExtOwnerOID_Type(ObjectIdentifier):
    """Custom type xcmCommsEngineExtOwnerOID based on ObjectIdentifier"""
    defaultValue = (0, 0)


_XcmCommsEngineExtOwnerOID_Object = MibTableColumn
xcmCommsEngineExtOwnerOID = _XcmCommsEngineExtOwnerOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 4, 2, 1, 8),
    _XcmCommsEngineExtOwnerOID_Type()
)
xcmCommsEngineExtOwnerOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineExtOwnerOID.setStatus("current")
_XcmCommsStack_ObjectIdentity = ObjectIdentity
xcmCommsStack = _XcmCommsStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 5)
)
_XcmCommsStackTable_Object = MibTable
xcmCommsStackTable = _XcmCommsStackTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 5, 2)
)
if mibBuilder.loadTexts:
    xcmCommsStackTable.setStatus("current")
_XcmCommsStackEntry_Object = MibTableRow
xcmCommsStackEntry = _XcmCommsStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 5, 2, 1)
)
xcmCommsStackEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-COMMS-ENGINE-MIB", "xcmCommsStackIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsStackEntry.setStatus("current")
_XcmCommsStackIndex_Type = Ordinal32
_XcmCommsStackIndex_Object = MibTableColumn
xcmCommsStackIndex = _XcmCommsStackIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 5, 2, 1, 1),
    _XcmCommsStackIndex_Type()
)
xcmCommsStackIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmCommsStackIndex.setStatus("current")
_XcmCommsStackRowStatus_Type = RowStatus
_XcmCommsStackRowStatus_Object = MibTableColumn
xcmCommsStackRowStatus = _XcmCommsStackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 5, 2, 1, 2),
    _XcmCommsStackRowStatus_Type()
)
xcmCommsStackRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackRowStatus.setStatus("current")


class _XcmCommsStackTypeOID_Type(ObjectIdentifier):
    """Custom type xcmCommsStackTypeOID based on ObjectIdentifier"""
    defaultValue = (0, 0)


_XcmCommsStackTypeOID_Object = MibTableColumn
xcmCommsStackTypeOID = _XcmCommsStackTypeOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 5, 2, 1, 3),
    _XcmCommsStackTypeOID_Type()
)
xcmCommsStackTypeOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackTypeOID.setStatus("current")


class _XcmCommsStackName_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmCommsStackName based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmCommsStackName_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmCommsStackName_Object = MibTableColumn
xcmCommsStackName = _XcmCommsStackName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 5, 2, 1, 4),
    _XcmCommsStackName_Type()
)
xcmCommsStackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackName.setStatus("current")


class _XcmCommsStackPosition_Type(XcmCommsStackPosition):
    """Custom type xcmCommsStackPosition based on XcmCommsStackPosition"""


_XcmCommsStackPosition_Object = MibTableColumn
xcmCommsStackPosition = _XcmCommsStackPosition_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 5, 2, 1, 5),
    _XcmCommsStackPosition_Type()
)
xcmCommsStackPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackPosition.setStatus("current")


class _XcmCommsStackLowerStackIndex_Type(Cardinal32):
    """Custom type xcmCommsStackLowerStackIndex based on Cardinal32"""
    defaultValue = 0


_XcmCommsStackLowerStackIndex_Object = MibTableColumn
xcmCommsStackLowerStackIndex = _XcmCommsStackLowerStackIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 5, 2, 1, 6),
    _XcmCommsStackLowerStackIndex_Type()
)
xcmCommsStackLowerStackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackLowerStackIndex.setStatus("current")


class _XcmCommsStackUpperStackIndex_Type(Cardinal32):
    """Custom type xcmCommsStackUpperStackIndex based on Cardinal32"""
    defaultValue = 0


_XcmCommsStackUpperStackIndex_Object = MibTableColumn
xcmCommsStackUpperStackIndex = _XcmCommsStackUpperStackIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 5, 2, 1, 7),
    _XcmCommsStackUpperStackIndex_Type()
)
xcmCommsStackUpperStackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackUpperStackIndex.setStatus("current")


class _XcmCommsStackAddressIndex_Type(Cardinal32):
    """Custom type xcmCommsStackAddressIndex based on Cardinal32"""
    defaultValue = 0


_XcmCommsStackAddressIndex_Object = MibTableColumn
xcmCommsStackAddressIndex = _XcmCommsStackAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 5, 2, 1, 8),
    _XcmCommsStackAddressIndex_Type()
)
xcmCommsStackAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackAddressIndex.setStatus("current")


class _XcmCommsStackOptionIndex_Type(Cardinal32):
    """Custom type xcmCommsStackOptionIndex based on Cardinal32"""
    defaultValue = 0


_XcmCommsStackOptionIndex_Object = MibTableColumn
xcmCommsStackOptionIndex = _XcmCommsStackOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 5, 2, 1, 9),
    _XcmCommsStackOptionIndex_Type()
)
xcmCommsStackOptionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackOptionIndex.setStatus("current")


class _XcmCommsStackLowerMuxIndex_Type(Cardinal32):
    """Custom type xcmCommsStackLowerMuxIndex based on Cardinal32"""
    defaultValue = 0


_XcmCommsStackLowerMuxIndex_Object = MibTableColumn
xcmCommsStackLowerMuxIndex = _XcmCommsStackLowerMuxIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 5, 2, 1, 10),
    _XcmCommsStackLowerMuxIndex_Type()
)
xcmCommsStackLowerMuxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackLowerMuxIndex.setStatus("current")


class _XcmCommsStackUpperMuxIndex_Type(Cardinal32):
    """Custom type xcmCommsStackUpperMuxIndex based on Cardinal32"""
    defaultValue = 0


_XcmCommsStackUpperMuxIndex_Object = MibTableColumn
xcmCommsStackUpperMuxIndex = _XcmCommsStackUpperMuxIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 5, 2, 1, 11),
    _XcmCommsStackUpperMuxIndex_Type()
)
xcmCommsStackUpperMuxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackUpperMuxIndex.setStatus("current")
_XcmCommsStackExt_ObjectIdentity = ObjectIdentity
xcmCommsStackExt = _XcmCommsStackExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 6)
)
_XcmCommsStackExtTable_Object = MibTable
xcmCommsStackExtTable = _XcmCommsStackExtTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 6, 2)
)
if mibBuilder.loadTexts:
    xcmCommsStackExtTable.setStatus("current")
_XcmCommsStackExtEntry_Object = MibTableRow
xcmCommsStackExtEntry = _XcmCommsStackExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 6, 2, 1)
)
xcmCommsStackExtEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-COMMS-ENGINE-MIB", "xcmCommsStackIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsStackExtEntry.setStatus("current")
_XcmCommsStackExtRowStatus_Type = RowStatus
_XcmCommsStackExtRowStatus_Object = MibTableColumn
xcmCommsStackExtRowStatus = _XcmCommsStackExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 6, 2, 1, 1),
    _XcmCommsStackExtRowStatus_Type()
)
xcmCommsStackExtRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackExtRowStatus.setStatus("current")


class _XcmCommsStackExtState_Type(XcmCommsMgmtState):
    """Custom type xcmCommsStackExtState based on XcmCommsMgmtState"""


_XcmCommsStackExtState_Object = MibTableColumn
xcmCommsStackExtState = _XcmCommsStackExtState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 6, 2, 1, 2),
    _XcmCommsStackExtState_Type()
)
xcmCommsStackExtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackExtState.setStatus("current")


class _XcmCommsStackExtConditions_Type(XcmCommsMgmtConditions):
    """Custom type xcmCommsStackExtConditions based on XcmCommsMgmtConditions"""
    defaultValue = 0


_XcmCommsStackExtConditions_Object = MibTableColumn
xcmCommsStackExtConditions = _XcmCommsStackExtConditions_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 6, 2, 1, 3),
    _XcmCommsStackExtConditions_Type()
)
xcmCommsStackExtConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackExtConditions.setStatus("current")


class _XcmCommsStackExtPurpose_Type(XcmCommsStackExtPurpose):
    """Custom type xcmCommsStackExtPurpose based on XcmCommsStackExtPurpose"""


_XcmCommsStackExtPurpose_Object = MibTableColumn
xcmCommsStackExtPurpose = _XcmCommsStackExtPurpose_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 6, 2, 1, 4),
    _XcmCommsStackExtPurpose_Type()
)
xcmCommsStackExtPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackExtPurpose.setStatus("current")


class _XcmCommsStackExtRole_Type(XcmCommsStackExtRole):
    """Custom type xcmCommsStackExtRole based on XcmCommsStackExtRole"""


_XcmCommsStackExtRole_Object = MibTableColumn
xcmCommsStackExtRole = _XcmCommsStackExtRole_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 6, 2, 1, 5),
    _XcmCommsStackExtRole_Type()
)
xcmCommsStackExtRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackExtRole.setStatus("current")


class _XcmCommsStackExtSuite_Type(XcmCommsStackExtSuite):
    """Custom type xcmCommsStackExtSuite based on XcmCommsStackExtSuite"""


_XcmCommsStackExtSuite_Object = MibTableColumn
xcmCommsStackExtSuite = _XcmCommsStackExtSuite_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 6, 2, 1, 6),
    _XcmCommsStackExtSuite_Type()
)
xcmCommsStackExtSuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackExtSuite.setStatus("current")


class _XcmCommsStackExtSuiteVersion_Type(XcmCommsStackExtSuiteVersion):
    """Custom type xcmCommsStackExtSuiteVersion based on XcmCommsStackExtSuiteVersion"""


_XcmCommsStackExtSuiteVersion_Object = MibTableColumn
xcmCommsStackExtSuiteVersion = _XcmCommsStackExtSuiteVersion_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 6, 2, 1, 7),
    _XcmCommsStackExtSuiteVersion_Type()
)
xcmCommsStackExtSuiteVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackExtSuiteVersion.setStatus("current")


class _XcmCommsStackExtLayer_Type(XcmCommsStackExtLayer):
    """Custom type xcmCommsStackExtLayer based on XcmCommsStackExtLayer"""


_XcmCommsStackExtLayer_Object = MibTableColumn
xcmCommsStackExtLayer = _XcmCommsStackExtLayer_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 6, 2, 1, 8),
    _XcmCommsStackExtLayer_Type()
)
xcmCommsStackExtLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackExtLayer.setStatus("current")


class _XcmCommsStackExtProtocol_Type(XcmCommsStackExtProtocol):
    """Custom type xcmCommsStackExtProtocol based on XcmCommsStackExtProtocol"""


_XcmCommsStackExtProtocol_Object = MibTableColumn
xcmCommsStackExtProtocol = _XcmCommsStackExtProtocol_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 6, 2, 1, 9),
    _XcmCommsStackExtProtocol_Type()
)
xcmCommsStackExtProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackExtProtocol.setStatus("current")


class _XcmCommsStackExtMgmtIndex_Type(Cardinal32):
    """Custom type xcmCommsStackExtMgmtIndex based on Cardinal32"""
    defaultValue = 0


_XcmCommsStackExtMgmtIndex_Object = MibTableColumn
xcmCommsStackExtMgmtIndex = _XcmCommsStackExtMgmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 6, 2, 1, 10),
    _XcmCommsStackExtMgmtIndex_Type()
)
xcmCommsStackExtMgmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackExtMgmtIndex.setStatus("current")


class _XcmCommsStackExtOwnerOID_Type(ObjectIdentifier):
    """Custom type xcmCommsStackExtOwnerOID based on ObjectIdentifier"""
    defaultValue = (0, 0)


_XcmCommsStackExtOwnerOID_Object = MibTableColumn
xcmCommsStackExtOwnerOID = _XcmCommsStackExtOwnerOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 6, 2, 1, 11),
    _XcmCommsStackExtOwnerOID_Type()
)
xcmCommsStackExtOwnerOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackExtOwnerOID.setStatus("current")
_XcmCommsStackXref_ObjectIdentity = ObjectIdentity
xcmCommsStackXref = _XcmCommsStackXref_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 7)
)
_XcmCommsStackXrefTable_Object = MibTable
xcmCommsStackXrefTable = _XcmCommsStackXrefTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 7, 2)
)
if mibBuilder.loadTexts:
    xcmCommsStackXrefTable.setStatus("current")
_XcmCommsStackXrefEntry_Object = MibTableRow
xcmCommsStackXrefEntry = _XcmCommsStackXrefEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 7, 2, 1)
)
xcmCommsStackXrefEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-COMMS-ENGINE-MIB", "xcmCommsStackIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsStackXrefEntry.setStatus("current")
_XcmCommsStackXrefRowStatus_Type = RowStatus
_XcmCommsStackXrefRowStatus_Object = MibTableColumn
xcmCommsStackXrefRowStatus = _XcmCommsStackXrefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 7, 2, 1, 1),
    _XcmCommsStackXrefRowStatus_Type()
)
xcmCommsStackXrefRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackXrefRowStatus.setStatus("current")


class _XcmCommsStackXrefLayerMgmtIndex_Type(Cardinal32):
    """Custom type xcmCommsStackXrefLayerMgmtIndex based on Cardinal32"""
    defaultValue = 0


_XcmCommsStackXrefLayerMgmtIndex_Object = MibTableColumn
xcmCommsStackXrefLayerMgmtIndex = _XcmCommsStackXrefLayerMgmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 7, 2, 1, 2),
    _XcmCommsStackXrefLayerMgmtIndex_Type()
)
xcmCommsStackXrefLayerMgmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackXrefLayerMgmtIndex.setStatus("current")


class _XcmCommsStackXrefLayerSecIndex_Type(Cardinal32):
    """Custom type xcmCommsStackXrefLayerSecIndex based on Cardinal32"""
    defaultValue = 0


_XcmCommsStackXrefLayerSecIndex_Object = MibTableColumn
xcmCommsStackXrefLayerSecIndex = _XcmCommsStackXrefLayerSecIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 7, 2, 1, 3),
    _XcmCommsStackXrefLayerSecIndex_Type()
)
xcmCommsStackXrefLayerSecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackXrefLayerSecIndex.setStatus("current")


class _XcmCommsStackXrefLayerIWUIndex_Type(Cardinal32):
    """Custom type xcmCommsStackXrefLayerIWUIndex based on Cardinal32"""
    defaultValue = 0


_XcmCommsStackXrefLayerIWUIndex_Object = MibTableColumn
xcmCommsStackXrefLayerIWUIndex = _XcmCommsStackXrefLayerIWUIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 7, 2, 1, 4),
    _XcmCommsStackXrefLayerIWUIndex_Type()
)
xcmCommsStackXrefLayerIWUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackXrefLayerIWUIndex.setStatus("current")


class _XcmCommsStackXrefHrSWRunIndex_Type(Cardinal32):
    """Custom type xcmCommsStackXrefHrSWRunIndex based on Cardinal32"""
    defaultValue = 0


_XcmCommsStackXrefHrSWRunIndex_Object = MibTableColumn
xcmCommsStackXrefHrSWRunIndex = _XcmCommsStackXrefHrSWRunIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 7, 2, 1, 5),
    _XcmCommsStackXrefHrSWRunIndex_Type()
)
xcmCommsStackXrefHrSWRunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackXrefHrSWRunIndex.setStatus("current")


class _XcmCommsStackXrefHrSWInsIndex_Type(Cardinal32):
    """Custom type xcmCommsStackXrefHrSWInsIndex based on Cardinal32"""
    defaultValue = 0


_XcmCommsStackXrefHrSWInsIndex_Object = MibTableColumn
xcmCommsStackXrefHrSWInsIndex = _XcmCommsStackXrefHrSWInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 7, 2, 1, 6),
    _XcmCommsStackXrefHrSWInsIndex_Type()
)
xcmCommsStackXrefHrSWInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackXrefHrSWInsIndex.setStatus("current")


class _XcmCommsStackXrefIfIndex_Type(Cardinal32):
    """Custom type xcmCommsStackXrefIfIndex based on Cardinal32"""
    defaultValue = 0


_XcmCommsStackXrefIfIndex_Object = MibTableColumn
xcmCommsStackXrefIfIndex = _XcmCommsStackXrefIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 7, 2, 1, 7),
    _XcmCommsStackXrefIfIndex_Type()
)
xcmCommsStackXrefIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackXrefIfIndex.setStatus("current")


class _XcmCommsStackXrefHrCommDevIndex_Type(Cardinal32):
    """Custom type xcmCommsStackXrefHrCommDevIndex based on Cardinal32"""
    defaultValue = 0


_XcmCommsStackXrefHrCommDevIndex_Object = MibTableColumn
xcmCommsStackXrefHrCommDevIndex = _XcmCommsStackXrefHrCommDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 7, 2, 1, 8),
    _XcmCommsStackXrefHrCommDevIndex_Type()
)
xcmCommsStackXrefHrCommDevIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackXrefHrCommDevIndex.setStatus("current")
_XcmCommsMux_ObjectIdentity = ObjectIdentity
xcmCommsMux = _XcmCommsMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 8)
)
_XcmCommsMuxTable_Object = MibTable
xcmCommsMuxTable = _XcmCommsMuxTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 8, 2)
)
if mibBuilder.loadTexts:
    xcmCommsMuxTable.setStatus("current")
_XcmCommsMuxEntry_Object = MibTableRow
xcmCommsMuxEntry = _XcmCommsMuxEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 8, 2, 1)
)
xcmCommsMuxEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-COMMS-ENGINE-MIB", "xcmCommsMuxIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsMuxEntry.setStatus("current")
_XcmCommsMuxIndex_Type = Ordinal32
_XcmCommsMuxIndex_Object = MibTableColumn
xcmCommsMuxIndex = _XcmCommsMuxIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 8, 2, 1, 1),
    _XcmCommsMuxIndex_Type()
)
xcmCommsMuxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmCommsMuxIndex.setStatus("current")
_XcmCommsMuxRowStatus_Type = RowStatus
_XcmCommsMuxRowStatus_Object = MibTableColumn
xcmCommsMuxRowStatus = _XcmCommsMuxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 8, 2, 1, 2),
    _XcmCommsMuxRowStatus_Type()
)
xcmCommsMuxRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsMuxRowStatus.setStatus("current")


class _XcmCommsMuxNextIndex_Type(Cardinal32):
    """Custom type xcmCommsMuxNextIndex based on Cardinal32"""
    defaultValue = 0


_XcmCommsMuxNextIndex_Object = MibTableColumn
xcmCommsMuxNextIndex = _XcmCommsMuxNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 8, 2, 1, 3),
    _XcmCommsMuxNextIndex_Type()
)
xcmCommsMuxNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsMuxNextIndex.setStatus("current")


class _XcmCommsMuxPreviousIndex_Type(Cardinal32):
    """Custom type xcmCommsMuxPreviousIndex based on Cardinal32"""
    defaultValue = 0


_XcmCommsMuxPreviousIndex_Object = MibTableColumn
xcmCommsMuxPreviousIndex = _XcmCommsMuxPreviousIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 8, 2, 1, 4),
    _XcmCommsMuxPreviousIndex_Type()
)
xcmCommsMuxPreviousIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsMuxPreviousIndex.setStatus("current")


class _XcmCommsMuxOptionIndex_Type(Cardinal32):
    """Custom type xcmCommsMuxOptionIndex based on Cardinal32"""
    defaultValue = 0


_XcmCommsMuxOptionIndex_Object = MibTableColumn
xcmCommsMuxOptionIndex = _XcmCommsMuxOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 8, 2, 1, 5),
    _XcmCommsMuxOptionIndex_Type()
)
xcmCommsMuxOptionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsMuxOptionIndex.setStatus("current")
_XcmCommsMuxBaseStackIndex_Type = Ordinal32
_XcmCommsMuxBaseStackIndex_Object = MibTableColumn
xcmCommsMuxBaseStackIndex = _XcmCommsMuxBaseStackIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 8, 2, 1, 6),
    _XcmCommsMuxBaseStackIndex_Type()
)
xcmCommsMuxBaseStackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsMuxBaseStackIndex.setStatus("current")
_XcmCommsMuxAdjacentStackIndex_Type = Ordinal32
_XcmCommsMuxAdjacentStackIndex_Object = MibTableColumn
xcmCommsMuxAdjacentStackIndex = _XcmCommsMuxAdjacentStackIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 8, 2, 1, 7),
    _XcmCommsMuxAdjacentStackIndex_Type()
)
xcmCommsMuxAdjacentStackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsMuxAdjacentStackIndex.setStatus("current")
_XcmCommsMuxExt_ObjectIdentity = ObjectIdentity
xcmCommsMuxExt = _XcmCommsMuxExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 9)
)
_XcmCommsMuxExtTable_Object = MibTable
xcmCommsMuxExtTable = _XcmCommsMuxExtTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 9, 2)
)
if mibBuilder.loadTexts:
    xcmCommsMuxExtTable.setStatus("current")
_XcmCommsMuxExtEntry_Object = MibTableRow
xcmCommsMuxExtEntry = _XcmCommsMuxExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 9, 2, 1)
)
xcmCommsMuxExtEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-COMMS-ENGINE-MIB", "xcmCommsMuxIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsMuxExtEntry.setStatus("current")
_XcmCommsMuxExtRowStatus_Type = RowStatus
_XcmCommsMuxExtRowStatus_Object = MibTableColumn
xcmCommsMuxExtRowStatus = _XcmCommsMuxExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 9, 2, 1, 1),
    _XcmCommsMuxExtRowStatus_Type()
)
xcmCommsMuxExtRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsMuxExtRowStatus.setStatus("current")


class _XcmCommsMuxExtState_Type(XcmCommsMgmtState):
    """Custom type xcmCommsMuxExtState based on XcmCommsMgmtState"""


_XcmCommsMuxExtState_Object = MibTableColumn
xcmCommsMuxExtState = _XcmCommsMuxExtState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 9, 2, 1, 2),
    _XcmCommsMuxExtState_Type()
)
xcmCommsMuxExtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsMuxExtState.setStatus("current")


class _XcmCommsMuxExtConditions_Type(XcmCommsMgmtConditions):
    """Custom type xcmCommsMuxExtConditions based on XcmCommsMgmtConditions"""
    defaultValue = 0


_XcmCommsMuxExtConditions_Object = MibTableColumn
xcmCommsMuxExtConditions = _XcmCommsMuxExtConditions_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 9, 2, 1, 3),
    _XcmCommsMuxExtConditions_Type()
)
xcmCommsMuxExtConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsMuxExtConditions.setStatus("current")


class _XcmCommsMuxExtMgmtIndex_Type(Cardinal32):
    """Custom type xcmCommsMuxExtMgmtIndex based on Cardinal32"""
    defaultValue = 0


_XcmCommsMuxExtMgmtIndex_Object = MibTableColumn
xcmCommsMuxExtMgmtIndex = _XcmCommsMuxExtMgmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 9, 2, 1, 4),
    _XcmCommsMuxExtMgmtIndex_Type()
)
xcmCommsMuxExtMgmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsMuxExtMgmtIndex.setStatus("current")


class _XcmCommsMuxExtAddressIndex_Type(Cardinal32):
    """Custom type xcmCommsMuxExtAddressIndex based on Cardinal32"""
    defaultHexValue = 0


_XcmCommsMuxExtAddressIndex_Object = MibTableColumn
xcmCommsMuxExtAddressIndex = _XcmCommsMuxExtAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 9, 2, 1, 5),
    _XcmCommsMuxExtAddressIndex_Type()
)
xcmCommsMuxExtAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsMuxExtAddressIndex.setStatus("current")


class _XcmCommsMuxExtOwnerOID_Type(ObjectIdentifier):
    """Custom type xcmCommsMuxExtOwnerOID based on ObjectIdentifier"""
    defaultValue = (0, 0)


_XcmCommsMuxExtOwnerOID_Object = MibTableColumn
xcmCommsMuxExtOwnerOID = _XcmCommsMuxExtOwnerOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 9, 2, 1, 6),
    _XcmCommsMuxExtOwnerOID_Type()
)
xcmCommsMuxExtOwnerOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsMuxExtOwnerOID.setStatus("current")
_XcmCommsAddress_ObjectIdentity = ObjectIdentity
xcmCommsAddress = _XcmCommsAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 10)
)
_XcmCommsAddressTable_Object = MibTable
xcmCommsAddressTable = _XcmCommsAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 10, 2)
)
if mibBuilder.loadTexts:
    xcmCommsAddressTable.setStatus("current")
_XcmCommsAddressEntry_Object = MibTableRow
xcmCommsAddressEntry = _XcmCommsAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 10, 2, 1)
)
xcmCommsAddressEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsAddressEntry.setStatus("current")
_XcmCommsAddressIndex_Type = Ordinal32
_XcmCommsAddressIndex_Object = MibTableColumn
xcmCommsAddressIndex = _XcmCommsAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 10, 2, 1, 1),
    _XcmCommsAddressIndex_Type()
)
xcmCommsAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmCommsAddressIndex.setStatus("current")
_XcmCommsAddressRowStatus_Type = RowStatus
_XcmCommsAddressRowStatus_Object = MibTableColumn
xcmCommsAddressRowStatus = _XcmCommsAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 10, 2, 1, 2),
    _XcmCommsAddressRowStatus_Type()
)
xcmCommsAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsAddressRowStatus.setStatus("current")


class _XcmCommsAddressTypeOID_Type(ObjectIdentifier):
    """Custom type xcmCommsAddressTypeOID based on ObjectIdentifier"""
    defaultValue = (0, 0)


_XcmCommsAddressTypeOID_Object = MibTableColumn
xcmCommsAddressTypeOID = _XcmCommsAddressTypeOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 10, 2, 1, 3),
    _XcmCommsAddressTypeOID_Type()
)
xcmCommsAddressTypeOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsAddressTypeOID.setStatus("current")
_XcmCommsAddressUserRole_Type = Integer32
_XcmCommsAddressUserRole_Object = MibTableColumn
xcmCommsAddressUserRole = _XcmCommsAddressUserRole_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 10, 2, 1, 4),
    _XcmCommsAddressUserRole_Type()
)
xcmCommsAddressUserRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsAddressUserRole.setStatus("current")


class _XcmCommsAddressName_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmCommsAddressName based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmCommsAddressName_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmCommsAddressName_Object = MibTableColumn
xcmCommsAddressName = _XcmCommsAddressName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 10, 2, 1, 5),
    _XcmCommsAddressName_Type()
)
xcmCommsAddressName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsAddressName.setStatus("current")


class _XcmCommsAddressCanonical_Type(OctetString):
    """Custom type xcmCommsAddressCanonical based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmCommsAddressCanonical_Type.__name__ = "OctetString"
_XcmCommsAddressCanonical_Object = MibTableColumn
xcmCommsAddressCanonical = _XcmCommsAddressCanonical_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 10, 2, 1, 6),
    _XcmCommsAddressCanonical_Type()
)
xcmCommsAddressCanonical.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsAddressCanonical.setStatus("current")


class _XcmCommsAddressNextIndex_Type(Cardinal32):
    """Custom type xcmCommsAddressNextIndex based on Cardinal32"""
    defaultValue = 0


_XcmCommsAddressNextIndex_Object = MibTableColumn
xcmCommsAddressNextIndex = _XcmCommsAddressNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 10, 2, 1, 7),
    _XcmCommsAddressNextIndex_Type()
)
xcmCommsAddressNextIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsAddressNextIndex.setStatus("current")


class _XcmCommsAddressPreviousIndex_Type(Cardinal32):
    """Custom type xcmCommsAddressPreviousIndex based on Cardinal32"""
    defaultValue = 0


_XcmCommsAddressPreviousIndex_Object = MibTableColumn
xcmCommsAddressPreviousIndex = _XcmCommsAddressPreviousIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 10, 2, 1, 8),
    _XcmCommsAddressPreviousIndex_Type()
)
xcmCommsAddressPreviousIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsAddressPreviousIndex.setStatus("current")


class _XcmCommsAddressOptionIndex_Type(Cardinal32):
    """Custom type xcmCommsAddressOptionIndex based on Cardinal32"""
    defaultHexValue = 0


_XcmCommsAddressOptionIndex_Object = MibTableColumn
xcmCommsAddressOptionIndex = _XcmCommsAddressOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 10, 2, 1, 9),
    _XcmCommsAddressOptionIndex_Type()
)
xcmCommsAddressOptionIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsAddressOptionIndex.setStatus("current")
_XcmCommsAddressExt_ObjectIdentity = ObjectIdentity
xcmCommsAddressExt = _XcmCommsAddressExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 11)
)
_XcmCommsAddressExtTable_Object = MibTable
xcmCommsAddressExtTable = _XcmCommsAddressExtTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 11, 2)
)
if mibBuilder.loadTexts:
    xcmCommsAddressExtTable.setStatus("current")
_XcmCommsAddressExtEntry_Object = MibTableRow
xcmCommsAddressExtEntry = _XcmCommsAddressExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 11, 2, 1)
)
xcmCommsAddressExtEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsAddressExtEntry.setStatus("current")
_XcmCommsAddressExtRowStatus_Type = RowStatus
_XcmCommsAddressExtRowStatus_Object = MibTableColumn
xcmCommsAddressExtRowStatus = _XcmCommsAddressExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 11, 2, 1, 1),
    _XcmCommsAddressExtRowStatus_Type()
)
xcmCommsAddressExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsAddressExtRowStatus.setStatus("current")


class _XcmCommsAddressExtState_Type(XcmCommsMgmtState):
    """Custom type xcmCommsAddressExtState based on XcmCommsMgmtState"""


_XcmCommsAddressExtState_Object = MibTableColumn
xcmCommsAddressExtState = _XcmCommsAddressExtState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 11, 2, 1, 2),
    _XcmCommsAddressExtState_Type()
)
xcmCommsAddressExtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsAddressExtState.setStatus("current")


class _XcmCommsAddressExtConditions_Type(XcmCommsMgmtConditions):
    """Custom type xcmCommsAddressExtConditions based on XcmCommsMgmtConditions"""
    defaultValue = 0


_XcmCommsAddressExtConditions_Object = MibTableColumn
xcmCommsAddressExtConditions = _XcmCommsAddressExtConditions_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 11, 2, 1, 3),
    _XcmCommsAddressExtConditions_Type()
)
xcmCommsAddressExtConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsAddressExtConditions.setStatus("current")


class _XcmCommsAddressExtForm_Type(XcmCommsAddressExtForm):
    """Custom type xcmCommsAddressExtForm based on XcmCommsAddressExtForm"""


_XcmCommsAddressExtForm_Object = MibTableColumn
xcmCommsAddressExtForm = _XcmCommsAddressExtForm_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 11, 2, 1, 4),
    _XcmCommsAddressExtForm_Type()
)
xcmCommsAddressExtForm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsAddressExtForm.setStatus("current")


class _XcmCommsAddressExtScope_Type(XcmCommsAddressExtScope):
    """Custom type xcmCommsAddressExtScope based on XcmCommsAddressExtScope"""


_XcmCommsAddressExtScope_Object = MibTableColumn
xcmCommsAddressExtScope = _XcmCommsAddressExtScope_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 11, 2, 1, 5),
    _XcmCommsAddressExtScope_Type()
)
xcmCommsAddressExtScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsAddressExtScope.setStatus("current")


class _XcmCommsAddressExtFanout_Type(XcmCommsAddressExtFanout):
    """Custom type xcmCommsAddressExtFanout based on XcmCommsAddressExtFanout"""


_XcmCommsAddressExtFanout_Object = MibTableColumn
xcmCommsAddressExtFanout = _XcmCommsAddressExtFanout_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 11, 2, 1, 6),
    _XcmCommsAddressExtFanout_Type()
)
xcmCommsAddressExtFanout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsAddressExtFanout.setStatus("current")


class _XcmCommsAddressExtMgmtIndex_Type(Cardinal32):
    """Custom type xcmCommsAddressExtMgmtIndex based on Cardinal32"""
    defaultHexValue = 0


_XcmCommsAddressExtMgmtIndex_Object = MibTableColumn
xcmCommsAddressExtMgmtIndex = _XcmCommsAddressExtMgmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 11, 2, 1, 7),
    _XcmCommsAddressExtMgmtIndex_Type()
)
xcmCommsAddressExtMgmtIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsAddressExtMgmtIndex.setStatus("current")


class _XcmCommsAddressExtOwnerOID_Type(ObjectIdentifier):
    """Custom type xcmCommsAddressExtOwnerOID based on ObjectIdentifier"""
    defaultValue = (0, 0)


_XcmCommsAddressExtOwnerOID_Object = MibTableColumn
xcmCommsAddressExtOwnerOID = _XcmCommsAddressExtOwnerOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 11, 2, 1, 8),
    _XcmCommsAddressExtOwnerOID_Type()
)
xcmCommsAddressExtOwnerOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsAddressExtOwnerOID.setStatus("current")
_XcmCommsTraffic_ObjectIdentity = ObjectIdentity
xcmCommsTraffic = _XcmCommsTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 12)
)
_XcmCommsTrafficTable_Object = MibTable
xcmCommsTrafficTable = _XcmCommsTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 12, 2)
)
if mibBuilder.loadTexts:
    xcmCommsTrafficTable.setStatus("current")
_XcmCommsTrafficEntry_Object = MibTableRow
xcmCommsTrafficEntry = _XcmCommsTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 12, 2, 1)
)
xcmCommsTrafficEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-COMMS-ENGINE-MIB", "xcmCommsStackIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsTrafficEntry.setStatus("current")
_XcmCommsTrafficRowStatus_Type = RowStatus
_XcmCommsTrafficRowStatus_Object = MibTableColumn
xcmCommsTrafficRowStatus = _XcmCommsTrafficRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 12, 2, 1, 1),
    _XcmCommsTrafficRowStatus_Type()
)
xcmCommsTrafficRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsTrafficRowStatus.setStatus("current")


class _XcmCommsTrafficInputUnit_Type(XcmHrDevTrafficUnit):
    """Custom type xcmCommsTrafficInputUnit based on XcmHrDevTrafficUnit"""


_XcmCommsTrafficInputUnit_Object = MibTableColumn
xcmCommsTrafficInputUnit = _XcmCommsTrafficInputUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 12, 2, 1, 2),
    _XcmCommsTrafficInputUnit_Type()
)
xcmCommsTrafficInputUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsTrafficInputUnit.setStatus("current")


class _XcmCommsTrafficOutputUnit_Type(XcmHrDevTrafficUnit):
    """Custom type xcmCommsTrafficOutputUnit based on XcmHrDevTrafficUnit"""


_XcmCommsTrafficOutputUnit_Object = MibTableColumn
xcmCommsTrafficOutputUnit = _XcmCommsTrafficOutputUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 12, 2, 1, 3),
    _XcmCommsTrafficOutputUnit_Type()
)
xcmCommsTrafficOutputUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsTrafficOutputUnit.setStatus("current")
_XcmCommsTrafficInputCount_Type = Counter32
_XcmCommsTrafficInputCount_Object = MibTableColumn
xcmCommsTrafficInputCount = _XcmCommsTrafficInputCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 12, 2, 1, 4),
    _XcmCommsTrafficInputCount_Type()
)
xcmCommsTrafficInputCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsTrafficInputCount.setStatus("current")
_XcmCommsTrafficOutputCount_Type = Counter32
_XcmCommsTrafficOutputCount_Object = MibTableColumn
xcmCommsTrafficOutputCount = _XcmCommsTrafficOutputCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 12, 2, 1, 5),
    _XcmCommsTrafficOutputCount_Type()
)
xcmCommsTrafficOutputCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsTrafficOutputCount.setStatus("current")
_XcmCommsTrafficInputErrors_Type = Counter32
_XcmCommsTrafficInputErrors_Object = MibTableColumn
xcmCommsTrafficInputErrors = _XcmCommsTrafficInputErrors_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 12, 2, 1, 6),
    _XcmCommsTrafficInputErrors_Type()
)
xcmCommsTrafficInputErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsTrafficInputErrors.setStatus("current")
_XcmCommsTrafficOutputErrors_Type = Counter32
_XcmCommsTrafficOutputErrors_Object = MibTableColumn
xcmCommsTrafficOutputErrors = _XcmCommsTrafficOutputErrors_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 12, 2, 1, 7),
    _XcmCommsTrafficOutputErrors_Type()
)
xcmCommsTrafficOutputErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsTrafficOutputErrors.setStatus("current")
_XcmCommsAccess_ObjectIdentity = ObjectIdentity
xcmCommsAccess = _XcmCommsAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 13)
)
_XcmCommsAccessTable_Object = MibTable
xcmCommsAccessTable = _XcmCommsAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 13, 2)
)
if mibBuilder.loadTexts:
    xcmCommsAccessTable.setStatus("current")
_XcmCommsAccessEntry_Object = MibTableRow
xcmCommsAccessEntry = _XcmCommsAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 13, 2, 1)
)
xcmCommsAccessEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-COMMS-ENGINE-MIB", "xcmCommsStackIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsAccessEntry.setStatus("current")
_XcmCommsAccessRowStatus_Type = RowStatus
_XcmCommsAccessRowStatus_Object = MibTableColumn
xcmCommsAccessRowStatus = _XcmCommsAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 13, 2, 1, 1),
    _XcmCommsAccessRowStatus_Type()
)
xcmCommsAccessRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsAccessRowStatus.setStatus("current")


class _XcmCommsAccessConnectPorts_Type(Gauge32):
    """Custom type xcmCommsAccessConnectPorts based on Gauge32"""
    defaultValue = 0


_XcmCommsAccessConnectPorts_Object = MibTableColumn
xcmCommsAccessConnectPorts = _XcmCommsAccessConnectPorts_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 13, 2, 1, 2),
    _XcmCommsAccessConnectPorts_Type()
)
xcmCommsAccessConnectPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsAccessConnectPorts.setStatus("current")


class _XcmCommsAccessHighConnectPorts_Type(Gauge32):
    """Custom type xcmCommsAccessHighConnectPorts based on Gauge32"""
    defaultValue = 0


_XcmCommsAccessHighConnectPorts_Object = MibTableColumn
xcmCommsAccessHighConnectPorts = _XcmCommsAccessHighConnectPorts_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 13, 2, 1, 3),
    _XcmCommsAccessHighConnectPorts_Type()
)
xcmCommsAccessHighConnectPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsAccessHighConnectPorts.setStatus("current")


class _XcmCommsAccessMaxConnectPorts_Type(Cardinal32):
    """Custom type xcmCommsAccessMaxConnectPorts based on Cardinal32"""
    defaultValue = 0


_XcmCommsAccessMaxConnectPorts_Object = MibTableColumn
xcmCommsAccessMaxConnectPorts = _XcmCommsAccessMaxConnectPorts_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 13, 2, 1, 4),
    _XcmCommsAccessMaxConnectPorts_Type()
)
xcmCommsAccessMaxConnectPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsAccessMaxConnectPorts.setStatus("current")


class _XcmCommsAccessDatagramPorts_Type(Gauge32):
    """Custom type xcmCommsAccessDatagramPorts based on Gauge32"""
    defaultValue = 0


_XcmCommsAccessDatagramPorts_Object = MibTableColumn
xcmCommsAccessDatagramPorts = _XcmCommsAccessDatagramPorts_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 13, 2, 1, 5),
    _XcmCommsAccessDatagramPorts_Type()
)
xcmCommsAccessDatagramPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsAccessDatagramPorts.setStatus("current")


class _XcmCommsAccessHighDatagramPorts_Type(Gauge32):
    """Custom type xcmCommsAccessHighDatagramPorts based on Gauge32"""
    defaultValue = 0


_XcmCommsAccessHighDatagramPorts_Object = MibTableColumn
xcmCommsAccessHighDatagramPorts = _XcmCommsAccessHighDatagramPorts_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 13, 2, 1, 6),
    _XcmCommsAccessHighDatagramPorts_Type()
)
xcmCommsAccessHighDatagramPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsAccessHighDatagramPorts.setStatus("current")


class _XcmCommsAccessMaxDatagramPorts_Type(Cardinal32):
    """Custom type xcmCommsAccessMaxDatagramPorts based on Cardinal32"""
    defaultValue = 0


_XcmCommsAccessMaxDatagramPorts_Object = MibTableColumn
xcmCommsAccessMaxDatagramPorts = _XcmCommsAccessMaxDatagramPorts_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 13, 2, 1, 7),
    _XcmCommsAccessMaxDatagramPorts_Type()
)
xcmCommsAccessMaxDatagramPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsAccessMaxDatagramPorts.setStatus("current")
_XcmCommsMgmt_ObjectIdentity = ObjectIdentity
xcmCommsMgmt = _XcmCommsMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 14)
)
_XcmCommsMgmtTable_Object = MibTable
xcmCommsMgmtTable = _XcmCommsMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 14, 2)
)
if mibBuilder.loadTexts:
    xcmCommsMgmtTable.setStatus("current")
_XcmCommsMgmtEntry_Object = MibTableRow
xcmCommsMgmtEntry = _XcmCommsMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 14, 2, 1)
)
xcmCommsMgmtEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-COMMS-ENGINE-MIB", "xcmCommsMgmtIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsMgmtEntry.setStatus("current")
_XcmCommsMgmtIndex_Type = Ordinal32
_XcmCommsMgmtIndex_Object = MibTableColumn
xcmCommsMgmtIndex = _XcmCommsMgmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 14, 2, 1, 1),
    _XcmCommsMgmtIndex_Type()
)
xcmCommsMgmtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmCommsMgmtIndex.setStatus("current")
_XcmCommsMgmtRowStatus_Type = RowStatus
_XcmCommsMgmtRowStatus_Object = MibTableColumn
xcmCommsMgmtRowStatus = _XcmCommsMgmtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 14, 2, 1, 2),
    _XcmCommsMgmtRowStatus_Type()
)
xcmCommsMgmtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsMgmtRowStatus.setStatus("current")


class _XcmCommsMgmtCommandRequest_Type(XcmCommsMgmtCommandRequest):
    """Custom type xcmCommsMgmtCommandRequest based on XcmCommsMgmtCommandRequest"""


_XcmCommsMgmtCommandRequest_Object = MibTableColumn
xcmCommsMgmtCommandRequest = _XcmCommsMgmtCommandRequest_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 14, 2, 1, 3),
    _XcmCommsMgmtCommandRequest_Type()
)
xcmCommsMgmtCommandRequest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsMgmtCommandRequest.setStatus("current")


class _XcmCommsMgmtCommandData_Type(XcmCommsMgmtCommandData):
    """Custom type xcmCommsMgmtCommandData based on XcmCommsMgmtCommandData"""
    defaultHexValue = ""

    subtypeSpec = XcmCommsMgmtCommandData.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmCommsMgmtCommandData_Type.__name__ = "XcmCommsMgmtCommandData"
_XcmCommsMgmtCommandData_Object = MibTableColumn
xcmCommsMgmtCommandData = _XcmCommsMgmtCommandData_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 14, 2, 1, 4),
    _XcmCommsMgmtCommandData_Type()
)
xcmCommsMgmtCommandData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsMgmtCommandData.setStatus("current")
_XcmCommsMgmtCommandStatus_Type = XcmGenSNMPv2ErrorStatus
_XcmCommsMgmtCommandStatus_Object = MibTableColumn
xcmCommsMgmtCommandStatus = _XcmCommsMgmtCommandStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 14, 2, 1, 5),
    _XcmCommsMgmtCommandStatus_Type()
)
xcmCommsMgmtCommandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsMgmtCommandStatus.setStatus("current")


class _XcmCommsMgmtCommandInProgress_Type(TruthValue):
    """Custom type xcmCommsMgmtCommandInProgress based on TruthValue"""


_XcmCommsMgmtCommandInProgress_Object = MibTableColumn
xcmCommsMgmtCommandInProgress = _XcmCommsMgmtCommandInProgress_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 14, 2, 1, 6),
    _XcmCommsMgmtCommandInProgress_Type()
)
xcmCommsMgmtCommandInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsMgmtCommandInProgress.setStatus("current")

# Managed Objects groups

xcmCommsEngineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 2, 3)
)
xcmCommsEngineGroup.setObjects(
      *(("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineRowStatus"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineName"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineStackLast"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineMuxLast"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineAddressLast"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineMgmtLast"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineGroupSupport"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineCreateSupport"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineUpdateSupport"))
)
if mibBuilder.loadTexts:
    xcmCommsEngineGroup.setStatus("current")

xcmCommsEngineExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 2, 4)
)
xcmCommsEngineExtGroup.setObjects(
      *(("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineExtRowStatus"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineExtState"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineExtConditions"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineExtVersionID"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineExtVersionDate"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineExtMgmtIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineExtOwnerOID"))
)
if mibBuilder.loadTexts:
    xcmCommsEngineExtGroup.setStatus("current")

xcmCommsStackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 2, 5)
)
xcmCommsStackGroup.setObjects(
      *(("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackRowStatus"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackTypeOID"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackName"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackPosition"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackLowerStackIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackUpperStackIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackAddressIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackOptionIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackLowerMuxIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackUpperMuxIndex"))
)
if mibBuilder.loadTexts:
    xcmCommsStackGroup.setStatus("current")

xcmCommsStackExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 2, 6)
)
xcmCommsStackExtGroup.setObjects(
      *(("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackExtRowStatus"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackExtState"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackExtConditions"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackExtPurpose"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackExtRole"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackExtSuite"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackExtSuiteVersion"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackExtLayer"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackExtProtocol"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackExtMgmtIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackExtOwnerOID"))
)
if mibBuilder.loadTexts:
    xcmCommsStackExtGroup.setStatus("current")

xcmCommsStackXrefGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 2, 7)
)
xcmCommsStackXrefGroup.setObjects(
      *(("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackXrefRowStatus"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackXrefLayerMgmtIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackXrefLayerSecIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackXrefLayerIWUIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackXrefHrSWRunIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackXrefHrSWInsIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackXrefIfIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackXrefHrCommDevIndex"))
)
if mibBuilder.loadTexts:
    xcmCommsStackXrefGroup.setStatus("current")

xcmCommsMuxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 2, 8)
)
xcmCommsMuxGroup.setObjects(
      *(("XEROX-COMMS-ENGINE-MIB", "xcmCommsMuxRowStatus"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsMuxNextIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsMuxPreviousIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsMuxOptionIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsMuxBaseStackIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsMuxAdjacentStackIndex"))
)
if mibBuilder.loadTexts:
    xcmCommsMuxGroup.setStatus("current")

xcmCommsMuxExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 2, 9)
)
xcmCommsMuxExtGroup.setObjects(
      *(("XEROX-COMMS-ENGINE-MIB", "xcmCommsMuxExtRowStatus"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsMuxExtState"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsMuxExtConditions"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsMuxExtMgmtIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsMuxExtAddressIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsMuxExtOwnerOID"))
)
if mibBuilder.loadTexts:
    xcmCommsMuxExtGroup.setStatus("current")

xcmCommsAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 2, 10)
)
xcmCommsAddressGroup.setObjects(
      *(("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressRowStatus"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressTypeOID"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressUserRole"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressName"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressCanonical"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressNextIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressPreviousIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressOptionIndex"))
)
if mibBuilder.loadTexts:
    xcmCommsAddressGroup.setStatus("current")

xcmCommsAddressExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 2, 11)
)
xcmCommsAddressExtGroup.setObjects(
      *(("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressExtRowStatus"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressExtState"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressExtConditions"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressExtForm"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressExtScope"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressExtFanout"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressExtMgmtIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressExtOwnerOID"))
)
if mibBuilder.loadTexts:
    xcmCommsAddressExtGroup.setStatus("current")

xcmCommsTrafficGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 2, 12)
)
xcmCommsTrafficGroup.setObjects(
      *(("XEROX-COMMS-ENGINE-MIB", "xcmCommsTrafficRowStatus"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsTrafficInputUnit"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsTrafficOutputUnit"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsTrafficInputCount"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsTrafficOutputCount"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsTrafficInputErrors"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsTrafficOutputErrors"))
)
if mibBuilder.loadTexts:
    xcmCommsTrafficGroup.setStatus("current")

xcmCommsAccessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 2, 13)
)
xcmCommsAccessGroup.setObjects(
      *(("XEROX-COMMS-ENGINE-MIB", "xcmCommsAccessRowStatus"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAccessConnectPorts"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAccessHighConnectPorts"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAccessMaxConnectPorts"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAccessDatagramPorts"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAccessHighDatagramPorts"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAccessMaxDatagramPorts"))
)
if mibBuilder.loadTexts:
    xcmCommsAccessGroup.setStatus("current")

xcmCommsMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 2, 14)
)
xcmCommsMgmtGroup.setObjects(
      *(("XEROX-COMMS-ENGINE-MIB", "xcmCommsMgmtRowStatus"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsMgmtCommandRequest"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsMgmtCommandData"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsMgmtCommandStatus"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsMgmtCommandInProgress"))
)
if mibBuilder.loadTexts:
    xcmCommsMgmtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xcmCommsEngineMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 3)
)
if mibBuilder.loadTexts:
    xcmCommsEngineMIBCompliance.setStatus(
        "current"
    )

xcmCommsEngineMIBHelpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 4)
)
if mibBuilder.loadTexts:
    xcmCommsEngineMIBHelpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-COMMS-ENGINE-MIB",
    **{"xcmCommsEngineZeroDummy": xcmCommsEngineZeroDummy,
       "xcmCommsEngineMIB": xcmCommsEngineMIB,
       "xcmCommsEngineMIBConformance": xcmCommsEngineMIBConformance,
       "xcmCommsEngineMIBGroups": xcmCommsEngineMIBGroups,
       "xcmCommsEngineGroup": xcmCommsEngineGroup,
       "xcmCommsEngineExtGroup": xcmCommsEngineExtGroup,
       "xcmCommsStackGroup": xcmCommsStackGroup,
       "xcmCommsStackExtGroup": xcmCommsStackExtGroup,
       "xcmCommsStackXrefGroup": xcmCommsStackXrefGroup,
       "xcmCommsMuxGroup": xcmCommsMuxGroup,
       "xcmCommsMuxExtGroup": xcmCommsMuxExtGroup,
       "xcmCommsAddressGroup": xcmCommsAddressGroup,
       "xcmCommsAddressExtGroup": xcmCommsAddressExtGroup,
       "xcmCommsTrafficGroup": xcmCommsTrafficGroup,
       "xcmCommsAccessGroup": xcmCommsAccessGroup,
       "xcmCommsMgmtGroup": xcmCommsMgmtGroup,
       "xcmCommsEngineMIBCompliance": xcmCommsEngineMIBCompliance,
       "xcmCommsEngineMIBHelpCompliance": xcmCommsEngineMIBHelpCompliance,
       "xcmCommsEngine": xcmCommsEngine,
       "xcmCommsEngineTable": xcmCommsEngineTable,
       "xcmCommsEngineEntry": xcmCommsEngineEntry,
       "xcmCommsEngineRowStatus": xcmCommsEngineRowStatus,
       "xcmCommsEngineName": xcmCommsEngineName,
       "xcmCommsEngineStackLast": xcmCommsEngineStackLast,
       "xcmCommsEngineMuxLast": xcmCommsEngineMuxLast,
       "xcmCommsEngineAddressLast": xcmCommsEngineAddressLast,
       "xcmCommsEngineMgmtLast": xcmCommsEngineMgmtLast,
       "xcmCommsEngineGroupSupport": xcmCommsEngineGroupSupport,
       "xcmCommsEngineCreateSupport": xcmCommsEngineCreateSupport,
       "xcmCommsEngineUpdateSupport": xcmCommsEngineUpdateSupport,
       "xcmCommsEngineExt": xcmCommsEngineExt,
       "xcmCommsEngineExtTable": xcmCommsEngineExtTable,
       "xcmCommsEngineExtEntry": xcmCommsEngineExtEntry,
       "xcmCommsEngineExtRowStatus": xcmCommsEngineExtRowStatus,
       "xcmCommsEngineExtState": xcmCommsEngineExtState,
       "xcmCommsEngineExtConditions": xcmCommsEngineExtConditions,
       "xcmCommsEngineExtVersionID": xcmCommsEngineExtVersionID,
       "xcmCommsEngineExtVersionDate": xcmCommsEngineExtVersionDate,
       "xcmCommsEngineExtMgmtIndex": xcmCommsEngineExtMgmtIndex,
       "xcmCommsEngineExtOwnerOID": xcmCommsEngineExtOwnerOID,
       "xcmCommsStack": xcmCommsStack,
       "xcmCommsStackTable": xcmCommsStackTable,
       "xcmCommsStackEntry": xcmCommsStackEntry,
       "xcmCommsStackIndex": xcmCommsStackIndex,
       "xcmCommsStackRowStatus": xcmCommsStackRowStatus,
       "xcmCommsStackTypeOID": xcmCommsStackTypeOID,
       "xcmCommsStackName": xcmCommsStackName,
       "xcmCommsStackPosition": xcmCommsStackPosition,
       "xcmCommsStackLowerStackIndex": xcmCommsStackLowerStackIndex,
       "xcmCommsStackUpperStackIndex": xcmCommsStackUpperStackIndex,
       "xcmCommsStackAddressIndex": xcmCommsStackAddressIndex,
       "xcmCommsStackOptionIndex": xcmCommsStackOptionIndex,
       "xcmCommsStackLowerMuxIndex": xcmCommsStackLowerMuxIndex,
       "xcmCommsStackUpperMuxIndex": xcmCommsStackUpperMuxIndex,
       "xcmCommsStackExt": xcmCommsStackExt,
       "xcmCommsStackExtTable": xcmCommsStackExtTable,
       "xcmCommsStackExtEntry": xcmCommsStackExtEntry,
       "xcmCommsStackExtRowStatus": xcmCommsStackExtRowStatus,
       "xcmCommsStackExtState": xcmCommsStackExtState,
       "xcmCommsStackExtConditions": xcmCommsStackExtConditions,
       "xcmCommsStackExtPurpose": xcmCommsStackExtPurpose,
       "xcmCommsStackExtRole": xcmCommsStackExtRole,
       "xcmCommsStackExtSuite": xcmCommsStackExtSuite,
       "xcmCommsStackExtSuiteVersion": xcmCommsStackExtSuiteVersion,
       "xcmCommsStackExtLayer": xcmCommsStackExtLayer,
       "xcmCommsStackExtProtocol": xcmCommsStackExtProtocol,
       "xcmCommsStackExtMgmtIndex": xcmCommsStackExtMgmtIndex,
       "xcmCommsStackExtOwnerOID": xcmCommsStackExtOwnerOID,
       "xcmCommsStackXref": xcmCommsStackXref,
       "xcmCommsStackXrefTable": xcmCommsStackXrefTable,
       "xcmCommsStackXrefEntry": xcmCommsStackXrefEntry,
       "xcmCommsStackXrefRowStatus": xcmCommsStackXrefRowStatus,
       "xcmCommsStackXrefLayerMgmtIndex": xcmCommsStackXrefLayerMgmtIndex,
       "xcmCommsStackXrefLayerSecIndex": xcmCommsStackXrefLayerSecIndex,
       "xcmCommsStackXrefLayerIWUIndex": xcmCommsStackXrefLayerIWUIndex,
       "xcmCommsStackXrefHrSWRunIndex": xcmCommsStackXrefHrSWRunIndex,
       "xcmCommsStackXrefHrSWInsIndex": xcmCommsStackXrefHrSWInsIndex,
       "xcmCommsStackXrefIfIndex": xcmCommsStackXrefIfIndex,
       "xcmCommsStackXrefHrCommDevIndex": xcmCommsStackXrefHrCommDevIndex,
       "xcmCommsMux": xcmCommsMux,
       "xcmCommsMuxTable": xcmCommsMuxTable,
       "xcmCommsMuxEntry": xcmCommsMuxEntry,
       "xcmCommsMuxIndex": xcmCommsMuxIndex,
       "xcmCommsMuxRowStatus": xcmCommsMuxRowStatus,
       "xcmCommsMuxNextIndex": xcmCommsMuxNextIndex,
       "xcmCommsMuxPreviousIndex": xcmCommsMuxPreviousIndex,
       "xcmCommsMuxOptionIndex": xcmCommsMuxOptionIndex,
       "xcmCommsMuxBaseStackIndex": xcmCommsMuxBaseStackIndex,
       "xcmCommsMuxAdjacentStackIndex": xcmCommsMuxAdjacentStackIndex,
       "xcmCommsMuxExt": xcmCommsMuxExt,
       "xcmCommsMuxExtTable": xcmCommsMuxExtTable,
       "xcmCommsMuxExtEntry": xcmCommsMuxExtEntry,
       "xcmCommsMuxExtRowStatus": xcmCommsMuxExtRowStatus,
       "xcmCommsMuxExtState": xcmCommsMuxExtState,
       "xcmCommsMuxExtConditions": xcmCommsMuxExtConditions,
       "xcmCommsMuxExtMgmtIndex": xcmCommsMuxExtMgmtIndex,
       "xcmCommsMuxExtAddressIndex": xcmCommsMuxExtAddressIndex,
       "xcmCommsMuxExtOwnerOID": xcmCommsMuxExtOwnerOID,
       "xcmCommsAddress": xcmCommsAddress,
       "xcmCommsAddressTable": xcmCommsAddressTable,
       "xcmCommsAddressEntry": xcmCommsAddressEntry,
       "xcmCommsAddressIndex": xcmCommsAddressIndex,
       "xcmCommsAddressRowStatus": xcmCommsAddressRowStatus,
       "xcmCommsAddressTypeOID": xcmCommsAddressTypeOID,
       "xcmCommsAddressUserRole": xcmCommsAddressUserRole,
       "xcmCommsAddressName": xcmCommsAddressName,
       "xcmCommsAddressCanonical": xcmCommsAddressCanonical,
       "xcmCommsAddressNextIndex": xcmCommsAddressNextIndex,
       "xcmCommsAddressPreviousIndex": xcmCommsAddressPreviousIndex,
       "xcmCommsAddressOptionIndex": xcmCommsAddressOptionIndex,
       "xcmCommsAddressExt": xcmCommsAddressExt,
       "xcmCommsAddressExtTable": xcmCommsAddressExtTable,
       "xcmCommsAddressExtEntry": xcmCommsAddressExtEntry,
       "xcmCommsAddressExtRowStatus": xcmCommsAddressExtRowStatus,
       "xcmCommsAddressExtState": xcmCommsAddressExtState,
       "xcmCommsAddressExtConditions": xcmCommsAddressExtConditions,
       "xcmCommsAddressExtForm": xcmCommsAddressExtForm,
       "xcmCommsAddressExtScope": xcmCommsAddressExtScope,
       "xcmCommsAddressExtFanout": xcmCommsAddressExtFanout,
       "xcmCommsAddressExtMgmtIndex": xcmCommsAddressExtMgmtIndex,
       "xcmCommsAddressExtOwnerOID": xcmCommsAddressExtOwnerOID,
       "xcmCommsTraffic": xcmCommsTraffic,
       "xcmCommsTrafficTable": xcmCommsTrafficTable,
       "xcmCommsTrafficEntry": xcmCommsTrafficEntry,
       "xcmCommsTrafficRowStatus": xcmCommsTrafficRowStatus,
       "xcmCommsTrafficInputUnit": xcmCommsTrafficInputUnit,
       "xcmCommsTrafficOutputUnit": xcmCommsTrafficOutputUnit,
       "xcmCommsTrafficInputCount": xcmCommsTrafficInputCount,
       "xcmCommsTrafficOutputCount": xcmCommsTrafficOutputCount,
       "xcmCommsTrafficInputErrors": xcmCommsTrafficInputErrors,
       "xcmCommsTrafficOutputErrors": xcmCommsTrafficOutputErrors,
       "xcmCommsAccess": xcmCommsAccess,
       "xcmCommsAccessTable": xcmCommsAccessTable,
       "xcmCommsAccessEntry": xcmCommsAccessEntry,
       "xcmCommsAccessRowStatus": xcmCommsAccessRowStatus,
       "xcmCommsAccessConnectPorts": xcmCommsAccessConnectPorts,
       "xcmCommsAccessHighConnectPorts": xcmCommsAccessHighConnectPorts,
       "xcmCommsAccessMaxConnectPorts": xcmCommsAccessMaxConnectPorts,
       "xcmCommsAccessDatagramPorts": xcmCommsAccessDatagramPorts,
       "xcmCommsAccessHighDatagramPorts": xcmCommsAccessHighDatagramPorts,
       "xcmCommsAccessMaxDatagramPorts": xcmCommsAccessMaxDatagramPorts,
       "xcmCommsMgmt": xcmCommsMgmt,
       "xcmCommsMgmtTable": xcmCommsMgmtTable,
       "xcmCommsMgmtEntry": xcmCommsMgmtEntry,
       "xcmCommsMgmtIndex": xcmCommsMgmtIndex,
       "xcmCommsMgmtRowStatus": xcmCommsMgmtRowStatus,
       "xcmCommsMgmtCommandRequest": xcmCommsMgmtCommandRequest,
       "xcmCommsMgmtCommandData": xcmCommsMgmtCommandData,
       "xcmCommsMgmtCommandStatus": xcmCommsMgmtCommandStatus,
       "xcmCommsMgmtCommandInProgress": xcmCommsMgmtCommandInProgress}
)
