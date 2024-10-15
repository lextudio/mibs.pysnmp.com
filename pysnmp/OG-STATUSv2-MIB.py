# SNMP MIB module (OG-STATUSv2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OG-STATUSv2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:53 2024
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

(opengear,) = mibBuilder.importSymbols(
    "OG-SMI-MIB",
    "opengear")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ogStatus2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 17)
)
ogStatus2.setRevisions(
        ("2014-01-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OgSystem_ObjectIdentity = ObjectIdentity
ogSystem = _OgSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 17, 1)
)


class _OgFirmwareVersion_Type(DisplayString):
    """Custom type ogFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgFirmwareVersion_Type.__name__ = "DisplayString"
_OgFirmwareVersion_Object = MibScalar
ogFirmwareVersion = _OgFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 1, 1),
    _OgFirmwareVersion_Type()
)
ogFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogFirmwareVersion.setStatus("current")


class _OgSerialNumber_Type(DisplayString):
    """Custom type ogSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgSerialNumber_Type.__name__ = "DisplayString"
_OgSerialNumber_Object = MibScalar
ogSerialNumber = _OgSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 1, 2),
    _OgSerialNumber_Type()
)
ogSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialNumber.setStatus("current")
_OgSerialPortTable_Object = MibTable
ogSerialPortTable = _OgSerialPortTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 2)
)
if mibBuilder.loadTexts:
    ogSerialPortTable.setStatus("current")
_OgSerialPortEntry_Object = MibTableRow
ogSerialPortEntry = _OgSerialPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 2, 1)
)
ogSerialPortEntry.setIndexNames(
    (0, "OG-STATUSv2-MIB", "ogSerialPortIndex"),
)
if mibBuilder.loadTexts:
    ogSerialPortEntry.setStatus("current")


class _OgSerialPortIndex_Type(Integer32):
    """Custom type ogSerialPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgSerialPortIndex_Type.__name__ = "Integer32"
_OgSerialPortIndex_Object = MibTableColumn
ogSerialPortIndex = _OgSerialPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 2, 1, 1),
    _OgSerialPortIndex_Type()
)
ogSerialPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogSerialPortIndex.setStatus("current")


class _OgSerialPortLabel_Type(DisplayString):
    """Custom type ogSerialPortLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgSerialPortLabel_Type.__name__ = "DisplayString"
_OgSerialPortLabel_Object = MibTableColumn
ogSerialPortLabel = _OgSerialPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 2, 1, 2),
    _OgSerialPortLabel_Type()
)
ogSerialPortLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortLabel.setStatus("current")
_OgSerialPortSpeed_Type = Integer32
_OgSerialPortSpeed_Object = MibTableColumn
ogSerialPortSpeed = _OgSerialPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 2, 1, 3),
    _OgSerialPortSpeed_Type()
)
ogSerialPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortSpeed.setStatus("current")
_OgSerialPortDataBits_Type = Integer32
_OgSerialPortDataBits_Object = MibTableColumn
ogSerialPortDataBits = _OgSerialPortDataBits_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 2, 1, 4),
    _OgSerialPortDataBits_Type()
)
ogSerialPortDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortDataBits.setStatus("current")


class _OgSerialPortParity_Type(Integer32):
    """Custom type ogSerialPortParity based on Integer32"""
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
        *(("even", 3),
          ("mark", 4),
          ("none", 1),
          ("odd", 2),
          ("space", 5))
    )


_OgSerialPortParity_Type.__name__ = "Integer32"
_OgSerialPortParity_Object = MibTableColumn
ogSerialPortParity = _OgSerialPortParity_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 2, 1, 5),
    _OgSerialPortParity_Type()
)
ogSerialPortParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortParity.setStatus("current")


class _OgSerialPortStopBits_Type(Integer32):
    """Custom type ogSerialPortStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("oneAndAHalf", 3),
          ("two", 2))
    )


_OgSerialPortStopBits_Type.__name__ = "Integer32"
_OgSerialPortStopBits_Object = MibTableColumn
ogSerialPortStopBits = _OgSerialPortStopBits_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 2, 1, 6),
    _OgSerialPortStopBits_Type()
)
ogSerialPortStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortStopBits.setStatus("current")


class _OgSerialPortFlowControl_Type(Integer32):
    """Custom type ogSerialPortFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("none", 1),
          ("software", 3))
    )


_OgSerialPortFlowControl_Type.__name__ = "Integer32"
_OgSerialPortFlowControl_Object = MibTableColumn
ogSerialPortFlowControl = _OgSerialPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 2, 1, 7),
    _OgSerialPortFlowControl_Type()
)
ogSerialPortFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortFlowControl.setStatus("current")


class _OgSerialPortMode_Type(Integer32):
    """Custom type ogSerialPortMode based on Integer32"""
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
          ("console", 2),
          ("none", 1),
          ("sdt", 3),
          ("terminal", 4))
    )


_OgSerialPortMode_Type.__name__ = "Integer32"
_OgSerialPortMode_Object = MibTableColumn
ogSerialPortMode = _OgSerialPortMode_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 2, 1, 8),
    _OgSerialPortMode_Type()
)
ogSerialPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortMode.setStatus("current")


class _OgSerialPortLogLevel_Type(Integer32):
    """Custom type ogSerialPortLogLevel based on Integer32"""
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
        *(("connect", 2),
          ("disabled", 1),
          ("inputAndOutput", 3),
          ("inputOnly", 4),
          ("outputOnly", 5))
    )


_OgSerialPortLogLevel_Type.__name__ = "Integer32"
_OgSerialPortLogLevel_Object = MibTableColumn
ogSerialPortLogLevel = _OgSerialPortLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 2, 1, 9),
    _OgSerialPortLogLevel_Type()
)
ogSerialPortLogLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortLogLevel.setStatus("current")
_OgSerialPortRxBytes_Type = Counter64
_OgSerialPortRxBytes_Object = MibTableColumn
ogSerialPortRxBytes = _OgSerialPortRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 2, 1, 10),
    _OgSerialPortRxBytes_Type()
)
ogSerialPortRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortRxBytes.setStatus("current")
_OgSerialPortTxBytes_Type = Counter64
_OgSerialPortTxBytes_Object = MibTableColumn
ogSerialPortTxBytes = _OgSerialPortTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 2, 1, 11),
    _OgSerialPortTxBytes_Type()
)
ogSerialPortTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortTxBytes.setStatus("current")
_OgSerialPortFramingErrors_Type = Counter64
_OgSerialPortFramingErrors_Object = MibTableColumn
ogSerialPortFramingErrors = _OgSerialPortFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 2, 1, 12),
    _OgSerialPortFramingErrors_Type()
)
ogSerialPortFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortFramingErrors.setStatus("current")
_OgSerialPortParityErrors_Type = Counter64
_OgSerialPortParityErrors_Object = MibTableColumn
ogSerialPortParityErrors = _OgSerialPortParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 2, 1, 13),
    _OgSerialPortParityErrors_Type()
)
ogSerialPortParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortParityErrors.setStatus("current")
_OgSerialPortOverrunErrors_Type = Counter64
_OgSerialPortOverrunErrors_Object = MibTableColumn
ogSerialPortOverrunErrors = _OgSerialPortOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 2, 1, 14),
    _OgSerialPortOverrunErrors_Type()
)
ogSerialPortOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortOverrunErrors.setStatus("current")
_OgSerialPortBreaks_Type = Counter64
_OgSerialPortBreaks_Object = MibTableColumn
ogSerialPortBreaks = _OgSerialPortBreaks_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 2, 1, 15),
    _OgSerialPortBreaks_Type()
)
ogSerialPortBreaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortBreaks.setStatus("current")


class _OgSerialPortDCD_Type(Integer32):
    """Custom type ogSerialPortDCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_OgSerialPortDCD_Type.__name__ = "Integer32"
_OgSerialPortDCD_Object = MibTableColumn
ogSerialPortDCD = _OgSerialPortDCD_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 2, 1, 16),
    _OgSerialPortDCD_Type()
)
ogSerialPortDCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortDCD.setStatus("current")


class _OgSerialPortDTR_Type(Integer32):
    """Custom type ogSerialPortDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_OgSerialPortDTR_Type.__name__ = "Integer32"
_OgSerialPortDTR_Object = MibTableColumn
ogSerialPortDTR = _OgSerialPortDTR_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 2, 1, 17),
    _OgSerialPortDTR_Type()
)
ogSerialPortDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortDTR.setStatus("current")


class _OgSerialPortDSR_Type(Integer32):
    """Custom type ogSerialPortDSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_OgSerialPortDSR_Type.__name__ = "Integer32"
_OgSerialPortDSR_Object = MibTableColumn
ogSerialPortDSR = _OgSerialPortDSR_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 2, 1, 18),
    _OgSerialPortDSR_Type()
)
ogSerialPortDSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortDSR.setStatus("current")


class _OgSerialPortCTS_Type(Integer32):
    """Custom type ogSerialPortCTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_OgSerialPortCTS_Type.__name__ = "Integer32"
_OgSerialPortCTS_Object = MibTableColumn
ogSerialPortCTS = _OgSerialPortCTS_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 2, 1, 19),
    _OgSerialPortCTS_Type()
)
ogSerialPortCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortCTS.setStatus("current")


class _OgSerialPortRTS_Type(Integer32):
    """Custom type ogSerialPortRTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_OgSerialPortRTS_Type.__name__ = "Integer32"
_OgSerialPortRTS_Object = MibTableColumn
ogSerialPortRTS = _OgSerialPortRTS_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 2, 1, 20),
    _OgSerialPortRTS_Type()
)
ogSerialPortRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortRTS.setStatus("current")
_OgSerialUserTable_Object = MibTable
ogSerialUserTable = _OgSerialUserTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 3)
)
if mibBuilder.loadTexts:
    ogSerialUserTable.setStatus("current")
_OgSerialUserEntry_Object = MibTableRow
ogSerialUserEntry = _OgSerialUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 3, 1)
)
ogSerialUserEntry.setIndexNames(
    (0, "OG-STATUSv2-MIB", "ogSerialUserIndex"),
)
if mibBuilder.loadTexts:
    ogSerialUserEntry.setStatus("current")


class _OgSerialUserIndex_Type(Integer32):
    """Custom type ogSerialUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgSerialUserIndex_Type.__name__ = "Integer32"
_OgSerialUserIndex_Object = MibTableColumn
ogSerialUserIndex = _OgSerialUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 3, 1, 1),
    _OgSerialUserIndex_Type()
)
ogSerialUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogSerialUserIndex.setStatus("current")
_OgSerialUserStartTime_Type = DateAndTime
_OgSerialUserStartTime_Object = MibTableColumn
ogSerialUserStartTime = _OgSerialUserStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 3, 1, 2),
    _OgSerialUserStartTime_Type()
)
ogSerialUserStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialUserStartTime.setStatus("current")
_OgSerialUserPort_Type = Integer32
_OgSerialUserPort_Object = MibTableColumn
ogSerialUserPort = _OgSerialUserPort_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 3, 1, 3),
    _OgSerialUserPort_Type()
)
ogSerialUserPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialUserPort.setStatus("current")


class _OgSerialUserLabel_Type(DisplayString):
    """Custom type ogSerialUserLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgSerialUserLabel_Type.__name__ = "DisplayString"
_OgSerialUserLabel_Object = MibTableColumn
ogSerialUserLabel = _OgSerialUserLabel_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 3, 1, 4),
    _OgSerialUserLabel_Type()
)
ogSerialUserLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialUserLabel.setStatus("current")


class _OgSerialUserName_Type(DisplayString):
    """Custom type ogSerialUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgSerialUserName_Type.__name__ = "DisplayString"
_OgSerialUserName_Object = MibTableColumn
ogSerialUserName = _OgSerialUserName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 3, 1, 5),
    _OgSerialUserName_Type()
)
ogSerialUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialUserName.setStatus("current")
_OgHostTable_Object = MibTable
ogHostTable = _OgHostTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 4)
)
if mibBuilder.loadTexts:
    ogHostTable.setStatus("current")
_OgHostEntry_Object = MibTableRow
ogHostEntry = _OgHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 4, 1)
)
ogHostEntry.setIndexNames(
    (0, "OG-STATUSv2-MIB", "ogHostIndex"),
)
if mibBuilder.loadTexts:
    ogHostEntry.setStatus("current")


class _OgHostIndex_Type(Integer32):
    """Custom type ogHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgHostIndex_Type.__name__ = "Integer32"
_OgHostIndex_Object = MibTableColumn
ogHostIndex = _OgHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 4, 1, 1),
    _OgHostIndex_Type()
)
ogHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogHostIndex.setStatus("current")
_OgHostName_Type = DisplayString
_OgHostName_Object = MibTableColumn
ogHostName = _OgHostName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 4, 1, 2),
    _OgHostName_Type()
)
ogHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogHostName.setStatus("current")
_OgHostIpV4Address_Type = DisplayString
_OgHostIpV4Address_Object = MibTableColumn
ogHostIpV4Address = _OgHostIpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 4, 1, 3),
    _OgHostIpV4Address_Type()
)
ogHostIpV4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogHostIpV4Address.setStatus("current")
_OgHostIpV6Address_Type = DisplayString
_OgHostIpV6Address_Object = MibTableColumn
ogHostIpV6Address = _OgHostIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 4, 1, 4),
    _OgHostIpV6Address_Type()
)
ogHostIpV6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogHostIpV6Address.setStatus("current")
_OgHostServiceTable_Object = MibTable
ogHostServiceTable = _OgHostServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 5)
)
if mibBuilder.loadTexts:
    ogHostServiceTable.setStatus("current")
_OgHostServiceEntry_Object = MibTableRow
ogHostServiceEntry = _OgHostServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 5, 1)
)
ogHostServiceEntry.setIndexNames(
    (0, "OG-STATUSv2-MIB", "ogHostIndex"),
    (0, "OG-STATUSv2-MIB", "ogHostServiceIndex"),
)
if mibBuilder.loadTexts:
    ogHostServiceEntry.setStatus("current")


class _OgHostServiceIndex_Type(Integer32):
    """Custom type ogHostServiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgHostServiceIndex_Type.__name__ = "Integer32"
_OgHostServiceIndex_Object = MibTableColumn
ogHostServiceIndex = _OgHostServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 5, 1, 1),
    _OgHostServiceIndex_Type()
)
ogHostServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogHostServiceIndex.setStatus("current")
_OgHostServiceHost_Type = ObjectIdentifier
_OgHostServiceHost_Object = MibTableColumn
ogHostServiceHost = _OgHostServiceHost_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 5, 1, 2),
    _OgHostServiceHost_Type()
)
ogHostServiceHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogHostServiceHost.setStatus("current")


class _OgHostServiceType_Type(Integer32):
    """Custom type ogHostServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_OgHostServiceType_Type.__name__ = "Integer32"
_OgHostServiceType_Object = MibTableColumn
ogHostServiceType = _OgHostServiceType_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 5, 1, 3),
    _OgHostServiceType_Type()
)
ogHostServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogHostServiceType.setStatus("current")


class _OgHostServicePort_Type(Unsigned32):
    """Custom type ogHostServicePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgHostServicePort_Type.__name__ = "Unsigned32"
_OgHostServicePort_Object = MibTableColumn
ogHostServicePort = _OgHostServicePort_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 5, 1, 4),
    _OgHostServicePort_Type()
)
ogHostServicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogHostServicePort.setStatus("current")


class _OgHostServiceStatus_Type(Integer32):
    """Custom type ogHostServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("unavailable", 3),
          ("unknown", 1))
    )


_OgHostServiceStatus_Type.__name__ = "Integer32"
_OgHostServiceStatus_Object = MibTableColumn
ogHostServiceStatus = _OgHostServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 5, 1, 5),
    _OgHostServiceStatus_Type()
)
ogHostServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogHostServiceStatus.setStatus("current")
_OgHostServiceCounter_Type = Counter32
_OgHostServiceCounter_Object = MibTableColumn
ogHostServiceCounter = _OgHostServiceCounter_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 5, 1, 6),
    _OgHostServiceCounter_Type()
)
ogHostServiceCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogHostServiceCounter.setStatus("current")
_OgHostUserTable_Object = MibTable
ogHostUserTable = _OgHostUserTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 6)
)
if mibBuilder.loadTexts:
    ogHostUserTable.setStatus("current")
_OgHostUserEntry_Object = MibTableRow
ogHostUserEntry = _OgHostUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 6, 1)
)
ogHostUserEntry.setIndexNames(
    (0, "OG-STATUSv2-MIB", "ogHostUserIndex"),
)
if mibBuilder.loadTexts:
    ogHostUserEntry.setStatus("current")


class _OgHostUserIndex_Type(Integer32):
    """Custom type ogHostUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgHostUserIndex_Type.__name__ = "Integer32"
_OgHostUserIndex_Object = MibTableColumn
ogHostUserIndex = _OgHostUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 6, 1, 1),
    _OgHostUserIndex_Type()
)
ogHostUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogHostUserIndex.setStatus("current")
_OgHostUserHost_Type = ObjectIdentifier
_OgHostUserHost_Object = MibTableColumn
ogHostUserHost = _OgHostUserHost_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 6, 1, 2),
    _OgHostUserHost_Type()
)
ogHostUserHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogHostUserHost.setStatus("current")
_OgHostUserStartTime_Type = DateAndTime
_OgHostUserStartTime_Object = MibTableColumn
ogHostUserStartTime = _OgHostUserStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 6, 1, 3),
    _OgHostUserStartTime_Type()
)
ogHostUserStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogHostUserStartTime.setStatus("current")


class _OgHostUserAddress_Type(DisplayString):
    """Custom type ogHostUserAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgHostUserAddress_Type.__name__ = "DisplayString"
_OgHostUserAddress_Object = MibTableColumn
ogHostUserAddress = _OgHostUserAddress_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 6, 1, 4),
    _OgHostUserAddress_Type()
)
ogHostUserAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogHostUserAddress.setStatus("current")


class _OgHostUserHostName_Type(DisplayString):
    """Custom type ogHostUserHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgHostUserHostName_Type.__name__ = "DisplayString"
_OgHostUserHostName_Object = MibTableColumn
ogHostUserHostName = _OgHostUserHostName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 6, 1, 5),
    _OgHostUserHostName_Type()
)
ogHostUserHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogHostUserHostName.setStatus("current")


class _OgHostUserName_Type(DisplayString):
    """Custom type ogHostUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_OgHostUserName_Type.__name__ = "DisplayString"
_OgHostUserName_Object = MibTableColumn
ogHostUserName = _OgHostUserName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 6, 1, 6),
    _OgHostUserName_Type()
)
ogHostUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogHostUserName.setStatus("current")
_OgWebUserTable_Object = MibTable
ogWebUserTable = _OgWebUserTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 7)
)
if mibBuilder.loadTexts:
    ogWebUserTable.setStatus("current")
_OgWebUserEntry_Object = MibTableRow
ogWebUserEntry = _OgWebUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 7, 1)
)
ogWebUserEntry.setIndexNames(
    (0, "OG-STATUSv2-MIB", "ogWebUserIndex"),
)
if mibBuilder.loadTexts:
    ogWebUserEntry.setStatus("current")


class _OgWebUserIndex_Type(Integer32):
    """Custom type ogWebUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgWebUserIndex_Type.__name__ = "Integer32"
_OgWebUserIndex_Object = MibTableColumn
ogWebUserIndex = _OgWebUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 7, 1, 1),
    _OgWebUserIndex_Type()
)
ogWebUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogWebUserIndex.setStatus("current")
_OgWebUserStartTime_Type = DateAndTime
_OgWebUserStartTime_Object = MibTableColumn
ogWebUserStartTime = _OgWebUserStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 7, 1, 2),
    _OgWebUserStartTime_Type()
)
ogWebUserStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWebUserStartTime.setStatus("current")


class _OgWebUserName_Type(DisplayString):
    """Custom type ogWebUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgWebUserName_Type.__name__ = "DisplayString"
_OgWebUserName_Object = MibTableColumn
ogWebUserName = _OgWebUserName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 7, 1, 3),
    _OgWebUserName_Type()
)
ogWebUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWebUserName.setStatus("current")


class _OgWebUserSourceAddress_Type(DisplayString):
    """Custom type ogWebUserSourceAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgWebUserSourceAddress_Type.__name__ = "DisplayString"
_OgWebUserSourceAddress_Object = MibTableColumn
ogWebUserSourceAddress = _OgWebUserSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 7, 1, 4),
    _OgWebUserSourceAddress_Type()
)
ogWebUserSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWebUserSourceAddress.setStatus("current")


class _OgWebUserSourcePort_Type(Integer32):
    """Custom type ogWebUserSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgWebUserSourcePort_Type.__name__ = "Integer32"
_OgWebUserSourcePort_Object = MibTableColumn
ogWebUserSourcePort = _OgWebUserSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 7, 1, 5),
    _OgWebUserSourcePort_Type()
)
ogWebUserSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWebUserSourcePort.setStatus("current")
_OgEmdTable_Object = MibTable
ogEmdTable = _OgEmdTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 8)
)
if mibBuilder.loadTexts:
    ogEmdTable.setStatus("current")
_OgEmdEntry_Object = MibTableRow
ogEmdEntry = _OgEmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 8, 1)
)
ogEmdEntry.setIndexNames(
    (0, "OG-STATUSv2-MIB", "ogEmdIndex"),
)
if mibBuilder.loadTexts:
    ogEmdEntry.setStatus("current")


class _OgEmdIndex_Type(Integer32):
    """Custom type ogEmdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgEmdIndex_Type.__name__ = "Integer32"
_OgEmdIndex_Object = MibTableColumn
ogEmdIndex = _OgEmdIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 8, 1, 1),
    _OgEmdIndex_Type()
)
ogEmdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogEmdIndex.setStatus("current")


class _OgEmdName_Type(DisplayString):
    """Custom type ogEmdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgEmdName_Type.__name__ = "DisplayString"
_OgEmdName_Object = MibTableColumn
ogEmdName = _OgEmdName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 8, 1, 2),
    _OgEmdName_Type()
)
ogEmdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdName.setStatus("current")


class _OgEmdDescription_Type(DisplayString):
    """Custom type ogEmdDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgEmdDescription_Type.__name__ = "DisplayString"
_OgEmdDescription_Object = MibTableColumn
ogEmdDescription = _OgEmdDescription_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 8, 1, 3),
    _OgEmdDescription_Type()
)
ogEmdDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdDescription.setStatus("current")


class _OgEmdEnabled_Type(Integer32):
    """Custom type ogEmdEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_OgEmdEnabled_Type.__name__ = "Integer32"
_OgEmdEnabled_Object = MibTableColumn
ogEmdEnabled = _OgEmdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 8, 1, 4),
    _OgEmdEnabled_Type()
)
ogEmdEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdEnabled.setStatus("current")


class _OgEmdLogEnabled_Type(Integer32):
    """Custom type ogEmdLogEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_OgEmdLogEnabled_Type.__name__ = "Integer32"
_OgEmdLogEnabled_Object = MibTableColumn
ogEmdLogEnabled = _OgEmdLogEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 8, 1, 5),
    _OgEmdLogEnabled_Type()
)
ogEmdLogEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdLogEnabled.setStatus("current")


class _OgEmdConnectType_Type(Integer32):
    """Custom type ogEmdConnectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("network", 3),
          ("serial", 2))
    )


_OgEmdConnectType_Type.__name__ = "Integer32"
_OgEmdConnectType_Object = MibTableColumn
ogEmdConnectType = _OgEmdConnectType_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 8, 1, 6),
    _OgEmdConnectType_Type()
)
ogEmdConnectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdConnectType.setStatus("current")
_OgEmdTemperatureTotal_Type = Counter32
_OgEmdTemperatureTotal_Object = MibTableColumn
ogEmdTemperatureTotal = _OgEmdTemperatureTotal_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 8, 1, 7),
    _OgEmdTemperatureTotal_Type()
)
ogEmdTemperatureTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdTemperatureTotal.setStatus("current")
_OgEmdHumidityTotal_Type = Counter32
_OgEmdHumidityTotal_Object = MibTableColumn
ogEmdHumidityTotal = _OgEmdHumidityTotal_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 8, 1, 8),
    _OgEmdHumidityTotal_Type()
)
ogEmdHumidityTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdHumidityTotal.setStatus("current")
_OgEmdDioInputTotal_Type = Counter32
_OgEmdDioInputTotal_Object = MibTableColumn
ogEmdDioInputTotal = _OgEmdDioInputTotal_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 8, 1, 9),
    _OgEmdDioInputTotal_Type()
)
ogEmdDioInputTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdDioInputTotal.setStatus("current")
_OgEmdTemperatureTable_Object = MibTable
ogEmdTemperatureTable = _OgEmdTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 9)
)
if mibBuilder.loadTexts:
    ogEmdTemperatureTable.setStatus("current")
_OgEmdTemperatureEntry_Object = MibTableRow
ogEmdTemperatureEntry = _OgEmdTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 9, 1)
)
ogEmdTemperatureEntry.setIndexNames(
    (0, "OG-STATUSv2-MIB", "ogEmdIndex"),
    (0, "OG-STATUSv2-MIB", "ogEmdTemperatureIndex"),
)
if mibBuilder.loadTexts:
    ogEmdTemperatureEntry.setStatus("current")


class _OgEmdTemperatureIndex_Type(Integer32):
    """Custom type ogEmdTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgEmdTemperatureIndex_Type.__name__ = "Integer32"
_OgEmdTemperatureIndex_Object = MibTableColumn
ogEmdTemperatureIndex = _OgEmdTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 9, 1, 1),
    _OgEmdTemperatureIndex_Type()
)
ogEmdTemperatureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogEmdTemperatureIndex.setStatus("current")
_OgEmdTemperatureEmd_Type = ObjectIdentifier
_OgEmdTemperatureEmd_Object = MibTableColumn
ogEmdTemperatureEmd = _OgEmdTemperatureEmd_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 9, 1, 2),
    _OgEmdTemperatureEmd_Type()
)
ogEmdTemperatureEmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdTemperatureEmd.setStatus("current")


class _OgEmdTemperatureName_Type(DisplayString):
    """Custom type ogEmdTemperatureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgEmdTemperatureName_Type.__name__ = "DisplayString"
_OgEmdTemperatureName_Object = MibTableColumn
ogEmdTemperatureName = _OgEmdTemperatureName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 9, 1, 3),
    _OgEmdTemperatureName_Type()
)
ogEmdTemperatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdTemperatureName.setStatus("current")


class _OgEmdTemperatureDescription_Type(DisplayString):
    """Custom type ogEmdTemperatureDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgEmdTemperatureDescription_Type.__name__ = "DisplayString"
_OgEmdTemperatureDescription_Object = MibTableColumn
ogEmdTemperatureDescription = _OgEmdTemperatureDescription_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 9, 1, 4),
    _OgEmdTemperatureDescription_Type()
)
ogEmdTemperatureDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdTemperatureDescription.setStatus("current")
_OgEmdTemperatureValue_Type = Integer32
_OgEmdTemperatureValue_Object = MibTableColumn
ogEmdTemperatureValue = _OgEmdTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 9, 1, 5),
    _OgEmdTemperatureValue_Type()
)
ogEmdTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdTemperatureValue.setStatus("current")
if mibBuilder.loadTexts:
    ogEmdTemperatureValue.setUnits("degrees")
_OgEmdTemperatureCounter_Type = Counter32
_OgEmdTemperatureCounter_Object = MibTableColumn
ogEmdTemperatureCounter = _OgEmdTemperatureCounter_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 9, 1, 6),
    _OgEmdTemperatureCounter_Type()
)
ogEmdTemperatureCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdTemperatureCounter.setStatus("current")
_OgEmdHumidityTable_Object = MibTable
ogEmdHumidityTable = _OgEmdHumidityTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 10)
)
if mibBuilder.loadTexts:
    ogEmdHumidityTable.setStatus("current")
_OgEmdHumidityEntry_Object = MibTableRow
ogEmdHumidityEntry = _OgEmdHumidityEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 10, 1)
)
ogEmdHumidityEntry.setIndexNames(
    (0, "OG-STATUSv2-MIB", "ogEmdIndex"),
    (0, "OG-STATUSv2-MIB", "ogEmdHumidityIndex"),
)
if mibBuilder.loadTexts:
    ogEmdHumidityEntry.setStatus("current")


class _OgEmdHumidityIndex_Type(Integer32):
    """Custom type ogEmdHumidityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgEmdHumidityIndex_Type.__name__ = "Integer32"
_OgEmdHumidityIndex_Object = MibTableColumn
ogEmdHumidityIndex = _OgEmdHumidityIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 10, 1, 1),
    _OgEmdHumidityIndex_Type()
)
ogEmdHumidityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogEmdHumidityIndex.setStatus("current")
_OgEmdHumidityEmd_Type = ObjectIdentifier
_OgEmdHumidityEmd_Object = MibTableColumn
ogEmdHumidityEmd = _OgEmdHumidityEmd_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 10, 1, 2),
    _OgEmdHumidityEmd_Type()
)
ogEmdHumidityEmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdHumidityEmd.setStatus("current")


class _OgEmdHumidityName_Type(DisplayString):
    """Custom type ogEmdHumidityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgEmdHumidityName_Type.__name__ = "DisplayString"
_OgEmdHumidityName_Object = MibTableColumn
ogEmdHumidityName = _OgEmdHumidityName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 10, 1, 3),
    _OgEmdHumidityName_Type()
)
ogEmdHumidityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdHumidityName.setStatus("current")


class _OgEmdHumidityDescription_Type(DisplayString):
    """Custom type ogEmdHumidityDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgEmdHumidityDescription_Type.__name__ = "DisplayString"
_OgEmdHumidityDescription_Object = MibTableColumn
ogEmdHumidityDescription = _OgEmdHumidityDescription_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 10, 1, 4),
    _OgEmdHumidityDescription_Type()
)
ogEmdHumidityDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdHumidityDescription.setStatus("current")
_OgEmdHumidityValue_Type = Integer32
_OgEmdHumidityValue_Object = MibTableColumn
ogEmdHumidityValue = _OgEmdHumidityValue_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 10, 1, 5),
    _OgEmdHumidityValue_Type()
)
ogEmdHumidityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdHumidityValue.setStatus("current")
if mibBuilder.loadTexts:
    ogEmdHumidityValue.setUnits("percent")
_OgEmdHumidityCounter_Type = Counter32
_OgEmdHumidityCounter_Object = MibTableColumn
ogEmdHumidityCounter = _OgEmdHumidityCounter_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 10, 1, 6),
    _OgEmdHumidityCounter_Type()
)
ogEmdHumidityCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdHumidityCounter.setStatus("current")
_OgEmdDioTable_Object = MibTable
ogEmdDioTable = _OgEmdDioTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 11)
)
if mibBuilder.loadTexts:
    ogEmdDioTable.setStatus("current")
_OgEmdDioEntry_Object = MibTableRow
ogEmdDioEntry = _OgEmdDioEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 11, 1)
)
ogEmdDioEntry.setIndexNames(
    (0, "OG-STATUSv2-MIB", "ogEmdIndex"),
    (0, "OG-STATUSv2-MIB", "ogEmdDioIndex"),
)
if mibBuilder.loadTexts:
    ogEmdDioEntry.setStatus("current")


class _OgEmdDioIndex_Type(Integer32):
    """Custom type ogEmdDioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgEmdDioIndex_Type.__name__ = "Integer32"
_OgEmdDioIndex_Object = MibTableColumn
ogEmdDioIndex = _OgEmdDioIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 11, 1, 1),
    _OgEmdDioIndex_Type()
)
ogEmdDioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogEmdDioIndex.setStatus("current")
_OgEmdDioEmd_Type = ObjectIdentifier
_OgEmdDioEmd_Object = MibTableColumn
ogEmdDioEmd = _OgEmdDioEmd_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 11, 1, 2),
    _OgEmdDioEmd_Type()
)
ogEmdDioEmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdDioEmd.setStatus("current")


class _OgEmdDioName_Type(DisplayString):
    """Custom type ogEmdDioName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgEmdDioName_Type.__name__ = "DisplayString"
_OgEmdDioName_Object = MibTableColumn
ogEmdDioName = _OgEmdDioName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 11, 1, 3),
    _OgEmdDioName_Type()
)
ogEmdDioName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdDioName.setStatus("current")


class _OgEmdDioDescription_Type(DisplayString):
    """Custom type ogEmdDioDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgEmdDioDescription_Type.__name__ = "DisplayString"
_OgEmdDioDescription_Object = MibTableColumn
ogEmdDioDescription = _OgEmdDioDescription_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 11, 1, 4),
    _OgEmdDioDescription_Type()
)
ogEmdDioDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdDioDescription.setStatus("current")


class _OgEmdDioType_Type(Integer32):
    """Custom type ogEmdDioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highVoltageOutput", 2),
          ("ttlInputOutput", 1))
    )


_OgEmdDioType_Type.__name__ = "Integer32"
_OgEmdDioType_Object = MibTableColumn
ogEmdDioType = _OgEmdDioType_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 11, 1, 5),
    _OgEmdDioType_Type()
)
ogEmdDioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdDioType.setStatus("current")


class _OgEmdDioDirection_Type(Integer32):
    """Custom type ogEmdDioDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 2),
          ("output", 1))
    )


_OgEmdDioDirection_Type.__name__ = "Integer32"
_OgEmdDioDirection_Object = MibTableColumn
ogEmdDioDirection = _OgEmdDioDirection_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 11, 1, 6),
    _OgEmdDioDirection_Type()
)
ogEmdDioDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdDioDirection.setStatus("current")


class _OgEmdDioState_Type(Integer32):
    """Custom type ogEmdDioState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 2))
    )


_OgEmdDioState_Type.__name__ = "Integer32"
_OgEmdDioState_Object = MibTableColumn
ogEmdDioState = _OgEmdDioState_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 11, 1, 7),
    _OgEmdDioState_Type()
)
ogEmdDioState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdDioState.setStatus("current")


class _OgEmdDioTriggerMode_Type(Integer32):
    """Custom type ogEmdDioTriggerMode based on Integer32"""
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
        *(("fallingEdge", 3),
          ("invalid", 1),
          ("risingEdge", 2),
          ("risingFallingEdge", 4))
    )


_OgEmdDioTriggerMode_Type.__name__ = "Integer32"
_OgEmdDioTriggerMode_Object = MibTableColumn
ogEmdDioTriggerMode = _OgEmdDioTriggerMode_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 11, 1, 8),
    _OgEmdDioTriggerMode_Type()
)
ogEmdDioTriggerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdDioTriggerMode.setStatus("current")
_OgEmdDioCounter_Type = Counter32
_OgEmdDioCounter_Object = MibTableColumn
ogEmdDioCounter = _OgEmdDioCounter_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 11, 1, 9),
    _OgEmdDioCounter_Type()
)
ogEmdDioCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdDioCounter.setStatus("current")
_OgNetInterfaceTable_Object = MibTable
ogNetInterfaceTable = _OgNetInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 12)
)
if mibBuilder.loadTexts:
    ogNetInterfaceTable.setStatus("current")
_OgNetInterfaceEntry_Object = MibTableRow
ogNetInterfaceEntry = _OgNetInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 12, 1)
)
ogNetInterfaceEntry.setIndexNames(
    (0, "OG-STATUSv2-MIB", "ogNetInterfaceIndex"),
)
if mibBuilder.loadTexts:
    ogNetInterfaceEntry.setStatus("current")


class _OgNetInterfaceIndex_Type(Integer32):
    """Custom type ogNetInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgNetInterfaceIndex_Type.__name__ = "Integer32"
_OgNetInterfaceIndex_Object = MibTableColumn
ogNetInterfaceIndex = _OgNetInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 12, 1, 1),
    _OgNetInterfaceIndex_Type()
)
ogNetInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogNetInterfaceIndex.setStatus("current")


class _OgNetInterfaceName_Type(DisplayString):
    """Custom type ogNetInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgNetInterfaceName_Type.__name__ = "DisplayString"
_OgNetInterfaceName_Object = MibTableColumn
ogNetInterfaceName = _OgNetInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 12, 1, 2),
    _OgNetInterfaceName_Type()
)
ogNetInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogNetInterfaceName.setStatus("current")


class _OgNetInterfaceType_Type(Integer32):
    """Custom type ogNetInterfaceType based on Integer32"""
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
        *(("cellModem", 4),
          ("ethernet", 2),
          ("unavailable", 1),
          ("v92Modem", 5),
          ("vpn", 6),
          ("wifi", 3))
    )


_OgNetInterfaceType_Type.__name__ = "Integer32"
_OgNetInterfaceType_Object = MibTableColumn
ogNetInterfaceType = _OgNetInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 12, 1, 3),
    _OgNetInterfaceType_Type()
)
ogNetInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogNetInterfaceType.setStatus("current")


class _OgNetInterfaceState_Type(Integer32):
    """Custom type ogNetInterfaceState based on Integer32"""
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
        *(("down", 2),
          ("starting", 3),
          ("stopping", 5),
          ("unavailable", 1),
          ("up", 4))
    )


_OgNetInterfaceState_Type.__name__ = "Integer32"
_OgNetInterfaceState_Object = MibTableColumn
ogNetInterfaceState = _OgNetInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 12, 1, 4),
    _OgNetInterfaceState_Type()
)
ogNetInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogNetInterfaceState.setStatus("current")
_OgPowerSupplyTable_Object = MibTable
ogPowerSupplyTable = _OgPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 13)
)
if mibBuilder.loadTexts:
    ogPowerSupplyTable.setStatus("current")
_OgPowerSupplyEntry_Object = MibTableRow
ogPowerSupplyEntry = _OgPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 13, 1)
)
ogPowerSupplyEntry.setIndexNames(
    (0, "OG-STATUSv2-MIB", "ogPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    ogPowerSupplyEntry.setStatus("current")


class _OgPowerSupplyIndex_Type(Integer32):
    """Custom type ogPowerSupplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OgPowerSupplyIndex_Type.__name__ = "Integer32"
_OgPowerSupplyIndex_Object = MibTableColumn
ogPowerSupplyIndex = _OgPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 13, 1, 1),
    _OgPowerSupplyIndex_Type()
)
ogPowerSupplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogPowerSupplyIndex.setStatus("current")


class _OgPowerSupplyName_Type(DisplayString):
    """Custom type ogPowerSupplyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgPowerSupplyName_Type.__name__ = "DisplayString"
_OgPowerSupplyName_Object = MibTableColumn
ogPowerSupplyName = _OgPowerSupplyName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 13, 1, 2),
    _OgPowerSupplyName_Type()
)
ogPowerSupplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogPowerSupplyName.setStatus("current")
_OgPowerSupplyInputVoltage_Type = Integer32
_OgPowerSupplyInputVoltage_Object = MibTableColumn
ogPowerSupplyInputVoltage = _OgPowerSupplyInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 13, 1, 3),
    _OgPowerSupplyInputVoltage_Type()
)
ogPowerSupplyInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogPowerSupplyInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    ogPowerSupplyInputVoltage.setUnits("volts")
_OgPowerSupplyOutputCurrent_Type = Integer32
_OgPowerSupplyOutputCurrent_Object = MibTableColumn
ogPowerSupplyOutputCurrent = _OgPowerSupplyOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 13, 1, 4),
    _OgPowerSupplyOutputCurrent_Type()
)
ogPowerSupplyOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogPowerSupplyOutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    ogPowerSupplyOutputCurrent.setUnits("milliamps")
_OgPowerSupplyTemperature_Type = Integer32
_OgPowerSupplyTemperature_Object = MibTableColumn
ogPowerSupplyTemperature = _OgPowerSupplyTemperature_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 13, 1, 5),
    _OgPowerSupplyTemperature_Type()
)
ogPowerSupplyTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogPowerSupplyTemperature.setStatus("current")
if mibBuilder.loadTexts:
    ogPowerSupplyTemperature.setUnits("degrees celsius")
_OgUpsTable_Object = MibTable
ogUpsTable = _OgUpsTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14)
)
if mibBuilder.loadTexts:
    ogUpsTable.setStatus("current")
_OgUpsEntry_Object = MibTableRow
ogUpsEntry = _OgUpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1)
)
ogUpsEntry.setIndexNames(
    (0, "OG-STATUSv2-MIB", "ogUpsIndex"),
)
if mibBuilder.loadTexts:
    ogUpsEntry.setStatus("current")


class _OgUpsIndex_Type(Integer32):
    """Custom type ogUpsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgUpsIndex_Type.__name__ = "Integer32"
_OgUpsIndex_Object = MibTableColumn
ogUpsIndex = _OgUpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 1),
    _OgUpsIndex_Type()
)
ogUpsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogUpsIndex.setStatus("current")


class _OgUpsName_Type(DisplayString):
    """Custom type ogUpsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgUpsName_Type.__name__ = "DisplayString"
_OgUpsName_Object = MibTableColumn
ogUpsName = _OgUpsName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 2),
    _OgUpsName_Type()
)
ogUpsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsName.setStatus("current")


class _OgUpsDescription_Type(DisplayString):
    """Custom type ogUpsDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgUpsDescription_Type.__name__ = "DisplayString"
_OgUpsDescription_Object = MibTableColumn
ogUpsDescription = _OgUpsDescription_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 3),
    _OgUpsDescription_Type()
)
ogUpsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsDescription.setStatus("current")


class _OgUpsType_Type(DisplayString):
    """Custom type ogUpsType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgUpsType_Type.__name__ = "DisplayString"
_OgUpsType_Object = MibTableColumn
ogUpsType = _OgUpsType_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 4),
    _OgUpsType_Type()
)
ogUpsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsType.setStatus("current")


class _OgUpsLogEnabled_Type(Integer32):
    """Custom type ogUpsLogEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_OgUpsLogEnabled_Type.__name__ = "Integer32"
_OgUpsLogEnabled_Object = MibTableColumn
ogUpsLogEnabled = _OgUpsLogEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 5),
    _OgUpsLogEnabled_Type()
)
ogUpsLogEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsLogEnabled.setStatus("current")


class _OgUpsConnectType_Type(Integer32):
    """Custom type ogUpsConnectType based on Integer32"""
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
        *(("http", 3),
          ("https", 4),
          ("serial", 6),
          ("snmp", 5),
          ("unknown", 1),
          ("usb", 2))
    )


_OgUpsConnectType_Type.__name__ = "Integer32"
_OgUpsConnectType_Object = MibTableColumn
ogUpsConnectType = _OgUpsConnectType_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 6),
    _OgUpsConnectType_Type()
)
ogUpsConnectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsConnectType.setStatus("current")


class _OgUpsState_Type(Integer32):
    """Custom type ogUpsState based on Integer32"""
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
        *(("lowBattery", 4),
          ("onBattery", 3),
          ("onBypass", 5),
          ("onLine", 2),
          ("unknown", 1))
    )


_OgUpsState_Type.__name__ = "Integer32"
_OgUpsState_Object = MibTableColumn
ogUpsState = _OgUpsState_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 7),
    _OgUpsState_Type()
)
ogUpsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsState.setStatus("current")
_OgUpsTemperature_Type = Integer32
_OgUpsTemperature_Object = MibTableColumn
ogUpsTemperature = _OgUpsTemperature_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 8),
    _OgUpsTemperature_Type()
)
ogUpsTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsTemperature.setStatus("current")
if mibBuilder.loadTexts:
    ogUpsTemperature.setUnits("degrees")
_OgUpsHumidity_Type = Integer32
_OgUpsHumidity_Object = MibTableColumn
ogUpsHumidity = _OgUpsHumidity_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 9),
    _OgUpsHumidity_Type()
)
ogUpsHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsHumidity.setStatus("current")
if mibBuilder.loadTexts:
    ogUpsHumidity.setUnits("percent")


class _OgUpsBatteryState_Type(Integer32):
    """Custom type ogUpsBatteryState based on Integer32"""
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
        *(("depleted", 5),
          ("low", 4),
          ("normal", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_OgUpsBatteryState_Type.__name__ = "Integer32"
_OgUpsBatteryState_Object = MibTableColumn
ogUpsBatteryState = _OgUpsBatteryState_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 10),
    _OgUpsBatteryState_Type()
)
ogUpsBatteryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsBatteryState.setStatus("current")


class _OgUpsBatteryRunTime_Type(Integer32):
    """Custom type ogUpsBatteryRunTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 31449600),
    )


_OgUpsBatteryRunTime_Type.__name__ = "Integer32"
_OgUpsBatteryRunTime_Object = MibTableColumn
ogUpsBatteryRunTime = _OgUpsBatteryRunTime_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 11),
    _OgUpsBatteryRunTime_Type()
)
ogUpsBatteryRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsBatteryRunTime.setStatus("current")
if mibBuilder.loadTexts:
    ogUpsBatteryRunTime.setUnits("seconds")


class _OgUpsBatteryRunTimeLow_Type(Integer32):
    """Custom type ogUpsBatteryRunTimeLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 31449600),
    )


_OgUpsBatteryRunTimeLow_Type.__name__ = "Integer32"
_OgUpsBatteryRunTimeLow_Object = MibTableColumn
ogUpsBatteryRunTimeLow = _OgUpsBatteryRunTimeLow_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 12),
    _OgUpsBatteryRunTimeLow_Type()
)
ogUpsBatteryRunTimeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsBatteryRunTimeLow.setStatus("current")
if mibBuilder.loadTexts:
    ogUpsBatteryRunTimeLow.setUnits("seconds")


class _OgUpsBatteryRunTimeRestart_Type(Integer32):
    """Custom type ogUpsBatteryRunTimeRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 31449600),
    )


_OgUpsBatteryRunTimeRestart_Type.__name__ = "Integer32"
_OgUpsBatteryRunTimeRestart_Object = MibTableColumn
ogUpsBatteryRunTimeRestart = _OgUpsBatteryRunTimeRestart_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 13),
    _OgUpsBatteryRunTimeRestart_Type()
)
ogUpsBatteryRunTimeRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsBatteryRunTimeRestart.setStatus("current")
if mibBuilder.loadTexts:
    ogUpsBatteryRunTimeRestart.setUnits("seconds")


class _OgUpsBatteryCharge_Type(Integer32):
    """Custom type ogUpsBatteryCharge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_OgUpsBatteryCharge_Type.__name__ = "Integer32"
_OgUpsBatteryCharge_Object = MibTableColumn
ogUpsBatteryCharge = _OgUpsBatteryCharge_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 14),
    _OgUpsBatteryCharge_Type()
)
ogUpsBatteryCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsBatteryCharge.setStatus("current")
if mibBuilder.loadTexts:
    ogUpsBatteryCharge.setUnits("percent")
_OgUpsBatteryVoltage_Type = Integer32
_OgUpsBatteryVoltage_Object = MibTableColumn
ogUpsBatteryVoltage = _OgUpsBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 15),
    _OgUpsBatteryVoltage_Type()
)
ogUpsBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsBatteryVoltage.setStatus("current")
if mibBuilder.loadTexts:
    ogUpsBatteryVoltage.setUnits("0.1 Volt DC")
_OgUpsBatteryNominalVoltage_Type = Integer32
_OgUpsBatteryNominalVoltage_Object = MibTableColumn
ogUpsBatteryNominalVoltage = _OgUpsBatteryNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 16),
    _OgUpsBatteryNominalVoltage_Type()
)
ogUpsBatteryNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsBatteryNominalVoltage.setStatus("current")
if mibBuilder.loadTexts:
    ogUpsBatteryNominalVoltage.setUnits("0.1 Volt DC")
_OgUpsBatteryCurrent_Type = Integer32
_OgUpsBatteryCurrent_Object = MibTableColumn
ogUpsBatteryCurrent = _OgUpsBatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 17),
    _OgUpsBatteryCurrent_Type()
)
ogUpsBatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsBatteryCurrent.setStatus("current")
if mibBuilder.loadTexts:
    ogUpsBatteryCurrent.setUnits("0.1 Amp DC")
_OgUpsBatteryNominalCurrent_Type = Integer32
_OgUpsBatteryNominalCurrent_Object = MibTableColumn
ogUpsBatteryNominalCurrent = _OgUpsBatteryNominalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 18),
    _OgUpsBatteryNominalCurrent_Type()
)
ogUpsBatteryNominalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsBatteryNominalCurrent.setStatus("current")
if mibBuilder.loadTexts:
    ogUpsBatteryNominalCurrent.setUnits("0.1 Amp DC")
_OgUpsBatteryTemperature_Type = Integer32
_OgUpsBatteryTemperature_Object = MibTableColumn
ogUpsBatteryTemperature = _OgUpsBatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 19),
    _OgUpsBatteryTemperature_Type()
)
ogUpsBatteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsBatteryTemperature.setStatus("current")
if mibBuilder.loadTexts:
    ogUpsBatteryTemperature.setUnits("degrees")
_OgUpsInputFrequency_Type = Integer32
_OgUpsInputFrequency_Object = MibTableColumn
ogUpsInputFrequency = _OgUpsInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 20),
    _OgUpsInputFrequency_Type()
)
ogUpsInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsInputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    ogUpsInputFrequency.setUnits("Hz")
_OgUpsInputNominalFrequency_Type = Integer32
_OgUpsInputNominalFrequency_Object = MibTableColumn
ogUpsInputNominalFrequency = _OgUpsInputNominalFrequency_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 21),
    _OgUpsInputNominalFrequency_Type()
)
ogUpsInputNominalFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsInputNominalFrequency.setStatus("current")
if mibBuilder.loadTexts:
    ogUpsInputNominalFrequency.setUnits("Hz")
_OgUpsInputVoltage_Type = Integer32
_OgUpsInputVoltage_Object = MibTableColumn
ogUpsInputVoltage = _OgUpsInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 22),
    _OgUpsInputVoltage_Type()
)
ogUpsInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    ogUpsInputVoltage.setUnits("RMS Volts")
_OgUpsInputNominalVoltage_Type = Integer32
_OgUpsInputNominalVoltage_Object = MibTableColumn
ogUpsInputNominalVoltage = _OgUpsInputNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 23),
    _OgUpsInputNominalVoltage_Type()
)
ogUpsInputNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsInputNominalVoltage.setStatus("current")
if mibBuilder.loadTexts:
    ogUpsInputNominalVoltage.setUnits("RMS Volts")
_OgUpsInputCurrent_Type = Integer32
_OgUpsInputCurrent_Object = MibTableColumn
ogUpsInputCurrent = _OgUpsInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 24),
    _OgUpsInputCurrent_Type()
)
ogUpsInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsInputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    ogUpsInputCurrent.setUnits("0.1 RMS Amp")
_OgUpsInputNominalCurrent_Type = Integer32
_OgUpsInputNominalCurrent_Object = MibTableColumn
ogUpsInputNominalCurrent = _OgUpsInputNominalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 25),
    _OgUpsInputNominalCurrent_Type()
)
ogUpsInputNominalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsInputNominalCurrent.setStatus("current")
if mibBuilder.loadTexts:
    ogUpsInputNominalCurrent.setUnits("0.1 RMS Amp")
_OgUpsOutputFrequency_Type = Integer32
_OgUpsOutputFrequency_Object = MibTableColumn
ogUpsOutputFrequency = _OgUpsOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 26),
    _OgUpsOutputFrequency_Type()
)
ogUpsOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsOutputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    ogUpsOutputFrequency.setUnits("Hz")
_OgUpsOutputNominalFrequency_Type = Integer32
_OgUpsOutputNominalFrequency_Object = MibTableColumn
ogUpsOutputNominalFrequency = _OgUpsOutputNominalFrequency_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 27),
    _OgUpsOutputNominalFrequency_Type()
)
ogUpsOutputNominalFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsOutputNominalFrequency.setStatus("current")
if mibBuilder.loadTexts:
    ogUpsOutputNominalFrequency.setUnits("Hz")
_OgUpsOutputVoltage_Type = Integer32
_OgUpsOutputVoltage_Object = MibTableColumn
ogUpsOutputVoltage = _OgUpsOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 28),
    _OgUpsOutputVoltage_Type()
)
ogUpsOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsOutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    ogUpsOutputVoltage.setUnits("RMS Volts")
_OgUpsOutputNominalVoltage_Type = Integer32
_OgUpsOutputNominalVoltage_Object = MibTableColumn
ogUpsOutputNominalVoltage = _OgUpsOutputNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 29),
    _OgUpsOutputNominalVoltage_Type()
)
ogUpsOutputNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsOutputNominalVoltage.setStatus("current")
if mibBuilder.loadTexts:
    ogUpsOutputNominalVoltage.setUnits("RMS Volts")
_OgUpsOutputCurrent_Type = Integer32
_OgUpsOutputCurrent_Object = MibTableColumn
ogUpsOutputCurrent = _OgUpsOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 30),
    _OgUpsOutputCurrent_Type()
)
ogUpsOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsOutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    ogUpsOutputCurrent.setUnits("0.1 RMS Amp")
_OgUpsOutputNominalCurrent_Type = Integer32
_OgUpsOutputNominalCurrent_Object = MibTableColumn
ogUpsOutputNominalCurrent = _OgUpsOutputNominalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 31),
    _OgUpsOutputNominalCurrent_Type()
)
ogUpsOutputNominalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsOutputNominalCurrent.setStatus("current")
if mibBuilder.loadTexts:
    ogUpsOutputNominalCurrent.setUnits("0.1 RMS Amp")


class _OgUpsOutputLoad_Type(Integer32):
    """Custom type ogUpsOutputLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_OgUpsOutputLoad_Type.__name__ = "Integer32"
_OgUpsOutputLoad_Object = MibTableColumn
ogUpsOutputLoad = _OgUpsOutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 32),
    _OgUpsOutputLoad_Type()
)
ogUpsOutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsOutputLoad.setStatus("current")
if mibBuilder.loadTexts:
    ogUpsOutputLoad.setUnits("percent")
_OgUpsOutputPower_Type = Integer32
_OgUpsOutputPower_Object = MibTableColumn
ogUpsOutputPower = _OgUpsOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 33),
    _OgUpsOutputPower_Type()
)
ogUpsOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    ogUpsOutputPower.setUnits("Volt-Amps")
_OgUpsOutputTruePower_Type = Integer32
_OgUpsOutputTruePower_Object = MibTableColumn
ogUpsOutputTruePower = _OgUpsOutputTruePower_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 34),
    _OgUpsOutputTruePower_Type()
)
ogUpsOutputTruePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsOutputTruePower.setStatus("current")
if mibBuilder.loadTexts:
    ogUpsOutputTruePower.setUnits("Watts")
_OgUpsCounter_Type = Counter32
_OgUpsCounter_Object = MibTableColumn
ogUpsCounter = _OgUpsCounter_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 14, 1, 35),
    _OgUpsCounter_Type()
)
ogUpsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogUpsCounter.setStatus("current")
_OgRpcTable_Object = MibTable
ogRpcTable = _OgRpcTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 15)
)
if mibBuilder.loadTexts:
    ogRpcTable.setStatus("current")
_OgRpcEntry_Object = MibTableRow
ogRpcEntry = _OgRpcEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 15, 1)
)
ogRpcEntry.setIndexNames(
    (0, "OG-STATUSv2-MIB", "ogRpcIndex"),
)
if mibBuilder.loadTexts:
    ogRpcEntry.setStatus("current")


class _OgRpcIndex_Type(Integer32):
    """Custom type ogRpcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OgRpcIndex_Type.__name__ = "Integer32"
_OgRpcIndex_Object = MibTableColumn
ogRpcIndex = _OgRpcIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 15, 1, 1),
    _OgRpcIndex_Type()
)
ogRpcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogRpcIndex.setStatus("current")


class _OgRpcName_Type(DisplayString):
    """Custom type ogRpcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgRpcName_Type.__name__ = "DisplayString"
_OgRpcName_Object = MibTableColumn
ogRpcName = _OgRpcName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 15, 1, 2),
    _OgRpcName_Type()
)
ogRpcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogRpcName.setStatus("current")


class _OgRpcDescription_Type(DisplayString):
    """Custom type ogRpcDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgRpcDescription_Type.__name__ = "DisplayString"
_OgRpcDescription_Object = MibTableColumn
ogRpcDescription = _OgRpcDescription_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 15, 1, 3),
    _OgRpcDescription_Type()
)
ogRpcDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogRpcDescription.setStatus("current")


class _OgRpcType_Type(DisplayString):
    """Custom type ogRpcType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgRpcType_Type.__name__ = "DisplayString"
_OgRpcType_Object = MibTableColumn
ogRpcType = _OgRpcType_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 15, 1, 4),
    _OgRpcType_Type()
)
ogRpcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogRpcType.setStatus("current")


class _OgRpcLogEnabled_Type(Integer32):
    """Custom type ogRpcLogEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_OgRpcLogEnabled_Type.__name__ = "Integer32"
_OgRpcLogEnabled_Object = MibTableColumn
ogRpcLogEnabled = _OgRpcLogEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 15, 1, 5),
    _OgRpcLogEnabled_Type()
)
ogRpcLogEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogRpcLogEnabled.setStatus("current")
_OgRpcOutletTotal_Type = Counter32
_OgRpcOutletTotal_Object = MibTableColumn
ogRpcOutletTotal = _OgRpcOutletTotal_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 15, 1, 6),
    _OgRpcOutletTotal_Type()
)
ogRpcOutletTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogRpcOutletTotal.setStatus("current")
_OgRpcMaxTemperature_Type = Integer32
_OgRpcMaxTemperature_Object = MibTableColumn
ogRpcMaxTemperature = _OgRpcMaxTemperature_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 15, 1, 7),
    _OgRpcMaxTemperature_Type()
)
ogRpcMaxTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogRpcMaxTemperature.setStatus("current")
if mibBuilder.loadTexts:
    ogRpcMaxTemperature.setUnits("degrees")


class _OgRpcConnectType_Type(Integer32):
    """Custom type ogRpcConnectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 2),
          ("serial", 1))
    )


_OgRpcConnectType_Type.__name__ = "Integer32"
_OgRpcConnectType_Object = MibTableColumn
ogRpcConnectType = _OgRpcConnectType_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 15, 1, 8),
    _OgRpcConnectType_Type()
)
ogRpcConnectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogRpcConnectType.setStatus("current")
_OgRpcInputFrequency_Type = Integer32
_OgRpcInputFrequency_Object = MibTableColumn
ogRpcInputFrequency = _OgRpcInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 15, 1, 9),
    _OgRpcInputFrequency_Type()
)
ogRpcInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogRpcInputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    ogRpcInputFrequency.setUnits("Hz")
_OgRpcInputVoltage_Type = Integer32
_OgRpcInputVoltage_Object = MibTableColumn
ogRpcInputVoltage = _OgRpcInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 15, 1, 10),
    _OgRpcInputVoltage_Type()
)
ogRpcInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogRpcInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    ogRpcInputVoltage.setUnits("RMS Volts")
_OgRpcInputCurrent_Type = Integer32
_OgRpcInputCurrent_Object = MibTableColumn
ogRpcInputCurrent = _OgRpcInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 15, 1, 11),
    _OgRpcInputCurrent_Type()
)
ogRpcInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogRpcInputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    ogRpcInputCurrent.setUnits("0.1 RMS Amp")
_OgRpcCounter_Type = Counter32
_OgRpcCounter_Object = MibTableColumn
ogRpcCounter = _OgRpcCounter_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 15, 1, 12),
    _OgRpcCounter_Type()
)
ogRpcCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogRpcCounter.setStatus("current")
_OgRpcOutletTable_Object = MibTable
ogRpcOutletTable = _OgRpcOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 16)
)
if mibBuilder.loadTexts:
    ogRpcOutletTable.setStatus("current")
_OgRpcOutletEntry_Object = MibTableRow
ogRpcOutletEntry = _OgRpcOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 16, 1)
)
ogRpcOutletEntry.setIndexNames(
    (0, "OG-STATUSv2-MIB", "ogRpcIndex"),
    (0, "OG-STATUSv2-MIB", "ogRpcOutletIndex"),
)
if mibBuilder.loadTexts:
    ogRpcOutletEntry.setStatus("current")


class _OgRpcOutletIndex_Type(Integer32):
    """Custom type ogRpcOutletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgRpcOutletIndex_Type.__name__ = "Integer32"
_OgRpcOutletIndex_Object = MibTableColumn
ogRpcOutletIndex = _OgRpcOutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 16, 1, 1),
    _OgRpcOutletIndex_Type()
)
ogRpcOutletIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogRpcOutletIndex.setStatus("current")
_OgRpcOutletRpc_Type = ObjectIdentifier
_OgRpcOutletRpc_Object = MibTableColumn
ogRpcOutletRpc = _OgRpcOutletRpc_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 16, 1, 2),
    _OgRpcOutletRpc_Type()
)
ogRpcOutletRpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogRpcOutletRpc.setStatus("current")


class _OgRpcOutletName_Type(DisplayString):
    """Custom type ogRpcOutletName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgRpcOutletName_Type.__name__ = "DisplayString"
_OgRpcOutletName_Object = MibTableColumn
ogRpcOutletName = _OgRpcOutletName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 16, 1, 3),
    _OgRpcOutletName_Type()
)
ogRpcOutletName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogRpcOutletName.setStatus("current")


class _OgRpcOutletState_Type(Integer32):
    """Custom type ogRpcOutletState based on Integer32"""
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
        *(("off", 2),
          ("on", 1),
          ("transitioning", 3),
          ("unavailable", 4))
    )


_OgRpcOutletState_Type.__name__ = "Integer32"
_OgRpcOutletState_Object = MibTableColumn
ogRpcOutletState = _OgRpcOutletState_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 16, 1, 4),
    _OgRpcOutletState_Type()
)
ogRpcOutletState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogRpcOutletState.setStatus("current")
_OgRpcOutletFrequency_Type = Integer32
_OgRpcOutletFrequency_Object = MibTableColumn
ogRpcOutletFrequency = _OgRpcOutletFrequency_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 16, 1, 5),
    _OgRpcOutletFrequency_Type()
)
ogRpcOutletFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogRpcOutletFrequency.setStatus("current")
if mibBuilder.loadTexts:
    ogRpcOutletFrequency.setUnits("Hz")


class _OgRpcOutletVoltage_Type(Integer32):
    """Custom type ogRpcOutletVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2640),
    )


_OgRpcOutletVoltage_Type.__name__ = "Integer32"
_OgRpcOutletVoltage_Object = MibTableColumn
ogRpcOutletVoltage = _OgRpcOutletVoltage_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 16, 1, 6),
    _OgRpcOutletVoltage_Type()
)
ogRpcOutletVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogRpcOutletVoltage.setStatus("current")
if mibBuilder.loadTexts:
    ogRpcOutletVoltage.setUnits("0.01 Amps")


class _OgRpcOutletCurrent_Type(Integer32):
    """Custom type ogRpcOutletCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 25500),
    )


_OgRpcOutletCurrent_Type.__name__ = "Integer32"
_OgRpcOutletCurrent_Object = MibTableColumn
ogRpcOutletCurrent = _OgRpcOutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 16, 1, 7),
    _OgRpcOutletCurrent_Type()
)
ogRpcOutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogRpcOutletCurrent.setStatus("current")
if mibBuilder.loadTexts:
    ogRpcOutletCurrent.setUnits("0.01 Amps")


class _OgRpcOutletLoad_Type(Integer32):
    """Custom type ogRpcOutletLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_OgRpcOutletLoad_Type.__name__ = "Integer32"
_OgRpcOutletLoad_Object = MibTableColumn
ogRpcOutletLoad = _OgRpcOutletLoad_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 16, 1, 8),
    _OgRpcOutletLoad_Type()
)
ogRpcOutletLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogRpcOutletLoad.setStatus("current")
if mibBuilder.loadTexts:
    ogRpcOutletLoad.setUnits("percent")
_OgCellModemTable_Object = MibTable
ogCellModemTable = _OgCellModemTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 17)
)
if mibBuilder.loadTexts:
    ogCellModemTable.setStatus("current")
_OgCellModemEntry_Object = MibTableRow
ogCellModemEntry = _OgCellModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 17, 1)
)
ogCellModemEntry.setIndexNames(
    (0, "OG-STATUSv2-MIB", "ogCellModemIndex"),
)
if mibBuilder.loadTexts:
    ogCellModemEntry.setStatus("current")


class _OgCellModemIndex_Type(Integer32):
    """Custom type ogCellModemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgCellModemIndex_Type.__name__ = "Integer32"
_OgCellModemIndex_Object = MibTableColumn
ogCellModemIndex = _OgCellModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 17, 1, 1),
    _OgCellModemIndex_Type()
)
ogCellModemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogCellModemIndex.setStatus("current")


class _OgCellModemVendor_Type(DisplayString):
    """Custom type ogCellModemVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgCellModemVendor_Type.__name__ = "DisplayString"
_OgCellModemVendor_Object = MibTableColumn
ogCellModemVendor = _OgCellModemVendor_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 17, 1, 2),
    _OgCellModemVendor_Type()
)
ogCellModemVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCellModemVendor.setStatus("current")


class _OgCellModemModel_Type(DisplayString):
    """Custom type ogCellModemModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgCellModemModel_Type.__name__ = "DisplayString"
_OgCellModemModel_Object = MibTableColumn
ogCellModemModel = _OgCellModemModel_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 17, 1, 3),
    _OgCellModemModel_Type()
)
ogCellModemModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCellModemModel.setStatus("current")


class _OgCellModemEnabled_Type(Integer32):
    """Custom type ogCellModemEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_OgCellModemEnabled_Type.__name__ = "Integer32"
_OgCellModemEnabled_Object = MibTableColumn
ogCellModemEnabled = _OgCellModemEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 17, 1, 4),
    _OgCellModemEnabled_Type()
)
ogCellModemEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCellModemEnabled.setStatus("current")


class _OgCellModemConnected_Type(Integer32):
    """Custom type ogCellModemConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 2))
    )


_OgCellModemConnected_Type.__name__ = "Integer32"
_OgCellModemConnected_Object = MibTableColumn
ogCellModemConnected = _OgCellModemConnected_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 17, 1, 5),
    _OgCellModemConnected_Type()
)
ogCellModemConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCellModemConnected.setStatus("current")


class _OgCellModemNetwork_Type(DisplayString):
    """Custom type ogCellModemNetwork based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgCellModemNetwork_Type.__name__ = "DisplayString"
_OgCellModemNetwork_Object = MibTableColumn
ogCellModemNetwork = _OgCellModemNetwork_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 17, 1, 6),
    _OgCellModemNetwork_Type()
)
ogCellModemNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCellModemNetwork.setStatus("current")


class _OgCellModemRegistered_Type(Integer32):
    """Custom type ogCellModemRegistered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("registered", 1),
          ("unregistered", 2))
    )


_OgCellModemRegistered_Type.__name__ = "Integer32"
_OgCellModemRegistered_Object = MibTableColumn
ogCellModemRegistered = _OgCellModemRegistered_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 17, 1, 7),
    _OgCellModemRegistered_Type()
)
ogCellModemRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCellModemRegistered.setStatus("current")
_OgCellModemTower_Type = Integer32
_OgCellModemTower_Object = MibTableColumn
ogCellModemTower = _OgCellModemTower_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 17, 1, 8),
    _OgCellModemTower_Type()
)
ogCellModemTower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCellModemTower.setStatus("current")


class _OgCellModemRadioTechnology_Type(Integer32):
    """Custom type ogCellModemRadioTechnology based on Integer32"""
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
        *(("cdma", 2),
          ("evdo", 3),
          ("gsm", 4),
          ("lte", 6),
          ("umts", 5),
          ("unavailable", 1))
    )


_OgCellModemRadioTechnology_Type.__name__ = "Integer32"
_OgCellModemRadioTechnology_Object = MibTableColumn
ogCellModemRadioTechnology = _OgCellModemRadioTechnology_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 17, 1, 9),
    _OgCellModemRadioTechnology_Type()
)
ogCellModemRadioTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCellModemRadioTechnology.setStatus("current")


class _OgCellModemApn_Type(DisplayString):
    """Custom type ogCellModemApn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgCellModemApn_Type.__name__ = "DisplayString"
_OgCellModemApn_Object = MibTableColumn
ogCellModemApn = _OgCellModemApn_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 17, 1, 10),
    _OgCellModemApn_Type()
)
ogCellModemApn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCellModemApn.setStatus("current")


class _OgCellModem3gRssi_Type(Integer32):
    """Custom type ogCellModem3gRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, 99),
    )


_OgCellModem3gRssi_Type.__name__ = "Integer32"
_OgCellModem3gRssi_Object = MibTableColumn
ogCellModem3gRssi = _OgCellModem3gRssi_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 17, 1, 11),
    _OgCellModem3gRssi_Type()
)
ogCellModem3gRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCellModem3gRssi.setStatus("current")


class _OgCellModem4gRssi_Type(Integer32):
    """Custom type ogCellModem4gRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, 99),
    )


_OgCellModem4gRssi_Type.__name__ = "Integer32"
_OgCellModem4gRssi_Object = MibTableColumn
ogCellModem4gRssi = _OgCellModem4gRssi_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 17, 1, 12),
    _OgCellModem4gRssi_Type()
)
ogCellModem4gRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCellModem4gRssi.setStatus("current")
_OgCellModemSessionTime_Type = Counter32
_OgCellModemSessionTime_Object = MibTableColumn
ogCellModemSessionTime = _OgCellModemSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 17, 1, 13),
    _OgCellModemSessionTime_Type()
)
ogCellModemSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCellModemSessionTime.setStatus("current")
_OgCellModemSelectedSimCard_Type = Counter32
_OgCellModemSelectedSimCard_Object = MibTableColumn
ogCellModemSelectedSimCard = _OgCellModemSelectedSimCard_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 17, 1, 14),
    _OgCellModemSelectedSimCard_Type()
)
ogCellModemSelectedSimCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCellModemSelectedSimCard.setStatus("current")
_OgCellModemTemperature_Type = Integer32
_OgCellModemTemperature_Object = MibTableColumn
ogCellModemTemperature = _OgCellModemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 17, 1, 15),
    _OgCellModemTemperature_Type()
)
ogCellModemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCellModemTemperature.setStatus("current")
if mibBuilder.loadTexts:
    ogCellModemTemperature.setUnits("degrees")
_OgCellModemCounter_Type = Counter32
_OgCellModemCounter_Object = MibTableColumn
ogCellModemCounter = _OgCellModemCounter_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 17, 1, 16),
    _OgCellModemCounter_Type()
)
ogCellModemCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCellModemCounter.setStatus("current")
_OgWifiClientTable_Object = MibTable
ogWifiClientTable = _OgWifiClientTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 18)
)
if mibBuilder.loadTexts:
    ogWifiClientTable.setStatus("current")
_OgWifiClientEntry_Object = MibTableRow
ogWifiClientEntry = _OgWifiClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 18, 1)
)
ogWifiClientEntry.setIndexNames(
    (0, "OG-STATUSv2-MIB", "ogWifiClientIndex"),
)
if mibBuilder.loadTexts:
    ogWifiClientEntry.setStatus("current")


class _OgWifiClientIndex_Type(Integer32):
    """Custom type ogWifiClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgWifiClientIndex_Type.__name__ = "Integer32"
_OgWifiClientIndex_Object = MibTableColumn
ogWifiClientIndex = _OgWifiClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 18, 1, 1),
    _OgWifiClientIndex_Type()
)
ogWifiClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogWifiClientIndex.setStatus("current")


class _OgWifiClientInterface_Type(DisplayString):
    """Custom type ogWifiClientInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_OgWifiClientInterface_Type.__name__ = "DisplayString"
_OgWifiClientInterface_Object = MibTableColumn
ogWifiClientInterface = _OgWifiClientInterface_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 18, 1, 2),
    _OgWifiClientInterface_Type()
)
ogWifiClientInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiClientInterface.setStatus("current")


class _OgWifiClientEnabled_Type(Integer32):
    """Custom type ogWifiClientEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_OgWifiClientEnabled_Type.__name__ = "Integer32"
_OgWifiClientEnabled_Object = MibTableColumn
ogWifiClientEnabled = _OgWifiClientEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 18, 1, 3),
    _OgWifiClientEnabled_Type()
)
ogWifiClientEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiClientEnabled.setStatus("current")


class _OgWifiClientEssid_Type(DisplayString):
    """Custom type ogWifiClientEssid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgWifiClientEssid_Type.__name__ = "DisplayString"
_OgWifiClientEssid_Object = MibTableColumn
ogWifiClientEssid = _OgWifiClientEssid_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 18, 1, 4),
    _OgWifiClientEssid_Type()
)
ogWifiClientEssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiClientEssid.setStatus("current")


class _OgWifiClientIeeeMode_Type(Integer32):
    """Custom type ogWifiClientIeeeMode based on Integer32"""
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
        *(("ieee802Dot11ABGN", 5),
          ("ieee802Dot11B", 2),
          ("ieee802Dot11BG", 3),
          ("ieee802Dot11BGN", 4),
          ("unavailable", 1))
    )


_OgWifiClientIeeeMode_Type.__name__ = "Integer32"
_OgWifiClientIeeeMode_Object = MibTableColumn
ogWifiClientIeeeMode = _OgWifiClientIeeeMode_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 18, 1, 5),
    _OgWifiClientIeeeMode_Type()
)
ogWifiClientIeeeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiClientIeeeMode.setStatus("current")


class _OgWifiClientMode_Type(Integer32):
    """Custom type ogWifiClientMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adhoc", 3),
          ("managed", 2),
          ("unavailable", 1))
    )


_OgWifiClientMode_Type.__name__ = "Integer32"
_OgWifiClientMode_Object = MibTableColumn
ogWifiClientMode = _OgWifiClientMode_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 18, 1, 6),
    _OgWifiClientMode_Type()
)
ogWifiClientMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiClientMode.setStatus("current")
_OgWifiClientFrequency_Type = Unsigned32
_OgWifiClientFrequency_Object = MibTableColumn
ogWifiClientFrequency = _OgWifiClientFrequency_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 18, 1, 7),
    _OgWifiClientFrequency_Type()
)
ogWifiClientFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiClientFrequency.setStatus("current")
if mibBuilder.loadTexts:
    ogWifiClientFrequency.setUnits("0.0001 THz")


class _OgWifiClientApMac_Type(DisplayString):
    """Custom type ogWifiClientApMac based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OgWifiClientApMac_Type.__name__ = "DisplayString"
_OgWifiClientApMac_Object = MibTableColumn
ogWifiClientApMac = _OgWifiClientApMac_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 18, 1, 8),
    _OgWifiClientApMac_Type()
)
ogWifiClientApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiClientApMac.setStatus("current")
_OgWifiClientBitRate_Type = Unsigned32
_OgWifiClientBitRate_Object = MibTableColumn
ogWifiClientBitRate = _OgWifiClientBitRate_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 18, 1, 9),
    _OgWifiClientBitRate_Type()
)
ogWifiClientBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiClientBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ogWifiClientBitRate.setUnits("Mb/s")
_OgWifiClientTxPower_Type = Integer32
_OgWifiClientTxPower_Object = MibTableColumn
ogWifiClientTxPower = _OgWifiClientTxPower_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 18, 1, 10),
    _OgWifiClientTxPower_Type()
)
ogWifiClientTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiClientTxPower.setStatus("current")
if mibBuilder.loadTexts:
    ogWifiClientTxPower.setUnits("dBm")
_OgWifiClientLinkQuality_Type = Unsigned32
_OgWifiClientLinkQuality_Object = MibTableColumn
ogWifiClientLinkQuality = _OgWifiClientLinkQuality_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 18, 1, 11),
    _OgWifiClientLinkQuality_Type()
)
ogWifiClientLinkQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiClientLinkQuality.setStatus("current")
if mibBuilder.loadTexts:
    ogWifiClientLinkQuality.setUnits("percent")
_OgWifiClientRssi_Type = Integer32
_OgWifiClientRssi_Object = MibTableColumn
ogWifiClientRssi = _OgWifiClientRssi_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 18, 1, 12),
    _OgWifiClientRssi_Type()
)
ogWifiClientRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiClientRssi.setStatus("current")
if mibBuilder.loadTexts:
    ogWifiClientRssi.setUnits("dBm")
_OgWifiClientRxInvalidNwid_Type = Counter32
_OgWifiClientRxInvalidNwid_Object = MibTableColumn
ogWifiClientRxInvalidNwid = _OgWifiClientRxInvalidNwid_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 18, 1, 13),
    _OgWifiClientRxInvalidNwid_Type()
)
ogWifiClientRxInvalidNwid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiClientRxInvalidNwid.setStatus("current")
_OgWifiClientRxInvalidCrypt_Type = Counter32
_OgWifiClientRxInvalidCrypt_Object = MibTableColumn
ogWifiClientRxInvalidCrypt = _OgWifiClientRxInvalidCrypt_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 18, 1, 14),
    _OgWifiClientRxInvalidCrypt_Type()
)
ogWifiClientRxInvalidCrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiClientRxInvalidCrypt.setStatus("current")
_OgWifiClientRxInvalidFrag_Type = Counter32
_OgWifiClientRxInvalidFrag_Object = MibTableColumn
ogWifiClientRxInvalidFrag = _OgWifiClientRxInvalidFrag_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 18, 1, 15),
    _OgWifiClientRxInvalidFrag_Type()
)
ogWifiClientRxInvalidFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiClientRxInvalidFrag.setStatus("current")
_OgWifiClientRxInvalidRetries_Type = Counter32
_OgWifiClientRxInvalidRetries_Object = MibTableColumn
ogWifiClientRxInvalidRetries = _OgWifiClientRxInvalidRetries_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 18, 1, 16),
    _OgWifiClientRxInvalidRetries_Type()
)
ogWifiClientRxInvalidRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiClientRxInvalidRetries.setStatus("current")
_OgWifiClientRxInvalidMisc_Type = Counter32
_OgWifiClientRxInvalidMisc_Object = MibTableColumn
ogWifiClientRxInvalidMisc = _OgWifiClientRxInvalidMisc_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 18, 1, 17),
    _OgWifiClientRxInvalidMisc_Type()
)
ogWifiClientRxInvalidMisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiClientRxInvalidMisc.setStatus("current")
_OgWifiClientMissedBeacon_Type = Counter32
_OgWifiClientMissedBeacon_Object = MibTableColumn
ogWifiClientMissedBeacon = _OgWifiClientMissedBeacon_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 18, 1, 18),
    _OgWifiClientMissedBeacon_Type()
)
ogWifiClientMissedBeacon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiClientMissedBeacon.setStatus("current")
_OgWifiClientCounter_Type = Counter32
_OgWifiClientCounter_Object = MibTableColumn
ogWifiClientCounter = _OgWifiClientCounter_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 18, 1, 19),
    _OgWifiClientCounter_Type()
)
ogWifiClientCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiClientCounter.setStatus("current")
_OgWifiApTable_Object = MibTable
ogWifiApTable = _OgWifiApTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 19)
)
if mibBuilder.loadTexts:
    ogWifiApTable.setStatus("current")
_OgWifiApEntry_Object = MibTableRow
ogWifiApEntry = _OgWifiApEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 19, 1)
)
ogWifiApEntry.setIndexNames(
    (0, "OG-STATUSv2-MIB", "ogWifiApIndex"),
)
if mibBuilder.loadTexts:
    ogWifiApEntry.setStatus("current")


class _OgWifiApIndex_Type(Integer32):
    """Custom type ogWifiApIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgWifiApIndex_Type.__name__ = "Integer32"
_OgWifiApIndex_Object = MibTableColumn
ogWifiApIndex = _OgWifiApIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 19, 1, 1),
    _OgWifiApIndex_Type()
)
ogWifiApIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogWifiApIndex.setStatus("current")


class _OgWifiApInterface_Type(DisplayString):
    """Custom type ogWifiApInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_OgWifiApInterface_Type.__name__ = "DisplayString"
_OgWifiApInterface_Object = MibTableColumn
ogWifiApInterface = _OgWifiApInterface_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 19, 1, 2),
    _OgWifiApInterface_Type()
)
ogWifiApInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiApInterface.setStatus("current")


class _OgWifiApEnabled_Type(Integer32):
    """Custom type ogWifiApEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_OgWifiApEnabled_Type.__name__ = "Integer32"
_OgWifiApEnabled_Object = MibTableColumn
ogWifiApEnabled = _OgWifiApEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 19, 1, 3),
    _OgWifiApEnabled_Type()
)
ogWifiApEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiApEnabled.setStatus("current")


class _OgWifiApSsid_Type(DisplayString):
    """Custom type ogWifiApSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgWifiApSsid_Type.__name__ = "DisplayString"
_OgWifiApSsid_Object = MibTableColumn
ogWifiApSsid = _OgWifiApSsid_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 19, 1, 4),
    _OgWifiApSsid_Type()
)
ogWifiApSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiApSsid.setStatus("current")


class _OgWifiApIeeeMode_Type(Integer32):
    """Custom type ogWifiApIeeeMode based on Integer32"""
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
        *(("ieee802Dot11ABGN", 5),
          ("ieee802Dot11B", 2),
          ("ieee802Dot11BG", 3),
          ("ieee802Dot11BGN", 4),
          ("unavailable", 1))
    )


_OgWifiApIeeeMode_Type.__name__ = "Integer32"
_OgWifiApIeeeMode_Object = MibTableColumn
ogWifiApIeeeMode = _OgWifiApIeeeMode_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 19, 1, 5),
    _OgWifiApIeeeMode_Type()
)
ogWifiApIeeeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiApIeeeMode.setStatus("current")
_OgWifiApFrequency_Type = Unsigned32
_OgWifiApFrequency_Object = MibTableColumn
ogWifiApFrequency = _OgWifiApFrequency_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 19, 1, 6),
    _OgWifiApFrequency_Type()
)
ogWifiApFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiApFrequency.setStatus("current")
if mibBuilder.loadTexts:
    ogWifiApFrequency.setUnits("0.0001 THz")
_OgWifiApTxPower_Type = Integer32
_OgWifiApTxPower_Object = MibTableColumn
ogWifiApTxPower = _OgWifiApTxPower_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 19, 1, 7),
    _OgWifiApTxPower_Type()
)
ogWifiApTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiApTxPower.setStatus("current")
if mibBuilder.loadTexts:
    ogWifiApTxPower.setUnits("dBm")
_OgWifiApCounter_Type = Counter32
_OgWifiApCounter_Object = MibTableColumn
ogWifiApCounter = _OgWifiApCounter_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 19, 1, 8),
    _OgWifiApCounter_Type()
)
ogWifiApCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiApCounter.setStatus("current")
_OgWifiApClientTable_Object = MibTable
ogWifiApClientTable = _OgWifiApClientTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 20)
)
if mibBuilder.loadTexts:
    ogWifiApClientTable.setStatus("current")
_OgWifiApClientEntry_Object = MibTableRow
ogWifiApClientEntry = _OgWifiApClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 20, 1)
)
ogWifiApClientEntry.setIndexNames(
    (0, "OG-STATUSv2-MIB", "ogWifiApIndex"),
    (0, "OG-STATUSv2-MIB", "ogWifiApClientIndex"),
)
if mibBuilder.loadTexts:
    ogWifiApClientEntry.setStatus("current")


class _OgWifiApClientIndex_Type(Integer32):
    """Custom type ogWifiApClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgWifiApClientIndex_Type.__name__ = "Integer32"
_OgWifiApClientIndex_Object = MibTableColumn
ogWifiApClientIndex = _OgWifiApClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 20, 1, 1),
    _OgWifiApClientIndex_Type()
)
ogWifiApClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogWifiApClientIndex.setStatus("current")
_OgWifiApClientAp_Type = ObjectIdentifier
_OgWifiApClientAp_Object = MibTableColumn
ogWifiApClientAp = _OgWifiApClientAp_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 20, 1, 2),
    _OgWifiApClientAp_Type()
)
ogWifiApClientAp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiApClientAp.setStatus("current")


class _OgWifiApClientMac_Type(DisplayString):
    """Custom type ogWifiApClientMac based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OgWifiApClientMac_Type.__name__ = "DisplayString"
_OgWifiApClientMac_Object = MibTableColumn
ogWifiApClientMac = _OgWifiApClientMac_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 20, 1, 3),
    _OgWifiApClientMac_Type()
)
ogWifiApClientMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiApClientMac.setStatus("current")
_OgWifiApClientInactiveTime_Type = Counter32
_OgWifiApClientInactiveTime_Object = MibTableColumn
ogWifiApClientInactiveTime = _OgWifiApClientInactiveTime_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 20, 1, 4),
    _OgWifiApClientInactiveTime_Type()
)
ogWifiApClientInactiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiApClientInactiveTime.setStatus("current")
if mibBuilder.loadTexts:
    ogWifiApClientInactiveTime.setUnits("milliseconds")
_OgWifiApClientRxBytes_Type = Counter32
_OgWifiApClientRxBytes_Object = MibTableColumn
ogWifiApClientRxBytes = _OgWifiApClientRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 20, 1, 5),
    _OgWifiApClientRxBytes_Type()
)
ogWifiApClientRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiApClientRxBytes.setStatus("current")
if mibBuilder.loadTexts:
    ogWifiApClientRxBytes.setUnits("bytes")
_OgWifiApClientRxPackets_Type = Counter32
_OgWifiApClientRxPackets_Object = MibTableColumn
ogWifiApClientRxPackets = _OgWifiApClientRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 20, 1, 6),
    _OgWifiApClientRxPackets_Type()
)
ogWifiApClientRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiApClientRxPackets.setStatus("current")
if mibBuilder.loadTexts:
    ogWifiApClientRxPackets.setUnits("packets")
_OgWifiApClientTxBytes_Type = Counter32
_OgWifiApClientTxBytes_Object = MibTableColumn
ogWifiApClientTxBytes = _OgWifiApClientTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 20, 1, 7),
    _OgWifiApClientTxBytes_Type()
)
ogWifiApClientTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiApClientTxBytes.setStatus("current")
if mibBuilder.loadTexts:
    ogWifiApClientTxBytes.setUnits("bytes")
_OgWifiApClientTxPackets_Type = Counter32
_OgWifiApClientTxPackets_Object = MibTableColumn
ogWifiApClientTxPackets = _OgWifiApClientTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 20, 1, 8),
    _OgWifiApClientTxPackets_Type()
)
ogWifiApClientTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiApClientTxPackets.setStatus("current")
if mibBuilder.loadTexts:
    ogWifiApClientTxPackets.setUnits("packets")
_OgWifiApClientRssi_Type = Integer32
_OgWifiApClientRssi_Object = MibTableColumn
ogWifiApClientRssi = _OgWifiApClientRssi_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 20, 1, 9),
    _OgWifiApClientRssi_Type()
)
ogWifiApClientRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiApClientRssi.setStatus("current")
if mibBuilder.loadTexts:
    ogWifiApClientRssi.setUnits("dBm")
_OgWifiApClientTxBitRate_Type = Unsigned32
_OgWifiApClientTxBitRate_Object = MibTableColumn
ogWifiApClientTxBitRate = _OgWifiApClientTxBitRate_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 20, 1, 10),
    _OgWifiApClientTxBitRate_Type()
)
ogWifiApClientTxBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogWifiApClientTxBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ogWifiApClientTxBitRate.setUnits("Mb/s")
_OgCheckTable_Object = MibTable
ogCheckTable = _OgCheckTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 21)
)
if mibBuilder.loadTexts:
    ogCheckTable.setStatus("current")
_OgCheckEntry_Object = MibTableRow
ogCheckEntry = _OgCheckEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 21, 1)
)
ogCheckEntry.setIndexNames(
    (0, "OG-STATUSv2-MIB", "ogCheckIndex"),
)
if mibBuilder.loadTexts:
    ogCheckEntry.setStatus("current")


class _OgCheckIndex_Type(Integer32):
    """Custom type ogCheckIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgCheckIndex_Type.__name__ = "Integer32"
_OgCheckIndex_Object = MibTableColumn
ogCheckIndex = _OgCheckIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 21, 1, 1),
    _OgCheckIndex_Type()
)
ogCheckIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogCheckIndex.setStatus("current")


class _OgCheckName_Type(DisplayString):
    """Custom type ogCheckName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgCheckName_Type.__name__ = "DisplayString"
_OgCheckName_Object = MibTableColumn
ogCheckName = _OgCheckName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 21, 1, 2),
    _OgCheckName_Type()
)
ogCheckName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCheckName.setStatus("current")


class _OgCheckRepeatTimeout_Type(Integer32):
    """Custom type ogCheckRepeatTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgCheckRepeatTimeout_Type.__name__ = "Integer32"
_OgCheckRepeatTimeout_Object = MibTableColumn
ogCheckRepeatTimeout = _OgCheckRepeatTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 21, 1, 3),
    _OgCheckRepeatTimeout_Type()
)
ogCheckRepeatTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCheckRepeatTimeout.setStatus("current")


class _OgCheckResetTimeout_Type(Integer32):
    """Custom type ogCheckResetTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgCheckResetTimeout_Type.__name__ = "Integer32"
_OgCheckResetTimeout_Object = MibTableColumn
ogCheckResetTimeout = _OgCheckResetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 21, 1, 4),
    _OgCheckResetTimeout_Type()
)
ogCheckResetTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCheckResetTimeout.setStatus("current")


class _OgCheckType_Type(Integer32):
    """Custom type ogCheckType based on Integer32"""
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
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cellApn", 29),
          ("cellData", 27),
          ("cellMessage", 26),
          ("cellNetwork", 31),
          ("cellSignal", 28),
          ("cellTower", 30),
          ("custom", 255),
          ("dialPoolHealth", 36),
          ("dioInput", 11),
          ("envHumidity", 10),
          ("envTemperature", 9),
          ("hostPing", 5),
          ("hostService", 6),
          ("hostUser", 7),
          ("netInterface", 12),
          ("powerSupplyInputVoltage", 13),
          ("powerSupplyOutputCurrent", 14),
          ("powerSupplyTemperature", 15),
          ("rpcInput", 23),
          ("rpcOutletOutput", 25),
          ("rpcOutletState", 24),
          ("serialPattern", 4),
          ("serialSignal", 2),
          ("serialUser", 3),
          ("unknown", 1),
          ("upsBatteryCharge", 17),
          ("upsBatteryTemperature", 18),
          ("upsInputFrequency", 20),
          ("upsInputVoltage", 16),
          ("upsOutputLoad", 19),
          ("upsStateLowBattery", 22),
          ("upsStateOnBattery", 21),
          ("webUser", 8),
          ("wirelessApAssociation", 34),
          ("wirelessApAuthentication", 35),
          ("wirelessClientConnect", 32),
          ("wirelessClientSignal", 33))
    )


_OgCheckType_Type.__name__ = "Integer32"
_OgCheckType_Object = MibTableColumn
ogCheckType = _OgCheckType_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 21, 1, 5),
    _OgCheckType_Type()
)
ogCheckType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCheckType.setStatus("current")
_OgCheckTriggerActions_Type = Counter32
_OgCheckTriggerActions_Object = MibTableColumn
ogCheckTriggerActions = _OgCheckTriggerActions_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 21, 1, 6),
    _OgCheckTriggerActions_Type()
)
ogCheckTriggerActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCheckTriggerActions.setStatus("current")
_OgCheckResolveActions_Type = Counter32
_OgCheckResolveActions_Object = MibTableColumn
ogCheckResolveActions = _OgCheckResolveActions_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 21, 1, 7),
    _OgCheckResolveActions_Type()
)
ogCheckResolveActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCheckResolveActions.setStatus("current")
_OgCheckDeviceTable_Object = MibTable
ogCheckDeviceTable = _OgCheckDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 22)
)
if mibBuilder.loadTexts:
    ogCheckDeviceTable.setStatus("current")
_OgCheckDeviceEntry_Object = MibTableRow
ogCheckDeviceEntry = _OgCheckDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 22, 1)
)
ogCheckDeviceEntry.setIndexNames(
    (0, "OG-STATUSv2-MIB", "ogCheckIndex"),
    (0, "OG-STATUSv2-MIB", "ogCheckDeviceIndex"),
)
if mibBuilder.loadTexts:
    ogCheckDeviceEntry.setStatus("current")


class _OgCheckDeviceIndex_Type(Integer32):
    """Custom type ogCheckDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgCheckDeviceIndex_Type.__name__ = "Integer32"
_OgCheckDeviceIndex_Object = MibTableColumn
ogCheckDeviceIndex = _OgCheckDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 22, 1, 1),
    _OgCheckDeviceIndex_Type()
)
ogCheckDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogCheckDeviceIndex.setStatus("current")
_OgCheckDeviceCheck_Type = ObjectIdentifier
_OgCheckDeviceCheck_Object = MibTableColumn
ogCheckDeviceCheck = _OgCheckDeviceCheck_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 22, 1, 2),
    _OgCheckDeviceCheck_Type()
)
ogCheckDeviceCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCheckDeviceCheck.setStatus("current")


class _OgCheckDeviceName_Type(DisplayString):
    """Custom type ogCheckDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgCheckDeviceName_Type.__name__ = "DisplayString"
_OgCheckDeviceName_Object = MibTableColumn
ogCheckDeviceName = _OgCheckDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 22, 1, 3),
    _OgCheckDeviceName_Type()
)
ogCheckDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCheckDeviceName.setStatus("current")


class _OgCheckDeviceRef_Type(DisplayString):
    """Custom type ogCheckDeviceRef based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgCheckDeviceRef_Type.__name__ = "DisplayString"
_OgCheckDeviceRef_Object = MibTableColumn
ogCheckDeviceRef = _OgCheckDeviceRef_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 22, 1, 4),
    _OgCheckDeviceRef_Type()
)
ogCheckDeviceRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCheckDeviceRef.setStatus("current")
_OgAlarm_ObjectIdentity = ObjectIdentity
ogAlarm = _OgAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23)
)
_OgAlarmLogTable_Object = MibTable
ogAlarmLogTable = _OgAlarmLogTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 1)
)
if mibBuilder.loadTexts:
    ogAlarmLogTable.setStatus("current")
_OgAlarmLogEntry_Object = MibTableRow
ogAlarmLogEntry = _OgAlarmLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 1, 1)
)
ogAlarmLogEntry.setIndexNames(
    (0, "OG-STATUSv2-MIB", "ogAlarmLogIndex"),
)
if mibBuilder.loadTexts:
    ogAlarmLogEntry.setStatus("current")


class _OgAlarmLogIndex_Type(Integer32):
    """Custom type ogAlarmLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgAlarmLogIndex_Type.__name__ = "Integer32"
_OgAlarmLogIndex_Object = MibTableColumn
ogAlarmLogIndex = _OgAlarmLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 1, 1, 1),
    _OgAlarmLogIndex_Type()
)
ogAlarmLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogAlarmLogIndex.setStatus("current")
_OgAlarmEventId_Type = Integer32
_OgAlarmEventId_Object = MibTableColumn
ogAlarmEventId = _OgAlarmEventId_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 1, 1, 2),
    _OgAlarmEventId_Type()
)
ogAlarmEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogAlarmEventId.setStatus("current")


class _OgAlarmName_Type(DisplayString):
    """Custom type ogAlarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OgAlarmName_Type.__name__ = "DisplayString"
_OgAlarmName_Object = MibTableColumn
ogAlarmName = _OgAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 1, 1, 3),
    _OgAlarmName_Type()
)
ogAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogAlarmName.setStatus("current")
_OgAlarmCheck_Type = Integer32
_OgAlarmCheck_Object = MibTableColumn
ogAlarmCheck = _OgAlarmCheck_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 1, 1, 4),
    _OgAlarmCheck_Type()
)
ogAlarmCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogAlarmCheck.setStatus("current")
_OgAlarmInstance_Type = Integer32
_OgAlarmInstance_Object = MibTableColumn
ogAlarmInstance = _OgAlarmInstance_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 1, 1, 5),
    _OgAlarmInstance_Type()
)
ogAlarmInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogAlarmInstance.setStatus("current")
_OgAlarmTime_Type = DateAndTime
_OgAlarmTime_Object = MibTableColumn
ogAlarmTime = _OgAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 1, 1, 6),
    _OgAlarmTime_Type()
)
ogAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogAlarmTime.setStatus("current")


class _OgAlarmType_Type(Integer32):
    """Custom type ogAlarmType based on Integer32"""
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
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              255,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("cellApnChanged", 79),
          ("cellDataUsage", 75),
          ("cellMessageReceived", 76),
          ("cellNetworkChanged", 81),
          ("cellSignalHigh", 78),
          ("cellSignalLow", 77),
          ("cellTowerChanged", 80),
          ("customCheckFailure", 255),
          ("dialPoolHealth", 89),
          ("dioSignalClosed", 18),
          ("dioSignalOpened", 17),
          ("envHumidityHigh", 16),
          ("envHumidityLow", 15),
          ("envTemperatureHigh", 14),
          ("envTemperatureLow", 13),
          ("hostPingDown", 7),
          ("hostPingUp", 8),
          ("hostServiceDown", 9),
          ("hostServiceUp", 10),
          ("hostUserSession", 11),
          ("netInterfaceDown", 19),
          ("netInterfaceStarting", 20),
          ("netInterfaceStopping", 22),
          ("netInterfaceUp", 21),
          ("powerSupplyInputVoltageHigh", 24),
          ("powerSupplyInputVoltageLow", 23),
          ("powerSupplyOutputCurrentHigh", 26),
          ("powerSupplyOutputCurrentLow", 25),
          ("powerSupplyTemperatureHigh", 28),
          ("powerSupplyTemperatureLow", 27),
          ("rpcInputCurrentHigh", 66),
          ("rpcInputCurrentLow", 65),
          ("rpcInputFrequencyHigh", 62),
          ("rpcInputFrequencyLow", 61),
          ("rpcInputVoltageHigh", 64),
          ("rpcInputVoltageLow", 63),
          ("rpcOutletCurrentHigh", 71),
          ("rpcOutletCurrentLow", 72),
          ("rpcOutletFrequencyHigh", 67),
          ("rpcOutletFrequencyLow", 68),
          ("rpcOutletStateOff", 73),
          ("rpcOutletStateOn", 74),
          ("rpcOutletVoltageHigh", 69),
          ("rpcOutletVoltageLow", 70),
          ("serialPatternRx", 5),
          ("serialPatternTx", 4),
          ("serialSignalCts", 1),
          ("serialSignalDcd", 2),
          ("serialSignalDsr", 3),
          ("serialUserSession", 6),
          ("unknown", 65535),
          ("upsBatteryChargeHigh", 36),
          ("upsBatteryChargeLow", 35),
          ("upsBatteryCurrentHigh", 40),
          ("upsBatteryCurrentLow", 39),
          ("upsBatteryTemperatureHigh", 42),
          ("upsBatteryTemperatureLow", 41),
          ("upsBatteryVoltageHigh", 38),
          ("upsBatteryVoltageLow", 37),
          ("upsHumidityHigh", 31),
          ("upsHumidityLow", 32),
          ("upsInputCurrentHigh", 48),
          ("upsInputCurrentLow", 47),
          ("upsInputFrequencyHigh", 44),
          ("upsInputFrequencyLow", 43),
          ("upsInputVoltageHigh", 46),
          ("upsInputVoltageLow", 45),
          ("upsLowBattery", 34),
          ("upsOnBattery", 33),
          ("upsOutputCurrentHigh", 54),
          ("upsOutputCurrentLow", 53),
          ("upsOutputFrequencyHigh", 50),
          ("upsOutputFrequencyLow", 49),
          ("upsOutputLoadHigh", 56),
          ("upsOutputLoadLow", 55),
          ("upsOutputPowerHigh", 58),
          ("upsOutputPowerLow", 57),
          ("upsOutputTruePowerHigh", 60),
          ("upsOutputTruePowerLow", 59),
          ("upsOutputVoltageHigh", 52),
          ("upsOutputVoltageLow", 51),
          ("upsTemperatureHigh", 29),
          ("upsTemperatureLow", 30),
          ("webUserSession", 12),
          ("wirelessApAssociation", 86),
          ("wirelessApAuthenticationFailure", 88),
          ("wirelessApDisassociation", 87),
          ("wirelessClientConnected", 82),
          ("wirelessClientDisconnected", 83),
          ("wirelessClientSignalHigh", 85),
          ("wirelessClientSignalLow", 84))
    )


_OgAlarmType_Type.__name__ = "Integer32"
_OgAlarmType_Object = MibTableColumn
ogAlarmType = _OgAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 1, 1, 7),
    _OgAlarmType_Type()
)
ogAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogAlarmType.setStatus("current")
_OgAlarmSummary_Type = DisplayString
_OgAlarmSummary_Object = MibTableColumn
ogAlarmSummary = _OgAlarmSummary_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 1, 1, 8),
    _OgAlarmSummary_Type()
)
ogAlarmSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogAlarmSummary.setStatus("current")
_OgAlarmDevice_Type = DisplayString
_OgAlarmDevice_Object = MibTableColumn
ogAlarmDevice = _OgAlarmDevice_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 1, 1, 9),
    _OgAlarmDevice_Type()
)
ogAlarmDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogAlarmDevice.setStatus("current")
_OgAlarmUser_Type = DisplayString
_OgAlarmUser_Object = MibTableColumn
ogAlarmUser = _OgAlarmUser_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 1, 1, 10),
    _OgAlarmUser_Type()
)
ogAlarmUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogAlarmUser.setStatus("current")
_OgAlarmTriggerValue_Type = Integer32
_OgAlarmTriggerValue_Object = MibTableColumn
ogAlarmTriggerValue = _OgAlarmTriggerValue_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 1, 1, 11),
    _OgAlarmTriggerValue_Type()
)
ogAlarmTriggerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogAlarmTriggerValue.setStatus("current")
_OgAlarmCurrentValue_Type = Integer32
_OgAlarmCurrentValue_Object = MibTableColumn
ogAlarmCurrentValue = _OgAlarmCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 1, 1, 12),
    _OgAlarmCurrentValue_Type()
)
ogAlarmCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogAlarmCurrentValue.setStatus("current")
_OgAlarmPreviousValue_Type = Integer32
_OgAlarmPreviousValue_Object = MibTableColumn
ogAlarmPreviousValue = _OgAlarmPreviousValue_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 1, 1, 13),
    _OgAlarmPreviousValue_Type()
)
ogAlarmPreviousValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogAlarmPreviousValue.setStatus("current")


class _OgAlarmState_Type(Integer32):
    """Custom type ogAlarmState based on Integer32"""
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
        *(("disabled", 5),
          ("normal", 1),
          ("resolving", 3),
          ("triggered", 2),
          ("unresolvable", 6),
          ("waiting", 4))
    )


_OgAlarmState_Type.__name__ = "Integer32"
_OgAlarmState_Object = MibTableColumn
ogAlarmState = _OgAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 1, 1, 14),
    _OgAlarmState_Type()
)
ogAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogAlarmState.setStatus("current")
_OgCurrentAlarmTable_Object = MibTable
ogCurrentAlarmTable = _OgCurrentAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 2)
)
if mibBuilder.loadTexts:
    ogCurrentAlarmTable.setStatus("current")
_OgCurrentAlarmEntry_Object = MibTableRow
ogCurrentAlarmEntry = _OgCurrentAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 2, 1)
)
ogCurrentAlarmEntry.setIndexNames(
    (0, "OG-STATUSv2-MIB", "ogCurrentAlarmIndex"),
)
if mibBuilder.loadTexts:
    ogCurrentAlarmEntry.setStatus("current")


class _OgCurrentAlarmIndex_Type(Integer32):
    """Custom type ogCurrentAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgCurrentAlarmIndex_Type.__name__ = "Integer32"
_OgCurrentAlarmIndex_Object = MibTableColumn
ogCurrentAlarmIndex = _OgCurrentAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 2, 1, 1),
    _OgCurrentAlarmIndex_Type()
)
ogCurrentAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogCurrentAlarmIndex.setStatus("current")
_OgCurrentAlarmEventId_Type = Integer32
_OgCurrentAlarmEventId_Object = MibTableColumn
ogCurrentAlarmEventId = _OgCurrentAlarmEventId_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 2, 1, 2),
    _OgCurrentAlarmEventId_Type()
)
ogCurrentAlarmEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCurrentAlarmEventId.setStatus("current")


class _OgCurrentAlarmName_Type(DisplayString):
    """Custom type ogCurrentAlarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OgCurrentAlarmName_Type.__name__ = "DisplayString"
_OgCurrentAlarmName_Object = MibTableColumn
ogCurrentAlarmName = _OgCurrentAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 2, 1, 3),
    _OgCurrentAlarmName_Type()
)
ogCurrentAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCurrentAlarmName.setStatus("current")
_OgCurrentAlarmCheck_Type = Integer32
_OgCurrentAlarmCheck_Object = MibTableColumn
ogCurrentAlarmCheck = _OgCurrentAlarmCheck_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 2, 1, 4),
    _OgCurrentAlarmCheck_Type()
)
ogCurrentAlarmCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCurrentAlarmCheck.setStatus("current")
_OgCurrentAlarmInstance_Type = Integer32
_OgCurrentAlarmInstance_Object = MibTableColumn
ogCurrentAlarmInstance = _OgCurrentAlarmInstance_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 2, 1, 5),
    _OgCurrentAlarmInstance_Type()
)
ogCurrentAlarmInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCurrentAlarmInstance.setStatus("current")
_OgCurrentAlarmTime_Type = DateAndTime
_OgCurrentAlarmTime_Object = MibTableColumn
ogCurrentAlarmTime = _OgCurrentAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 2, 1, 6),
    _OgCurrentAlarmTime_Type()
)
ogCurrentAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCurrentAlarmTime.setStatus("current")


class _OgCurrentAlarmType_Type(Integer32):
    """Custom type ogCurrentAlarmType based on Integer32"""
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
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              255,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("cellApnChanged", 79),
          ("cellDataUsage", 75),
          ("cellMessageReceived", 76),
          ("cellNetworkChanged", 81),
          ("cellSignalHigh", 78),
          ("cellSignalLow", 77),
          ("cellTowerChanged", 80),
          ("customCheckFailure", 255),
          ("dialPoolHealth", 89),
          ("dioSignalClosed", 18),
          ("dioSignalOpened", 17),
          ("envHumidityHigh", 16),
          ("envHumidityLow", 15),
          ("envTemperatureHigh", 14),
          ("envTemperatureLow", 13),
          ("hostPingDown", 7),
          ("hostPingUp", 8),
          ("hostServiceDown", 9),
          ("hostServiceUp", 10),
          ("hostUserSession", 11),
          ("netInterfaceDown", 19),
          ("netInterfaceStarting", 20),
          ("netInterfaceStopping", 22),
          ("netInterfaceUp", 21),
          ("powerSupplyInputVoltageHigh", 24),
          ("powerSupplyInputVoltageLow", 23),
          ("powerSupplyOutputCurrentHigh", 26),
          ("powerSupplyOutputCurrentLow", 25),
          ("powerSupplyTemperatureHigh", 28),
          ("powerSupplyTemperatureLow", 27),
          ("rpcInputCurrentHigh", 66),
          ("rpcInputCurrentLow", 65),
          ("rpcInputFrequencyHigh", 62),
          ("rpcInputFrequencyLow", 61),
          ("rpcInputVoltageHigh", 64),
          ("rpcInputVoltageLow", 63),
          ("rpcOutletCurrentHigh", 71),
          ("rpcOutletCurrentLow", 72),
          ("rpcOutletFrequencyHigh", 67),
          ("rpcOutletFrequencyLow", 68),
          ("rpcOutletStateOff", 73),
          ("rpcOutletStateOn", 74),
          ("rpcOutletVoltageHigh", 69),
          ("rpcOutletVoltageLow", 70),
          ("serialPatternRx", 5),
          ("serialPatternTx", 4),
          ("serialSignalCts", 1),
          ("serialSignalDcd", 2),
          ("serialSignalDsr", 3),
          ("serialUserSession", 6),
          ("unknown", 65535),
          ("upsBatteryChargeHigh", 36),
          ("upsBatteryChargeLow", 35),
          ("upsBatteryCurrentHigh", 40),
          ("upsBatteryCurrentLow", 39),
          ("upsBatteryTemperatureHigh", 42),
          ("upsBatteryTemperatureLow", 41),
          ("upsBatteryVoltageHigh", 38),
          ("upsBatteryVoltageLow", 37),
          ("upsHumidityHigh", 31),
          ("upsHumidityLow", 32),
          ("upsInputCurrentHigh", 48),
          ("upsInputCurrentLow", 47),
          ("upsInputFrequencyHigh", 44),
          ("upsInputFrequencyLow", 43),
          ("upsInputVoltageHigh", 46),
          ("upsInputVoltageLow", 45),
          ("upsLowBattery", 34),
          ("upsOnBattery", 33),
          ("upsOutputCurrentHigh", 54),
          ("upsOutputCurrentLow", 53),
          ("upsOutputFrequencyHigh", 50),
          ("upsOutputFrequencyLow", 49),
          ("upsOutputLoadHigh", 56),
          ("upsOutputLoadLow", 55),
          ("upsOutputPowerHigh", 58),
          ("upsOutputPowerLow", 57),
          ("upsOutputTruePowerHigh", 60),
          ("upsOutputTruePowerLow", 59),
          ("upsOutputVoltageHigh", 52),
          ("upsOutputVoltageLow", 51),
          ("upsTemperatureHigh", 29),
          ("upsTemperatureLow", 30),
          ("webUserSession", 12),
          ("wirelessApAssociation", 86),
          ("wirelessApAuthenticationFailure", 88),
          ("wirelessApDisassociation", 87),
          ("wirelessClientConnected", 82),
          ("wirelessClientDisconnected", 83),
          ("wirelessClientSignalHigh", 85),
          ("wirelessClientSignalLow", 84))
    )


_OgCurrentAlarmType_Type.__name__ = "Integer32"
_OgCurrentAlarmType_Object = MibTableColumn
ogCurrentAlarmType = _OgCurrentAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 2, 1, 7),
    _OgCurrentAlarmType_Type()
)
ogCurrentAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCurrentAlarmType.setStatus("current")
_OgCurrentAlarmSummary_Type = DisplayString
_OgCurrentAlarmSummary_Object = MibTableColumn
ogCurrentAlarmSummary = _OgCurrentAlarmSummary_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 2, 1, 8),
    _OgCurrentAlarmSummary_Type()
)
ogCurrentAlarmSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCurrentAlarmSummary.setStatus("current")
_OgCurrentAlarmDevice_Type = DisplayString
_OgCurrentAlarmDevice_Object = MibTableColumn
ogCurrentAlarmDevice = _OgCurrentAlarmDevice_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 2, 1, 9),
    _OgCurrentAlarmDevice_Type()
)
ogCurrentAlarmDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCurrentAlarmDevice.setStatus("current")
_OgCurrentAlarmUser_Type = DisplayString
_OgCurrentAlarmUser_Object = MibTableColumn
ogCurrentAlarmUser = _OgCurrentAlarmUser_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 2, 1, 10),
    _OgCurrentAlarmUser_Type()
)
ogCurrentAlarmUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCurrentAlarmUser.setStatus("current")
_OgCurrentAlarmTriggerValue_Type = Integer32
_OgCurrentAlarmTriggerValue_Object = MibTableColumn
ogCurrentAlarmTriggerValue = _OgCurrentAlarmTriggerValue_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 2, 1, 11),
    _OgCurrentAlarmTriggerValue_Type()
)
ogCurrentAlarmTriggerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCurrentAlarmTriggerValue.setStatus("current")
_OgCurrentAlarmCurrentValue_Type = Integer32
_OgCurrentAlarmCurrentValue_Object = MibTableColumn
ogCurrentAlarmCurrentValue = _OgCurrentAlarmCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 2, 1, 12),
    _OgCurrentAlarmCurrentValue_Type()
)
ogCurrentAlarmCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCurrentAlarmCurrentValue.setStatus("current")
_OgCurrentAlarmPreviousValue_Type = Integer32
_OgCurrentAlarmPreviousValue_Object = MibTableColumn
ogCurrentAlarmPreviousValue = _OgCurrentAlarmPreviousValue_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 2, 1, 13),
    _OgCurrentAlarmPreviousValue_Type()
)
ogCurrentAlarmPreviousValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCurrentAlarmPreviousValue.setStatus("current")


class _OgCurrentAlarmState_Type(Integer32):
    """Custom type ogCurrentAlarmState based on Integer32"""
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
        *(("disabled", 5),
          ("normal", 1),
          ("resolving", 3),
          ("triggered", 2),
          ("unresolvable", 6),
          ("waiting", 4))
    )


_OgCurrentAlarmState_Type.__name__ = "Integer32"
_OgCurrentAlarmState_Object = MibTableColumn
ogCurrentAlarmState = _OgCurrentAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 25049, 17, 23, 2, 1, 14),
    _OgCurrentAlarmState_Type()
)
ogCurrentAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogCurrentAlarmState.setStatus("current")
_OgStatus2NotificationPrefix_ObjectIdentity = ObjectIdentity
ogStatus2NotificationPrefix = _OgStatus2NotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100)
)
_OgMibNotifications_ObjectIdentity = ObjectIdentity
ogMibNotifications = _OgMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0)
)
_OgStatus2Conformance_ObjectIdentity = ObjectIdentity
ogStatus2Conformance = _OgStatus2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 17, 65535)
)
_OgStatus2Compliances_ObjectIdentity = ObjectIdentity
ogStatus2Compliances = _OgStatus2Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 17, 65535, 1)
)
_OgStatus2Groups_ObjectIdentity = ObjectIdentity
ogStatus2Groups = _OgStatus2Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 17, 65535, 2)
)

# Managed Objects groups

ogBasicStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25049, 17, 65535, 2, 1)
)
ogBasicStatusGroup.setObjects(
      *(("OG-STATUSv2-MIB", "ogFirmwareVersion"),
        ("OG-STATUSv2-MIB", "ogSerialNumber"),
        ("OG-STATUSv2-MIB", "ogSerialPortLabel"),
        ("OG-STATUSv2-MIB", "ogSerialPortSpeed"),
        ("OG-STATUSv2-MIB", "ogSerialPortDataBits"),
        ("OG-STATUSv2-MIB", "ogSerialPortParity"),
        ("OG-STATUSv2-MIB", "ogSerialPortStopBits"),
        ("OG-STATUSv2-MIB", "ogSerialPortFlowControl"),
        ("OG-STATUSv2-MIB", "ogSerialPortMode"),
        ("OG-STATUSv2-MIB", "ogSerialPortLogLevel"),
        ("OG-STATUSv2-MIB", "ogSerialPortRxBytes"),
        ("OG-STATUSv2-MIB", "ogSerialPortTxBytes"),
        ("OG-STATUSv2-MIB", "ogSerialPortFramingErrors"),
        ("OG-STATUSv2-MIB", "ogSerialPortParityErrors"),
        ("OG-STATUSv2-MIB", "ogSerialPortOverrunErrors"),
        ("OG-STATUSv2-MIB", "ogSerialPortBreaks"),
        ("OG-STATUSv2-MIB", "ogSerialPortDCD"),
        ("OG-STATUSv2-MIB", "ogSerialPortDTR"),
        ("OG-STATUSv2-MIB", "ogSerialPortDSR"),
        ("OG-STATUSv2-MIB", "ogSerialPortCTS"),
        ("OG-STATUSv2-MIB", "ogSerialPortRTS"),
        ("OG-STATUSv2-MIB", "ogSerialUserStartTime"),
        ("OG-STATUSv2-MIB", "ogSerialUserPort"),
        ("OG-STATUSv2-MIB", "ogSerialUserLabel"),
        ("OG-STATUSv2-MIB", "ogSerialUserName"),
        ("OG-STATUSv2-MIB", "ogHostName"),
        ("OG-STATUSv2-MIB", "ogHostIpV4Address"),
        ("OG-STATUSv2-MIB", "ogHostIpV6Address"),
        ("OG-STATUSv2-MIB", "ogHostServiceHost"),
        ("OG-STATUSv2-MIB", "ogHostServiceType"),
        ("OG-STATUSv2-MIB", "ogHostServicePort"),
        ("OG-STATUSv2-MIB", "ogHostServiceStatus"),
        ("OG-STATUSv2-MIB", "ogHostServiceCounter"),
        ("OG-STATUSv2-MIB", "ogHostUserHost"),
        ("OG-STATUSv2-MIB", "ogHostUserStartTime"),
        ("OG-STATUSv2-MIB", "ogHostUserAddress"),
        ("OG-STATUSv2-MIB", "ogHostUserHostName"),
        ("OG-STATUSv2-MIB", "ogHostUserName"),
        ("OG-STATUSv2-MIB", "ogWebUserStartTime"),
        ("OG-STATUSv2-MIB", "ogWebUserName"),
        ("OG-STATUSv2-MIB", "ogWebUserSourceAddress"),
        ("OG-STATUSv2-MIB", "ogWebUserSourcePort"),
        ("OG-STATUSv2-MIB", "ogEmdName"),
        ("OG-STATUSv2-MIB", "ogEmdDescription"),
        ("OG-STATUSv2-MIB", "ogEmdEnabled"),
        ("OG-STATUSv2-MIB", "ogEmdLogEnabled"),
        ("OG-STATUSv2-MIB", "ogEmdConnectType"),
        ("OG-STATUSv2-MIB", "ogEmdTemperatureTotal"),
        ("OG-STATUSv2-MIB", "ogEmdHumidityTotal"),
        ("OG-STATUSv2-MIB", "ogEmdDioInputTotal"),
        ("OG-STATUSv2-MIB", "ogEmdTemperatureEmd"),
        ("OG-STATUSv2-MIB", "ogEmdTemperatureName"),
        ("OG-STATUSv2-MIB", "ogEmdTemperatureDescription"),
        ("OG-STATUSv2-MIB", "ogEmdTemperatureValue"),
        ("OG-STATUSv2-MIB", "ogEmdTemperatureCounter"),
        ("OG-STATUSv2-MIB", "ogEmdHumidityEmd"),
        ("OG-STATUSv2-MIB", "ogEmdHumidityName"),
        ("OG-STATUSv2-MIB", "ogEmdHumidityDescription"),
        ("OG-STATUSv2-MIB", "ogEmdHumidityValue"),
        ("OG-STATUSv2-MIB", "ogEmdHumidityCounter"),
        ("OG-STATUSv2-MIB", "ogEmdDioEmd"),
        ("OG-STATUSv2-MIB", "ogEmdDioName"),
        ("OG-STATUSv2-MIB", "ogEmdDioDescription"),
        ("OG-STATUSv2-MIB", "ogEmdDioType"),
        ("OG-STATUSv2-MIB", "ogEmdDioDirection"),
        ("OG-STATUSv2-MIB", "ogEmdDioState"),
        ("OG-STATUSv2-MIB", "ogEmdDioTriggerMode"),
        ("OG-STATUSv2-MIB", "ogEmdDioCounter"),
        ("OG-STATUSv2-MIB", "ogNetInterfaceName"),
        ("OG-STATUSv2-MIB", "ogNetInterfaceType"),
        ("OG-STATUSv2-MIB", "ogNetInterfaceState"),
        ("OG-STATUSv2-MIB", "ogPowerSupplyName"),
        ("OG-STATUSv2-MIB", "ogPowerSupplyInputVoltage"),
        ("OG-STATUSv2-MIB", "ogPowerSupplyOutputCurrent"),
        ("OG-STATUSv2-MIB", "ogPowerSupplyTemperature"),
        ("OG-STATUSv2-MIB", "ogUpsName"),
        ("OG-STATUSv2-MIB", "ogUpsDescription"),
        ("OG-STATUSv2-MIB", "ogUpsType"),
        ("OG-STATUSv2-MIB", "ogUpsLogEnabled"),
        ("OG-STATUSv2-MIB", "ogUpsConnectType"),
        ("OG-STATUSv2-MIB", "ogUpsState"),
        ("OG-STATUSv2-MIB", "ogUpsTemperature"),
        ("OG-STATUSv2-MIB", "ogUpsHumidity"),
        ("OG-STATUSv2-MIB", "ogUpsBatteryState"),
        ("OG-STATUSv2-MIB", "ogUpsBatteryRunTime"),
        ("OG-STATUSv2-MIB", "ogUpsBatteryRunTimeLow"),
        ("OG-STATUSv2-MIB", "ogUpsBatteryRunTimeRestart"),
        ("OG-STATUSv2-MIB", "ogUpsBatteryCharge"),
        ("OG-STATUSv2-MIB", "ogUpsBatteryVoltage"),
        ("OG-STATUSv2-MIB", "ogUpsBatteryNominalVoltage"),
        ("OG-STATUSv2-MIB", "ogUpsBatteryCurrent"),
        ("OG-STATUSv2-MIB", "ogUpsBatteryNominalCurrent"),
        ("OG-STATUSv2-MIB", "ogUpsBatteryTemperature"),
        ("OG-STATUSv2-MIB", "ogUpsInputFrequency"),
        ("OG-STATUSv2-MIB", "ogUpsInputNominalFrequency"),
        ("OG-STATUSv2-MIB", "ogUpsInputVoltage"),
        ("OG-STATUSv2-MIB", "ogUpsInputNominalVoltage"),
        ("OG-STATUSv2-MIB", "ogUpsInputCurrent"),
        ("OG-STATUSv2-MIB", "ogUpsInputNominalCurrent"),
        ("OG-STATUSv2-MIB", "ogUpsOutputFrequency"),
        ("OG-STATUSv2-MIB", "ogUpsOutputNominalFrequency"),
        ("OG-STATUSv2-MIB", "ogUpsOutputVoltage"),
        ("OG-STATUSv2-MIB", "ogUpsOutputNominalVoltage"),
        ("OG-STATUSv2-MIB", "ogUpsOutputCurrent"),
        ("OG-STATUSv2-MIB", "ogUpsOutputNominalCurrent"),
        ("OG-STATUSv2-MIB", "ogUpsOutputLoad"),
        ("OG-STATUSv2-MIB", "ogUpsOutputPower"),
        ("OG-STATUSv2-MIB", "ogUpsOutputTruePower"),
        ("OG-STATUSv2-MIB", "ogUpsCounter"),
        ("OG-STATUSv2-MIB", "ogRpcName"),
        ("OG-STATUSv2-MIB", "ogRpcDescription"),
        ("OG-STATUSv2-MIB", "ogRpcType"),
        ("OG-STATUSv2-MIB", "ogRpcLogEnabled"),
        ("OG-STATUSv2-MIB", "ogRpcOutletTotal"),
        ("OG-STATUSv2-MIB", "ogRpcMaxTemperature"),
        ("OG-STATUSv2-MIB", "ogRpcConnectType"),
        ("OG-STATUSv2-MIB", "ogRpcInputFrequency"),
        ("OG-STATUSv2-MIB", "ogRpcInputVoltage"),
        ("OG-STATUSv2-MIB", "ogRpcInputCurrent"),
        ("OG-STATUSv2-MIB", "ogRpcCounter"),
        ("OG-STATUSv2-MIB", "ogRpcOutletRpc"),
        ("OG-STATUSv2-MIB", "ogRpcOutletName"),
        ("OG-STATUSv2-MIB", "ogRpcOutletState"),
        ("OG-STATUSv2-MIB", "ogRpcOutletFrequency"),
        ("OG-STATUSv2-MIB", "ogRpcOutletCurrent"),
        ("OG-STATUSv2-MIB", "ogRpcOutletVoltage"),
        ("OG-STATUSv2-MIB", "ogRpcOutletLoad"),
        ("OG-STATUSv2-MIB", "ogCellModemVendor"),
        ("OG-STATUSv2-MIB", "ogCellModemModel"),
        ("OG-STATUSv2-MIB", "ogCellModemEnabled"),
        ("OG-STATUSv2-MIB", "ogCellModemConnected"),
        ("OG-STATUSv2-MIB", "ogCellModemNetwork"),
        ("OG-STATUSv2-MIB", "ogCellModemRegistered"),
        ("OG-STATUSv2-MIB", "ogCellModemTower"),
        ("OG-STATUSv2-MIB", "ogCellModemRadioTechnology"),
        ("OG-STATUSv2-MIB", "ogCellModemApn"),
        ("OG-STATUSv2-MIB", "ogCellModem3gRssi"),
        ("OG-STATUSv2-MIB", "ogCellModem4gRssi"),
        ("OG-STATUSv2-MIB", "ogCellModemSessionTime"),
        ("OG-STATUSv2-MIB", "ogCellModemSelectedSimCard"),
        ("OG-STATUSv2-MIB", "ogCellModemTemperature"),
        ("OG-STATUSv2-MIB", "ogCellModemCounter"),
        ("OG-STATUSv2-MIB", "ogWifiClientInterface"),
        ("OG-STATUSv2-MIB", "ogWifiClientEnabled"),
        ("OG-STATUSv2-MIB", "ogWifiClientEssid"),
        ("OG-STATUSv2-MIB", "ogWifiClientIeeeMode"),
        ("OG-STATUSv2-MIB", "ogWifiClientMode"),
        ("OG-STATUSv2-MIB", "ogWifiClientFrequency"),
        ("OG-STATUSv2-MIB", "ogWifiClientApMac"),
        ("OG-STATUSv2-MIB", "ogWifiClientBitRate"),
        ("OG-STATUSv2-MIB", "ogWifiClientTxPower"),
        ("OG-STATUSv2-MIB", "ogWifiClientLinkQuality"),
        ("OG-STATUSv2-MIB", "ogWifiClientRssi"),
        ("OG-STATUSv2-MIB", "ogWifiClientRxInvalidNwid"),
        ("OG-STATUSv2-MIB", "ogWifiClientRxInvalidCrypt"),
        ("OG-STATUSv2-MIB", "ogWifiClientRxInvalidFrag"),
        ("OG-STATUSv2-MIB", "ogWifiClientRxInvalidRetries"),
        ("OG-STATUSv2-MIB", "ogWifiClientRxInvalidMisc"),
        ("OG-STATUSv2-MIB", "ogWifiClientMissedBeacon"),
        ("OG-STATUSv2-MIB", "ogWifiClientCounter"),
        ("OG-STATUSv2-MIB", "ogWifiApInterface"),
        ("OG-STATUSv2-MIB", "ogWifiApEnabled"),
        ("OG-STATUSv2-MIB", "ogWifiApSsid"),
        ("OG-STATUSv2-MIB", "ogWifiApIeeeMode"),
        ("OG-STATUSv2-MIB", "ogWifiApFrequency"),
        ("OG-STATUSv2-MIB", "ogWifiApTxPower"),
        ("OG-STATUSv2-MIB", "ogWifiApCounter"),
        ("OG-STATUSv2-MIB", "ogWifiApClientAp"),
        ("OG-STATUSv2-MIB", "ogWifiApClientMac"),
        ("OG-STATUSv2-MIB", "ogWifiApClientInactiveTime"),
        ("OG-STATUSv2-MIB", "ogWifiApClientRxBytes"),
        ("OG-STATUSv2-MIB", "ogWifiApClientRxPackets"),
        ("OG-STATUSv2-MIB", "ogWifiApClientTxBytes"),
        ("OG-STATUSv2-MIB", "ogWifiApClientTxPackets"),
        ("OG-STATUSv2-MIB", "ogWifiApClientRssi"),
        ("OG-STATUSv2-MIB", "ogWifiApClientTxBitRate"),
        ("OG-STATUSv2-MIB", "ogCheckName"),
        ("OG-STATUSv2-MIB", "ogCheckRepeatTimeout"),
        ("OG-STATUSv2-MIB", "ogCheckResetTimeout"),
        ("OG-STATUSv2-MIB", "ogCheckType"),
        ("OG-STATUSv2-MIB", "ogCheckTriggerActions"),
        ("OG-STATUSv2-MIB", "ogCheckResolveActions"),
        ("OG-STATUSv2-MIB", "ogCheckDeviceCheck"),
        ("OG-STATUSv2-MIB", "ogCheckDeviceName"),
        ("OG-STATUSv2-MIB", "ogCheckDeviceRef"))
)
if mibBuilder.loadTexts:
    ogBasicStatusGroup.setStatus("current")

ogBasicAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25049, 17, 65535, 2, 2)
)
ogBasicAlarmGroup.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"),
        ("OG-STATUSv2-MIB", "ogCurrentAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogCurrentAlarmName"),
        ("OG-STATUSv2-MIB", "ogCurrentAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogCurrentAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogCurrentAlarmTime"),
        ("OG-STATUSv2-MIB", "ogCurrentAlarmType"),
        ("OG-STATUSv2-MIB", "ogCurrentAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogCurrentAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogCurrentAlarmUser"),
        ("OG-STATUSv2-MIB", "ogCurrentAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogCurrentAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogCurrentAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogCurrentAlarmState"))
)
if mibBuilder.loadTexts:
    ogBasicAlarmGroup.setStatus("current")


# Notification objects

ogSerialSignalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 1)
)
ogSerialSignalNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogSerialSignalNotification.setStatus(
        "current"
    )

ogSerialPatternNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 2)
)
ogSerialPatternNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogSerialPatternNotification.setStatus(
        "current"
    )

ogSerialUserNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 3)
)
ogSerialUserNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogSerialUserNotification.setStatus(
        "current"
    )

ogHostPingNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 4)
)
ogHostPingNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogHostPingNotification.setStatus(
        "current"
    )

ogHostServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 5)
)
ogHostServiceNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogHostServiceNotification.setStatus(
        "current"
    )

ogHostUserNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 6)
)
ogHostUserNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogHostUserNotification.setStatus(
        "current"
    )

ogWebUserNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 7)
)
ogWebUserNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogWebUserNotification.setStatus(
        "current"
    )

ogEmdTemperatureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 8)
)
ogEmdTemperatureNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogEmdTemperatureNotification.setStatus(
        "current"
    )

ogEmdHumidityNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 9)
)
ogEmdHumidityNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogEmdHumidityNotification.setStatus(
        "current"
    )

ogEmdDioNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 10)
)
ogEmdDioNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogEmdDioNotification.setStatus(
        "current"
    )

ogPowerSupplyInputNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 11)
)
ogPowerSupplyInputNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogPowerSupplyInputNotification.setStatus(
        "current"
    )

ogPowerSupplyOutputNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 12)
)
ogPowerSupplyOutputNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogPowerSupplyOutputNotification.setStatus(
        "current"
    )

ogPowerSupplyTempNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 13)
)
ogPowerSupplyTempNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogPowerSupplyTempNotification.setStatus(
        "current"
    )

ogUpsNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 14)
)
ogUpsNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogUpsNotification.setStatus(
        "current"
    )

ogUpsBatteryNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 15)
)
ogUpsBatteryNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogUpsBatteryNotification.setStatus(
        "current"
    )

ogUpsInputNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 16)
)
ogUpsInputNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogUpsInputNotification.setStatus(
        "current"
    )

ogUpsOutputNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 17)
)
ogUpsOutputNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogUpsOutputNotification.setStatus(
        "current"
    )

ogRpcInputNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 18)
)
ogRpcInputNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogRpcInputNotification.setStatus(
        "current"
    )

ogRpcOutputNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 19)
)
ogRpcOutputNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogRpcOutputNotification.setStatus(
        "current"
    )

ogRpcOutletNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 20)
)
ogRpcOutletNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogRpcOutletNotification.setStatus(
        "current"
    )

ogNetInterfaceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 21)
)
ogNetInterfaceNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogNetInterfaceNotification.setStatus(
        "current"
    )

ogCellDataNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 22)
)
ogCellDataNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogCellDataNotification.setStatus(
        "current"
    )

ogCellMessageNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 23)
)
ogCellMessageNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogCellMessageNotification.setStatus(
        "current"
    )

ogCellSignalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 24)
)
ogCellSignalNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogCellSignalNotification.setStatus(
        "current"
    )

ogCellApnNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 25)
)
ogCellApnNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogCellApnNotification.setStatus(
        "current"
    )

ogCellTowerNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 26)
)
ogCellTowerNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogCellTowerNotification.setStatus(
        "current"
    )

ogCellNetworkNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 27)
)
ogCellNetworkNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogCellNetworkNotification.setStatus(
        "current"
    )

ogWifiClientConnectNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 28)
)
ogWifiClientConnectNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogWifiClientConnectNotification.setStatus(
        "current"
    )

ogWifiClientSignalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 29)
)
ogWifiClientSignalNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogWifiClientSignalNotification.setStatus(
        "current"
    )

ogWifiApAssociationNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 30)
)
ogWifiApAssociationNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogWifiApAssociationNotification.setStatus(
        "current"
    )

ogWifiApAuthNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 31)
)
ogWifiApAuthNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogWifiApAuthNotification.setStatus(
        "current"
    )

ogDialPoolHealthNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 32)
)
ogDialPoolHealthNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogDialPoolHealthNotification.setStatus(
        "current"
    )

ogCustomNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 17, 100, 0, 33)
)
ogCustomNotification.setObjects(
      *(("OG-STATUSv2-MIB", "ogAlarmEventId"),
        ("OG-STATUSv2-MIB", "ogAlarmName"),
        ("OG-STATUSv2-MIB", "ogAlarmCheck"),
        ("OG-STATUSv2-MIB", "ogAlarmInstance"),
        ("OG-STATUSv2-MIB", "ogAlarmTime"),
        ("OG-STATUSv2-MIB", "ogAlarmType"),
        ("OG-STATUSv2-MIB", "ogAlarmSummary"),
        ("OG-STATUSv2-MIB", "ogAlarmDevice"),
        ("OG-STATUSv2-MIB", "ogAlarmUser"),
        ("OG-STATUSv2-MIB", "ogAlarmTriggerValue"),
        ("OG-STATUSv2-MIB", "ogAlarmCurrentValue"),
        ("OG-STATUSv2-MIB", "ogAlarmPreviousValue"),
        ("OG-STATUSv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogCustomNotification.setStatus(
        "current"
    )


# Notifications groups

ogBasicNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25049, 17, 65535, 2, 3)
)
ogBasicNotificationGroup.setObjects(
      *(("OG-STATUSv2-MIB", "ogSerialSignalNotification"),
        ("OG-STATUSv2-MIB", "ogSerialPatternNotification"),
        ("OG-STATUSv2-MIB", "ogSerialUserNotification"),
        ("OG-STATUSv2-MIB", "ogHostPingNotification"),
        ("OG-STATUSv2-MIB", "ogHostServiceNotification"),
        ("OG-STATUSv2-MIB", "ogHostUserNotification"),
        ("OG-STATUSv2-MIB", "ogWebUserNotification"),
        ("OG-STATUSv2-MIB", "ogEmdDioNotification"),
        ("OG-STATUSv2-MIB", "ogEmdTemperatureNotification"),
        ("OG-STATUSv2-MIB", "ogEmdHumidityNotification"),
        ("OG-STATUSv2-MIB", "ogPowerSupplyInputNotification"),
        ("OG-STATUSv2-MIB", "ogPowerSupplyOutputNotification"),
        ("OG-STATUSv2-MIB", "ogPowerSupplyTempNotification"),
        ("OG-STATUSv2-MIB", "ogUpsNotification"),
        ("OG-STATUSv2-MIB", "ogUpsInputNotification"),
        ("OG-STATUSv2-MIB", "ogUpsBatteryNotification"),
        ("OG-STATUSv2-MIB", "ogUpsOutputNotification"),
        ("OG-STATUSv2-MIB", "ogRpcInputNotification"),
        ("OG-STATUSv2-MIB", "ogRpcOutputNotification"),
        ("OG-STATUSv2-MIB", "ogRpcOutletNotification"),
        ("OG-STATUSv2-MIB", "ogNetInterfaceNotification"),
        ("OG-STATUSv2-MIB", "ogCellDataNotification"),
        ("OG-STATUSv2-MIB", "ogCellMessageNotification"),
        ("OG-STATUSv2-MIB", "ogCellSignalNotification"),
        ("OG-STATUSv2-MIB", "ogCellApnNotification"),
        ("OG-STATUSv2-MIB", "ogCellTowerNotification"),
        ("OG-STATUSv2-MIB", "ogCellNetworkNotification"),
        ("OG-STATUSv2-MIB", "ogWifiClientConnectNotification"),
        ("OG-STATUSv2-MIB", "ogWifiClientSignalNotification"),
        ("OG-STATUSv2-MIB", "ogWifiApAssociationNotification"),
        ("OG-STATUSv2-MIB", "ogWifiApAuthNotification"),
        ("OG-STATUSv2-MIB", "ogDialPoolHealthNotification"),
        ("OG-STATUSv2-MIB", "ogCustomNotification"))
)
if mibBuilder.loadTexts:
    ogBasicNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ogStatus2Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25049, 17, 65535, 1, 1)
)
if mibBuilder.loadTexts:
    ogStatus2Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OG-STATUSv2-MIB",
    **{"ogStatus2": ogStatus2,
       "ogSystem": ogSystem,
       "ogFirmwareVersion": ogFirmwareVersion,
       "ogSerialNumber": ogSerialNumber,
       "ogSerialPortTable": ogSerialPortTable,
       "ogSerialPortEntry": ogSerialPortEntry,
       "ogSerialPortIndex": ogSerialPortIndex,
       "ogSerialPortLabel": ogSerialPortLabel,
       "ogSerialPortSpeed": ogSerialPortSpeed,
       "ogSerialPortDataBits": ogSerialPortDataBits,
       "ogSerialPortParity": ogSerialPortParity,
       "ogSerialPortStopBits": ogSerialPortStopBits,
       "ogSerialPortFlowControl": ogSerialPortFlowControl,
       "ogSerialPortMode": ogSerialPortMode,
       "ogSerialPortLogLevel": ogSerialPortLogLevel,
       "ogSerialPortRxBytes": ogSerialPortRxBytes,
       "ogSerialPortTxBytes": ogSerialPortTxBytes,
       "ogSerialPortFramingErrors": ogSerialPortFramingErrors,
       "ogSerialPortParityErrors": ogSerialPortParityErrors,
       "ogSerialPortOverrunErrors": ogSerialPortOverrunErrors,
       "ogSerialPortBreaks": ogSerialPortBreaks,
       "ogSerialPortDCD": ogSerialPortDCD,
       "ogSerialPortDTR": ogSerialPortDTR,
       "ogSerialPortDSR": ogSerialPortDSR,
       "ogSerialPortCTS": ogSerialPortCTS,
       "ogSerialPortRTS": ogSerialPortRTS,
       "ogSerialUserTable": ogSerialUserTable,
       "ogSerialUserEntry": ogSerialUserEntry,
       "ogSerialUserIndex": ogSerialUserIndex,
       "ogSerialUserStartTime": ogSerialUserStartTime,
       "ogSerialUserPort": ogSerialUserPort,
       "ogSerialUserLabel": ogSerialUserLabel,
       "ogSerialUserName": ogSerialUserName,
       "ogHostTable": ogHostTable,
       "ogHostEntry": ogHostEntry,
       "ogHostIndex": ogHostIndex,
       "ogHostName": ogHostName,
       "ogHostIpV4Address": ogHostIpV4Address,
       "ogHostIpV6Address": ogHostIpV6Address,
       "ogHostServiceTable": ogHostServiceTable,
       "ogHostServiceEntry": ogHostServiceEntry,
       "ogHostServiceIndex": ogHostServiceIndex,
       "ogHostServiceHost": ogHostServiceHost,
       "ogHostServiceType": ogHostServiceType,
       "ogHostServicePort": ogHostServicePort,
       "ogHostServiceStatus": ogHostServiceStatus,
       "ogHostServiceCounter": ogHostServiceCounter,
       "ogHostUserTable": ogHostUserTable,
       "ogHostUserEntry": ogHostUserEntry,
       "ogHostUserIndex": ogHostUserIndex,
       "ogHostUserHost": ogHostUserHost,
       "ogHostUserStartTime": ogHostUserStartTime,
       "ogHostUserAddress": ogHostUserAddress,
       "ogHostUserHostName": ogHostUserHostName,
       "ogHostUserName": ogHostUserName,
       "ogWebUserTable": ogWebUserTable,
       "ogWebUserEntry": ogWebUserEntry,
       "ogWebUserIndex": ogWebUserIndex,
       "ogWebUserStartTime": ogWebUserStartTime,
       "ogWebUserName": ogWebUserName,
       "ogWebUserSourceAddress": ogWebUserSourceAddress,
       "ogWebUserSourcePort": ogWebUserSourcePort,
       "ogEmdTable": ogEmdTable,
       "ogEmdEntry": ogEmdEntry,
       "ogEmdIndex": ogEmdIndex,
       "ogEmdName": ogEmdName,
       "ogEmdDescription": ogEmdDescription,
       "ogEmdEnabled": ogEmdEnabled,
       "ogEmdLogEnabled": ogEmdLogEnabled,
       "ogEmdConnectType": ogEmdConnectType,
       "ogEmdTemperatureTotal": ogEmdTemperatureTotal,
       "ogEmdHumidityTotal": ogEmdHumidityTotal,
       "ogEmdDioInputTotal": ogEmdDioInputTotal,
       "ogEmdTemperatureTable": ogEmdTemperatureTable,
       "ogEmdTemperatureEntry": ogEmdTemperatureEntry,
       "ogEmdTemperatureIndex": ogEmdTemperatureIndex,
       "ogEmdTemperatureEmd": ogEmdTemperatureEmd,
       "ogEmdTemperatureName": ogEmdTemperatureName,
       "ogEmdTemperatureDescription": ogEmdTemperatureDescription,
       "ogEmdTemperatureValue": ogEmdTemperatureValue,
       "ogEmdTemperatureCounter": ogEmdTemperatureCounter,
       "ogEmdHumidityTable": ogEmdHumidityTable,
       "ogEmdHumidityEntry": ogEmdHumidityEntry,
       "ogEmdHumidityIndex": ogEmdHumidityIndex,
       "ogEmdHumidityEmd": ogEmdHumidityEmd,
       "ogEmdHumidityName": ogEmdHumidityName,
       "ogEmdHumidityDescription": ogEmdHumidityDescription,
       "ogEmdHumidityValue": ogEmdHumidityValue,
       "ogEmdHumidityCounter": ogEmdHumidityCounter,
       "ogEmdDioTable": ogEmdDioTable,
       "ogEmdDioEntry": ogEmdDioEntry,
       "ogEmdDioIndex": ogEmdDioIndex,
       "ogEmdDioEmd": ogEmdDioEmd,
       "ogEmdDioName": ogEmdDioName,
       "ogEmdDioDescription": ogEmdDioDescription,
       "ogEmdDioType": ogEmdDioType,
       "ogEmdDioDirection": ogEmdDioDirection,
       "ogEmdDioState": ogEmdDioState,
       "ogEmdDioTriggerMode": ogEmdDioTriggerMode,
       "ogEmdDioCounter": ogEmdDioCounter,
       "ogNetInterfaceTable": ogNetInterfaceTable,
       "ogNetInterfaceEntry": ogNetInterfaceEntry,
       "ogNetInterfaceIndex": ogNetInterfaceIndex,
       "ogNetInterfaceName": ogNetInterfaceName,
       "ogNetInterfaceType": ogNetInterfaceType,
       "ogNetInterfaceState": ogNetInterfaceState,
       "ogPowerSupplyTable": ogPowerSupplyTable,
       "ogPowerSupplyEntry": ogPowerSupplyEntry,
       "ogPowerSupplyIndex": ogPowerSupplyIndex,
       "ogPowerSupplyName": ogPowerSupplyName,
       "ogPowerSupplyInputVoltage": ogPowerSupplyInputVoltage,
       "ogPowerSupplyOutputCurrent": ogPowerSupplyOutputCurrent,
       "ogPowerSupplyTemperature": ogPowerSupplyTemperature,
       "ogUpsTable": ogUpsTable,
       "ogUpsEntry": ogUpsEntry,
       "ogUpsIndex": ogUpsIndex,
       "ogUpsName": ogUpsName,
       "ogUpsDescription": ogUpsDescription,
       "ogUpsType": ogUpsType,
       "ogUpsLogEnabled": ogUpsLogEnabled,
       "ogUpsConnectType": ogUpsConnectType,
       "ogUpsState": ogUpsState,
       "ogUpsTemperature": ogUpsTemperature,
       "ogUpsHumidity": ogUpsHumidity,
       "ogUpsBatteryState": ogUpsBatteryState,
       "ogUpsBatteryRunTime": ogUpsBatteryRunTime,
       "ogUpsBatteryRunTimeLow": ogUpsBatteryRunTimeLow,
       "ogUpsBatteryRunTimeRestart": ogUpsBatteryRunTimeRestart,
       "ogUpsBatteryCharge": ogUpsBatteryCharge,
       "ogUpsBatteryVoltage": ogUpsBatteryVoltage,
       "ogUpsBatteryNominalVoltage": ogUpsBatteryNominalVoltage,
       "ogUpsBatteryCurrent": ogUpsBatteryCurrent,
       "ogUpsBatteryNominalCurrent": ogUpsBatteryNominalCurrent,
       "ogUpsBatteryTemperature": ogUpsBatteryTemperature,
       "ogUpsInputFrequency": ogUpsInputFrequency,
       "ogUpsInputNominalFrequency": ogUpsInputNominalFrequency,
       "ogUpsInputVoltage": ogUpsInputVoltage,
       "ogUpsInputNominalVoltage": ogUpsInputNominalVoltage,
       "ogUpsInputCurrent": ogUpsInputCurrent,
       "ogUpsInputNominalCurrent": ogUpsInputNominalCurrent,
       "ogUpsOutputFrequency": ogUpsOutputFrequency,
       "ogUpsOutputNominalFrequency": ogUpsOutputNominalFrequency,
       "ogUpsOutputVoltage": ogUpsOutputVoltage,
       "ogUpsOutputNominalVoltage": ogUpsOutputNominalVoltage,
       "ogUpsOutputCurrent": ogUpsOutputCurrent,
       "ogUpsOutputNominalCurrent": ogUpsOutputNominalCurrent,
       "ogUpsOutputLoad": ogUpsOutputLoad,
       "ogUpsOutputPower": ogUpsOutputPower,
       "ogUpsOutputTruePower": ogUpsOutputTruePower,
       "ogUpsCounter": ogUpsCounter,
       "ogRpcTable": ogRpcTable,
       "ogRpcEntry": ogRpcEntry,
       "ogRpcIndex": ogRpcIndex,
       "ogRpcName": ogRpcName,
       "ogRpcDescription": ogRpcDescription,
       "ogRpcType": ogRpcType,
       "ogRpcLogEnabled": ogRpcLogEnabled,
       "ogRpcOutletTotal": ogRpcOutletTotal,
       "ogRpcMaxTemperature": ogRpcMaxTemperature,
       "ogRpcConnectType": ogRpcConnectType,
       "ogRpcInputFrequency": ogRpcInputFrequency,
       "ogRpcInputVoltage": ogRpcInputVoltage,
       "ogRpcInputCurrent": ogRpcInputCurrent,
       "ogRpcCounter": ogRpcCounter,
       "ogRpcOutletTable": ogRpcOutletTable,
       "ogRpcOutletEntry": ogRpcOutletEntry,
       "ogRpcOutletIndex": ogRpcOutletIndex,
       "ogRpcOutletRpc": ogRpcOutletRpc,
       "ogRpcOutletName": ogRpcOutletName,
       "ogRpcOutletState": ogRpcOutletState,
       "ogRpcOutletFrequency": ogRpcOutletFrequency,
       "ogRpcOutletVoltage": ogRpcOutletVoltage,
       "ogRpcOutletCurrent": ogRpcOutletCurrent,
       "ogRpcOutletLoad": ogRpcOutletLoad,
       "ogCellModemTable": ogCellModemTable,
       "ogCellModemEntry": ogCellModemEntry,
       "ogCellModemIndex": ogCellModemIndex,
       "ogCellModemVendor": ogCellModemVendor,
       "ogCellModemModel": ogCellModemModel,
       "ogCellModemEnabled": ogCellModemEnabled,
       "ogCellModemConnected": ogCellModemConnected,
       "ogCellModemNetwork": ogCellModemNetwork,
       "ogCellModemRegistered": ogCellModemRegistered,
       "ogCellModemTower": ogCellModemTower,
       "ogCellModemRadioTechnology": ogCellModemRadioTechnology,
       "ogCellModemApn": ogCellModemApn,
       "ogCellModem3gRssi": ogCellModem3gRssi,
       "ogCellModem4gRssi": ogCellModem4gRssi,
       "ogCellModemSessionTime": ogCellModemSessionTime,
       "ogCellModemSelectedSimCard": ogCellModemSelectedSimCard,
       "ogCellModemTemperature": ogCellModemTemperature,
       "ogCellModemCounter": ogCellModemCounter,
       "ogWifiClientTable": ogWifiClientTable,
       "ogWifiClientEntry": ogWifiClientEntry,
       "ogWifiClientIndex": ogWifiClientIndex,
       "ogWifiClientInterface": ogWifiClientInterface,
       "ogWifiClientEnabled": ogWifiClientEnabled,
       "ogWifiClientEssid": ogWifiClientEssid,
       "ogWifiClientIeeeMode": ogWifiClientIeeeMode,
       "ogWifiClientMode": ogWifiClientMode,
       "ogWifiClientFrequency": ogWifiClientFrequency,
       "ogWifiClientApMac": ogWifiClientApMac,
       "ogWifiClientBitRate": ogWifiClientBitRate,
       "ogWifiClientTxPower": ogWifiClientTxPower,
       "ogWifiClientLinkQuality": ogWifiClientLinkQuality,
       "ogWifiClientRssi": ogWifiClientRssi,
       "ogWifiClientRxInvalidNwid": ogWifiClientRxInvalidNwid,
       "ogWifiClientRxInvalidCrypt": ogWifiClientRxInvalidCrypt,
       "ogWifiClientRxInvalidFrag": ogWifiClientRxInvalidFrag,
       "ogWifiClientRxInvalidRetries": ogWifiClientRxInvalidRetries,
       "ogWifiClientRxInvalidMisc": ogWifiClientRxInvalidMisc,
       "ogWifiClientMissedBeacon": ogWifiClientMissedBeacon,
       "ogWifiClientCounter": ogWifiClientCounter,
       "ogWifiApTable": ogWifiApTable,
       "ogWifiApEntry": ogWifiApEntry,
       "ogWifiApIndex": ogWifiApIndex,
       "ogWifiApInterface": ogWifiApInterface,
       "ogWifiApEnabled": ogWifiApEnabled,
       "ogWifiApSsid": ogWifiApSsid,
       "ogWifiApIeeeMode": ogWifiApIeeeMode,
       "ogWifiApFrequency": ogWifiApFrequency,
       "ogWifiApTxPower": ogWifiApTxPower,
       "ogWifiApCounter": ogWifiApCounter,
       "ogWifiApClientTable": ogWifiApClientTable,
       "ogWifiApClientEntry": ogWifiApClientEntry,
       "ogWifiApClientIndex": ogWifiApClientIndex,
       "ogWifiApClientAp": ogWifiApClientAp,
       "ogWifiApClientMac": ogWifiApClientMac,
       "ogWifiApClientInactiveTime": ogWifiApClientInactiveTime,
       "ogWifiApClientRxBytes": ogWifiApClientRxBytes,
       "ogWifiApClientRxPackets": ogWifiApClientRxPackets,
       "ogWifiApClientTxBytes": ogWifiApClientTxBytes,
       "ogWifiApClientTxPackets": ogWifiApClientTxPackets,
       "ogWifiApClientRssi": ogWifiApClientRssi,
       "ogWifiApClientTxBitRate": ogWifiApClientTxBitRate,
       "ogCheckTable": ogCheckTable,
       "ogCheckEntry": ogCheckEntry,
       "ogCheckIndex": ogCheckIndex,
       "ogCheckName": ogCheckName,
       "ogCheckRepeatTimeout": ogCheckRepeatTimeout,
       "ogCheckResetTimeout": ogCheckResetTimeout,
       "ogCheckType": ogCheckType,
       "ogCheckTriggerActions": ogCheckTriggerActions,
       "ogCheckResolveActions": ogCheckResolveActions,
       "ogCheckDeviceTable": ogCheckDeviceTable,
       "ogCheckDeviceEntry": ogCheckDeviceEntry,
       "ogCheckDeviceIndex": ogCheckDeviceIndex,
       "ogCheckDeviceCheck": ogCheckDeviceCheck,
       "ogCheckDeviceName": ogCheckDeviceName,
       "ogCheckDeviceRef": ogCheckDeviceRef,
       "ogAlarm": ogAlarm,
       "ogAlarmLogTable": ogAlarmLogTable,
       "ogAlarmLogEntry": ogAlarmLogEntry,
       "ogAlarmLogIndex": ogAlarmLogIndex,
       "ogAlarmEventId": ogAlarmEventId,
       "ogAlarmName": ogAlarmName,
       "ogAlarmCheck": ogAlarmCheck,
       "ogAlarmInstance": ogAlarmInstance,
       "ogAlarmTime": ogAlarmTime,
       "ogAlarmType": ogAlarmType,
       "ogAlarmSummary": ogAlarmSummary,
       "ogAlarmDevice": ogAlarmDevice,
       "ogAlarmUser": ogAlarmUser,
       "ogAlarmTriggerValue": ogAlarmTriggerValue,
       "ogAlarmCurrentValue": ogAlarmCurrentValue,
       "ogAlarmPreviousValue": ogAlarmPreviousValue,
       "ogAlarmState": ogAlarmState,
       "ogCurrentAlarmTable": ogCurrentAlarmTable,
       "ogCurrentAlarmEntry": ogCurrentAlarmEntry,
       "ogCurrentAlarmIndex": ogCurrentAlarmIndex,
       "ogCurrentAlarmEventId": ogCurrentAlarmEventId,
       "ogCurrentAlarmName": ogCurrentAlarmName,
       "ogCurrentAlarmCheck": ogCurrentAlarmCheck,
       "ogCurrentAlarmInstance": ogCurrentAlarmInstance,
       "ogCurrentAlarmTime": ogCurrentAlarmTime,
       "ogCurrentAlarmType": ogCurrentAlarmType,
       "ogCurrentAlarmSummary": ogCurrentAlarmSummary,
       "ogCurrentAlarmDevice": ogCurrentAlarmDevice,
       "ogCurrentAlarmUser": ogCurrentAlarmUser,
       "ogCurrentAlarmTriggerValue": ogCurrentAlarmTriggerValue,
       "ogCurrentAlarmCurrentValue": ogCurrentAlarmCurrentValue,
       "ogCurrentAlarmPreviousValue": ogCurrentAlarmPreviousValue,
       "ogCurrentAlarmState": ogCurrentAlarmState,
       "ogStatus2NotificationPrefix": ogStatus2NotificationPrefix,
       "ogMibNotifications": ogMibNotifications,
       "ogSerialSignalNotification": ogSerialSignalNotification,
       "ogSerialPatternNotification": ogSerialPatternNotification,
       "ogSerialUserNotification": ogSerialUserNotification,
       "ogHostPingNotification": ogHostPingNotification,
       "ogHostServiceNotification": ogHostServiceNotification,
       "ogHostUserNotification": ogHostUserNotification,
       "ogWebUserNotification": ogWebUserNotification,
       "ogEmdTemperatureNotification": ogEmdTemperatureNotification,
       "ogEmdHumidityNotification": ogEmdHumidityNotification,
       "ogEmdDioNotification": ogEmdDioNotification,
       "ogPowerSupplyInputNotification": ogPowerSupplyInputNotification,
       "ogPowerSupplyOutputNotification": ogPowerSupplyOutputNotification,
       "ogPowerSupplyTempNotification": ogPowerSupplyTempNotification,
       "ogUpsNotification": ogUpsNotification,
       "ogUpsBatteryNotification": ogUpsBatteryNotification,
       "ogUpsInputNotification": ogUpsInputNotification,
       "ogUpsOutputNotification": ogUpsOutputNotification,
       "ogRpcInputNotification": ogRpcInputNotification,
       "ogRpcOutputNotification": ogRpcOutputNotification,
       "ogRpcOutletNotification": ogRpcOutletNotification,
       "ogNetInterfaceNotification": ogNetInterfaceNotification,
       "ogCellDataNotification": ogCellDataNotification,
       "ogCellMessageNotification": ogCellMessageNotification,
       "ogCellSignalNotification": ogCellSignalNotification,
       "ogCellApnNotification": ogCellApnNotification,
       "ogCellTowerNotification": ogCellTowerNotification,
       "ogCellNetworkNotification": ogCellNetworkNotification,
       "ogWifiClientConnectNotification": ogWifiClientConnectNotification,
       "ogWifiClientSignalNotification": ogWifiClientSignalNotification,
       "ogWifiApAssociationNotification": ogWifiApAssociationNotification,
       "ogWifiApAuthNotification": ogWifiApAuthNotification,
       "ogDialPoolHealthNotification": ogDialPoolHealthNotification,
       "ogCustomNotification": ogCustomNotification,
       "ogStatus2Conformance": ogStatus2Conformance,
       "ogStatus2Compliances": ogStatus2Compliances,
       "ogStatus2Compliance": ogStatus2Compliance,
       "ogStatus2Groups": ogStatus2Groups,
       "ogBasicStatusGroup": ogBasicStatusGroup,
       "ogBasicAlarmGroup": ogBasicAlarmGroup,
       "ogBasicNotificationGroup": ogBasicNotificationGroup}
)
