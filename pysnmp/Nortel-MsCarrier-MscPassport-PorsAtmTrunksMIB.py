# SNMP MIB module (Nortel-MsCarrier-MscPassport-PorsAtmTrunksMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-PorsAtmTrunksMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:55 2024
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

(mscTrkPa,
 mscTrkPaIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-PorsTrunksMIB",
    "mscTrkPa",
    "mscTrkPaIndex")

(DisplayString,
 RowStatus,
 StorageType) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "DisplayString",
    "RowStatus",
    "StorageType")

(Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "Link",
    "NonReplicated")

(mscTrkIndex,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TrunksMIB",
    "mscTrkIndex")

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

_MscTrkPaAtm_ObjectIdentity = ObjectIdentity
mscTrkPaAtm = _MscTrkPaAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 3)
)
_MscTrkPaAtmRowStatusTable_Object = MibTable
mscTrkPaAtmRowStatusTable = _MscTrkPaAtmRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 3, 1)
)
if mibBuilder.loadTexts:
    mscTrkPaAtmRowStatusTable.setStatus("mandatory")
_MscTrkPaAtmRowStatusEntry_Object = MibTableRow
mscTrkPaAtmRowStatusEntry = _MscTrkPaAtmRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 3, 1, 1)
)
mscTrkPaAtmRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkPaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsAtmTrunksMIB", "mscTrkPaAtmIndex"),
)
if mibBuilder.loadTexts:
    mscTrkPaAtmRowStatusEntry.setStatus("mandatory")
_MscTrkPaAtmRowStatus_Type = RowStatus
_MscTrkPaAtmRowStatus_Object = MibTableColumn
mscTrkPaAtmRowStatus = _MscTrkPaAtmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 3, 1, 1, 1),
    _MscTrkPaAtmRowStatus_Type()
)
mscTrkPaAtmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkPaAtmRowStatus.setStatus("mandatory")
_MscTrkPaAtmComponentName_Type = DisplayString
_MscTrkPaAtmComponentName_Object = MibTableColumn
mscTrkPaAtmComponentName = _MscTrkPaAtmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 3, 1, 1, 2),
    _MscTrkPaAtmComponentName_Type()
)
mscTrkPaAtmComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPaAtmComponentName.setStatus("mandatory")
_MscTrkPaAtmStorageType_Type = StorageType
_MscTrkPaAtmStorageType_Object = MibTableColumn
mscTrkPaAtmStorageType = _MscTrkPaAtmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 3, 1, 1, 4),
    _MscTrkPaAtmStorageType_Type()
)
mscTrkPaAtmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkPaAtmStorageType.setStatus("mandatory")
_MscTrkPaAtmIndex_Type = NonReplicated
_MscTrkPaAtmIndex_Object = MibTableColumn
mscTrkPaAtmIndex = _MscTrkPaAtmIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 3, 1, 1, 10),
    _MscTrkPaAtmIndex_Type()
)
mscTrkPaAtmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkPaAtmIndex.setStatus("mandatory")
_MscTrkPaAtmProvTable_Object = MibTable
mscTrkPaAtmProvTable = _MscTrkPaAtmProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 3, 10)
)
if mibBuilder.loadTexts:
    mscTrkPaAtmProvTable.setStatus("mandatory")
_MscTrkPaAtmProvEntry_Object = MibTableRow
mscTrkPaAtmProvEntry = _MscTrkPaAtmProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 3, 10, 1)
)
mscTrkPaAtmProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkPaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PorsAtmTrunksMIB", "mscTrkPaAtmIndex"),
)
if mibBuilder.loadTexts:
    mscTrkPaAtmProvEntry.setStatus("mandatory")
_MscTrkPaAtmAtmConnection_Type = Link
_MscTrkPaAtmAtmConnection_Object = MibTableColumn
mscTrkPaAtmAtmConnection = _MscTrkPaAtmAtmConnection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 3, 10, 1, 1),
    _MscTrkPaAtmAtmConnection_Type()
)
mscTrkPaAtmAtmConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkPaAtmAtmConnection.setStatus("mandatory")


class _MscTrkPaAtmMode_Type(Integer32):
    """Custom type mscTrkPaAtmMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mapping", 1),
          ("multiplexing", 0))
    )


_MscTrkPaAtmMode_Type.__name__ = "Integer32"
_MscTrkPaAtmMode_Object = MibTableColumn
mscTrkPaAtmMode = _MscTrkPaAtmMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 3, 10, 1, 2),
    _MscTrkPaAtmMode_Type()
)
mscTrkPaAtmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkPaAtmMode.setStatus("mandatory")
_PorsAtmTrunksMIB_ObjectIdentity = ObjectIdentity
porsAtmTrunksMIB = _PorsAtmTrunksMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 137)
)
_PorsAtmTrunksGroup_ObjectIdentity = ObjectIdentity
porsAtmTrunksGroup = _PorsAtmTrunksGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 137, 1)
)
_PorsAtmTrunksGroupCA_ObjectIdentity = ObjectIdentity
porsAtmTrunksGroupCA = _PorsAtmTrunksGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 137, 1, 1)
)
_PorsAtmTrunksGroupCA02_ObjectIdentity = ObjectIdentity
porsAtmTrunksGroupCA02 = _PorsAtmTrunksGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 137, 1, 1, 3)
)
_PorsAtmTrunksGroupCA02A_ObjectIdentity = ObjectIdentity
porsAtmTrunksGroupCA02A = _PorsAtmTrunksGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 137, 1, 1, 3, 2)
)
_PorsAtmTrunksCapabilities_ObjectIdentity = ObjectIdentity
porsAtmTrunksCapabilities = _PorsAtmTrunksCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 137, 3)
)
_PorsAtmTrunksCapabilitiesCA_ObjectIdentity = ObjectIdentity
porsAtmTrunksCapabilitiesCA = _PorsAtmTrunksCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 137, 3, 1)
)
_PorsAtmTrunksCapabilitiesCA02_ObjectIdentity = ObjectIdentity
porsAtmTrunksCapabilitiesCA02 = _PorsAtmTrunksCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 137, 3, 1, 3)
)
_PorsAtmTrunksCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
porsAtmTrunksCapabilitiesCA02A = _PorsAtmTrunksCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 137, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-PorsAtmTrunksMIB",
    **{"mscTrkPaAtm": mscTrkPaAtm,
       "mscTrkPaAtmRowStatusTable": mscTrkPaAtmRowStatusTable,
       "mscTrkPaAtmRowStatusEntry": mscTrkPaAtmRowStatusEntry,
       "mscTrkPaAtmRowStatus": mscTrkPaAtmRowStatus,
       "mscTrkPaAtmComponentName": mscTrkPaAtmComponentName,
       "mscTrkPaAtmStorageType": mscTrkPaAtmStorageType,
       "mscTrkPaAtmIndex": mscTrkPaAtmIndex,
       "mscTrkPaAtmProvTable": mscTrkPaAtmProvTable,
       "mscTrkPaAtmProvEntry": mscTrkPaAtmProvEntry,
       "mscTrkPaAtmAtmConnection": mscTrkPaAtmAtmConnection,
       "mscTrkPaAtmMode": mscTrkPaAtmMode,
       "porsAtmTrunksMIB": porsAtmTrunksMIB,
       "porsAtmTrunksGroup": porsAtmTrunksGroup,
       "porsAtmTrunksGroupCA": porsAtmTrunksGroupCA,
       "porsAtmTrunksGroupCA02": porsAtmTrunksGroupCA02,
       "porsAtmTrunksGroupCA02A": porsAtmTrunksGroupCA02A,
       "porsAtmTrunksCapabilities": porsAtmTrunksCapabilities,
       "porsAtmTrunksCapabilitiesCA": porsAtmTrunksCapabilitiesCA,
       "porsAtmTrunksCapabilitiesCA02": porsAtmTrunksCapabilitiesCA02,
       "porsAtmTrunksCapabilitiesCA02A": porsAtmTrunksCapabilitiesCA02A}
)
