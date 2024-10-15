# SNMP MIB module (CYCLADES-ACS-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYCLADES-ACS-PM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:25 2024
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

(cyACSMgmt,) = mibBuilder.importSymbols(
    "CYCLADES-ACS-MIB",
    "cyACSMgmt")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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

cyPM = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5)
)
cyPM.setRevisions(
        ("2005-08-29 00:00",
         "2003-10-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyNumberOfPM_Type = Integer32
_CyNumberOfPM_Object = MibScalar
cyNumberOfPM = _CyNumberOfPM_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5, 1),
    _CyNumberOfPM_Type()
)
cyNumberOfPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyNumberOfPM.setStatus("current")
_CyPMTable_Object = MibTable
cyPMTable = _CyPMTable_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5, 2)
)
if mibBuilder.loadTexts:
    cyPMTable.setStatus("current")
_CyPMEntry_Object = MibTableRow
cyPMEntry = _CyPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5, 2, 1)
)
cyPMEntry.setIndexNames(
    (0, "CYCLADES-ACS-PM-MIB", "cyPMSerialPortNumber"),
)
if mibBuilder.loadTexts:
    cyPMEntry.setStatus("current")
_CyPMSerialPortNumber_Type = InterfaceIndex
_CyPMSerialPortNumber_Object = MibTableColumn
cyPMSerialPortNumber = _CyPMSerialPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5, 2, 1, 1),
    _CyPMSerialPortNumber_Type()
)
cyPMSerialPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMSerialPortNumber.setStatus("current")
_CyPMNumberOutlets_Type = Integer32
_CyPMNumberOutlets_Object = MibTableColumn
cyPMNumberOutlets = _CyPMNumberOutlets_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5, 2, 1, 2),
    _CyPMNumberOutlets_Type()
)
cyPMNumberOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMNumberOutlets.setStatus("current")
_CyPMNumberUnits_Type = Integer32
_CyPMNumberUnits_Object = MibTableColumn
cyPMNumberUnits = _CyPMNumberUnits_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5, 2, 1, 3),
    _CyPMNumberUnits_Type()
)
cyPMNumberUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMNumberUnits.setStatus("current")
_CyPMCurrent_Type = DisplayString
_CyPMCurrent_Object = MibTableColumn
cyPMCurrent = _CyPMCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5, 2, 1, 4),
    _CyPMCurrent_Type()
)
cyPMCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMCurrent.setStatus("current")
_CyPMVersion_Type = DisplayString
_CyPMVersion_Object = MibTableColumn
cyPMVersion = _CyPMVersion_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5, 2, 1, 5),
    _CyPMVersion_Type()
)
cyPMVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMVersion.setStatus("current")
_CyPMTemperature_Type = DisplayString
_CyPMTemperature_Object = MibTableColumn
cyPMTemperature = _CyPMTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5, 2, 1, 6),
    _CyPMTemperature_Type()
)
cyPMTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMTemperature.setStatus("current")


class _CyPMCommand_Type(DisplayString):
    """Custom type cyPMCommand based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CyPMCommand_Type.__name__ = "DisplayString"
_CyPMCommand_Object = MibTableColumn
cyPMCommand = _CyPMCommand_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5, 2, 1, 7),
    _CyPMCommand_Type()
)
cyPMCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyPMCommand.setStatus("current")
_CyPMUnitTable_Object = MibTable
cyPMUnitTable = _CyPMUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5, 3)
)
if mibBuilder.loadTexts:
    cyPMUnitTable.setStatus("current")
_CyPMUnitEntry_Object = MibTableRow
cyPMUnitEntry = _CyPMUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5, 3, 1)
)
cyPMUnitEntry.setIndexNames(
    (0, "CYCLADES-ACS-PM-MIB", "cyPMSerialPortNumber"),
    (0, "CYCLADES-ACS-PM-MIB", "cyPMUnitNumber"),
)
if mibBuilder.loadTexts:
    cyPMUnitEntry.setStatus("current")
_CyPMUnitNumber_Type = InterfaceIndex
_CyPMUnitNumber_Object = MibTableColumn
cyPMUnitNumber = _CyPMUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5, 3, 1, 1),
    _CyPMUnitNumber_Type()
)
cyPMUnitNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyPMUnitNumber.setStatus("current")
_CyPMUnitVersion_Type = DisplayString
_CyPMUnitVersion_Object = MibTableColumn
cyPMUnitVersion = _CyPMUnitVersion_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5, 3, 1, 2),
    _CyPMUnitVersion_Type()
)
cyPMUnitVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMUnitVersion.setStatus("current")
_CyPMUnitOutlets_Type = Integer32
_CyPMUnitOutlets_Object = MibTableColumn
cyPMUnitOutlets = _CyPMUnitOutlets_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5, 3, 1, 3),
    _CyPMUnitOutlets_Type()
)
cyPMUnitOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMUnitOutlets.setStatus("current")
_CyPMUnitFirstOutlet_Type = Integer32
_CyPMUnitFirstOutlet_Object = MibTableColumn
cyPMUnitFirstOutlet = _CyPMUnitFirstOutlet_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5, 3, 1, 4),
    _CyPMUnitFirstOutlet_Type()
)
cyPMUnitFirstOutlet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMUnitFirstOutlet.setStatus("current")
_CyPMUnitCurrent_Type = Integer32
_CyPMUnitCurrent_Object = MibTableColumn
cyPMUnitCurrent = _CyPMUnitCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5, 3, 1, 5),
    _CyPMUnitCurrent_Type()
)
cyPMUnitCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMUnitCurrent.setStatus("current")
_CyPMUnitMaxCurrent_Type = Integer32
_CyPMUnitMaxCurrent_Object = MibTableColumn
cyPMUnitMaxCurrent = _CyPMUnitMaxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5, 3, 1, 6),
    _CyPMUnitMaxCurrent_Type()
)
cyPMUnitMaxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMUnitMaxCurrent.setStatus("current")
_CyPMUnitTemperature_Type = Integer32
_CyPMUnitTemperature_Object = MibTableColumn
cyPMUnitTemperature = _CyPMUnitTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5, 3, 1, 7),
    _CyPMUnitTemperature_Type()
)
cyPMUnitTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMUnitTemperature.setStatus("current")
_CyPMUnitMaxTemperature_Type = Integer32
_CyPMUnitMaxTemperature_Object = MibTableColumn
cyPMUnitMaxTemperature = _CyPMUnitMaxTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5, 3, 1, 8),
    _CyPMUnitMaxTemperature_Type()
)
cyPMUnitMaxTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyPMUnitMaxTemperature.setStatus("current")
_CyOutletTable_Object = MibTable
cyOutletTable = _CyOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5, 4)
)
if mibBuilder.loadTexts:
    cyOutletTable.setStatus("current")
_CyOutletEntry_Object = MibTableRow
cyOutletEntry = _CyOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5, 4, 1)
)
cyOutletEntry.setIndexNames(
    (0, "CYCLADES-ACS-PM-MIB", "cyPMSerialPortNumber"),
    (0, "CYCLADES-ACS-PM-MIB", "cyOutletNumber"),
)
if mibBuilder.loadTexts:
    cyOutletEntry.setStatus("current")
_CyOutletNumber_Type = InterfaceIndexOrZero
_CyOutletNumber_Object = MibTableColumn
cyOutletNumber = _CyOutletNumber_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5, 4, 1, 1),
    _CyOutletNumber_Type()
)
cyOutletNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyOutletNumber.setStatus("current")


class _CyOutletName_Type(DisplayString):
    """Custom type cyOutletName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_CyOutletName_Type.__name__ = "DisplayString"
_CyOutletName_Object = MibTableColumn
cyOutletName = _CyOutletName_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5, 4, 1, 2),
    _CyOutletName_Type()
)
cyOutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyOutletName.setStatus("current")
_CyOutletServer_Type = DisplayString
_CyOutletServer_Object = MibTableColumn
cyOutletServer = _CyOutletServer_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5, 4, 1, 3),
    _CyOutletServer_Type()
)
cyOutletServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyOutletServer.setStatus("current")


class _CyOutletPower_Type(Integer32):
    """Custom type cyOutletPower based on Integer32"""
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
        *(("cycle", 2),
          ("off", 0),
          ("on", 1),
          ("unknow", 3))
    )


_CyOutletPower_Type.__name__ = "Integer32"
_CyOutletPower_Object = MibTableColumn
cyOutletPower = _CyOutletPower_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5, 4, 1, 4),
    _CyOutletPower_Type()
)
cyOutletPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyOutletPower.setStatus("current")


class _CyOutletLock_Type(Integer32):
    """Custom type cyOutletLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lock", 1),
          ("unknow", 2),
          ("unlock", 0))
    )


_CyOutletLock_Type.__name__ = "Integer32"
_CyOutletLock_Object = MibTableColumn
cyOutletLock = _CyOutletLock_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5, 4, 1, 5),
    _CyOutletLock_Type()
)
cyOutletLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyOutletLock.setStatus("current")
_CyOutletPUInterval_Type = Integer32
_CyOutletPUInterval_Object = MibTableColumn
cyOutletPUInterval = _CyOutletPUInterval_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 5, 4, 1, 6),
    _CyOutletPUInterval_Type()
)
cyOutletPUInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyOutletPUInterval.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYCLADES-ACS-PM-MIB",
    **{"cyPM": cyPM,
       "cyNumberOfPM": cyNumberOfPM,
       "cyPMTable": cyPMTable,
       "cyPMEntry": cyPMEntry,
       "cyPMSerialPortNumber": cyPMSerialPortNumber,
       "cyPMNumberOutlets": cyPMNumberOutlets,
       "cyPMNumberUnits": cyPMNumberUnits,
       "cyPMCurrent": cyPMCurrent,
       "cyPMVersion": cyPMVersion,
       "cyPMTemperature": cyPMTemperature,
       "cyPMCommand": cyPMCommand,
       "cyPMUnitTable": cyPMUnitTable,
       "cyPMUnitEntry": cyPMUnitEntry,
       "cyPMUnitNumber": cyPMUnitNumber,
       "cyPMUnitVersion": cyPMUnitVersion,
       "cyPMUnitOutlets": cyPMUnitOutlets,
       "cyPMUnitFirstOutlet": cyPMUnitFirstOutlet,
       "cyPMUnitCurrent": cyPMUnitCurrent,
       "cyPMUnitMaxCurrent": cyPMUnitMaxCurrent,
       "cyPMUnitTemperature": cyPMUnitTemperature,
       "cyPMUnitMaxTemperature": cyPMUnitMaxTemperature,
       "cyOutletTable": cyOutletTable,
       "cyOutletEntry": cyOutletEntry,
       "cyOutletNumber": cyOutletNumber,
       "cyOutletName": cyOutletName,
       "cyOutletServer": cyOutletServer,
       "cyOutletPower": cyOutletPower,
       "cyOutletLock": cyOutletLock,
       "cyOutletPUInterval": cyOutletPUInterval}
)
