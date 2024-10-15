# SNMP MIB module (APPIAN-PPORT-SERIAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPIAN-PPORT-SERIAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:41 2024
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

(acChassisCurrentTime,
 acChassisRingId) = mibBuilder.importSymbols(
    "APPIAN-CHASSIS-MIB",
    "acChassisCurrentTime",
    "acChassisRingId")

(AcAdminStatus,
 AcNodeId,
 AcOpStatus,
 acPport) = mibBuilder.importSymbols(
    "APPIAN-SMI-MIB",
    "AcAdminStatus",
    "AcNodeId",
    "AcOpStatus",
    "acPport")

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

acSerial = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 2)
)
acSerial.setRevisions(
        ("1900-02-23 16:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcSerialTraps_ObjectIdentity = ObjectIdentity
acSerialTraps = _AcSerialTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 2, 0)
)
_AcSerialTable_Object = MibTable
acSerialTable = _AcSerialTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    acSerialTable.setStatus("current")
_AcSerialEntry_Object = MibTableRow
acSerialEntry = _AcSerialEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 2, 1, 1)
)
acSerialEntry.setIndexNames(
    (0, "APPIAN-PPORT-SERIAL-MIB", "acSerialNodeId"),
    (0, "APPIAN-PPORT-SERIAL-MIB", "acSerialSlot"),
    (0, "APPIAN-PPORT-SERIAL-MIB", "acSerialPort"),
)
if mibBuilder.loadTexts:
    acSerialEntry.setStatus("current")
_AcSerialNodeId_Type = AcNodeId
_AcSerialNodeId_Object = MibTableColumn
acSerialNodeId = _AcSerialNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 2, 1, 1, 1),
    _AcSerialNodeId_Type()
)
acSerialNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSerialNodeId.setStatus("current")


class _AcSerialSlot_Type(Integer32):
    """Custom type acSerialSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AcSerialSlot_Type.__name__ = "Integer32"
_AcSerialSlot_Object = MibTableColumn
acSerialSlot = _AcSerialSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 2, 1, 1, 2),
    _AcSerialSlot_Type()
)
acSerialSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSerialSlot.setStatus("current")


class _AcSerialPort_Type(Integer32):
    """Custom type acSerialPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AcSerialPort_Type.__name__ = "Integer32"
_AcSerialPort_Object = MibTableColumn
acSerialPort = _AcSerialPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 2, 1, 1, 3),
    _AcSerialPort_Type()
)
acSerialPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSerialPort.setStatus("current")


class _AcSerialAdminStatus_Type(AcAdminStatus):
    """Custom type acSerialAdminStatus based on AcAdminStatus"""


_AcSerialAdminStatus_Object = MibTableColumn
acSerialAdminStatus = _AcSerialAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 2, 1, 1, 4),
    _AcSerialAdminStatus_Type()
)
acSerialAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSerialAdminStatus.setStatus("current")
_AcSerialOpStatus_Type = AcOpStatus
_AcSerialOpStatus_Object = MibTableColumn
acSerialOpStatus = _AcSerialOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 2, 1, 1, 5),
    _AcSerialOpStatus_Type()
)
acSerialOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSerialOpStatus.setStatus("current")
_AcSerialOpCode_Type = Integer32
_AcSerialOpCode_Object = MibTableColumn
acSerialOpCode = _AcSerialOpCode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 2, 1, 1, 6),
    _AcSerialOpCode_Type()
)
acSerialOpCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSerialOpCode.setStatus("current")


class _AcSerialOpMode_Type(Integer32):
    """Custom type acSerialOpMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ppp", 2),
          ("terminal", 1),
          ("unknown", 0))
    )


_AcSerialOpMode_Type.__name__ = "Integer32"
_AcSerialOpMode_Object = MibTableColumn
acSerialOpMode = _AcSerialOpMode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 2, 1, 1, 7),
    _AcSerialOpMode_Type()
)
acSerialOpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSerialOpMode.setStatus("current")


class _AcSerialBaudRate_Type(Integer32):
    """Custom type acSerialBaudRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("baud115000", 6),
          ("baud19200", 3),
          ("baud56000", 4),
          ("baud64000", 5),
          ("baud9600", 2),
          ("unknown", 0))
    )


_AcSerialBaudRate_Type.__name__ = "Integer32"
_AcSerialBaudRate_Object = MibTableColumn
acSerialBaudRate = _AcSerialBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 2, 1, 1, 8),
    _AcSerialBaudRate_Type()
)
acSerialBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSerialBaudRate.setStatus("current")


class _AcSerialParity_Type(Integer32):
    """Custom type acSerialParity based on Integer32"""
    defaultValue = 1

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
        *(("even", 3),
          ("none", 1),
          ("odd", 2),
          ("unknown", 0))
    )


_AcSerialParity_Type.__name__ = "Integer32"
_AcSerialParity_Object = MibTableColumn
acSerialParity = _AcSerialParity_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 2, 1, 1, 9),
    _AcSerialParity_Type()
)
acSerialParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSerialParity.setStatus("current")


class _AcSerialNumberBits_Type(Integer32):
    """Custom type acSerialNumberBits based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bits-7", 1),
          ("bits-8", 2),
          ("unknown", 0))
    )


_AcSerialNumberBits_Type.__name__ = "Integer32"
_AcSerialNumberBits_Object = MibTableColumn
acSerialNumberBits = _AcSerialNumberBits_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 2, 1, 1, 10),
    _AcSerialNumberBits_Type()
)
acSerialNumberBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSerialNumberBits.setStatus("current")


class _AcSerialIpAddress_Type(IpAddress):
    """Custom type acSerialIpAddress based on IpAddress"""
    defaultValue = 0


_AcSerialIpAddress_Object = MibTableColumn
acSerialIpAddress = _AcSerialIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 2, 1, 1, 11),
    _AcSerialIpAddress_Type()
)
acSerialIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSerialIpAddress.setStatus("current")


class _AcSerialIpSubnet_Type(IpAddress):
    """Custom type acSerialIpSubnet based on IpAddress"""
    defaultValue = 0


_AcSerialIpSubnet_Object = MibTableColumn
acSerialIpSubnet = _AcSerialIpSubnet_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 2, 1, 1, 12),
    _AcSerialIpSubnet_Type()
)
acSerialIpSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSerialIpSubnet.setStatus("current")
_AcSerialRxOctets_Type = Integer32
_AcSerialRxOctets_Object = MibTableColumn
acSerialRxOctets = _AcSerialRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 2, 1, 1, 13),
    _AcSerialRxOctets_Type()
)
acSerialRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSerialRxOctets.setStatus("current")
_AcSerialTxOctets_Type = Integer32
_AcSerialTxOctets_Object = MibTableColumn
acSerialTxOctets = _AcSerialTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 2, 1, 1, 14),
    _AcSerialTxOctets_Type()
)
acSerialTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSerialTxOctets.setStatus("current")


class _AcSerialInterfaceName_Type(DisplayString):
    """Custom type acSerialInterfaceName based on DisplayString"""
    defaultValue = OctetString("Serial Interface")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AcSerialInterfaceName_Type.__name__ = "DisplayString"
_AcSerialInterfaceName_Object = MibTableColumn
acSerialInterfaceName = _AcSerialInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 2, 1, 1, 15),
    _AcSerialInterfaceName_Type()
)
acSerialInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSerialInterfaceName.setStatus("current")

# Managed Objects groups


# Notification objects

acSerialLinkDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 2, 0, 1)
)
acSerialLinkDownTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SERIAL-MIB", "acSerialNodeId"),
        ("APPIAN-PPORT-SERIAL-MIB", "acSerialSlot"),
        ("APPIAN-PPORT-SERIAL-MIB", "acSerialPort"))
)
if mibBuilder.loadTexts:
    acSerialLinkDownTrap.setStatus(
        "current"
    )

acSerialLinkUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 2, 0, 2)
)
acSerialLinkUpTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SERIAL-MIB", "acSerialNodeId"),
        ("APPIAN-PPORT-SERIAL-MIB", "acSerialSlot"),
        ("APPIAN-PPORT-SERIAL-MIB", "acSerialPort"))
)
if mibBuilder.loadTexts:
    acSerialLinkUpTrap.setStatus(
        "current"
    )

acSerialStatsResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 2, 0, 3)
)
acSerialStatsResetTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SERIAL-MIB", "acSerialNodeId"),
        ("APPIAN-PPORT-SERIAL-MIB", "acSerialSlot"),
        ("APPIAN-PPORT-SERIAL-MIB", "acSerialPort"))
)
if mibBuilder.loadTexts:
    acSerialStatsResetTrap.setStatus(
        "current"
    )

acSerialCfgErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 2, 0, 4)
)
acSerialCfgErrorTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SERIAL-MIB", "acSerialNodeId"),
        ("APPIAN-PPORT-SERIAL-MIB", "acSerialSlot"),
        ("APPIAN-PPORT-SERIAL-MIB", "acSerialPort"),
        ("APPIAN-PPORT-SERIAL-MIB", "acSerialOpCode"))
)
if mibBuilder.loadTexts:
    acSerialCfgErrorTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPIAN-PPORT-SERIAL-MIB",
    **{"acSerial": acSerial,
       "acSerialTraps": acSerialTraps,
       "acSerialLinkDownTrap": acSerialLinkDownTrap,
       "acSerialLinkUpTrap": acSerialLinkUpTrap,
       "acSerialStatsResetTrap": acSerialStatsResetTrap,
       "acSerialCfgErrorTrap": acSerialCfgErrorTrap,
       "acSerialTable": acSerialTable,
       "acSerialEntry": acSerialEntry,
       "acSerialNodeId": acSerialNodeId,
       "acSerialSlot": acSerialSlot,
       "acSerialPort": acSerialPort,
       "acSerialAdminStatus": acSerialAdminStatus,
       "acSerialOpStatus": acSerialOpStatus,
       "acSerialOpCode": acSerialOpCode,
       "acSerialOpMode": acSerialOpMode,
       "acSerialBaudRate": acSerialBaudRate,
       "acSerialParity": acSerialParity,
       "acSerialNumberBits": acSerialNumberBits,
       "acSerialIpAddress": acSerialIpAddress,
       "acSerialIpSubnet": acSerialIpSubnet,
       "acSerialRxOctets": acSerialRxOctets,
       "acSerialTxOctets": acSerialTxOctets,
       "acSerialInterfaceName": acSerialInterfaceName}
)
