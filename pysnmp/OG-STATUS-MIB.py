# SNMP MIB module (OG-STATUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OG-STATUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:52 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ogStatus = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 16)
)
ogStatus.setRevisions(
        ("2013-08-16 00:00",
         "2013-08-11 00:00",
         "2010-08-15 00:00",
         "2010-01-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OgSerialPortStatusTable_Object = MibTable
ogSerialPortStatusTable = _OgSerialPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 1)
)
if mibBuilder.loadTexts:
    ogSerialPortStatusTable.setStatus("current")
_OgSerialPortStatusEntry_Object = MibTableRow
ogSerialPortStatusEntry = _OgSerialPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 1, 1)
)
ogSerialPortStatusEntry.setIndexNames(
    (0, "OG-STATUS-MIB", "ogSerialPortStatusIndex"),
)
if mibBuilder.loadTexts:
    ogSerialPortStatusEntry.setStatus("current")


class _OgSerialPortStatusIndex_Type(Integer32):
    """Custom type ogSerialPortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_OgSerialPortStatusIndex_Type.__name__ = "Integer32"
_OgSerialPortStatusIndex_Object = MibTableColumn
ogSerialPortStatusIndex = _OgSerialPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 1, 1, 1),
    _OgSerialPortStatusIndex_Type()
)
ogSerialPortStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogSerialPortStatusIndex.setStatus("current")


class _OgSerialPortStatusPort_Type(Integer32):
    """Custom type ogSerialPortStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_OgSerialPortStatusPort_Type.__name__ = "Integer32"
_OgSerialPortStatusPort_Object = MibTableColumn
ogSerialPortStatusPort = _OgSerialPortStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 1, 1, 2),
    _OgSerialPortStatusPort_Type()
)
ogSerialPortStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortStatusPort.setStatus("current")
_OgSerialPortStatusRxBytes_Type = Counter64
_OgSerialPortStatusRxBytes_Object = MibTableColumn
ogSerialPortStatusRxBytes = _OgSerialPortStatusRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 1, 1, 3),
    _OgSerialPortStatusRxBytes_Type()
)
ogSerialPortStatusRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortStatusRxBytes.setStatus("current")
_OgSerialPortStatusTxBytes_Type = Counter64
_OgSerialPortStatusTxBytes_Object = MibTableColumn
ogSerialPortStatusTxBytes = _OgSerialPortStatusTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 1, 1, 4),
    _OgSerialPortStatusTxBytes_Type()
)
ogSerialPortStatusTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortStatusTxBytes.setStatus("current")
_OgSerialPortStatusSpeed_Type = Integer32
_OgSerialPortStatusSpeed_Object = MibTableColumn
ogSerialPortStatusSpeed = _OgSerialPortStatusSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 1, 1, 5),
    _OgSerialPortStatusSpeed_Type()
)
ogSerialPortStatusSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortStatusSpeed.setStatus("current")


class _OgSerialPortStatusDCD_Type(Integer32):
    """Custom type ogSerialPortStatusDCD based on Integer32"""
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


_OgSerialPortStatusDCD_Type.__name__ = "Integer32"
_OgSerialPortStatusDCD_Object = MibTableColumn
ogSerialPortStatusDCD = _OgSerialPortStatusDCD_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 1, 1, 6),
    _OgSerialPortStatusDCD_Type()
)
ogSerialPortStatusDCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortStatusDCD.setStatus("current")


class _OgSerialPortStatusDTR_Type(Integer32):
    """Custom type ogSerialPortStatusDTR based on Integer32"""
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


_OgSerialPortStatusDTR_Type.__name__ = "Integer32"
_OgSerialPortStatusDTR_Object = MibTableColumn
ogSerialPortStatusDTR = _OgSerialPortStatusDTR_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 1, 1, 7),
    _OgSerialPortStatusDTR_Type()
)
ogSerialPortStatusDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortStatusDTR.setStatus("current")


class _OgSerialPortStatusDSR_Type(Integer32):
    """Custom type ogSerialPortStatusDSR based on Integer32"""
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


_OgSerialPortStatusDSR_Type.__name__ = "Integer32"
_OgSerialPortStatusDSR_Object = MibTableColumn
ogSerialPortStatusDSR = _OgSerialPortStatusDSR_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 1, 1, 8),
    _OgSerialPortStatusDSR_Type()
)
ogSerialPortStatusDSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortStatusDSR.setStatus("current")


class _OgSerialPortStatusCTS_Type(Integer32):
    """Custom type ogSerialPortStatusCTS based on Integer32"""
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


_OgSerialPortStatusCTS_Type.__name__ = "Integer32"
_OgSerialPortStatusCTS_Object = MibTableColumn
ogSerialPortStatusCTS = _OgSerialPortStatusCTS_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 1, 1, 9),
    _OgSerialPortStatusCTS_Type()
)
ogSerialPortStatusCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortStatusCTS.setStatus("current")


class _OgSerialPortStatusRTS_Type(Integer32):
    """Custom type ogSerialPortStatusRTS based on Integer32"""
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


_OgSerialPortStatusRTS_Type.__name__ = "Integer32"
_OgSerialPortStatusRTS_Object = MibTableColumn
ogSerialPortStatusRTS = _OgSerialPortStatusRTS_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 1, 1, 10),
    _OgSerialPortStatusRTS_Type()
)
ogSerialPortStatusRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortStatusRTS.setStatus("current")


class _OgSerialPortStatusLabel_Type(DisplayString):
    """Custom type ogSerialPortStatusLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgSerialPortStatusLabel_Type.__name__ = "DisplayString"
_OgSerialPortStatusLabel_Object = MibTableColumn
ogSerialPortStatusLabel = _OgSerialPortStatusLabel_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 1, 1, 11),
    _OgSerialPortStatusLabel_Type()
)
ogSerialPortStatusLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortStatusLabel.setStatus("current")
_OgSerialPortActiveUsersTable_Object = MibTable
ogSerialPortActiveUsersTable = _OgSerialPortActiveUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 2)
)
if mibBuilder.loadTexts:
    ogSerialPortActiveUsersTable.setStatus("current")
_OgSerialPortActiveUsersEntry_Object = MibTableRow
ogSerialPortActiveUsersEntry = _OgSerialPortActiveUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 2, 1)
)
ogSerialPortActiveUsersEntry.setIndexNames(
    (0, "OG-STATUS-MIB", "ogSerialPortActiveUsersIndex"),
)
if mibBuilder.loadTexts:
    ogSerialPortActiveUsersEntry.setStatus("current")


class _OgSerialPortActiveUsersIndex_Type(Integer32):
    """Custom type ogSerialPortActiveUsersIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_OgSerialPortActiveUsersIndex_Type.__name__ = "Integer32"
_OgSerialPortActiveUsersIndex_Object = MibTableColumn
ogSerialPortActiveUsersIndex = _OgSerialPortActiveUsersIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 2, 1, 1),
    _OgSerialPortActiveUsersIndex_Type()
)
ogSerialPortActiveUsersIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogSerialPortActiveUsersIndex.setStatus("current")


class _OgSerialPortActiveUsersPort_Type(Integer32):
    """Custom type ogSerialPortActiveUsersPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_OgSerialPortActiveUsersPort_Type.__name__ = "Integer32"
_OgSerialPortActiveUsersPort_Object = MibTableColumn
ogSerialPortActiveUsersPort = _OgSerialPortActiveUsersPort_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 2, 1, 2),
    _OgSerialPortActiveUsersPort_Type()
)
ogSerialPortActiveUsersPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortActiveUsersPort.setStatus("current")


class _OgSerialPortActiveUsersName_Type(DisplayString):
    """Custom type ogSerialPortActiveUsersName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgSerialPortActiveUsersName_Type.__name__ = "DisplayString"
_OgSerialPortActiveUsersName_Object = MibTableColumn
ogSerialPortActiveUsersName = _OgSerialPortActiveUsersName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 2, 1, 3),
    _OgSerialPortActiveUsersName_Type()
)
ogSerialPortActiveUsersName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortActiveUsersName.setStatus("current")


class _OgSerialPortActiveUsersPortLabel_Type(DisplayString):
    """Custom type ogSerialPortActiveUsersPortLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgSerialPortActiveUsersPortLabel_Type.__name__ = "DisplayString"
_OgSerialPortActiveUsersPortLabel_Object = MibTableColumn
ogSerialPortActiveUsersPortLabel = _OgSerialPortActiveUsersPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 2, 1, 4),
    _OgSerialPortActiveUsersPortLabel_Type()
)
ogSerialPortActiveUsersPortLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSerialPortActiveUsersPortLabel.setStatus("current")
_OgRpcStatusTable_Object = MibTable
ogRpcStatusTable = _OgRpcStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 3)
)
if mibBuilder.loadTexts:
    ogRpcStatusTable.setStatus("current")
_OgRpcStatusEntry_Object = MibTableRow
ogRpcStatusEntry = _OgRpcStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 3, 1)
)
ogRpcStatusEntry.setIndexNames(
    (0, "OG-STATUS-MIB", "ogRpcStatusIndex"),
)
if mibBuilder.loadTexts:
    ogRpcStatusEntry.setStatus("current")


class _OgRpcStatusIndex_Type(Integer32):
    """Custom type ogRpcStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgRpcStatusIndex_Type.__name__ = "Integer32"
_OgRpcStatusIndex_Object = MibTableColumn
ogRpcStatusIndex = _OgRpcStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 3, 1, 1),
    _OgRpcStatusIndex_Type()
)
ogRpcStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogRpcStatusIndex.setStatus("current")


class _OgRpcStatusName_Type(DisplayString):
    """Custom type ogRpcStatusName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgRpcStatusName_Type.__name__ = "DisplayString"
_OgRpcStatusName_Object = MibTableColumn
ogRpcStatusName = _OgRpcStatusName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 3, 1, 2),
    _OgRpcStatusName_Type()
)
ogRpcStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogRpcStatusName.setStatus("current")
_OgRpcStatusMaxTemp_Type = Integer32
_OgRpcStatusMaxTemp_Object = MibTableColumn
ogRpcStatusMaxTemp = _OgRpcStatusMaxTemp_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 3, 1, 3),
    _OgRpcStatusMaxTemp_Type()
)
ogRpcStatusMaxTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogRpcStatusMaxTemp.setStatus("current")
_OgRpcStatusAlertCount_Type = Integer32
_OgRpcStatusAlertCount_Object = MibTableColumn
ogRpcStatusAlertCount = _OgRpcStatusAlertCount_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 3, 1, 4),
    _OgRpcStatusAlertCount_Type()
)
ogRpcStatusAlertCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogRpcStatusAlertCount.setStatus("current")
_OgEmdStatusTable_Object = MibTable
ogEmdStatusTable = _OgEmdStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 4)
)
if mibBuilder.loadTexts:
    ogEmdStatusTable.setStatus("current")
_OgEmdStatusEntry_Object = MibTableRow
ogEmdStatusEntry = _OgEmdStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 4, 1)
)
ogEmdStatusEntry.setIndexNames(
    (0, "OG-STATUS-MIB", "ogEmdStatusIndex"),
)
if mibBuilder.loadTexts:
    ogEmdStatusEntry.setStatus("current")


class _OgEmdStatusIndex_Type(Integer32):
    """Custom type ogEmdStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgEmdStatusIndex_Type.__name__ = "Integer32"
_OgEmdStatusIndex_Object = MibTableColumn
ogEmdStatusIndex = _OgEmdStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 4, 1, 1),
    _OgEmdStatusIndex_Type()
)
ogEmdStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogEmdStatusIndex.setStatus("current")


class _OgEmdStatusName_Type(DisplayString):
    """Custom type ogEmdStatusName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgEmdStatusName_Type.__name__ = "DisplayString"
_OgEmdStatusName_Object = MibTableColumn
ogEmdStatusName = _OgEmdStatusName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 4, 1, 2),
    _OgEmdStatusName_Type()
)
ogEmdStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdStatusName.setStatus("current")
_OgEmdStatusTemp_Type = Integer32
_OgEmdStatusTemp_Object = MibTableColumn
ogEmdStatusTemp = _OgEmdStatusTemp_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 4, 1, 3),
    _OgEmdStatusTemp_Type()
)
ogEmdStatusTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdStatusTemp.setStatus("current")
_OgEmdStatusHumidity_Type = Integer32
_OgEmdStatusHumidity_Object = MibTableColumn
ogEmdStatusHumidity = _OgEmdStatusHumidity_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 4, 1, 4),
    _OgEmdStatusHumidity_Type()
)
ogEmdStatusHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdStatusHumidity.setStatus("current")
_OgEmdStatusAlertCount_Type = Integer32
_OgEmdStatusAlertCount_Object = MibTableColumn
ogEmdStatusAlertCount = _OgEmdStatusAlertCount_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 4, 1, 5),
    _OgEmdStatusAlertCount_Type()
)
ogEmdStatusAlertCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEmdStatusAlertCount.setStatus("current")
_OgDioStatusTable_Object = MibTable
ogDioStatusTable = _OgDioStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 5)
)
if mibBuilder.loadTexts:
    ogDioStatusTable.setStatus("current")
_OgDioStatusEntry_Object = MibTableRow
ogDioStatusEntry = _OgDioStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 5, 1)
)
ogDioStatusEntry.setIndexNames(
    (0, "OG-STATUS-MIB", "ogDioStatusIndex"),
)
if mibBuilder.loadTexts:
    ogDioStatusEntry.setStatus("current")


class _OgDioStatusIndex_Type(Integer32):
    """Custom type ogDioStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgDioStatusIndex_Type.__name__ = "Integer32"
_OgDioStatusIndex_Object = MibTableColumn
ogDioStatusIndex = _OgDioStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 5, 1, 1),
    _OgDioStatusIndex_Type()
)
ogDioStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogDioStatusIndex.setStatus("current")


class _OgDioStatusName_Type(DisplayString):
    """Custom type ogDioStatusName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgDioStatusName_Type.__name__ = "DisplayString"
_OgDioStatusName_Object = MibTableColumn
ogDioStatusName = _OgDioStatusName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 5, 1, 2),
    _OgDioStatusName_Type()
)
ogDioStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogDioStatusName.setStatus("current")


class _OgDioStatusType_Type(Integer32):
    """Custom type ogDioStatusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("highVoltageOutput", 1),
          ("ttlInputOutput", 0))
    )


_OgDioStatusType_Type.__name__ = "Integer32"
_OgDioStatusType_Object = MibTableColumn
ogDioStatusType = _OgDioStatusType_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 5, 1, 3),
    _OgDioStatusType_Type()
)
ogDioStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogDioStatusType.setStatus("current")


class _OgDioStatusDirection_Type(Integer32):
    """Custom type ogDioStatusDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 0))
    )


_OgDioStatusDirection_Type.__name__ = "Integer32"
_OgDioStatusDirection_Object = MibTableColumn
ogDioStatusDirection = _OgDioStatusDirection_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 5, 1, 4),
    _OgDioStatusDirection_Type()
)
ogDioStatusDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogDioStatusDirection.setStatus("current")


class _OgDioStatusState_Type(Integer32):
    """Custom type ogDioStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OgDioStatusState_Type.__name__ = "Integer32"
_OgDioStatusState_Object = MibTableColumn
ogDioStatusState = _OgDioStatusState_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 5, 1, 5),
    _OgDioStatusState_Type()
)
ogDioStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogDioStatusState.setStatus("current")
_OgDioStatusCounter_Type = Counter64
_OgDioStatusCounter_Object = MibTableColumn
ogDioStatusCounter = _OgDioStatusCounter_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 5, 1, 6),
    _OgDioStatusCounter_Type()
)
ogDioStatusCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogDioStatusCounter.setStatus("current")


class _OgDioStatusTriggerMode_Type(Integer32):
    """Custom type ogDioStatusTriggerMode based on Integer32"""
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
        *(("fallingEdge", 2),
          ("invalid", 0),
          ("risingEdge", 1),
          ("risingFallingEdge", 3))
    )


_OgDioStatusTriggerMode_Type.__name__ = "Integer32"
_OgDioStatusTriggerMode_Object = MibTableColumn
ogDioStatusTriggerMode = _OgDioStatusTriggerMode_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 5, 1, 7),
    _OgDioStatusTriggerMode_Type()
)
ogDioStatusTriggerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogDioStatusTriggerMode.setStatus("current")
_OgSignalAlertStatusTable_Object = MibTable
ogSignalAlertStatusTable = _OgSignalAlertStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 6)
)
if mibBuilder.loadTexts:
    ogSignalAlertStatusTable.setStatus("current")
_OgSignalAlertStatusEntry_Object = MibTableRow
ogSignalAlertStatusEntry = _OgSignalAlertStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 6, 1)
)
ogSignalAlertStatusEntry.setIndexNames(
    (0, "OG-STATUS-MIB", "ogSignalAlertStatusIndex"),
)
if mibBuilder.loadTexts:
    ogSignalAlertStatusEntry.setStatus("current")


class _OgSignalAlertStatusIndex_Type(Integer32):
    """Custom type ogSignalAlertStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgSignalAlertStatusIndex_Type.__name__ = "Integer32"
_OgSignalAlertStatusIndex_Object = MibTableColumn
ogSignalAlertStatusIndex = _OgSignalAlertStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 6, 1, 1),
    _OgSignalAlertStatusIndex_Type()
)
ogSignalAlertStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogSignalAlertStatusIndex.setStatus("current")
_OgSignalAlertStatusPort_Type = Integer32
_OgSignalAlertStatusPort_Object = MibTableColumn
ogSignalAlertStatusPort = _OgSignalAlertStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 6, 1, 2),
    _OgSignalAlertStatusPort_Type()
)
ogSignalAlertStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSignalAlertStatusPort.setStatus("current")
_OgSignalAlertStatusLabel_Type = DisplayString
_OgSignalAlertStatusLabel_Object = MibTableColumn
ogSignalAlertStatusLabel = _OgSignalAlertStatusLabel_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 6, 1, 3),
    _OgSignalAlertStatusLabel_Type()
)
ogSignalAlertStatusLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSignalAlertStatusLabel.setStatus("current")
_OgSignalAlertStatusSignalName_Type = DisplayString
_OgSignalAlertStatusSignalName_Object = MibTableColumn
ogSignalAlertStatusSignalName = _OgSignalAlertStatusSignalName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 6, 1, 4),
    _OgSignalAlertStatusSignalName_Type()
)
ogSignalAlertStatusSignalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSignalAlertStatusSignalName.setStatus("current")


class _OgSignalAlertStatusState_Type(Integer32):
    """Custom type ogSignalAlertStatusState based on Integer32"""
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


_OgSignalAlertStatusState_Type.__name__ = "Integer32"
_OgSignalAlertStatusState_Object = MibTableColumn
ogSignalAlertStatusState = _OgSignalAlertStatusState_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 6, 1, 5),
    _OgSignalAlertStatusState_Type()
)
ogSignalAlertStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogSignalAlertStatusState.setStatus("current")
_OgEnvAlertStatusTable_Object = MibTable
ogEnvAlertStatusTable = _OgEnvAlertStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 7)
)
if mibBuilder.loadTexts:
    ogEnvAlertStatusTable.setStatus("current")
_OgEnvAlertStatusEntry_Object = MibTableRow
ogEnvAlertStatusEntry = _OgEnvAlertStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 7, 1)
)
ogEnvAlertStatusEntry.setIndexNames(
    (0, "OG-STATUS-MIB", "ogEnvAlertStatusIndex"),
)
if mibBuilder.loadTexts:
    ogEnvAlertStatusEntry.setStatus("current")


class _OgEnvAlertStatusIndex_Type(Integer32):
    """Custom type ogEnvAlertStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgEnvAlertStatusIndex_Type.__name__ = "Integer32"
_OgEnvAlertStatusIndex_Object = MibTableColumn
ogEnvAlertStatusIndex = _OgEnvAlertStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 7, 1, 1),
    _OgEnvAlertStatusIndex_Type()
)
ogEnvAlertStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogEnvAlertStatusIndex.setStatus("current")
_OgEnvAlertStatusDevice_Type = DisplayString
_OgEnvAlertStatusDevice_Object = MibTableColumn
ogEnvAlertStatusDevice = _OgEnvAlertStatusDevice_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 7, 1, 2),
    _OgEnvAlertStatusDevice_Type()
)
ogEnvAlertStatusDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEnvAlertStatusDevice.setStatus("current")
_OgEnvAlertStatusSensor_Type = DisplayString
_OgEnvAlertStatusSensor_Object = MibTableColumn
ogEnvAlertStatusSensor = _OgEnvAlertStatusSensor_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 7, 1, 3),
    _OgEnvAlertStatusSensor_Type()
)
ogEnvAlertStatusSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEnvAlertStatusSensor.setStatus("current")
_OgEnvAlertStatusOutlet_Type = Integer32
_OgEnvAlertStatusOutlet_Object = MibTableColumn
ogEnvAlertStatusOutlet = _OgEnvAlertStatusOutlet_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 7, 1, 4),
    _OgEnvAlertStatusOutlet_Type()
)
ogEnvAlertStatusOutlet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEnvAlertStatusOutlet.setStatus("current")
_OgEnvAlertStatusValue_Type = Integer32
_OgEnvAlertStatusValue_Object = MibTableColumn
ogEnvAlertStatusValue = _OgEnvAlertStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 7, 1, 5),
    _OgEnvAlertStatusValue_Type()
)
ogEnvAlertStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEnvAlertStatusValue.setStatus("current")
_OgEnvAlertStatusOldValue_Type = Integer32
_OgEnvAlertStatusOldValue_Object = MibTableColumn
ogEnvAlertStatusOldValue = _OgEnvAlertStatusOldValue_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 7, 1, 6),
    _OgEnvAlertStatusOldValue_Type()
)
ogEnvAlertStatusOldValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEnvAlertStatusOldValue.setStatus("current")
_OgEnvAlertStatusStatus_Type = Integer32
_OgEnvAlertStatusStatus_Object = MibTableColumn
ogEnvAlertStatusStatus = _OgEnvAlertStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 7, 1, 7),
    _OgEnvAlertStatusStatus_Type()
)
ogEnvAlertStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogEnvAlertStatusStatus.setStatus("current")
_OgNutAlertStatusTable_Object = MibTable
ogNutAlertStatusTable = _OgNutAlertStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 8)
)
if mibBuilder.loadTexts:
    ogNutAlertStatusTable.setStatus("current")
_OgNutAlertStatusEntry_Object = MibTableRow
ogNutAlertStatusEntry = _OgNutAlertStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 8, 1)
)
ogNutAlertStatusEntry.setIndexNames(
    (0, "OG-STATUS-MIB", "ogNutAlertStatusIndex"),
)
if mibBuilder.loadTexts:
    ogNutAlertStatusEntry.setStatus("current")


class _OgNutAlertStatusIndex_Type(Integer32):
    """Custom type ogNutAlertStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgNutAlertStatusIndex_Type.__name__ = "Integer32"
_OgNutAlertStatusIndex_Object = MibTableColumn
ogNutAlertStatusIndex = _OgNutAlertStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 8, 1, 1),
    _OgNutAlertStatusIndex_Type()
)
ogNutAlertStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogNutAlertStatusIndex.setStatus("current")
_OgNutAlertStatusPort_Type = Integer32
_OgNutAlertStatusPort_Object = MibTableColumn
ogNutAlertStatusPort = _OgNutAlertStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 8, 1, 2),
    _OgNutAlertStatusPort_Type()
)
ogNutAlertStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogNutAlertStatusPort.setStatus("current")
_OgNutAlertStatusName_Type = DisplayString
_OgNutAlertStatusName_Object = MibTableColumn
ogNutAlertStatusName = _OgNutAlertStatusName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 8, 1, 3),
    _OgNutAlertStatusName_Type()
)
ogNutAlertStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogNutAlertStatusName.setStatus("current")
_OgNutAlertStatusHost_Type = DisplayString
_OgNutAlertStatusHost_Object = MibTableColumn
ogNutAlertStatusHost = _OgNutAlertStatusHost_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 8, 1, 4),
    _OgNutAlertStatusHost_Type()
)
ogNutAlertStatusHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogNutAlertStatusHost.setStatus("current")
_OgNutAlertStatusStatus_Type = DisplayString
_OgNutAlertStatusStatus_Object = MibTableColumn
ogNutAlertStatusStatus = _OgNutAlertStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 8, 1, 5),
    _OgNutAlertStatusStatus_Type()
)
ogNutAlertStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogNutAlertStatusStatus.setStatus("current")
_OgDataAlertStatusTable_Object = MibTable
ogDataAlertStatusTable = _OgDataAlertStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 9)
)
if mibBuilder.loadTexts:
    ogDataAlertStatusTable.setStatus("current")
_OgDataAlertStatusEntry_Object = MibTableRow
ogDataAlertStatusEntry = _OgDataAlertStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 9, 1)
)
ogDataAlertStatusEntry.setIndexNames(
    (0, "OG-STATUS-MIB", "ogDataAlertStatusIndex"),
)
if mibBuilder.loadTexts:
    ogDataAlertStatusEntry.setStatus("current")


class _OgDataAlertStatusIndex_Type(Integer32):
    """Custom type ogDataAlertStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgDataAlertStatusIndex_Type.__name__ = "Integer32"
_OgDataAlertStatusIndex_Object = MibTableColumn
ogDataAlertStatusIndex = _OgDataAlertStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 9, 1, 1),
    _OgDataAlertStatusIndex_Type()
)
ogDataAlertStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogDataAlertStatusIndex.setStatus("current")
_OgDataAlertStatusBytes_Type = Integer32
_OgDataAlertStatusBytes_Object = MibTableColumn
ogDataAlertStatusBytes = _OgDataAlertStatusBytes_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 9, 1, 2),
    _OgDataAlertStatusBytes_Type()
)
ogDataAlertStatusBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogDataAlertStatusBytes.setStatus("current")
_OgDataAlertStatusSeconds_Type = Integer32
_OgDataAlertStatusSeconds_Object = MibTableColumn
ogDataAlertStatusSeconds = _OgDataAlertStatusSeconds_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 9, 1, 3),
    _OgDataAlertStatusSeconds_Type()
)
ogDataAlertStatusSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogDataAlertStatusSeconds.setStatus("current")
_OgDataAlertStatusDevice_Type = DisplayString
_OgDataAlertStatusDevice_Object = MibTableColumn
ogDataAlertStatusDevice = _OgDataAlertStatusDevice_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 9, 1, 4),
    _OgDataAlertStatusDevice_Type()
)
ogDataAlertStatusDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogDataAlertStatusDevice.setStatus("current")


class _OgDataAlertStatusState_Type(Integer32):
    """Custom type ogDataAlertStatusState based on Integer32"""
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


_OgDataAlertStatusState_Type.__name__ = "Integer32"
_OgDataAlertStatusState_Object = MibTableColumn
ogDataAlertStatusState = _OgDataAlertStatusState_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 9, 1, 5),
    _OgDataAlertStatusState_Type()
)
ogDataAlertStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogDataAlertStatusState.setStatus("current")
_OgDioAlertStatusTable_Object = MibTable
ogDioAlertStatusTable = _OgDioAlertStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 10)
)
if mibBuilder.loadTexts:
    ogDioAlertStatusTable.setStatus("current")
_OgDioAlertStatusEntry_Object = MibTableRow
ogDioAlertStatusEntry = _OgDioAlertStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 10, 1)
)
ogDioAlertStatusEntry.setIndexNames(
    (0, "OG-STATUS-MIB", "ogDioAlertStatusIndex"),
)
if mibBuilder.loadTexts:
    ogDioAlertStatusEntry.setStatus("current")


class _OgDioAlertStatusIndex_Type(Integer32):
    """Custom type ogDioAlertStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgDioAlertStatusIndex_Type.__name__ = "Integer32"
_OgDioAlertStatusIndex_Object = MibTableColumn
ogDioAlertStatusIndex = _OgDioAlertStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 10, 1, 1),
    _OgDioAlertStatusIndex_Type()
)
ogDioAlertStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogDioAlertStatusIndex.setStatus("current")
_OgDioAlertStatusName_Type = DisplayString
_OgDioAlertStatusName_Object = MibTableColumn
ogDioAlertStatusName = _OgDioAlertStatusName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 10, 1, 2),
    _OgDioAlertStatusName_Type()
)
ogDioAlertStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogDioAlertStatusName.setStatus("current")


class _OgDioAlertStatusValue_Type(Integer32):
    """Custom type ogDioAlertStatusValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 0))
    )


_OgDioAlertStatusValue_Type.__name__ = "Integer32"
_OgDioAlertStatusValue_Object = MibTableColumn
ogDioAlertStatusValue = _OgDioAlertStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 10, 1, 3),
    _OgDioAlertStatusValue_Type()
)
ogDioAlertStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogDioAlertStatusValue.setStatus("current")


class _OgDioAlertStatusOldValue_Type(Integer32):
    """Custom type ogDioAlertStatusOldValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 0))
    )


_OgDioAlertStatusOldValue_Type.__name__ = "Integer32"
_OgDioAlertStatusOldValue_Object = MibTableColumn
ogDioAlertStatusOldValue = _OgDioAlertStatusOldValue_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 10, 1, 4),
    _OgDioAlertStatusOldValue_Type()
)
ogDioAlertStatusOldValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogDioAlertStatusOldValue.setStatus("current")


class _OgDioAlertStatusTriggered_Type(Integer32):
    """Custom type ogDioAlertStatusTriggered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_OgDioAlertStatusTriggered_Type.__name__ = "Integer32"
_OgDioAlertStatusTriggered_Object = MibTableColumn
ogDioAlertStatusTriggered = _OgDioAlertStatusTriggered_Object(
    (1, 3, 6, 1, 4, 1, 25049, 16, 10, 1, 5),
    _OgDioAlertStatusTriggered_Type()
)
ogDioAlertStatusTriggered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogDioAlertStatusTriggered.setStatus("current")
_OgStatusConformance_ObjectIdentity = ObjectIdentity
ogStatusConformance = _OgStatusConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 16, 65535)
)
_OgStatusCompliances_ObjectIdentity = ObjectIdentity
ogStatusCompliances = _OgStatusCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 16, 65535, 1)
)
_OgStatusGroups_ObjectIdentity = ObjectIdentity
ogStatusGroups = _OgStatusGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 16, 65535, 2)
)

# Managed Objects groups

ogBasicStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25049, 16, 65535, 2, 1)
)
ogBasicStatusGroup.setObjects(
      *(("OG-STATUS-MIB", "ogSerialPortStatusPort"),
        ("OG-STATUS-MIB", "ogSerialPortStatusRxBytes"),
        ("OG-STATUS-MIB", "ogSerialPortStatusTxBytes"),
        ("OG-STATUS-MIB", "ogSerialPortStatusSpeed"),
        ("OG-STATUS-MIB", "ogSerialPortStatusDCD"),
        ("OG-STATUS-MIB", "ogSerialPortStatusDTR"),
        ("OG-STATUS-MIB", "ogSerialPortStatusDSR"),
        ("OG-STATUS-MIB", "ogSerialPortStatusCTS"),
        ("OG-STATUS-MIB", "ogSerialPortStatusRTS"),
        ("OG-STATUS-MIB", "ogSerialPortStatusLabel"),
        ("OG-STATUS-MIB", "ogSerialPortActiveUsersPort"),
        ("OG-STATUS-MIB", "ogSerialPortActiveUsersName"),
        ("OG-STATUS-MIB", "ogSerialPortActiveUsersPortLabel"),
        ("OG-STATUS-MIB", "ogRpcStatusName"),
        ("OG-STATUS-MIB", "ogRpcStatusMaxTemp"),
        ("OG-STATUS-MIB", "ogRpcStatusAlertCount"),
        ("OG-STATUS-MIB", "ogEmdStatusName"),
        ("OG-STATUS-MIB", "ogEmdStatusTemp"),
        ("OG-STATUS-MIB", "ogEmdStatusHumidity"),
        ("OG-STATUS-MIB", "ogEmdStatusAlertCount"),
        ("OG-STATUS-MIB", "ogDioStatusName"),
        ("OG-STATUS-MIB", "ogDioStatusType"),
        ("OG-STATUS-MIB", "ogDioStatusDirection"),
        ("OG-STATUS-MIB", "ogDioStatusState"),
        ("OG-STATUS-MIB", "ogDioStatusCounter"),
        ("OG-STATUS-MIB", "ogDioStatusTriggerMode"))
)
if mibBuilder.loadTexts:
    ogBasicStatusGroup.setStatus("current")

ogBasicAlertStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25049, 16, 65535, 2, 2)
)
ogBasicAlertStatusGroup.setObjects(
      *(("OG-STATUS-MIB", "ogSignalAlertStatusPort"),
        ("OG-STATUS-MIB", "ogSignalAlertStatusLabel"),
        ("OG-STATUS-MIB", "ogSignalAlertStatusSignalName"),
        ("OG-STATUS-MIB", "ogSignalAlertStatusState"),
        ("OG-STATUS-MIB", "ogEnvAlertStatusDevice"),
        ("OG-STATUS-MIB", "ogEnvAlertStatusSensor"),
        ("OG-STATUS-MIB", "ogEnvAlertStatusOutlet"),
        ("OG-STATUS-MIB", "ogEnvAlertStatusValue"),
        ("OG-STATUS-MIB", "ogEnvAlertStatusOldValue"),
        ("OG-STATUS-MIB", "ogEnvAlertStatusStatus"),
        ("OG-STATUS-MIB", "ogNutAlertStatusPort"),
        ("OG-STATUS-MIB", "ogNutAlertStatusName"),
        ("OG-STATUS-MIB", "ogNutAlertStatusHost"),
        ("OG-STATUS-MIB", "ogNutAlertStatusStatus"),
        ("OG-STATUS-MIB", "ogDataAlertStatusBytes"),
        ("OG-STATUS-MIB", "ogDataAlertStatusSeconds"),
        ("OG-STATUS-MIB", "ogDataAlertStatusDevice"),
        ("OG-STATUS-MIB", "ogDataAlertStatusState"),
        ("OG-STATUS-MIB", "ogDioAlertStatusName"),
        ("OG-STATUS-MIB", "ogDioAlertStatusValue"),
        ("OG-STATUS-MIB", "ogDioAlertStatusOldValue"),
        ("OG-STATUS-MIB", "ogDioAlertStatusTriggered"))
)
if mibBuilder.loadTexts:
    ogBasicAlertStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ogStatusCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25049, 16, 65535, 1, 1)
)
if mibBuilder.loadTexts:
    ogStatusCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OG-STATUS-MIB",
    **{"ogStatus": ogStatus,
       "ogSerialPortStatusTable": ogSerialPortStatusTable,
       "ogSerialPortStatusEntry": ogSerialPortStatusEntry,
       "ogSerialPortStatusIndex": ogSerialPortStatusIndex,
       "ogSerialPortStatusPort": ogSerialPortStatusPort,
       "ogSerialPortStatusRxBytes": ogSerialPortStatusRxBytes,
       "ogSerialPortStatusTxBytes": ogSerialPortStatusTxBytes,
       "ogSerialPortStatusSpeed": ogSerialPortStatusSpeed,
       "ogSerialPortStatusDCD": ogSerialPortStatusDCD,
       "ogSerialPortStatusDTR": ogSerialPortStatusDTR,
       "ogSerialPortStatusDSR": ogSerialPortStatusDSR,
       "ogSerialPortStatusCTS": ogSerialPortStatusCTS,
       "ogSerialPortStatusRTS": ogSerialPortStatusRTS,
       "ogSerialPortStatusLabel": ogSerialPortStatusLabel,
       "ogSerialPortActiveUsersTable": ogSerialPortActiveUsersTable,
       "ogSerialPortActiveUsersEntry": ogSerialPortActiveUsersEntry,
       "ogSerialPortActiveUsersIndex": ogSerialPortActiveUsersIndex,
       "ogSerialPortActiveUsersPort": ogSerialPortActiveUsersPort,
       "ogSerialPortActiveUsersName": ogSerialPortActiveUsersName,
       "ogSerialPortActiveUsersPortLabel": ogSerialPortActiveUsersPortLabel,
       "ogRpcStatusTable": ogRpcStatusTable,
       "ogRpcStatusEntry": ogRpcStatusEntry,
       "ogRpcStatusIndex": ogRpcStatusIndex,
       "ogRpcStatusName": ogRpcStatusName,
       "ogRpcStatusMaxTemp": ogRpcStatusMaxTemp,
       "ogRpcStatusAlertCount": ogRpcStatusAlertCount,
       "ogEmdStatusTable": ogEmdStatusTable,
       "ogEmdStatusEntry": ogEmdStatusEntry,
       "ogEmdStatusIndex": ogEmdStatusIndex,
       "ogEmdStatusName": ogEmdStatusName,
       "ogEmdStatusTemp": ogEmdStatusTemp,
       "ogEmdStatusHumidity": ogEmdStatusHumidity,
       "ogEmdStatusAlertCount": ogEmdStatusAlertCount,
       "ogDioStatusTable": ogDioStatusTable,
       "ogDioStatusEntry": ogDioStatusEntry,
       "ogDioStatusIndex": ogDioStatusIndex,
       "ogDioStatusName": ogDioStatusName,
       "ogDioStatusType": ogDioStatusType,
       "ogDioStatusDirection": ogDioStatusDirection,
       "ogDioStatusState": ogDioStatusState,
       "ogDioStatusCounter": ogDioStatusCounter,
       "ogDioStatusTriggerMode": ogDioStatusTriggerMode,
       "ogSignalAlertStatusTable": ogSignalAlertStatusTable,
       "ogSignalAlertStatusEntry": ogSignalAlertStatusEntry,
       "ogSignalAlertStatusIndex": ogSignalAlertStatusIndex,
       "ogSignalAlertStatusPort": ogSignalAlertStatusPort,
       "ogSignalAlertStatusLabel": ogSignalAlertStatusLabel,
       "ogSignalAlertStatusSignalName": ogSignalAlertStatusSignalName,
       "ogSignalAlertStatusState": ogSignalAlertStatusState,
       "ogEnvAlertStatusTable": ogEnvAlertStatusTable,
       "ogEnvAlertStatusEntry": ogEnvAlertStatusEntry,
       "ogEnvAlertStatusIndex": ogEnvAlertStatusIndex,
       "ogEnvAlertStatusDevice": ogEnvAlertStatusDevice,
       "ogEnvAlertStatusSensor": ogEnvAlertStatusSensor,
       "ogEnvAlertStatusOutlet": ogEnvAlertStatusOutlet,
       "ogEnvAlertStatusValue": ogEnvAlertStatusValue,
       "ogEnvAlertStatusOldValue": ogEnvAlertStatusOldValue,
       "ogEnvAlertStatusStatus": ogEnvAlertStatusStatus,
       "ogNutAlertStatusTable": ogNutAlertStatusTable,
       "ogNutAlertStatusEntry": ogNutAlertStatusEntry,
       "ogNutAlertStatusIndex": ogNutAlertStatusIndex,
       "ogNutAlertStatusPort": ogNutAlertStatusPort,
       "ogNutAlertStatusName": ogNutAlertStatusName,
       "ogNutAlertStatusHost": ogNutAlertStatusHost,
       "ogNutAlertStatusStatus": ogNutAlertStatusStatus,
       "ogDataAlertStatusTable": ogDataAlertStatusTable,
       "ogDataAlertStatusEntry": ogDataAlertStatusEntry,
       "ogDataAlertStatusIndex": ogDataAlertStatusIndex,
       "ogDataAlertStatusBytes": ogDataAlertStatusBytes,
       "ogDataAlertStatusSeconds": ogDataAlertStatusSeconds,
       "ogDataAlertStatusDevice": ogDataAlertStatusDevice,
       "ogDataAlertStatusState": ogDataAlertStatusState,
       "ogDioAlertStatusTable": ogDioAlertStatusTable,
       "ogDioAlertStatusEntry": ogDioAlertStatusEntry,
       "ogDioAlertStatusIndex": ogDioAlertStatusIndex,
       "ogDioAlertStatusName": ogDioAlertStatusName,
       "ogDioAlertStatusValue": ogDioAlertStatusValue,
       "ogDioAlertStatusOldValue": ogDioAlertStatusOldValue,
       "ogDioAlertStatusTriggered": ogDioAlertStatusTriggered,
       "ogStatusConformance": ogStatusConformance,
       "ogStatusCompliances": ogStatusCompliances,
       "ogStatusCompliance": ogStatusCompliance,
       "ogStatusGroups": ogStatusGroups,
       "ogBasicStatusGroup": ogBasicStatusGroup,
       "ogBasicAlertStatusGroup": ogBasicAlertStatusGroup}
)
