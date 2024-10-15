# SNMP MIB module (JUNIPER-RPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-RPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:07 2024
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

(jnxRPS,) = mibBuilder.importSymbols(
    "JUNIPER-EX-SMI",
    "jnxRPS")

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

jnxRPSMIBObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1)
)
jnxRPSMIBObjects.setRevisions(
        ("2009-08-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxRPSStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("amber", 2),
          ("amber-blink", 5),
          ("green", 0),
          ("green-blink", 3),
          ("off", 6),
          ("red", 1),
          ("red-blink", 4))
    )



# MIB Managed Objects in the order of their OIDs

_JnxRPSVersionTable_Object = MibTable
jnxRPSVersionTable = _JnxRPSVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    jnxRPSVersionTable.setStatus("current")
_JnxRPSVersionEntry_Object = MibTableRow
jnxRPSVersionEntry = _JnxRPSVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 1, 1)
)
jnxRPSVersionEntry.setIndexNames(
    (0, "JUNIPER-RPS-MIB", "jnxRPSSerialNumber"),
)
if mibBuilder.loadTexts:
    jnxRPSVersionEntry.setStatus("current")


class _JnxRPSSerialNumber_Type(DisplayString):
    """Custom type jnxRPSSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_JnxRPSSerialNumber_Type.__name__ = "DisplayString"
_JnxRPSSerialNumber_Object = MibTableColumn
jnxRPSSerialNumber = _JnxRPSSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 1, 1, 1),
    _JnxRPSSerialNumber_Type()
)
jnxRPSSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxRPSSerialNumber.setStatus("current")


class _JnxRPSModel_Type(DisplayString):
    """Custom type jnxRPSModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxRPSModel_Type.__name__ = "DisplayString"
_JnxRPSModel_Object = MibTableColumn
jnxRPSModel = _JnxRPSModel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 1, 1, 2),
    _JnxRPSModel_Type()
)
jnxRPSModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRPSModel.setStatus("current")


class _JnxRPSFirmwareVersion_Type(DisplayString):
    """Custom type jnxRPSFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_JnxRPSFirmwareVersion_Type.__name__ = "DisplayString"
_JnxRPSFirmwareVersion_Object = MibTableColumn
jnxRPSFirmwareVersion = _JnxRPSFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 1, 1, 3),
    _JnxRPSFirmwareVersion_Type()
)
jnxRPSFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRPSFirmwareVersion.setStatus("current")


class _JnxRPSUBootVersion_Type(DisplayString):
    """Custom type jnxRPSUBootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_JnxRPSUBootVersion_Type.__name__ = "DisplayString"
_JnxRPSUBootVersion_Object = MibTableColumn
jnxRPSUBootVersion = _JnxRPSUBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 1, 1, 4),
    _JnxRPSUBootVersion_Type()
)
jnxRPSUBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRPSUBootVersion.setStatus("current")
_JnxRPSStatusTable_Object = MibTable
jnxRPSStatusTable = _JnxRPSStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    jnxRPSStatusTable.setStatus("current")
_JnxRPSStatusEntry_Object = MibTableRow
jnxRPSStatusEntry = _JnxRPSStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 2, 1)
)
jnxRPSStatusEntry.setIndexNames(
    (0, "JUNIPER-RPS-MIB", "jnxRPSSerialNumber"),
)
if mibBuilder.loadTexts:
    jnxRPSStatusEntry.setStatus("current")
_JnxRPSFanStatus_Type = JnxRPSStatus
_JnxRPSFanStatus_Object = MibTableColumn
jnxRPSFanStatus = _JnxRPSFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 2, 1, 1),
    _JnxRPSFanStatus_Type()
)
jnxRPSFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRPSFanStatus.setStatus("current")
_JnxRPSSystemStatus_Type = JnxRPSStatus
_JnxRPSSystemStatus_Object = MibTableColumn
jnxRPSSystemStatus = _JnxRPSSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 2, 1, 2),
    _JnxRPSSystemStatus_Type()
)
jnxRPSSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRPSSystemStatus.setStatus("current")
_JnxRPSPowerSupplyTable_Object = MibTable
jnxRPSPowerSupplyTable = _JnxRPSPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 3)
)
if mibBuilder.loadTexts:
    jnxRPSPowerSupplyTable.setStatus("current")
_JnxRPSPowerSupplyEntry_Object = MibTableRow
jnxRPSPowerSupplyEntry = _JnxRPSPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 3, 1)
)
jnxRPSPowerSupplyEntry.setIndexNames(
    (0, "JUNIPER-RPS-MIB", "jnxRPSSerialNumber"),
    (0, "JUNIPER-RPS-MIB", "jnxRPSPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    jnxRPSPowerSupplyEntry.setStatus("current")


class _JnxRPSPowerSupplyIndex_Type(Integer32):
    """Custom type jnxRPSPowerSupplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_JnxRPSPowerSupplyIndex_Type.__name__ = "Integer32"
_JnxRPSPowerSupplyIndex_Object = MibTableColumn
jnxRPSPowerSupplyIndex = _JnxRPSPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 3, 1, 1),
    _JnxRPSPowerSupplyIndex_Type()
)
jnxRPSPowerSupplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxRPSPowerSupplyIndex.setStatus("current")


class _JnxRPSPowerSupplySlotId_Type(Integer32):
    """Custom type jnxRPSPowerSupplySlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_JnxRPSPowerSupplySlotId_Type.__name__ = "Integer32"
_JnxRPSPowerSupplySlotId_Object = MibTableColumn
jnxRPSPowerSupplySlotId = _JnxRPSPowerSupplySlotId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 3, 1, 2),
    _JnxRPSPowerSupplySlotId_Type()
)
jnxRPSPowerSupplySlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRPSPowerSupplySlotId.setStatus("current")


class _JnxRPSPowerSupplyStatus_Type(DisplayString):
    """Custom type jnxRPSPowerSupplyStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JnxRPSPowerSupplyStatus_Type.__name__ = "DisplayString"
_JnxRPSPowerSupplyStatus_Object = MibTableColumn
jnxRPSPowerSupplyStatus = _JnxRPSPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 3, 1, 3),
    _JnxRPSPowerSupplyStatus_Type()
)
jnxRPSPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRPSPowerSupplyStatus.setStatus("current")


class _JnxRPSPowerSupplyDescription_Type(DisplayString):
    """Custom type jnxRPSPowerSupplyDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JnxRPSPowerSupplyDescription_Type.__name__ = "DisplayString"
_JnxRPSPowerSupplyDescription_Object = MibTableColumn
jnxRPSPowerSupplyDescription = _JnxRPSPowerSupplyDescription_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 3, 1, 4),
    _JnxRPSPowerSupplyDescription_Type()
)
jnxRPSPowerSupplyDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRPSPowerSupplyDescription.setStatus("current")
_JnxRPSLedPortStatusTable_Object = MibTable
jnxRPSLedPortStatusTable = _JnxRPSLedPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 4)
)
if mibBuilder.loadTexts:
    jnxRPSLedPortStatusTable.setStatus("current")
_JnxRPSLedPortStatusEntry_Object = MibTableRow
jnxRPSLedPortStatusEntry = _JnxRPSLedPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 4, 1)
)
jnxRPSLedPortStatusEntry.setIndexNames(
    (0, "JUNIPER-RPS-MIB", "jnxRPSSerialNumber"),
    (0, "JUNIPER-RPS-MIB", "jnxRPSLedPortIndex"),
)
if mibBuilder.loadTexts:
    jnxRPSLedPortStatusEntry.setStatus("current")


class _JnxRPSLedPortIndex_Type(Integer32):
    """Custom type jnxRPSLedPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_JnxRPSLedPortIndex_Type.__name__ = "Integer32"
_JnxRPSLedPortIndex_Object = MibTableColumn
jnxRPSLedPortIndex = _JnxRPSLedPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 4, 1, 1),
    _JnxRPSLedPortIndex_Type()
)
jnxRPSLedPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxRPSLedPortIndex.setStatus("current")


class _JnxRPSLedPortStatus_Type(DisplayString):
    """Custom type jnxRPSLedPortStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JnxRPSLedPortStatus_Type.__name__ = "DisplayString"
_JnxRPSLedPortStatus_Object = MibTableColumn
jnxRPSLedPortStatus = _JnxRPSLedPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 4, 1, 2),
    _JnxRPSLedPortStatus_Type()
)
jnxRPSLedPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRPSLedPortStatus.setStatus("current")
_JnxRPSPortStatusTable_Object = MibTable
jnxRPSPortStatusTable = _JnxRPSPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 5)
)
if mibBuilder.loadTexts:
    jnxRPSPortStatusTable.setStatus("current")
_JnxRPSPortStatusEntry_Object = MibTableRow
jnxRPSPortStatusEntry = _JnxRPSPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 5, 1)
)
jnxRPSPortStatusEntry.setIndexNames(
    (0, "JUNIPER-RPS-MIB", "jnxRPSSerialNumber"),
    (0, "JUNIPER-RPS-MIB", "jnxRPSPortIndex"),
)
if mibBuilder.loadTexts:
    jnxRPSPortStatusEntry.setStatus("current")


class _JnxRPSPortIndex_Type(Integer32):
    """Custom type jnxRPSPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_JnxRPSPortIndex_Type.__name__ = "Integer32"
_JnxRPSPortIndex_Object = MibTableColumn
jnxRPSPortIndex = _JnxRPSPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 5, 1, 1),
    _JnxRPSPortIndex_Type()
)
jnxRPSPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxRPSPortIndex.setStatus("current")
_JnxRPSPortId_Type = Integer32
_JnxRPSPortId_Object = MibTableColumn
jnxRPSPortId = _JnxRPSPortId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 5, 1, 2),
    _JnxRPSPortId_Type()
)
jnxRPSPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRPSPortId.setStatus("current")
_JnxRPSPortStatus_Type = Integer32
_JnxRPSPortStatus_Object = MibTableColumn
jnxRPSPortStatus = _JnxRPSPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 5, 1, 3),
    _JnxRPSPortStatus_Type()
)
jnxRPSPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRPSPortStatus.setStatus("current")
_JnxRPSPortPriority_Type = Integer32
_JnxRPSPortPriority_Object = MibTableColumn
jnxRPSPortPriority = _JnxRPSPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 5, 1, 4),
    _JnxRPSPortPriority_Type()
)
jnxRPSPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRPSPortPriority.setStatus("current")


class _JnxRPSPortPowerRequested_Type(DisplayString):
    """Custom type jnxRPSPortPowerRequested based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JnxRPSPortPowerRequested_Type.__name__ = "DisplayString"
_JnxRPSPortPowerRequested_Object = MibTableColumn
jnxRPSPortPowerRequested = _JnxRPSPortPowerRequested_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 5, 1, 5),
    _JnxRPSPortPowerRequested_Type()
)
jnxRPSPortPowerRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRPSPortPowerRequested.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-RPS-MIB",
    **{"JnxRPSStatus": JnxRPSStatus,
       "jnxRPSMIBObjects": jnxRPSMIBObjects,
       "jnxRPSVersionTable": jnxRPSVersionTable,
       "jnxRPSVersionEntry": jnxRPSVersionEntry,
       "jnxRPSSerialNumber": jnxRPSSerialNumber,
       "jnxRPSModel": jnxRPSModel,
       "jnxRPSFirmwareVersion": jnxRPSFirmwareVersion,
       "jnxRPSUBootVersion": jnxRPSUBootVersion,
       "jnxRPSStatusTable": jnxRPSStatusTable,
       "jnxRPSStatusEntry": jnxRPSStatusEntry,
       "jnxRPSFanStatus": jnxRPSFanStatus,
       "jnxRPSSystemStatus": jnxRPSSystemStatus,
       "jnxRPSPowerSupplyTable": jnxRPSPowerSupplyTable,
       "jnxRPSPowerSupplyEntry": jnxRPSPowerSupplyEntry,
       "jnxRPSPowerSupplyIndex": jnxRPSPowerSupplyIndex,
       "jnxRPSPowerSupplySlotId": jnxRPSPowerSupplySlotId,
       "jnxRPSPowerSupplyStatus": jnxRPSPowerSupplyStatus,
       "jnxRPSPowerSupplyDescription": jnxRPSPowerSupplyDescription,
       "jnxRPSLedPortStatusTable": jnxRPSLedPortStatusTable,
       "jnxRPSLedPortStatusEntry": jnxRPSLedPortStatusEntry,
       "jnxRPSLedPortIndex": jnxRPSLedPortIndex,
       "jnxRPSLedPortStatus": jnxRPSLedPortStatus,
       "jnxRPSPortStatusTable": jnxRPSPortStatusTable,
       "jnxRPSPortStatusEntry": jnxRPSPortStatusEntry,
       "jnxRPSPortIndex": jnxRPSPortIndex,
       "jnxRPSPortId": jnxRPSPortId,
       "jnxRPSPortStatus": jnxRPSPortStatus,
       "jnxRPSPortPriority": jnxRPSPortPriority,
       "jnxRPSPortPowerRequested": jnxRPSPortPowerRequested}
)
