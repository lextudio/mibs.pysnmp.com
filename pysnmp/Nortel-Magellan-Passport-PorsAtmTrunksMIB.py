# SNMP MIB module (Nortel-Magellan-Passport-PorsAtmTrunksMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-PorsAtmTrunksMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:15 2024
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

(trkPa,
 trkPaIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-PorsTrunksMIB",
    "trkPa",
    "trkPaIndex")

(DisplayString,
 RowStatus,
 StorageType) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DisplayString",
    "RowStatus",
    "StorageType")

(Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "Link",
    "NonReplicated")

(trkIndex,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TrunksMIB",
    "trkIndex")

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

_TrkPaAtm_ObjectIdentity = ObjectIdentity
trkPaAtm = _TrkPaAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 3)
)
_TrkPaAtmRowStatusTable_Object = MibTable
trkPaAtmRowStatusTable = _TrkPaAtmRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 3, 1)
)
if mibBuilder.loadTexts:
    trkPaAtmRowStatusTable.setStatus("mandatory")
_TrkPaAtmRowStatusEntry_Object = MibTableRow
trkPaAtmRowStatusEntry = _TrkPaAtmRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 3, 1, 1)
)
trkPaAtmRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaIndex"),
    (0, "Nortel-Magellan-Passport-PorsAtmTrunksMIB", "trkPaAtmIndex"),
)
if mibBuilder.loadTexts:
    trkPaAtmRowStatusEntry.setStatus("mandatory")
_TrkPaAtmRowStatus_Type = RowStatus
_TrkPaAtmRowStatus_Object = MibTableColumn
trkPaAtmRowStatus = _TrkPaAtmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 3, 1, 1, 1),
    _TrkPaAtmRowStatus_Type()
)
trkPaAtmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkPaAtmRowStatus.setStatus("mandatory")
_TrkPaAtmComponentName_Type = DisplayString
_TrkPaAtmComponentName_Object = MibTableColumn
trkPaAtmComponentName = _TrkPaAtmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 3, 1, 1, 2),
    _TrkPaAtmComponentName_Type()
)
trkPaAtmComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPaAtmComponentName.setStatus("mandatory")
_TrkPaAtmStorageType_Type = StorageType
_TrkPaAtmStorageType_Object = MibTableColumn
trkPaAtmStorageType = _TrkPaAtmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 3, 1, 1, 4),
    _TrkPaAtmStorageType_Type()
)
trkPaAtmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkPaAtmStorageType.setStatus("mandatory")
_TrkPaAtmIndex_Type = NonReplicated
_TrkPaAtmIndex_Object = MibTableColumn
trkPaAtmIndex = _TrkPaAtmIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 3, 1, 1, 10),
    _TrkPaAtmIndex_Type()
)
trkPaAtmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkPaAtmIndex.setStatus("mandatory")
_TrkPaAtmProvTable_Object = MibTable
trkPaAtmProvTable = _TrkPaAtmProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 3, 10)
)
if mibBuilder.loadTexts:
    trkPaAtmProvTable.setStatus("mandatory")
_TrkPaAtmProvEntry_Object = MibTableRow
trkPaAtmProvEntry = _TrkPaAtmProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 3, 10, 1)
)
trkPaAtmProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaIndex"),
    (0, "Nortel-Magellan-Passport-PorsAtmTrunksMIB", "trkPaAtmIndex"),
)
if mibBuilder.loadTexts:
    trkPaAtmProvEntry.setStatus("mandatory")
_TrkPaAtmAtmConnection_Type = Link
_TrkPaAtmAtmConnection_Object = MibTableColumn
trkPaAtmAtmConnection = _TrkPaAtmAtmConnection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 3, 10, 1, 1),
    _TrkPaAtmAtmConnection_Type()
)
trkPaAtmAtmConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkPaAtmAtmConnection.setStatus("mandatory")


class _TrkPaAtmMode_Type(Integer32):
    """Custom type trkPaAtmMode based on Integer32"""
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


_TrkPaAtmMode_Type.__name__ = "Integer32"
_TrkPaAtmMode_Object = MibTableColumn
trkPaAtmMode = _TrkPaAtmMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 3, 10, 1, 2),
    _TrkPaAtmMode_Type()
)
trkPaAtmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkPaAtmMode.setStatus("mandatory")
_PorsAtmTrunksMIB_ObjectIdentity = ObjectIdentity
porsAtmTrunksMIB = _PorsAtmTrunksMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 137)
)
_PorsAtmTrunksGroup_ObjectIdentity = ObjectIdentity
porsAtmTrunksGroup = _PorsAtmTrunksGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 137, 1)
)
_PorsAtmTrunksGroupBE_ObjectIdentity = ObjectIdentity
porsAtmTrunksGroupBE = _PorsAtmTrunksGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 137, 1, 5)
)
_PorsAtmTrunksGroupBE01_ObjectIdentity = ObjectIdentity
porsAtmTrunksGroupBE01 = _PorsAtmTrunksGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 137, 1, 5, 2)
)
_PorsAtmTrunksGroupBE01A_ObjectIdentity = ObjectIdentity
porsAtmTrunksGroupBE01A = _PorsAtmTrunksGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 137, 1, 5, 2, 2)
)
_PorsAtmTrunksCapabilities_ObjectIdentity = ObjectIdentity
porsAtmTrunksCapabilities = _PorsAtmTrunksCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 137, 3)
)
_PorsAtmTrunksCapabilitiesBE_ObjectIdentity = ObjectIdentity
porsAtmTrunksCapabilitiesBE = _PorsAtmTrunksCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 137, 3, 5)
)
_PorsAtmTrunksCapabilitiesBE01_ObjectIdentity = ObjectIdentity
porsAtmTrunksCapabilitiesBE01 = _PorsAtmTrunksCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 137, 3, 5, 2)
)
_PorsAtmTrunksCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
porsAtmTrunksCapabilitiesBE01A = _PorsAtmTrunksCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 137, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-PorsAtmTrunksMIB",
    **{"trkPaAtm": trkPaAtm,
       "trkPaAtmRowStatusTable": trkPaAtmRowStatusTable,
       "trkPaAtmRowStatusEntry": trkPaAtmRowStatusEntry,
       "trkPaAtmRowStatus": trkPaAtmRowStatus,
       "trkPaAtmComponentName": trkPaAtmComponentName,
       "trkPaAtmStorageType": trkPaAtmStorageType,
       "trkPaAtmIndex": trkPaAtmIndex,
       "trkPaAtmProvTable": trkPaAtmProvTable,
       "trkPaAtmProvEntry": trkPaAtmProvEntry,
       "trkPaAtmAtmConnection": trkPaAtmAtmConnection,
       "trkPaAtmMode": trkPaAtmMode,
       "porsAtmTrunksMIB": porsAtmTrunksMIB,
       "porsAtmTrunksGroup": porsAtmTrunksGroup,
       "porsAtmTrunksGroupBE": porsAtmTrunksGroupBE,
       "porsAtmTrunksGroupBE01": porsAtmTrunksGroupBE01,
       "porsAtmTrunksGroupBE01A": porsAtmTrunksGroupBE01A,
       "porsAtmTrunksCapabilities": porsAtmTrunksCapabilities,
       "porsAtmTrunksCapabilitiesBE": porsAtmTrunksCapabilitiesBE,
       "porsAtmTrunksCapabilitiesBE01": porsAtmTrunksCapabilitiesBE01,
       "porsAtmTrunksCapabilitiesBE01A": porsAtmTrunksCapabilitiesBE01A}
)
