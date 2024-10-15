# SNMP MIB module (BDCOM-PROCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BDCOM-PROCESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:36 2024
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

(bdMgmt,) = mibBuilder.importSymbols(
    "BDCOM-SMI",
    "bdMgmt")

(EntPhysicalIndexOrZero,) = mibBuilder.importSymbols(
    "BDCOM-TC",
    "EntPhysicalIndexOrZero")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

bdcomProcessMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109)
)
bdcomProcessMIB.setRevisions(
        ("2003-10-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BdcomProcessMIBObjects_ObjectIdentity = ObjectIdentity
bdcomProcessMIBObjects = _BdcomProcessMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1)
)
_BdpmCPU_ObjectIdentity = ObjectIdentity
bdpmCPU = _BdpmCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 1)
)
_BdpmCPUTotalTable_Object = MibTable
bdpmCPUTotalTable = _BdpmCPUTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 1, 1)
)
if mibBuilder.loadTexts:
    bdpmCPUTotalTable.setStatus("current")
_BdpmCPUTotalEntry_Object = MibTableRow
bdpmCPUTotalEntry = _BdpmCPUTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 1, 1, 1)
)
bdpmCPUTotalEntry.setIndexNames(
    (0, "BDCOM-PROCESS-MIB", "bdpmCPUTotalIndex"),
)
if mibBuilder.loadTexts:
    bdpmCPUTotalEntry.setStatus("current")


class _BdpmCPUTotalIndex_Type(Unsigned32):
    """Custom type bdpmCPUTotalIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_BdpmCPUTotalIndex_Type.__name__ = "Unsigned32"
_BdpmCPUTotalIndex_Object = MibTableColumn
bdpmCPUTotalIndex = _BdpmCPUTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 1, 1, 1, 1),
    _BdpmCPUTotalIndex_Type()
)
bdpmCPUTotalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bdpmCPUTotalIndex.setStatus("current")
_BdpmCPUTotalPhysicalIndex_Type = EntPhysicalIndexOrZero
_BdpmCPUTotalPhysicalIndex_Object = MibTableColumn
bdpmCPUTotalPhysicalIndex = _BdpmCPUTotalPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 1, 1, 1, 2),
    _BdpmCPUTotalPhysicalIndex_Type()
)
bdpmCPUTotalPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdpmCPUTotalPhysicalIndex.setStatus("current")


class _BdpmCPUTotal5sec_Type(Gauge32):
    """Custom type bdpmCPUTotal5sec based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_BdpmCPUTotal5sec_Type.__name__ = "Gauge32"
_BdpmCPUTotal5sec_Object = MibTableColumn
bdpmCPUTotal5sec = _BdpmCPUTotal5sec_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 1, 1, 1, 3),
    _BdpmCPUTotal5sec_Type()
)
bdpmCPUTotal5sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdpmCPUTotal5sec.setStatus("current")
if mibBuilder.loadTexts:
    bdpmCPUTotal5sec.setUnits("percent")


class _BdpmCPUTotal1min_Type(Gauge32):
    """Custom type bdpmCPUTotal1min based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_BdpmCPUTotal1min_Type.__name__ = "Gauge32"
_BdpmCPUTotal1min_Object = MibTableColumn
bdpmCPUTotal1min = _BdpmCPUTotal1min_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 1, 1, 1, 4),
    _BdpmCPUTotal1min_Type()
)
bdpmCPUTotal1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdpmCPUTotal1min.setStatus("current")
if mibBuilder.loadTexts:
    bdpmCPUTotal1min.setUnits("percent")


class _BdpmCPUTotal5min_Type(Gauge32):
    """Custom type bdpmCPUTotal5min based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_BdpmCPUTotal5min_Type.__name__ = "Gauge32"
_BdpmCPUTotal5min_Object = MibTableColumn
bdpmCPUTotal5min = _BdpmCPUTotal5min_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 1, 1, 1, 5),
    _BdpmCPUTotal5min_Type()
)
bdpmCPUTotal5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdpmCPUTotal5min.setStatus("current")
if mibBuilder.loadTexts:
    bdpmCPUTotal5min.setUnits("percent")
_BdpmProcess_ObjectIdentity = ObjectIdentity
bdpmProcess = _BdpmProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 2)
)
_BdpmProcessTable_Object = MibTable
bdpmProcessTable = _BdpmProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 2, 1)
)
if mibBuilder.loadTexts:
    bdpmProcessTable.setStatus("current")
_BdpmProcessEntry_Object = MibTableRow
bdpmProcessEntry = _BdpmProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 2, 1, 1)
)
bdpmProcessEntry.setIndexNames(
    (0, "BDCOM-PROCESS-MIB", "bdpmCPUTotalIndex"),
    (0, "BDCOM-PROCESS-MIB", "bdpmProcessPID"),
)
if mibBuilder.loadTexts:
    bdpmProcessEntry.setStatus("current")
_BdpmProcessPID_Type = Unsigned32
_BdpmProcessPID_Object = MibTableColumn
bdpmProcessPID = _BdpmProcessPID_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 2, 1, 1, 1),
    _BdpmProcessPID_Type()
)
bdpmProcessPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdpmProcessPID.setStatus("current")


class _BdpmProcessName_Type(DisplayString):
    """Custom type bdpmProcessName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BdpmProcessName_Type.__name__ = "DisplayString"
_BdpmProcessName_Object = MibTableColumn
bdpmProcessName = _BdpmProcessName_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 2, 1, 1, 2),
    _BdpmProcessName_Type()
)
bdpmProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdpmProcessName.setStatus("current")


class _BdpmProcessPriority_Type(Integer32):
    """Custom type bdpmProcessPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              55,
              60,
              128,
              180,
              255)
        )
    )
    namedValues = NamedValues(
        *(("critical", 0),
          ("high", 60),
          ("low", 180),
          ("normal", 128),
          ("veryhigh", 55),
          ("verylow", 255))
    )


_BdpmProcessPriority_Type.__name__ = "Integer32"
_BdpmProcessPriority_Object = MibTableColumn
bdpmProcessPriority = _BdpmProcessPriority_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 2, 1, 1, 3),
    _BdpmProcessPriority_Type()
)
bdpmProcessPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdpmProcessPriority.setStatus("current")
_BdpmProcessTimeCreated_Type = TimeStamp
_BdpmProcessTimeCreated_Object = MibTableColumn
bdpmProcessTimeCreated = _BdpmProcessTimeCreated_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 2, 1, 1, 4),
    _BdpmProcessTimeCreated_Type()
)
bdpmProcessTimeCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdpmProcessTimeCreated.setStatus("current")
_BdcomProcessMIBNotifPrefix_ObjectIdentity = ObjectIdentity
bdcomProcessMIBNotifPrefix = _BdcomProcessMIBNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 2)
)
_BdcomProcessMIBNotifs_ObjectIdentity = ObjectIdentity
bdcomProcessMIBNotifs = _BdcomProcessMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 2, 0)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BDCOM-PROCESS-MIB",
    **{"bdcomProcessMIB": bdcomProcessMIB,
       "bdcomProcessMIBObjects": bdcomProcessMIBObjects,
       "bdpmCPU": bdpmCPU,
       "bdpmCPUTotalTable": bdpmCPUTotalTable,
       "bdpmCPUTotalEntry": bdpmCPUTotalEntry,
       "bdpmCPUTotalIndex": bdpmCPUTotalIndex,
       "bdpmCPUTotalPhysicalIndex": bdpmCPUTotalPhysicalIndex,
       "bdpmCPUTotal5sec": bdpmCPUTotal5sec,
       "bdpmCPUTotal1min": bdpmCPUTotal1min,
       "bdpmCPUTotal5min": bdpmCPUTotal5min,
       "bdpmProcess": bdpmProcess,
       "bdpmProcessTable": bdpmProcessTable,
       "bdpmProcessEntry": bdpmProcessEntry,
       "bdpmProcessPID": bdpmProcessPID,
       "bdpmProcessName": bdpmProcessName,
       "bdpmProcessPriority": bdpmProcessPriority,
       "bdpmProcessTimeCreated": bdpmProcessTimeCreated,
       "bdcomProcessMIBNotifPrefix": bdcomProcessMIBNotifPrefix,
       "bdcomProcessMIBNotifs": bdcomProcessMIBNotifs}
)
