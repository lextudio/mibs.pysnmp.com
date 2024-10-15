# SNMP MIB module (DMTF-LAN-ADAPTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DMTF-LAN-ADAPTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:31:41 2024
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

(DmiString,
 dmiCompId,
 dmiEventAssociatedGroup,
 dmiEventDateTime,
 dmiEventSeverity,
 dmiEventStateKey,
 dmiEventSubSystem,
 dmiEventSystem) = mibBuilder.importSymbols(
    "DMTF-DMI-MIB",
    "DmiString",
    "dmiCompId",
    "dmiEventAssociatedGroup",
    "dmiEventDateTime",
    "dmiEventSeverity",
    "dmiEventStateKey",
    "dmiEventSubSystem",
    "dmiEventSystem")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

dmtfLANAdapterMIF = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 412, 2, 2)
)


# Types definitions



class DmiCounter(Counter32):
    """Custom type DmiCounter based on Counter32"""




class DmiCounter64(Counter64):
    """Custom type DmiCounter64 based on Counter64"""




class DmiGauge(Gauge32):
    """Custom type DmiGauge based on Gauge32"""




class DmiInteger(Integer32):
    """Custom type DmiInteger based on Integer32"""




class DmiOctetstring(OctetString):
    """Custom type DmiOctetstring based on OctetString"""




class DmiCompId(Integer32):
    """Custom type DmiCompId based on Integer32"""




class DmiGroupId(Integer32):
    """Custom type DmiGroupId based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dmtf_ObjectIdentity = ObjectIdentity
dmtf = _Dmtf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412)
)
_DmtfStdMifs_ObjectIdentity = ObjectIdentity
dmtfStdMifs = _DmtfStdMifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 2)
)
_DmtfNetworkAdapter802PortTable_Object = MibTable
dmtfNetworkAdapter802PortTable = _DmtfNetworkAdapter802PortTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dmtfNetworkAdapter802PortTable.setStatus("current")
_DmtfNetworkAdapter802PortEntry_Object = MibTableRow
dmtfNetworkAdapter802PortEntry = _DmtfNetworkAdapter802PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 1, 1)
)
dmtfNetworkAdapter802PortEntry.setIndexNames(
    (0, "DMTF-LAN-ADAPTER-MIB", "DmiCompId"),
    (0, "DMTF-LAN-ADAPTER-MIB", "DmiGroupId"),
    (0, "DMTF-LAN-ADAPTER-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    dmtfNetworkAdapter802PortEntry.setStatus("current")


class _DmtfNetworkAdapter802PortState_Type(Integer32):
    """Custom type dmtfNetworkAdapter802PortState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DmtfNetworkAdapter802PortState_Type.__name__ = "Integer32"
_DmtfNetworkAdapter802PortState_Object = MibTableColumn
dmtfNetworkAdapter802PortState = _DmtfNetworkAdapter802PortState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 1, 1, 0),
    _DmtfNetworkAdapter802PortState_Type()
)
dmtfNetworkAdapter802PortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtfNetworkAdapter802PortState.setStatus("current")
_PortIndex2_Type = DmiInteger
_PortIndex2_Object = MibScalar
portIndex2 = _PortIndex2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 1, 1, 1),
    _PortIndex2_Type()
)
portIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex2.setStatus("current")
_PermanentNetworkAddress_Type = DmiString
_PermanentNetworkAddress_Object = MibTableColumn
permanentNetworkAddress = _PermanentNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 1, 1, 2),
    _PermanentNetworkAddress_Type()
)
permanentNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permanentNetworkAddress.setStatus("current")
_CurrentNetworkAddress_Type = DmiString
_CurrentNetworkAddress_Object = MibTableColumn
currentNetworkAddress = _CurrentNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 1, 1, 3),
    _CurrentNetworkAddress_Type()
)
currentNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentNetworkAddress.setStatus("current")


class _ConnectorType_Type(Integer32):
    """Custom type connectorType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("aUI", 2),
          ("appleAUI", 10),
          ("bNC", 6),
          ("fiberMIC", 9),
          ("sTPDB9", 8),
          ("sTPRJ45", 7),
          ("uTPCategory3", 3),
          ("uTPCategory4", 4),
          ("uTPCategory5", 5),
          ("unknown", 1))
    )


_ConnectorType_Type.__name__ = "Integer32"
_ConnectorType_Object = MibTableColumn
connectorType = _ConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 1, 1, 4),
    _ConnectorType_Type()
)
connectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectorType.setStatus("current")
_DataRate_Type = DmiInteger
_DataRate_Object = MibTableColumn
dataRate = _DataRate_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 1, 1, 5),
    _DataRate_Type()
)
dataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataRate.setStatus("current")
_TotalPacketsTransmitted_Type = DmiCounter64
_TotalPacketsTransmitted_Object = MibTableColumn
totalPacketsTransmitted = _TotalPacketsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 1, 1, 6),
    _TotalPacketsTransmitted_Type()
)
totalPacketsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalPacketsTransmitted.setStatus("current")
_TotalBytesTransmitted_Type = DmiCounter64
_TotalBytesTransmitted_Object = MibTableColumn
totalBytesTransmitted = _TotalBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 1, 1, 7),
    _TotalBytesTransmitted_Type()
)
totalBytesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBytesTransmitted.setStatus("current")
_TotalPacketsReceived_Type = DmiCounter64
_TotalPacketsReceived_Object = MibTableColumn
totalPacketsReceived = _TotalPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 1, 1, 8),
    _TotalPacketsReceived_Type()
)
totalPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalPacketsReceived.setStatus("current")
_TotalBytesReceived_Type = DmiCounter64
_TotalBytesReceived_Object = MibTableColumn
totalBytesReceived = _TotalBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 1, 1, 9),
    _TotalBytesReceived_Type()
)
totalBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBytesReceived.setStatus("current")
_TotalTransmitErrors_Type = DmiCounter64
_TotalTransmitErrors_Object = MibTableColumn
totalTransmitErrors = _TotalTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 1, 1, 10),
    _TotalTransmitErrors_Type()
)
totalTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalTransmitErrors.setStatus("current")
_TotalReceiveErrors_Type = DmiCounter64
_TotalReceiveErrors_Object = MibTableColumn
totalReceiveErrors = _TotalReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 1, 1, 11),
    _TotalReceiveErrors_Type()
)
totalReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalReceiveErrors.setStatus("current")
_TotalHostErrors_Type = DmiCounter64
_TotalHostErrors_Object = MibTableColumn
totalHostErrors = _TotalHostErrors_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 1, 1, 12),
    _TotalHostErrors_Type()
)
totalHostErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalHostErrors.setStatus("current")
_TotalWireErrors_Type = DmiCounter64
_TotalWireErrors_Object = MibTableColumn
totalWireErrors = _TotalWireErrors_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 1, 1, 13),
    _TotalWireErrors_Type()
)
totalWireErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalWireErrors.setStatus("current")
_Dmtf802AlternateAddressTable_Object = MibTable
dmtf802AlternateAddressTable = _Dmtf802AlternateAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 2)
)
if mibBuilder.loadTexts:
    dmtf802AlternateAddressTable.setStatus("current")
_Dmtf802AlternateAddressEntry_Object = MibTableRow
dmtf802AlternateAddressEntry = _Dmtf802AlternateAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 2, 1)
)
dmtf802AlternateAddressEntry.setIndexNames(
    (0, "DMTF-LAN-ADAPTER-MIB", "DmiCompId"),
    (0, "DMTF-LAN-ADAPTER-MIB", "DmiGroupId"),
    (0, "DMTF-LAN-ADAPTER-MIB", "alternateAddressIndex"),
)
if mibBuilder.loadTexts:
    dmtf802AlternateAddressEntry.setStatus("current")


class _Dmtf802AlternateAddressState_Type(Integer32):
    """Custom type dmtf802AlternateAddressState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_Dmtf802AlternateAddressState_Type.__name__ = "Integer32"
_Dmtf802AlternateAddressState_Object = MibTableColumn
dmtf802AlternateAddressState = _Dmtf802AlternateAddressState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 2, 1, 0),
    _Dmtf802AlternateAddressState_Type()
)
dmtf802AlternateAddressState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtf802AlternateAddressState.setStatus("current")
_AlternateAddressIndex_Type = DmiInteger
_AlternateAddressIndex_Object = MibTableColumn
alternateAddressIndex = _AlternateAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 2, 1, 1),
    _AlternateAddressIndex_Type()
)
alternateAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alternateAddressIndex.setStatus("current")
_PortIndex_Type = DmiInteger
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 2, 1, 2),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("current")


class _AddressType_Type(Integer32):
    """Custom type addressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("functional", 2),
          ("group", 3),
          ("multicast", 1))
    )


_AddressType_Type.__name__ = "Integer32"
_AddressType_Object = MibTableColumn
addressType = _AddressType_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 2, 1, 3),
    _AddressType_Type()
)
addressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addressType.setStatus("current")
_AlternateAddress_Type = DmiString
_AlternateAddress_Object = MibTableColumn
alternateAddress = _AlternateAddress_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 2, 1, 4),
    _AlternateAddress_Type()
)
alternateAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alternateAddress.setStatus("current")
_DmtfNetworkAdapterDriverTable_Object = MibTable
dmtfNetworkAdapterDriverTable = _DmtfNetworkAdapterDriverTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 3)
)
if mibBuilder.loadTexts:
    dmtfNetworkAdapterDriverTable.setStatus("current")
_DmtfNetworkAdapterDriverEntry_Object = MibTableRow
dmtfNetworkAdapterDriverEntry = _DmtfNetworkAdapterDriverEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 3, 1)
)
dmtfNetworkAdapterDriverEntry.setIndexNames(
    (0, "DMTF-LAN-ADAPTER-MIB", "DmiCompId"),
    (0, "DMTF-LAN-ADAPTER-MIB", "DmiGroupId"),
    (0, "DMTF-LAN-ADAPTER-MIB", "driverIndex"),
)
if mibBuilder.loadTexts:
    dmtfNetworkAdapterDriverEntry.setStatus("current")


class _DmtfNetworkAdapterDriverState_Type(Integer32):
    """Custom type dmtfNetworkAdapterDriverState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DmtfNetworkAdapterDriverState_Type.__name__ = "Integer32"
_DmtfNetworkAdapterDriverState_Object = MibTableColumn
dmtfNetworkAdapterDriverState = _DmtfNetworkAdapterDriverState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 3, 1, 0),
    _DmtfNetworkAdapterDriverState_Type()
)
dmtfNetworkAdapterDriverState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtfNetworkAdapterDriverState.setStatus("current")
_DriverIndex_Type = DmiInteger
_DriverIndex_Object = MibTableColumn
driverIndex = _DriverIndex_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 3, 1, 1),
    _DriverIndex_Type()
)
driverIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverIndex.setStatus("current")
_DriverSoftwareName_Type = DmiString
_DriverSoftwareName_Object = MibTableColumn
driverSoftwareName = _DriverSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 3, 1, 2),
    _DriverSoftwareName_Type()
)
driverSoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverSoftwareName.setStatus("current")
_DriverSoftwareVersion_Type = DmiString
_DriverSoftwareVersion_Object = MibTableColumn
driverSoftwareVersion = _DriverSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 3, 1, 3),
    _DriverSoftwareVersion_Type()
)
driverSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverSoftwareVersion.setStatus("current")
_DriverSoftwareDescription_Type = DmiString
_DriverSoftwareDescription_Object = MibTableColumn
driverSoftwareDescription = _DriverSoftwareDescription_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 3, 1, 4),
    _DriverSoftwareDescription_Type()
)
driverSoftwareDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverSoftwareDescription.setStatus("current")
_DriverSize_Type = DmiInteger
_DriverSize_Object = MibTableColumn
driverSize = _DriverSize_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 3, 1, 5),
    _DriverSize_Type()
)
driverSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverSize.setStatus("current")


class _DriverInterfaceType_Type(Integer32):
    """Custom type driverInterfaceType based on Integer32"""
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
        *(("appletalk", 8),
          ("iBMLanSupportProgram", 9),
          ("iPX", 2),
          ("lANtastic", 6),
          ("lLC", 10),
          ("nDIS", 4),
          ("netbios", 11),
          ("oDI", 3),
          ("other", 1),
          ("packetDriver", 5),
          ("pathworksDLL", 12),
          ("uNIX", 7))
    )


_DriverInterfaceType_Type.__name__ = "Integer32"
_DriverInterfaceType_Object = MibTableColumn
driverInterfaceType = _DriverInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 3, 1, 6),
    _DriverInterfaceType_Type()
)
driverInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverInterfaceType.setStatus("current")
_DriverInterfaceVersion_Type = DmiString
_DriverInterfaceVersion_Object = MibTableColumn
driverInterfaceVersion = _DriverInterfaceVersion_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 3, 1, 7),
    _DriverInterfaceVersion_Type()
)
driverInterfaceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverInterfaceVersion.setStatus("current")
_DriverInterfaceDescription_Type = DmiString
_DriverInterfaceDescription_Object = MibTableColumn
driverInterfaceDescription = _DriverInterfaceDescription_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 3, 1, 8),
    _DriverInterfaceDescription_Type()
)
driverInterfaceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverInterfaceDescription.setStatus("current")
_DmtfNetworkAdapterHardwareTable_Object = MibTable
dmtfNetworkAdapterHardwareTable = _DmtfNetworkAdapterHardwareTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 4)
)
if mibBuilder.loadTexts:
    dmtfNetworkAdapterHardwareTable.setStatus("current")
_DmtfNetworkAdapterHardwareEntry_Object = MibTableRow
dmtfNetworkAdapterHardwareEntry = _DmtfNetworkAdapterHardwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 4, 1)
)
dmtfNetworkAdapterHardwareEntry.setIndexNames(
    (0, "DMTF-LAN-ADAPTER-MIB", "DmiCompId"),
    (0, "DMTF-LAN-ADAPTER-MIB", "DmiGroupId"),
)
if mibBuilder.loadTexts:
    dmtfNetworkAdapterHardwareEntry.setStatus("current")


class _NetworkTopology_Type(Integer32):
    """Custom type networkTopology based on Integer32"""
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
        *(("aTM", 12),
          ("appleTalk", 13),
          ("fDDI", 11),
          ("other", 1),
          ("x10010MbpsEthernet", 4),
          ("x100MbpsEthernet", 3),
          ("x100MbpsVGAnyLAN", 5),
          ("x10MbpsEthernet", 2),
          ("x164MbpsTokenRing", 8),
          ("x16MbpsTokenRing", 7),
          ("x20MbpsArcnet", 10),
          ("x2MbpsArcnet", 9),
          ("x4MbpsTokenRing", 6))
    )


_NetworkTopology_Type.__name__ = "Integer32"
_NetworkTopology_Object = MibTableColumn
networkTopology = _NetworkTopology_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 4, 1, 1),
    _NetworkTopology_Type()
)
networkTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkTopology.setStatus("current")


class _TransmissionCapability_Type(Integer32):
    """Custom type transmissionCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 2),
          ("normal", 1))
    )


_TransmissionCapability_Type.__name__ = "Integer32"
_TransmissionCapability_Object = MibTableColumn
transmissionCapability = _TransmissionCapability_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 4, 1, 2),
    _TransmissionCapability_Type()
)
transmissionCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmissionCapability.setStatus("current")
_NetworkAdapterRAMSize_Type = DmiInteger
_NetworkAdapterRAMSize_Object = MibTableColumn
networkAdapterRAMSize = _NetworkAdapterRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 4, 1, 3),
    _NetworkAdapterRAMSize_Type()
)
networkAdapterRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAdapterRAMSize.setStatus("current")


class _BusType_Type(Integer32):
    """Custom type busType based on Integer32"""
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
              256)
        )
    )
    namedValues = NamedValues(
        *(("eISA", 3),
          ("iSA", 2),
          ("mCA", 4),
          ("motherboard", 256),
          ("nEC98", 9),
          ("other", 1),
          ("pCI", 5),
          ("pCMCIA", 7),
          ("parallel", 8),
          ("vL", 6))
    )


_BusType_Type.__name__ = "Integer32"
_BusType_Object = MibTableColumn
busType = _BusType_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 4, 1, 4),
    _BusType_Type()
)
busType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busType.setStatus("current")


class _BusWidth_Type(Integer32):
    """Custom type busWidth based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("x128BitCard", 7),
          ("x16BitCard", 4),
          ("x32BitCard", 5),
          ("x64BitCard", 6),
          ("x8BitCard", 3))
    )


_BusWidth_Type.__name__ = "Integer32"
_BusWidth_Object = MibTableColumn
busWidth = _BusWidth_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 4, 1, 5),
    _BusWidth_Type()
)
busWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busWidth.setStatus("current")
_DmtfBootROMConfigurationTable_Object = MibTable
dmtfBootROMConfigurationTable = _DmtfBootROMConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 5)
)
if mibBuilder.loadTexts:
    dmtfBootROMConfigurationTable.setStatus("current")
_DmtfBootROMConfigurationEntry_Object = MibTableRow
dmtfBootROMConfigurationEntry = _DmtfBootROMConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 5, 1)
)
dmtfBootROMConfigurationEntry.setIndexNames(
    (0, "DMTF-LAN-ADAPTER-MIB", "DmiCompId"),
    (0, "DMTF-LAN-ADAPTER-MIB", "DmiGroupId"),
)
if mibBuilder.loadTexts:
    dmtfBootROMConfigurationEntry.setStatus("current")
_BootROMDescription_Type = DmiString
_BootROMDescription_Object = MibTableColumn
bootROMDescription = _BootROMDescription_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 5, 1, 1),
    _BootROMDescription_Type()
)
bootROMDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootROMDescription.setStatus("current")
_BootROMVersion_Type = DmiString
_BootROMVersion_Object = MibTableColumn
bootROMVersion = _BootROMVersion_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 5, 1, 2),
    _BootROMVersion_Type()
)
bootROMVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootROMVersion.setStatus("current")


class _RemoteBootProtocolType_Type(Integer32):
    """Custom type remoteBootProtocolType based on Integer32"""
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
        *(("bootP", 4),
          ("dECMOP", 5),
          ("nativeNetWare", 6),
          ("none", 2),
          ("other", 1),
          ("rPL", 3))
    )


_RemoteBootProtocolType_Type.__name__ = "Integer32"
_RemoteBootProtocolType_Object = MibTableColumn
remoteBootProtocolType = _RemoteBootProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 5, 1, 3),
    _RemoteBootProtocolType_Type()
)
remoteBootProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteBootProtocolType.setStatus("current")
_RemoteBootProtocolVersion_Type = DmiString
_RemoteBootProtocolVersion_Object = MibTableColumn
remoteBootProtocolVersion = _RemoteBootProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 5, 1, 4),
    _RemoteBootProtocolVersion_Type()
)
remoteBootProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteBootProtocolVersion.setStatus("current")
_DmtfBootROMCapabilitiesTable_Object = MibTable
dmtfBootROMCapabilitiesTable = _DmtfBootROMCapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 6)
)
if mibBuilder.loadTexts:
    dmtfBootROMCapabilitiesTable.setStatus("current")
_DmtfBootROMCapabilitiesEntry_Object = MibTableRow
dmtfBootROMCapabilitiesEntry = _DmtfBootROMCapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 6, 1)
)
dmtfBootROMCapabilitiesEntry.setIndexNames(
    (0, "DMTF-LAN-ADAPTER-MIB", "DmiCompId"),
    (0, "DMTF-LAN-ADAPTER-MIB", "DmiGroupId"),
    (0, "DMTF-LAN-ADAPTER-MIB", "capabilityIndex"),
)
if mibBuilder.loadTexts:
    dmtfBootROMCapabilitiesEntry.setStatus("current")


class _DmtfBootROMCapabilitiesState_Type(Integer32):
    """Custom type dmtfBootROMCapabilitiesState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DmtfBootROMCapabilitiesState_Type.__name__ = "Integer32"
_DmtfBootROMCapabilitiesState_Object = MibTableColumn
dmtfBootROMCapabilitiesState = _DmtfBootROMCapabilitiesState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 6, 1, 0),
    _DmtfBootROMCapabilitiesState_Type()
)
dmtfBootROMCapabilitiesState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtfBootROMCapabilitiesState.setStatus("current")
_CapabilityIndex_Type = DmiInteger
_CapabilityIndex_Object = MibTableColumn
capabilityIndex = _CapabilityIndex_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 6, 1, 1),
    _CapabilityIndex_Type()
)
capabilityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capabilityIndex.setStatus("current")
_CapabilityDescription_Type = DmiString
_CapabilityDescription_Object = MibTableColumn
capabilityDescription = _CapabilityDescription_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 6, 1, 2),
    _CapabilityDescription_Type()
)
capabilityDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capabilityDescription.setStatus("current")
_CapabilityStatus_Type = DmiString
_CapabilityStatus_Object = MibTableColumn
capabilityStatus = _CapabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 2, 6, 1, 3),
    _CapabilityStatus_Type()
)
capabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capabilityStatus.setStatus("current")
_DmtfDynOids_ObjectIdentity = ObjectIdentity
dmtfDynOids = _DmtfDynOids_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DMTF-LAN-ADAPTER-MIB",
    **{"DmiCounter": DmiCounter,
       "DmiCounter64": DmiCounter64,
       "DmiGauge": DmiGauge,
       "DmiInteger": DmiInteger,
       "DmiOctetstring": DmiOctetstring,
       "DmiCompId": DmiCompId,
       "DmiGroupId": DmiGroupId,
       "dmtf": dmtf,
       "dmtfStdMifs": dmtfStdMifs,
       "dmtfLANAdapterMIF": dmtfLANAdapterMIF,
       "dmtfNetworkAdapter802PortTable": dmtfNetworkAdapter802PortTable,
       "dmtfNetworkAdapter802PortEntry": dmtfNetworkAdapter802PortEntry,
       "dmtfNetworkAdapter802PortState": dmtfNetworkAdapter802PortState,
       "portIndex2": portIndex2,
       "permanentNetworkAddress": permanentNetworkAddress,
       "currentNetworkAddress": currentNetworkAddress,
       "connectorType": connectorType,
       "dataRate": dataRate,
       "totalPacketsTransmitted": totalPacketsTransmitted,
       "totalBytesTransmitted": totalBytesTransmitted,
       "totalPacketsReceived": totalPacketsReceived,
       "totalBytesReceived": totalBytesReceived,
       "totalTransmitErrors": totalTransmitErrors,
       "totalReceiveErrors": totalReceiveErrors,
       "totalHostErrors": totalHostErrors,
       "totalWireErrors": totalWireErrors,
       "dmtf802AlternateAddressTable": dmtf802AlternateAddressTable,
       "dmtf802AlternateAddressEntry": dmtf802AlternateAddressEntry,
       "dmtf802AlternateAddressState": dmtf802AlternateAddressState,
       "alternateAddressIndex": alternateAddressIndex,
       "portIndex": portIndex,
       "addressType": addressType,
       "alternateAddress": alternateAddress,
       "dmtfNetworkAdapterDriverTable": dmtfNetworkAdapterDriverTable,
       "dmtfNetworkAdapterDriverEntry": dmtfNetworkAdapterDriverEntry,
       "dmtfNetworkAdapterDriverState": dmtfNetworkAdapterDriverState,
       "driverIndex": driverIndex,
       "driverSoftwareName": driverSoftwareName,
       "driverSoftwareVersion": driverSoftwareVersion,
       "driverSoftwareDescription": driverSoftwareDescription,
       "driverSize": driverSize,
       "driverInterfaceType": driverInterfaceType,
       "driverInterfaceVersion": driverInterfaceVersion,
       "driverInterfaceDescription": driverInterfaceDescription,
       "dmtfNetworkAdapterHardwareTable": dmtfNetworkAdapterHardwareTable,
       "dmtfNetworkAdapterHardwareEntry": dmtfNetworkAdapterHardwareEntry,
       "networkTopology": networkTopology,
       "transmissionCapability": transmissionCapability,
       "networkAdapterRAMSize": networkAdapterRAMSize,
       "busType": busType,
       "busWidth": busWidth,
       "dmtfBootROMConfigurationTable": dmtfBootROMConfigurationTable,
       "dmtfBootROMConfigurationEntry": dmtfBootROMConfigurationEntry,
       "bootROMDescription": bootROMDescription,
       "bootROMVersion": bootROMVersion,
       "remoteBootProtocolType": remoteBootProtocolType,
       "remoteBootProtocolVersion": remoteBootProtocolVersion,
       "dmtfBootROMCapabilitiesTable": dmtfBootROMCapabilitiesTable,
       "dmtfBootROMCapabilitiesEntry": dmtfBootROMCapabilitiesEntry,
       "dmtfBootROMCapabilitiesState": dmtfBootROMCapabilitiesState,
       "capabilityIndex": capabilityIndex,
       "capabilityDescription": capabilityDescription,
       "capabilityStatus": capabilityStatus,
       "dmtfDynOids": dmtfDynOids}
)
