# SNMP MIB module (BAY-STACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAY-STACK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:10 2024
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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 13)
)
bayStackMib.setRevisions(
        ("2013-10-11 00:00",
         "2012-10-02 00:00",
         "2009-09-28 00:00",
         "2007-09-04 00:00",
         "2005-08-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BayStackObjects_ObjectIdentity = ObjectIdentity
bayStackObjects = _BayStackObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 13, 1)
)
_BayStackConfig_ObjectIdentity = ObjectIdentity
bayStackConfig = _BayStackConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 13, 1, 1)
)


class _BayStackConfigExpectedStackSize_Type(Integer32):
    """Custom type bayStackConfigExpectedStackSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BayStackConfigExpectedStackSize_Type.__name__ = "Integer32"
_BayStackConfigExpectedStackSize_Object = MibScalar
bayStackConfigExpectedStackSize = _BayStackConfigExpectedStackSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 13, 1, 1, 1),
    _BayStackConfigExpectedStackSize_Type()
)
bayStackConfigExpectedStackSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bayStackConfigExpectedStackSize.setStatus("current")


class _BayStackConfigStackErrorNotificationInterval_Type(Integer32):
    """Custom type bayStackConfigStackErrorNotificationInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BayStackConfigStackErrorNotificationInterval_Type.__name__ = "Integer32"
_BayStackConfigStackErrorNotificationInterval_Object = MibScalar
bayStackConfigStackErrorNotificationInterval = _BayStackConfigStackErrorNotificationInterval_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 13, 1, 1, 2),
    _BayStackConfigStackErrorNotificationInterval_Type()
)
bayStackConfigStackErrorNotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bayStackConfigStackErrorNotificationInterval.setStatus("current")
if mibBuilder.loadTexts:
    bayStackConfigStackErrorNotificationInterval.setUnits("Seconds")
_BayStackConfigStackErrorNotificationEnabled_Type = TruthValue
_BayStackConfigStackErrorNotificationEnabled_Object = MibScalar
bayStackConfigStackErrorNotificationEnabled = _BayStackConfigStackErrorNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 13, 1, 1, 3),
    _BayStackConfigStackErrorNotificationEnabled_Type()
)
bayStackConfigStackErrorNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bayStackConfigStackErrorNotificationEnabled.setStatus("current")
_BayStackConfigStackRebootUnitOnFailure_Type = TruthValue
_BayStackConfigStackRebootUnitOnFailure_Object = MibScalar
bayStackConfigStackRebootUnitOnFailure = _BayStackConfigStackRebootUnitOnFailure_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 13, 1, 1, 4),
    _BayStackConfigStackRebootUnitOnFailure_Type()
)
bayStackConfigStackRebootUnitOnFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bayStackConfigStackRebootUnitOnFailure.setStatus("current")


class _BayStackConfigStackRetryCount_Type(Unsigned32):
    """Custom type bayStackConfigStackRetryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_BayStackConfigStackRetryCount_Type.__name__ = "Unsigned32"
_BayStackConfigStackRetryCount_Object = MibScalar
bayStackConfigStackRetryCount = _BayStackConfigStackRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 13, 1, 1, 5),
    _BayStackConfigStackRetryCount_Type()
)
bayStackConfigStackRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bayStackConfigStackRetryCount.setStatus("current")
_BayStackUnitConfigTable_Object = MibTable
bayStackUnitConfigTable = _BayStackUnitConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 13, 1, 2)
)
if mibBuilder.loadTexts:
    bayStackUnitConfigTable.setStatus("current")
_BayStackUnitConfigEntry_Object = MibTableRow
bayStackUnitConfigEntry = _BayStackUnitConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 13, 1, 2, 1)
)
bayStackUnitConfigEntry.setIndexNames(
    (0, "BAY-STACK-MIB", "bayStackUnitConfigIndex"),
)
if mibBuilder.loadTexts:
    bayStackUnitConfigEntry.setStatus("current")


class _BayStackUnitConfigIndex_Type(Integer32):
    """Custom type bayStackUnitConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BayStackUnitConfigIndex_Type.__name__ = "Integer32"
_BayStackUnitConfigIndex_Object = MibTableColumn
bayStackUnitConfigIndex = _BayStackUnitConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 13, 1, 2, 1, 1),
    _BayStackUnitConfigIndex_Type()
)
bayStackUnitConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bayStackUnitConfigIndex.setStatus("current")


class _BayStackUnitConfigRearPortAdminMode_Type(Integer32):
    """Custom type bayStackUnitConfigRearPortAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("spb", 3),
          ("stacking", 2),
          ("standalone", 1))
    )


_BayStackUnitConfigRearPortAdminMode_Type.__name__ = "Integer32"
_BayStackUnitConfigRearPortAdminMode_Object = MibTableColumn
bayStackUnitConfigRearPortAdminMode = _BayStackUnitConfigRearPortAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 13, 1, 2, 1, 2),
    _BayStackUnitConfigRearPortAdminMode_Type()
)
bayStackUnitConfigRearPortAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bayStackUnitConfigRearPortAdminMode.setStatus("current")


class _BayStackUnitConfigRearPortOperMode_Type(Integer32):
    """Custom type bayStackUnitConfigRearPortOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("spb", 3),
          ("stacking", 2),
          ("standalone", 1))
    )


_BayStackUnitConfigRearPortOperMode_Type.__name__ = "Integer32"
_BayStackUnitConfigRearPortOperMode_Object = MibTableColumn
bayStackUnitConfigRearPortOperMode = _BayStackUnitConfigRearPortOperMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 13, 1, 2, 1, 3),
    _BayStackUnitConfigRearPortOperMode_Type()
)
bayStackUnitConfigRearPortOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bayStackUnitConfigRearPortOperMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-MIB",
    **{"bayStackMib": bayStackMib,
       "bayStackObjects": bayStackObjects,
       "bayStackConfig": bayStackConfig,
       "bayStackConfigExpectedStackSize": bayStackConfigExpectedStackSize,
       "bayStackConfigStackErrorNotificationInterval": bayStackConfigStackErrorNotificationInterval,
       "bayStackConfigStackErrorNotificationEnabled": bayStackConfigStackErrorNotificationEnabled,
       "bayStackConfigStackRebootUnitOnFailure": bayStackConfigStackRebootUnitOnFailure,
       "bayStackConfigStackRetryCount": bayStackConfigStackRetryCount,
       "bayStackUnitConfigTable": bayStackUnitConfigTable,
       "bayStackUnitConfigEntry": bayStackUnitConfigEntry,
       "bayStackUnitConfigIndex": bayStackUnitConfigIndex,
       "bayStackUnitConfigRearPortAdminMode": bayStackUnitConfigRearPortAdminMode,
       "bayStackUnitConfigRearPortOperMode": bayStackUnitConfigRearPortOperMode}
)
