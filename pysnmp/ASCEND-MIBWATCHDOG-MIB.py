# SNMP MIB module (ASCEND-MIBWATCHDOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBWATCHDOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:35 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibwatchdogConfigProfile_ObjectIdentity = ObjectIdentity
mibwatchdogConfigProfile = _MibwatchdogConfigProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 162)
)
_MibwatchdogConfigProfileTable_Object = MibTable
mibwatchdogConfigProfileTable = _MibwatchdogConfigProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 162, 1)
)
if mibBuilder.loadTexts:
    mibwatchdogConfigProfileTable.setStatus("mandatory")
_MibwatchdogConfigProfileEntry_Object = MibTableRow
mibwatchdogConfigProfileEntry = _MibwatchdogConfigProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 162, 1, 1)
)
mibwatchdogConfigProfileEntry.setIndexNames(
    (0, "ASCEND-MIBWATCHDOG-MIB", "watchdogConfigProfile-WatchdogIndex-WatchdogType"),
    (0, "ASCEND-MIBWATCHDOG-MIB", "watchdogConfigProfile-WatchdogIndex-LocationId"),
    (0, "ASCEND-MIBWATCHDOG-MIB", "watchdogConfigProfile-WatchdogIndex-Unit"),
)
if mibBuilder.loadTexts:
    mibwatchdogConfigProfileEntry.setStatus("mandatory")
_WatchdogConfigProfile_WatchdogIndex_WatchdogType_Type = Integer32
_WatchdogConfigProfile_WatchdogIndex_WatchdogType_Object = MibScalar
watchdogConfigProfile_WatchdogIndex_WatchdogType = _WatchdogConfigProfile_WatchdogIndex_WatchdogType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 162, 1, 1, 1),
    _WatchdogConfigProfile_WatchdogIndex_WatchdogType_Type()
)
watchdogConfigProfile_WatchdogIndex_WatchdogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watchdogConfigProfile_WatchdogIndex_WatchdogType.setStatus("mandatory")
_WatchdogConfigProfile_WatchdogIndex_LocationId_Type = Integer32
_WatchdogConfigProfile_WatchdogIndex_LocationId_Object = MibScalar
watchdogConfigProfile_WatchdogIndex_LocationId = _WatchdogConfigProfile_WatchdogIndex_LocationId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 162, 1, 1, 2),
    _WatchdogConfigProfile_WatchdogIndex_LocationId_Type()
)
watchdogConfigProfile_WatchdogIndex_LocationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watchdogConfigProfile_WatchdogIndex_LocationId.setStatus("mandatory")
_WatchdogConfigProfile_WatchdogIndex_Unit_Type = Integer32
_WatchdogConfigProfile_WatchdogIndex_Unit_Object = MibScalar
watchdogConfigProfile_WatchdogIndex_Unit = _WatchdogConfigProfile_WatchdogIndex_Unit_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 162, 1, 1, 3),
    _WatchdogConfigProfile_WatchdogIndex_Unit_Type()
)
watchdogConfigProfile_WatchdogIndex_Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watchdogConfigProfile_WatchdogIndex_Unit.setStatus("mandatory")


class _WatchdogConfigProfile_WatchdogTrapEnable_Type(Integer32):
    """Custom type watchdogConfigProfile_WatchdogTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_WatchdogConfigProfile_WatchdogTrapEnable_Type.__name__ = "Integer32"
_WatchdogConfigProfile_WatchdogTrapEnable_Object = MibScalar
watchdogConfigProfile_WatchdogTrapEnable = _WatchdogConfigProfile_WatchdogTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 162, 1, 1, 4),
    _WatchdogConfigProfile_WatchdogTrapEnable_Type()
)
watchdogConfigProfile_WatchdogTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    watchdogConfigProfile_WatchdogTrapEnable.setStatus("mandatory")
_WatchdogConfigProfile_WatchdogName_Type = DisplayString
_WatchdogConfigProfile_WatchdogName_Object = MibScalar
watchdogConfigProfile_WatchdogName = _WatchdogConfigProfile_WatchdogName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 162, 1, 1, 5),
    _WatchdogConfigProfile_WatchdogName_Type()
)
watchdogConfigProfile_WatchdogName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    watchdogConfigProfile_WatchdogName.setStatus("mandatory")


class _WatchdogConfigProfile_Action_o_Type(Integer32):
    """Custom type watchdogConfigProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_WatchdogConfigProfile_Action_o_Type.__name__ = "Integer32"
_WatchdogConfigProfile_Action_o_Object = MibScalar
watchdogConfigProfile_Action_o = _WatchdogConfigProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 162, 1, 1, 6),
    _WatchdogConfigProfile_Action_o_Type()
)
watchdogConfigProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    watchdogConfigProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBWATCHDOG-MIB",
    **{"DisplayString": DisplayString,
       "mibwatchdogConfigProfile": mibwatchdogConfigProfile,
       "mibwatchdogConfigProfileTable": mibwatchdogConfigProfileTable,
       "mibwatchdogConfigProfileEntry": mibwatchdogConfigProfileEntry,
       "watchdogConfigProfile-WatchdogIndex-WatchdogType": watchdogConfigProfile_WatchdogIndex_WatchdogType,
       "watchdogConfigProfile-WatchdogIndex-LocationId": watchdogConfigProfile_WatchdogIndex_LocationId,
       "watchdogConfigProfile-WatchdogIndex-Unit": watchdogConfigProfile_WatchdogIndex_Unit,
       "watchdogConfigProfile-WatchdogTrapEnable": watchdogConfigProfile_WatchdogTrapEnable,
       "watchdogConfigProfile-WatchdogName": watchdogConfigProfile_WatchdogName,
       "watchdogConfigProfile-Action-o": watchdogConfigProfile_Action_o}
)
