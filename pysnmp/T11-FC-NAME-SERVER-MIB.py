# SNMP MIB module (T11-FC-NAME-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/T11-FC-NAME-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:21 2024
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
 FcClasses,
 FcNameIdOrZero,
 FcPortType,
 fcmInstanceIndex) = mibBuilder.importSymbols(
    "FC-MGMT-MIB",
    "FcAddressIdOrZero",
    "FcClasses",
    "FcNameIdOrZero",
    "FcPortType",
    "fcmInstanceIndex")

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

(T11FabricIndex,) = mibBuilder.importSymbols(
    "T11-TC-MIB",
    "T11FabricIndex")


# MODULE-IDENTITY

t11FcNameServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 135)
)
t11FcNameServerMIB.setRevisions(
        ("2006-03-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class T11NsGs4RejectReasonCode(Integer32, TextualConvention):
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
        *(("cmdNotSupported", 9),
          ("couldNotEstabSession", 11),
          ("invalidCmdCode", 2),
          ("invalidIUSize", 5),
          ("invalidVerLevel", 3),
          ("logicalBusy", 6),
          ("logicalError", 4),
          ("none", 1),
          ("protocolError", 7),
          ("serverNotAvailable", 10),
          ("unableToPerformCmdReq", 8),
          ("vendorError", 12))
    )



class T11NsRejReasonCodeExpl(Integer32, TextualConvention):
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
        *(("accessDenied", 17),
          ("authenticationException", 25),
          ("authorizationException", 24),
          ("classOfServiceNotRegistered", 5),
          ("databaseEmpty", 19),
          ("databaseFull", 26),
          ("domainIdNotPresent", 21),
          ("fabricPortNameNotRegistered", 13),
          ("fc4DescriptorNotRegistered", 15),
          ("fc4FeaturesNotRegistered", 16),
          ("fc4TypeNotRegistered", 8),
          ("hardAddressNotRegistered", 14),
          ("ipaNotRegistered", 7),
          ("noAdditionalExplanation", 1),
          ("noDeviceAttached", 23),
          ("noObjectRegInSpecifiedScope", 20),
          ("nodeIpAddressNotRegistered", 6),
          ("nodeNameNotRegistered", 4),
          ("portIdNotPresent", 22),
          ("portIdentifierNotRegistered", 2),
          ("portIpAddressNotRegistered", 12),
          ("portNameNotRegistered", 3),
          ("portTypeNotRegistered", 11),
          ("symbolicNodeNameNotRegistered", 10),
          ("symbolicPortNameNotRegistered", 9),
          ("unacceptablePortIdentifier", 18))
    )



# MIB Managed Objects in the order of their OIDs

_T11NsNotifications_ObjectIdentity = ObjectIdentity
t11NsNotifications = _T11NsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 135, 0)
)
_T11NsMIBObjects_ObjectIdentity = ObjectIdentity
t11NsMIBObjects = _T11NsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 135, 1)
)
_T11NsStatus_ObjectIdentity = ObjectIdentity
t11NsStatus = _T11NsStatus_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 135, 1, 1)
)
_T11NsInfoSubsetTable_Object = MibTable
t11NsInfoSubsetTable = _T11NsInfoSubsetTable_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 1)
)
if mibBuilder.loadTexts:
    t11NsInfoSubsetTable.setStatus("current")
_T11NsInfoSubsetEntry_Object = MibTableRow
t11NsInfoSubsetEntry = _T11NsInfoSubsetEntry_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 1, 1)
)
t11NsInfoSubsetEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-NAME-SERVER-MIB", "t11NsInfoSubsetIndex"),
)
if mibBuilder.loadTexts:
    t11NsInfoSubsetEntry.setStatus("current")


class _T11NsInfoSubsetIndex_Type(Unsigned32):
    """Custom type t11NsInfoSubsetIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11NsInfoSubsetIndex_Type.__name__ = "Unsigned32"
_T11NsInfoSubsetIndex_Object = MibTableColumn
t11NsInfoSubsetIndex = _T11NsInfoSubsetIndex_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 1, 1, 1),
    _T11NsInfoSubsetIndex_Type()
)
t11NsInfoSubsetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11NsInfoSubsetIndex.setStatus("current")


class _T11NsInfoSubsetSwitchIndex_Type(Unsigned32):
    """Custom type t11NsInfoSubsetSwitchIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_T11NsInfoSubsetSwitchIndex_Type.__name__ = "Unsigned32"
_T11NsInfoSubsetSwitchIndex_Object = MibTableColumn
t11NsInfoSubsetSwitchIndex = _T11NsInfoSubsetSwitchIndex_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 1, 1, 2),
    _T11NsInfoSubsetSwitchIndex_Type()
)
t11NsInfoSubsetSwitchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsInfoSubsetSwitchIndex.setStatus("current")
_T11NsInfoSubsetTableLastChange_Type = TimeStamp
_T11NsInfoSubsetTableLastChange_Object = MibTableColumn
t11NsInfoSubsetTableLastChange = _T11NsInfoSubsetTableLastChange_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 1, 1, 3),
    _T11NsInfoSubsetTableLastChange_Type()
)
t11NsInfoSubsetTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsInfoSubsetTableLastChange.setStatus("current")


class _T11NsInfoSubsetNumRows_Type(Integer32):
    """Custom type t11NsInfoSubsetNumRows based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_T11NsInfoSubsetNumRows_Type.__name__ = "Integer32"
_T11NsInfoSubsetNumRows_Object = MibTableColumn
t11NsInfoSubsetNumRows = _T11NsInfoSubsetNumRows_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 1, 1, 4),
    _T11NsInfoSubsetNumRows_Type()
)
t11NsInfoSubsetNumRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsInfoSubsetNumRows.setStatus("current")
_T11NsInfoSubsetTotalRejects_Type = Counter32
_T11NsInfoSubsetTotalRejects_Object = MibTableColumn
t11NsInfoSubsetTotalRejects = _T11NsInfoSubsetTotalRejects_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 1, 1, 5),
    _T11NsInfoSubsetTotalRejects_Type()
)
t11NsInfoSubsetTotalRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsInfoSubsetTotalRejects.setStatus("current")


class _T11NsInfoSubsetRejReqNotfyEnable_Type(TruthValue):
    """Custom type t11NsInfoSubsetRejReqNotfyEnable based on TruthValue"""


_T11NsInfoSubsetRejReqNotfyEnable_Object = MibTableColumn
t11NsInfoSubsetRejReqNotfyEnable = _T11NsInfoSubsetRejReqNotfyEnable_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 1, 1, 6),
    _T11NsInfoSubsetRejReqNotfyEnable_Type()
)
t11NsInfoSubsetRejReqNotfyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11NsInfoSubsetRejReqNotfyEnable.setStatus("current")
_T11NsRegTable_Object = MibTable
t11NsRegTable = _T11NsRegTable_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 2)
)
if mibBuilder.loadTexts:
    t11NsRegTable.setStatus("current")
_T11NsRegEntry_Object = MibTableRow
t11NsRegEntry = _T11NsRegEntry_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 2, 1)
)
t11NsRegEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-NAME-SERVER-MIB", "t11NsInfoSubsetIndex"),
    (0, "T11-FC-NAME-SERVER-MIB", "t11NsRegFabricIndex"),
    (0, "T11-FC-NAME-SERVER-MIB", "t11NsRegPortIdentifier"),
)
if mibBuilder.loadTexts:
    t11NsRegEntry.setStatus("current")
_T11NsRegFabricIndex_Type = T11FabricIndex
_T11NsRegFabricIndex_Object = MibTableColumn
t11NsRegFabricIndex = _T11NsRegFabricIndex_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 2, 1, 1),
    _T11NsRegFabricIndex_Type()
)
t11NsRegFabricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11NsRegFabricIndex.setStatus("current")
_T11NsRegPortIdentifier_Type = FcAddressIdOrZero
_T11NsRegPortIdentifier_Object = MibTableColumn
t11NsRegPortIdentifier = _T11NsRegPortIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 2, 1, 2),
    _T11NsRegPortIdentifier_Type()
)
t11NsRegPortIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11NsRegPortIdentifier.setStatus("current")


class _T11NsRegPortName_Type(FcNameIdOrZero):
    """Custom type t11NsRegPortName based on FcNameIdOrZero"""
    defaultHexValue = ""


_T11NsRegPortName_Object = MibTableColumn
t11NsRegPortName = _T11NsRegPortName_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 2, 1, 3),
    _T11NsRegPortName_Type()
)
t11NsRegPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsRegPortName.setStatus("current")


class _T11NsRegNodeName_Type(FcNameIdOrZero):
    """Custom type t11NsRegNodeName based on FcNameIdOrZero"""
    defaultHexValue = ""


_T11NsRegNodeName_Object = MibTableColumn
t11NsRegNodeName = _T11NsRegNodeName_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 2, 1, 4),
    _T11NsRegNodeName_Type()
)
t11NsRegNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsRegNodeName.setStatus("current")
_T11NsRegClassOfSvc_Type = FcClasses
_T11NsRegClassOfSvc_Object = MibTableColumn
t11NsRegClassOfSvc = _T11NsRegClassOfSvc_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 2, 1, 5),
    _T11NsRegClassOfSvc_Type()
)
t11NsRegClassOfSvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsRegClassOfSvc.setStatus("current")


class _T11NsRegNodeIpAddress_Type(OctetString):
    """Custom type t11NsRegNodeIpAddress based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_T11NsRegNodeIpAddress_Type.__name__ = "OctetString"
_T11NsRegNodeIpAddress_Object = MibTableColumn
t11NsRegNodeIpAddress = _T11NsRegNodeIpAddress_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 2, 1, 6),
    _T11NsRegNodeIpAddress_Type()
)
t11NsRegNodeIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsRegNodeIpAddress.setStatus("current")


class _T11NsRegProcAssoc_Type(OctetString):
    """Custom type t11NsRegProcAssoc based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_T11NsRegProcAssoc_Type.__name__ = "OctetString"
_T11NsRegProcAssoc_Object = MibTableColumn
t11NsRegProcAssoc = _T11NsRegProcAssoc_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 2, 1, 7),
    _T11NsRegProcAssoc_Type()
)
t11NsRegProcAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsRegProcAssoc.setStatus("current")


class _T11NsRegFc4Type_Type(OctetString):
    """Custom type t11NsRegFc4Type based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(32, 32),
    )


_T11NsRegFc4Type_Type.__name__ = "OctetString"
_T11NsRegFc4Type_Object = MibTableColumn
t11NsRegFc4Type = _T11NsRegFc4Type_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 2, 1, 8),
    _T11NsRegFc4Type_Type()
)
t11NsRegFc4Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsRegFc4Type.setStatus("current")


class _T11NsRegPortType_Type(FcPortType):
    """Custom type t11NsRegPortType based on FcPortType"""
    defaultValue = 1


_T11NsRegPortType_Object = MibTableColumn
t11NsRegPortType = _T11NsRegPortType_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 2, 1, 9),
    _T11NsRegPortType_Type()
)
t11NsRegPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsRegPortType.setStatus("current")


class _T11NsRegPortIpAddress_Type(OctetString):
    """Custom type t11NsRegPortIpAddress based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_T11NsRegPortIpAddress_Type.__name__ = "OctetString"
_T11NsRegPortIpAddress_Object = MibTableColumn
t11NsRegPortIpAddress = _T11NsRegPortIpAddress_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 2, 1, 10),
    _T11NsRegPortIpAddress_Type()
)
t11NsRegPortIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsRegPortIpAddress.setStatus("current")


class _T11NsRegFabricPortName_Type(FcNameIdOrZero):
    """Custom type t11NsRegFabricPortName based on FcNameIdOrZero"""
    defaultHexValue = ""


_T11NsRegFabricPortName_Object = MibTableColumn
t11NsRegFabricPortName = _T11NsRegFabricPortName_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 2, 1, 11),
    _T11NsRegFabricPortName_Type()
)
t11NsRegFabricPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsRegFabricPortName.setStatus("current")


class _T11NsRegHardAddress_Type(FcAddressIdOrZero):
    """Custom type t11NsRegHardAddress based on FcAddressIdOrZero"""
    defaultHexValue = ""


_T11NsRegHardAddress_Object = MibTableColumn
t11NsRegHardAddress = _T11NsRegHardAddress_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 2, 1, 12),
    _T11NsRegHardAddress_Type()
)
t11NsRegHardAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsRegHardAddress.setStatus("current")


class _T11NsRegSymbolicPortName_Type(SnmpAdminString):
    """Custom type t11NsRegSymbolicPortName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_T11NsRegSymbolicPortName_Type.__name__ = "SnmpAdminString"
_T11NsRegSymbolicPortName_Object = MibTableColumn
t11NsRegSymbolicPortName = _T11NsRegSymbolicPortName_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 2, 1, 13),
    _T11NsRegSymbolicPortName_Type()
)
t11NsRegSymbolicPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsRegSymbolicPortName.setStatus("current")


class _T11NsRegSymbolicNodeName_Type(SnmpAdminString):
    """Custom type t11NsRegSymbolicNodeName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_T11NsRegSymbolicNodeName_Type.__name__ = "SnmpAdminString"
_T11NsRegSymbolicNodeName_Object = MibTableColumn
t11NsRegSymbolicNodeName = _T11NsRegSymbolicNodeName_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 2, 1, 14),
    _T11NsRegSymbolicNodeName_Type()
)
t11NsRegSymbolicNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsRegSymbolicNodeName.setStatus("current")


class _T11NsRegFc4Features_Type(OctetString):
    """Custom type t11NsRegFc4Features based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(128, 128),
    )


_T11NsRegFc4Features_Type.__name__ = "OctetString"
_T11NsRegFc4Features_Object = MibTableColumn
t11NsRegFc4Features = _T11NsRegFc4Features_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 2, 1, 15),
    _T11NsRegFc4Features_Type()
)
t11NsRegFc4Features.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsRegFc4Features.setStatus("current")
_T11NsRegFc4DescriptorTable_Object = MibTable
t11NsRegFc4DescriptorTable = _T11NsRegFc4DescriptorTable_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 3)
)
if mibBuilder.loadTexts:
    t11NsRegFc4DescriptorTable.setStatus("current")
_T11NsRegFc4DescriptorEntry_Object = MibTableRow
t11NsRegFc4DescriptorEntry = _T11NsRegFc4DescriptorEntry_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 3, 1)
)
t11NsRegFc4DescriptorEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-NAME-SERVER-MIB", "t11NsInfoSubsetIndex"),
    (0, "T11-FC-NAME-SERVER-MIB", "t11NsRegFabricIndex"),
    (0, "T11-FC-NAME-SERVER-MIB", "t11NsRegPortIdentifier"),
    (0, "T11-FC-NAME-SERVER-MIB", "t11NsRegFc4TypeValue"),
)
if mibBuilder.loadTexts:
    t11NsRegFc4DescriptorEntry.setStatus("current")


class _T11NsRegFc4TypeValue_Type(Unsigned32):
    """Custom type t11NsRegFc4TypeValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_T11NsRegFc4TypeValue_Type.__name__ = "Unsigned32"
_T11NsRegFc4TypeValue_Object = MibTableColumn
t11NsRegFc4TypeValue = _T11NsRegFc4TypeValue_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 3, 1, 1),
    _T11NsRegFc4TypeValue_Type()
)
t11NsRegFc4TypeValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11NsRegFc4TypeValue.setStatus("current")


class _T11NsRegFc4Descriptor_Type(OctetString):
    """Custom type t11NsRegFc4Descriptor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_T11NsRegFc4Descriptor_Type.__name__ = "OctetString"
_T11NsRegFc4Descriptor_Object = MibTableColumn
t11NsRegFc4Descriptor = _T11NsRegFc4Descriptor_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 3, 1, 2),
    _T11NsRegFc4Descriptor_Type()
)
t11NsRegFc4Descriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsRegFc4Descriptor.setStatus("current")
_T11NsRejectTable_Object = MibTable
t11NsRejectTable = _T11NsRejectTable_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 4)
)
if mibBuilder.loadTexts:
    t11NsRejectTable.setStatus("current")
_T11NsRejectEntry_Object = MibTableRow
t11NsRejectEntry = _T11NsRejectEntry_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 4, 1)
)
t11NsRejectEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-NAME-SERVER-MIB", "t11NsInfoSubsetIndex"),
    (0, "T11-FC-NAME-SERVER-MIB", "t11NsRegFabricIndex"),
    (0, "T11-FC-NAME-SERVER-MIB", "t11NsRegPortIdentifier"),
)
if mibBuilder.loadTexts:
    t11NsRejectEntry.setStatus("current")


class _T11NsRejectCtCommandString_Type(OctetString):
    """Custom type t11NsRejectCtCommandString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_T11NsRejectCtCommandString_Type.__name__ = "OctetString"
_T11NsRejectCtCommandString_Object = MibTableColumn
t11NsRejectCtCommandString = _T11NsRejectCtCommandString_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 4, 1, 1),
    _T11NsRejectCtCommandString_Type()
)
t11NsRejectCtCommandString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsRejectCtCommandString.setStatus("current")
_T11NsRejectReasonCode_Type = T11NsGs4RejectReasonCode
_T11NsRejectReasonCode_Object = MibTableColumn
t11NsRejectReasonCode = _T11NsRejectReasonCode_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 4, 1, 2),
    _T11NsRejectReasonCode_Type()
)
t11NsRejectReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsRejectReasonCode.setStatus("current")
_T11NsRejReasonCodeExp_Type = T11NsRejReasonCodeExpl
_T11NsRejReasonCodeExp_Object = MibTableColumn
t11NsRejReasonCodeExp = _T11NsRejReasonCodeExp_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 4, 1, 3),
    _T11NsRejReasonCodeExp_Type()
)
t11NsRejReasonCodeExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsRejReasonCodeExp.setStatus("current")


class _T11NsRejReasonVendorCode_Type(OctetString):
    """Custom type t11NsRejReasonVendorCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_T11NsRejReasonVendorCode_Type.__name__ = "OctetString"
_T11NsRejReasonVendorCode_Object = MibTableColumn
t11NsRejReasonVendorCode = _T11NsRejReasonVendorCode_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 1, 4, 1, 4),
    _T11NsRejReasonVendorCode_Type()
)
t11NsRejReasonVendorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsRejReasonVendorCode.setStatus("current")
_T11NsStatistics_ObjectIdentity = ObjectIdentity
t11NsStatistics = _T11NsStatistics_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 135, 1, 2)
)
_T11NsStatsTable_Object = MibTable
t11NsStatsTable = _T11NsStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 2, 1)
)
if mibBuilder.loadTexts:
    t11NsStatsTable.setStatus("current")
_T11NsStatsEntry_Object = MibTableRow
t11NsStatsEntry = _T11NsStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 2, 1, 1)
)
t11NsStatsEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-NAME-SERVER-MIB", "t11NsInfoSubsetIndex"),
    (0, "T11-FC-NAME-SERVER-MIB", "t11NsRegFabricIndex"),
)
if mibBuilder.loadTexts:
    t11NsStatsEntry.setStatus("current")
_T11NsInGetReqs_Type = Counter32
_T11NsInGetReqs_Object = MibTableColumn
t11NsInGetReqs = _T11NsInGetReqs_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 2, 1, 1, 1),
    _T11NsInGetReqs_Type()
)
t11NsInGetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsInGetReqs.setStatus("current")
_T11NsOutGetReqs_Type = Counter32
_T11NsOutGetReqs_Object = MibTableColumn
t11NsOutGetReqs = _T11NsOutGetReqs_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 2, 1, 1, 2),
    _T11NsOutGetReqs_Type()
)
t11NsOutGetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsOutGetReqs.setStatus("current")
_T11NsInRegReqs_Type = Counter32
_T11NsInRegReqs_Object = MibTableColumn
t11NsInRegReqs = _T11NsInRegReqs_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 2, 1, 1, 3),
    _T11NsInRegReqs_Type()
)
t11NsInRegReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsInRegReqs.setStatus("current")
_T11NsInDeRegReqs_Type = Counter32
_T11NsInDeRegReqs_Object = MibTableColumn
t11NsInDeRegReqs = _T11NsInDeRegReqs_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 2, 1, 1, 4),
    _T11NsInDeRegReqs_Type()
)
t11NsInDeRegReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsInDeRegReqs.setStatus("current")
_T11NsInRscns_Type = Counter32
_T11NsInRscns_Object = MibTableColumn
t11NsInRscns = _T11NsInRscns_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 2, 1, 1, 5),
    _T11NsInRscns_Type()
)
t11NsInRscns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsInRscns.setStatus("current")
_T11NsOutRscns_Type = Counter32
_T11NsOutRscns_Object = MibTableColumn
t11NsOutRscns = _T11NsOutRscns_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 2, 1, 1, 6),
    _T11NsOutRscns_Type()
)
t11NsOutRscns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsOutRscns.setStatus("current")
_T11NsRejects_Type = Counter32
_T11NsRejects_Object = MibTableColumn
t11NsRejects = _T11NsRejects_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 2, 1, 1, 7),
    _T11NsRejects_Type()
)
t11NsRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsRejects.setStatus("current")
_T11NsDatabaseFull_Type = TruthValue
_T11NsDatabaseFull_Object = MibTableColumn
t11NsDatabaseFull = _T11NsDatabaseFull_Object(
    (1, 3, 6, 1, 2, 1, 135, 1, 2, 1, 1, 8),
    _T11NsDatabaseFull_Type()
)
t11NsDatabaseFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11NsDatabaseFull.setStatus("current")
_T11NsMIBConformance_ObjectIdentity = ObjectIdentity
t11NsMIBConformance = _T11NsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 135, 2)
)
_T11NsMIBCompliances_ObjectIdentity = ObjectIdentity
t11NsMIBCompliances = _T11NsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 135, 2, 1)
)
_T11NsMIBGroups_ObjectIdentity = ObjectIdentity
t11NsMIBGroups = _T11NsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 135, 2, 2)
)

# Managed Objects groups

t11NsDBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 135, 2, 2, 1)
)
t11NsDBGroup.setObjects(
      *(("T11-FC-NAME-SERVER-MIB", "t11NsInfoSubsetSwitchIndex"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsInfoSubsetTableLastChange"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsInfoSubsetNumRows"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsRegPortName"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsRegNodeName"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsRegClassOfSvc"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsRegNodeIpAddress"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsRegProcAssoc"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsRegFc4Type"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsRegPortType"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsRegPortIpAddress"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsRegFabricPortName"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsRegHardAddress"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsRegSymbolicPortName"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsRegSymbolicNodeName"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsRegFc4Features"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsRegFc4Descriptor"))
)
if mibBuilder.loadTexts:
    t11NsDBGroup.setStatus("current")

t11NsRequestStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 135, 2, 2, 2)
)
t11NsRequestStatsGroup.setObjects(
      *(("T11-FC-NAME-SERVER-MIB", "t11NsInGetReqs"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsOutGetReqs"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsInRegReqs"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsInDeRegReqs"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsDatabaseFull"))
)
if mibBuilder.loadTexts:
    t11NsRequestStatsGroup.setStatus("current")

t11NsRscnStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 135, 2, 2, 3)
)
t11NsRscnStatsGroup.setObjects(
      *(("T11-FC-NAME-SERVER-MIB", "t11NsInRscns"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsOutRscns"))
)
if mibBuilder.loadTexts:
    t11NsRscnStatsGroup.setStatus("current")

t11NsRejectStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 135, 2, 2, 4)
)
t11NsRejectStatsGroup.setObjects(
      *(("T11-FC-NAME-SERVER-MIB", "t11NsInfoSubsetTotalRejects"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsRejects"))
)
if mibBuilder.loadTexts:
    t11NsRejectStatsGroup.setStatus("current")

t11NsNotifyControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 135, 2, 2, 5)
)
t11NsNotifyControlGroup.setObjects(
      *(("T11-FC-NAME-SERVER-MIB", "t11NsRejectCtCommandString"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsRejectReasonCode"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsRejReasonCodeExp"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsRejReasonVendorCode"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsInfoSubsetRejReqNotfyEnable"))
)
if mibBuilder.loadTexts:
    t11NsNotifyControlGroup.setStatus("current")


# Notification objects

t11NsRejectRegNotify = NotificationType(
    (1, 3, 6, 1, 2, 1, 135, 0, 1)
)
t11NsRejectRegNotify.setObjects(
      *(("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamLocalSwitchWwn"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsRegPortName"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsRejectCtCommandString"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsRejectReasonCode"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsRejReasonCodeExp"),
        ("T11-FC-NAME-SERVER-MIB", "t11NsRejReasonVendorCode"))
)
if mibBuilder.loadTexts:
    t11NsRejectRegNotify.setStatus(
        "current"
    )


# Notifications groups

t11NsNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 135, 2, 2, 6)
)
t11NsNotifyGroup.setObjects(
    ("T11-FC-NAME-SERVER-MIB", "t11NsRejectRegNotify")
)
if mibBuilder.loadTexts:
    t11NsNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

t11NsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 135, 2, 1, 1)
)
if mibBuilder.loadTexts:
    t11NsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "T11-FC-NAME-SERVER-MIB",
    **{"T11NsGs4RejectReasonCode": T11NsGs4RejectReasonCode,
       "T11NsRejReasonCodeExpl": T11NsRejReasonCodeExpl,
       "t11FcNameServerMIB": t11FcNameServerMIB,
       "t11NsNotifications": t11NsNotifications,
       "t11NsRejectRegNotify": t11NsRejectRegNotify,
       "t11NsMIBObjects": t11NsMIBObjects,
       "t11NsStatus": t11NsStatus,
       "t11NsInfoSubsetTable": t11NsInfoSubsetTable,
       "t11NsInfoSubsetEntry": t11NsInfoSubsetEntry,
       "t11NsInfoSubsetIndex": t11NsInfoSubsetIndex,
       "t11NsInfoSubsetSwitchIndex": t11NsInfoSubsetSwitchIndex,
       "t11NsInfoSubsetTableLastChange": t11NsInfoSubsetTableLastChange,
       "t11NsInfoSubsetNumRows": t11NsInfoSubsetNumRows,
       "t11NsInfoSubsetTotalRejects": t11NsInfoSubsetTotalRejects,
       "t11NsInfoSubsetRejReqNotfyEnable": t11NsInfoSubsetRejReqNotfyEnable,
       "t11NsRegTable": t11NsRegTable,
       "t11NsRegEntry": t11NsRegEntry,
       "t11NsRegFabricIndex": t11NsRegFabricIndex,
       "t11NsRegPortIdentifier": t11NsRegPortIdentifier,
       "t11NsRegPortName": t11NsRegPortName,
       "t11NsRegNodeName": t11NsRegNodeName,
       "t11NsRegClassOfSvc": t11NsRegClassOfSvc,
       "t11NsRegNodeIpAddress": t11NsRegNodeIpAddress,
       "t11NsRegProcAssoc": t11NsRegProcAssoc,
       "t11NsRegFc4Type": t11NsRegFc4Type,
       "t11NsRegPortType": t11NsRegPortType,
       "t11NsRegPortIpAddress": t11NsRegPortIpAddress,
       "t11NsRegFabricPortName": t11NsRegFabricPortName,
       "t11NsRegHardAddress": t11NsRegHardAddress,
       "t11NsRegSymbolicPortName": t11NsRegSymbolicPortName,
       "t11NsRegSymbolicNodeName": t11NsRegSymbolicNodeName,
       "t11NsRegFc4Features": t11NsRegFc4Features,
       "t11NsRegFc4DescriptorTable": t11NsRegFc4DescriptorTable,
       "t11NsRegFc4DescriptorEntry": t11NsRegFc4DescriptorEntry,
       "t11NsRegFc4TypeValue": t11NsRegFc4TypeValue,
       "t11NsRegFc4Descriptor": t11NsRegFc4Descriptor,
       "t11NsRejectTable": t11NsRejectTable,
       "t11NsRejectEntry": t11NsRejectEntry,
       "t11NsRejectCtCommandString": t11NsRejectCtCommandString,
       "t11NsRejectReasonCode": t11NsRejectReasonCode,
       "t11NsRejReasonCodeExp": t11NsRejReasonCodeExp,
       "t11NsRejReasonVendorCode": t11NsRejReasonVendorCode,
       "t11NsStatistics": t11NsStatistics,
       "t11NsStatsTable": t11NsStatsTable,
       "t11NsStatsEntry": t11NsStatsEntry,
       "t11NsInGetReqs": t11NsInGetReqs,
       "t11NsOutGetReqs": t11NsOutGetReqs,
       "t11NsInRegReqs": t11NsInRegReqs,
       "t11NsInDeRegReqs": t11NsInDeRegReqs,
       "t11NsInRscns": t11NsInRscns,
       "t11NsOutRscns": t11NsOutRscns,
       "t11NsRejects": t11NsRejects,
       "t11NsDatabaseFull": t11NsDatabaseFull,
       "t11NsMIBConformance": t11NsMIBConformance,
       "t11NsMIBCompliances": t11NsMIBCompliances,
       "t11NsMIBCompliance": t11NsMIBCompliance,
       "t11NsMIBGroups": t11NsMIBGroups,
       "t11NsDBGroup": t11NsDBGroup,
       "t11NsRequestStatsGroup": t11NsRequestStatsGroup,
       "t11NsRscnStatsGroup": t11NsRscnStatsGroup,
       "t11NsRejectStatsGroup": t11NsRejectStatsGroup,
       "t11NsNotifyControlGroup": t11NsNotifyControlGroup,
       "t11NsNotifyGroup": t11NsNotifyGroup}
)
