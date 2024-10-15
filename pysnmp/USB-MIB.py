# SNMP MIB module (USB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/USB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:41 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

usbMib = ModuleIdentity(
    (1, 3, 6, 1, 3, 103)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsbMibObjects_ObjectIdentity = ObjectIdentity
usbMibObjects = _UsbMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 103, 1)
)


class _UsbNumber_Type(Integer32):
    """Custom type usbNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsbNumber_Type.__name__ = "Integer32"
_UsbNumber_Object = MibScalar
usbNumber = _UsbNumber_Object(
    (1, 3, 6, 1, 3, 103, 1, 1),
    _UsbNumber_Type()
)
usbNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbNumber.setStatus("current")
_UsbPortTable_Object = MibTable
usbPortTable = _UsbPortTable_Object(
    (1, 3, 6, 1, 3, 103, 1, 2)
)
if mibBuilder.loadTexts:
    usbPortTable.setStatus("current")
_UsbPortEntry_Object = MibTableRow
usbPortEntry = _UsbPortEntry_Object(
    (1, 3, 6, 1, 3, 103, 1, 2, 1)
)
usbPortEntry.setIndexNames(
    (0, "USB-MIB", "usbPortIndex"),
)
if mibBuilder.loadTexts:
    usbPortEntry.setStatus("current")


class _UsbPortIndex_Type(Integer32):
    """Custom type usbPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsbPortIndex_Type.__name__ = "Integer32"
_UsbPortIndex_Object = MibTableColumn
usbPortIndex = _UsbPortIndex_Object(
    (1, 3, 6, 1, 3, 103, 1, 2, 1, 1),
    _UsbPortIndex_Type()
)
usbPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbPortIndex.setStatus("current")


class _UsbPortType_Type(Integer32):
    """Custom type usbPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("device", 2),
          ("host", 1),
          ("hub", 3))
    )


_UsbPortType_Type.__name__ = "Integer32"
_UsbPortType_Object = MibTableColumn
usbPortType = _UsbPortType_Object(
    (1, 3, 6, 1, 3, 103, 1, 2, 1, 2),
    _UsbPortType_Type()
)
usbPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbPortType.setStatus("current")


class _UsbPortRate_Type(Integer32):
    """Custom type usbPortRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full-speed", 2),
          ("high-speed", 3),
          ("low-speed", 1))
    )


_UsbPortRate_Type.__name__ = "Integer32"
_UsbPortRate_Object = MibTableColumn
usbPortRate = _UsbPortRate_Object(
    (1, 3, 6, 1, 3, 103, 1, 2, 1, 3),
    _UsbPortRate_Type()
)
usbPortRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbPortRate.setStatus("current")
_UsbDeviceTable_Object = MibTable
usbDeviceTable = _UsbDeviceTable_Object(
    (1, 3, 6, 1, 3, 103, 1, 3)
)
if mibBuilder.loadTexts:
    usbDeviceTable.setStatus("current")
_UsbDeviceEntry_Object = MibTableRow
usbDeviceEntry = _UsbDeviceEntry_Object(
    (1, 3, 6, 1, 3, 103, 1, 3, 1)
)
usbDeviceEntry.setIndexNames(
    (0, "USB-MIB", "usbDeviceIndex"),
)
if mibBuilder.loadTexts:
    usbDeviceEntry.setStatus("current")


class _UsbDeviceIndex_Type(Integer32):
    """Custom type usbDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsbDeviceIndex_Type.__name__ = "Integer32"
_UsbDeviceIndex_Object = MibTableColumn
usbDeviceIndex = _UsbDeviceIndex_Object(
    (1, 3, 6, 1, 3, 103, 1, 3, 1, 1),
    _UsbDeviceIndex_Type()
)
usbDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbDeviceIndex.setStatus("current")


class _UsbDevicePower_Type(Integer32):
    """Custom type usbDevicePower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bus-powered", 3),
          ("self-powered", 2),
          ("unknown", 1))
    )


_UsbDevicePower_Type.__name__ = "Integer32"
_UsbDevicePower_Object = MibTableColumn
usbDevicePower = _UsbDevicePower_Object(
    (1, 3, 6, 1, 3, 103, 1, 3, 1, 2),
    _UsbDevicePower_Type()
)
usbDevicePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbDevicePower.setStatus("current")
_UsbDeviceVendorID_Type = OctetString
_UsbDeviceVendorID_Object = MibTableColumn
usbDeviceVendorID = _UsbDeviceVendorID_Object(
    (1, 3, 6, 1, 3, 103, 1, 3, 1, 3),
    _UsbDeviceVendorID_Type()
)
usbDeviceVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbDeviceVendorID.setStatus("current")
_UsbDeviceProductID_Type = OctetString
_UsbDeviceProductID_Object = MibTableColumn
usbDeviceProductID = _UsbDeviceProductID_Object(
    (1, 3, 6, 1, 3, 103, 1, 3, 1, 4),
    _UsbDeviceProductID_Type()
)
usbDeviceProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbDeviceProductID.setStatus("current")


class _UsbDeviceNumberConfigurations_Type(Integer32):
    """Custom type usbDeviceNumberConfigurations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsbDeviceNumberConfigurations_Type.__name__ = "Integer32"
_UsbDeviceNumberConfigurations_Object = MibTableColumn
usbDeviceNumberConfigurations = _UsbDeviceNumberConfigurations_Object(
    (1, 3, 6, 1, 3, 103, 1, 3, 1, 5),
    _UsbDeviceNumberConfigurations_Type()
)
usbDeviceNumberConfigurations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbDeviceNumberConfigurations.setStatus("current")


class _UsbDeviceActiveClass_Type(Integer32):
    """Custom type usbDeviceActiveClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cdc", 2),
          ("other", 1))
    )


_UsbDeviceActiveClass_Type.__name__ = "Integer32"
_UsbDeviceActiveClass_Object = MibTableColumn
usbDeviceActiveClass = _UsbDeviceActiveClass_Object(
    (1, 3, 6, 1, 3, 103, 1, 3, 1, 6),
    _UsbDeviceActiveClass_Type()
)
usbDeviceActiveClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbDeviceActiveClass.setStatus("current")


class _UsbDeviceStatus_Type(Integer32):
    """Custom type usbDeviceStatus based on Integer32"""
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
        *(("address", 5),
          ("attached", 2),
          ("configured", 6),
          ("default", 4),
          ("powered", 3),
          ("suspended", 7),
          ("unattached", 1))
    )


_UsbDeviceStatus_Type.__name__ = "Integer32"
_UsbDeviceStatus_Object = MibTableColumn
usbDeviceStatus = _UsbDeviceStatus_Object(
    (1, 3, 6, 1, 3, 103, 1, 3, 1, 7),
    _UsbDeviceStatus_Type()
)
usbDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbDeviceStatus.setStatus("current")
_UsbDeviceEnumCounter_Type = Counter32
_UsbDeviceEnumCounter_Object = MibTableColumn
usbDeviceEnumCounter = _UsbDeviceEnumCounter_Object(
    (1, 3, 6, 1, 3, 103, 1, 3, 1, 8),
    _UsbDeviceEnumCounter_Type()
)
usbDeviceEnumCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbDeviceEnumCounter.setStatus("current")
_UsbDeviceRemoteWakeup_Type = TruthValue
_UsbDeviceRemoteWakeup_Object = MibTableColumn
usbDeviceRemoteWakeup = _UsbDeviceRemoteWakeup_Object(
    (1, 3, 6, 1, 3, 103, 1, 3, 1, 9),
    _UsbDeviceRemoteWakeup_Type()
)
usbDeviceRemoteWakeup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbDeviceRemoteWakeup.setStatus("current")
_UsbDeviceRemoteWakeupOn_Type = TruthValue
_UsbDeviceRemoteWakeupOn_Object = MibTableColumn
usbDeviceRemoteWakeupOn = _UsbDeviceRemoteWakeupOn_Object(
    (1, 3, 6, 1, 3, 103, 1, 3, 1, 10),
    _UsbDeviceRemoteWakeupOn_Type()
)
usbDeviceRemoteWakeupOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbDeviceRemoteWakeupOn.setStatus("current")
_UsbCDCTable_Object = MibTable
usbCDCTable = _UsbCDCTable_Object(
    (1, 3, 6, 1, 3, 103, 1, 4)
)
if mibBuilder.loadTexts:
    usbCDCTable.setStatus("current")
_UsbCDCEntry_Object = MibTableRow
usbCDCEntry = _UsbCDCEntry_Object(
    (1, 3, 6, 1, 3, 103, 1, 4, 1)
)
usbCDCEntry.setIndexNames(
    (0, "USB-MIB", "usbCDCIndex"),
    (0, "USB-MIB", "usbCDCIfIndex"),
)
if mibBuilder.loadTexts:
    usbCDCEntry.setStatus("current")


class _UsbCDCIndex_Type(Integer32):
    """Custom type usbCDCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsbCDCIndex_Type.__name__ = "Integer32"
_UsbCDCIndex_Object = MibTableColumn
usbCDCIndex = _UsbCDCIndex_Object(
    (1, 3, 6, 1, 3, 103, 1, 4, 1, 1),
    _UsbCDCIndex_Type()
)
usbCDCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbCDCIndex.setStatus("current")
_UsbCDCIfIndex_Type = InterfaceIndexOrZero
_UsbCDCIfIndex_Object = MibTableColumn
usbCDCIfIndex = _UsbCDCIfIndex_Object(
    (1, 3, 6, 1, 3, 103, 1, 4, 1, 2),
    _UsbCDCIfIndex_Type()
)
usbCDCIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbCDCIfIndex.setStatus("current")


class _UsbCDCSubclass_Type(Integer32):
    """Custom type usbCDCSubclass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("acm", 2),
          ("atm", 7),
          ("capi", 5),
          ("directLine", 1),
          ("ethernet", 6),
          ("multichannel", 4),
          ("other", 0),
          ("telephony", 3))
    )


_UsbCDCSubclass_Type.__name__ = "Integer32"
_UsbCDCSubclass_Object = MibTableColumn
usbCDCSubclass = _UsbCDCSubclass_Object(
    (1, 3, 6, 1, 3, 103, 1, 4, 1, 3),
    _UsbCDCSubclass_Type()
)
usbCDCSubclass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbCDCSubclass.setStatus("current")


class _UsbCDCVersion_Type(OctetString):
    """Custom type usbCDCVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_UsbCDCVersion_Type.__name__ = "OctetString"
_UsbCDCVersion_Object = MibTableColumn
usbCDCVersion = _UsbCDCVersion_Object(
    (1, 3, 6, 1, 3, 103, 1, 4, 1, 4),
    _UsbCDCVersion_Type()
)
usbCDCVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbCDCVersion.setStatus("current")


class _UsbCDCDataTransferType_Type(Integer32):
    """Custom type usbCDCDataTransferType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asynchronous", 2),
          ("synchronous", 1))
    )


_UsbCDCDataTransferType_Type.__name__ = "Integer32"
_UsbCDCDataTransferType_Object = MibTableColumn
usbCDCDataTransferType = _UsbCDCDataTransferType_Object(
    (1, 3, 6, 1, 3, 103, 1, 4, 1, 5),
    _UsbCDCDataTransferType_Type()
)
usbCDCDataTransferType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbCDCDataTransferType.setStatus("current")


class _UsbCDCDataEndpoints_Type(Integer32):
    """Custom type usbCDCDataEndpoints based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_UsbCDCDataEndpoints_Type.__name__ = "Integer32"
_UsbCDCDataEndpoints_Object = MibTableColumn
usbCDCDataEndpoints = _UsbCDCDataEndpoints_Object(
    (1, 3, 6, 1, 3, 103, 1, 4, 1, 6),
    _UsbCDCDataEndpoints_Type()
)
usbCDCDataEndpoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbCDCDataEndpoints.setStatus("current")
_UsbCDCStalls_Type = Counter32
_UsbCDCStalls_Object = MibTableColumn
usbCDCStalls = _UsbCDCStalls_Object(
    (1, 3, 6, 1, 3, 103, 1, 4, 1, 7),
    _UsbCDCStalls_Type()
)
usbCDCStalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbCDCStalls.setStatus("current")
_UsbCDCEtherTable_Object = MibTable
usbCDCEtherTable = _UsbCDCEtherTable_Object(
    (1, 3, 6, 1, 3, 103, 1, 5)
)
if mibBuilder.loadTexts:
    usbCDCEtherTable.setStatus("current")
_UsbCDCEtherEntry_Object = MibTableRow
usbCDCEtherEntry = _UsbCDCEtherEntry_Object(
    (1, 3, 6, 1, 3, 103, 1, 5, 1)
)
usbCDCEtherEntry.setIndexNames(
    (0, "USB-MIB", "usbCDCEtherIndex"),
    (0, "USB-MIB", "usbCDCEtherIfIndex"),
)
if mibBuilder.loadTexts:
    usbCDCEtherEntry.setStatus("current")


class _UsbCDCEtherIndex_Type(Integer32):
    """Custom type usbCDCEtherIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsbCDCEtherIndex_Type.__name__ = "Integer32"
_UsbCDCEtherIndex_Object = MibTableColumn
usbCDCEtherIndex = _UsbCDCEtherIndex_Object(
    (1, 3, 6, 1, 3, 103, 1, 5, 1, 1),
    _UsbCDCEtherIndex_Type()
)
usbCDCEtherIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbCDCEtherIndex.setStatus("current")
_UsbCDCEtherIfIndex_Type = InterfaceIndexOrZero
_UsbCDCEtherIfIndex_Object = MibTableColumn
usbCDCEtherIfIndex = _UsbCDCEtherIfIndex_Object(
    (1, 3, 6, 1, 3, 103, 1, 5, 1, 2),
    _UsbCDCEtherIfIndex_Type()
)
usbCDCEtherIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbCDCEtherIfIndex.setStatus("current")
_UsbCDCEtherMacAddress_Type = MacAddress
_UsbCDCEtherMacAddress_Object = MibTableColumn
usbCDCEtherMacAddress = _UsbCDCEtherMacAddress_Object(
    (1, 3, 6, 1, 3, 103, 1, 5, 1, 3),
    _UsbCDCEtherMacAddress_Type()
)
usbCDCEtherMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbCDCEtherMacAddress.setStatus("current")


class _UsbCDCEtherPacketFilter_Type(Bits):
    """Custom type usbCDCEtherPacketFilter based on Bits"""
    namedValues = NamedValues(
        *(("packetAllMulticast", 1),
          ("packetBroadcast", 3),
          ("packetDirected", 2),
          ("packetMulticast", 4),
          ("packetPromiscuous", 0))
    )

_UsbCDCEtherPacketFilter_Type.__name__ = "Bits"
_UsbCDCEtherPacketFilter_Object = MibTableColumn
usbCDCEtherPacketFilter = _UsbCDCEtherPacketFilter_Object(
    (1, 3, 6, 1, 3, 103, 1, 5, 1, 4),
    _UsbCDCEtherPacketFilter_Type()
)
usbCDCEtherPacketFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbCDCEtherPacketFilter.setStatus("current")


class _UsbCDCEtherDataStatisticsCapabilities_Type(Bits):
    """Custom type usbCDCEtherDataStatisticsCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("bytesRcvBroadcastOk", 15),
          ("bytesRcvDirectOk", 11),
          ("bytesRcvMulticastOk", 13),
          ("bytesXmitBroadcastOk", 9),
          ("bytesXmitDirectOk", 5),
          ("bytesXmitMulticastOk", 7),
          ("frameRcvErr", 3),
          ("frameRcvNoBuff", 4),
          ("frameRcvOk", 1),
          ("frameXmitErr", 2),
          ("frameXmitOk", 0),
          ("framesRcvBroadcastOk", 16),
          ("framesRcvCrcErr", 17),
          ("framesRcvDirectOk", 12),
          ("framesRcvMulticastOk", 14),
          ("framesXmitBroadcastOk", 10),
          ("framesXmitDirectOk", 6),
          ("framesXmitMulticastOk", 8),
          ("rcvErrAlignment", 19),
          ("rcvOverrun", 24),
          ("xmitDeferred", 22),
          ("xmitHearbeatFailure", 26),
          ("xmitLateCollisions", 28),
          ("xmitMaxCollision", 23),
          ("xmitMoreCollisions", 21),
          ("xmitOneCollision", 20),
          ("xmitQueueLen", 18),
          ("xmitTimesCrsLost", 27),
          ("xmitUnderrun", 25))
    )

_UsbCDCEtherDataStatisticsCapabilities_Type.__name__ = "Bits"
_UsbCDCEtherDataStatisticsCapabilities_Object = MibTableColumn
usbCDCEtherDataStatisticsCapabilities = _UsbCDCEtherDataStatisticsCapabilities_Object(
    (1, 3, 6, 1, 3, 103, 1, 5, 1, 5),
    _UsbCDCEtherDataStatisticsCapabilities_Type()
)
usbCDCEtherDataStatisticsCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbCDCEtherDataStatisticsCapabilities.setStatus("current")
_UsbCDCEtherDataCheckErrs_Type = Counter32
_UsbCDCEtherDataCheckErrs_Object = MibTableColumn
usbCDCEtherDataCheckErrs = _UsbCDCEtherDataCheckErrs_Object(
    (1, 3, 6, 1, 3, 103, 1, 5, 1, 6),
    _UsbCDCEtherDataCheckErrs_Type()
)
usbCDCEtherDataCheckErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbCDCEtherDataCheckErrs.setStatus("current")
_UsbCDCEtherXmtAddressTable_Object = MibTable
usbCDCEtherXmtAddressTable = _UsbCDCEtherXmtAddressTable_Object(
    (1, 3, 6, 1, 3, 103, 1, 6)
)
if mibBuilder.loadTexts:
    usbCDCEtherXmtAddressTable.setStatus("current")
_UsbCDCEtherXmtAddressEntry_Object = MibTableRow
usbCDCEtherXmtAddressEntry = _UsbCDCEtherXmtAddressEntry_Object(
    (1, 3, 6, 1, 3, 103, 1, 6, 1)
)
usbCDCEtherXmtAddressEntry.setIndexNames(
    (0, "USB-MIB", "usbCDCEtherIndex"),
    (0, "USB-MIB", "usbCDCEtherIfIndex"),
    (0, "USB-MIB", "ifCDCEtherXmtAddress"),
)
if mibBuilder.loadTexts:
    usbCDCEtherXmtAddressEntry.setStatus("current")
_IfCDCEtherXmtAddress_Type = MacAddress
_IfCDCEtherXmtAddress_Object = MibTableColumn
ifCDCEtherXmtAddress = _IfCDCEtherXmtAddress_Object(
    (1, 3, 6, 1, 3, 103, 1, 6, 1, 1),
    _IfCDCEtherXmtAddress_Type()
)
ifCDCEtherXmtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCDCEtherXmtAddress.setStatus("current")
_UsbMibNotification_ObjectIdentity = ObjectIdentity
usbMibNotification = _UsbMibNotification_ObjectIdentity(
    (1, 3, 6, 1, 3, 103, 2)
)
_UsbMibConformance_ObjectIdentity = ObjectIdentity
usbMibConformance = _UsbMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 103, 3)
)
_UsbMibCompliances_ObjectIdentity = ObjectIdentity
usbMibCompliances = _UsbMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 103, 3, 1)
)
_UsbMibGroups_ObjectIdentity = ObjectIdentity
usbMibGroups = _UsbMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 103, 3, 2)
)

# Managed Objects groups

usbMibBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 103, 3, 2, 1)
)
usbMibBasicGroup.setObjects(
      *(("USB-MIB", "usbNumber"),
        ("USB-MIB", "usbPortIndex"),
        ("USB-MIB", "usbPortType"),
        ("USB-MIB", "usbPortRate"),
        ("USB-MIB", "usbDeviceIndex"),
        ("USB-MIB", "usbDevicePower"),
        ("USB-MIB", "usbDeviceVendorID"),
        ("USB-MIB", "usbDeviceProductID"),
        ("USB-MIB", "usbDeviceNumberConfigurations"),
        ("USB-MIB", "usbDeviceActiveClass"),
        ("USB-MIB", "usbDeviceStatus"),
        ("USB-MIB", "usbDeviceEnumCounter"),
        ("USB-MIB", "usbDeviceRemoteWakeup"),
        ("USB-MIB", "usbDeviceRemoteWakeupOn"))
)
if mibBuilder.loadTexts:
    usbMibBasicGroup.setStatus("current")

usbMibCDCGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 103, 3, 2, 2)
)
usbMibCDCGroup.setObjects(
      *(("USB-MIB", "usbCDCIndex"),
        ("USB-MIB", "usbCDCIfIndex"),
        ("USB-MIB", "usbCDCSubclass"),
        ("USB-MIB", "usbCDCVersion"),
        ("USB-MIB", "usbCDCDataTransferType"),
        ("USB-MIB", "usbCDCDataEndpoints"),
        ("USB-MIB", "usbCDCStalls"))
)
if mibBuilder.loadTexts:
    usbMibCDCGroup.setStatus("current")

usbMibCDCEtherGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 103, 3, 2, 3)
)
usbMibCDCEtherGroup.setObjects(
      *(("USB-MIB", "usbCDCEtherIndex"),
        ("USB-MIB", "usbCDCEtherIfIndex"),
        ("USB-MIB", "usbCDCEtherMacAddress"),
        ("USB-MIB", "usbCDCEtherPacketFilter"),
        ("USB-MIB", "usbCDCEtherDataStatisticsCapabilities"),
        ("USB-MIB", "usbCDCEtherDataCheckErrs"))
)
if mibBuilder.loadTexts:
    usbMibCDCEtherGroup.setStatus("current")

usbCDCEtherXmtAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 103, 3, 2, 4)
)
usbCDCEtherXmtAddressGroup.setObjects(
    ("USB-MIB", "ifCDCEtherXmtAddress")
)
if mibBuilder.loadTexts:
    usbCDCEtherXmtAddressGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usbMibBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 103, 3, 1, 1)
)
if mibBuilder.loadTexts:
    usbMibBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "USB-MIB",
    **{"usbMib": usbMib,
       "usbMibObjects": usbMibObjects,
       "usbNumber": usbNumber,
       "usbPortTable": usbPortTable,
       "usbPortEntry": usbPortEntry,
       "usbPortIndex": usbPortIndex,
       "usbPortType": usbPortType,
       "usbPortRate": usbPortRate,
       "usbDeviceTable": usbDeviceTable,
       "usbDeviceEntry": usbDeviceEntry,
       "usbDeviceIndex": usbDeviceIndex,
       "usbDevicePower": usbDevicePower,
       "usbDeviceVendorID": usbDeviceVendorID,
       "usbDeviceProductID": usbDeviceProductID,
       "usbDeviceNumberConfigurations": usbDeviceNumberConfigurations,
       "usbDeviceActiveClass": usbDeviceActiveClass,
       "usbDeviceStatus": usbDeviceStatus,
       "usbDeviceEnumCounter": usbDeviceEnumCounter,
       "usbDeviceRemoteWakeup": usbDeviceRemoteWakeup,
       "usbDeviceRemoteWakeupOn": usbDeviceRemoteWakeupOn,
       "usbCDCTable": usbCDCTable,
       "usbCDCEntry": usbCDCEntry,
       "usbCDCIndex": usbCDCIndex,
       "usbCDCIfIndex": usbCDCIfIndex,
       "usbCDCSubclass": usbCDCSubclass,
       "usbCDCVersion": usbCDCVersion,
       "usbCDCDataTransferType": usbCDCDataTransferType,
       "usbCDCDataEndpoints": usbCDCDataEndpoints,
       "usbCDCStalls": usbCDCStalls,
       "usbCDCEtherTable": usbCDCEtherTable,
       "usbCDCEtherEntry": usbCDCEtherEntry,
       "usbCDCEtherIndex": usbCDCEtherIndex,
       "usbCDCEtherIfIndex": usbCDCEtherIfIndex,
       "usbCDCEtherMacAddress": usbCDCEtherMacAddress,
       "usbCDCEtherPacketFilter": usbCDCEtherPacketFilter,
       "usbCDCEtherDataStatisticsCapabilities": usbCDCEtherDataStatisticsCapabilities,
       "usbCDCEtherDataCheckErrs": usbCDCEtherDataCheckErrs,
       "usbCDCEtherXmtAddressTable": usbCDCEtherXmtAddressTable,
       "usbCDCEtherXmtAddressEntry": usbCDCEtherXmtAddressEntry,
       "ifCDCEtherXmtAddress": ifCDCEtherXmtAddress,
       "usbMibNotification": usbMibNotification,
       "usbMibConformance": usbMibConformance,
       "usbMibCompliances": usbMibCompliances,
       "usbMibBasicCompliance": usbMibBasicCompliance,
       "usbMibGroups": usbMibGroups,
       "usbMibBasicGroup": usbMibBasicGroup,
       "usbMibCDCGroup": usbMibCDCGroup,
       "usbMibCDCEtherGroup": usbMibCDCEtherGroup,
       "usbCDCEtherXmtAddressGroup": usbCDCEtherXmtAddressGroup}
)
