# SNMP MIB module (Nortel-Magellan-Passport-StateSummaryMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-StateSummaryMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:25 2024
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

(components,
 passportMIBs) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "components",
    "passportMIBs")

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

stateSummaryMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StateSummary_ObjectIdentity = ObjectIdentity
stateSummary = _StateSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5)
)
_TimeOfLastTableChange_ObjectIdentity = ObjectIdentity
timeOfLastTableChange = _TimeOfLastTableChange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5, 1)
)
_TimeOfLastStateSummTableChange_Type = TimeTicks
_TimeOfLastStateSummTableChange_Object = MibScalar
timeOfLastStateSummTableChange = _TimeOfLastStateSummTableChange_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5, 1, 1),
    _TimeOfLastStateSummTableChange_Type()
)
timeOfLastStateSummTableChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeOfLastStateSummTableChange.setStatus("current")
_CompClassTable_Object = MibTable
compClassTable = _CompClassTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5, 2)
)
if mibBuilder.loadTexts:
    compClassTable.setStatus("current")
_CompClassEntry_Object = MibTableRow
compClassEntry = _CompClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5, 2, 1)
)
compClassEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-StateSummaryMIB", "compClass"),
)
if mibBuilder.loadTexts:
    compClassEntry.setStatus("current")
_CompClass_Type = ObjectIdentifier
_CompClass_Object = MibTableColumn
compClass = _CompClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5, 2, 1, 1),
    _CompClass_Type()
)
compClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compClass.setStatus("current")
_CompName_Type = DisplayString
_CompName_Object = MibTableColumn
compName = _CompName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5, 2, 1, 2),
    _CompName_Type()
)
compName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compName.setStatus("current")
_TimeOfLastStateStatusChange_Type = TimeTicks
_TimeOfLastStateStatusChange_Object = MibTableColumn
timeOfLastStateStatusChange = _TimeOfLastStateStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5, 2, 1, 3),
    _TimeOfLastStateStatusChange_Type()
)
timeOfLastStateStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeOfLastStateStatusChange.setStatus("current")
_NumberDown_Type = Gauge32
_NumberDown_Object = MibTableColumn
numberDown = _NumberDown_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5, 2, 1, 4),
    _NumberDown_Type()
)
numberDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberDown.setStatus("current")
_NumberTroubled_Type = Gauge32
_NumberTroubled_Object = MibTableColumn
numberTroubled = _NumberTroubled_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5, 2, 1, 5),
    _NumberTroubled_Type()
)
numberTroubled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberTroubled.setStatus("current")
_StateSummaryGroupBE00A_ObjectIdentity = ObjectIdentity
stateSummaryGroupBE00A = _StateSummaryGroupBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 7, 1, 3, 2, 2)
)
_StateSummaryCapabilitiesBE00A_ObjectIdentity = ObjectIdentity
stateSummaryCapabilitiesBE00A = _StateSummaryCapabilitiesBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 7, 3, 3, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-StateSummaryMIB",
    **{"stateSummary": stateSummary,
       "timeOfLastTableChange": timeOfLastTableChange,
       "timeOfLastStateSummTableChange": timeOfLastStateSummTableChange,
       "compClassTable": compClassTable,
       "compClassEntry": compClassEntry,
       "compClass": compClass,
       "compName": compName,
       "timeOfLastStateStatusChange": timeOfLastStateStatusChange,
       "numberDown": numberDown,
       "numberTroubled": numberTroubled,
       "stateSummaryMIB": stateSummaryMIB,
       "stateSummaryGroupBE00A": stateSummaryGroupBE00A,
       "stateSummaryCapabilitiesBE00A": stateSummaryCapabilitiesBE00A}
)
