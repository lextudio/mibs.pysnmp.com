# SNMP MIB module (NOVELSAT-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOVELSAT-COMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:04 2024
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(ItuPerceivedSeverity,) = mibBuilder.importSymbols(
    "ITU-ALARM-TC-MIB",
    "ItuPerceivedSeverity")

(nsRoot,) = mibBuilder.importSymbols(
    "NOVELSAT-ROOT-MIB",
    "nsRoot")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

nsCommon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2)
)
nsCommon.setRevisions(
        ("2010-09-12 15:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsCommonConfig_ObjectIdentity = ObjectIdentity
nsCommonConfig = _NsCommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1)
)
if mibBuilder.loadTexts:
    nsCommonConfig.setStatus("current")
_NsCommonConfigManagementIP_ObjectIdentity = ObjectIdentity
nsCommonConfigManagementIP = _NsCommonConfigManagementIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 3)
)
if mibBuilder.loadTexts:
    nsCommonConfigManagementIP.setStatus("current")
_NsCommonConfigMgmtHostIP_Type = IpAddress
_NsCommonConfigMgmtHostIP_Object = MibScalar
nsCommonConfigMgmtHostIP = _NsCommonConfigMgmtHostIP_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 3, 1),
    _NsCommonConfigMgmtHostIP_Type()
)
nsCommonConfigMgmtHostIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfigMgmtHostIP.setStatus("current")
_NsCommonConfigMgmtHostMask_Type = IpAddress
_NsCommonConfigMgmtHostMask_Object = MibScalar
nsCommonConfigMgmtHostMask = _NsCommonConfigMgmtHostMask_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 3, 2),
    _NsCommonConfigMgmtHostMask_Type()
)
nsCommonConfigMgmtHostMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfigMgmtHostMask.setStatus("current")
_NsCommonConfigMgmtHostGW_Type = IpAddress
_NsCommonConfigMgmtHostGW_Object = MibScalar
nsCommonConfigMgmtHostGW = _NsCommonConfigMgmtHostGW_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 3, 3),
    _NsCommonConfigMgmtHostGW_Type()
)
nsCommonConfigMgmtHostGW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfigMgmtHostGW.setStatus("current")


class _NsCommonConfigMgmtHostDHCP_Type(Integer32):
    """Custom type nsCommonConfigMgmtHostDHCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NsCommonConfigMgmtHostDHCP_Type.__name__ = "Integer32"
_NsCommonConfigMgmtHostDHCP_Object = MibScalar
nsCommonConfigMgmtHostDHCP = _NsCommonConfigMgmtHostDHCP_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 3, 4),
    _NsCommonConfigMgmtHostDHCP_Type()
)
nsCommonConfigMgmtHostDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfigMgmtHostDHCP.setStatus("current")
_NsCommonConfigMgmtHostDNS_Type = IpAddress
_NsCommonConfigMgmtHostDNS_Object = MibScalar
nsCommonConfigMgmtHostDNS = _NsCommonConfigMgmtHostDNS_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 3, 5),
    _NsCommonConfigMgmtHostDNS_Type()
)
nsCommonConfigMgmtHostDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfigMgmtHostDNS.setStatus("current")
_NsCommonConfig10MhzClock_ObjectIdentity = ObjectIdentity
nsCommonConfig10MhzClock = _NsCommonConfig10MhzClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 4)
)
if mibBuilder.loadTexts:
    nsCommonConfig10MhzClock.setStatus("current")


class _NsCommonConfig10MhzClockSource_Type(Integer32):
    """Custom type nsCommonConfig10MhzClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 0))
    )


_NsCommonConfig10MhzClockSource_Type.__name__ = "Integer32"
_NsCommonConfig10MhzClockSource_Object = MibScalar
nsCommonConfig10MhzClockSource = _NsCommonConfig10MhzClockSource_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 4, 1),
    _NsCommonConfig10MhzClockSource_Type()
)
nsCommonConfig10MhzClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfig10MhzClockSource.setStatus("current")


class _NsCommonConfig10MhzClockOut_Type(Integer32):
    """Custom type nsCommonConfig10MhzClockOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NsCommonConfig10MhzClockOut_Type.__name__ = "Integer32"
_NsCommonConfig10MhzClockOut_Object = MibScalar
nsCommonConfig10MhzClockOut = _NsCommonConfig10MhzClockOut_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 4, 2),
    _NsCommonConfig10MhzClockOut_Type()
)
nsCommonConfig10MhzClockOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfig10MhzClockOut.setStatus("current")


class _NsCommonConfig10MhzClockTxPortClock_Type(Integer32):
    """Custom type nsCommonConfig10MhzClockTxPortClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("buc", 2),
          ("lband", 1),
          ("off", 0))
    )


_NsCommonConfig10MhzClockTxPortClock_Type.__name__ = "Integer32"
_NsCommonConfig10MhzClockTxPortClock_Object = MibScalar
nsCommonConfig10MhzClockTxPortClock = _NsCommonConfig10MhzClockTxPortClock_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 4, 3),
    _NsCommonConfig10MhzClockTxPortClock_Type()
)
nsCommonConfig10MhzClockTxPortClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfig10MhzClockTxPortClock.setStatus("current")


class _NsCommonConfig10MhzClockLnbRefClock_Type(Integer32):
    """Custom type nsCommonConfig10MhzClockLnbRefClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NsCommonConfig10MhzClockLnbRefClock_Type.__name__ = "Integer32"
_NsCommonConfig10MhzClockLnbRefClock_Object = MibScalar
nsCommonConfig10MhzClockLnbRefClock = _NsCommonConfig10MhzClockLnbRefClock_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 4, 4),
    _NsCommonConfig10MhzClockLnbRefClock_Type()
)
nsCommonConfig10MhzClockLnbRefClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfig10MhzClockLnbRefClock.setStatus("current")
_NsCommonConfigSerialPort_ObjectIdentity = ObjectIdentity
nsCommonConfigSerialPort = _NsCommonConfigSerialPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 5)
)
if mibBuilder.loadTexts:
    nsCommonConfigSerialPort.setStatus("current")


class _NsCommonConfigSerialPortBaudRate_Type(Integer32):
    """Custom type nsCommonConfigSerialPortBaudRate based on Integer32"""
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
        *(("baudRate115200", 3),
          ("baudRate19200", 1),
          ("baudRate38400", 2),
          ("baudRate9600", 0))
    )


_NsCommonConfigSerialPortBaudRate_Type.__name__ = "Integer32"
_NsCommonConfigSerialPortBaudRate_Object = MibScalar
nsCommonConfigSerialPortBaudRate = _NsCommonConfigSerialPortBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 5, 1),
    _NsCommonConfigSerialPortBaudRate_Type()
)
nsCommonConfigSerialPortBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfigSerialPortBaudRate.setStatus("current")


class _NsCommonConfigSerialPortParity_Type(Integer32):
    """Custom type nsCommonConfigSerialPortParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("even", 1),
          ("none", 2),
          ("odd", 0))
    )


_NsCommonConfigSerialPortParity_Type.__name__ = "Integer32"
_NsCommonConfigSerialPortParity_Object = MibScalar
nsCommonConfigSerialPortParity = _NsCommonConfigSerialPortParity_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 5, 2),
    _NsCommonConfigSerialPortParity_Type()
)
nsCommonConfigSerialPortParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfigSerialPortParity.setStatus("current")


class _NsCommonConfigSerialPortDataBits_Type(Integer32):
    """Custom type nsCommonConfigSerialPortDataBits based on Integer32"""
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
        *(("dataBits5", 0),
          ("dataBits6", 1),
          ("dataBits7", 2),
          ("dataBits8", 3))
    )


_NsCommonConfigSerialPortDataBits_Type.__name__ = "Integer32"
_NsCommonConfigSerialPortDataBits_Object = MibScalar
nsCommonConfigSerialPortDataBits = _NsCommonConfigSerialPortDataBits_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 5, 3),
    _NsCommonConfigSerialPortDataBits_Type()
)
nsCommonConfigSerialPortDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfigSerialPortDataBits.setStatus("current")


class _NsCommonConfigSerialPortStopBit_Type(Integer32):
    """Custom type nsCommonConfigSerialPortStopBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("stopBit1", 0),
          ("stopBit2", 1))
    )


_NsCommonConfigSerialPortStopBit_Type.__name__ = "Integer32"
_NsCommonConfigSerialPortStopBit_Object = MibScalar
nsCommonConfigSerialPortStopBit = _NsCommonConfigSerialPortStopBit_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 5, 4),
    _NsCommonConfigSerialPortStopBit_Type()
)
nsCommonConfigSerialPortStopBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfigSerialPortStopBit.setStatus("current")
_NsCommonConfigDateTime_ObjectIdentity = ObjectIdentity
nsCommonConfigDateTime = _NsCommonConfigDateTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 6)
)
if mibBuilder.loadTexts:
    nsCommonConfigDateTime.setStatus("current")
_NsCommonConfigDateAndTime_Type = DateAndTime
_NsCommonConfigDateAndTime_Object = MibScalar
nsCommonConfigDateAndTime = _NsCommonConfigDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 6, 1),
    _NsCommonConfigDateAndTime_Type()
)
nsCommonConfigDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfigDateAndTime.setStatus("current")
_NsCommonConfigNetwork_ObjectIdentity = ObjectIdentity
nsCommonConfigNetwork = _NsCommonConfigNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7)
)
if mibBuilder.loadTexts:
    nsCommonConfigNetwork.setStatus("current")
_NsCommonConfigNetworkForwardingMode_ObjectIdentity = ObjectIdentity
nsCommonConfigNetworkForwardingMode = _NsCommonConfigNetworkForwardingMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkForwardingMode.setStatus("current")


class _NsCommonConfigNetworkMode_Type(Integer32):
    """Custom type nsCommonConfigNetworkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("l2TransparentBridging", 0),
          ("l2VlanSwitching", 1),
          ("l3IpRouting", 2),
          ("notApplicable", 255))
    )


_NsCommonConfigNetworkMode_Type.__name__ = "Integer32"
_NsCommonConfigNetworkMode_Object = MibScalar
nsCommonConfigNetworkMode = _NsCommonConfigNetworkMode_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 1, 1),
    _NsCommonConfigNetworkMode_Type()
)
nsCommonConfigNetworkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkMode.setStatus("current")
_NsCommonConfigNetworkInterfaces_ObjectIdentity = ObjectIdentity
nsCommonConfigNetworkInterfaces = _NsCommonConfigNetworkInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkInterfaces.setStatus("current")
_NsCommonConfigNetworkInterfacesTable_Object = MibTable
nsCommonConfigNetworkInterfacesTable = _NsCommonConfigNetworkInterfacesTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkInterfacesTable.setStatus("current")
_NsCommonConfigNetworkInterfacesEntry_Object = MibTableRow
nsCommonConfigNetworkInterfacesEntry = _NsCommonConfigNetworkInterfacesEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 2, 1, 1)
)
nsCommonConfigNetworkInterfacesEntry.setIndexNames(
    (0, "NOVELSAT-COMMON-MIB", "nsCommonConfigNetworkInterfacesIndex"),
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkInterfacesEntry.setStatus("current")
_NsCommonConfigNetworkInterfacesIndex_Type = Unsigned32
_NsCommonConfigNetworkInterfacesIndex_Object = MibTableColumn
nsCommonConfigNetworkInterfacesIndex = _NsCommonConfigNetworkInterfacesIndex_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 2, 1, 1, 1),
    _NsCommonConfigNetworkInterfacesIndex_Type()
)
nsCommonConfigNetworkInterfacesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkInterfacesIndex.setStatus("current")


class _NsCommonConfigNetworkInterfacesName_Type(DisplayString):
    """Custom type nsCommonConfigNetworkInterfacesName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonConfigNetworkInterfacesName_Type.__name__ = "DisplayString"
_NsCommonConfigNetworkInterfacesName_Object = MibTableColumn
nsCommonConfigNetworkInterfacesName = _NsCommonConfigNetworkInterfacesName_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 2, 1, 1, 2),
    _NsCommonConfigNetworkInterfacesName_Type()
)
nsCommonConfigNetworkInterfacesName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkInterfacesName.setStatus("current")


class _NsCommonConfigNetworkInterfacesAdminStatus_Type(Integer32):
    """Custom type nsCommonConfigNetworkInterfacesAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notApplicable", 255))
    )


_NsCommonConfigNetworkInterfacesAdminStatus_Type.__name__ = "Integer32"
_NsCommonConfigNetworkInterfacesAdminStatus_Object = MibTableColumn
nsCommonConfigNetworkInterfacesAdminStatus = _NsCommonConfigNetworkInterfacesAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 2, 1, 1, 3),
    _NsCommonConfigNetworkInterfacesAdminStatus_Type()
)
nsCommonConfigNetworkInterfacesAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkInterfacesAdminStatus.setStatus("current")


class _NsCommonConfigNetworkInterfacesPortType_Type(Integer32):
    """Custom type nsCommonConfigNetworkInterfacesPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 4),
          ("lan", 0),
          ("loopback", 3),
          ("mngmt", 2),
          ("notApplicable", 255),
          ("wan", 1))
    )


_NsCommonConfigNetworkInterfacesPortType_Type.__name__ = "Integer32"
_NsCommonConfigNetworkInterfacesPortType_Object = MibTableColumn
nsCommonConfigNetworkInterfacesPortType = _NsCommonConfigNetworkInterfacesPortType_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 2, 1, 1, 4),
    _NsCommonConfigNetworkInterfacesPortType_Type()
)
nsCommonConfigNetworkInterfacesPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkInterfacesPortType.setStatus("current")
_NsCommonConfigNetworkInterfacesMtu_Type = Unsigned32
_NsCommonConfigNetworkInterfacesMtu_Object = MibTableColumn
nsCommonConfigNetworkInterfacesMtu = _NsCommonConfigNetworkInterfacesMtu_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 2, 1, 1, 6),
    _NsCommonConfigNetworkInterfacesMtu_Type()
)
nsCommonConfigNetworkInterfacesMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkInterfacesMtu.setStatus("current")
_NsCommonConfigNetworkInterfacesVlan_Type = Unsigned32
_NsCommonConfigNetworkInterfacesVlan_Object = MibTableColumn
nsCommonConfigNetworkInterfacesVlan = _NsCommonConfigNetworkInterfacesVlan_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 2, 1, 1, 7),
    _NsCommonConfigNetworkInterfacesVlan_Type()
)
nsCommonConfigNetworkInterfacesVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkInterfacesVlan.setStatus("current")
_NsCommonConfigNetworkInterfacesIp_Type = IpAddress
_NsCommonConfigNetworkInterfacesIp_Object = MibTableColumn
nsCommonConfigNetworkInterfacesIp = _NsCommonConfigNetworkInterfacesIp_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 2, 1, 1, 8),
    _NsCommonConfigNetworkInterfacesIp_Type()
)
nsCommonConfigNetworkInterfacesIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkInterfacesIp.setStatus("current")


class _NsCommonConfigNetworkInterfacesMac_Type(DisplayString):
    """Custom type nsCommonConfigNetworkInterfacesMac based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonConfigNetworkInterfacesMac_Type.__name__ = "DisplayString"
_NsCommonConfigNetworkInterfacesMac_Object = MibTableColumn
nsCommonConfigNetworkInterfacesMac = _NsCommonConfigNetworkInterfacesMac_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 2, 1, 1, 9),
    _NsCommonConfigNetworkInterfacesMac_Type()
)
nsCommonConfigNetworkInterfacesMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkInterfacesMac.setStatus("current")
_NsCommonConfigNetworkInterfacesSubnetMask_Type = IpAddress
_NsCommonConfigNetworkInterfacesSubnetMask_Object = MibTableColumn
nsCommonConfigNetworkInterfacesSubnetMask = _NsCommonConfigNetworkInterfacesSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 2, 1, 1, 10),
    _NsCommonConfigNetworkInterfacesSubnetMask_Type()
)
nsCommonConfigNetworkInterfacesSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkInterfacesSubnetMask.setStatus("current")


class _NsCommonConfigNetworkInterfacesEncapsulation_Type(Integer32):
    """Custom type nsCommonConfigNetworkInterfacesEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("encapsulationEth", 0),
          ("encapsulationEth8021q", 1),
          ("gse", 3),
          ("notApplicable", 255),
          ("nspe", 4),
          ("nspe2", 5),
          ("ule", 2))
    )


_NsCommonConfigNetworkInterfacesEncapsulation_Type.__name__ = "Integer32"
_NsCommonConfigNetworkInterfacesEncapsulation_Object = MibTableColumn
nsCommonConfigNetworkInterfacesEncapsulation = _NsCommonConfigNetworkInterfacesEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 2, 1, 1, 11),
    _NsCommonConfigNetworkInterfacesEncapsulation_Type()
)
nsCommonConfigNetworkInterfacesEncapsulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkInterfacesEncapsulation.setStatus("current")


class _NsCommonConfigNetworkInterfacesManagementControl_Type(Integer32):
    """Custom type nsCommonConfigNetworkInterfacesManagementControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notApplicable", 255))
    )


_NsCommonConfigNetworkInterfacesManagementControl_Type.__name__ = "Integer32"
_NsCommonConfigNetworkInterfacesManagementControl_Object = MibTableColumn
nsCommonConfigNetworkInterfacesManagementControl = _NsCommonConfigNetworkInterfacesManagementControl_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 2, 1, 1, 12),
    _NsCommonConfigNetworkInterfacesManagementControl_Type()
)
nsCommonConfigNetworkInterfacesManagementControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkInterfacesManagementControl.setStatus("current")


class _NsCommonConfigNetworkInterfacesAcmControl_Type(Integer32):
    """Custom type nsCommonConfigNetworkInterfacesAcmControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notApplicable", 255))
    )


_NsCommonConfigNetworkInterfacesAcmControl_Type.__name__ = "Integer32"
_NsCommonConfigNetworkInterfacesAcmControl_Object = MibTableColumn
nsCommonConfigNetworkInterfacesAcmControl = _NsCommonConfigNetworkInterfacesAcmControl_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 2, 1, 1, 13),
    _NsCommonConfigNetworkInterfacesAcmControl_Type()
)
nsCommonConfigNetworkInterfacesAcmControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkInterfacesAcmControl.setStatus("current")
_NsCommonConfigNetworkInterfacesNotifyRowStatus_Type = RowStatus
_NsCommonConfigNetworkInterfacesNotifyRowStatus_Object = MibTableColumn
nsCommonConfigNetworkInterfacesNotifyRowStatus = _NsCommonConfigNetworkInterfacesNotifyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 2, 1, 1, 14),
    _NsCommonConfigNetworkInterfacesNotifyRowStatus_Type()
)
nsCommonConfigNetworkInterfacesNotifyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkInterfacesNotifyRowStatus.setStatus("current")
_NsCommonConfigNetworkNeighbors_ObjectIdentity = ObjectIdentity
nsCommonConfigNetworkNeighbors = _NsCommonConfigNetworkNeighbors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 3)
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkNeighbors.setStatus("current")
_NsCommonConfigNetworkNeighborsTable_Object = MibTable
nsCommonConfigNetworkNeighborsTable = _NsCommonConfigNetworkNeighborsTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 3, 1)
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkNeighborsTable.setStatus("current")
_NsCommonConfigNetworkNeighborsEntry_Object = MibTableRow
nsCommonConfigNetworkNeighborsEntry = _NsCommonConfigNetworkNeighborsEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 3, 1, 1)
)
nsCommonConfigNetworkNeighborsEntry.setIndexNames(
    (0, "NOVELSAT-COMMON-MIB", "nsCommonConfigNetworkNeighborsIndex"),
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkNeighborsEntry.setStatus("current")
_NsCommonConfigNetworkNeighborsIndex_Type = Unsigned32
_NsCommonConfigNetworkNeighborsIndex_Object = MibTableColumn
nsCommonConfigNetworkNeighborsIndex = _NsCommonConfigNetworkNeighborsIndex_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 3, 1, 1, 1),
    _NsCommonConfigNetworkNeighborsIndex_Type()
)
nsCommonConfigNetworkNeighborsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkNeighborsIndex.setStatus("current")


class _NsCommonConfigNetworkNeighborsName_Type(DisplayString):
    """Custom type nsCommonConfigNetworkNeighborsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonConfigNetworkNeighborsName_Type.__name__ = "DisplayString"
_NsCommonConfigNetworkNeighborsName_Object = MibTableColumn
nsCommonConfigNetworkNeighborsName = _NsCommonConfigNetworkNeighborsName_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 3, 1, 1, 2),
    _NsCommonConfigNetworkNeighborsName_Type()
)
nsCommonConfigNetworkNeighborsName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkNeighborsName.setStatus("current")
_NsCommonConfigNetworkNeighborsIfIndex_Type = Unsigned32
_NsCommonConfigNetworkNeighborsIfIndex_Object = MibTableColumn
nsCommonConfigNetworkNeighborsIfIndex = _NsCommonConfigNetworkNeighborsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 3, 1, 1, 3),
    _NsCommonConfigNetworkNeighborsIfIndex_Type()
)
nsCommonConfigNetworkNeighborsIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkNeighborsIfIndex.setStatus("current")
_NsCommonConfigNetworkNeighborsIp_Type = IpAddress
_NsCommonConfigNetworkNeighborsIp_Object = MibTableColumn
nsCommonConfigNetworkNeighborsIp = _NsCommonConfigNetworkNeighborsIp_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 3, 1, 1, 4),
    _NsCommonConfigNetworkNeighborsIp_Type()
)
nsCommonConfigNetworkNeighborsIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkNeighborsIp.setStatus("current")


class _NsCommonConfigNetworkNeighborsMac_Type(DisplayString):
    """Custom type nsCommonConfigNetworkNeighborsMac based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonConfigNetworkNeighborsMac_Type.__name__ = "DisplayString"
_NsCommonConfigNetworkNeighborsMac_Object = MibTableColumn
nsCommonConfigNetworkNeighborsMac = _NsCommonConfigNetworkNeighborsMac_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 3, 1, 1, 5),
    _NsCommonConfigNetworkNeighborsMac_Type()
)
nsCommonConfigNetworkNeighborsMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkNeighborsMac.setStatus("current")
_NsCommonConfigNetworkNeighborsSignalingIp_Type = IpAddress
_NsCommonConfigNetworkNeighborsSignalingIp_Object = MibTableColumn
nsCommonConfigNetworkNeighborsSignalingIp = _NsCommonConfigNetworkNeighborsSignalingIp_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 3, 1, 1, 6),
    _NsCommonConfigNetworkNeighborsSignalingIp_Type()
)
nsCommonConfigNetworkNeighborsSignalingIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkNeighborsSignalingIp.setStatus("current")


class _NsCommonConfigNetworkNeighborsModulation_Type(Integer32):
    """Custom type nsCommonConfigNetworkNeighborsModulation based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("modulation16Apsk", 4),
          ("modulation16Qam", 3),
          ("modulation32Apsk", 5),
          ("modulation64Apsk", 6),
          ("modulation8Psk", 2),
          ("modulationBpsk", 0),
          ("modulationQpsk", 1),
          ("notApplicable", 255))
    )


_NsCommonConfigNetworkNeighborsModulation_Type.__name__ = "Integer32"
_NsCommonConfigNetworkNeighborsModulation_Object = MibTableColumn
nsCommonConfigNetworkNeighborsModulation = _NsCommonConfigNetworkNeighborsModulation_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 3, 1, 1, 7),
    _NsCommonConfigNetworkNeighborsModulation_Type()
)
nsCommonConfigNetworkNeighborsModulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkNeighborsModulation.setStatus("current")


class _NsCommonConfigNetworkNeighborsFecRate_Type(Integer32):
    """Custom type nsCommonConfigNetworkNeighborsFecRate based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("fec11Div15", 17),
          ("fec13Div30", 4),
          ("fec17Div30", 11),
          ("fec19Div30", 14),
          ("fec1Div2", 8),
          ("fec1Div3", 2),
          ("fec1Div4", 1),
          ("fec1Div5", 0),
          ("fec22Div45", 7),
          ("fec28Div45", 13),
          ("fec2Div3", 15),
          ("fec2Div5", 3),
          ("fec32Div45", 16),
          ("fec37Div45", 21),
          ("fec3Div4", 18),
          ("fec3Div5", 12),
          ("fec4Div5", 20),
          ("fec4Div9", 5),
          ("fec5Div6", 22),
          ("fec5Div9", 10),
          ("fec7Div15", 6),
          ("fec7Div8", 23),
          ("fec7Div9", 19),
          ("fec8Div15", 9),
          ("fec8Div9", 24),
          ("fec9Div10", 25),
          ("notApplicable", 255))
    )


_NsCommonConfigNetworkNeighborsFecRate_Type.__name__ = "Integer32"
_NsCommonConfigNetworkNeighborsFecRate_Object = MibTableColumn
nsCommonConfigNetworkNeighborsFecRate = _NsCommonConfigNetworkNeighborsFecRate_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 3, 1, 1, 8),
    _NsCommonConfigNetworkNeighborsFecRate_Type()
)
nsCommonConfigNetworkNeighborsFecRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkNeighborsFecRate.setStatus("current")
_NsCommonConfigNetworkNeighborsNotifyRowStatus_Type = RowStatus
_NsCommonConfigNetworkNeighborsNotifyRowStatus_Object = MibTableColumn
nsCommonConfigNetworkNeighborsNotifyRowStatus = _NsCommonConfigNetworkNeighborsNotifyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 3, 1, 1, 9),
    _NsCommonConfigNetworkNeighborsNotifyRowStatus_Type()
)
nsCommonConfigNetworkNeighborsNotifyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkNeighborsNotifyRowStatus.setStatus("current")
_NsCommonConfigNetworkRouting_ObjectIdentity = ObjectIdentity
nsCommonConfigNetworkRouting = _NsCommonConfigNetworkRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 4)
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkRouting.setStatus("current")
_NsCommonConfigNetworkPolicyRoute_ObjectIdentity = ObjectIdentity
nsCommonConfigNetworkPolicyRoute = _NsCommonConfigNetworkPolicyRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 4, 1)
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkPolicyRoute.setStatus("current")
_NsCommonConfigNetworkPolicyRouteTable_Object = MibTable
nsCommonConfigNetworkPolicyRouteTable = _NsCommonConfigNetworkPolicyRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 4, 1, 1)
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkPolicyRouteTable.setStatus("current")
_NsCommonConfigNetworkPolicyRouteEntry_Object = MibTableRow
nsCommonConfigNetworkPolicyRouteEntry = _NsCommonConfigNetworkPolicyRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 4, 1, 1, 1)
)
nsCommonConfigNetworkPolicyRouteEntry.setIndexNames(
    (0, "NOVELSAT-COMMON-MIB", "nsCommonConfigNetworkPolicyRouteIndex"),
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkPolicyRouteEntry.setStatus("current")
_NsCommonConfigNetworkPolicyRouteIndex_Type = Unsigned32
_NsCommonConfigNetworkPolicyRouteIndex_Object = MibTableColumn
nsCommonConfigNetworkPolicyRouteIndex = _NsCommonConfigNetworkPolicyRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 4, 1, 1, 1, 1),
    _NsCommonConfigNetworkPolicyRouteIndex_Type()
)
nsCommonConfigNetworkPolicyRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkPolicyRouteIndex.setStatus("current")
_NsCommonConfigNetworkPolicyRouteInputInterfaceId_Type = Unsigned32
_NsCommonConfigNetworkPolicyRouteInputInterfaceId_Object = MibTableColumn
nsCommonConfigNetworkPolicyRouteInputInterfaceId = _NsCommonConfigNetworkPolicyRouteInputInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 4, 1, 1, 1, 2),
    _NsCommonConfigNetworkPolicyRouteInputInterfaceId_Type()
)
nsCommonConfigNetworkPolicyRouteInputInterfaceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkPolicyRouteInputInterfaceId.setStatus("current")
_NsCommonConfigNetworkPolicyRouteRoutingTableId_Type = Unsigned32
_NsCommonConfigNetworkPolicyRouteRoutingTableId_Object = MibTableColumn
nsCommonConfigNetworkPolicyRouteRoutingTableId = _NsCommonConfigNetworkPolicyRouteRoutingTableId_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 4, 1, 1, 1, 3),
    _NsCommonConfigNetworkPolicyRouteRoutingTableId_Type()
)
nsCommonConfigNetworkPolicyRouteRoutingTableId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkPolicyRouteRoutingTableId.setStatus("current")
_NsCommonConfigNetworkPolicyRouteNotifyRowStatus_Type = RowStatus
_NsCommonConfigNetworkPolicyRouteNotifyRowStatus_Object = MibTableColumn
nsCommonConfigNetworkPolicyRouteNotifyRowStatus = _NsCommonConfigNetworkPolicyRouteNotifyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 4, 1, 1, 1, 4),
    _NsCommonConfigNetworkPolicyRouteNotifyRowStatus_Type()
)
nsCommonConfigNetworkPolicyRouteNotifyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkPolicyRouteNotifyRowStatus.setStatus("current")
_NsCommonConfigNetworkRoutes_ObjectIdentity = ObjectIdentity
nsCommonConfigNetworkRoutes = _NsCommonConfigNetworkRoutes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 4, 2)
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkRoutes.setStatus("current")
_NsCommonConfigNetworkRoutesTable_Object = MibTable
nsCommonConfigNetworkRoutesTable = _NsCommonConfigNetworkRoutesTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 4, 2, 1)
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkRoutesTable.setStatus("current")
_NsCommonConfigNetworkRoutesEntry_Object = MibTableRow
nsCommonConfigNetworkRoutesEntry = _NsCommonConfigNetworkRoutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 4, 2, 1, 1)
)
nsCommonConfigNetworkRoutesEntry.setIndexNames(
    (0, "NOVELSAT-COMMON-MIB", "nsCommonConfigNetworkRoutesDestIpAddress"),
    (0, "NOVELSAT-COMMON-MIB", "nsCommonConfigNetworkRoutesDestSubnetMask"),
    (0, "NOVELSAT-COMMON-MIB", "nsCommonConfigNetworkRoutesNexthopIpAddress"),
    (0, "NOVELSAT-COMMON-MIB", "nsCommonConfigNetworkRoutesTableId"),
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkRoutesEntry.setStatus("current")
_NsCommonConfigNetworkRoutesDestIpAddress_Type = IpAddress
_NsCommonConfigNetworkRoutesDestIpAddress_Object = MibTableColumn
nsCommonConfigNetworkRoutesDestIpAddress = _NsCommonConfigNetworkRoutesDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 4, 2, 1, 1, 1),
    _NsCommonConfigNetworkRoutesDestIpAddress_Type()
)
nsCommonConfigNetworkRoutesDestIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkRoutesDestIpAddress.setStatus("current")
_NsCommonConfigNetworkRoutesDestSubnetMask_Type = IpAddress
_NsCommonConfigNetworkRoutesDestSubnetMask_Object = MibTableColumn
nsCommonConfigNetworkRoutesDestSubnetMask = _NsCommonConfigNetworkRoutesDestSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 4, 2, 1, 1, 2),
    _NsCommonConfigNetworkRoutesDestSubnetMask_Type()
)
nsCommonConfigNetworkRoutesDestSubnetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkRoutesDestSubnetMask.setStatus("current")
_NsCommonConfigNetworkRoutesNexthopIpAddress_Type = IpAddress
_NsCommonConfigNetworkRoutesNexthopIpAddress_Object = MibTableColumn
nsCommonConfigNetworkRoutesNexthopIpAddress = _NsCommonConfigNetworkRoutesNexthopIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 4, 2, 1, 1, 3),
    _NsCommonConfigNetworkRoutesNexthopIpAddress_Type()
)
nsCommonConfigNetworkRoutesNexthopIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkRoutesNexthopIpAddress.setStatus("current")
_NsCommonConfigNetworkRoutesTableId_Type = Unsigned32
_NsCommonConfigNetworkRoutesTableId_Object = MibTableColumn
nsCommonConfigNetworkRoutesTableId = _NsCommonConfigNetworkRoutesTableId_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 4, 2, 1, 1, 4),
    _NsCommonConfigNetworkRoutesTableId_Type()
)
nsCommonConfigNetworkRoutesTableId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkRoutesTableId.setStatus("current")


class _NsCommonConfigNetworkRoutesAdminStatus_Type(Integer32):
    """Custom type nsCommonConfigNetworkRoutesAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notApplicable", 255))
    )


_NsCommonConfigNetworkRoutesAdminStatus_Type.__name__ = "Integer32"
_NsCommonConfigNetworkRoutesAdminStatus_Object = MibTableColumn
nsCommonConfigNetworkRoutesAdminStatus = _NsCommonConfigNetworkRoutesAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 4, 2, 1, 1, 5),
    _NsCommonConfigNetworkRoutesAdminStatus_Type()
)
nsCommonConfigNetworkRoutesAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkRoutesAdminStatus.setStatus("current")
_NsCommonConfigNetworkRoutesNotifyRowStatus_Type = RowStatus
_NsCommonConfigNetworkRoutesNotifyRowStatus_Object = MibTableColumn
nsCommonConfigNetworkRoutesNotifyRowStatus = _NsCommonConfigNetworkRoutesNotifyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 4, 2, 1, 1, 6),
    _NsCommonConfigNetworkRoutesNotifyRowStatus_Type()
)
nsCommonConfigNetworkRoutesNotifyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkRoutesNotifyRowStatus.setStatus("current")
_NsCommonConfigNetworkVlanSwitching_ObjectIdentity = ObjectIdentity
nsCommonConfigNetworkVlanSwitching = _NsCommonConfigNetworkVlanSwitching_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 5)
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkVlanSwitching.setStatus("current")
_NsCommonConfigNetworkVlanSwitchingTable_Object = MibTable
nsCommonConfigNetworkVlanSwitchingTable = _NsCommonConfigNetworkVlanSwitchingTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 5, 1)
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkVlanSwitchingTable.setStatus("current")
_NsCommonConfigNetworkVlanSwitchingEntry_Object = MibTableRow
nsCommonConfigNetworkVlanSwitchingEntry = _NsCommonConfigNetworkVlanSwitchingEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 5, 1, 1)
)
nsCommonConfigNetworkVlanSwitchingEntry.setIndexNames(
    (0, "NOVELSAT-COMMON-MIB", "nsCommonConfigNetworkVlanSwitchingVid"),
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkVlanSwitchingEntry.setStatus("current")
_NsCommonConfigNetworkVlanSwitchingVid_Type = Unsigned32
_NsCommonConfigNetworkVlanSwitchingVid_Object = MibTableColumn
nsCommonConfigNetworkVlanSwitchingVid = _NsCommonConfigNetworkVlanSwitchingVid_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 5, 1, 1, 1),
    _NsCommonConfigNetworkVlanSwitchingVid_Type()
)
nsCommonConfigNetworkVlanSwitchingVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkVlanSwitchingVid.setStatus("current")
_NsCommonConfigNetworkVlanSwitchingNeighborIndex_Type = Unsigned32
_NsCommonConfigNetworkVlanSwitchingNeighborIndex_Object = MibTableColumn
nsCommonConfigNetworkVlanSwitchingNeighborIndex = _NsCommonConfigNetworkVlanSwitchingNeighborIndex_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 5, 1, 1, 2),
    _NsCommonConfigNetworkVlanSwitchingNeighborIndex_Type()
)
nsCommonConfigNetworkVlanSwitchingNeighborIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkVlanSwitchingNeighborIndex.setStatus("current")


class _NsCommonConfigNetworkVlanSwitchingAdminStatus_Type(Integer32):
    """Custom type nsCommonConfigNetworkVlanSwitchingAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notApplicable", 255))
    )


_NsCommonConfigNetworkVlanSwitchingAdminStatus_Type.__name__ = "Integer32"
_NsCommonConfigNetworkVlanSwitchingAdminStatus_Object = MibTableColumn
nsCommonConfigNetworkVlanSwitchingAdminStatus = _NsCommonConfigNetworkVlanSwitchingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 5, 1, 1, 3),
    _NsCommonConfigNetworkVlanSwitchingAdminStatus_Type()
)
nsCommonConfigNetworkVlanSwitchingAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkVlanSwitchingAdminStatus.setStatus("current")
_NsCommonConfigNetworkVlanSwitchingNotifyRowStatus_Type = RowStatus
_NsCommonConfigNetworkVlanSwitchingNotifyRowStatus_Object = MibTableColumn
nsCommonConfigNetworkVlanSwitchingNotifyRowStatus = _NsCommonConfigNetworkVlanSwitchingNotifyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 5, 1, 1, 4),
    _NsCommonConfigNetworkVlanSwitchingNotifyRowStatus_Type()
)
nsCommonConfigNetworkVlanSwitchingNotifyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkVlanSwitchingNotifyRowStatus.setStatus("current")
_NsCommonConfigNetworkQoS_ObjectIdentity = ObjectIdentity
nsCommonConfigNetworkQoS = _NsCommonConfigNetworkQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6)
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkQoS.setStatus("current")
_NsCommonConfigNetworkClassification_ObjectIdentity = ObjectIdentity
nsCommonConfigNetworkClassification = _NsCommonConfigNetworkClassification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1)
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassification.setStatus("current")


class _NsCommonConfigNetworkClassificationMode_Type(Integer32):
    """Custom type nsCommonConfigNetworkClassificationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("classMode802", 0),
          ("classModeMf", 2),
          ("classModeTos", 1),
          ("notApplicable", 255))
    )


_NsCommonConfigNetworkClassificationMode_Type.__name__ = "Integer32"
_NsCommonConfigNetworkClassificationMode_Object = MibScalar
nsCommonConfigNetworkClassificationMode = _NsCommonConfigNetworkClassificationMode_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 1),
    _NsCommonConfigNetworkClassificationMode_Type()
)
nsCommonConfigNetworkClassificationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationMode.setStatus("current")
_NsCommonConfigNetworkClassification802_ObjectIdentity = ObjectIdentity
nsCommonConfigNetworkClassification802 = _NsCommonConfigNetworkClassification802_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 2)
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassification802.setStatus("current")
_NsCommonConfigNetworkClassification802Table_Object = MibTable
nsCommonConfigNetworkClassification802Table = _NsCommonConfigNetworkClassification802Table_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassification802Table.setStatus("current")
_NsCommonConfigNetworkClassification802Entry_Object = MibTableRow
nsCommonConfigNetworkClassification802Entry = _NsCommonConfigNetworkClassification802Entry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 2, 1, 1)
)
nsCommonConfigNetworkClassification802Entry.setIndexNames(
    (0, "NOVELSAT-COMMON-MIB", "nsCommonConfigNetworkClassification802Priority"),
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassification802Entry.setStatus("current")
_NsCommonConfigNetworkClassification802Priority_Type = Unsigned32
_NsCommonConfigNetworkClassification802Priority_Object = MibTableColumn
nsCommonConfigNetworkClassification802Priority = _NsCommonConfigNetworkClassification802Priority_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 2, 1, 1, 1),
    _NsCommonConfigNetworkClassification802Priority_Type()
)
nsCommonConfigNetworkClassification802Priority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassification802Priority.setStatus("current")


class _NsCommonConfigNetworkClassification802CoS_Type(Integer32):
    """Custom type nsCommonConfigNetworkClassification802CoS based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("cos0", 1),
          ("cos1", 2),
          ("cos2", 3),
          ("cos3", 4),
          ("cos4", 5),
          ("cos5", 6),
          ("cos6", 7),
          ("cos7", 8),
          ("notApplicable", 255))
    )


_NsCommonConfigNetworkClassification802CoS_Type.__name__ = "Integer32"
_NsCommonConfigNetworkClassification802CoS_Object = MibTableColumn
nsCommonConfigNetworkClassification802CoS = _NsCommonConfigNetworkClassification802CoS_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 2, 1, 1, 2),
    _NsCommonConfigNetworkClassification802CoS_Type()
)
nsCommonConfigNetworkClassification802CoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassification802CoS.setStatus("current")
_NsCommonConfigNetworkClassificationTos_ObjectIdentity = ObjectIdentity
nsCommonConfigNetworkClassificationTos = _NsCommonConfigNetworkClassificationTos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 3)
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationTos.setStatus("current")
_NsCommonConfigNetworkClassificationTosTable_Object = MibTable
nsCommonConfigNetworkClassificationTosTable = _NsCommonConfigNetworkClassificationTosTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationTosTable.setStatus("current")
_NsCommonConfigNetworkClassificationTosEntry_Object = MibTableRow
nsCommonConfigNetworkClassificationTosEntry = _NsCommonConfigNetworkClassificationTosEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 3, 1, 1)
)
nsCommonConfigNetworkClassificationTosEntry.setIndexNames(
    (0, "NOVELSAT-COMMON-MIB", "nsCommonConfigNetworkClassificationTosPriority"),
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationTosEntry.setStatus("current")
_NsCommonConfigNetworkClassificationTosPriority_Type = Unsigned32
_NsCommonConfigNetworkClassificationTosPriority_Object = MibTableColumn
nsCommonConfigNetworkClassificationTosPriority = _NsCommonConfigNetworkClassificationTosPriority_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 3, 1, 1, 1),
    _NsCommonConfigNetworkClassificationTosPriority_Type()
)
nsCommonConfigNetworkClassificationTosPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationTosPriority.setStatus("current")
_NsCommonConfigNetworkClassificationTosFieldValue_Type = Unsigned32
_NsCommonConfigNetworkClassificationTosFieldValue_Object = MibTableColumn
nsCommonConfigNetworkClassificationTosFieldValue = _NsCommonConfigNetworkClassificationTosFieldValue_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 3, 1, 1, 2),
    _NsCommonConfigNetworkClassificationTosFieldValue_Type()
)
nsCommonConfigNetworkClassificationTosFieldValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationTosFieldValue.setStatus("current")
_NsCommonConfigNetworkClassificationTosFieldMask_Type = Unsigned32
_NsCommonConfigNetworkClassificationTosFieldMask_Object = MibTableColumn
nsCommonConfigNetworkClassificationTosFieldMask = _NsCommonConfigNetworkClassificationTosFieldMask_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 3, 1, 1, 3),
    _NsCommonConfigNetworkClassificationTosFieldMask_Type()
)
nsCommonConfigNetworkClassificationTosFieldMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationTosFieldMask.setStatus("current")


class _NsCommonConfigNetworkClassificationTosCoS_Type(Integer32):
    """Custom type nsCommonConfigNetworkClassificationTosCoS based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("cos0", 1),
          ("cos1", 2),
          ("cos2", 3),
          ("cos3", 4),
          ("cos4", 5),
          ("cos5", 6),
          ("cos6", 7),
          ("cos7", 8),
          ("notApplicable", 255))
    )


_NsCommonConfigNetworkClassificationTosCoS_Type.__name__ = "Integer32"
_NsCommonConfigNetworkClassificationTosCoS_Object = MibTableColumn
nsCommonConfigNetworkClassificationTosCoS = _NsCommonConfigNetworkClassificationTosCoS_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 3, 1, 1, 4),
    _NsCommonConfigNetworkClassificationTosCoS_Type()
)
nsCommonConfigNetworkClassificationTosCoS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationTosCoS.setStatus("current")
_NsCommonConfigNetworkClassificationTosNotifyRowStatus_Type = RowStatus
_NsCommonConfigNetworkClassificationTosNotifyRowStatus_Object = MibTableColumn
nsCommonConfigNetworkClassificationTosNotifyRowStatus = _NsCommonConfigNetworkClassificationTosNotifyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 3, 1, 1, 5),
    _NsCommonConfigNetworkClassificationTosNotifyRowStatus_Type()
)
nsCommonConfigNetworkClassificationTosNotifyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationTosNotifyRowStatus.setStatus("current")


class _NsCommonConfigNetworkClassificationTosColor_Type(Integer32):
    """Custom type nsCommonConfigNetworkClassificationTosColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("green", 0),
          ("notApplicable", 255),
          ("yellow", 1))
    )


_NsCommonConfigNetworkClassificationTosColor_Type.__name__ = "Integer32"
_NsCommonConfigNetworkClassificationTosColor_Object = MibTableColumn
nsCommonConfigNetworkClassificationTosColor = _NsCommonConfigNetworkClassificationTosColor_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 3, 1, 1, 6),
    _NsCommonConfigNetworkClassificationTosColor_Type()
)
nsCommonConfigNetworkClassificationTosColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationTosColor.setStatus("current")
_NsCommonConfigNetworkClassificationMf_ObjectIdentity = ObjectIdentity
nsCommonConfigNetworkClassificationMf = _NsCommonConfigNetworkClassificationMf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 4)
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationMf.setStatus("current")
_NsCommonConfigNetworkClassificationMfTable_Object = MibTable
nsCommonConfigNetworkClassificationMfTable = _NsCommonConfigNetworkClassificationMfTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 4, 1)
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationMfTable.setStatus("current")
_NsCommonConfigNetworkClassificationMfEntry_Object = MibTableRow
nsCommonConfigNetworkClassificationMfEntry = _NsCommonConfigNetworkClassificationMfEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 4, 1, 1)
)
nsCommonConfigNetworkClassificationMfEntry.setIndexNames(
    (0, "NOVELSAT-COMMON-MIB", "nsCommonConfigNetworkClassificationMfPriority"),
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationMfEntry.setStatus("current")
_NsCommonConfigNetworkClassificationMfPriority_Type = Unsigned32
_NsCommonConfigNetworkClassificationMfPriority_Object = MibTableColumn
nsCommonConfigNetworkClassificationMfPriority = _NsCommonConfigNetworkClassificationMfPriority_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 4, 1, 1, 1),
    _NsCommonConfigNetworkClassificationMfPriority_Type()
)
nsCommonConfigNetworkClassificationMfPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationMfPriority.setStatus("current")


class _NsCommonConfigNetworkClassificationMfName_Type(DisplayString):
    """Custom type nsCommonConfigNetworkClassificationMfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonConfigNetworkClassificationMfName_Type.__name__ = "DisplayString"
_NsCommonConfigNetworkClassificationMfName_Object = MibTableColumn
nsCommonConfigNetworkClassificationMfName = _NsCommonConfigNetworkClassificationMfName_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 4, 1, 1, 2),
    _NsCommonConfigNetworkClassificationMfName_Type()
)
nsCommonConfigNetworkClassificationMfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationMfName.setStatus("current")


class _NsCommonConfigNetworkClassificationMfAdminStatus_Type(Integer32):
    """Custom type nsCommonConfigNetworkClassificationMfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notApplicable", 255))
    )


_NsCommonConfigNetworkClassificationMfAdminStatus_Type.__name__ = "Integer32"
_NsCommonConfigNetworkClassificationMfAdminStatus_Object = MibTableColumn
nsCommonConfigNetworkClassificationMfAdminStatus = _NsCommonConfigNetworkClassificationMfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 4, 1, 1, 3),
    _NsCommonConfigNetworkClassificationMfAdminStatus_Type()
)
nsCommonConfigNetworkClassificationMfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationMfAdminStatus.setStatus("current")
_NsCommonConfigNetworkClassificationMfVidHigh_Type = Unsigned32
_NsCommonConfigNetworkClassificationMfVidHigh_Object = MibTableColumn
nsCommonConfigNetworkClassificationMfVidHigh = _NsCommonConfigNetworkClassificationMfVidHigh_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 4, 1, 1, 4),
    _NsCommonConfigNetworkClassificationMfVidHigh_Type()
)
nsCommonConfigNetworkClassificationMfVidHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationMfVidHigh.setStatus("current")
_NsCommonConfigNetworkClassificationMfVidLow_Type = Unsigned32
_NsCommonConfigNetworkClassificationMfVidLow_Object = MibTableColumn
nsCommonConfigNetworkClassificationMfVidLow = _NsCommonConfigNetworkClassificationMfVidLow_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 4, 1, 1, 5),
    _NsCommonConfigNetworkClassificationMfVidLow_Type()
)
nsCommonConfigNetworkClassificationMfVidLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationMfVidLow.setStatus("current")
_NsCommonConfigNetworkClassificationMfSrcIpAddressHigh_Type = IpAddress
_NsCommonConfigNetworkClassificationMfSrcIpAddressHigh_Object = MibTableColumn
nsCommonConfigNetworkClassificationMfSrcIpAddressHigh = _NsCommonConfigNetworkClassificationMfSrcIpAddressHigh_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 4, 1, 1, 6),
    _NsCommonConfigNetworkClassificationMfSrcIpAddressHigh_Type()
)
nsCommonConfigNetworkClassificationMfSrcIpAddressHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationMfSrcIpAddressHigh.setStatus("current")
_NsCommonConfigNetworkClassificationMfSrcIpAddressLow_Type = IpAddress
_NsCommonConfigNetworkClassificationMfSrcIpAddressLow_Object = MibTableColumn
nsCommonConfigNetworkClassificationMfSrcIpAddressLow = _NsCommonConfigNetworkClassificationMfSrcIpAddressLow_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 4, 1, 1, 7),
    _NsCommonConfigNetworkClassificationMfSrcIpAddressLow_Type()
)
nsCommonConfigNetworkClassificationMfSrcIpAddressLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationMfSrcIpAddressLow.setStatus("current")
_NsCommonConfigNetworkClassificationMfDestIpAddressHigh_Type = IpAddress
_NsCommonConfigNetworkClassificationMfDestIpAddressHigh_Object = MibTableColumn
nsCommonConfigNetworkClassificationMfDestIpAddressHigh = _NsCommonConfigNetworkClassificationMfDestIpAddressHigh_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 4, 1, 1, 8),
    _NsCommonConfigNetworkClassificationMfDestIpAddressHigh_Type()
)
nsCommonConfigNetworkClassificationMfDestIpAddressHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationMfDestIpAddressHigh.setStatus("current")
_NsCommonConfigNetworkClassificationMfDestIpAddressLow_Type = IpAddress
_NsCommonConfigNetworkClassificationMfDestIpAddressLow_Object = MibTableColumn
nsCommonConfigNetworkClassificationMfDestIpAddressLow = _NsCommonConfigNetworkClassificationMfDestIpAddressLow_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 4, 1, 1, 9),
    _NsCommonConfigNetworkClassificationMfDestIpAddressLow_Type()
)
nsCommonConfigNetworkClassificationMfDestIpAddressLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationMfDestIpAddressLow.setStatus("current")


class _NsCommonConfigNetworkClassificationMfProtocolStatus_Type(Integer32):
    """Custom type nsCommonConfigNetworkClassificationMfProtocolStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notApplicable", 255))
    )


_NsCommonConfigNetworkClassificationMfProtocolStatus_Type.__name__ = "Integer32"
_NsCommonConfigNetworkClassificationMfProtocolStatus_Object = MibTableColumn
nsCommonConfigNetworkClassificationMfProtocolStatus = _NsCommonConfigNetworkClassificationMfProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 4, 1, 1, 10),
    _NsCommonConfigNetworkClassificationMfProtocolStatus_Type()
)
nsCommonConfigNetworkClassificationMfProtocolStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationMfProtocolStatus.setStatus("current")
_NsCommonConfigNetworkClassificationMfProtocol_Type = Unsigned32
_NsCommonConfigNetworkClassificationMfProtocol_Object = MibTableColumn
nsCommonConfigNetworkClassificationMfProtocol = _NsCommonConfigNetworkClassificationMfProtocol_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 4, 1, 1, 11),
    _NsCommonConfigNetworkClassificationMfProtocol_Type()
)
nsCommonConfigNetworkClassificationMfProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationMfProtocol.setStatus("current")
_NsCommonConfigNetworkClassificationMfSrcPortHigh_Type = Unsigned32
_NsCommonConfigNetworkClassificationMfSrcPortHigh_Object = MibTableColumn
nsCommonConfigNetworkClassificationMfSrcPortHigh = _NsCommonConfigNetworkClassificationMfSrcPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 4, 1, 1, 12),
    _NsCommonConfigNetworkClassificationMfSrcPortHigh_Type()
)
nsCommonConfigNetworkClassificationMfSrcPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationMfSrcPortHigh.setStatus("current")
_NsCommonConfigNetworkClassificationMfSrcPortLow_Type = Unsigned32
_NsCommonConfigNetworkClassificationMfSrcPortLow_Object = MibTableColumn
nsCommonConfigNetworkClassificationMfSrcPortLow = _NsCommonConfigNetworkClassificationMfSrcPortLow_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 4, 1, 1, 13),
    _NsCommonConfigNetworkClassificationMfSrcPortLow_Type()
)
nsCommonConfigNetworkClassificationMfSrcPortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationMfSrcPortLow.setStatus("current")
_NsCommonConfigNetworkClassificationMfDestPortHigh_Type = Unsigned32
_NsCommonConfigNetworkClassificationMfDestPortHigh_Object = MibTableColumn
nsCommonConfigNetworkClassificationMfDestPortHigh = _NsCommonConfigNetworkClassificationMfDestPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 4, 1, 1, 14),
    _NsCommonConfigNetworkClassificationMfDestPortHigh_Type()
)
nsCommonConfigNetworkClassificationMfDestPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationMfDestPortHigh.setStatus("current")
_NsCommonConfigNetworkClassificationMfDestPortLow_Type = Unsigned32
_NsCommonConfigNetworkClassificationMfDestPortLow_Object = MibTableColumn
nsCommonConfigNetworkClassificationMfDestPortLow = _NsCommonConfigNetworkClassificationMfDestPortLow_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 4, 1, 1, 15),
    _NsCommonConfigNetworkClassificationMfDestPortLow_Type()
)
nsCommonConfigNetworkClassificationMfDestPortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationMfDestPortLow.setStatus("current")


class _NsCommonConfigNetworkClassificationMfCoS_Type(Integer32):
    """Custom type nsCommonConfigNetworkClassificationMfCoS based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("cos0", 1),
          ("cos1", 2),
          ("cos2", 3),
          ("cos3", 4),
          ("cos4", 5),
          ("cos5", 6),
          ("cos6", 7),
          ("cos7", 8),
          ("notApplicable", 255))
    )


_NsCommonConfigNetworkClassificationMfCoS_Type.__name__ = "Integer32"
_NsCommonConfigNetworkClassificationMfCoS_Object = MibTableColumn
nsCommonConfigNetworkClassificationMfCoS = _NsCommonConfigNetworkClassificationMfCoS_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 4, 1, 1, 16),
    _NsCommonConfigNetworkClassificationMfCoS_Type()
)
nsCommonConfigNetworkClassificationMfCoS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationMfCoS.setStatus("current")
_NsCommonConfigNetworkClassificationMfNotifyRowStatus_Type = RowStatus
_NsCommonConfigNetworkClassificationMfNotifyRowStatus_Object = MibTableColumn
nsCommonConfigNetworkClassificationMfNotifyRowStatus = _NsCommonConfigNetworkClassificationMfNotifyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 1, 4, 1, 1, 17),
    _NsCommonConfigNetworkClassificationMfNotifyRowStatus_Type()
)
nsCommonConfigNetworkClassificationMfNotifyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkClassificationMfNotifyRowStatus.setStatus("current")
_NsCommonConfigNetworkQueues_ObjectIdentity = ObjectIdentity
nsCommonConfigNetworkQueues = _NsCommonConfigNetworkQueues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 2)
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkQueues.setStatus("current")
_NsCommonConfigNetworkQueuesTable_Object = MibTable
nsCommonConfigNetworkQueuesTable = _NsCommonConfigNetworkQueuesTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 2, 1)
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkQueuesTable.setStatus("current")
_NsCommonConfigNetworkQueuesEntry_Object = MibTableRow
nsCommonConfigNetworkQueuesEntry = _NsCommonConfigNetworkQueuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 2, 1, 1)
)
nsCommonConfigNetworkQueuesEntry.setIndexNames(
    (0, "NOVELSAT-COMMON-MIB", "nsCommonConfigNetworkQueuesCos"),
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkQueuesEntry.setStatus("current")
_NsCommonConfigNetworkQueuesCos_Type = Unsigned32
_NsCommonConfigNetworkQueuesCos_Object = MibTableColumn
nsCommonConfigNetworkQueuesCos = _NsCommonConfigNetworkQueuesCos_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 2, 1, 1, 1),
    _NsCommonConfigNetworkQueuesCos_Type()
)
nsCommonConfigNetworkQueuesCos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkQueuesCos.setStatus("current")


class _NsCommonConfigNetworkQueuesSchedulingMethod_Type(Integer32):
    """Custom type nsCommonConfigNetworkQueuesSchedulingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("drr", 1),
          ("notApplicable", 255),
          ("strictPriority", 0))
    )


_NsCommonConfigNetworkQueuesSchedulingMethod_Type.__name__ = "Integer32"
_NsCommonConfigNetworkQueuesSchedulingMethod_Object = MibTableColumn
nsCommonConfigNetworkQueuesSchedulingMethod = _NsCommonConfigNetworkQueuesSchedulingMethod_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 2, 1, 1, 2),
    _NsCommonConfigNetworkQueuesSchedulingMethod_Type()
)
nsCommonConfigNetworkQueuesSchedulingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkQueuesSchedulingMethod.setStatus("current")
_NsCommonConfigNetworkQueuesWeight_Type = Unsigned32
_NsCommonConfigNetworkQueuesWeight_Object = MibTableColumn
nsCommonConfigNetworkQueuesWeight = _NsCommonConfigNetworkQueuesWeight_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 2, 1, 1, 3),
    _NsCommonConfigNetworkQueuesWeight_Type()
)
nsCommonConfigNetworkQueuesWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkQueuesWeight.setStatus("current")
_NsCommonConfigNetworkQueuesQueueDepth_Type = Unsigned32
_NsCommonConfigNetworkQueuesQueueDepth_Object = MibTableColumn
nsCommonConfigNetworkQueuesQueueDepth = _NsCommonConfigNetworkQueuesQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 2, 1, 1, 4),
    _NsCommonConfigNetworkQueuesQueueDepth_Type()
)
nsCommonConfigNetworkQueuesQueueDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkQueuesQueueDepth.setStatus("current")


class _NsCommonConfigNetworkQueuesDropDiscipline_Type(Integer32):
    """Custom type nsCommonConfigNetworkQueuesDropDiscipline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 255),
          ("tailDrop", 0),
          ("wred", 1))
    )


_NsCommonConfigNetworkQueuesDropDiscipline_Type.__name__ = "Integer32"
_NsCommonConfigNetworkQueuesDropDiscipline_Object = MibTableColumn
nsCommonConfigNetworkQueuesDropDiscipline = _NsCommonConfigNetworkQueuesDropDiscipline_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 2, 1, 1, 5),
    _NsCommonConfigNetworkQueuesDropDiscipline_Type()
)
nsCommonConfigNetworkQueuesDropDiscipline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkQueuesDropDiscipline.setStatus("current")
_NsCommonConfigNetworkRemoteScheduling_ObjectIdentity = ObjectIdentity
nsCommonConfigNetworkRemoteScheduling = _NsCommonConfigNetworkRemoteScheduling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 3)
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkRemoteScheduling.setStatus("current")


class _NsCommonConfigNetworkRemoteSchedulingMethod_Type(Integer32):
    """Custom type nsCommonConfigNetworkRemoteSchedulingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("drr", 1),
          ("notApplicable", 255),
          ("proprietry", 0),
          ("wrr", 2))
    )


_NsCommonConfigNetworkRemoteSchedulingMethod_Type.__name__ = "Integer32"
_NsCommonConfigNetworkRemoteSchedulingMethod_Object = MibScalar
nsCommonConfigNetworkRemoteSchedulingMethod = _NsCommonConfigNetworkRemoteSchedulingMethod_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 3, 1),
    _NsCommonConfigNetworkRemoteSchedulingMethod_Type()
)
nsCommonConfigNetworkRemoteSchedulingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkRemoteSchedulingMethod.setStatus("current")


class _NsCommonConfigNetworkRemoteSchedulingFrameMerging_Type(Integer32):
    """Custom type nsCommonConfigNetworkRemoteSchedulingFrameMerging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notApplicable", 255))
    )


_NsCommonConfigNetworkRemoteSchedulingFrameMerging_Type.__name__ = "Integer32"
_NsCommonConfigNetworkRemoteSchedulingFrameMerging_Object = MibScalar
nsCommonConfigNetworkRemoteSchedulingFrameMerging = _NsCommonConfigNetworkRemoteSchedulingFrameMerging_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 3, 2),
    _NsCommonConfigNetworkRemoteSchedulingFrameMerging_Type()
)
nsCommonConfigNetworkRemoteSchedulingFrameMerging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkRemoteSchedulingFrameMerging.setStatus("current")


class _NsCommonConfigNetworkRemoteSchedulingCosSignificance_Type(Integer32):
    """Custom type nsCommonConfigNetworkRemoteSchedulingCosSignificance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("global", 0),
          ("notApplicable", 255),
          ("perRemote", 1))
    )


_NsCommonConfigNetworkRemoteSchedulingCosSignificance_Type.__name__ = "Integer32"
_NsCommonConfigNetworkRemoteSchedulingCosSignificance_Object = MibScalar
nsCommonConfigNetworkRemoteSchedulingCosSignificance = _NsCommonConfigNetworkRemoteSchedulingCosSignificance_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 3, 3),
    _NsCommonConfigNetworkRemoteSchedulingCosSignificance_Type()
)
nsCommonConfigNetworkRemoteSchedulingCosSignificance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkRemoteSchedulingCosSignificance.setStatus("current")
_NsCommonConfigNetworkBwManagement_ObjectIdentity = ObjectIdentity
nsCommonConfigNetworkBwManagement = _NsCommonConfigNetworkBwManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 4)
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkBwManagement.setStatus("current")
_NsCommonConfigNetworkBwManagementTable_Object = MibTable
nsCommonConfigNetworkBwManagementTable = _NsCommonConfigNetworkBwManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 4, 1)
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkBwManagementTable.setStatus("current")
_NsCommonConfigNetworkBwManagementEntry_Object = MibTableRow
nsCommonConfigNetworkBwManagementEntry = _NsCommonConfigNetworkBwManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 4, 1, 1)
)
nsCommonConfigNetworkBwManagementEntry.setIndexNames(
    (0, "NOVELSAT-COMMON-MIB", "nsCommonConfigNetworkBwManagementIndex"),
)
if mibBuilder.loadTexts:
    nsCommonConfigNetworkBwManagementEntry.setStatus("current")
_NsCommonConfigNetworkBwManagementIndex_Type = Unsigned32
_NsCommonConfigNetworkBwManagementIndex_Object = MibTableColumn
nsCommonConfigNetworkBwManagementIndex = _NsCommonConfigNetworkBwManagementIndex_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 4, 1, 1, 1),
    _NsCommonConfigNetworkBwManagementIndex_Type()
)
nsCommonConfigNetworkBwManagementIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkBwManagementIndex.setStatus("current")
_NsCommonConfigNetworkBwManagementNeighborIndex_Type = Unsigned32
_NsCommonConfigNetworkBwManagementNeighborIndex_Object = MibTableColumn
nsCommonConfigNetworkBwManagementNeighborIndex = _NsCommonConfigNetworkBwManagementNeighborIndex_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 4, 1, 1, 2),
    _NsCommonConfigNetworkBwManagementNeighborIndex_Type()
)
nsCommonConfigNetworkBwManagementNeighborIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkBwManagementNeighborIndex.setStatus("current")


class _NsCommonConfigNetworkBwManagementAdminStatus_Type(Integer32):
    """Custom type nsCommonConfigNetworkBwManagementAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notApplicable", 255))
    )


_NsCommonConfigNetworkBwManagementAdminStatus_Type.__name__ = "Integer32"
_NsCommonConfigNetworkBwManagementAdminStatus_Object = MibTableColumn
nsCommonConfigNetworkBwManagementAdminStatus = _NsCommonConfigNetworkBwManagementAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 4, 1, 1, 3),
    _NsCommonConfigNetworkBwManagementAdminStatus_Type()
)
nsCommonConfigNetworkBwManagementAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkBwManagementAdminStatus.setStatus("current")
_NsCommonConfigNetworkBwManagementCIR_Type = Unsigned32
_NsCommonConfigNetworkBwManagementCIR_Object = MibTableColumn
nsCommonConfigNetworkBwManagementCIR = _NsCommonConfigNetworkBwManagementCIR_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 4, 1, 1, 4),
    _NsCommonConfigNetworkBwManagementCIR_Type()
)
nsCommonConfigNetworkBwManagementCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkBwManagementCIR.setStatus("current")
_NsCommonConfigNetworkBwManagementCBS_Type = Unsigned32
_NsCommonConfigNetworkBwManagementCBS_Object = MibTableColumn
nsCommonConfigNetworkBwManagementCBS = _NsCommonConfigNetworkBwManagementCBS_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 4, 1, 1, 5),
    _NsCommonConfigNetworkBwManagementCBS_Type()
)
nsCommonConfigNetworkBwManagementCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkBwManagementCBS.setStatus("current")
_NsCommonConfigNetworkBwManagementEIR_Type = Unsigned32
_NsCommonConfigNetworkBwManagementEIR_Object = MibTableColumn
nsCommonConfigNetworkBwManagementEIR = _NsCommonConfigNetworkBwManagementEIR_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 4, 1, 1, 6),
    _NsCommonConfigNetworkBwManagementEIR_Type()
)
nsCommonConfigNetworkBwManagementEIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkBwManagementEIR.setStatus("current")
_NsCommonConfigNetworkBwManagementEBS_Type = Unsigned32
_NsCommonConfigNetworkBwManagementEBS_Object = MibTableColumn
nsCommonConfigNetworkBwManagementEBS = _NsCommonConfigNetworkBwManagementEBS_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 4, 1, 1, 7),
    _NsCommonConfigNetworkBwManagementEBS_Type()
)
nsCommonConfigNetworkBwManagementEBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkBwManagementEBS.setStatus("current")


class _NsCommonConfigNetworkBwManagementRefModulation_Type(Integer32):
    """Custom type nsCommonConfigNetworkBwManagementRefModulation based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("modulation16Apsk", 4),
          ("modulation16Qam", 3),
          ("modulation32Apsk", 5),
          ("modulation64Apsk", 6),
          ("modulation8Psk", 2),
          ("modulationBpsk", 0),
          ("modulationQpsk", 1),
          ("notApplicable", 255))
    )


_NsCommonConfigNetworkBwManagementRefModulation_Type.__name__ = "Integer32"
_NsCommonConfigNetworkBwManagementRefModulation_Object = MibTableColumn
nsCommonConfigNetworkBwManagementRefModulation = _NsCommonConfigNetworkBwManagementRefModulation_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 4, 1, 1, 8),
    _NsCommonConfigNetworkBwManagementRefModulation_Type()
)
nsCommonConfigNetworkBwManagementRefModulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkBwManagementRefModulation.setStatus("current")


class _NsCommonConfigNetworkBwManagementRefFecRate_Type(Integer32):
    """Custom type nsCommonConfigNetworkBwManagementRefFecRate based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("fec11Div15", 17),
          ("fec13Div30", 4),
          ("fec17Div30", 11),
          ("fec19Div30", 14),
          ("fec1Div2", 8),
          ("fec1Div3", 2),
          ("fec1Div4", 1),
          ("fec1Div5", 0),
          ("fec22Div45", 7),
          ("fec28Div45", 13),
          ("fec2Div3", 15),
          ("fec2Div5", 3),
          ("fec32Div45", 16),
          ("fec37Div45", 21),
          ("fec3Div4", 18),
          ("fec3Div5", 12),
          ("fec4Div5", 20),
          ("fec4Div9", 5),
          ("fec5Div6", 22),
          ("fec5Div9", 10),
          ("fec7Div15", 6),
          ("fec7Div8", 23),
          ("fec7Div9", 19),
          ("fec8Div15", 9),
          ("fec8Div9", 24),
          ("fec9Div10", 25),
          ("notApplicable", 255))
    )


_NsCommonConfigNetworkBwManagementRefFecRate_Type.__name__ = "Integer32"
_NsCommonConfigNetworkBwManagementRefFecRate_Object = MibTableColumn
nsCommonConfigNetworkBwManagementRefFecRate = _NsCommonConfigNetworkBwManagementRefFecRate_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 4, 1, 1, 9),
    _NsCommonConfigNetworkBwManagementRefFecRate_Type()
)
nsCommonConfigNetworkBwManagementRefFecRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkBwManagementRefFecRate.setStatus("current")
_NsCommonConfigNetworkBwManagementPercentage_Type = Unsigned32
_NsCommonConfigNetworkBwManagementPercentage_Object = MibTableColumn
nsCommonConfigNetworkBwManagementPercentage = _NsCommonConfigNetworkBwManagementPercentage_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 4, 1, 1, 10),
    _NsCommonConfigNetworkBwManagementPercentage_Type()
)
nsCommonConfigNetworkBwManagementPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkBwManagementPercentage.setStatus("current")
_NsCommonConfigNetworkBwManagementNotifyRowStatus_Type = RowStatus
_NsCommonConfigNetworkBwManagementNotifyRowStatus_Object = MibTableColumn
nsCommonConfigNetworkBwManagementNotifyRowStatus = _NsCommonConfigNetworkBwManagementNotifyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 7, 6, 4, 1, 1, 11),
    _NsCommonConfigNetworkBwManagementNotifyRowStatus_Type()
)
nsCommonConfigNetworkBwManagementNotifyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigNetworkBwManagementNotifyRowStatus.setStatus("current")
_NsCommonConfigManagementOta_ObjectIdentity = ObjectIdentity
nsCommonConfigManagementOta = _NsCommonConfigManagementOta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 8)
)
if mibBuilder.loadTexts:
    nsCommonConfigManagementOta.setStatus("current")
_NsCommonConfigMgmtOtaIP_Type = IpAddress
_NsCommonConfigMgmtOtaIP_Object = MibScalar
nsCommonConfigMgmtOtaIP = _NsCommonConfigMgmtOtaIP_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 8, 1),
    _NsCommonConfigMgmtOtaIP_Type()
)
nsCommonConfigMgmtOtaIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfigMgmtOtaIP.setStatus("current")
_NsCommonConfigMgmtOtaMask_Type = IpAddress
_NsCommonConfigMgmtOtaMask_Object = MibScalar
nsCommonConfigMgmtOtaMask = _NsCommonConfigMgmtOtaMask_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 8, 2),
    _NsCommonConfigMgmtOtaMask_Type()
)
nsCommonConfigMgmtOtaMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfigMgmtOtaMask.setStatus("current")
_NsCommonConfigManagementRollback_ObjectIdentity = ObjectIdentity
nsCommonConfigManagementRollback = _NsCommonConfigManagementRollback_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 9)
)
if mibBuilder.loadTexts:
    nsCommonConfigManagementRollback.setStatus("current")


class _NsCommonConfigMgmtRollbackMode_Type(Integer32):
    """Custom type nsCommonConfigMgmtRollbackMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NsCommonConfigMgmtRollbackMode_Type.__name__ = "Integer32"
_NsCommonConfigMgmtRollbackMode_Object = MibScalar
nsCommonConfigMgmtRollbackMode = _NsCommonConfigMgmtRollbackMode_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 9, 1),
    _NsCommonConfigMgmtRollbackMode_Type()
)
nsCommonConfigMgmtRollbackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfigMgmtRollbackMode.setStatus("current")
_NsCommonConfigMgmtRollbackTimeout_Type = Unsigned32
_NsCommonConfigMgmtRollbackTimeout_Object = MibScalar
nsCommonConfigMgmtRollbackTimeout = _NsCommonConfigMgmtRollbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 9, 2),
    _NsCommonConfigMgmtRollbackTimeout_Type()
)
nsCommonConfigMgmtRollbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfigMgmtRollbackTimeout.setStatus("current")
_NsCommonConfigManagementRateLimiter_ObjectIdentity = ObjectIdentity
nsCommonConfigManagementRateLimiter = _NsCommonConfigManagementRateLimiter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 10)
)
if mibBuilder.loadTexts:
    nsCommonConfigManagementRateLimiter.setStatus("current")
_NsCommonConfigMgmtRateLimit_Type = Unsigned32
_NsCommonConfigMgmtRateLimit_Object = MibScalar
nsCommonConfigMgmtRateLimit = _NsCommonConfigMgmtRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 10, 1),
    _NsCommonConfigMgmtRateLimit_Type()
)
nsCommonConfigMgmtRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonConfigMgmtRateLimit.setStatus("current")
_NsCommonConfigAlarmsEvents_ObjectIdentity = ObjectIdentity
nsCommonConfigAlarmsEvents = _NsCommonConfigAlarmsEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 11)
)
if mibBuilder.loadTexts:
    nsCommonConfigAlarmsEvents.setStatus("current")
_NsCommonConfigAlarmsEventsTable_Object = MibTable
nsCommonConfigAlarmsEventsTable = _NsCommonConfigAlarmsEventsTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 11, 1)
)
if mibBuilder.loadTexts:
    nsCommonConfigAlarmsEventsTable.setStatus("current")
_NsCommonConfigAlarmsEventsEntry_Object = MibTableRow
nsCommonConfigAlarmsEventsEntry = _NsCommonConfigAlarmsEventsEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 11, 1, 1)
)
nsCommonConfigAlarmsEventsEntry.setIndexNames(
    (0, "NOVELSAT-COMMON-MIB", "nsCommonConfigAlarmsEventsIndex"),
)
if mibBuilder.loadTexts:
    nsCommonConfigAlarmsEventsEntry.setStatus("current")
_NsCommonConfigAlarmsEventsIndex_Type = Unsigned32
_NsCommonConfigAlarmsEventsIndex_Object = MibTableColumn
nsCommonConfigAlarmsEventsIndex = _NsCommonConfigAlarmsEventsIndex_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 11, 1, 1, 1),
    _NsCommonConfigAlarmsEventsIndex_Type()
)
nsCommonConfigAlarmsEventsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonConfigAlarmsEventsIndex.setStatus("current")


class _NsCommonConfigAlarmsEventsName_Type(DisplayString):
    """Custom type nsCommonConfigAlarmsEventsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonConfigAlarmsEventsName_Type.__name__ = "DisplayString"
_NsCommonConfigAlarmsEventsName_Object = MibTableColumn
nsCommonConfigAlarmsEventsName = _NsCommonConfigAlarmsEventsName_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 11, 1, 1, 2),
    _NsCommonConfigAlarmsEventsName_Type()
)
nsCommonConfigAlarmsEventsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonConfigAlarmsEventsName.setStatus("current")


class _NsCommonConfigAlarmsEventsMask_Type(Integer32):
    """Custom type nsCommonConfigAlarmsEventsMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notApplicable", 255))
    )


_NsCommonConfigAlarmsEventsMask_Type.__name__ = "Integer32"
_NsCommonConfigAlarmsEventsMask_Object = MibTableColumn
nsCommonConfigAlarmsEventsMask = _NsCommonConfigAlarmsEventsMask_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 11, 1, 1, 3),
    _NsCommonConfigAlarmsEventsMask_Type()
)
nsCommonConfigAlarmsEventsMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigAlarmsEventsMask.setStatus("current")


class _NsCommonConfigAlarmsEventsRelayMask_Type(Integer32):
    """Custom type nsCommonConfigAlarmsEventsRelayMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notApplicable", 255))
    )


_NsCommonConfigAlarmsEventsRelayMask_Type.__name__ = "Integer32"
_NsCommonConfigAlarmsEventsRelayMask_Object = MibTableColumn
nsCommonConfigAlarmsEventsRelayMask = _NsCommonConfigAlarmsEventsRelayMask_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 1, 11, 1, 1, 4),
    _NsCommonConfigAlarmsEventsRelayMask_Type()
)
nsCommonConfigAlarmsEventsRelayMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsCommonConfigAlarmsEventsRelayMask.setStatus("current")
_NsCommonMonitor_ObjectIdentity = ObjectIdentity
nsCommonMonitor = _NsCommonMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2)
)
if mibBuilder.loadTexts:
    nsCommonMonitor.setStatus("current")
_NsCommonMonitorNotifications_ObjectIdentity = ObjectIdentity
nsCommonMonitorNotifications = _NsCommonMonitorNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 0)
)
if mibBuilder.loadTexts:
    nsCommonMonitorNotifications.setStatus("current")
_NsCommonMonitorAlarms_ObjectIdentity = ObjectIdentity
nsCommonMonitorAlarms = _NsCommonMonitorAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nsCommonMonitorAlarms.setStatus("current")
_NsCommonMonitorAlarmsTable_Object = MibTable
nsCommonMonitorAlarmsTable = _NsCommonMonitorAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nsCommonMonitorAlarmsTable.setStatus("current")
_NsCommonMonitorAlarmsEntry_Object = MibTableRow
nsCommonMonitorAlarmsEntry = _NsCommonMonitorAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 1, 1, 1)
)
nsCommonMonitorAlarmsEntry.setIndexNames(
    (0, "NOVELSAT-COMMON-MIB", "nsCommonMonitorAlarmsUtcSecondsHigh"),
    (0, "NOVELSAT-COMMON-MIB", "nsCommonMonitorAlarmsUtcSecondsLow"),
    (0, "NOVELSAT-COMMON-MIB", "nsCommonMonitorAlarmsUtcNanoSecondsHigh"),
    (0, "NOVELSAT-COMMON-MIB", "nsCommonMonitorAlarmsUtcNanoSecondsLow"),
)
if mibBuilder.loadTexts:
    nsCommonMonitorAlarmsEntry.setStatus("current")
_NsCommonMonitorAlarmsUtcSecondsHigh_Type = Counter32
_NsCommonMonitorAlarmsUtcSecondsHigh_Object = MibTableColumn
nsCommonMonitorAlarmsUtcSecondsHigh = _NsCommonMonitorAlarmsUtcSecondsHigh_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 1, 1, 1, 1),
    _NsCommonMonitorAlarmsUtcSecondsHigh_Type()
)
nsCommonMonitorAlarmsUtcSecondsHigh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonMonitorAlarmsUtcSecondsHigh.setStatus("current")
_NsCommonMonitorAlarmsUtcSecondsLow_Type = Counter32
_NsCommonMonitorAlarmsUtcSecondsLow_Object = MibTableColumn
nsCommonMonitorAlarmsUtcSecondsLow = _NsCommonMonitorAlarmsUtcSecondsLow_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 1, 1, 1, 2),
    _NsCommonMonitorAlarmsUtcSecondsLow_Type()
)
nsCommonMonitorAlarmsUtcSecondsLow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonMonitorAlarmsUtcSecondsLow.setStatus("current")
_NsCommonMonitorAlarmsUtcNanoSecondsHigh_Type = Counter32
_NsCommonMonitorAlarmsUtcNanoSecondsHigh_Object = MibTableColumn
nsCommonMonitorAlarmsUtcNanoSecondsHigh = _NsCommonMonitorAlarmsUtcNanoSecondsHigh_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 1, 1, 1, 3),
    _NsCommonMonitorAlarmsUtcNanoSecondsHigh_Type()
)
nsCommonMonitorAlarmsUtcNanoSecondsHigh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonMonitorAlarmsUtcNanoSecondsHigh.setStatus("current")
_NsCommonMonitorAlarmsUtcNanoSecondsLow_Type = Counter32
_NsCommonMonitorAlarmsUtcNanoSecondsLow_Object = MibTableColumn
nsCommonMonitorAlarmsUtcNanoSecondsLow = _NsCommonMonitorAlarmsUtcNanoSecondsLow_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 1, 1, 1, 4),
    _NsCommonMonitorAlarmsUtcNanoSecondsLow_Type()
)
nsCommonMonitorAlarmsUtcNanoSecondsLow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonMonitorAlarmsUtcNanoSecondsLow.setStatus("current")
_NsCommonMonitorAlarmsDateAndTime_Type = DateAndTime
_NsCommonMonitorAlarmsDateAndTime_Object = MibTableColumn
nsCommonMonitorAlarmsDateAndTime = _NsCommonMonitorAlarmsDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 1, 1, 1, 5),
    _NsCommonMonitorAlarmsDateAndTime_Type()
)
nsCommonMonitorAlarmsDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorAlarmsDateAndTime.setStatus("current")
_NsCommonMonitorAlarmsSeverity_Type = ItuPerceivedSeverity
_NsCommonMonitorAlarmsSeverity_Object = MibTableColumn
nsCommonMonitorAlarmsSeverity = _NsCommonMonitorAlarmsSeverity_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 1, 1, 1, 6),
    _NsCommonMonitorAlarmsSeverity_Type()
)
nsCommonMonitorAlarmsSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorAlarmsSeverity.setStatus("current")


class _NsCommonMonitorAlarmsSource_Type(DisplayString):
    """Custom type nsCommonMonitorAlarmsSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonMonitorAlarmsSource_Type.__name__ = "DisplayString"
_NsCommonMonitorAlarmsSource_Object = MibTableColumn
nsCommonMonitorAlarmsSource = _NsCommonMonitorAlarmsSource_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 1, 1, 1, 7),
    _NsCommonMonitorAlarmsSource_Type()
)
nsCommonMonitorAlarmsSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorAlarmsSource.setStatus("current")


class _NsCommonMonitorAlarmsEvent_Type(DisplayString):
    """Custom type nsCommonMonitorAlarmsEvent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonMonitorAlarmsEvent_Type.__name__ = "DisplayString"
_NsCommonMonitorAlarmsEvent_Object = MibTableColumn
nsCommonMonitorAlarmsEvent = _NsCommonMonitorAlarmsEvent_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 1, 1, 1, 8),
    _NsCommonMonitorAlarmsEvent_Type()
)
nsCommonMonitorAlarmsEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorAlarmsEvent.setStatus("current")


class _NsCommonMonitorAlarmsDescription_Type(DisplayString):
    """Custom type nsCommonMonitorAlarmsDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonMonitorAlarmsDescription_Type.__name__ = "DisplayString"
_NsCommonMonitorAlarmsDescription_Object = MibTableColumn
nsCommonMonitorAlarmsDescription = _NsCommonMonitorAlarmsDescription_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 1, 1, 1, 9),
    _NsCommonMonitorAlarmsDescription_Type()
)
nsCommonMonitorAlarmsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorAlarmsDescription.setStatus("current")
_NsCommonMonitorEvents_ObjectIdentity = ObjectIdentity
nsCommonMonitorEvents = _NsCommonMonitorEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 2)
)
if mibBuilder.loadTexts:
    nsCommonMonitorEvents.setStatus("current")
_NsCommonMonitorEventsTable_Object = MibTable
nsCommonMonitorEventsTable = _NsCommonMonitorEventsTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nsCommonMonitorEventsTable.setStatus("current")
_NsCommonMonitorEventsEntry_Object = MibTableRow
nsCommonMonitorEventsEntry = _NsCommonMonitorEventsEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 2, 1, 1)
)
nsCommonMonitorEventsEntry.setIndexNames(
    (0, "NOVELSAT-COMMON-MIB", "nsCommonMonitorEventsUtcSecondsHigh"),
    (0, "NOVELSAT-COMMON-MIB", "nsCommonMonitorEventsUtcSecondsLow"),
    (0, "NOVELSAT-COMMON-MIB", "nsCommonMonitorEventsUtcNanoSecondsHigh"),
    (0, "NOVELSAT-COMMON-MIB", "nsCommonMonitorEventsUtcNanoSecondsLow"),
)
if mibBuilder.loadTexts:
    nsCommonMonitorEventsEntry.setStatus("current")
_NsCommonMonitorEventsUtcSecondsHigh_Type = Counter32
_NsCommonMonitorEventsUtcSecondsHigh_Object = MibTableColumn
nsCommonMonitorEventsUtcSecondsHigh = _NsCommonMonitorEventsUtcSecondsHigh_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 2, 1, 1, 1),
    _NsCommonMonitorEventsUtcSecondsHigh_Type()
)
nsCommonMonitorEventsUtcSecondsHigh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonMonitorEventsUtcSecondsHigh.setStatus("current")
_NsCommonMonitorEventsUtcSecondsLow_Type = Counter32
_NsCommonMonitorEventsUtcSecondsLow_Object = MibTableColumn
nsCommonMonitorEventsUtcSecondsLow = _NsCommonMonitorEventsUtcSecondsLow_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 2, 1, 1, 2),
    _NsCommonMonitorEventsUtcSecondsLow_Type()
)
nsCommonMonitorEventsUtcSecondsLow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonMonitorEventsUtcSecondsLow.setStatus("current")
_NsCommonMonitorEventsUtcNanoSecondsHigh_Type = Counter32
_NsCommonMonitorEventsUtcNanoSecondsHigh_Object = MibTableColumn
nsCommonMonitorEventsUtcNanoSecondsHigh = _NsCommonMonitorEventsUtcNanoSecondsHigh_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 2, 1, 1, 3),
    _NsCommonMonitorEventsUtcNanoSecondsHigh_Type()
)
nsCommonMonitorEventsUtcNanoSecondsHigh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonMonitorEventsUtcNanoSecondsHigh.setStatus("current")
_NsCommonMonitorEventsUtcNanoSecondsLow_Type = Counter32
_NsCommonMonitorEventsUtcNanoSecondsLow_Object = MibTableColumn
nsCommonMonitorEventsUtcNanoSecondsLow = _NsCommonMonitorEventsUtcNanoSecondsLow_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 2, 1, 1, 4),
    _NsCommonMonitorEventsUtcNanoSecondsLow_Type()
)
nsCommonMonitorEventsUtcNanoSecondsLow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonMonitorEventsUtcNanoSecondsLow.setStatus("current")
_NsCommonMonitorEventsDateAndTime_Type = DateAndTime
_NsCommonMonitorEventsDateAndTime_Object = MibTableColumn
nsCommonMonitorEventsDateAndTime = _NsCommonMonitorEventsDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 2, 1, 1, 5),
    _NsCommonMonitorEventsDateAndTime_Type()
)
nsCommonMonitorEventsDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorEventsDateAndTime.setStatus("current")


class _NsCommonMonitorEventsType_Type(Integer32):
    """Custom type nsCommonMonitorEventsType based on Integer32"""
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
        *(("alarmOff", 3),
          ("alarmOn", 2),
          ("info", 1),
          ("none", 0))
    )


_NsCommonMonitorEventsType_Type.__name__ = "Integer32"
_NsCommonMonitorEventsType_Object = MibTableColumn
nsCommonMonitorEventsType = _NsCommonMonitorEventsType_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 2, 1, 1, 6),
    _NsCommonMonitorEventsType_Type()
)
nsCommonMonitorEventsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorEventsType.setStatus("current")
_NsCommonMonitorEventsSeverity_Type = ItuPerceivedSeverity
_NsCommonMonitorEventsSeverity_Object = MibTableColumn
nsCommonMonitorEventsSeverity = _NsCommonMonitorEventsSeverity_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 2, 1, 1, 7),
    _NsCommonMonitorEventsSeverity_Type()
)
nsCommonMonitorEventsSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorEventsSeverity.setStatus("current")


class _NsCommonMonitorEventsSource_Type(DisplayString):
    """Custom type nsCommonMonitorEventsSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonMonitorEventsSource_Type.__name__ = "DisplayString"
_NsCommonMonitorEventsSource_Object = MibTableColumn
nsCommonMonitorEventsSource = _NsCommonMonitorEventsSource_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 2, 1, 1, 8),
    _NsCommonMonitorEventsSource_Type()
)
nsCommonMonitorEventsSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorEventsSource.setStatus("current")


class _NsCommonMonitorEventsEvent_Type(DisplayString):
    """Custom type nsCommonMonitorEventsEvent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonMonitorEventsEvent_Type.__name__ = "DisplayString"
_NsCommonMonitorEventsEvent_Object = MibTableColumn
nsCommonMonitorEventsEvent = _NsCommonMonitorEventsEvent_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 2, 1, 1, 9),
    _NsCommonMonitorEventsEvent_Type()
)
nsCommonMonitorEventsEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorEventsEvent.setStatus("current")


class _NsCommonMonitorEventsDescription_Type(DisplayString):
    """Custom type nsCommonMonitorEventsDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonMonitorEventsDescription_Type.__name__ = "DisplayString"
_NsCommonMonitorEventsDescription_Object = MibTableColumn
nsCommonMonitorEventsDescription = _NsCommonMonitorEventsDescription_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 2, 1, 1, 10),
    _NsCommonMonitorEventsDescription_Type()
)
nsCommonMonitorEventsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorEventsDescription.setStatus("current")
_NsCommonMonitorVoltage_ObjectIdentity = ObjectIdentity
nsCommonMonitorVoltage = _NsCommonMonitorVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 3)
)
if mibBuilder.loadTexts:
    nsCommonMonitorVoltage.setStatus("current")
_NsCommonMonitorVoltageTable_Object = MibTable
nsCommonMonitorVoltageTable = _NsCommonMonitorVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    nsCommonMonitorVoltageTable.setStatus("current")
_NsCommonMonitorVoltageEntry_Object = MibTableRow
nsCommonMonitorVoltageEntry = _NsCommonMonitorVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 3, 1, 1)
)
nsCommonMonitorVoltageEntry.setIndexNames(
    (0, "NOVELSAT-COMMON-MIB", "nsCommonMonitorVoltageIndex"),
)
if mibBuilder.loadTexts:
    nsCommonMonitorVoltageEntry.setStatus("current")
_NsCommonMonitorVoltageIndex_Type = Counter32
_NsCommonMonitorVoltageIndex_Object = MibTableColumn
nsCommonMonitorVoltageIndex = _NsCommonMonitorVoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 3, 1, 1, 1),
    _NsCommonMonitorVoltageIndex_Type()
)
nsCommonMonitorVoltageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonMonitorVoltageIndex.setStatus("current")


class _NsCommonMonitorVoltageName_Type(DisplayString):
    """Custom type nsCommonMonitorVoltageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonMonitorVoltageName_Type.__name__ = "DisplayString"
_NsCommonMonitorVoltageName_Object = MibTableColumn
nsCommonMonitorVoltageName = _NsCommonMonitorVoltageName_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 3, 1, 1, 2),
    _NsCommonMonitorVoltageName_Type()
)
nsCommonMonitorVoltageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorVoltageName.setStatus("current")
_NsCommonMonitorVoltageValue_Type = Integer32
_NsCommonMonitorVoltageValue_Object = MibTableColumn
nsCommonMonitorVoltageValue = _NsCommonMonitorVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 3, 1, 1, 3),
    _NsCommonMonitorVoltageValue_Type()
)
nsCommonMonitorVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorVoltageValue.setStatus("current")
_NsCommonMonitorPowerSupply_ObjectIdentity = ObjectIdentity
nsCommonMonitorPowerSupply = _NsCommonMonitorPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 4)
)
if mibBuilder.loadTexts:
    nsCommonMonitorPowerSupply.setStatus("current")
_NsCommonMonitorPowerSupplyTable_Object = MibTable
nsCommonMonitorPowerSupplyTable = _NsCommonMonitorPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    nsCommonMonitorPowerSupplyTable.setStatus("current")
_NsCommonMonitorPowerSupplyEntry_Object = MibTableRow
nsCommonMonitorPowerSupplyEntry = _NsCommonMonitorPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 4, 1, 1)
)
nsCommonMonitorPowerSupplyEntry.setIndexNames(
    (0, "NOVELSAT-COMMON-MIB", "nsCommonMonitorPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    nsCommonMonitorPowerSupplyEntry.setStatus("current")
_NsCommonMonitorPowerSupplyIndex_Type = Counter32
_NsCommonMonitorPowerSupplyIndex_Object = MibTableColumn
nsCommonMonitorPowerSupplyIndex = _NsCommonMonitorPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 4, 1, 1, 1),
    _NsCommonMonitorPowerSupplyIndex_Type()
)
nsCommonMonitorPowerSupplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonMonitorPowerSupplyIndex.setStatus("current")


class _NsCommonMonitorPowerSupplyName_Type(DisplayString):
    """Custom type nsCommonMonitorPowerSupplyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonMonitorPowerSupplyName_Type.__name__ = "DisplayString"
_NsCommonMonitorPowerSupplyName_Object = MibTableColumn
nsCommonMonitorPowerSupplyName = _NsCommonMonitorPowerSupplyName_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 4, 1, 1, 2),
    _NsCommonMonitorPowerSupplyName_Type()
)
nsCommonMonitorPowerSupplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorPowerSupplyName.setStatus("current")


class _NsCommonMonitorPowerSupplyValue_Type(DisplayString):
    """Custom type nsCommonMonitorPowerSupplyValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonMonitorPowerSupplyValue_Type.__name__ = "DisplayString"
_NsCommonMonitorPowerSupplyValue_Object = MibTableColumn
nsCommonMonitorPowerSupplyValue = _NsCommonMonitorPowerSupplyValue_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 4, 1, 1, 3),
    _NsCommonMonitorPowerSupplyValue_Type()
)
nsCommonMonitorPowerSupplyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorPowerSupplyValue.setStatus("current")
_NsCommonMonitorNetwork_ObjectIdentity = ObjectIdentity
nsCommonMonitorNetwork = _NsCommonMonitorNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5)
)
if mibBuilder.loadTexts:
    nsCommonMonitorNetwork.setStatus("current")
_NsCommonMonitorNetworkInterfaces_ObjectIdentity = ObjectIdentity
nsCommonMonitorNetworkInterfaces = _NsCommonMonitorNetworkInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfaces.setStatus("current")
_NsCommonMonitorNetworkInterfacesLanTable_Object = MibTable
nsCommonMonitorNetworkInterfacesLanTable = _NsCommonMonitorNetworkInterfacesLanTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfacesLanTable.setStatus("current")
_NsCommonMonitorNetworkInterfacesLanEntry_Object = MibTableRow
nsCommonMonitorNetworkInterfacesLanEntry = _NsCommonMonitorNetworkInterfacesLanEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 1, 1, 1)
)
nsCommonMonitorNetworkInterfacesLanEntry.setIndexNames(
    (0, "NOVELSAT-COMMON-MIB", "nsCommonMonitorNetworkInterfacesLanIndex"),
)
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfacesLanEntry.setStatus("current")
_NsCommonMonitorNetworkInterfacesLanIndex_Type = Counter32
_NsCommonMonitorNetworkInterfacesLanIndex_Object = MibTableColumn
nsCommonMonitorNetworkInterfacesLanIndex = _NsCommonMonitorNetworkInterfacesLanIndex_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 1, 1, 1, 1),
    _NsCommonMonitorNetworkInterfacesLanIndex_Type()
)
nsCommonMonitorNetworkInterfacesLanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfacesLanIndex.setStatus("current")


class _NsCommonMonitorNetworkInterfacesLanName_Type(DisplayString):
    """Custom type nsCommonMonitorNetworkInterfacesLanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonMonitorNetworkInterfacesLanName_Type.__name__ = "DisplayString"
_NsCommonMonitorNetworkInterfacesLanName_Object = MibTableColumn
nsCommonMonitorNetworkInterfacesLanName = _NsCommonMonitorNetworkInterfacesLanName_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 1, 1, 1, 2),
    _NsCommonMonitorNetworkInterfacesLanName_Type()
)
nsCommonMonitorNetworkInterfacesLanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfacesLanName.setStatus("current")


class _NsCommonMonitorNetworkInterfacesLanAdminStatus_Type(Integer32):
    """Custom type nsCommonMonitorNetworkInterfacesLanAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notApplicable", 255))
    )


_NsCommonMonitorNetworkInterfacesLanAdminStatus_Type.__name__ = "Integer32"
_NsCommonMonitorNetworkInterfacesLanAdminStatus_Object = MibTableColumn
nsCommonMonitorNetworkInterfacesLanAdminStatus = _NsCommonMonitorNetworkInterfacesLanAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 1, 1, 1, 3),
    _NsCommonMonitorNetworkInterfacesLanAdminStatus_Type()
)
nsCommonMonitorNetworkInterfacesLanAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfacesLanAdminStatus.setStatus("current")


class _NsCommonMonitorNetworkInterfacesLanOperStatus_Type(Integer32):
    """Custom type nsCommonMonitorNetworkInterfacesLanOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notApplicable", 255))
    )


_NsCommonMonitorNetworkInterfacesLanOperStatus_Type.__name__ = "Integer32"
_NsCommonMonitorNetworkInterfacesLanOperStatus_Object = MibTableColumn
nsCommonMonitorNetworkInterfacesLanOperStatus = _NsCommonMonitorNetworkInterfacesLanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 1, 1, 1, 4),
    _NsCommonMonitorNetworkInterfacesLanOperStatus_Type()
)
nsCommonMonitorNetworkInterfacesLanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfacesLanOperStatus.setStatus("current")
_NsCommonMonitorNetworkInterfacesLanPort_Type = Unsigned32
_NsCommonMonitorNetworkInterfacesLanPort_Object = MibTableColumn
nsCommonMonitorNetworkInterfacesLanPort = _NsCommonMonitorNetworkInterfacesLanPort_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 1, 1, 1, 5),
    _NsCommonMonitorNetworkInterfacesLanPort_Type()
)
nsCommonMonitorNetworkInterfacesLanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfacesLanPort.setStatus("current")
_NsCommonMonitorNetworkInterfacesLanVlan_Type = Unsigned32
_NsCommonMonitorNetworkInterfacesLanVlan_Object = MibTableColumn
nsCommonMonitorNetworkInterfacesLanVlan = _NsCommonMonitorNetworkInterfacesLanVlan_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 1, 1, 1, 6),
    _NsCommonMonitorNetworkInterfacesLanVlan_Type()
)
nsCommonMonitorNetworkInterfacesLanVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfacesLanVlan.setStatus("current")


class _NsCommonMonitorNetworkInterfacesLanMacAddress_Type(DisplayString):
    """Custom type nsCommonMonitorNetworkInterfacesLanMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonMonitorNetworkInterfacesLanMacAddress_Type.__name__ = "DisplayString"
_NsCommonMonitorNetworkInterfacesLanMacAddress_Object = MibTableColumn
nsCommonMonitorNetworkInterfacesLanMacAddress = _NsCommonMonitorNetworkInterfacesLanMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 1, 1, 1, 7),
    _NsCommonMonitorNetworkInterfacesLanMacAddress_Type()
)
nsCommonMonitorNetworkInterfacesLanMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfacesLanMacAddress.setStatus("current")
_NsCommonMonitorNetworkInterfacesLanIpAddress_Type = IpAddress
_NsCommonMonitorNetworkInterfacesLanIpAddress_Object = MibTableColumn
nsCommonMonitorNetworkInterfacesLanIpAddress = _NsCommonMonitorNetworkInterfacesLanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 1, 1, 1, 8),
    _NsCommonMonitorNetworkInterfacesLanIpAddress_Type()
)
nsCommonMonitorNetworkInterfacesLanIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfacesLanIpAddress.setStatus("current")
_NsCommonMonitorNetworkInterfacesLanSubnetMask_Type = IpAddress
_NsCommonMonitorNetworkInterfacesLanSubnetMask_Object = MibTableColumn
nsCommonMonitorNetworkInterfacesLanSubnetMask = _NsCommonMonitorNetworkInterfacesLanSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 1, 1, 1, 9),
    _NsCommonMonitorNetworkInterfacesLanSubnetMask_Type()
)
nsCommonMonitorNetworkInterfacesLanSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfacesLanSubnetMask.setStatus("current")
_NsCommonMonitorNetworkInterfacesSatTable_Object = MibTable
nsCommonMonitorNetworkInterfacesSatTable = _NsCommonMonitorNetworkInterfacesSatTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 1, 2)
)
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfacesSatTable.setStatus("current")
_NsCommonMonitorNetworkInterfacesSatEntry_Object = MibTableRow
nsCommonMonitorNetworkInterfacesSatEntry = _NsCommonMonitorNetworkInterfacesSatEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 1, 2, 1)
)
nsCommonMonitorNetworkInterfacesSatEntry.setIndexNames(
    (0, "NOVELSAT-COMMON-MIB", "nsCommonMonitorNetworkInterfacesSatIndex"),
)
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfacesSatEntry.setStatus("current")
_NsCommonMonitorNetworkInterfacesSatIndex_Type = Counter32
_NsCommonMonitorNetworkInterfacesSatIndex_Object = MibTableColumn
nsCommonMonitorNetworkInterfacesSatIndex = _NsCommonMonitorNetworkInterfacesSatIndex_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 1, 2, 1, 1),
    _NsCommonMonitorNetworkInterfacesSatIndex_Type()
)
nsCommonMonitorNetworkInterfacesSatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfacesSatIndex.setStatus("current")


class _NsCommonMonitorNetworkInterfacesSatName_Type(DisplayString):
    """Custom type nsCommonMonitorNetworkInterfacesSatName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonMonitorNetworkInterfacesSatName_Type.__name__ = "DisplayString"
_NsCommonMonitorNetworkInterfacesSatName_Object = MibTableColumn
nsCommonMonitorNetworkInterfacesSatName = _NsCommonMonitorNetworkInterfacesSatName_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 1, 2, 1, 2),
    _NsCommonMonitorNetworkInterfacesSatName_Type()
)
nsCommonMonitorNetworkInterfacesSatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfacesSatName.setStatus("current")


class _NsCommonMonitorNetworkInterfacesSatAdminStatus_Type(Integer32):
    """Custom type nsCommonMonitorNetworkInterfacesSatAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notApplicable", 255))
    )


_NsCommonMonitorNetworkInterfacesSatAdminStatus_Type.__name__ = "Integer32"
_NsCommonMonitorNetworkInterfacesSatAdminStatus_Object = MibTableColumn
nsCommonMonitorNetworkInterfacesSatAdminStatus = _NsCommonMonitorNetworkInterfacesSatAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 1, 2, 1, 3),
    _NsCommonMonitorNetworkInterfacesSatAdminStatus_Type()
)
nsCommonMonitorNetworkInterfacesSatAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfacesSatAdminStatus.setStatus("current")


class _NsCommonMonitorNetworkInterfacesSatOperStatus_Type(Integer32):
    """Custom type nsCommonMonitorNetworkInterfacesSatOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notApplicable", 255))
    )


_NsCommonMonitorNetworkInterfacesSatOperStatus_Type.__name__ = "Integer32"
_NsCommonMonitorNetworkInterfacesSatOperStatus_Object = MibTableColumn
nsCommonMonitorNetworkInterfacesSatOperStatus = _NsCommonMonitorNetworkInterfacesSatOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 1, 2, 1, 4),
    _NsCommonMonitorNetworkInterfacesSatOperStatus_Type()
)
nsCommonMonitorNetworkInterfacesSatOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfacesSatOperStatus.setStatus("current")
_NsCommonMonitorNetworkInterfacesSatPort_Type = Unsigned32
_NsCommonMonitorNetworkInterfacesSatPort_Object = MibTableColumn
nsCommonMonitorNetworkInterfacesSatPort = _NsCommonMonitorNetworkInterfacesSatPort_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 1, 2, 1, 5),
    _NsCommonMonitorNetworkInterfacesSatPort_Type()
)
nsCommonMonitorNetworkInterfacesSatPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfacesSatPort.setStatus("current")
_NsCommonMonitorNetworkInterfacesSatPid_Type = Unsigned32
_NsCommonMonitorNetworkInterfacesSatPid_Object = MibTableColumn
nsCommonMonitorNetworkInterfacesSatPid = _NsCommonMonitorNetworkInterfacesSatPid_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 1, 2, 1, 6),
    _NsCommonMonitorNetworkInterfacesSatPid_Type()
)
nsCommonMonitorNetworkInterfacesSatPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfacesSatPid.setStatus("current")


class _NsCommonMonitorNetworkInterfacesSatMacAddress_Type(DisplayString):
    """Custom type nsCommonMonitorNetworkInterfacesSatMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonMonitorNetworkInterfacesSatMacAddress_Type.__name__ = "DisplayString"
_NsCommonMonitorNetworkInterfacesSatMacAddress_Object = MibTableColumn
nsCommonMonitorNetworkInterfacesSatMacAddress = _NsCommonMonitorNetworkInterfacesSatMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 1, 2, 1, 7),
    _NsCommonMonitorNetworkInterfacesSatMacAddress_Type()
)
nsCommonMonitorNetworkInterfacesSatMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfacesSatMacAddress.setStatus("current")
_NsCommonMonitorNetworkInterfacesSatIpAddress_Type = IpAddress
_NsCommonMonitorNetworkInterfacesSatIpAddress_Object = MibTableColumn
nsCommonMonitorNetworkInterfacesSatIpAddress = _NsCommonMonitorNetworkInterfacesSatIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 1, 2, 1, 8),
    _NsCommonMonitorNetworkInterfacesSatIpAddress_Type()
)
nsCommonMonitorNetworkInterfacesSatIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfacesSatIpAddress.setStatus("current")
_NsCommonMonitorNetworkInterfacesSatSubnetMask_Type = IpAddress
_NsCommonMonitorNetworkInterfacesSatSubnetMask_Object = MibTableColumn
nsCommonMonitorNetworkInterfacesSatSubnetMask = _NsCommonMonitorNetworkInterfacesSatSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 1, 2, 1, 9),
    _NsCommonMonitorNetworkInterfacesSatSubnetMask_Type()
)
nsCommonMonitorNetworkInterfacesSatSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfacesSatSubnetMask.setStatus("current")


class _NsCommonMonitorNetworkInterfacesSatEncapsulation_Type(Integer32):
    """Custom type nsCommonMonitorNetworkInterfacesSatEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("encapsulationEth", 0),
          ("encapsulationEth8021q", 1),
          ("gse", 3),
          ("notApplicable", 255),
          ("nspe", 4),
          ("ule", 2))
    )


_NsCommonMonitorNetworkInterfacesSatEncapsulation_Type.__name__ = "Integer32"
_NsCommonMonitorNetworkInterfacesSatEncapsulation_Object = MibTableColumn
nsCommonMonitorNetworkInterfacesSatEncapsulation = _NsCommonMonitorNetworkInterfacesSatEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 1, 2, 1, 10),
    _NsCommonMonitorNetworkInterfacesSatEncapsulation_Type()
)
nsCommonMonitorNetworkInterfacesSatEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfacesSatEncapsulation.setStatus("current")
_NsCommonMonitorNetworkInterfaceStatisticsTable_Object = MibTable
nsCommonMonitorNetworkInterfaceStatisticsTable = _NsCommonMonitorNetworkInterfaceStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 2)
)
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfaceStatisticsTable.setStatus("current")
_NsCommonMonitorNetworkInterfaceStatisticsEntry_Object = MibTableRow
nsCommonMonitorNetworkInterfaceStatisticsEntry = _NsCommonMonitorNetworkInterfaceStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 2, 1)
)
nsCommonMonitorNetworkInterfaceStatisticsEntry.setIndexNames(
    (0, "NOVELSAT-COMMON-MIB", "nsCommonMonitorNetworkInterfaceStatisticsIndex"),
)
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfaceStatisticsEntry.setStatus("current")
_NsCommonMonitorNetworkInterfaceStatisticsIndex_Type = Counter32
_NsCommonMonitorNetworkInterfaceStatisticsIndex_Object = MibTableColumn
nsCommonMonitorNetworkInterfaceStatisticsIndex = _NsCommonMonitorNetworkInterfaceStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 2, 1, 1),
    _NsCommonMonitorNetworkInterfaceStatisticsIndex_Type()
)
nsCommonMonitorNetworkInterfaceStatisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfaceStatisticsIndex.setStatus("current")
_NsCommonMonitorNetworkInterfaceStatisticsMtu_Type = Unsigned32
_NsCommonMonitorNetworkInterfaceStatisticsMtu_Object = MibTableColumn
nsCommonMonitorNetworkInterfaceStatisticsMtu = _NsCommonMonitorNetworkInterfaceStatisticsMtu_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 2, 1, 2),
    _NsCommonMonitorNetworkInterfaceStatisticsMtu_Type()
)
nsCommonMonitorNetworkInterfaceStatisticsMtu.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfaceStatisticsMtu.setStatus("current")
_NsCommonMonitorNetworkInterfaceStatisticsRxOk_Type = CounterBasedGauge64
_NsCommonMonitorNetworkInterfaceStatisticsRxOk_Object = MibTableColumn
nsCommonMonitorNetworkInterfaceStatisticsRxOk = _NsCommonMonitorNetworkInterfaceStatisticsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 2, 1, 3),
    _NsCommonMonitorNetworkInterfaceStatisticsRxOk_Type()
)
nsCommonMonitorNetworkInterfaceStatisticsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfaceStatisticsRxOk.setStatus("current")
_NsCommonMonitorNetworkInterfaceStatisticsRxError_Type = CounterBasedGauge64
_NsCommonMonitorNetworkInterfaceStatisticsRxError_Object = MibTableColumn
nsCommonMonitorNetworkInterfaceStatisticsRxError = _NsCommonMonitorNetworkInterfaceStatisticsRxError_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 2, 1, 4),
    _NsCommonMonitorNetworkInterfaceStatisticsRxError_Type()
)
nsCommonMonitorNetworkInterfaceStatisticsRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfaceStatisticsRxError.setStatus("current")
_NsCommonMonitorNetworkInterfaceStatisticsRxDrop_Type = CounterBasedGauge64
_NsCommonMonitorNetworkInterfaceStatisticsRxDrop_Object = MibTableColumn
nsCommonMonitorNetworkInterfaceStatisticsRxDrop = _NsCommonMonitorNetworkInterfaceStatisticsRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 2, 1, 5),
    _NsCommonMonitorNetworkInterfaceStatisticsRxDrop_Type()
)
nsCommonMonitorNetworkInterfaceStatisticsRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfaceStatisticsRxDrop.setStatus("current")
_NsCommonMonitorNetworkInterfaceStatisticsRxOvr_Type = CounterBasedGauge64
_NsCommonMonitorNetworkInterfaceStatisticsRxOvr_Object = MibTableColumn
nsCommonMonitorNetworkInterfaceStatisticsRxOvr = _NsCommonMonitorNetworkInterfaceStatisticsRxOvr_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 2, 1, 6),
    _NsCommonMonitorNetworkInterfaceStatisticsRxOvr_Type()
)
nsCommonMonitorNetworkInterfaceStatisticsRxOvr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfaceStatisticsRxOvr.setStatus("current")
_NsCommonMonitorNetworkInterfaceStatisticsTxOk_Type = CounterBasedGauge64
_NsCommonMonitorNetworkInterfaceStatisticsTxOk_Object = MibTableColumn
nsCommonMonitorNetworkInterfaceStatisticsTxOk = _NsCommonMonitorNetworkInterfaceStatisticsTxOk_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 2, 1, 7),
    _NsCommonMonitorNetworkInterfaceStatisticsTxOk_Type()
)
nsCommonMonitorNetworkInterfaceStatisticsTxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfaceStatisticsTxOk.setStatus("current")
_NsCommonMonitorNetworkInterfaceStatisticsTxError_Type = CounterBasedGauge64
_NsCommonMonitorNetworkInterfaceStatisticsTxError_Object = MibTableColumn
nsCommonMonitorNetworkInterfaceStatisticsTxError = _NsCommonMonitorNetworkInterfaceStatisticsTxError_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 2, 1, 8),
    _NsCommonMonitorNetworkInterfaceStatisticsTxError_Type()
)
nsCommonMonitorNetworkInterfaceStatisticsTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfaceStatisticsTxError.setStatus("current")
_NsCommonMonitorNetworkInterfaceStatisticsTxDrop_Type = CounterBasedGauge64
_NsCommonMonitorNetworkInterfaceStatisticsTxDrop_Object = MibTableColumn
nsCommonMonitorNetworkInterfaceStatisticsTxDrop = _NsCommonMonitorNetworkInterfaceStatisticsTxDrop_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 2, 1, 9),
    _NsCommonMonitorNetworkInterfaceStatisticsTxDrop_Type()
)
nsCommonMonitorNetworkInterfaceStatisticsTxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfaceStatisticsTxDrop.setStatus("current")
_NsCommonMonitorNetworkInterfaceStatisticsTxOvr_Type = CounterBasedGauge64
_NsCommonMonitorNetworkInterfaceStatisticsTxOvr_Object = MibTableColumn
nsCommonMonitorNetworkInterfaceStatisticsTxOvr = _NsCommonMonitorNetworkInterfaceStatisticsTxOvr_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 2, 1, 10),
    _NsCommonMonitorNetworkInterfaceStatisticsTxOvr_Type()
)
nsCommonMonitorNetworkInterfaceStatisticsTxOvr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfaceStatisticsTxOvr.setStatus("current")
_NsCommonMonitorNetworkInterfaceStatisticsRxBytes_Type = CounterBasedGauge64
_NsCommonMonitorNetworkInterfaceStatisticsRxBytes_Object = MibTableColumn
nsCommonMonitorNetworkInterfaceStatisticsRxBytes = _NsCommonMonitorNetworkInterfaceStatisticsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 2, 1, 11),
    _NsCommonMonitorNetworkInterfaceStatisticsRxBytes_Type()
)
nsCommonMonitorNetworkInterfaceStatisticsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfaceStatisticsRxBytes.setStatus("current")
_NsCommonMonitorNetworkInterfaceStatisticsTxBytes_Type = CounterBasedGauge64
_NsCommonMonitorNetworkInterfaceStatisticsTxBytes_Object = MibTableColumn
nsCommonMonitorNetworkInterfaceStatisticsTxBytes = _NsCommonMonitorNetworkInterfaceStatisticsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 2, 1, 12),
    _NsCommonMonitorNetworkInterfaceStatisticsTxBytes_Type()
)
nsCommonMonitorNetworkInterfaceStatisticsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfaceStatisticsTxBytes.setStatus("current")
_NsCommonMonitorNetworkInterfaceStatisticsRxBps_Type = CounterBasedGauge64
_NsCommonMonitorNetworkInterfaceStatisticsRxBps_Object = MibTableColumn
nsCommonMonitorNetworkInterfaceStatisticsRxBps = _NsCommonMonitorNetworkInterfaceStatisticsRxBps_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 2, 1, 13),
    _NsCommonMonitorNetworkInterfaceStatisticsRxBps_Type()
)
nsCommonMonitorNetworkInterfaceStatisticsRxBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfaceStatisticsRxBps.setStatus("current")
_NsCommonMonitorNetworkInterfaceStatisticsTxBps_Type = CounterBasedGauge64
_NsCommonMonitorNetworkInterfaceStatisticsTxBps_Object = MibTableColumn
nsCommonMonitorNetworkInterfaceStatisticsTxBps = _NsCommonMonitorNetworkInterfaceStatisticsTxBps_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 2, 1, 14),
    _NsCommonMonitorNetworkInterfaceStatisticsTxBps_Type()
)
nsCommonMonitorNetworkInterfaceStatisticsTxBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfaceStatisticsTxBps.setStatus("current")


class _NsCommonMonitorNetworkInterfaceStatisticsName_Type(DisplayString):
    """Custom type nsCommonMonitorNetworkInterfaceStatisticsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonMonitorNetworkInterfaceStatisticsName_Type.__name__ = "DisplayString"
_NsCommonMonitorNetworkInterfaceStatisticsName_Object = MibTableColumn
nsCommonMonitorNetworkInterfaceStatisticsName = _NsCommonMonitorNetworkInterfaceStatisticsName_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 2, 1, 15),
    _NsCommonMonitorNetworkInterfaceStatisticsName_Type()
)
nsCommonMonitorNetworkInterfaceStatisticsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfaceStatisticsName.setStatus("current")
_NsCommonMonitorNetworkQueuesStatisticsTable_Object = MibTable
nsCommonMonitorNetworkQueuesStatisticsTable = _NsCommonMonitorNetworkQueuesStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 3)
)
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkQueuesStatisticsTable.setStatus("current")
_NsCommonMonitorNetworkQueuesStatisticsEntry_Object = MibTableRow
nsCommonMonitorNetworkQueuesStatisticsEntry = _NsCommonMonitorNetworkQueuesStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 3, 1)
)
nsCommonMonitorNetworkQueuesStatisticsEntry.setIndexNames(
    (0, "NOVELSAT-COMMON-MIB", "nsCommonMonitorNetworkQueuesStatisticsNeighborIndex"),
    (0, "NOVELSAT-COMMON-MIB", "nsCommonMonitorNetworkQueuesStatisticsCos"),
)
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkQueuesStatisticsEntry.setStatus("current")
_NsCommonMonitorNetworkQueuesStatisticsNeighborIndex_Type = Counter32
_NsCommonMonitorNetworkQueuesStatisticsNeighborIndex_Object = MibTableColumn
nsCommonMonitorNetworkQueuesStatisticsNeighborIndex = _NsCommonMonitorNetworkQueuesStatisticsNeighborIndex_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 3, 1, 1),
    _NsCommonMonitorNetworkQueuesStatisticsNeighborIndex_Type()
)
nsCommonMonitorNetworkQueuesStatisticsNeighborIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkQueuesStatisticsNeighborIndex.setStatus("current")


class _NsCommonMonitorNetworkQueuesStatisticsCos_Type(Integer32):
    """Custom type nsCommonMonitorNetworkQueuesStatisticsCos based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("cos0", 1),
          ("cos1", 2),
          ("cos2", 3),
          ("cos3", 4),
          ("cos4", 5),
          ("cos5", 6),
          ("cos6", 7),
          ("cos7", 8),
          ("notApplicable", 255))
    )


_NsCommonMonitorNetworkQueuesStatisticsCos_Type.__name__ = "Integer32"
_NsCommonMonitorNetworkQueuesStatisticsCos_Object = MibTableColumn
nsCommonMonitorNetworkQueuesStatisticsCos = _NsCommonMonitorNetworkQueuesStatisticsCos_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 3, 1, 2),
    _NsCommonMonitorNetworkQueuesStatisticsCos_Type()
)
nsCommonMonitorNetworkQueuesStatisticsCos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkQueuesStatisticsCos.setStatus("current")
_NsCommonMonitorNetworkQueuesStatisticsEnqueuedBytes_Type = Counter64
_NsCommonMonitorNetworkQueuesStatisticsEnqueuedBytes_Object = MibTableColumn
nsCommonMonitorNetworkQueuesStatisticsEnqueuedBytes = _NsCommonMonitorNetworkQueuesStatisticsEnqueuedBytes_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 3, 1, 3),
    _NsCommonMonitorNetworkQueuesStatisticsEnqueuedBytes_Type()
)
nsCommonMonitorNetworkQueuesStatisticsEnqueuedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkQueuesStatisticsEnqueuedBytes.setStatus("current")
_NsCommonMonitorNetworkQueuesStatisticsEnqueuedPackets_Type = Counter64
_NsCommonMonitorNetworkQueuesStatisticsEnqueuedPackets_Object = MibTableColumn
nsCommonMonitorNetworkQueuesStatisticsEnqueuedPackets = _NsCommonMonitorNetworkQueuesStatisticsEnqueuedPackets_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 3, 1, 4),
    _NsCommonMonitorNetworkQueuesStatisticsEnqueuedPackets_Type()
)
nsCommonMonitorNetworkQueuesStatisticsEnqueuedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkQueuesStatisticsEnqueuedPackets.setStatus("current")
_NsCommonMonitorNetworkQueuesStatisticsBackloggedBytes_Type = Counter64
_NsCommonMonitorNetworkQueuesStatisticsBackloggedBytes_Object = MibTableColumn
nsCommonMonitorNetworkQueuesStatisticsBackloggedBytes = _NsCommonMonitorNetworkQueuesStatisticsBackloggedBytes_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 3, 1, 5),
    _NsCommonMonitorNetworkQueuesStatisticsBackloggedBytes_Type()
)
nsCommonMonitorNetworkQueuesStatisticsBackloggedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkQueuesStatisticsBackloggedBytes.setStatus("current")
_NsCommonMonitorNetworkQueuesStatisticsBackloggedPackets_Type = Counter64
_NsCommonMonitorNetworkQueuesStatisticsBackloggedPackets_Object = MibTableColumn
nsCommonMonitorNetworkQueuesStatisticsBackloggedPackets = _NsCommonMonitorNetworkQueuesStatisticsBackloggedPackets_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 3, 1, 6),
    _NsCommonMonitorNetworkQueuesStatisticsBackloggedPackets_Type()
)
nsCommonMonitorNetworkQueuesStatisticsBackloggedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkQueuesStatisticsBackloggedPackets.setStatus("current")
_NsCommonMonitorNetworkQueuesStatisticsDroppedYellowPackets_Type = Counter64
_NsCommonMonitorNetworkQueuesStatisticsDroppedYellowPackets_Object = MibTableColumn
nsCommonMonitorNetworkQueuesStatisticsDroppedYellowPackets = _NsCommonMonitorNetworkQueuesStatisticsDroppedYellowPackets_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 3, 1, 7),
    _NsCommonMonitorNetworkQueuesStatisticsDroppedYellowPackets_Type()
)
nsCommonMonitorNetworkQueuesStatisticsDroppedYellowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkQueuesStatisticsDroppedYellowPackets.setStatus("current")
_NsCommonMonitorNetworkQueuesStatisticsDroppedGreenPackets_Type = Counter64
_NsCommonMonitorNetworkQueuesStatisticsDroppedGreenPackets_Object = MibTableColumn
nsCommonMonitorNetworkQueuesStatisticsDroppedGreenPackets = _NsCommonMonitorNetworkQueuesStatisticsDroppedGreenPackets_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 3, 1, 8),
    _NsCommonMonitorNetworkQueuesStatisticsDroppedGreenPackets_Type()
)
nsCommonMonitorNetworkQueuesStatisticsDroppedGreenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkQueuesStatisticsDroppedGreenPackets.setStatus("current")
_NsCommonMonitorNetworkNeighborsStatisticsTable_Object = MibTable
nsCommonMonitorNetworkNeighborsStatisticsTable = _NsCommonMonitorNetworkNeighborsStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 4)
)
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkNeighborsStatisticsTable.setStatus("current")
_NsCommonMonitorNetworkNeighborsStatisticsEntry_Object = MibTableRow
nsCommonMonitorNetworkNeighborsStatisticsEntry = _NsCommonMonitorNetworkNeighborsStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 4, 1)
)
nsCommonMonitorNetworkNeighborsStatisticsEntry.setIndexNames(
    (0, "NOVELSAT-COMMON-MIB", "nsCommonMonitorNetworkNeighborsStatisticsIndex"),
)
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkNeighborsStatisticsEntry.setStatus("current")
_NsCommonMonitorNetworkNeighborsStatisticsIndex_Type = Counter32
_NsCommonMonitorNetworkNeighborsStatisticsIndex_Object = MibTableColumn
nsCommonMonitorNetworkNeighborsStatisticsIndex = _NsCommonMonitorNetworkNeighborsStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 4, 1, 1),
    _NsCommonMonitorNetworkNeighborsStatisticsIndex_Type()
)
nsCommonMonitorNetworkNeighborsStatisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkNeighborsStatisticsIndex.setStatus("current")
_NsCommonMonitorNetworkNeighborsStatisticsAverageTxRate_Type = Counter64
_NsCommonMonitorNetworkNeighborsStatisticsAverageTxRate_Object = MibTableColumn
nsCommonMonitorNetworkNeighborsStatisticsAverageTxRate = _NsCommonMonitorNetworkNeighborsStatisticsAverageTxRate_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 4, 1, 2),
    _NsCommonMonitorNetworkNeighborsStatisticsAverageTxRate_Type()
)
nsCommonMonitorNetworkNeighborsStatisticsAverageTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkNeighborsStatisticsAverageTxRate.setStatus("current")
_NsCommonMonitorNetworkNeighborsStatisticsAverageTxPacketRate_Type = Counter64
_NsCommonMonitorNetworkNeighborsStatisticsAverageTxPacketRate_Object = MibTableColumn
nsCommonMonitorNetworkNeighborsStatisticsAverageTxPacketRate = _NsCommonMonitorNetworkNeighborsStatisticsAverageTxPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 4, 1, 3),
    _NsCommonMonitorNetworkNeighborsStatisticsAverageTxPacketRate_Type()
)
nsCommonMonitorNetworkNeighborsStatisticsAverageTxPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkNeighborsStatisticsAverageTxPacketRate.setStatus("current")
_NsCommonMonitorNetworkNeighborsStatisticsTxBytes_Type = Counter64
_NsCommonMonitorNetworkNeighborsStatisticsTxBytes_Object = MibTableColumn
nsCommonMonitorNetworkNeighborsStatisticsTxBytes = _NsCommonMonitorNetworkNeighborsStatisticsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 4, 1, 4),
    _NsCommonMonitorNetworkNeighborsStatisticsTxBytes_Type()
)
nsCommonMonitorNetworkNeighborsStatisticsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkNeighborsStatisticsTxBytes.setStatus("current")
_NsCommonMonitorNetworkNeighborsStatisticsTxPackets_Type = Counter64
_NsCommonMonitorNetworkNeighborsStatisticsTxPackets_Object = MibTableColumn
nsCommonMonitorNetworkNeighborsStatisticsTxPackets = _NsCommonMonitorNetworkNeighborsStatisticsTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 4, 1, 5),
    _NsCommonMonitorNetworkNeighborsStatisticsTxPackets_Type()
)
nsCommonMonitorNetworkNeighborsStatisticsTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkNeighborsStatisticsTxPackets.setStatus("current")
_NsCommonMonitorNetworkBwManagementStatisticsTable_Object = MibTable
nsCommonMonitorNetworkBwManagementStatisticsTable = _NsCommonMonitorNetworkBwManagementStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 5)
)
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkBwManagementStatisticsTable.setStatus("current")
_NsCommonMonitorNetworkBwManagementStatisticsEntry_Object = MibTableRow
nsCommonMonitorNetworkBwManagementStatisticsEntry = _NsCommonMonitorNetworkBwManagementStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 5, 1)
)
nsCommonMonitorNetworkBwManagementStatisticsEntry.setIndexNames(
    (0, "NOVELSAT-COMMON-MIB", "nsCommonMonitorNetworkBwManagementStatisticsNeighborIndex"),
)
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkBwManagementStatisticsEntry.setStatus("current")
_NsCommonMonitorNetworkBwManagementStatisticsNeighborIndex_Type = Counter32
_NsCommonMonitorNetworkBwManagementStatisticsNeighborIndex_Object = MibTableColumn
nsCommonMonitorNetworkBwManagementStatisticsNeighborIndex = _NsCommonMonitorNetworkBwManagementStatisticsNeighborIndex_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 5, 1, 1),
    _NsCommonMonitorNetworkBwManagementStatisticsNeighborIndex_Type()
)
nsCommonMonitorNetworkBwManagementStatisticsNeighborIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkBwManagementStatisticsNeighborIndex.setStatus("current")
_NsCommonMonitorNetworkBwManagementStatisticsGreenPackets_Type = Counter64
_NsCommonMonitorNetworkBwManagementStatisticsGreenPackets_Object = MibTableColumn
nsCommonMonitorNetworkBwManagementStatisticsGreenPackets = _NsCommonMonitorNetworkBwManagementStatisticsGreenPackets_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 5, 1, 2),
    _NsCommonMonitorNetworkBwManagementStatisticsGreenPackets_Type()
)
nsCommonMonitorNetworkBwManagementStatisticsGreenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkBwManagementStatisticsGreenPackets.setStatus("current")
_NsCommonMonitorNetworkBwManagementStatisticsGreenRates_Type = Counter64
_NsCommonMonitorNetworkBwManagementStatisticsGreenRates_Object = MibTableColumn
nsCommonMonitorNetworkBwManagementStatisticsGreenRates = _NsCommonMonitorNetworkBwManagementStatisticsGreenRates_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 5, 1, 3),
    _NsCommonMonitorNetworkBwManagementStatisticsGreenRates_Type()
)
nsCommonMonitorNetworkBwManagementStatisticsGreenRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkBwManagementStatisticsGreenRates.setStatus("current")
_NsCommonMonitorNetworkBwManagementStatisticsYellowPackets_Type = Counter64
_NsCommonMonitorNetworkBwManagementStatisticsYellowPackets_Object = MibTableColumn
nsCommonMonitorNetworkBwManagementStatisticsYellowPackets = _NsCommonMonitorNetworkBwManagementStatisticsYellowPackets_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 5, 1, 4),
    _NsCommonMonitorNetworkBwManagementStatisticsYellowPackets_Type()
)
nsCommonMonitorNetworkBwManagementStatisticsYellowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkBwManagementStatisticsYellowPackets.setStatus("current")
_NsCommonMonitorNetworkBwManagementStatisticsYellowRates_Type = Counter64
_NsCommonMonitorNetworkBwManagementStatisticsYellowRates_Object = MibTableColumn
nsCommonMonitorNetworkBwManagementStatisticsYellowRates = _NsCommonMonitorNetworkBwManagementStatisticsYellowRates_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 5, 1, 5),
    _NsCommonMonitorNetworkBwManagementStatisticsYellowRates_Type()
)
nsCommonMonitorNetworkBwManagementStatisticsYellowRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkBwManagementStatisticsYellowRates.setStatus("current")
_NsCommonMonitorNetworkBwManagementStatisticsRedPackets_Type = Counter64
_NsCommonMonitorNetworkBwManagementStatisticsRedPackets_Object = MibTableColumn
nsCommonMonitorNetworkBwManagementStatisticsRedPackets = _NsCommonMonitorNetworkBwManagementStatisticsRedPackets_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 5, 1, 6),
    _NsCommonMonitorNetworkBwManagementStatisticsRedPackets_Type()
)
nsCommonMonitorNetworkBwManagementStatisticsRedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkBwManagementStatisticsRedPackets.setStatus("current")
_NsCommonMonitorNetworkBwManagementStatisticsRedRates_Type = Counter64
_NsCommonMonitorNetworkBwManagementStatisticsRedRates_Object = MibTableColumn
nsCommonMonitorNetworkBwManagementStatisticsRedRates = _NsCommonMonitorNetworkBwManagementStatisticsRedRates_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 5, 1, 7),
    _NsCommonMonitorNetworkBwManagementStatisticsRedRates_Type()
)
nsCommonMonitorNetworkBwManagementStatisticsRedRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkBwManagementStatisticsRedRates.setStatus("current")


class _NsCommonMonitorNetworkInterfaceClrCmd_Type(Integer32):
    """Custom type nsCommonMonitorNetworkInterfaceClrCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("execute", 1),
          ("none", 0),
          ("notApplicable", 255))
    )


_NsCommonMonitorNetworkInterfaceClrCmd_Type.__name__ = "Integer32"
_NsCommonMonitorNetworkInterfaceClrCmd_Object = MibScalar
nsCommonMonitorNetworkInterfaceClrCmd = _NsCommonMonitorNetworkInterfaceClrCmd_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 5, 6),
    _NsCommonMonitorNetworkInterfaceClrCmd_Type()
)
nsCommonMonitorNetworkInterfaceClrCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonMonitorNetworkInterfaceClrCmd.setStatus("current")
_NsCommonSystem_ObjectIdentity = ObjectIdentity
nsCommonSystem = _NsCommonSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3)
)
if mibBuilder.loadTexts:
    nsCommonSystem.setStatus("current")
_NsCommonSystemSwVersion_ObjectIdentity = ObjectIdentity
nsCommonSystemSwVersion = _NsCommonSystemSwVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 1)
)
if mibBuilder.loadTexts:
    nsCommonSystemSwVersion.setStatus("current")


class _NsCommonSystemSwVersionFirmware_Type(DisplayString):
    """Custom type nsCommonSystemSwVersionFirmware based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonSystemSwVersionFirmware_Type.__name__ = "DisplayString"
_NsCommonSystemSwVersionFirmware_Object = MibScalar
nsCommonSystemSwVersionFirmware = _NsCommonSystemSwVersionFirmware_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 1, 1),
    _NsCommonSystemSwVersionFirmware_Type()
)
nsCommonSystemSwVersionFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonSystemSwVersionFirmware.setStatus("current")


class _NsCommonSystemSwVersionOs_Type(DisplayString):
    """Custom type nsCommonSystemSwVersionOs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonSystemSwVersionOs_Type.__name__ = "DisplayString"
_NsCommonSystemSwVersionOs_Object = MibScalar
nsCommonSystemSwVersionOs = _NsCommonSystemSwVersionOs_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 1, 2),
    _NsCommonSystemSwVersionOs_Type()
)
nsCommonSystemSwVersionOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonSystemSwVersionOs.setStatus("current")


class _NsCommonSystemSwVersionFs_Type(DisplayString):
    """Custom type nsCommonSystemSwVersionFs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonSystemSwVersionFs_Type.__name__ = "DisplayString"
_NsCommonSystemSwVersionFs_Object = MibScalar
nsCommonSystemSwVersionFs = _NsCommonSystemSwVersionFs_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 1, 3),
    _NsCommonSystemSwVersionFs_Type()
)
nsCommonSystemSwVersionFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonSystemSwVersionFs.setStatus("current")


class _NsCommonSystemSwVersionDb_Type(DisplayString):
    """Custom type nsCommonSystemSwVersionDb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonSystemSwVersionDb_Type.__name__ = "DisplayString"
_NsCommonSystemSwVersionDb_Object = MibScalar
nsCommonSystemSwVersionDb = _NsCommonSystemSwVersionDb_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 1, 4),
    _NsCommonSystemSwVersionDb_Type()
)
nsCommonSystemSwVersionDb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonSystemSwVersionDb.setStatus("current")
_NsCommonSystemSwVersionAppTable_Object = MibTable
nsCommonSystemSwVersionAppTable = _NsCommonSystemSwVersionAppTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 1, 5)
)
if mibBuilder.loadTexts:
    nsCommonSystemSwVersionAppTable.setStatus("current")
_NsCommonSystemSwVersionAppEntry_Object = MibTableRow
nsCommonSystemSwVersionAppEntry = _NsCommonSystemSwVersionAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 1, 5, 1)
)
nsCommonSystemSwVersionAppEntry.setIndexNames(
    (0, "NOVELSAT-COMMON-MIB", "nsCommonSystemSwVersionAppType"),
)
if mibBuilder.loadTexts:
    nsCommonSystemSwVersionAppEntry.setStatus("current")


class _NsCommonSystemSwVersionAppType_Type(Integer32):
    """Custom type nsCommonSystemSwVersionAppType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("backup", 3),
          ("main", 2))
    )


_NsCommonSystemSwVersionAppType_Type.__name__ = "Integer32"
_NsCommonSystemSwVersionAppType_Object = MibTableColumn
nsCommonSystemSwVersionAppType = _NsCommonSystemSwVersionAppType_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 1, 5, 1, 1),
    _NsCommonSystemSwVersionAppType_Type()
)
nsCommonSystemSwVersionAppType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonSystemSwVersionAppType.setStatus("current")


class _NsCommonSystemSwVersionAppWeb_Type(DisplayString):
    """Custom type nsCommonSystemSwVersionAppWeb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonSystemSwVersionAppWeb_Type.__name__ = "DisplayString"
_NsCommonSystemSwVersionAppWeb_Object = MibTableColumn
nsCommonSystemSwVersionAppWeb = _NsCommonSystemSwVersionAppWeb_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 1, 5, 1, 2),
    _NsCommonSystemSwVersionAppWeb_Type()
)
nsCommonSystemSwVersionAppWeb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonSystemSwVersionAppWeb.setStatus("current")


class _NsCommonSystemSwVersionAppFP_Type(DisplayString):
    """Custom type nsCommonSystemSwVersionAppFP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonSystemSwVersionAppFP_Type.__name__ = "DisplayString"
_NsCommonSystemSwVersionAppFP_Object = MibTableColumn
nsCommonSystemSwVersionAppFP = _NsCommonSystemSwVersionAppFP_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 1, 5, 1, 3),
    _NsCommonSystemSwVersionAppFP_Type()
)
nsCommonSystemSwVersionAppFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonSystemSwVersionAppFP.setStatus("current")


class _NsCommonSystemSwVersionAppCLI_Type(DisplayString):
    """Custom type nsCommonSystemSwVersionAppCLI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonSystemSwVersionAppCLI_Type.__name__ = "DisplayString"
_NsCommonSystemSwVersionAppCLI_Object = MibTableColumn
nsCommonSystemSwVersionAppCLI = _NsCommonSystemSwVersionAppCLI_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 1, 5, 1, 4),
    _NsCommonSystemSwVersionAppCLI_Type()
)
nsCommonSystemSwVersionAppCLI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonSystemSwVersionAppCLI.setStatus("current")


class _NsCommonSystemSwVersionAppNsmd_Type(DisplayString):
    """Custom type nsCommonSystemSwVersionAppNsmd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonSystemSwVersionAppNsmd_Type.__name__ = "DisplayString"
_NsCommonSystemSwVersionAppNsmd_Object = MibTableColumn
nsCommonSystemSwVersionAppNsmd = _NsCommonSystemSwVersionAppNsmd_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 1, 5, 1, 5),
    _NsCommonSystemSwVersionAppNsmd_Type()
)
nsCommonSystemSwVersionAppNsmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonSystemSwVersionAppNsmd.setStatus("current")


class _NsCommonSystemSwVersionAppPIC_Type(DisplayString):
    """Custom type nsCommonSystemSwVersionAppPIC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonSystemSwVersionAppPIC_Type.__name__ = "DisplayString"
_NsCommonSystemSwVersionAppPIC_Object = MibTableColumn
nsCommonSystemSwVersionAppPIC = _NsCommonSystemSwVersionAppPIC_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 1, 5, 1, 6),
    _NsCommonSystemSwVersionAppPIC_Type()
)
nsCommonSystemSwVersionAppPIC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonSystemSwVersionAppPIC.setStatus("current")
_NsCommonSystemHwConfig_ObjectIdentity = ObjectIdentity
nsCommonSystemHwConfig = _NsCommonSystemHwConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 2)
)
if mibBuilder.loadTexts:
    nsCommonSystemHwConfig.setStatus("current")


class _NsCommonSystemHwConfigProductType_Type(DisplayString):
    """Custom type nsCommonSystemHwConfigProductType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonSystemHwConfigProductType_Type.__name__ = "DisplayString"
_NsCommonSystemHwConfigProductType_Object = MibScalar
nsCommonSystemHwConfigProductType = _NsCommonSystemHwConfigProductType_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 2, 1),
    _NsCommonSystemHwConfigProductType_Type()
)
nsCommonSystemHwConfigProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonSystemHwConfigProductType.setStatus("current")


class _NsCommonSystemHwConfigSerialNumber_Type(DisplayString):
    """Custom type nsCommonSystemHwConfigSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonSystemHwConfigSerialNumber_Type.__name__ = "DisplayString"
_NsCommonSystemHwConfigSerialNumber_Object = MibScalar
nsCommonSystemHwConfigSerialNumber = _NsCommonSystemHwConfigSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 2, 2),
    _NsCommonSystemHwConfigSerialNumber_Type()
)
nsCommonSystemHwConfigSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonSystemHwConfigSerialNumber.setStatus("current")


class _NsCommonSystemHwConfigHardwareVersion_Type(DisplayString):
    """Custom type nsCommonSystemHwConfigHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonSystemHwConfigHardwareVersion_Type.__name__ = "DisplayString"
_NsCommonSystemHwConfigHardwareVersion_Object = MibScalar
nsCommonSystemHwConfigHardwareVersion = _NsCommonSystemHwConfigHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 2, 3),
    _NsCommonSystemHwConfigHardwareVersion_Type()
)
nsCommonSystemHwConfigHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonSystemHwConfigHardwareVersion.setStatus("current")


class _NsCommonSystemHwConfigMacAddress_Type(DisplayString):
    """Custom type nsCommonSystemHwConfigMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonSystemHwConfigMacAddress_Type.__name__ = "DisplayString"
_NsCommonSystemHwConfigMacAddress_Object = MibScalar
nsCommonSystemHwConfigMacAddress = _NsCommonSystemHwConfigMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 2, 4),
    _NsCommonSystemHwConfigMacAddress_Type()
)
nsCommonSystemHwConfigMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonSystemHwConfigMacAddress.setStatus("current")


class _NsCommonSystemHwConfigInternalClockType_Type(DisplayString):
    """Custom type nsCommonSystemHwConfigInternalClockType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonSystemHwConfigInternalClockType_Type.__name__ = "DisplayString"
_NsCommonSystemHwConfigInternalClockType_Object = MibScalar
nsCommonSystemHwConfigInternalClockType = _NsCommonSystemHwConfigInternalClockType_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 2, 5),
    _NsCommonSystemHwConfigInternalClockType_Type()
)
nsCommonSystemHwConfigInternalClockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonSystemHwConfigInternalClockType.setStatus("current")
_NsCommonSystemHwConfigCardTable_Object = MibTable
nsCommonSystemHwConfigCardTable = _NsCommonSystemHwConfigCardTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 2, 6)
)
if mibBuilder.loadTexts:
    nsCommonSystemHwConfigCardTable.setStatus("current")
_NsCommonSystemHwConfigCardEntry_Object = MibTableRow
nsCommonSystemHwConfigCardEntry = _NsCommonSystemHwConfigCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 2, 6, 1)
)
nsCommonSystemHwConfigCardEntry.setIndexNames(
    (0, "NOVELSAT-COMMON-MIB", "nsCommonSystemHwConfigCardID"),
)
if mibBuilder.loadTexts:
    nsCommonSystemHwConfigCardEntry.setStatus("current")
_NsCommonSystemHwConfigCardID_Type = Unsigned32
_NsCommonSystemHwConfigCardID_Object = MibTableColumn
nsCommonSystemHwConfigCardID = _NsCommonSystemHwConfigCardID_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 2, 6, 1, 1),
    _NsCommonSystemHwConfigCardID_Type()
)
nsCommonSystemHwConfigCardID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonSystemHwConfigCardID.setStatus("current")


class _NsCommonSystemHwConfigCardType_Type(DisplayString):
    """Custom type nsCommonSystemHwConfigCardType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonSystemHwConfigCardType_Type.__name__ = "DisplayString"
_NsCommonSystemHwConfigCardType_Object = MibTableColumn
nsCommonSystemHwConfigCardType = _NsCommonSystemHwConfigCardType_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 2, 6, 1, 2),
    _NsCommonSystemHwConfigCardType_Type()
)
nsCommonSystemHwConfigCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonSystemHwConfigCardType.setStatus("current")


class _NsCommonSystemHwConfigCardSerialNumber_Type(DisplayString):
    """Custom type nsCommonSystemHwConfigCardSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonSystemHwConfigCardSerialNumber_Type.__name__ = "DisplayString"
_NsCommonSystemHwConfigCardSerialNumber_Object = MibTableColumn
nsCommonSystemHwConfigCardSerialNumber = _NsCommonSystemHwConfigCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 2, 6, 1, 3),
    _NsCommonSystemHwConfigCardSerialNumber_Type()
)
nsCommonSystemHwConfigCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonSystemHwConfigCardSerialNumber.setStatus("current")


class _NsCommonSystemHwConfigCardHwVersion_Type(DisplayString):
    """Custom type nsCommonSystemHwConfigCardHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonSystemHwConfigCardHwVersion_Type.__name__ = "DisplayString"
_NsCommonSystemHwConfigCardHwVersion_Object = MibTableColumn
nsCommonSystemHwConfigCardHwVersion = _NsCommonSystemHwConfigCardHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 2, 6, 1, 4),
    _NsCommonSystemHwConfigCardHwVersion_Type()
)
nsCommonSystemHwConfigCardHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonSystemHwConfigCardHwVersion.setStatus("current")


class _NsCommonSystemHwConfigCardSwVersion_Type(DisplayString):
    """Custom type nsCommonSystemHwConfigCardSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonSystemHwConfigCardSwVersion_Type.__name__ = "DisplayString"
_NsCommonSystemHwConfigCardSwVersion_Object = MibTableColumn
nsCommonSystemHwConfigCardSwVersion = _NsCommonSystemHwConfigCardSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 2, 6, 1, 5),
    _NsCommonSystemHwConfigCardSwVersion_Type()
)
nsCommonSystemHwConfigCardSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonSystemHwConfigCardSwVersion.setStatus("current")


class _NsCommonSystemHwConfigBUCFeeder_Type(DisplayString):
    """Custom type nsCommonSystemHwConfigBUCFeeder based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonSystemHwConfigBUCFeeder_Type.__name__ = "DisplayString"
_NsCommonSystemHwConfigBUCFeeder_Object = MibScalar
nsCommonSystemHwConfigBUCFeeder = _NsCommonSystemHwConfigBUCFeeder_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 2, 7),
    _NsCommonSystemHwConfigBUCFeeder_Type()
)
nsCommonSystemHwConfigBUCFeeder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonSystemHwConfigBUCFeeder.setStatus("current")
_NsCommonSystemSwUpdate_ObjectIdentity = ObjectIdentity
nsCommonSystemSwUpdate = _NsCommonSystemSwUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 3)
)
if mibBuilder.loadTexts:
    nsCommonSystemSwUpdate.setStatus("current")
_NsCommonSystemSwUpdateServerIP_Type = IpAddress
_NsCommonSystemSwUpdateServerIP_Object = MibScalar
nsCommonSystemSwUpdateServerIP = _NsCommonSystemSwUpdateServerIP_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 3, 1),
    _NsCommonSystemSwUpdateServerIP_Type()
)
nsCommonSystemSwUpdateServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonSystemSwUpdateServerIP.setStatus("current")


class _NsCommonSystemSwUpdateUserName_Type(DisplayString):
    """Custom type nsCommonSystemSwUpdateUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonSystemSwUpdateUserName_Type.__name__ = "DisplayString"
_NsCommonSystemSwUpdateUserName_Object = MibScalar
nsCommonSystemSwUpdateUserName = _NsCommonSystemSwUpdateUserName_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 3, 2),
    _NsCommonSystemSwUpdateUserName_Type()
)
nsCommonSystemSwUpdateUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonSystemSwUpdateUserName.setStatus("current")


class _NsCommonSystemSwUpdatePassword_Type(DisplayString):
    """Custom type nsCommonSystemSwUpdatePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonSystemSwUpdatePassword_Type.__name__ = "DisplayString"
_NsCommonSystemSwUpdatePassword_Object = MibScalar
nsCommonSystemSwUpdatePassword = _NsCommonSystemSwUpdatePassword_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 3, 3),
    _NsCommonSystemSwUpdatePassword_Type()
)
nsCommonSystemSwUpdatePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonSystemSwUpdatePassword.setStatus("current")


class _NsCommonSystemSwUpdateFileName_Type(DisplayString):
    """Custom type nsCommonSystemSwUpdateFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonSystemSwUpdateFileName_Type.__name__ = "DisplayString"
_NsCommonSystemSwUpdateFileName_Object = MibScalar
nsCommonSystemSwUpdateFileName = _NsCommonSystemSwUpdateFileName_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 3, 4),
    _NsCommonSystemSwUpdateFileName_Type()
)
nsCommonSystemSwUpdateFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonSystemSwUpdateFileName.setStatus("current")


class _NsCommonSystemSwUpdateCmd_Type(Integer32):
    """Custom type nsCommonSystemSwUpdateCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("execute", 1),
          ("none", 0),
          ("notApplicable", 255))
    )


_NsCommonSystemSwUpdateCmd_Type.__name__ = "Integer32"
_NsCommonSystemSwUpdateCmd_Object = MibScalar
nsCommonSystemSwUpdateCmd = _NsCommonSystemSwUpdateCmd_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 3, 5),
    _NsCommonSystemSwUpdateCmd_Type()
)
nsCommonSystemSwUpdateCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonSystemSwUpdateCmd.setStatus("current")


class _NsCommonSystemSwUpdateComplete_Type(Integer32):
    """Custom type nsCommonSystemSwUpdateComplete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("inProgress", 1))
    )


_NsCommonSystemSwUpdateComplete_Type.__name__ = "Integer32"
_NsCommonSystemSwUpdateComplete_Object = MibScalar
nsCommonSystemSwUpdateComplete = _NsCommonSystemSwUpdateComplete_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 3, 6),
    _NsCommonSystemSwUpdateComplete_Type()
)
nsCommonSystemSwUpdateComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonSystemSwUpdateComplete.setStatus("current")


class _NsCommonSystemSwUpdateStatus_Type(Integer32):
    """Custom type nsCommonSystemSwUpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("notApplicable", 255),
          ("ok", 0))
    )


_NsCommonSystemSwUpdateStatus_Type.__name__ = "Integer32"
_NsCommonSystemSwUpdateStatus_Object = MibScalar
nsCommonSystemSwUpdateStatus = _NsCommonSystemSwUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 3, 7),
    _NsCommonSystemSwUpdateStatus_Type()
)
nsCommonSystemSwUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonSystemSwUpdateStatus.setStatus("current")


class _NsCommonSystemSwActivateBackupCmd_Type(Integer32):
    """Custom type nsCommonSystemSwActivateBackupCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("execute", 1),
          ("none", 0),
          ("notApplicable", 255))
    )


_NsCommonSystemSwActivateBackupCmd_Type.__name__ = "Integer32"
_NsCommonSystemSwActivateBackupCmd_Object = MibScalar
nsCommonSystemSwActivateBackupCmd = _NsCommonSystemSwActivateBackupCmd_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 3, 8),
    _NsCommonSystemSwActivateBackupCmd_Type()
)
nsCommonSystemSwActivateBackupCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonSystemSwActivateBackupCmd.setStatus("current")
_NsCommonSystemDatabase_ObjectIdentity = ObjectIdentity
nsCommonSystemDatabase = _NsCommonSystemDatabase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 4)
)
if mibBuilder.loadTexts:
    nsCommonSystemDatabase.setStatus("current")


class _NsCommonSystemDatabaseCmdDbName_Type(DisplayString):
    """Custom type nsCommonSystemDatabaseCmdDbName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonSystemDatabaseCmdDbName_Type.__name__ = "DisplayString"
_NsCommonSystemDatabaseCmdDbName_Object = MibScalar
nsCommonSystemDatabaseCmdDbName = _NsCommonSystemDatabaseCmdDbName_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 4, 1),
    _NsCommonSystemDatabaseCmdDbName_Type()
)
nsCommonSystemDatabaseCmdDbName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonSystemDatabaseCmdDbName.setStatus("current")
_NsCommonSystemDatabaseServerIP_Type = IpAddress
_NsCommonSystemDatabaseServerIP_Object = MibScalar
nsCommonSystemDatabaseServerIP = _NsCommonSystemDatabaseServerIP_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 4, 2),
    _NsCommonSystemDatabaseServerIP_Type()
)
nsCommonSystemDatabaseServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonSystemDatabaseServerIP.setStatus("current")


class _NsCommonSystemDatabaseCmd_Type(Integer32):
    """Custom type nsCommonSystemDatabaseCmd based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("defaults", 4),
          ("delete", 3),
          ("download", 6),
          ("load", 2),
          ("none", 0),
          ("notApplicable", 255),
          ("save", 1),
          ("upload", 5))
    )


_NsCommonSystemDatabaseCmd_Type.__name__ = "Integer32"
_NsCommonSystemDatabaseCmd_Object = MibScalar
nsCommonSystemDatabaseCmd = _NsCommonSystemDatabaseCmd_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 4, 3),
    _NsCommonSystemDatabaseCmd_Type()
)
nsCommonSystemDatabaseCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsCommonSystemDatabaseCmd.setStatus("current")
_NsCommonSystemDatabaseTable_Object = MibTable
nsCommonSystemDatabaseTable = _NsCommonSystemDatabaseTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 4, 4)
)
if mibBuilder.loadTexts:
    nsCommonSystemDatabaseTable.setStatus("current")
_NsCommonSystemDatabaseEntry_Object = MibTableRow
nsCommonSystemDatabaseEntry = _NsCommonSystemDatabaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 4, 4, 1)
)
nsCommonSystemDatabaseEntry.setIndexNames(
    (0, "NOVELSAT-COMMON-MIB", "nsCommonSystemDatabaseID"),
)
if mibBuilder.loadTexts:
    nsCommonSystemDatabaseEntry.setStatus("current")
_NsCommonSystemDatabaseID_Type = Unsigned32
_NsCommonSystemDatabaseID_Object = MibTableColumn
nsCommonSystemDatabaseID = _NsCommonSystemDatabaseID_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 4, 4, 1, 1),
    _NsCommonSystemDatabaseID_Type()
)
nsCommonSystemDatabaseID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonSystemDatabaseID.setStatus("current")


class _NsCommonSystemDatabaseName_Type(DisplayString):
    """Custom type nsCommonSystemDatabaseName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonSystemDatabaseName_Type.__name__ = "DisplayString"
_NsCommonSystemDatabaseName_Object = MibTableColumn
nsCommonSystemDatabaseName = _NsCommonSystemDatabaseName_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 4, 4, 1, 2),
    _NsCommonSystemDatabaseName_Type()
)
nsCommonSystemDatabaseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonSystemDatabaseName.setStatus("current")
_NsCommonSystemLicense_ObjectIdentity = ObjectIdentity
nsCommonSystemLicense = _NsCommonSystemLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 5)
)
if mibBuilder.loadTexts:
    nsCommonSystemLicense.setStatus("current")
_NsCommonSystemLicenseIssueDate_Type = DisplayString
_NsCommonSystemLicenseIssueDate_Object = MibScalar
nsCommonSystemLicenseIssueDate = _NsCommonSystemLicenseIssueDate_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 5, 1),
    _NsCommonSystemLicenseIssueDate_Type()
)
nsCommonSystemLicenseIssueDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonSystemLicenseIssueDate.setStatus("current")
_NsCommonSystemLicenseID_Type = Integer32
_NsCommonSystemLicenseID_Object = MibScalar
nsCommonSystemLicenseID = _NsCommonSystemLicenseID_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 5, 2),
    _NsCommonSystemLicenseID_Type()
)
nsCommonSystemLicenseID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonSystemLicenseID.setStatus("current")
_NsCommonSystemLicenseFeaturesTable_Object = MibTable
nsCommonSystemLicenseFeaturesTable = _NsCommonSystemLicenseFeaturesTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 5, 3)
)
if mibBuilder.loadTexts:
    nsCommonSystemLicenseFeaturesTable.setStatus("current")
_NsCommonSystemLicenseFeaturesEntry_Object = MibTableRow
nsCommonSystemLicenseFeaturesEntry = _NsCommonSystemLicenseFeaturesEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 5, 3, 1)
)
nsCommonSystemLicenseFeaturesEntry.setIndexNames(
    (0, "NOVELSAT-COMMON-MIB", "nsCommonSystemLicenseFeatureIndx"),
)
if mibBuilder.loadTexts:
    nsCommonSystemLicenseFeaturesEntry.setStatus("current")
_NsCommonSystemLicenseFeatureIndx_Type = Unsigned32
_NsCommonSystemLicenseFeatureIndx_Object = MibTableColumn
nsCommonSystemLicenseFeatureIndx = _NsCommonSystemLicenseFeatureIndx_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 5, 3, 1, 1),
    _NsCommonSystemLicenseFeatureIndx_Type()
)
nsCommonSystemLicenseFeatureIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsCommonSystemLicenseFeatureIndx.setStatus("current")


class _NsCommonSystemLicenseFeatureName_Type(DisplayString):
    """Custom type nsCommonSystemLicenseFeatureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsCommonSystemLicenseFeatureName_Type.__name__ = "DisplayString"
_NsCommonSystemLicenseFeatureName_Object = MibTableColumn
nsCommonSystemLicenseFeatureName = _NsCommonSystemLicenseFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 5, 3, 1, 2),
    _NsCommonSystemLicenseFeatureName_Type()
)
nsCommonSystemLicenseFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonSystemLicenseFeatureName.setStatus("current")


class _NsCommonSystemLicenseFeatureType_Type(Integer32):
    """Custom type nsCommonSystemLicenseFeatureType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notExist", 0),
          ("permanent", 1),
          ("temporary", 2))
    )


_NsCommonSystemLicenseFeatureType_Type.__name__ = "Integer32"
_NsCommonSystemLicenseFeatureType_Object = MibTableColumn
nsCommonSystemLicenseFeatureType = _NsCommonSystemLicenseFeatureType_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 5, 3, 1, 3),
    _NsCommonSystemLicenseFeatureType_Type()
)
nsCommonSystemLicenseFeatureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonSystemLicenseFeatureType.setStatus("current")
_NsCommonSystemLicenseFeatureDaysLeft_Type = Integer32
_NsCommonSystemLicenseFeatureDaysLeft_Object = MibTableColumn
nsCommonSystemLicenseFeatureDaysLeft = _NsCommonSystemLicenseFeatureDaysLeft_Object(
    (1, 3, 6, 1, 4, 1, 37576, 2, 3, 5, 3, 1, 4),
    _NsCommonSystemLicenseFeatureDaysLeft_Type()
)
nsCommonSystemLicenseFeatureDaysLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsCommonSystemLicenseFeatureDaysLeft.setStatus("current")
_NsCommonProducts_ObjectIdentity = ObjectIdentity
nsCommonProducts = _NsCommonProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 4)
)
if mibBuilder.loadTexts:
    nsCommonProducts.setStatus("current")
_NsNS1000_ObjectIdentity = ObjectIdentity
nsNS1000 = _NsNS1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 4, 1)
)
_NsNS2000_ObjectIdentity = ObjectIdentity
nsNS2000 = _NsNS2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 4, 2)
)
_NsNS3000_ObjectIdentity = ObjectIdentity
nsNS3000 = _NsNS3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 2, 4, 3)
)

# Managed Objects groups


# Notification objects

nsCommonMonitorEventNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 37576, 2, 2, 0, 1)
)
nsCommonMonitorEventNotification.setObjects(
      *(("NOVELSAT-COMMON-MIB", "nsCommonMonitorEventsDateAndTime"),
        ("NOVELSAT-COMMON-MIB", "nsCommonMonitorEventsType"),
        ("NOVELSAT-COMMON-MIB", "nsCommonMonitorEventsSeverity"),
        ("NOVELSAT-COMMON-MIB", "nsCommonMonitorEventsSource"),
        ("NOVELSAT-COMMON-MIB", "nsCommonMonitorEventsEvent"),
        ("NOVELSAT-COMMON-MIB", "nsCommonMonitorEventsDescription"))
)
if mibBuilder.loadTexts:
    nsCommonMonitorEventNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOVELSAT-COMMON-MIB",
    **{"nsCommon": nsCommon,
       "nsCommonConfig": nsCommonConfig,
       "nsCommonConfigManagementIP": nsCommonConfigManagementIP,
       "nsCommonConfigMgmtHostIP": nsCommonConfigMgmtHostIP,
       "nsCommonConfigMgmtHostMask": nsCommonConfigMgmtHostMask,
       "nsCommonConfigMgmtHostGW": nsCommonConfigMgmtHostGW,
       "nsCommonConfigMgmtHostDHCP": nsCommonConfigMgmtHostDHCP,
       "nsCommonConfigMgmtHostDNS": nsCommonConfigMgmtHostDNS,
       "nsCommonConfig10MhzClock": nsCommonConfig10MhzClock,
       "nsCommonConfig10MhzClockSource": nsCommonConfig10MhzClockSource,
       "nsCommonConfig10MhzClockOut": nsCommonConfig10MhzClockOut,
       "nsCommonConfig10MhzClockTxPortClock": nsCommonConfig10MhzClockTxPortClock,
       "nsCommonConfig10MhzClockLnbRefClock": nsCommonConfig10MhzClockLnbRefClock,
       "nsCommonConfigSerialPort": nsCommonConfigSerialPort,
       "nsCommonConfigSerialPortBaudRate": nsCommonConfigSerialPortBaudRate,
       "nsCommonConfigSerialPortParity": nsCommonConfigSerialPortParity,
       "nsCommonConfigSerialPortDataBits": nsCommonConfigSerialPortDataBits,
       "nsCommonConfigSerialPortStopBit": nsCommonConfigSerialPortStopBit,
       "nsCommonConfigDateTime": nsCommonConfigDateTime,
       "nsCommonConfigDateAndTime": nsCommonConfigDateAndTime,
       "nsCommonConfigNetwork": nsCommonConfigNetwork,
       "nsCommonConfigNetworkForwardingMode": nsCommonConfigNetworkForwardingMode,
       "nsCommonConfigNetworkMode": nsCommonConfigNetworkMode,
       "nsCommonConfigNetworkInterfaces": nsCommonConfigNetworkInterfaces,
       "nsCommonConfigNetworkInterfacesTable": nsCommonConfigNetworkInterfacesTable,
       "nsCommonConfigNetworkInterfacesEntry": nsCommonConfigNetworkInterfacesEntry,
       "nsCommonConfigNetworkInterfacesIndex": nsCommonConfigNetworkInterfacesIndex,
       "nsCommonConfigNetworkInterfacesName": nsCommonConfigNetworkInterfacesName,
       "nsCommonConfigNetworkInterfacesAdminStatus": nsCommonConfigNetworkInterfacesAdminStatus,
       "nsCommonConfigNetworkInterfacesPortType": nsCommonConfigNetworkInterfacesPortType,
       "nsCommonConfigNetworkInterfacesMtu": nsCommonConfigNetworkInterfacesMtu,
       "nsCommonConfigNetworkInterfacesVlan": nsCommonConfigNetworkInterfacesVlan,
       "nsCommonConfigNetworkInterfacesIp": nsCommonConfigNetworkInterfacesIp,
       "nsCommonConfigNetworkInterfacesMac": nsCommonConfigNetworkInterfacesMac,
       "nsCommonConfigNetworkInterfacesSubnetMask": nsCommonConfigNetworkInterfacesSubnetMask,
       "nsCommonConfigNetworkInterfacesEncapsulation": nsCommonConfigNetworkInterfacesEncapsulation,
       "nsCommonConfigNetworkInterfacesManagementControl": nsCommonConfigNetworkInterfacesManagementControl,
       "nsCommonConfigNetworkInterfacesAcmControl": nsCommonConfigNetworkInterfacesAcmControl,
       "nsCommonConfigNetworkInterfacesNotifyRowStatus": nsCommonConfigNetworkInterfacesNotifyRowStatus,
       "nsCommonConfigNetworkNeighbors": nsCommonConfigNetworkNeighbors,
       "nsCommonConfigNetworkNeighborsTable": nsCommonConfigNetworkNeighborsTable,
       "nsCommonConfigNetworkNeighborsEntry": nsCommonConfigNetworkNeighborsEntry,
       "nsCommonConfigNetworkNeighborsIndex": nsCommonConfigNetworkNeighborsIndex,
       "nsCommonConfigNetworkNeighborsName": nsCommonConfigNetworkNeighborsName,
       "nsCommonConfigNetworkNeighborsIfIndex": nsCommonConfigNetworkNeighborsIfIndex,
       "nsCommonConfigNetworkNeighborsIp": nsCommonConfigNetworkNeighborsIp,
       "nsCommonConfigNetworkNeighborsMac": nsCommonConfigNetworkNeighborsMac,
       "nsCommonConfigNetworkNeighborsSignalingIp": nsCommonConfigNetworkNeighborsSignalingIp,
       "nsCommonConfigNetworkNeighborsModulation": nsCommonConfigNetworkNeighborsModulation,
       "nsCommonConfigNetworkNeighborsFecRate": nsCommonConfigNetworkNeighborsFecRate,
       "nsCommonConfigNetworkNeighborsNotifyRowStatus": nsCommonConfigNetworkNeighborsNotifyRowStatus,
       "nsCommonConfigNetworkRouting": nsCommonConfigNetworkRouting,
       "nsCommonConfigNetworkPolicyRoute": nsCommonConfigNetworkPolicyRoute,
       "nsCommonConfigNetworkPolicyRouteTable": nsCommonConfigNetworkPolicyRouteTable,
       "nsCommonConfigNetworkPolicyRouteEntry": nsCommonConfigNetworkPolicyRouteEntry,
       "nsCommonConfigNetworkPolicyRouteIndex": nsCommonConfigNetworkPolicyRouteIndex,
       "nsCommonConfigNetworkPolicyRouteInputInterfaceId": nsCommonConfigNetworkPolicyRouteInputInterfaceId,
       "nsCommonConfigNetworkPolicyRouteRoutingTableId": nsCommonConfigNetworkPolicyRouteRoutingTableId,
       "nsCommonConfigNetworkPolicyRouteNotifyRowStatus": nsCommonConfigNetworkPolicyRouteNotifyRowStatus,
       "nsCommonConfigNetworkRoutes": nsCommonConfigNetworkRoutes,
       "nsCommonConfigNetworkRoutesTable": nsCommonConfigNetworkRoutesTable,
       "nsCommonConfigNetworkRoutesEntry": nsCommonConfigNetworkRoutesEntry,
       "nsCommonConfigNetworkRoutesDestIpAddress": nsCommonConfigNetworkRoutesDestIpAddress,
       "nsCommonConfigNetworkRoutesDestSubnetMask": nsCommonConfigNetworkRoutesDestSubnetMask,
       "nsCommonConfigNetworkRoutesNexthopIpAddress": nsCommonConfigNetworkRoutesNexthopIpAddress,
       "nsCommonConfigNetworkRoutesTableId": nsCommonConfigNetworkRoutesTableId,
       "nsCommonConfigNetworkRoutesAdminStatus": nsCommonConfigNetworkRoutesAdminStatus,
       "nsCommonConfigNetworkRoutesNotifyRowStatus": nsCommonConfigNetworkRoutesNotifyRowStatus,
       "nsCommonConfigNetworkVlanSwitching": nsCommonConfigNetworkVlanSwitching,
       "nsCommonConfigNetworkVlanSwitchingTable": nsCommonConfigNetworkVlanSwitchingTable,
       "nsCommonConfigNetworkVlanSwitchingEntry": nsCommonConfigNetworkVlanSwitchingEntry,
       "nsCommonConfigNetworkVlanSwitchingVid": nsCommonConfigNetworkVlanSwitchingVid,
       "nsCommonConfigNetworkVlanSwitchingNeighborIndex": nsCommonConfigNetworkVlanSwitchingNeighborIndex,
       "nsCommonConfigNetworkVlanSwitchingAdminStatus": nsCommonConfigNetworkVlanSwitchingAdminStatus,
       "nsCommonConfigNetworkVlanSwitchingNotifyRowStatus": nsCommonConfigNetworkVlanSwitchingNotifyRowStatus,
       "nsCommonConfigNetworkQoS": nsCommonConfigNetworkQoS,
       "nsCommonConfigNetworkClassification": nsCommonConfigNetworkClassification,
       "nsCommonConfigNetworkClassificationMode": nsCommonConfigNetworkClassificationMode,
       "nsCommonConfigNetworkClassification802": nsCommonConfigNetworkClassification802,
       "nsCommonConfigNetworkClassification802Table": nsCommonConfigNetworkClassification802Table,
       "nsCommonConfigNetworkClassification802Entry": nsCommonConfigNetworkClassification802Entry,
       "nsCommonConfigNetworkClassification802Priority": nsCommonConfigNetworkClassification802Priority,
       "nsCommonConfigNetworkClassification802CoS": nsCommonConfigNetworkClassification802CoS,
       "nsCommonConfigNetworkClassificationTos": nsCommonConfigNetworkClassificationTos,
       "nsCommonConfigNetworkClassificationTosTable": nsCommonConfigNetworkClassificationTosTable,
       "nsCommonConfigNetworkClassificationTosEntry": nsCommonConfigNetworkClassificationTosEntry,
       "nsCommonConfigNetworkClassificationTosPriority": nsCommonConfigNetworkClassificationTosPriority,
       "nsCommonConfigNetworkClassificationTosFieldValue": nsCommonConfigNetworkClassificationTosFieldValue,
       "nsCommonConfigNetworkClassificationTosFieldMask": nsCommonConfigNetworkClassificationTosFieldMask,
       "nsCommonConfigNetworkClassificationTosCoS": nsCommonConfigNetworkClassificationTosCoS,
       "nsCommonConfigNetworkClassificationTosNotifyRowStatus": nsCommonConfigNetworkClassificationTosNotifyRowStatus,
       "nsCommonConfigNetworkClassificationTosColor": nsCommonConfigNetworkClassificationTosColor,
       "nsCommonConfigNetworkClassificationMf": nsCommonConfigNetworkClassificationMf,
       "nsCommonConfigNetworkClassificationMfTable": nsCommonConfigNetworkClassificationMfTable,
       "nsCommonConfigNetworkClassificationMfEntry": nsCommonConfigNetworkClassificationMfEntry,
       "nsCommonConfigNetworkClassificationMfPriority": nsCommonConfigNetworkClassificationMfPriority,
       "nsCommonConfigNetworkClassificationMfName": nsCommonConfigNetworkClassificationMfName,
       "nsCommonConfigNetworkClassificationMfAdminStatus": nsCommonConfigNetworkClassificationMfAdminStatus,
       "nsCommonConfigNetworkClassificationMfVidHigh": nsCommonConfigNetworkClassificationMfVidHigh,
       "nsCommonConfigNetworkClassificationMfVidLow": nsCommonConfigNetworkClassificationMfVidLow,
       "nsCommonConfigNetworkClassificationMfSrcIpAddressHigh": nsCommonConfigNetworkClassificationMfSrcIpAddressHigh,
       "nsCommonConfigNetworkClassificationMfSrcIpAddressLow": nsCommonConfigNetworkClassificationMfSrcIpAddressLow,
       "nsCommonConfigNetworkClassificationMfDestIpAddressHigh": nsCommonConfigNetworkClassificationMfDestIpAddressHigh,
       "nsCommonConfigNetworkClassificationMfDestIpAddressLow": nsCommonConfigNetworkClassificationMfDestIpAddressLow,
       "nsCommonConfigNetworkClassificationMfProtocolStatus": nsCommonConfigNetworkClassificationMfProtocolStatus,
       "nsCommonConfigNetworkClassificationMfProtocol": nsCommonConfigNetworkClassificationMfProtocol,
       "nsCommonConfigNetworkClassificationMfSrcPortHigh": nsCommonConfigNetworkClassificationMfSrcPortHigh,
       "nsCommonConfigNetworkClassificationMfSrcPortLow": nsCommonConfigNetworkClassificationMfSrcPortLow,
       "nsCommonConfigNetworkClassificationMfDestPortHigh": nsCommonConfigNetworkClassificationMfDestPortHigh,
       "nsCommonConfigNetworkClassificationMfDestPortLow": nsCommonConfigNetworkClassificationMfDestPortLow,
       "nsCommonConfigNetworkClassificationMfCoS": nsCommonConfigNetworkClassificationMfCoS,
       "nsCommonConfigNetworkClassificationMfNotifyRowStatus": nsCommonConfigNetworkClassificationMfNotifyRowStatus,
       "nsCommonConfigNetworkQueues": nsCommonConfigNetworkQueues,
       "nsCommonConfigNetworkQueuesTable": nsCommonConfigNetworkQueuesTable,
       "nsCommonConfigNetworkQueuesEntry": nsCommonConfigNetworkQueuesEntry,
       "nsCommonConfigNetworkQueuesCos": nsCommonConfigNetworkQueuesCos,
       "nsCommonConfigNetworkQueuesSchedulingMethod": nsCommonConfigNetworkQueuesSchedulingMethod,
       "nsCommonConfigNetworkQueuesWeight": nsCommonConfigNetworkQueuesWeight,
       "nsCommonConfigNetworkQueuesQueueDepth": nsCommonConfigNetworkQueuesQueueDepth,
       "nsCommonConfigNetworkQueuesDropDiscipline": nsCommonConfigNetworkQueuesDropDiscipline,
       "nsCommonConfigNetworkRemoteScheduling": nsCommonConfigNetworkRemoteScheduling,
       "nsCommonConfigNetworkRemoteSchedulingMethod": nsCommonConfigNetworkRemoteSchedulingMethod,
       "nsCommonConfigNetworkRemoteSchedulingFrameMerging": nsCommonConfigNetworkRemoteSchedulingFrameMerging,
       "nsCommonConfigNetworkRemoteSchedulingCosSignificance": nsCommonConfigNetworkRemoteSchedulingCosSignificance,
       "nsCommonConfigNetworkBwManagement": nsCommonConfigNetworkBwManagement,
       "nsCommonConfigNetworkBwManagementTable": nsCommonConfigNetworkBwManagementTable,
       "nsCommonConfigNetworkBwManagementEntry": nsCommonConfigNetworkBwManagementEntry,
       "nsCommonConfigNetworkBwManagementIndex": nsCommonConfigNetworkBwManagementIndex,
       "nsCommonConfigNetworkBwManagementNeighborIndex": nsCommonConfigNetworkBwManagementNeighborIndex,
       "nsCommonConfigNetworkBwManagementAdminStatus": nsCommonConfigNetworkBwManagementAdminStatus,
       "nsCommonConfigNetworkBwManagementCIR": nsCommonConfigNetworkBwManagementCIR,
       "nsCommonConfigNetworkBwManagementCBS": nsCommonConfigNetworkBwManagementCBS,
       "nsCommonConfigNetworkBwManagementEIR": nsCommonConfigNetworkBwManagementEIR,
       "nsCommonConfigNetworkBwManagementEBS": nsCommonConfigNetworkBwManagementEBS,
       "nsCommonConfigNetworkBwManagementRefModulation": nsCommonConfigNetworkBwManagementRefModulation,
       "nsCommonConfigNetworkBwManagementRefFecRate": nsCommonConfigNetworkBwManagementRefFecRate,
       "nsCommonConfigNetworkBwManagementPercentage": nsCommonConfigNetworkBwManagementPercentage,
       "nsCommonConfigNetworkBwManagementNotifyRowStatus": nsCommonConfigNetworkBwManagementNotifyRowStatus,
       "nsCommonConfigManagementOta": nsCommonConfigManagementOta,
       "nsCommonConfigMgmtOtaIP": nsCommonConfigMgmtOtaIP,
       "nsCommonConfigMgmtOtaMask": nsCommonConfigMgmtOtaMask,
       "nsCommonConfigManagementRollback": nsCommonConfigManagementRollback,
       "nsCommonConfigMgmtRollbackMode": nsCommonConfigMgmtRollbackMode,
       "nsCommonConfigMgmtRollbackTimeout": nsCommonConfigMgmtRollbackTimeout,
       "nsCommonConfigManagementRateLimiter": nsCommonConfigManagementRateLimiter,
       "nsCommonConfigMgmtRateLimit": nsCommonConfigMgmtRateLimit,
       "nsCommonConfigAlarmsEvents": nsCommonConfigAlarmsEvents,
       "nsCommonConfigAlarmsEventsTable": nsCommonConfigAlarmsEventsTable,
       "nsCommonConfigAlarmsEventsEntry": nsCommonConfigAlarmsEventsEntry,
       "nsCommonConfigAlarmsEventsIndex": nsCommonConfigAlarmsEventsIndex,
       "nsCommonConfigAlarmsEventsName": nsCommonConfigAlarmsEventsName,
       "nsCommonConfigAlarmsEventsMask": nsCommonConfigAlarmsEventsMask,
       "nsCommonConfigAlarmsEventsRelayMask": nsCommonConfigAlarmsEventsRelayMask,
       "nsCommonMonitor": nsCommonMonitor,
       "nsCommonMonitorNotifications": nsCommonMonitorNotifications,
       "nsCommonMonitorEventNotification": nsCommonMonitorEventNotification,
       "nsCommonMonitorAlarms": nsCommonMonitorAlarms,
       "nsCommonMonitorAlarmsTable": nsCommonMonitorAlarmsTable,
       "nsCommonMonitorAlarmsEntry": nsCommonMonitorAlarmsEntry,
       "nsCommonMonitorAlarmsUtcSecondsHigh": nsCommonMonitorAlarmsUtcSecondsHigh,
       "nsCommonMonitorAlarmsUtcSecondsLow": nsCommonMonitorAlarmsUtcSecondsLow,
       "nsCommonMonitorAlarmsUtcNanoSecondsHigh": nsCommonMonitorAlarmsUtcNanoSecondsHigh,
       "nsCommonMonitorAlarmsUtcNanoSecondsLow": nsCommonMonitorAlarmsUtcNanoSecondsLow,
       "nsCommonMonitorAlarmsDateAndTime": nsCommonMonitorAlarmsDateAndTime,
       "nsCommonMonitorAlarmsSeverity": nsCommonMonitorAlarmsSeverity,
       "nsCommonMonitorAlarmsSource": nsCommonMonitorAlarmsSource,
       "nsCommonMonitorAlarmsEvent": nsCommonMonitorAlarmsEvent,
       "nsCommonMonitorAlarmsDescription": nsCommonMonitorAlarmsDescription,
       "nsCommonMonitorEvents": nsCommonMonitorEvents,
       "nsCommonMonitorEventsTable": nsCommonMonitorEventsTable,
       "nsCommonMonitorEventsEntry": nsCommonMonitorEventsEntry,
       "nsCommonMonitorEventsUtcSecondsHigh": nsCommonMonitorEventsUtcSecondsHigh,
       "nsCommonMonitorEventsUtcSecondsLow": nsCommonMonitorEventsUtcSecondsLow,
       "nsCommonMonitorEventsUtcNanoSecondsHigh": nsCommonMonitorEventsUtcNanoSecondsHigh,
       "nsCommonMonitorEventsUtcNanoSecondsLow": nsCommonMonitorEventsUtcNanoSecondsLow,
       "nsCommonMonitorEventsDateAndTime": nsCommonMonitorEventsDateAndTime,
       "nsCommonMonitorEventsType": nsCommonMonitorEventsType,
       "nsCommonMonitorEventsSeverity": nsCommonMonitorEventsSeverity,
       "nsCommonMonitorEventsSource": nsCommonMonitorEventsSource,
       "nsCommonMonitorEventsEvent": nsCommonMonitorEventsEvent,
       "nsCommonMonitorEventsDescription": nsCommonMonitorEventsDescription,
       "nsCommonMonitorVoltage": nsCommonMonitorVoltage,
       "nsCommonMonitorVoltageTable": nsCommonMonitorVoltageTable,
       "nsCommonMonitorVoltageEntry": nsCommonMonitorVoltageEntry,
       "nsCommonMonitorVoltageIndex": nsCommonMonitorVoltageIndex,
       "nsCommonMonitorVoltageName": nsCommonMonitorVoltageName,
       "nsCommonMonitorVoltageValue": nsCommonMonitorVoltageValue,
       "nsCommonMonitorPowerSupply": nsCommonMonitorPowerSupply,
       "nsCommonMonitorPowerSupplyTable": nsCommonMonitorPowerSupplyTable,
       "nsCommonMonitorPowerSupplyEntry": nsCommonMonitorPowerSupplyEntry,
       "nsCommonMonitorPowerSupplyIndex": nsCommonMonitorPowerSupplyIndex,
       "nsCommonMonitorPowerSupplyName": nsCommonMonitorPowerSupplyName,
       "nsCommonMonitorPowerSupplyValue": nsCommonMonitorPowerSupplyValue,
       "nsCommonMonitorNetwork": nsCommonMonitorNetwork,
       "nsCommonMonitorNetworkInterfaces": nsCommonMonitorNetworkInterfaces,
       "nsCommonMonitorNetworkInterfacesLanTable": nsCommonMonitorNetworkInterfacesLanTable,
       "nsCommonMonitorNetworkInterfacesLanEntry": nsCommonMonitorNetworkInterfacesLanEntry,
       "nsCommonMonitorNetworkInterfacesLanIndex": nsCommonMonitorNetworkInterfacesLanIndex,
       "nsCommonMonitorNetworkInterfacesLanName": nsCommonMonitorNetworkInterfacesLanName,
       "nsCommonMonitorNetworkInterfacesLanAdminStatus": nsCommonMonitorNetworkInterfacesLanAdminStatus,
       "nsCommonMonitorNetworkInterfacesLanOperStatus": nsCommonMonitorNetworkInterfacesLanOperStatus,
       "nsCommonMonitorNetworkInterfacesLanPort": nsCommonMonitorNetworkInterfacesLanPort,
       "nsCommonMonitorNetworkInterfacesLanVlan": nsCommonMonitorNetworkInterfacesLanVlan,
       "nsCommonMonitorNetworkInterfacesLanMacAddress": nsCommonMonitorNetworkInterfacesLanMacAddress,
       "nsCommonMonitorNetworkInterfacesLanIpAddress": nsCommonMonitorNetworkInterfacesLanIpAddress,
       "nsCommonMonitorNetworkInterfacesLanSubnetMask": nsCommonMonitorNetworkInterfacesLanSubnetMask,
       "nsCommonMonitorNetworkInterfacesSatTable": nsCommonMonitorNetworkInterfacesSatTable,
       "nsCommonMonitorNetworkInterfacesSatEntry": nsCommonMonitorNetworkInterfacesSatEntry,
       "nsCommonMonitorNetworkInterfacesSatIndex": nsCommonMonitorNetworkInterfacesSatIndex,
       "nsCommonMonitorNetworkInterfacesSatName": nsCommonMonitorNetworkInterfacesSatName,
       "nsCommonMonitorNetworkInterfacesSatAdminStatus": nsCommonMonitorNetworkInterfacesSatAdminStatus,
       "nsCommonMonitorNetworkInterfacesSatOperStatus": nsCommonMonitorNetworkInterfacesSatOperStatus,
       "nsCommonMonitorNetworkInterfacesSatPort": nsCommonMonitorNetworkInterfacesSatPort,
       "nsCommonMonitorNetworkInterfacesSatPid": nsCommonMonitorNetworkInterfacesSatPid,
       "nsCommonMonitorNetworkInterfacesSatMacAddress": nsCommonMonitorNetworkInterfacesSatMacAddress,
       "nsCommonMonitorNetworkInterfacesSatIpAddress": nsCommonMonitorNetworkInterfacesSatIpAddress,
       "nsCommonMonitorNetworkInterfacesSatSubnetMask": nsCommonMonitorNetworkInterfacesSatSubnetMask,
       "nsCommonMonitorNetworkInterfacesSatEncapsulation": nsCommonMonitorNetworkInterfacesSatEncapsulation,
       "nsCommonMonitorNetworkInterfaceStatisticsTable": nsCommonMonitorNetworkInterfaceStatisticsTable,
       "nsCommonMonitorNetworkInterfaceStatisticsEntry": nsCommonMonitorNetworkInterfaceStatisticsEntry,
       "nsCommonMonitorNetworkInterfaceStatisticsIndex": nsCommonMonitorNetworkInterfaceStatisticsIndex,
       "nsCommonMonitorNetworkInterfaceStatisticsMtu": nsCommonMonitorNetworkInterfaceStatisticsMtu,
       "nsCommonMonitorNetworkInterfaceStatisticsRxOk": nsCommonMonitorNetworkInterfaceStatisticsRxOk,
       "nsCommonMonitorNetworkInterfaceStatisticsRxError": nsCommonMonitorNetworkInterfaceStatisticsRxError,
       "nsCommonMonitorNetworkInterfaceStatisticsRxDrop": nsCommonMonitorNetworkInterfaceStatisticsRxDrop,
       "nsCommonMonitorNetworkInterfaceStatisticsRxOvr": nsCommonMonitorNetworkInterfaceStatisticsRxOvr,
       "nsCommonMonitorNetworkInterfaceStatisticsTxOk": nsCommonMonitorNetworkInterfaceStatisticsTxOk,
       "nsCommonMonitorNetworkInterfaceStatisticsTxError": nsCommonMonitorNetworkInterfaceStatisticsTxError,
       "nsCommonMonitorNetworkInterfaceStatisticsTxDrop": nsCommonMonitorNetworkInterfaceStatisticsTxDrop,
       "nsCommonMonitorNetworkInterfaceStatisticsTxOvr": nsCommonMonitorNetworkInterfaceStatisticsTxOvr,
       "nsCommonMonitorNetworkInterfaceStatisticsRxBytes": nsCommonMonitorNetworkInterfaceStatisticsRxBytes,
       "nsCommonMonitorNetworkInterfaceStatisticsTxBytes": nsCommonMonitorNetworkInterfaceStatisticsTxBytes,
       "nsCommonMonitorNetworkInterfaceStatisticsRxBps": nsCommonMonitorNetworkInterfaceStatisticsRxBps,
       "nsCommonMonitorNetworkInterfaceStatisticsTxBps": nsCommonMonitorNetworkInterfaceStatisticsTxBps,
       "nsCommonMonitorNetworkInterfaceStatisticsName": nsCommonMonitorNetworkInterfaceStatisticsName,
       "nsCommonMonitorNetworkQueuesStatisticsTable": nsCommonMonitorNetworkQueuesStatisticsTable,
       "nsCommonMonitorNetworkQueuesStatisticsEntry": nsCommonMonitorNetworkQueuesStatisticsEntry,
       "nsCommonMonitorNetworkQueuesStatisticsNeighborIndex": nsCommonMonitorNetworkQueuesStatisticsNeighborIndex,
       "nsCommonMonitorNetworkQueuesStatisticsCos": nsCommonMonitorNetworkQueuesStatisticsCos,
       "nsCommonMonitorNetworkQueuesStatisticsEnqueuedBytes": nsCommonMonitorNetworkQueuesStatisticsEnqueuedBytes,
       "nsCommonMonitorNetworkQueuesStatisticsEnqueuedPackets": nsCommonMonitorNetworkQueuesStatisticsEnqueuedPackets,
       "nsCommonMonitorNetworkQueuesStatisticsBackloggedBytes": nsCommonMonitorNetworkQueuesStatisticsBackloggedBytes,
       "nsCommonMonitorNetworkQueuesStatisticsBackloggedPackets": nsCommonMonitorNetworkQueuesStatisticsBackloggedPackets,
       "nsCommonMonitorNetworkQueuesStatisticsDroppedYellowPackets": nsCommonMonitorNetworkQueuesStatisticsDroppedYellowPackets,
       "nsCommonMonitorNetworkQueuesStatisticsDroppedGreenPackets": nsCommonMonitorNetworkQueuesStatisticsDroppedGreenPackets,
       "nsCommonMonitorNetworkNeighborsStatisticsTable": nsCommonMonitorNetworkNeighborsStatisticsTable,
       "nsCommonMonitorNetworkNeighborsStatisticsEntry": nsCommonMonitorNetworkNeighborsStatisticsEntry,
       "nsCommonMonitorNetworkNeighborsStatisticsIndex": nsCommonMonitorNetworkNeighborsStatisticsIndex,
       "nsCommonMonitorNetworkNeighborsStatisticsAverageTxRate": nsCommonMonitorNetworkNeighborsStatisticsAverageTxRate,
       "nsCommonMonitorNetworkNeighborsStatisticsAverageTxPacketRate": nsCommonMonitorNetworkNeighborsStatisticsAverageTxPacketRate,
       "nsCommonMonitorNetworkNeighborsStatisticsTxBytes": nsCommonMonitorNetworkNeighborsStatisticsTxBytes,
       "nsCommonMonitorNetworkNeighborsStatisticsTxPackets": nsCommonMonitorNetworkNeighborsStatisticsTxPackets,
       "nsCommonMonitorNetworkBwManagementStatisticsTable": nsCommonMonitorNetworkBwManagementStatisticsTable,
       "nsCommonMonitorNetworkBwManagementStatisticsEntry": nsCommonMonitorNetworkBwManagementStatisticsEntry,
       "nsCommonMonitorNetworkBwManagementStatisticsNeighborIndex": nsCommonMonitorNetworkBwManagementStatisticsNeighborIndex,
       "nsCommonMonitorNetworkBwManagementStatisticsGreenPackets": nsCommonMonitorNetworkBwManagementStatisticsGreenPackets,
       "nsCommonMonitorNetworkBwManagementStatisticsGreenRates": nsCommonMonitorNetworkBwManagementStatisticsGreenRates,
       "nsCommonMonitorNetworkBwManagementStatisticsYellowPackets": nsCommonMonitorNetworkBwManagementStatisticsYellowPackets,
       "nsCommonMonitorNetworkBwManagementStatisticsYellowRates": nsCommonMonitorNetworkBwManagementStatisticsYellowRates,
       "nsCommonMonitorNetworkBwManagementStatisticsRedPackets": nsCommonMonitorNetworkBwManagementStatisticsRedPackets,
       "nsCommonMonitorNetworkBwManagementStatisticsRedRates": nsCommonMonitorNetworkBwManagementStatisticsRedRates,
       "nsCommonMonitorNetworkInterfaceClrCmd": nsCommonMonitorNetworkInterfaceClrCmd,
       "nsCommonSystem": nsCommonSystem,
       "nsCommonSystemSwVersion": nsCommonSystemSwVersion,
       "nsCommonSystemSwVersionFirmware": nsCommonSystemSwVersionFirmware,
       "nsCommonSystemSwVersionOs": nsCommonSystemSwVersionOs,
       "nsCommonSystemSwVersionFs": nsCommonSystemSwVersionFs,
       "nsCommonSystemSwVersionDb": nsCommonSystemSwVersionDb,
       "nsCommonSystemSwVersionAppTable": nsCommonSystemSwVersionAppTable,
       "nsCommonSystemSwVersionAppEntry": nsCommonSystemSwVersionAppEntry,
       "nsCommonSystemSwVersionAppType": nsCommonSystemSwVersionAppType,
       "nsCommonSystemSwVersionAppWeb": nsCommonSystemSwVersionAppWeb,
       "nsCommonSystemSwVersionAppFP": nsCommonSystemSwVersionAppFP,
       "nsCommonSystemSwVersionAppCLI": nsCommonSystemSwVersionAppCLI,
       "nsCommonSystemSwVersionAppNsmd": nsCommonSystemSwVersionAppNsmd,
       "nsCommonSystemSwVersionAppPIC": nsCommonSystemSwVersionAppPIC,
       "nsCommonSystemHwConfig": nsCommonSystemHwConfig,
       "nsCommonSystemHwConfigProductType": nsCommonSystemHwConfigProductType,
       "nsCommonSystemHwConfigSerialNumber": nsCommonSystemHwConfigSerialNumber,
       "nsCommonSystemHwConfigHardwareVersion": nsCommonSystemHwConfigHardwareVersion,
       "nsCommonSystemHwConfigMacAddress": nsCommonSystemHwConfigMacAddress,
       "nsCommonSystemHwConfigInternalClockType": nsCommonSystemHwConfigInternalClockType,
       "nsCommonSystemHwConfigCardTable": nsCommonSystemHwConfigCardTable,
       "nsCommonSystemHwConfigCardEntry": nsCommonSystemHwConfigCardEntry,
       "nsCommonSystemHwConfigCardID": nsCommonSystemHwConfigCardID,
       "nsCommonSystemHwConfigCardType": nsCommonSystemHwConfigCardType,
       "nsCommonSystemHwConfigCardSerialNumber": nsCommonSystemHwConfigCardSerialNumber,
       "nsCommonSystemHwConfigCardHwVersion": nsCommonSystemHwConfigCardHwVersion,
       "nsCommonSystemHwConfigCardSwVersion": nsCommonSystemHwConfigCardSwVersion,
       "nsCommonSystemHwConfigBUCFeeder": nsCommonSystemHwConfigBUCFeeder,
       "nsCommonSystemSwUpdate": nsCommonSystemSwUpdate,
       "nsCommonSystemSwUpdateServerIP": nsCommonSystemSwUpdateServerIP,
       "nsCommonSystemSwUpdateUserName": nsCommonSystemSwUpdateUserName,
       "nsCommonSystemSwUpdatePassword": nsCommonSystemSwUpdatePassword,
       "nsCommonSystemSwUpdateFileName": nsCommonSystemSwUpdateFileName,
       "nsCommonSystemSwUpdateCmd": nsCommonSystemSwUpdateCmd,
       "nsCommonSystemSwUpdateComplete": nsCommonSystemSwUpdateComplete,
       "nsCommonSystemSwUpdateStatus": nsCommonSystemSwUpdateStatus,
       "nsCommonSystemSwActivateBackupCmd": nsCommonSystemSwActivateBackupCmd,
       "nsCommonSystemDatabase": nsCommonSystemDatabase,
       "nsCommonSystemDatabaseCmdDbName": nsCommonSystemDatabaseCmdDbName,
       "nsCommonSystemDatabaseServerIP": nsCommonSystemDatabaseServerIP,
       "nsCommonSystemDatabaseCmd": nsCommonSystemDatabaseCmd,
       "nsCommonSystemDatabaseTable": nsCommonSystemDatabaseTable,
       "nsCommonSystemDatabaseEntry": nsCommonSystemDatabaseEntry,
       "nsCommonSystemDatabaseID": nsCommonSystemDatabaseID,
       "nsCommonSystemDatabaseName": nsCommonSystemDatabaseName,
       "nsCommonSystemLicense": nsCommonSystemLicense,
       "nsCommonSystemLicenseIssueDate": nsCommonSystemLicenseIssueDate,
       "nsCommonSystemLicenseID": nsCommonSystemLicenseID,
       "nsCommonSystemLicenseFeaturesTable": nsCommonSystemLicenseFeaturesTable,
       "nsCommonSystemLicenseFeaturesEntry": nsCommonSystemLicenseFeaturesEntry,
       "nsCommonSystemLicenseFeatureIndx": nsCommonSystemLicenseFeatureIndx,
       "nsCommonSystemLicenseFeatureName": nsCommonSystemLicenseFeatureName,
       "nsCommonSystemLicenseFeatureType": nsCommonSystemLicenseFeatureType,
       "nsCommonSystemLicenseFeatureDaysLeft": nsCommonSystemLicenseFeatureDaysLeft,
       "nsCommonProducts": nsCommonProducts,
       "nsNS1000": nsNS1000,
       "nsNS2000": nsNS2000,
       "nsNS3000": nsNS3000}
)
