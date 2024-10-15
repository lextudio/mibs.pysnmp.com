# SNMP MIB module (Nortel-MsCarrier-MscPassport-StateSummaryMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-StateSummaryMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:05 2024
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

(mscComponents,
 mscPassportMIBs) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscComponents",
    "mscPassportMIBs")

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
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MscStateSummary_ObjectIdentity = ObjectIdentity
mscStateSummary = _MscStateSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5)
)
_MscTimeOfLastTableChange_ObjectIdentity = ObjectIdentity
mscTimeOfLastTableChange = _MscTimeOfLastTableChange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5, 1)
)
_MscTimeOfLastStateSummTableChange_Type = TimeTicks
_MscTimeOfLastStateSummTableChange_Object = MibScalar
mscTimeOfLastStateSummTableChange = _MscTimeOfLastStateSummTableChange_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5, 1, 1),
    _MscTimeOfLastStateSummTableChange_Type()
)
mscTimeOfLastStateSummTableChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTimeOfLastStateSummTableChange.setStatus("current")
_MscCompClassTable_Object = MibTable
mscCompClassTable = _MscCompClassTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    mscCompClassTable.setStatus("current")
_MscCompClassEntry_Object = MibTableRow
mscCompClassEntry = _MscCompClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5, 2, 1)
)
mscCompClassEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-StateSummaryMIB", "mscCompClass"),
)
if mibBuilder.loadTexts:
    mscCompClassEntry.setStatus("current")
_MscCompClass_Type = ObjectIdentifier
_MscCompClass_Object = MibTableColumn
mscCompClass = _MscCompClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5, 2, 1, 1),
    _MscCompClass_Type()
)
mscCompClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCompClass.setStatus("current")
_MscCompName_Type = DisplayString
_MscCompName_Object = MibTableColumn
mscCompName = _MscCompName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5, 2, 1, 2),
    _MscCompName_Type()
)
mscCompName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCompName.setStatus("current")
_MscTimeOfLastStateStatusChange_Type = TimeTicks
_MscTimeOfLastStateStatusChange_Object = MibTableColumn
mscTimeOfLastStateStatusChange = _MscTimeOfLastStateStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5, 2, 1, 3),
    _MscTimeOfLastStateStatusChange_Type()
)
mscTimeOfLastStateStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTimeOfLastStateStatusChange.setStatus("current")
_MscNumberDown_Type = Gauge32
_MscNumberDown_Object = MibTableColumn
mscNumberDown = _MscNumberDown_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5, 2, 1, 4),
    _MscNumberDown_Type()
)
mscNumberDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNumberDown.setStatus("current")
_MscNumberTroubled_Type = Gauge32
_MscNumberTroubled_Object = MibTableColumn
mscNumberTroubled = _MscNumberTroubled_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5, 2, 1, 5),
    _MscNumberTroubled_Type()
)
mscNumberTroubled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNumberTroubled.setStatus("current")
_StateSummaryGroupCA01A_ObjectIdentity = ObjectIdentity
stateSummaryGroupCA01A = _StateSummaryGroupCA01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 7, 1, 1, 2, 2)
)
_StateSummaryCapabilitiesCA01A_ObjectIdentity = ObjectIdentity
stateSummaryCapabilitiesCA01A = _StateSummaryCapabilitiesCA01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 7, 3, 1, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-StateSummaryMIB",
    **{"mscStateSummary": mscStateSummary,
       "mscTimeOfLastTableChange": mscTimeOfLastTableChange,
       "mscTimeOfLastStateSummTableChange": mscTimeOfLastStateSummTableChange,
       "mscCompClassTable": mscCompClassTable,
       "mscCompClassEntry": mscCompClassEntry,
       "mscCompClass": mscCompClass,
       "mscCompName": mscCompName,
       "mscTimeOfLastStateStatusChange": mscTimeOfLastStateStatusChange,
       "mscNumberDown": mscNumberDown,
       "mscNumberTroubled": mscNumberTroubled,
       "stateSummaryMIB": stateSummaryMIB,
       "stateSummaryGroupCA01A": stateSummaryGroupCA01A,
       "stateSummaryCapabilitiesCA01A": stateSummaryCapabilitiesCA01A}
)
