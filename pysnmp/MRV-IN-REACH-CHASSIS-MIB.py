# SNMP MIB module (MRV-IN-REACH-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MRV-IN-REACH-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:39 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

(AddressType,
 HardwareType,
 IOType,
 mrvInReachProductDivision) = mibBuilder.importSymbols(
    "MRV-IN-REACH-PRODUCT-DIVISION-MIB",
    "AddressType",
    "HardwareType",
    "IOType",
    "mrvInReachProductDivision")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class NetworkType(Integer32):
    """Custom type NetworkType based on Integer32"""
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
        *(("atm", 10),
          ("ethernet", 3),
          ("ethernetRepeater", 7),
          ("fddi", 5),
          ("fddiConcentrator", 9),
          ("isdn", 11),
          ("other", 2),
          ("switchedEthernet", 13),
          ("switchplane", 12),
          ("tokenRing", 4),
          ("tokenRingConcentrator", 8),
          ("unknown", 1),
          ("wan", 6))
    )





class SerialNumber(OctetString):
    """Custom type SerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )





class Letter(Integer32):
    """Custom type Letter based on Integer32"""
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
        *(("a", 1),
          ("b", 2),
          ("c", 3),
          ("d", 4),
          ("e", 5),
          ("f", 6),
          ("g", 7),
          ("h", 8),
          ("i", 9),
          ("j", 10),
          ("k", 11),
          ("l", 12),
          ("m", 13),
          ("n", 14),
          ("o", 15),
          ("p", 16),
          ("q", 17),
          ("r", 18),
          ("s", 19),
          ("t", 20),
          ("u", 21),
          ("v", 22),
          ("w", 23),
          ("x", 24),
          ("y", 25),
          ("z", 26))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XChassis_ObjectIdentity = ObjectIdentity
xChassis = _XChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 16)
)
_XChassisBasic_ObjectIdentity = ObjectIdentity
xChassisBasic = _XChassisBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 16, 1)
)
_BasicBase802Address_Type = MacAddress
_BasicBase802Address_Object = MibScalar
basicBase802Address = _BasicBase802Address_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 1, 1),
    _BasicBase802Address_Type()
)
basicBase802Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicBase802Address.setStatus("mandatory")
_BasicSlot_Type = Integer32
_BasicSlot_Object = MibScalar
basicSlot = _BasicSlot_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 1, 2),
    _BasicSlot_Type()
)
basicSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicSlot.setStatus("mandatory")
_BasicSlotNumber_Type = Integer32
_BasicSlotNumber_Object = MibScalar
basicSlotNumber = _BasicSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 1, 3),
    _BasicSlotNumber_Type()
)
basicSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicSlotNumber.setStatus("mandatory")
_BasicNewBase802Address_Type = MacAddress
_BasicNewBase802Address_Object = MibScalar
basicNewBase802Address = _BasicNewBase802Address_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 1, 4),
    _BasicNewBase802Address_Type()
)
basicNewBase802Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicNewBase802Address.setStatus("mandatory")
_XSegment_ObjectIdentity = ObjectIdentity
xSegment = _XSegment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 16, 2)
)
_SegmentTable_Object = MibTable
segmentTable = _SegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 2, 1)
)
if mibBuilder.loadTexts:
    segmentTable.setStatus("mandatory")
_SegmentEntry_Object = MibTableRow
segmentEntry = _SegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 2, 1, 1)
)
segmentEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHASSIS-MIB", "segmentType"),
    (0, "MRV-IN-REACH-CHASSIS-MIB", "segmentIndex"),
)
if mibBuilder.loadTexts:
    segmentEntry.setStatus("mandatory")
_SegmentType_Type = NetworkType
_SegmentType_Object = MibTableColumn
segmentType = _SegmentType_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 2, 1, 1, 1),
    _SegmentType_Type()
)
segmentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentType.setStatus("mandatory")
_SegmentIndex_Type = Letter
_SegmentIndex_Object = MibTableColumn
segmentIndex = _SegmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 2, 1, 1, 2),
    _SegmentIndex_Type()
)
segmentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentIndex.setStatus("mandatory")
_XPort_ObjectIdentity = ObjectIdentity
xPort = _XPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 16, 3)
)
_PortIOCardType_Type = IOType
_PortIOCardType_Object = MibScalar
portIOCardType = _PortIOCardType_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 3, 1),
    _PortIOCardType_Type()
)
portIOCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIOCardType.setStatus("mandatory")
_PortIOCardSerialNumber_Type = SerialNumber
_PortIOCardSerialNumber_Object = MibScalar
portIOCardSerialNumber = _PortIOCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 3, 2),
    _PortIOCardSerialNumber_Type()
)
portIOCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIOCardSerialNumber.setStatus("mandatory")


class _PortIOCardOperStatus_Type(Integer32):
    """Custom type portIOCardOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("good", 3),
          ("mismatch", 2),
          ("unknown", 1))
    )


_PortIOCardOperStatus_Type.__name__ = "Integer32"
_PortIOCardOperStatus_Object = MibScalar
portIOCardOperStatus = _PortIOCardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 3, 3),
    _PortIOCardOperStatus_Type()
)
portIOCardOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIOCardOperStatus.setStatus("mandatory")
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 3, 4)
)
if mibBuilder.loadTexts:
    portTable.setStatus("mandatory")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 3, 4, 1)
)
portEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHASSIS-MIB", "portType"),
    (0, "MRV-IN-REACH-CHASSIS-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("mandatory")
_PortType_Type = NetworkType
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 3, 4, 1, 1),
    _PortType_Type()
)
portType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portType.setStatus("mandatory")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 3, 4, 1, 2),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("mandatory")
_XController_ObjectIdentity = ObjectIdentity
xController = _XController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 16, 4)
)
_ControllerTable_Object = MibTable
controllerTable = _ControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 4, 1)
)
if mibBuilder.loadTexts:
    controllerTable.setStatus("mandatory")
_ControllerEntry_Object = MibTableRow
controllerEntry = _ControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 4, 1, 1)
)
controllerEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHASSIS-MIB", "controllerType"),
    (0, "MRV-IN-REACH-CHASSIS-MIB", "controllerIndex"),
)
if mibBuilder.loadTexts:
    controllerEntry.setStatus("mandatory")
_ControllerType_Type = NetworkType
_ControllerType_Object = MibTableColumn
controllerType = _ControllerType_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 4, 1, 1, 1),
    _ControllerType_Type()
)
controllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerType.setStatus("mandatory")
_ControllerIndex_Type = Integer32
_ControllerIndex_Object = MibTableColumn
controllerIndex = _ControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 4, 1, 1, 2),
    _ControllerIndex_Type()
)
controllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerIndex.setStatus("mandatory")
_ControllerNetwork_Type = ObjectIdentifier
_ControllerNetwork_Object = MibTableColumn
controllerNetwork = _ControllerNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 4, 1, 1, 3),
    _ControllerNetwork_Type()
)
controllerNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controllerNetwork.setStatus("mandatory")
_XInterface_ObjectIdentity = ObjectIdentity
xInterface = _XInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 16, 5)
)
_InterfaceTable_Object = MibTable
interfaceTable = _InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 5, 1)
)
if mibBuilder.loadTexts:
    interfaceTable.setStatus("mandatory")
_InterfaceEntry_Object = MibTableRow
interfaceEntry = _InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 5, 1, 1)
)
interfaceEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHASSIS-MIB", "interfaceIndex"),
)
if mibBuilder.loadTexts:
    interfaceEntry.setStatus("mandatory")
_InterfaceIndex_Type = Integer32
_InterfaceIndex_Object = MibTableColumn
interfaceIndex = _InterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 5, 1, 1, 1),
    _InterfaceIndex_Type()
)
interfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceIndex.setStatus("mandatory")
_InterfaceNetwork_Type = ObjectIdentifier
_InterfaceNetwork_Object = MibTableColumn
interfaceNetwork = _InterfaceNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 5, 1, 1, 2),
    _InterfaceNetwork_Type()
)
interfaceNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceNetwork.setStatus("mandatory")
_XSlotBootControl_ObjectIdentity = ObjectIdentity
xSlotBootControl = _XSlotBootControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 16, 6)
)
_SlotBootControlTable_Object = MibTable
slotBootControlTable = _SlotBootControlTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 1)
)
if mibBuilder.loadTexts:
    slotBootControlTable.setStatus("mandatory")
_SlotBootControlEntry_Object = MibTableRow
slotBootControlEntry = _SlotBootControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 1, 1)
)
slotBootControlEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHASSIS-MIB", "slotBootControlSlot"),
    (0, "MRV-IN-REACH-CHASSIS-MIB", "slotBootControlIndex"),
)
if mibBuilder.loadTexts:
    slotBootControlEntry.setStatus("mandatory")
_SlotBootControlSlot_Type = Integer32
_SlotBootControlSlot_Object = MibTableColumn
slotBootControlSlot = _SlotBootControlSlot_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 1, 1, 1),
    _SlotBootControlSlot_Type()
)
slotBootControlSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBootControlSlot.setStatus("mandatory")
_SlotBootControlIndex_Type = Integer32
_SlotBootControlIndex_Object = MibTableColumn
slotBootControlIndex = _SlotBootControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 1, 1, 2),
    _SlotBootControlIndex_Type()
)
slotBootControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBootControlIndex.setStatus("mandatory")


class _SlotBootControlStatus_Type(Integer32):
    """Custom type slotBootControlStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SlotBootControlStatus_Type.__name__ = "Integer32"
_SlotBootControlStatus_Object = MibTableColumn
slotBootControlStatus = _SlotBootControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 1, 1, 3),
    _SlotBootControlStatus_Type()
)
slotBootControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBootControlStatus.setStatus("mandatory")
_SlotBootControlController_Type = ObjectIdentifier
_SlotBootControlController_Object = MibTableColumn
slotBootControlController = _SlotBootControlController_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 1, 1, 4),
    _SlotBootControlController_Type()
)
slotBootControlController.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBootControlController.setStatus("mandatory")
_SlotBootControlNetwork_Type = ObjectIdentifier
_SlotBootControlNetwork_Object = MibTableColumn
slotBootControlNetwork = _SlotBootControlNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 1, 1, 5),
    _SlotBootControlNetwork_Type()
)
slotBootControlNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBootControlNetwork.setStatus("mandatory")


class _SlotBootControlMopFile_Type(DisplayString):
    """Custom type slotBootControlMopFile based on DisplayString"""
    defaultHexValue = "00"

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SlotBootControlMopFile_Type.__name__ = "DisplayString"
_SlotBootControlMopFile_Object = MibTableColumn
slotBootControlMopFile = _SlotBootControlMopFile_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 1, 1, 6),
    _SlotBootControlMopFile_Type()
)
slotBootControlMopFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBootControlMopFile.setStatus("mandatory")


class _SlotBootControlInternetFile_Type(DisplayString):
    """Custom type slotBootControlInternetFile based on DisplayString"""
    defaultHexValue = "00"

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SlotBootControlInternetFile_Type.__name__ = "DisplayString"
_SlotBootControlInternetFile_Object = MibTableColumn
slotBootControlInternetFile = _SlotBootControlInternetFile_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 1, 1, 7),
    _SlotBootControlInternetFile_Type()
)
slotBootControlInternetFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBootControlInternetFile.setStatus("mandatory")


class _SlotBootControlInternetAddress_Type(IpAddress):
    """Custom type slotBootControlInternetAddress based on IpAddress"""
    defaultValue = 0


_SlotBootControlInternetAddress_Object = MibTableColumn
slotBootControlInternetAddress = _SlotBootControlInternetAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 1, 1, 8),
    _SlotBootControlInternetAddress_Type()
)
slotBootControlInternetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBootControlInternetAddress.setStatus("mandatory")


class _SlotBootControlInternetServer_Type(IpAddress):
    """Custom type slotBootControlInternetServer based on IpAddress"""
    defaultValue = 0


_SlotBootControlInternetServer_Object = MibTableColumn
slotBootControlInternetServer = _SlotBootControlInternetServer_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 1, 1, 9),
    _SlotBootControlInternetServer_Type()
)
slotBootControlInternetServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBootControlInternetServer.setStatus("mandatory")


class _SlotBootControlInternetGateway_Type(IpAddress):
    """Custom type slotBootControlInternetGateway based on IpAddress"""
    defaultValue = 0


_SlotBootControlInternetGateway_Object = MibTableColumn
slotBootControlInternetGateway = _SlotBootControlInternetGateway_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 1, 1, 10),
    _SlotBootControlInternetGateway_Type()
)
slotBootControlInternetGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBootControlInternetGateway.setStatus("mandatory")


class _SlotBootControlInternetDelimiter_Type(DisplayString):
    """Custom type slotBootControlInternetDelimiter based on DisplayString"""
    defaultHexValue = "00"

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_SlotBootControlInternetDelimiter_Type.__name__ = "DisplayString"
_SlotBootControlInternetDelimiter_Object = MibTableColumn
slotBootControlInternetDelimiter = _SlotBootControlInternetDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 1, 1, 11),
    _SlotBootControlInternetDelimiter_Type()
)
slotBootControlInternetDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBootControlInternetDelimiter.setStatus("mandatory")
_SlotBootControlFlagTable_Object = MibTable
slotBootControlFlagTable = _SlotBootControlFlagTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 2)
)
if mibBuilder.loadTexts:
    slotBootControlFlagTable.setStatus("mandatory")
_SlotBootControlFlagEntry_Object = MibTableRow
slotBootControlFlagEntry = _SlotBootControlFlagEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 2, 1)
)
slotBootControlFlagEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHASSIS-MIB", "slotBootControlSlot"),
    (0, "MRV-IN-REACH-CHASSIS-MIB", "slotBootControlIndex"),
)
if mibBuilder.loadTexts:
    slotBootControlFlagEntry.setStatus("mandatory")


class _SlotBootControlFlagLoadBootpTftp_Type(Integer32):
    """Custom type slotBootControlFlagLoadBootpTftp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SlotBootControlFlagLoadBootpTftp_Type.__name__ = "Integer32"
_SlotBootControlFlagLoadBootpTftp_Object = MibTableColumn
slotBootControlFlagLoadBootpTftp = _SlotBootControlFlagLoadBootpTftp_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 2, 1, 1),
    _SlotBootControlFlagLoadBootpTftp_Type()
)
slotBootControlFlagLoadBootpTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBootControlFlagLoadBootpTftp.setStatus("mandatory")


class _SlotBootControlFlagParamBootpTftp_Type(Integer32):
    """Custom type slotBootControlFlagParamBootpTftp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SlotBootControlFlagParamBootpTftp_Type.__name__ = "Integer32"
_SlotBootControlFlagParamBootpTftp_Object = MibTableColumn
slotBootControlFlagParamBootpTftp = _SlotBootControlFlagParamBootpTftp_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 2, 1, 2),
    _SlotBootControlFlagParamBootpTftp_Type()
)
slotBootControlFlagParamBootpTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBootControlFlagParamBootpTftp.setStatus("mandatory")


class _SlotBootControlFlagDumpBootpTftp_Type(Integer32):
    """Custom type slotBootControlFlagDumpBootpTftp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SlotBootControlFlagDumpBootpTftp_Type.__name__ = "Integer32"
_SlotBootControlFlagDumpBootpTftp_Object = MibTableColumn
slotBootControlFlagDumpBootpTftp = _SlotBootControlFlagDumpBootpTftp_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 2, 1, 3),
    _SlotBootControlFlagDumpBootpTftp_Type()
)
slotBootControlFlagDumpBootpTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBootControlFlagDumpBootpTftp.setStatus("mandatory")


class _SlotBootControlFlagLoadTftpDirect_Type(Integer32):
    """Custom type slotBootControlFlagLoadTftpDirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SlotBootControlFlagLoadTftpDirect_Type.__name__ = "Integer32"
_SlotBootControlFlagLoadTftpDirect_Object = MibTableColumn
slotBootControlFlagLoadTftpDirect = _SlotBootControlFlagLoadTftpDirect_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 2, 1, 4),
    _SlotBootControlFlagLoadTftpDirect_Type()
)
slotBootControlFlagLoadTftpDirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBootControlFlagLoadTftpDirect.setStatus("mandatory")


class _SlotBootControlFlagParamTftpDirect_Type(Integer32):
    """Custom type slotBootControlFlagParamTftpDirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SlotBootControlFlagParamTftpDirect_Type.__name__ = "Integer32"
_SlotBootControlFlagParamTftpDirect_Object = MibTableColumn
slotBootControlFlagParamTftpDirect = _SlotBootControlFlagParamTftpDirect_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 2, 1, 5),
    _SlotBootControlFlagParamTftpDirect_Type()
)
slotBootControlFlagParamTftpDirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBootControlFlagParamTftpDirect.setStatus("mandatory")


class _SlotBootControlFlagDumpTftpDirect_Type(Integer32):
    """Custom type slotBootControlFlagDumpTftpDirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SlotBootControlFlagDumpTftpDirect_Type.__name__ = "Integer32"
_SlotBootControlFlagDumpTftpDirect_Object = MibTableColumn
slotBootControlFlagDumpTftpDirect = _SlotBootControlFlagDumpTftpDirect_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 2, 1, 6),
    _SlotBootControlFlagDumpTftpDirect_Type()
)
slotBootControlFlagDumpTftpDirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBootControlFlagDumpTftpDirect.setStatus("mandatory")


class _SlotBootControlFlagLoadLocal_Type(Integer32):
    """Custom type slotBootControlFlagLoadLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SlotBootControlFlagLoadLocal_Type.__name__ = "Integer32"
_SlotBootControlFlagLoadLocal_Object = MibTableColumn
slotBootControlFlagLoadLocal = _SlotBootControlFlagLoadLocal_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 2, 1, 7),
    _SlotBootControlFlagLoadLocal_Type()
)
slotBootControlFlagLoadLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBootControlFlagLoadLocal.setStatus("mandatory")


class _SlotBootControlFlagParamLocal_Type(Integer32):
    """Custom type slotBootControlFlagParamLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SlotBootControlFlagParamLocal_Type.__name__ = "Integer32"
_SlotBootControlFlagParamLocal_Object = MibTableColumn
slotBootControlFlagParamLocal = _SlotBootControlFlagParamLocal_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 2, 1, 8),
    _SlotBootControlFlagParamLocal_Type()
)
slotBootControlFlagParamLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBootControlFlagParamLocal.setStatus("mandatory")


class _SlotBootControlFlagDumpLocal_Type(Integer32):
    """Custom type slotBootControlFlagDumpLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SlotBootControlFlagDumpLocal_Type.__name__ = "Integer32"
_SlotBootControlFlagDumpLocal_Object = MibTableColumn
slotBootControlFlagDumpLocal = _SlotBootControlFlagDumpLocal_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 2, 1, 9),
    _SlotBootControlFlagDumpLocal_Type()
)
slotBootControlFlagDumpLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBootControlFlagDumpLocal.setStatus("mandatory")


class _SlotBootControlFlagLoadMop_Type(Integer32):
    """Custom type slotBootControlFlagLoadMop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SlotBootControlFlagLoadMop_Type.__name__ = "Integer32"
_SlotBootControlFlagLoadMop_Object = MibTableColumn
slotBootControlFlagLoadMop = _SlotBootControlFlagLoadMop_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 2, 1, 10),
    _SlotBootControlFlagLoadMop_Type()
)
slotBootControlFlagLoadMop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBootControlFlagLoadMop.setStatus("mandatory")


class _SlotBootControlFlagParamMop_Type(Integer32):
    """Custom type slotBootControlFlagParamMop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SlotBootControlFlagParamMop_Type.__name__ = "Integer32"
_SlotBootControlFlagParamMop_Object = MibTableColumn
slotBootControlFlagParamMop = _SlotBootControlFlagParamMop_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 2, 1, 11),
    _SlotBootControlFlagParamMop_Type()
)
slotBootControlFlagParamMop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBootControlFlagParamMop.setStatus("mandatory")


class _SlotBootControlFlagDumpMop_Type(Integer32):
    """Custom type slotBootControlFlagDumpMop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SlotBootControlFlagDumpMop_Type.__name__ = "Integer32"
_SlotBootControlFlagDumpMop_Object = MibTableColumn
slotBootControlFlagDumpMop = _SlotBootControlFlagDumpMop_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 2, 1, 12),
    _SlotBootControlFlagDumpMop_Type()
)
slotBootControlFlagDumpMop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBootControlFlagDumpMop.setStatus("mandatory")


class _SlotBootControlFlagLoadXmop_Type(Integer32):
    """Custom type slotBootControlFlagLoadXmop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SlotBootControlFlagLoadXmop_Type.__name__ = "Integer32"
_SlotBootControlFlagLoadXmop_Object = MibTableColumn
slotBootControlFlagLoadXmop = _SlotBootControlFlagLoadXmop_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 2, 1, 13),
    _SlotBootControlFlagLoadXmop_Type()
)
slotBootControlFlagLoadXmop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBootControlFlagLoadXmop.setStatus("mandatory")


class _SlotBootControlFlagParamXmop_Type(Integer32):
    """Custom type slotBootControlFlagParamXmop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SlotBootControlFlagParamXmop_Type.__name__ = "Integer32"
_SlotBootControlFlagParamXmop_Object = MibTableColumn
slotBootControlFlagParamXmop = _SlotBootControlFlagParamXmop_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 2, 1, 14),
    _SlotBootControlFlagParamXmop_Type()
)
slotBootControlFlagParamXmop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBootControlFlagParamXmop.setStatus("mandatory")


class _SlotBootControlFlagDumpXmop_Type(Integer32):
    """Custom type slotBootControlFlagDumpXmop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SlotBootControlFlagDumpXmop_Type.__name__ = "Integer32"
_SlotBootControlFlagDumpXmop_Object = MibTableColumn
slotBootControlFlagDumpXmop = _SlotBootControlFlagDumpXmop_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 2, 1, 15),
    _SlotBootControlFlagDumpXmop_Type()
)
slotBootControlFlagDumpXmop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBootControlFlagDumpXmop.setStatus("mandatory")


class _SlotBootControlFlagLoadRarpTftp_Type(Integer32):
    """Custom type slotBootControlFlagLoadRarpTftp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SlotBootControlFlagLoadRarpTftp_Type.__name__ = "Integer32"
_SlotBootControlFlagLoadRarpTftp_Object = MibTableColumn
slotBootControlFlagLoadRarpTftp = _SlotBootControlFlagLoadRarpTftp_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 2, 1, 16),
    _SlotBootControlFlagLoadRarpTftp_Type()
)
slotBootControlFlagLoadRarpTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBootControlFlagLoadRarpTftp.setStatus("mandatory")


class _SlotBootControlFlagParamRarpTftp_Type(Integer32):
    """Custom type slotBootControlFlagParamRarpTftp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SlotBootControlFlagParamRarpTftp_Type.__name__ = "Integer32"
_SlotBootControlFlagParamRarpTftp_Object = MibTableColumn
slotBootControlFlagParamRarpTftp = _SlotBootControlFlagParamRarpTftp_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 2, 1, 17),
    _SlotBootControlFlagParamRarpTftp_Type()
)
slotBootControlFlagParamRarpTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBootControlFlagParamRarpTftp.setStatus("mandatory")


class _SlotBootControlFlagDumpRarpTftp_Type(Integer32):
    """Custom type slotBootControlFlagDumpRarpTftp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SlotBootControlFlagDumpRarpTftp_Type.__name__ = "Integer32"
_SlotBootControlFlagDumpRarpTftp_Object = MibTableColumn
slotBootControlFlagDumpRarpTftp = _SlotBootControlFlagDumpRarpTftp_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 2, 1, 18),
    _SlotBootControlFlagDumpRarpTftp_Type()
)
slotBootControlFlagDumpRarpTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotBootControlFlagDumpRarpTftp.setStatus("mandatory")
_SlotBootControlStorageTable_Object = MibTable
slotBootControlStorageTable = _SlotBootControlStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 3)
)
if mibBuilder.loadTexts:
    slotBootControlStorageTable.setStatus("mandatory")
_SlotBootControlStorageEntry_Object = MibTableRow
slotBootControlStorageEntry = _SlotBootControlStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 3, 1)
)
slotBootControlStorageEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHASSIS-MIB", "slotBootControlStorageClientSlot"),
    (0, "MRV-IN-REACH-CHASSIS-MIB", "slotBootControlStorageServerSlot"),
)
if mibBuilder.loadTexts:
    slotBootControlStorageEntry.setStatus("mandatory")
_SlotBootControlStorageClientSlot_Type = Integer32
_SlotBootControlStorageClientSlot_Object = MibTableColumn
slotBootControlStorageClientSlot = _SlotBootControlStorageClientSlot_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 3, 1, 1),
    _SlotBootControlStorageClientSlot_Type()
)
slotBootControlStorageClientSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBootControlStorageClientSlot.setStatus("mandatory")
_SlotBootControlStorageServerSlot_Type = Integer32
_SlotBootControlStorageServerSlot_Object = MibTableColumn
slotBootControlStorageServerSlot = _SlotBootControlStorageServerSlot_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 3, 1, 2),
    _SlotBootControlStorageServerSlot_Type()
)
slotBootControlStorageServerSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBootControlStorageServerSlot.setStatus("mandatory")


class _SlotBootControlStorageStatus_Type(Integer32):
    """Custom type slotBootControlStorageStatus based on Integer32"""
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
        *(("failed", 2),
          ("notpresent", 4),
          ("ok", 3),
          ("present", 1))
    )


_SlotBootControlStorageStatus_Type.__name__ = "Integer32"
_SlotBootControlStorageStatus_Object = MibTableColumn
slotBootControlStorageStatus = _SlotBootControlStorageStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 3, 1, 3),
    _SlotBootControlStorageStatus_Type()
)
slotBootControlStorageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBootControlStorageStatus.setStatus("mandatory")
_SlotBootControlStorageFailures_Type = Counter32
_SlotBootControlStorageFailures_Object = MibTableColumn
slotBootControlStorageFailures = _SlotBootControlStorageFailures_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 6, 3, 1, 4),
    _SlotBootControlStorageFailures_Type()
)
slotBootControlStorageFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBootControlStorageFailures.setStatus("mandatory")
_XSlot_ObjectIdentity = ObjectIdentity
xSlot = _XSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 16, 7)
)
_SlotTable_Object = MibTable
slotTable = _SlotTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 1)
)
if mibBuilder.loadTexts:
    slotTable.setStatus("mandatory")
_SlotEntry_Object = MibTableRow
slotEntry = _SlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 1, 1)
)
slotEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHASSIS-MIB", "slotIndex"),
)
if mibBuilder.loadTexts:
    slotEntry.setStatus("mandatory")
_SlotIndex_Type = Integer32
_SlotIndex_Object = MibTableColumn
slotIndex = _SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 1, 1, 1),
    _SlotIndex_Type()
)
slotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotIndex.setStatus("mandatory")


class _SlotAdminAction_Type(Integer32):
    """Custom type slotAdminAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("reset", 2),
          ("resetHold", 3))
    )


_SlotAdminAction_Type.__name__ = "Integer32"
_SlotAdminAction_Object = MibTableColumn
slotAdminAction = _SlotAdminAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 1, 1, 2),
    _SlotAdminAction_Type()
)
slotAdminAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotAdminAction.setStatus("mandatory")


class _SlotOperStatus_Type(Integer32):
    """Custom type slotOperStatus based on Integer32"""
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
              64,
              65,
              66,
              67,
              68,
              69)
        )
    )
    namedValues = NamedValues(
        *(("attended", 9),
          ("broken", 67),
          ("dumpRequested", 3),
          ("dumping", 4),
          ("inhibited", 12),
          ("initializing", 8),
          ("internal10", 10),
          ("internal11", 11),
          ("invalidConfigStorage", 14),
          ("loadRequested", 1),
          ("loading", 2),
          ("maxserverCard", 13),
          ("notApplicable", 69),
          ("notResponding", 66),
          ("paramLoading", 6),
          ("paramRequested", 5),
          ("resetHold", 64),
          ("running", 7),
          ("securityLockdown", 15),
          ("selfTest", 65),
          ("unknown", 68))
    )


_SlotOperStatus_Type.__name__ = "Integer32"
_SlotOperStatus_Object = MibTableColumn
slotOperStatus = _SlotOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 1, 1, 3),
    _SlotOperStatus_Type()
)
slotOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotOperStatus.setStatus("mandatory")
_SlotSecondsSinceReset_Type = Gauge32
_SlotSecondsSinceReset_Object = MibTableColumn
slotSecondsSinceReset = _SlotSecondsSinceReset_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 1, 1, 4),
    _SlotSecondsSinceReset_Type()
)
slotSecondsSinceReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotSecondsSinceReset.setStatus("mandatory")
_SlotHardwareType_Type = HardwareType
_SlotHardwareType_Object = MibTableColumn
slotHardwareType = _SlotHardwareType_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 1, 1, 5),
    _SlotHardwareType_Type()
)
slotHardwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotHardwareType.setStatus("mandatory")
_SlotHardwareSerialNumber_Type = SerialNumber
_SlotHardwareSerialNumber_Object = MibTableColumn
slotHardwareSerialNumber = _SlotHardwareSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 1, 1, 6),
    _SlotHardwareSerialNumber_Type()
)
slotHardwareSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotHardwareSerialNumber.setStatus("mandatory")
_SlotHardwareRevision_Type = Integer32
_SlotHardwareRevision_Object = MibTableColumn
slotHardwareRevision = _SlotHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 1, 1, 7),
    _SlotHardwareRevision_Type()
)
slotHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotHardwareRevision.setStatus("mandatory")
_SlotIOCardType_Type = IOType
_SlotIOCardType_Object = MibTableColumn
slotIOCardType = _SlotIOCardType_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 1, 1, 8),
    _SlotIOCardType_Type()
)
slotIOCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotIOCardType.setStatus("mandatory")
_SlotIOCardSerialNumber_Type = SerialNumber
_SlotIOCardSerialNumber_Object = MibTableColumn
slotIOCardSerialNumber = _SlotIOCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 1, 1, 9),
    _SlotIOCardSerialNumber_Type()
)
slotIOCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotIOCardSerialNumber.setStatus("mandatory")


class _SlotIOCardOperStatus_Type(Integer32):
    """Custom type slotIOCardOperStatus based on Integer32"""
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
        *(("good", 3),
          ("mismatch", 2),
          ("notApplicable", 4),
          ("unknown", 1))
    )


_SlotIOCardOperStatus_Type.__name__ = "Integer32"
_SlotIOCardOperStatus_Object = MibTableColumn
slotIOCardOperStatus = _SlotIOCardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 1, 1, 10),
    _SlotIOCardOperStatus_Type()
)
slotIOCardOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotIOCardOperStatus.setStatus("mandatory")
_SlotBootstrapFirmwareRevision_Type = Integer32
_SlotBootstrapFirmwareRevision_Object = MibTableColumn
slotBootstrapFirmwareRevision = _SlotBootstrapFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 1, 1, 11),
    _SlotBootstrapFirmwareRevision_Type()
)
slotBootstrapFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBootstrapFirmwareRevision.setStatus("mandatory")
_SlotElementalFirmwareRevision_Type = Integer32
_SlotElementalFirmwareRevision_Object = MibTableColumn
slotElementalFirmwareRevision = _SlotElementalFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 1, 1, 12),
    _SlotElementalFirmwareRevision_Type()
)
slotElementalFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotElementalFirmwareRevision.setStatus("mandatory")
_SlotMemorySize_Type = Integer32
_SlotMemorySize_Object = MibTableColumn
slotMemorySize = _SlotMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 1, 1, 13),
    _SlotMemorySize_Type()
)
slotMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotMemorySize.setStatus("mandatory")
_SlotLedNumber_Type = Gauge32
_SlotLedNumber_Object = MibTableColumn
slotLedNumber = _SlotLedNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 1, 1, 14),
    _SlotLedNumber_Type()
)
slotLedNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotLedNumber.setStatus("mandatory")


class _SlotLedStatus_Type(OctetString):
    """Custom type slotLedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_SlotLedStatus_Type.__name__ = "OctetString"
_SlotLedStatus_Object = MibTableColumn
slotLedStatus = _SlotLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 1, 1, 15),
    _SlotLedStatus_Type()
)
slotLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotLedStatus.setStatus("mandatory")
_SlotBase802Address_Type = MacAddress
_SlotBase802Address_Object = MibTableColumn
slotBase802Address = _SlotBase802Address_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 1, 1, 16),
    _SlotBase802Address_Type()
)
slotBase802Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBase802Address.setStatus("mandatory")
_SlotIpAddress_Type = IpAddress
_SlotIpAddress_Object = MibTableColumn
slotIpAddress = _SlotIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 1, 1, 17),
    _SlotIpAddress_Type()
)
slotIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotIpAddress.setStatus("mandatory")


class _SlotPlus5Status_Type(Integer32):
    """Custom type slotPlus5Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broken", 2),
          ("good", 3),
          ("unknown", 1))
    )


_SlotPlus5Status_Type.__name__ = "Integer32"
_SlotPlus5Status_Object = MibTableColumn
slotPlus5Status = _SlotPlus5Status_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 1, 1, 18),
    _SlotPlus5Status_Type()
)
slotPlus5Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotPlus5Status.setStatus("mandatory")


class _SlotPlus12Status_Type(Integer32):
    """Custom type slotPlus12Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broken", 2),
          ("good", 3),
          ("unknown", 1))
    )


_SlotPlus12Status_Type.__name__ = "Integer32"
_SlotPlus12Status_Object = MibTableColumn
slotPlus12Status = _SlotPlus12Status_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 1, 1, 19),
    _SlotPlus12Status_Type()
)
slotPlus12Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotPlus12Status.setStatus("mandatory")


class _SlotMinus12Status_Type(Integer32):
    """Custom type slotMinus12Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broken", 2),
          ("good", 3),
          ("unknown", 1))
    )


_SlotMinus12Status_Type.__name__ = "Integer32"
_SlotMinus12Status_Object = MibTableColumn
slotMinus12Status = _SlotMinus12Status_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 1, 1, 20),
    _SlotMinus12Status_Type()
)
slotMinus12Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotMinus12Status.setStatus("mandatory")
_SlotPlus5Watts_Type = Gauge32
_SlotPlus5Watts_Object = MibTableColumn
slotPlus5Watts = _SlotPlus5Watts_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 1, 1, 21),
    _SlotPlus5Watts_Type()
)
slotPlus5Watts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotPlus5Watts.setStatus("mandatory")
_SlotPlus12Watts_Type = Gauge32
_SlotPlus12Watts_Object = MibTableColumn
slotPlus12Watts = _SlotPlus12Watts_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 1, 1, 22),
    _SlotPlus12Watts_Type()
)
slotPlus12Watts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotPlus12Watts.setStatus("mandatory")
_SlotMinus12Watts_Type = Gauge32
_SlotMinus12Watts_Object = MibTableColumn
slotMinus12Watts = _SlotMinus12Watts_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 1, 1, 23),
    _SlotMinus12Watts_Type()
)
slotMinus12Watts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotMinus12Watts.setStatus("mandatory")
_SlotIOCardHardwareVersion_Type = Integer32
_SlotIOCardHardwareVersion_Object = MibTableColumn
slotIOCardHardwareVersion = _SlotIOCardHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 1, 1, 24),
    _SlotIOCardHardwareVersion_Type()
)
slotIOCardHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotIOCardHardwareVersion.setStatus("mandatory")


class _SlotRestoreNVS_Type(Integer32):
    """Custom type slotRestoreNVS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_SlotRestoreNVS_Type.__name__ = "Integer32"
_SlotRestoreNVS_Object = MibTableColumn
slotRestoreNVS = _SlotRestoreNVS_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 1, 1, 25),
    _SlotRestoreNVS_Type()
)
slotRestoreNVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotRestoreNVS.setStatus("mandatory")


class _SlotDefaultNVS_Type(Integer32):
    """Custom type slotDefaultNVS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_SlotDefaultNVS_Type.__name__ = "Integer32"
_SlotDefaultNVS_Object = MibTableColumn
slotDefaultNVS = _SlotDefaultNVS_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 1, 1, 26),
    _SlotDefaultNVS_Type()
)
slotDefaultNVS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotDefaultNVS.setStatus("mandatory")
_SlotBootTable_Object = MibTable
slotBootTable = _SlotBootTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 2)
)
if mibBuilder.loadTexts:
    slotBootTable.setStatus("mandatory")
_SlotBootEntry_Object = MibTableRow
slotBootEntry = _SlotBootEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 2, 1)
)
slotBootEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHASSIS-MIB", "slotBootIndex"),
)
if mibBuilder.loadTexts:
    slotBootEntry.setStatus("mandatory")
_SlotBootIndex_Type = Integer32
_SlotBootIndex_Object = MibTableColumn
slotBootIndex = _SlotBootIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 2, 1, 1),
    _SlotBootIndex_Type()
)
slotBootIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBootIndex.setStatus("mandatory")
_SlotBootIfIndex_Type = Integer32
_SlotBootIfIndex_Object = MibTableColumn
slotBootIfIndex = _SlotBootIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 2, 1, 2),
    _SlotBootIfIndex_Type()
)
slotBootIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBootIfIndex.setStatus("mandatory")
_SlotBootNetwork_Type = ObjectIdentifier
_SlotBootNetwork_Object = MibTableColumn
slotBootNetwork = _SlotBootNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 2, 1, 3),
    _SlotBootNetwork_Type()
)
slotBootNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBootNetwork.setStatus("mandatory")


class _SlotBootProtocol_Type(Integer32):
    """Custom type slotBootProtocol based on Integer32"""
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
        *(("bootpTftp", 6),
          ("local", 8),
          ("managementBus", 9),
          ("mop", 3),
          ("other", 1),
          ("rarpTftp", 5),
          ("tftp", 7),
          ("unknown", 2),
          ("xmop", 4))
    )


_SlotBootProtocol_Type.__name__ = "Integer32"
_SlotBootProtocol_Object = MibTableColumn
slotBootProtocol = _SlotBootProtocol_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 2, 1, 4),
    _SlotBootProtocol_Type()
)
slotBootProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBootProtocol.setStatus("mandatory")
_SlotBoot802Address_Type = MacAddress
_SlotBoot802Address_Object = MibTableColumn
slotBoot802Address = _SlotBoot802Address_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 2, 1, 5),
    _SlotBoot802Address_Type()
)
slotBoot802Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBoot802Address.setStatus("mandatory")
_SlotBootAddressType_Type = AddressType
_SlotBootAddressType_Object = MibTableColumn
slotBootAddressType = _SlotBootAddressType_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 2, 1, 6),
    _SlotBootAddressType_Type()
)
slotBootAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBootAddressType.setStatus("mandatory")


class _SlotBootAddress_Type(OctetString):
    """Custom type slotBootAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_SlotBootAddress_Type.__name__ = "OctetString"
_SlotBootAddress_Object = MibTableColumn
slotBootAddress = _SlotBootAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 2, 1, 7),
    _SlotBootAddress_Type()
)
slotBootAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBootAddress.setStatus("mandatory")
_SlotBootServerAddressType_Type = AddressType
_SlotBootServerAddressType_Object = MibTableColumn
slotBootServerAddressType = _SlotBootServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 2, 1, 8),
    _SlotBootServerAddressType_Type()
)
slotBootServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBootServerAddressType.setStatus("mandatory")


class _SlotBootServerAddress_Type(OctetString):
    """Custom type slotBootServerAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_SlotBootServerAddress_Type.__name__ = "OctetString"
_SlotBootServerAddress_Object = MibTableColumn
slotBootServerAddress = _SlotBootServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 2, 1, 9),
    _SlotBootServerAddress_Type()
)
slotBootServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBootServerAddress.setStatus("mandatory")
_SlotBootGatewayAddress_Type = IpAddress
_SlotBootGatewayAddress_Object = MibTableColumn
slotBootGatewayAddress = _SlotBootGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 2, 1, 10),
    _SlotBootGatewayAddress_Type()
)
slotBootGatewayAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBootGatewayAddress.setStatus("mandatory")


class _SlotBootFileName_Type(DisplayString):
    """Custom type slotBootFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SlotBootFileName_Type.__name__ = "DisplayString"
_SlotBootFileName_Object = MibTableColumn
slotBootFileName = _SlotBootFileName_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 2, 1, 11),
    _SlotBootFileName_Type()
)
slotBootFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBootFileName.setStatus("mandatory")
_SlotBootBlockNumber_Type = Gauge32
_SlotBootBlockNumber_Object = MibTableColumn
slotBootBlockNumber = _SlotBootBlockNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 2, 1, 12),
    _SlotBootBlockNumber_Type()
)
slotBootBlockNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBootBlockNumber.setStatus("mandatory")


class _SlotBootCrashCode_Type(OctetString):
    """Custom type slotBootCrashCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_SlotBootCrashCode_Type.__name__ = "OctetString"
_SlotBootCrashCode_Object = MibTableColumn
slotBootCrashCode = _SlotBootCrashCode_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 2, 1, 13),
    _SlotBootCrashCode_Type()
)
slotBootCrashCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotBootCrashCode.setStatus("mandatory")
_SlotControllerTable_Object = MibTable
slotControllerTable = _SlotControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 3)
)
if mibBuilder.loadTexts:
    slotControllerTable.setStatus("mandatory")
_SlotControllerEntry_Object = MibTableRow
slotControllerEntry = _SlotControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 3, 1)
)
slotControllerEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHASSIS-MIB", "slotControllerType"),
    (0, "MRV-IN-REACH-CHASSIS-MIB", "slotControllerIndex"),
)
if mibBuilder.loadTexts:
    slotControllerEntry.setStatus("mandatory")
_SlotControllerType_Type = NetworkType
_SlotControllerType_Object = MibTableColumn
slotControllerType = _SlotControllerType_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 3, 1, 1),
    _SlotControllerType_Type()
)
slotControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotControllerType.setStatus("mandatory")
_SlotControllerIndex_Type = Integer32
_SlotControllerIndex_Object = MibTableColumn
slotControllerIndex = _SlotControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 3, 1, 2),
    _SlotControllerIndex_Type()
)
slotControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotControllerIndex.setStatus("mandatory")
_SlotControllerNetwork_Type = ObjectIdentifier
_SlotControllerNetwork_Object = MibTableColumn
slotControllerNetwork = _SlotControllerNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 7, 3, 1, 3),
    _SlotControllerNetwork_Type()
)
slotControllerNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotControllerNetwork.setStatus("mandatory")
_XPowerSupply_ObjectIdentity = ObjectIdentity
xPowerSupply = _XPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 16, 8)
)
_PowerSupplyTable_Object = MibTable
powerSupplyTable = _PowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 8, 1)
)
if mibBuilder.loadTexts:
    powerSupplyTable.setStatus("mandatory")
_PowerSupplyEntry_Object = MibTableRow
powerSupplyEntry = _PowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 8, 1, 1)
)
powerSupplyEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHASSIS-MIB", "powerSupplyIndex"),
)
if mibBuilder.loadTexts:
    powerSupplyEntry.setStatus("mandatory")
_PowerSupplyIndex_Type = Integer32
_PowerSupplyIndex_Object = MibTableColumn
powerSupplyIndex = _PowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 8, 1, 1, 1),
    _PowerSupplyIndex_Type()
)
powerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyIndex.setStatus("mandatory")


class _PowerSupplyAdminAction_Type(Integer32):
    """Custom type powerSupplyAdminAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("reset", 2),
          ("resetHold", 3))
    )


_PowerSupplyAdminAction_Type.__name__ = "Integer32"
_PowerSupplyAdminAction_Object = MibTableColumn
powerSupplyAdminAction = _PowerSupplyAdminAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 8, 1, 1, 2),
    _PowerSupplyAdminAction_Type()
)
powerSupplyAdminAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSupplyAdminAction.setStatus("mandatory")
_PowerSupplyFirmwareVersion_Type = Integer32
_PowerSupplyFirmwareVersion_Object = MibTableColumn
powerSupplyFirmwareVersion = _PowerSupplyFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 8, 1, 1, 3),
    _PowerSupplyFirmwareVersion_Type()
)
powerSupplyFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyFirmwareVersion.setStatus("mandatory")


class _PowerSupplyRedundancyStatus_Type(Integer32):
    """Custom type powerSupplyRedundancyStatus based on Integer32"""
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
        *(("disabled", 2),
          ("engaged", 4),
          ("redundant", 3),
          ("unknown", 1))
    )


_PowerSupplyRedundancyStatus_Type.__name__ = "Integer32"
_PowerSupplyRedundancyStatus_Object = MibTableColumn
powerSupplyRedundancyStatus = _PowerSupplyRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 8, 1, 1, 4),
    _PowerSupplyRedundancyStatus_Type()
)
powerSupplyRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyRedundancyStatus.setStatus("mandatory")


class _PowerSupplyPlus5Status_Type(Integer32):
    """Custom type powerSupplyPlus5Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broken", 3),
          ("good", 2),
          ("unknown", 1))
    )


_PowerSupplyPlus5Status_Type.__name__ = "Integer32"
_PowerSupplyPlus5Status_Object = MibTableColumn
powerSupplyPlus5Status = _PowerSupplyPlus5Status_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 8, 1, 1, 5),
    _PowerSupplyPlus5Status_Type()
)
powerSupplyPlus5Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyPlus5Status.setStatus("mandatory")


class _PowerSupplyPlus12Status_Type(Integer32):
    """Custom type powerSupplyPlus12Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broken", 3),
          ("good", 2),
          ("unknown", 1))
    )


_PowerSupplyPlus12Status_Type.__name__ = "Integer32"
_PowerSupplyPlus12Status_Object = MibTableColumn
powerSupplyPlus12Status = _PowerSupplyPlus12Status_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 8, 1, 1, 6),
    _PowerSupplyPlus12Status_Type()
)
powerSupplyPlus12Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyPlus12Status.setStatus("mandatory")


class _PowerSupplyMinus12Status_Type(Integer32):
    """Custom type powerSupplyMinus12Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broken", 3),
          ("good", 2),
          ("unknown", 1))
    )


_PowerSupplyMinus12Status_Type.__name__ = "Integer32"
_PowerSupplyMinus12Status_Object = MibTableColumn
powerSupplyMinus12Status = _PowerSupplyMinus12Status_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 8, 1, 1, 7),
    _PowerSupplyMinus12Status_Type()
)
powerSupplyMinus12Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyMinus12Status.setStatus("mandatory")


class _PowerSupplyThermalWarningStatus_Type(Integer32):
    """Custom type powerSupplyThermalWarningStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broken", 3),
          ("good", 2),
          ("unknown", 1))
    )


_PowerSupplyThermalWarningStatus_Type.__name__ = "Integer32"
_PowerSupplyThermalWarningStatus_Object = MibTableColumn
powerSupplyThermalWarningStatus = _PowerSupplyThermalWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 8, 1, 1, 8),
    _PowerSupplyThermalWarningStatus_Type()
)
powerSupplyThermalWarningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyThermalWarningStatus.setStatus("mandatory")


class _PowerSupplyThermalShutdownStatus_Type(Integer32):
    """Custom type powerSupplyThermalShutdownStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broken", 3),
          ("good", 2),
          ("unknown", 1))
    )


_PowerSupplyThermalShutdownStatus_Type.__name__ = "Integer32"
_PowerSupplyThermalShutdownStatus_Object = MibTableColumn
powerSupplyThermalShutdownStatus = _PowerSupplyThermalShutdownStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 8, 1, 1, 9),
    _PowerSupplyThermalShutdownStatus_Type()
)
powerSupplyThermalShutdownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyThermalShutdownStatus.setStatus("mandatory")


class _PowerSupplyFanStatus_Type(Integer32):
    """Custom type powerSupplyFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broken", 3),
          ("good", 2),
          ("unknown", 1))
    )


_PowerSupplyFanStatus_Type.__name__ = "Integer32"
_PowerSupplyFanStatus_Object = MibTableColumn
powerSupplyFanStatus = _PowerSupplyFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 8, 1, 1, 10),
    _PowerSupplyFanStatus_Type()
)
powerSupplyFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyFanStatus.setStatus("mandatory")


class _PowerSupplyHardwareInhibitStatus_Type(Integer32):
    """Custom type powerSupplyHardwareInhibitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broken", 3),
          ("good", 2),
          ("unknown", 1))
    )


_PowerSupplyHardwareInhibitStatus_Type.__name__ = "Integer32"
_PowerSupplyHardwareInhibitStatus_Object = MibTableColumn
powerSupplyHardwareInhibitStatus = _PowerSupplyHardwareInhibitStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 8, 1, 1, 11),
    _PowerSupplyHardwareInhibitStatus_Type()
)
powerSupplyHardwareInhibitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyHardwareInhibitStatus.setStatus("mandatory")


class _PowerSupplyPlus5History_Type(Integer32):
    """Custom type powerSupplyPlus5History based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broken", 3),
          ("good", 2),
          ("unknown", 1))
    )


_PowerSupplyPlus5History_Type.__name__ = "Integer32"
_PowerSupplyPlus5History_Object = MibTableColumn
powerSupplyPlus5History = _PowerSupplyPlus5History_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 8, 1, 1, 12),
    _PowerSupplyPlus5History_Type()
)
powerSupplyPlus5History.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyPlus5History.setStatus("mandatory")


class _PowerSupplyPlus12History_Type(Integer32):
    """Custom type powerSupplyPlus12History based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broken", 3),
          ("good", 2),
          ("unknown", 1))
    )


_PowerSupplyPlus12History_Type.__name__ = "Integer32"
_PowerSupplyPlus12History_Object = MibTableColumn
powerSupplyPlus12History = _PowerSupplyPlus12History_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 8, 1, 1, 13),
    _PowerSupplyPlus12History_Type()
)
powerSupplyPlus12History.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyPlus12History.setStatus("mandatory")


class _PowerSupplyMinus12History_Type(Integer32):
    """Custom type powerSupplyMinus12History based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broken", 3),
          ("good", 2),
          ("unknown", 1))
    )


_PowerSupplyMinus12History_Type.__name__ = "Integer32"
_PowerSupplyMinus12History_Object = MibTableColumn
powerSupplyMinus12History = _PowerSupplyMinus12History_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 8, 1, 1, 14),
    _PowerSupplyMinus12History_Type()
)
powerSupplyMinus12History.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyMinus12History.setStatus("mandatory")


class _PowerSupplyThermalWarningHistory_Type(Integer32):
    """Custom type powerSupplyThermalWarningHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broken", 3),
          ("good", 2),
          ("unknown", 1))
    )


_PowerSupplyThermalWarningHistory_Type.__name__ = "Integer32"
_PowerSupplyThermalWarningHistory_Object = MibTableColumn
powerSupplyThermalWarningHistory = _PowerSupplyThermalWarningHistory_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 8, 1, 1, 15),
    _PowerSupplyThermalWarningHistory_Type()
)
powerSupplyThermalWarningHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyThermalWarningHistory.setStatus("mandatory")


class _PowerSupplyThermalShutdownHistory_Type(Integer32):
    """Custom type powerSupplyThermalShutdownHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broken", 3),
          ("good", 2),
          ("unknown", 1))
    )


_PowerSupplyThermalShutdownHistory_Type.__name__ = "Integer32"
_PowerSupplyThermalShutdownHistory_Object = MibTableColumn
powerSupplyThermalShutdownHistory = _PowerSupplyThermalShutdownHistory_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 8, 1, 1, 16),
    _PowerSupplyThermalShutdownHistory_Type()
)
powerSupplyThermalShutdownHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyThermalShutdownHistory.setStatus("mandatory")


class _PowerSupplyFanHistory_Type(Integer32):
    """Custom type powerSupplyFanHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broken", 3),
          ("good", 2),
          ("unknown", 1))
    )


_PowerSupplyFanHistory_Type.__name__ = "Integer32"
_PowerSupplyFanHistory_Object = MibTableColumn
powerSupplyFanHistory = _PowerSupplyFanHistory_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 8, 1, 1, 17),
    _PowerSupplyFanHistory_Type()
)
powerSupplyFanHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyFanHistory.setStatus("mandatory")


class _PowerSupplyHardwareInhibitHistory_Type(Integer32):
    """Custom type powerSupplyHardwareInhibitHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broken", 3),
          ("good", 2),
          ("unknown", 1))
    )


_PowerSupplyHardwareInhibitHistory_Type.__name__ = "Integer32"
_PowerSupplyHardwareInhibitHistory_Object = MibTableColumn
powerSupplyHardwareInhibitHistory = _PowerSupplyHardwareInhibitHistory_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 8, 1, 1, 18),
    _PowerSupplyHardwareInhibitHistory_Type()
)
powerSupplyHardwareInhibitHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyHardwareInhibitHistory.setStatus("mandatory")
_PowerSupplyPlus5Volts_Type = Gauge32
_PowerSupplyPlus5Volts_Object = MibTableColumn
powerSupplyPlus5Volts = _PowerSupplyPlus5Volts_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 8, 1, 1, 19),
    _PowerSupplyPlus5Volts_Type()
)
powerSupplyPlus5Volts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyPlus5Volts.setStatus("mandatory")
_PowerSupplyPlus12Volts_Type = Gauge32
_PowerSupplyPlus12Volts_Object = MibTableColumn
powerSupplyPlus12Volts = _PowerSupplyPlus12Volts_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 8, 1, 1, 20),
    _PowerSupplyPlus12Volts_Type()
)
powerSupplyPlus12Volts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyPlus12Volts.setStatus("mandatory")
_PowerSupplyMinus12Volts_Type = Gauge32
_PowerSupplyMinus12Volts_Object = MibTableColumn
powerSupplyMinus12Volts = _PowerSupplyMinus12Volts_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 8, 1, 1, 21),
    _PowerSupplyMinus12Volts_Type()
)
powerSupplyMinus12Volts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyMinus12Volts.setStatus("mandatory")
_PowerSupplyWatts_Type = Gauge32
_PowerSupplyWatts_Object = MibTableColumn
powerSupplyWatts = _PowerSupplyWatts_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 8, 1, 1, 22),
    _PowerSupplyWatts_Type()
)
powerSupplyWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyWatts.setStatus("mandatory")
_PowerSupplyWattsMax_Type = Gauge32
_PowerSupplyWattsMax_Object = MibTableColumn
powerSupplyWattsMax = _PowerSupplyWattsMax_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 8, 1, 1, 23),
    _PowerSupplyWattsMax_Type()
)
powerSupplyWattsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyWattsMax.setStatus("mandatory")
_PowerSupplyChassisWatts_Type = Gauge32
_PowerSupplyChassisWatts_Object = MibTableColumn
powerSupplyChassisWatts = _PowerSupplyChassisWatts_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 8, 1, 1, 24),
    _PowerSupplyChassisWatts_Type()
)
powerSupplyChassisWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyChassisWatts.setStatus("mandatory")
_PowerSupplyChassisWattsMax_Type = Gauge32
_PowerSupplyChassisWattsMax_Object = MibTableColumn
powerSupplyChassisWattsMax = _PowerSupplyChassisWattsMax_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 8, 1, 1, 25),
    _PowerSupplyChassisWattsMax_Type()
)
powerSupplyChassisWattsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyChassisWattsMax.setStatus("mandatory")


class _PowerSupplyHardwareType_Type(Integer32):
    """Custom type powerSupplyHardwareType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bb190", 3),
          ("other", 1),
          ("ps130", 2))
    )


_PowerSupplyHardwareType_Type.__name__ = "Integer32"
_PowerSupplyHardwareType_Object = MibTableColumn
powerSupplyHardwareType = _PowerSupplyHardwareType_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 8, 1, 1, 26),
    _PowerSupplyHardwareType_Type()
)
powerSupplyHardwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyHardwareType.setStatus("mandatory")
_XFirmwareUpdate_ObjectIdentity = ObjectIdentity
xFirmwareUpdate = _XFirmwareUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 16, 9)
)
_FirmwareUpdateTable_Object = MibTable
firmwareUpdateTable = _FirmwareUpdateTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 9, 1)
)
if mibBuilder.loadTexts:
    firmwareUpdateTable.setStatus("mandatory")
_FirmwareUpdateEntry_Object = MibTableRow
firmwareUpdateEntry = _FirmwareUpdateEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 9, 1, 1)
)
firmwareUpdateEntry.setIndexNames(
    (0, "MRV-IN-REACH-CHASSIS-MIB", "firmwareUpdateSlotIndex"),
)
if mibBuilder.loadTexts:
    firmwareUpdateEntry.setStatus("mandatory")
_FirmwareUpdateSlotIndex_Type = Integer32
_FirmwareUpdateSlotIndex_Object = MibTableColumn
firmwareUpdateSlotIndex = _FirmwareUpdateSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 9, 1, 1, 1),
    _FirmwareUpdateSlotIndex_Type()
)
firmwareUpdateSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareUpdateSlotIndex.setStatus("mandatory")
_FirmwareUpdateDefaultFileName_Type = DisplayString
_FirmwareUpdateDefaultFileName_Object = MibTableColumn
firmwareUpdateDefaultFileName = _FirmwareUpdateDefaultFileName_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 9, 1, 1, 2),
    _FirmwareUpdateDefaultFileName_Type()
)
firmwareUpdateDefaultFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareUpdateDefaultFileName.setStatus("mandatory")
_FirmwareUpdateFileName_Type = DisplayString
_FirmwareUpdateFileName_Object = MibTableColumn
firmwareUpdateFileName = _FirmwareUpdateFileName_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 9, 1, 1, 3),
    _FirmwareUpdateFileName_Type()
)
firmwareUpdateFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareUpdateFileName.setStatus("mandatory")


class _FirmwareUpdateStatus_Type(Integer32):
    """Custom type firmwareUpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_FirmwareUpdateStatus_Type.__name__ = "Integer32"
_FirmwareUpdateStatus_Object = MibTableColumn
firmwareUpdateStatus = _FirmwareUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 9, 1, 1, 4),
    _FirmwareUpdateStatus_Type()
)
firmwareUpdateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareUpdateStatus.setStatus("mandatory")


class _FirmwareUpdateState_Type(Integer32):
    """Custom type firmwareUpdateState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("writing", 2))
    )


_FirmwareUpdateState_Type.__name__ = "Integer32"
_FirmwareUpdateState_Object = MibTableColumn
firmwareUpdateState = _FirmwareUpdateState_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 9, 1, 1, 5),
    _FirmwareUpdateState_Type()
)
firmwareUpdateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareUpdateState.setStatus("mandatory")


class _FirmwareUpdateCompletionStatus_Type(Integer32):
    """Custom type firmwareUpdateCompletionStatus based on Integer32"""
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
        *(("badFileName", 5),
          ("busError", 4),
          ("noTarget", 3),
          ("none", 1),
          ("success", 2),
          ("targetError", 6),
          ("timeout", 7))
    )


_FirmwareUpdateCompletionStatus_Type.__name__ = "Integer32"
_FirmwareUpdateCompletionStatus_Object = MibTableColumn
firmwareUpdateCompletionStatus = _FirmwareUpdateCompletionStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 9, 1, 1, 6),
    _FirmwareUpdateCompletionStatus_Type()
)
firmwareUpdateCompletionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareUpdateCompletionStatus.setStatus("mandatory")


class _FirmwareUpdateMethod_Type(Integer32):
    """Custom type firmwareUpdateMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("card", 1),
          ("local", 2))
    )


_FirmwareUpdateMethod_Type.__name__ = "Integer32"
_FirmwareUpdateMethod_Object = MibTableColumn
firmwareUpdateMethod = _FirmwareUpdateMethod_Object(
    (1, 3, 6, 1, 4, 1, 33, 16, 9, 1, 1, 7),
    _FirmwareUpdateMethod_Type()
)
firmwareUpdateMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareUpdateMethod.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MRV-IN-REACH-CHASSIS-MIB",
    **{"NetworkType": NetworkType,
       "SerialNumber": SerialNumber,
       "Letter": Letter,
       "xChassis": xChassis,
       "xChassisBasic": xChassisBasic,
       "basicBase802Address": basicBase802Address,
       "basicSlot": basicSlot,
       "basicSlotNumber": basicSlotNumber,
       "basicNewBase802Address": basicNewBase802Address,
       "xSegment": xSegment,
       "segmentTable": segmentTable,
       "segmentEntry": segmentEntry,
       "segmentType": segmentType,
       "segmentIndex": segmentIndex,
       "xPort": xPort,
       "portIOCardType": portIOCardType,
       "portIOCardSerialNumber": portIOCardSerialNumber,
       "portIOCardOperStatus": portIOCardOperStatus,
       "portTable": portTable,
       "portEntry": portEntry,
       "portType": portType,
       "portIndex": portIndex,
       "xController": xController,
       "controllerTable": controllerTable,
       "controllerEntry": controllerEntry,
       "controllerType": controllerType,
       "controllerIndex": controllerIndex,
       "controllerNetwork": controllerNetwork,
       "xInterface": xInterface,
       "interfaceTable": interfaceTable,
       "interfaceEntry": interfaceEntry,
       "interfaceIndex": interfaceIndex,
       "interfaceNetwork": interfaceNetwork,
       "xSlotBootControl": xSlotBootControl,
       "slotBootControlTable": slotBootControlTable,
       "slotBootControlEntry": slotBootControlEntry,
       "slotBootControlSlot": slotBootControlSlot,
       "slotBootControlIndex": slotBootControlIndex,
       "slotBootControlStatus": slotBootControlStatus,
       "slotBootControlController": slotBootControlController,
       "slotBootControlNetwork": slotBootControlNetwork,
       "slotBootControlMopFile": slotBootControlMopFile,
       "slotBootControlInternetFile": slotBootControlInternetFile,
       "slotBootControlInternetAddress": slotBootControlInternetAddress,
       "slotBootControlInternetServer": slotBootControlInternetServer,
       "slotBootControlInternetGateway": slotBootControlInternetGateway,
       "slotBootControlInternetDelimiter": slotBootControlInternetDelimiter,
       "slotBootControlFlagTable": slotBootControlFlagTable,
       "slotBootControlFlagEntry": slotBootControlFlagEntry,
       "slotBootControlFlagLoadBootpTftp": slotBootControlFlagLoadBootpTftp,
       "slotBootControlFlagParamBootpTftp": slotBootControlFlagParamBootpTftp,
       "slotBootControlFlagDumpBootpTftp": slotBootControlFlagDumpBootpTftp,
       "slotBootControlFlagLoadTftpDirect": slotBootControlFlagLoadTftpDirect,
       "slotBootControlFlagParamTftpDirect": slotBootControlFlagParamTftpDirect,
       "slotBootControlFlagDumpTftpDirect": slotBootControlFlagDumpTftpDirect,
       "slotBootControlFlagLoadLocal": slotBootControlFlagLoadLocal,
       "slotBootControlFlagParamLocal": slotBootControlFlagParamLocal,
       "slotBootControlFlagDumpLocal": slotBootControlFlagDumpLocal,
       "slotBootControlFlagLoadMop": slotBootControlFlagLoadMop,
       "slotBootControlFlagParamMop": slotBootControlFlagParamMop,
       "slotBootControlFlagDumpMop": slotBootControlFlagDumpMop,
       "slotBootControlFlagLoadXmop": slotBootControlFlagLoadXmop,
       "slotBootControlFlagParamXmop": slotBootControlFlagParamXmop,
       "slotBootControlFlagDumpXmop": slotBootControlFlagDumpXmop,
       "slotBootControlFlagLoadRarpTftp": slotBootControlFlagLoadRarpTftp,
       "slotBootControlFlagParamRarpTftp": slotBootControlFlagParamRarpTftp,
       "slotBootControlFlagDumpRarpTftp": slotBootControlFlagDumpRarpTftp,
       "slotBootControlStorageTable": slotBootControlStorageTable,
       "slotBootControlStorageEntry": slotBootControlStorageEntry,
       "slotBootControlStorageClientSlot": slotBootControlStorageClientSlot,
       "slotBootControlStorageServerSlot": slotBootControlStorageServerSlot,
       "slotBootControlStorageStatus": slotBootControlStorageStatus,
       "slotBootControlStorageFailures": slotBootControlStorageFailures,
       "xSlot": xSlot,
       "slotTable": slotTable,
       "slotEntry": slotEntry,
       "slotIndex": slotIndex,
       "slotAdminAction": slotAdminAction,
       "slotOperStatus": slotOperStatus,
       "slotSecondsSinceReset": slotSecondsSinceReset,
       "slotHardwareType": slotHardwareType,
       "slotHardwareSerialNumber": slotHardwareSerialNumber,
       "slotHardwareRevision": slotHardwareRevision,
       "slotIOCardType": slotIOCardType,
       "slotIOCardSerialNumber": slotIOCardSerialNumber,
       "slotIOCardOperStatus": slotIOCardOperStatus,
       "slotBootstrapFirmwareRevision": slotBootstrapFirmwareRevision,
       "slotElementalFirmwareRevision": slotElementalFirmwareRevision,
       "slotMemorySize": slotMemorySize,
       "slotLedNumber": slotLedNumber,
       "slotLedStatus": slotLedStatus,
       "slotBase802Address": slotBase802Address,
       "slotIpAddress": slotIpAddress,
       "slotPlus5Status": slotPlus5Status,
       "slotPlus12Status": slotPlus12Status,
       "slotMinus12Status": slotMinus12Status,
       "slotPlus5Watts": slotPlus5Watts,
       "slotPlus12Watts": slotPlus12Watts,
       "slotMinus12Watts": slotMinus12Watts,
       "slotIOCardHardwareVersion": slotIOCardHardwareVersion,
       "slotRestoreNVS": slotRestoreNVS,
       "slotDefaultNVS": slotDefaultNVS,
       "slotBootTable": slotBootTable,
       "slotBootEntry": slotBootEntry,
       "slotBootIndex": slotBootIndex,
       "slotBootIfIndex": slotBootIfIndex,
       "slotBootNetwork": slotBootNetwork,
       "slotBootProtocol": slotBootProtocol,
       "slotBoot802Address": slotBoot802Address,
       "slotBootAddressType": slotBootAddressType,
       "slotBootAddress": slotBootAddress,
       "slotBootServerAddressType": slotBootServerAddressType,
       "slotBootServerAddress": slotBootServerAddress,
       "slotBootGatewayAddress": slotBootGatewayAddress,
       "slotBootFileName": slotBootFileName,
       "slotBootBlockNumber": slotBootBlockNumber,
       "slotBootCrashCode": slotBootCrashCode,
       "slotControllerTable": slotControllerTable,
       "slotControllerEntry": slotControllerEntry,
       "slotControllerType": slotControllerType,
       "slotControllerIndex": slotControllerIndex,
       "slotControllerNetwork": slotControllerNetwork,
       "xPowerSupply": xPowerSupply,
       "powerSupplyTable": powerSupplyTable,
       "powerSupplyEntry": powerSupplyEntry,
       "powerSupplyIndex": powerSupplyIndex,
       "powerSupplyAdminAction": powerSupplyAdminAction,
       "powerSupplyFirmwareVersion": powerSupplyFirmwareVersion,
       "powerSupplyRedundancyStatus": powerSupplyRedundancyStatus,
       "powerSupplyPlus5Status": powerSupplyPlus5Status,
       "powerSupplyPlus12Status": powerSupplyPlus12Status,
       "powerSupplyMinus12Status": powerSupplyMinus12Status,
       "powerSupplyThermalWarningStatus": powerSupplyThermalWarningStatus,
       "powerSupplyThermalShutdownStatus": powerSupplyThermalShutdownStatus,
       "powerSupplyFanStatus": powerSupplyFanStatus,
       "powerSupplyHardwareInhibitStatus": powerSupplyHardwareInhibitStatus,
       "powerSupplyPlus5History": powerSupplyPlus5History,
       "powerSupplyPlus12History": powerSupplyPlus12History,
       "powerSupplyMinus12History": powerSupplyMinus12History,
       "powerSupplyThermalWarningHistory": powerSupplyThermalWarningHistory,
       "powerSupplyThermalShutdownHistory": powerSupplyThermalShutdownHistory,
       "powerSupplyFanHistory": powerSupplyFanHistory,
       "powerSupplyHardwareInhibitHistory": powerSupplyHardwareInhibitHistory,
       "powerSupplyPlus5Volts": powerSupplyPlus5Volts,
       "powerSupplyPlus12Volts": powerSupplyPlus12Volts,
       "powerSupplyMinus12Volts": powerSupplyMinus12Volts,
       "powerSupplyWatts": powerSupplyWatts,
       "powerSupplyWattsMax": powerSupplyWattsMax,
       "powerSupplyChassisWatts": powerSupplyChassisWatts,
       "powerSupplyChassisWattsMax": powerSupplyChassisWattsMax,
       "powerSupplyHardwareType": powerSupplyHardwareType,
       "xFirmwareUpdate": xFirmwareUpdate,
       "firmwareUpdateTable": firmwareUpdateTable,
       "firmwareUpdateEntry": firmwareUpdateEntry,
       "firmwareUpdateSlotIndex": firmwareUpdateSlotIndex,
       "firmwareUpdateDefaultFileName": firmwareUpdateDefaultFileName,
       "firmwareUpdateFileName": firmwareUpdateFileName,
       "firmwareUpdateStatus": firmwareUpdateStatus,
       "firmwareUpdateState": firmwareUpdateState,
       "firmwareUpdateCompletionStatus": firmwareUpdateCompletionStatus,
       "firmwareUpdateMethod": firmwareUpdateMethod}
)
