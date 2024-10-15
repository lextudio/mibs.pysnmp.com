# SNMP MIB module (Nortel-MsCarrier-MscPassport-HuntGroupEngMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-HuntGroupEngMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:35 2024
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

(mscLpEng,
 mscLpEngIndex,
 mscLpIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB",
    "mscLpEng",
    "mscLpEngIndex",
    "mscLpIndex")

(Counter32,
 DisplayString,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(NonReplicated,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "NonReplicated")

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MscLpEngHgs_ObjectIdentity = ObjectIdentity
mscLpEngHgs = _MscLpEngHgs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 4)
)
_MscLpEngHgsRowStatusTable_Object = MibTable
mscLpEngHgsRowStatusTable = _MscLpEngHgsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 4, 1)
)
if mibBuilder.loadTexts:
    mscLpEngHgsRowStatusTable.setStatus("mandatory")
_MscLpEngHgsRowStatusEntry_Object = MibTableRow
mscLpEngHgsRowStatusEntry = _MscLpEngHgsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 4, 1, 1)
)
mscLpEngHgsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-HuntGroupEngMIB", "mscLpEngHgsIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngHgsRowStatusEntry.setStatus("mandatory")
_MscLpEngHgsRowStatus_Type = RowStatus
_MscLpEngHgsRowStatus_Object = MibTableColumn
mscLpEngHgsRowStatus = _MscLpEngHgsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 4, 1, 1, 1),
    _MscLpEngHgsRowStatus_Type()
)
mscLpEngHgsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEngHgsRowStatus.setStatus("mandatory")
_MscLpEngHgsComponentName_Type = DisplayString
_MscLpEngHgsComponentName_Object = MibTableColumn
mscLpEngHgsComponentName = _MscLpEngHgsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 4, 1, 1, 2),
    _MscLpEngHgsComponentName_Type()
)
mscLpEngHgsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngHgsComponentName.setStatus("mandatory")
_MscLpEngHgsStorageType_Type = StorageType
_MscLpEngHgsStorageType_Object = MibTableColumn
mscLpEngHgsStorageType = _MscLpEngHgsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 4, 1, 1, 4),
    _MscLpEngHgsStorageType_Type()
)
mscLpEngHgsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngHgsStorageType.setStatus("mandatory")
_MscLpEngHgsIndex_Type = NonReplicated
_MscLpEngHgsIndex_Object = MibTableColumn
mscLpEngHgsIndex = _MscLpEngHgsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 4, 1, 1, 10),
    _MscLpEngHgsIndex_Type()
)
mscLpEngHgsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEngHgsIndex.setStatus("mandatory")
_MscLpEngHgsOperationalTable_Object = MibTable
mscLpEngHgsOperationalTable = _MscLpEngHgsOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 4, 10)
)
if mibBuilder.loadTexts:
    mscLpEngHgsOperationalTable.setStatus("mandatory")
_MscLpEngHgsOperationalEntry_Object = MibTableRow
mscLpEngHgsOperationalEntry = _MscLpEngHgsOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 4, 10, 1)
)
mscLpEngHgsOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-HuntGroupEngMIB", "mscLpEngHgsIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngHgsOperationalEntry.setStatus("mandatory")


class _MscLpEngHgsHuntGroups_Type(Unsigned32):
    """Custom type mscLpEngHgsHuntGroups based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscLpEngHgsHuntGroups_Type.__name__ = "Unsigned32"
_MscLpEngHgsHuntGroups_Object = MibTableColumn
mscLpEngHgsHuntGroups = _MscLpEngHgsHuntGroups_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 4, 10, 1, 1),
    _MscLpEngHgsHuntGroups_Type()
)
mscLpEngHgsHuntGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngHgsHuntGroups.setStatus("mandatory")
_MscLpEngHgsHuntAttempts_Type = Counter32
_MscLpEngHgsHuntAttempts_Object = MibTableColumn
mscLpEngHgsHuntAttempts = _MscLpEngHgsHuntAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 4, 10, 1, 2),
    _MscLpEngHgsHuntAttempts_Type()
)
mscLpEngHgsHuntAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngHgsHuntAttempts.setStatus("mandatory")
_HuntGroupEngMIB_ObjectIdentity = ObjectIdentity
huntGroupEngMIB = _HuntGroupEngMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 131)
)
_HuntGroupEngGroup_ObjectIdentity = ObjectIdentity
huntGroupEngGroup = _HuntGroupEngGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 131, 1)
)
_HuntGroupEngGroupCA_ObjectIdentity = ObjectIdentity
huntGroupEngGroupCA = _HuntGroupEngGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 131, 1, 1)
)
_HuntGroupEngGroupCA02_ObjectIdentity = ObjectIdentity
huntGroupEngGroupCA02 = _HuntGroupEngGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 131, 1, 1, 3)
)
_HuntGroupEngGroupCA02A_ObjectIdentity = ObjectIdentity
huntGroupEngGroupCA02A = _HuntGroupEngGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 131, 1, 1, 3, 2)
)
_HuntGroupEngCapabilities_ObjectIdentity = ObjectIdentity
huntGroupEngCapabilities = _HuntGroupEngCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 131, 3)
)
_HuntGroupEngCapabilitiesCA_ObjectIdentity = ObjectIdentity
huntGroupEngCapabilitiesCA = _HuntGroupEngCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 131, 3, 1)
)
_HuntGroupEngCapabilitiesCA02_ObjectIdentity = ObjectIdentity
huntGroupEngCapabilitiesCA02 = _HuntGroupEngCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 131, 3, 1, 3)
)
_HuntGroupEngCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
huntGroupEngCapabilitiesCA02A = _HuntGroupEngCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 131, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-HuntGroupEngMIB",
    **{"mscLpEngHgs": mscLpEngHgs,
       "mscLpEngHgsRowStatusTable": mscLpEngHgsRowStatusTable,
       "mscLpEngHgsRowStatusEntry": mscLpEngHgsRowStatusEntry,
       "mscLpEngHgsRowStatus": mscLpEngHgsRowStatus,
       "mscLpEngHgsComponentName": mscLpEngHgsComponentName,
       "mscLpEngHgsStorageType": mscLpEngHgsStorageType,
       "mscLpEngHgsIndex": mscLpEngHgsIndex,
       "mscLpEngHgsOperationalTable": mscLpEngHgsOperationalTable,
       "mscLpEngHgsOperationalEntry": mscLpEngHgsOperationalEntry,
       "mscLpEngHgsHuntGroups": mscLpEngHgsHuntGroups,
       "mscLpEngHgsHuntAttempts": mscLpEngHgsHuntAttempts,
       "huntGroupEngMIB": huntGroupEngMIB,
       "huntGroupEngGroup": huntGroupEngGroup,
       "huntGroupEngGroupCA": huntGroupEngGroupCA,
       "huntGroupEngGroupCA02": huntGroupEngGroupCA02,
       "huntGroupEngGroupCA02A": huntGroupEngGroupCA02A,
       "huntGroupEngCapabilities": huntGroupEngCapabilities,
       "huntGroupEngCapabilitiesCA": huntGroupEngCapabilitiesCA,
       "huntGroupEngCapabilitiesCA02": huntGroupEngCapabilitiesCA02,
       "huntGroupEngCapabilitiesCA02A": huntGroupEngCapabilitiesCA02A}
)
