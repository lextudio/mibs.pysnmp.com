# SNMP MIB module (VERTICAL-ENV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VERTICAL-ENV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:20 2024
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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Vertical_ObjectIdentity = ObjectIdentity
vertical = _Vertical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338)
)
_Environment_ObjectIdentity = ObjectIdentity
environment = _Environment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 11)
)
_IOFanTable_Object = MibTable
iOFanTable = _IOFanTable_Object(
    (1, 3, 6, 1, 4, 1, 2338, 11, 1)
)
if mibBuilder.loadTexts:
    iOFanTable.setStatus("current")
_IOFanEntry_Object = MibTableRow
iOFanEntry = _IOFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2338, 11, 1, 1)
)
iOFanEntry.setIndexNames(
    (0, "VERTICAL-ENV-MIB", "fanIndex"),
)
if mibBuilder.loadTexts:
    iOFanEntry.setStatus("mandatory")
_FanIndex_Type = Integer32
_FanIndex_Object = MibTableColumn
fanIndex = _FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2338, 11, 1, 1, 1),
    _FanIndex_Type()
)
fanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanIndex.setStatus("mandatory")


class _FanOperStatus_Type(Integer32):
    """Custom type fanOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("stopped", 2),
          ("unknown", 3))
    )


_FanOperStatus_Type.__name__ = "Integer32"
_FanOperStatus_Object = MibTableColumn
fanOperStatus = _FanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2338, 11, 1, 1, 2),
    _FanOperStatus_Type()
)
fanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanOperStatus.setStatus("mandatory")
_IOPSTable_Object = MibTable
iOPSTable = _IOPSTable_Object(
    (1, 3, 6, 1, 4, 1, 2338, 11, 2)
)
if mibBuilder.loadTexts:
    iOPSTable.setStatus("current")
_IOPSEntry_Object = MibTableRow
iOPSEntry = _IOPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2338, 11, 2, 1)
)
iOPSEntry.setIndexNames(
    (0, "VERTICAL-ENV-MIB", "psIndex"),
)
if mibBuilder.loadTexts:
    iOPSEntry.setStatus("mandatory")
_PsIndex_Type = Integer32
_PsIndex_Object = MibTableColumn
psIndex = _PsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2338, 11, 2, 1, 1),
    _PsIndex_Type()
)
psIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psIndex.setStatus("mandatory")


class _PsOperStatus_Type(Integer32):
    """Custom type psOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1),
          ("unknown", 3))
    )


_PsOperStatus_Type.__name__ = "Integer32"
_PsOperStatus_Object = MibTableColumn
psOperStatus = _PsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2338, 11, 2, 1, 2),
    _PsOperStatus_Type()
)
psOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psOperStatus.setStatus("mandatory")
_IOFaultMonitorGroup_ObjectIdentity = ObjectIdentity
iOFaultMonitorGroup = _IOFaultMonitorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 11, 3)
)


class _IOFaultMonitorStatus_Type(Integer32):
    """Custom type iOFaultMonitorStatus based on Integer32"""
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
        *(("modemFailed", 4),
          ("notResponding", 2),
          ("ok", 3),
          ("rAMFull", 1))
    )


_IOFaultMonitorStatus_Type.__name__ = "Integer32"
_IOFaultMonitorStatus_Object = MibScalar
iOFaultMonitorStatus = _IOFaultMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 2338, 11, 3, 1),
    _IOFaultMonitorStatus_Type()
)
iOFaultMonitorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iOFaultMonitorStatus.setStatus("mandatory")
_IOTrapInfoGroup_ObjectIdentity = ObjectIdentity
iOTrapInfoGroup = _IOTrapInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 11, 4)
)


class _IOLastFanTrap_Type(DisplayString):
    """Custom type iOLastFanTrap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IOLastFanTrap_Type.__name__ = "DisplayString"
_IOLastFanTrap_Object = MibScalar
iOLastFanTrap = _IOLastFanTrap_Object(
    (1, 3, 6, 1, 4, 1, 2338, 11, 4, 1),
    _IOLastFanTrap_Type()
)
iOLastFanTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iOLastFanTrap.setStatus("mandatory")


class _IOLastPowerSupplyTrap_Type(DisplayString):
    """Custom type iOLastPowerSupplyTrap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IOLastPowerSupplyTrap_Type.__name__ = "DisplayString"
_IOLastPowerSupplyTrap_Object = MibScalar
iOLastPowerSupplyTrap = _IOLastPowerSupplyTrap_Object(
    (1, 3, 6, 1, 4, 1, 2338, 11, 4, 2),
    _IOLastPowerSupplyTrap_Type()
)
iOLastPowerSupplyTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iOLastPowerSupplyTrap.setStatus("mandatory")


class _IOLastFaultMonitorTrap_Type(DisplayString):
    """Custom type iOLastFaultMonitorTrap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IOLastFaultMonitorTrap_Type.__name__ = "DisplayString"
_IOLastFaultMonitorTrap_Object = MibScalar
iOLastFaultMonitorTrap = _IOLastFaultMonitorTrap_Object(
    (1, 3, 6, 1, 4, 1, 2338, 11, 4, 3),
    _IOLastFaultMonitorTrap_Type()
)
iOLastFaultMonitorTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iOLastFaultMonitorTrap.setStatus("mandatory")

# Managed Objects groups


# Notification objects

iOFanStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 47)
)
iOFanStatus.setObjects(
    ("VERTICAL-ENV-MIB", "iOLastFanTrap")
)
if mibBuilder.loadTexts:
    iOFanStatus.setStatus(
        ""
    )

iOPowerSupplyStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 48)
)
iOPowerSupplyStatus.setObjects(
    ("VERTICAL-ENV-MIB", "iOLastPowerSupplyTrap")
)
if mibBuilder.loadTexts:
    iOPowerSupplyStatus.setStatus(
        ""
    )

iOFaultMonitorStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 49)
)
iOFaultMonitorStatusTrap.setObjects(
    ("VERTICAL-ENV-MIB", "iOLastFaultMonitorTrap")
)
if mibBuilder.loadTexts:
    iOFaultMonitorStatusTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VERTICAL-ENV-MIB",
    **{"vertical": vertical,
       "iOFanStatus": iOFanStatus,
       "iOPowerSupplyStatus": iOPowerSupplyStatus,
       "iOFaultMonitorStatusTrap": iOFaultMonitorStatusTrap,
       "environment": environment,
       "iOFanTable": iOFanTable,
       "iOFanEntry": iOFanEntry,
       "fanIndex": fanIndex,
       "fanOperStatus": fanOperStatus,
       "iOPSTable": iOPSTable,
       "iOPSEntry": iOPSEntry,
       "psIndex": psIndex,
       "psOperStatus": psOperStatus,
       "iOFaultMonitorGroup": iOFaultMonitorGroup,
       "iOFaultMonitorStatus": iOFaultMonitorStatus,
       "iOTrapInfoGroup": iOTrapInfoGroup,
       "iOLastFanTrap": iOLastFanTrap,
       "iOLastPowerSupplyTrap": iOLastPowerSupplyTrap,
       "iOLastFaultMonitorTrap": iOLastFaultMonitorTrap}
)
