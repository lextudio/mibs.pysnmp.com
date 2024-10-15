# SNMP MIB module (Nortel-Magellan-Passport-HuntGroupEngMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-HuntGroupEngMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:55 2024
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

(lpEng,
 lpEngIndex,
 lpIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-LogicalProcessorMIB",
    "lpEng",
    "lpEngIndex",
    "lpIndex")

(Counter32,
 DisplayString,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(NonReplicated,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "NonReplicated")

(passportMIBs,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LpEngHgs_ObjectIdentity = ObjectIdentity
lpEngHgs = _LpEngHgs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 4)
)
_LpEngHgsRowStatusTable_Object = MibTable
lpEngHgsRowStatusTable = _LpEngHgsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 4, 1)
)
if mibBuilder.loadTexts:
    lpEngHgsRowStatusTable.setStatus("mandatory")
_LpEngHgsRowStatusEntry_Object = MibTableRow
lpEngHgsRowStatusEntry = _LpEngHgsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 4, 1, 1)
)
lpEngHgsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-HuntGroupEngMIB", "lpEngHgsIndex"),
)
if mibBuilder.loadTexts:
    lpEngHgsRowStatusEntry.setStatus("mandatory")
_LpEngHgsRowStatus_Type = RowStatus
_LpEngHgsRowStatus_Object = MibTableColumn
lpEngHgsRowStatus = _LpEngHgsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 4, 1, 1, 1),
    _LpEngHgsRowStatus_Type()
)
lpEngHgsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngHgsRowStatus.setStatus("mandatory")
_LpEngHgsComponentName_Type = DisplayString
_LpEngHgsComponentName_Object = MibTableColumn
lpEngHgsComponentName = _LpEngHgsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 4, 1, 1, 2),
    _LpEngHgsComponentName_Type()
)
lpEngHgsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngHgsComponentName.setStatus("mandatory")
_LpEngHgsStorageType_Type = StorageType
_LpEngHgsStorageType_Object = MibTableColumn
lpEngHgsStorageType = _LpEngHgsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 4, 1, 1, 4),
    _LpEngHgsStorageType_Type()
)
lpEngHgsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngHgsStorageType.setStatus("mandatory")
_LpEngHgsIndex_Type = NonReplicated
_LpEngHgsIndex_Object = MibTableColumn
lpEngHgsIndex = _LpEngHgsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 4, 1, 1, 10),
    _LpEngHgsIndex_Type()
)
lpEngHgsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEngHgsIndex.setStatus("mandatory")
_LpEngHgsOperationalTable_Object = MibTable
lpEngHgsOperationalTable = _LpEngHgsOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 4, 10)
)
if mibBuilder.loadTexts:
    lpEngHgsOperationalTable.setStatus("mandatory")
_LpEngHgsOperationalEntry_Object = MibTableRow
lpEngHgsOperationalEntry = _LpEngHgsOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 4, 10, 1)
)
lpEngHgsOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-HuntGroupEngMIB", "lpEngHgsIndex"),
)
if mibBuilder.loadTexts:
    lpEngHgsOperationalEntry.setStatus("mandatory")


class _LpEngHgsHuntGroups_Type(Unsigned32):
    """Custom type lpEngHgsHuntGroups based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LpEngHgsHuntGroups_Type.__name__ = "Unsigned32"
_LpEngHgsHuntGroups_Object = MibTableColumn
lpEngHgsHuntGroups = _LpEngHgsHuntGroups_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 4, 10, 1, 1),
    _LpEngHgsHuntGroups_Type()
)
lpEngHgsHuntGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngHgsHuntGroups.setStatus("mandatory")
_LpEngHgsHuntAttempts_Type = Counter32
_LpEngHgsHuntAttempts_Object = MibTableColumn
lpEngHgsHuntAttempts = _LpEngHgsHuntAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 4, 10, 1, 2),
    _LpEngHgsHuntAttempts_Type()
)
lpEngHgsHuntAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngHgsHuntAttempts.setStatus("mandatory")
_HuntGroupEngMIB_ObjectIdentity = ObjectIdentity
huntGroupEngMIB = _HuntGroupEngMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 131)
)
_HuntGroupEngGroup_ObjectIdentity = ObjectIdentity
huntGroupEngGroup = _HuntGroupEngGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 131, 1)
)
_HuntGroupEngGroupBE_ObjectIdentity = ObjectIdentity
huntGroupEngGroupBE = _HuntGroupEngGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 131, 1, 5)
)
_HuntGroupEngGroupBE01_ObjectIdentity = ObjectIdentity
huntGroupEngGroupBE01 = _HuntGroupEngGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 131, 1, 5, 2)
)
_HuntGroupEngGroupBE01A_ObjectIdentity = ObjectIdentity
huntGroupEngGroupBE01A = _HuntGroupEngGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 131, 1, 5, 2, 2)
)
_HuntGroupEngCapabilities_ObjectIdentity = ObjectIdentity
huntGroupEngCapabilities = _HuntGroupEngCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 131, 3)
)
_HuntGroupEngCapabilitiesBE_ObjectIdentity = ObjectIdentity
huntGroupEngCapabilitiesBE = _HuntGroupEngCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 131, 3, 5)
)
_HuntGroupEngCapabilitiesBE01_ObjectIdentity = ObjectIdentity
huntGroupEngCapabilitiesBE01 = _HuntGroupEngCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 131, 3, 5, 2)
)
_HuntGroupEngCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
huntGroupEngCapabilitiesBE01A = _HuntGroupEngCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 131, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-HuntGroupEngMIB",
    **{"lpEngHgs": lpEngHgs,
       "lpEngHgsRowStatusTable": lpEngHgsRowStatusTable,
       "lpEngHgsRowStatusEntry": lpEngHgsRowStatusEntry,
       "lpEngHgsRowStatus": lpEngHgsRowStatus,
       "lpEngHgsComponentName": lpEngHgsComponentName,
       "lpEngHgsStorageType": lpEngHgsStorageType,
       "lpEngHgsIndex": lpEngHgsIndex,
       "lpEngHgsOperationalTable": lpEngHgsOperationalTable,
       "lpEngHgsOperationalEntry": lpEngHgsOperationalEntry,
       "lpEngHgsHuntGroups": lpEngHgsHuntGroups,
       "lpEngHgsHuntAttempts": lpEngHgsHuntAttempts,
       "huntGroupEngMIB": huntGroupEngMIB,
       "huntGroupEngGroup": huntGroupEngGroup,
       "huntGroupEngGroupBE": huntGroupEngGroupBE,
       "huntGroupEngGroupBE01": huntGroupEngGroupBE01,
       "huntGroupEngGroupBE01A": huntGroupEngGroupBE01A,
       "huntGroupEngCapabilities": huntGroupEngCapabilities,
       "huntGroupEngCapabilitiesBE": huntGroupEngCapabilitiesBE,
       "huntGroupEngCapabilitiesBE01": huntGroupEngCapabilitiesBE01,
       "huntGroupEngCapabilitiesBE01A": huntGroupEngCapabilitiesBE01A}
)
