# SNMP MIB module (CISCO-ATM-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ATM-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:51 2024
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

(aal5VccEntry,
 atmVclEntry) = mibBuilder.importSymbols(
    "ATM-MIB",
    "aal5VccEntry",
    "atmVclEntry")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoAtmExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 88)
)
ciscoAtmExtMIB.setRevisions(
        ("2003-01-06 00:00",
         "1997-06-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class OamCCStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 4),
          ("ready", 1),
          ("waitActiveConfirm", 3),
          ("waitActiveResponse", 2),
          ("waitDeactiveConfirm", 5))
    )



class OamCCVcState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aisrdi", 2),
          ("notManaged", 3),
          ("verified", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoAtmExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAtmExtMIBObjects = _CiscoAtmExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1)
)
_CAal5VccExtMIBObjects_ObjectIdentity = ObjectIdentity
cAal5VccExtMIBObjects = _CAal5VccExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 1)
)
_CAal5VccExtTable_Object = MibTable
cAal5VccExtTable = _CAal5VccExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cAal5VccExtTable.setStatus("current")
_CAal5VccExtEntry_Object = MibTableRow
cAal5VccExtEntry = _CAal5VccExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cAal5VccExtEntry.setStatus("current")
_CAal5VccExtCompEnabled_Type = TruthValue
_CAal5VccExtCompEnabled_Object = MibTableColumn
cAal5VccExtCompEnabled = _CAal5VccExtCompEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 1, 1, 1, 1),
    _CAal5VccExtCompEnabled_Type()
)
cAal5VccExtCompEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAal5VccExtCompEnabled.setStatus("current")
_CAal5VccExtVoice_Type = TruthValue
_CAal5VccExtVoice_Object = MibTableColumn
cAal5VccExtVoice = _CAal5VccExtVoice_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 1, 1, 1, 2),
    _CAal5VccExtVoice_Type()
)
cAal5VccExtVoice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAal5VccExtVoice.setStatus("current")
_CAal5VccExtInF5OamCells_Type = Counter32
_CAal5VccExtInF5OamCells_Object = MibTableColumn
cAal5VccExtInF5OamCells = _CAal5VccExtInF5OamCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 1, 1, 1, 3),
    _CAal5VccExtInF5OamCells_Type()
)
cAal5VccExtInF5OamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAal5VccExtInF5OamCells.setStatus("current")
_CAal5VccExtOutF5OamCells_Type = Counter32
_CAal5VccExtOutF5OamCells_Object = MibTableColumn
cAal5VccExtOutF5OamCells = _CAal5VccExtOutF5OamCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 1, 1, 1, 4),
    _CAal5VccExtOutF5OamCells_Type()
)
cAal5VccExtOutF5OamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAal5VccExtOutF5OamCells.setStatus("current")
_CatmxVcl_ObjectIdentity = ObjectIdentity
catmxVcl = _CatmxVcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 2)
)
_CatmxVclOamTable_Object = MibTable
catmxVclOamTable = _CatmxVclOamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 2, 1)
)
if mibBuilder.loadTexts:
    catmxVclOamTable.setStatus("current")
_CatmxVclOamEntry_Object = MibTableRow
catmxVclOamEntry = _CatmxVclOamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    catmxVclOamEntry.setStatus("current")
_CatmxVclOamLoopbackFreq_Type = Unsigned32
_CatmxVclOamLoopbackFreq_Object = MibTableColumn
catmxVclOamLoopbackFreq = _CatmxVclOamLoopbackFreq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 2, 1, 1, 1),
    _CatmxVclOamLoopbackFreq_Type()
)
catmxVclOamLoopbackFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    catmxVclOamLoopbackFreq.setStatus("current")
if mibBuilder.loadTexts:
    catmxVclOamLoopbackFreq.setUnits("seconds")
_CatmxVclOamRetryFreq_Type = Unsigned32
_CatmxVclOamRetryFreq_Object = MibTableColumn
catmxVclOamRetryFreq = _CatmxVclOamRetryFreq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 2, 1, 1, 2),
    _CatmxVclOamRetryFreq_Type()
)
catmxVclOamRetryFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    catmxVclOamRetryFreq.setStatus("current")
if mibBuilder.loadTexts:
    catmxVclOamRetryFreq.setUnits("seconds")
_CatmxVclOamUpRetryCount_Type = Unsigned32
_CatmxVclOamUpRetryCount_Object = MibTableColumn
catmxVclOamUpRetryCount = _CatmxVclOamUpRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 2, 1, 1, 3),
    _CatmxVclOamUpRetryCount_Type()
)
catmxVclOamUpRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    catmxVclOamUpRetryCount.setStatus("current")
_CatmxVclOamDownRetryCount_Type = Unsigned32
_CatmxVclOamDownRetryCount_Object = MibTableColumn
catmxVclOamDownRetryCount = _CatmxVclOamDownRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 2, 1, 1, 4),
    _CatmxVclOamDownRetryCount_Type()
)
catmxVclOamDownRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    catmxVclOamDownRetryCount.setStatus("current")
_CatmxVclOamEndCCActCount_Type = Unsigned32
_CatmxVclOamEndCCActCount_Object = MibTableColumn
catmxVclOamEndCCActCount = _CatmxVclOamEndCCActCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 2, 1, 1, 5),
    _CatmxVclOamEndCCActCount_Type()
)
catmxVclOamEndCCActCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    catmxVclOamEndCCActCount.setStatus("current")
_CatmxVclOamEndCCDeActCount_Type = Unsigned32
_CatmxVclOamEndCCDeActCount_Object = MibTableColumn
catmxVclOamEndCCDeActCount = _CatmxVclOamEndCCDeActCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 2, 1, 1, 6),
    _CatmxVclOamEndCCDeActCount_Type()
)
catmxVclOamEndCCDeActCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    catmxVclOamEndCCDeActCount.setStatus("current")
_CatmxVclOamEndCCRetryFreq_Type = Unsigned32
_CatmxVclOamEndCCRetryFreq_Object = MibTableColumn
catmxVclOamEndCCRetryFreq = _CatmxVclOamEndCCRetryFreq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 2, 1, 1, 7),
    _CatmxVclOamEndCCRetryFreq_Type()
)
catmxVclOamEndCCRetryFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    catmxVclOamEndCCRetryFreq.setStatus("current")
if mibBuilder.loadTexts:
    catmxVclOamEndCCRetryFreq.setUnits("seconds")
_CatmxVclOamSegCCActCount_Type = Unsigned32
_CatmxVclOamSegCCActCount_Object = MibTableColumn
catmxVclOamSegCCActCount = _CatmxVclOamSegCCActCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 2, 1, 1, 8),
    _CatmxVclOamSegCCActCount_Type()
)
catmxVclOamSegCCActCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    catmxVclOamSegCCActCount.setStatus("current")
_CatmxVclOamSegCCDeActCount_Type = Unsigned32
_CatmxVclOamSegCCDeActCount_Object = MibTableColumn
catmxVclOamSegCCDeActCount = _CatmxVclOamSegCCDeActCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 2, 1, 1, 9),
    _CatmxVclOamSegCCDeActCount_Type()
)
catmxVclOamSegCCDeActCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    catmxVclOamSegCCDeActCount.setStatus("current")
_CatmxVclOamSegCCRetryFreq_Type = Unsigned32
_CatmxVclOamSegCCRetryFreq_Object = MibTableColumn
catmxVclOamSegCCRetryFreq = _CatmxVclOamSegCCRetryFreq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 2, 1, 1, 10),
    _CatmxVclOamSegCCRetryFreq_Type()
)
catmxVclOamSegCCRetryFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    catmxVclOamSegCCRetryFreq.setStatus("current")
if mibBuilder.loadTexts:
    catmxVclOamSegCCRetryFreq.setUnits("seconds")


class _CatmxVclOamManage_Type(TruthValue):
    """Custom type catmxVclOamManage based on TruthValue"""


_CatmxVclOamManage_Object = MibTableColumn
catmxVclOamManage = _CatmxVclOamManage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 2, 1, 1, 11),
    _CatmxVclOamManage_Type()
)
catmxVclOamManage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    catmxVclOamManage.setStatus("current")


class _CatmxVclOamLoopBkStatus_Type(Integer32):
    """Custom type catmxVclOamLoopBkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("failed", 4),
          ("received", 3),
          ("sent", 2))
    )


_CatmxVclOamLoopBkStatus_Type.__name__ = "Integer32"
_CatmxVclOamLoopBkStatus_Object = MibTableColumn
catmxVclOamLoopBkStatus = _CatmxVclOamLoopBkStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 2, 1, 1, 12),
    _CatmxVclOamLoopBkStatus_Type()
)
catmxVclOamLoopBkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmxVclOamLoopBkStatus.setStatus("current")


class _CatmxVclOamVcState_Type(Integer32):
    """Custom type catmxVclOamVcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("aisOut", 6),
          ("aisRDI", 5),
          ("downRetry", 1),
          ("notManaged", 7),
          ("notVerified", 3),
          ("upRetry", 4),
          ("verified", 2))
    )


_CatmxVclOamVcState_Type.__name__ = "Integer32"
_CatmxVclOamVcState_Object = MibTableColumn
catmxVclOamVcState = _CatmxVclOamVcState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 2, 1, 1, 13),
    _CatmxVclOamVcState_Type()
)
catmxVclOamVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmxVclOamVcState.setStatus("current")
_CatmxVclOamEndCCStatus_Type = OamCCStatus
_CatmxVclOamEndCCStatus_Object = MibTableColumn
catmxVclOamEndCCStatus = _CatmxVclOamEndCCStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 2, 1, 1, 14),
    _CatmxVclOamEndCCStatus_Type()
)
catmxVclOamEndCCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmxVclOamEndCCStatus.setStatus("current")
_CatmxVclOamSegCCStatus_Type = OamCCStatus
_CatmxVclOamSegCCStatus_Object = MibTableColumn
catmxVclOamSegCCStatus = _CatmxVclOamSegCCStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 2, 1, 1, 15),
    _CatmxVclOamSegCCStatus_Type()
)
catmxVclOamSegCCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmxVclOamSegCCStatus.setStatus("current")
_CatmxVclOamEndCCVcState_Type = OamCCVcState
_CatmxVclOamEndCCVcState_Object = MibTableColumn
catmxVclOamEndCCVcState = _CatmxVclOamEndCCVcState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 2, 1, 1, 16),
    _CatmxVclOamEndCCVcState_Type()
)
catmxVclOamEndCCVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmxVclOamEndCCVcState.setStatus("current")
_CatmxVclOamSegCCVcState_Type = OamCCVcState
_CatmxVclOamSegCCVcState_Object = MibTableColumn
catmxVclOamSegCCVcState = _CatmxVclOamSegCCVcState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 2, 1, 1, 17),
    _CatmxVclOamSegCCVcState_Type()
)
catmxVclOamSegCCVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmxVclOamSegCCVcState.setStatus("current")
_CatmxVclOamCellsReceived_Type = Counter32
_CatmxVclOamCellsReceived_Object = MibTableColumn
catmxVclOamCellsReceived = _CatmxVclOamCellsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 2, 1, 1, 18),
    _CatmxVclOamCellsReceived_Type()
)
catmxVclOamCellsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmxVclOamCellsReceived.setStatus("current")
if mibBuilder.loadTexts:
    catmxVclOamCellsReceived.setUnits("cells")
_CatmxVclOamCellsSent_Type = Counter32
_CatmxVclOamCellsSent_Object = MibTableColumn
catmxVclOamCellsSent = _CatmxVclOamCellsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 2, 1, 1, 19),
    _CatmxVclOamCellsSent_Type()
)
catmxVclOamCellsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmxVclOamCellsSent.setStatus("current")
if mibBuilder.loadTexts:
    catmxVclOamCellsSent.setUnits("cells")
_CatmxVclOamCellsDropped_Type = Counter32
_CatmxVclOamCellsDropped_Object = MibTableColumn
catmxVclOamCellsDropped = _CatmxVclOamCellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 2, 1, 1, 20),
    _CatmxVclOamCellsDropped_Type()
)
catmxVclOamCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmxVclOamCellsDropped.setStatus("current")
if mibBuilder.loadTexts:
    catmxVclOamCellsDropped.setUnits("cells")
_CatmxVclOamInF5ais_Type = Counter32
_CatmxVclOamInF5ais_Object = MibTableColumn
catmxVclOamInF5ais = _CatmxVclOamInF5ais_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 2, 1, 1, 21),
    _CatmxVclOamInF5ais_Type()
)
catmxVclOamInF5ais.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmxVclOamInF5ais.setStatus("current")
if mibBuilder.loadTexts:
    catmxVclOamInF5ais.setUnits("cells")
_CatmxVclOamOutF5ais_Type = Counter32
_CatmxVclOamOutF5ais_Object = MibTableColumn
catmxVclOamOutF5ais = _CatmxVclOamOutF5ais_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 2, 1, 1, 22),
    _CatmxVclOamOutF5ais_Type()
)
catmxVclOamOutF5ais.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmxVclOamOutF5ais.setStatus("current")
if mibBuilder.loadTexts:
    catmxVclOamOutF5ais.setUnits("cells")
_CatmxVclOamInF5rdi_Type = Counter32
_CatmxVclOamInF5rdi_Object = MibTableColumn
catmxVclOamInF5rdi = _CatmxVclOamInF5rdi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 2, 1, 1, 23),
    _CatmxVclOamInF5rdi_Type()
)
catmxVclOamInF5rdi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmxVclOamInF5rdi.setStatus("current")
if mibBuilder.loadTexts:
    catmxVclOamInF5rdi.setUnits("cells")
_CatmxVclOamOutF5rdi_Type = Counter32
_CatmxVclOamOutF5rdi_Object = MibTableColumn
catmxVclOamOutF5rdi = _CatmxVclOamOutF5rdi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 1, 2, 1, 1, 24),
    _CatmxVclOamOutF5rdi_Type()
)
catmxVclOamOutF5rdi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmxVclOamOutF5rdi.setStatus("current")
if mibBuilder.loadTexts:
    catmxVclOamOutF5rdi.setUnits("cells")
_CiscoAal5ExtMIBConformance_ObjectIdentity = ObjectIdentity
ciscoAal5ExtMIBConformance = _CiscoAal5ExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 2)
)
_CiscoAal5ExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAal5ExtMIBCompliances = _CiscoAal5ExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 2, 1)
)
_CiscoAal5ExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoAal5ExtMIBGroups = _CiscoAal5ExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 2, 2)
)
aal5VccEntry.registerAugmentions(
    ("CISCO-ATM-EXT-MIB",
     "cAal5VccExtEntry")
)
cAal5VccExtEntry.setIndexNames(*aal5VccEntry.getIndexNames())
atmVclEntry.registerAugmentions(
    ("CISCO-ATM-EXT-MIB",
     "catmxVclOamEntry")
)
catmxVclOamEntry.setIndexNames(*atmVclEntry.getIndexNames())

# Managed Objects groups

ciscoAal5ExtMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 2, 2, 1)
)
ciscoAal5ExtMIBGroup.setObjects(
      *(("CISCO-ATM-EXT-MIB", "cAal5VccExtCompEnabled"),
        ("CISCO-ATM-EXT-MIB", "cAal5VccExtVoice"),
        ("CISCO-ATM-EXT-MIB", "cAal5VccExtInF5OamCells"),
        ("CISCO-ATM-EXT-MIB", "cAal5VccExtOutF5OamCells"))
)
if mibBuilder.loadTexts:
    ciscoAal5ExtMIBGroup.setStatus("current")

ciscoAtmExtVclOamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 2, 2, 2)
)
ciscoAtmExtVclOamGroup.setObjects(
      *(("CISCO-ATM-EXT-MIB", "catmxVclOamLoopbackFreq"),
        ("CISCO-ATM-EXT-MIB", "catmxVclOamRetryFreq"),
        ("CISCO-ATM-EXT-MIB", "catmxVclOamUpRetryCount"),
        ("CISCO-ATM-EXT-MIB", "catmxVclOamDownRetryCount"),
        ("CISCO-ATM-EXT-MIB", "catmxVclOamEndCCActCount"),
        ("CISCO-ATM-EXT-MIB", "catmxVclOamEndCCDeActCount"),
        ("CISCO-ATM-EXT-MIB", "catmxVclOamEndCCRetryFreq"),
        ("CISCO-ATM-EXT-MIB", "catmxVclOamSegCCActCount"),
        ("CISCO-ATM-EXT-MIB", "catmxVclOamSegCCDeActCount"),
        ("CISCO-ATM-EXT-MIB", "catmxVclOamSegCCRetryFreq"),
        ("CISCO-ATM-EXT-MIB", "catmxVclOamManage"),
        ("CISCO-ATM-EXT-MIB", "catmxVclOamLoopBkStatus"),
        ("CISCO-ATM-EXT-MIB", "catmxVclOamVcState"),
        ("CISCO-ATM-EXT-MIB", "catmxVclOamEndCCStatus"),
        ("CISCO-ATM-EXT-MIB", "catmxVclOamSegCCStatus"),
        ("CISCO-ATM-EXT-MIB", "catmxVclOamEndCCVcState"),
        ("CISCO-ATM-EXT-MIB", "catmxVclOamSegCCVcState"),
        ("CISCO-ATM-EXT-MIB", "catmxVclOamCellsReceived"),
        ("CISCO-ATM-EXT-MIB", "catmxVclOamCellsSent"),
        ("CISCO-ATM-EXT-MIB", "catmxVclOamCellsDropped"),
        ("CISCO-ATM-EXT-MIB", "catmxVclOamInF5ais"),
        ("CISCO-ATM-EXT-MIB", "catmxVclOamOutF5ais"),
        ("CISCO-ATM-EXT-MIB", "catmxVclOamInF5rdi"),
        ("CISCO-ATM-EXT-MIB", "catmxVclOamOutF5rdi"))
)
if mibBuilder.loadTexts:
    ciscoAtmExtVclOamGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoAal5ExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAal5ExtMIBCompliance.setStatus(
        "deprecated"
    )

ciscoAal5ExtMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 88, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoAal5ExtMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ATM-EXT-MIB",
    **{"OamCCStatus": OamCCStatus,
       "OamCCVcState": OamCCVcState,
       "ciscoAtmExtMIB": ciscoAtmExtMIB,
       "ciscoAtmExtMIBObjects": ciscoAtmExtMIBObjects,
       "cAal5VccExtMIBObjects": cAal5VccExtMIBObjects,
       "cAal5VccExtTable": cAal5VccExtTable,
       "cAal5VccExtEntry": cAal5VccExtEntry,
       "cAal5VccExtCompEnabled": cAal5VccExtCompEnabled,
       "cAal5VccExtVoice": cAal5VccExtVoice,
       "cAal5VccExtInF5OamCells": cAal5VccExtInF5OamCells,
       "cAal5VccExtOutF5OamCells": cAal5VccExtOutF5OamCells,
       "catmxVcl": catmxVcl,
       "catmxVclOamTable": catmxVclOamTable,
       "catmxVclOamEntry": catmxVclOamEntry,
       "catmxVclOamLoopbackFreq": catmxVclOamLoopbackFreq,
       "catmxVclOamRetryFreq": catmxVclOamRetryFreq,
       "catmxVclOamUpRetryCount": catmxVclOamUpRetryCount,
       "catmxVclOamDownRetryCount": catmxVclOamDownRetryCount,
       "catmxVclOamEndCCActCount": catmxVclOamEndCCActCount,
       "catmxVclOamEndCCDeActCount": catmxVclOamEndCCDeActCount,
       "catmxVclOamEndCCRetryFreq": catmxVclOamEndCCRetryFreq,
       "catmxVclOamSegCCActCount": catmxVclOamSegCCActCount,
       "catmxVclOamSegCCDeActCount": catmxVclOamSegCCDeActCount,
       "catmxVclOamSegCCRetryFreq": catmxVclOamSegCCRetryFreq,
       "catmxVclOamManage": catmxVclOamManage,
       "catmxVclOamLoopBkStatus": catmxVclOamLoopBkStatus,
       "catmxVclOamVcState": catmxVclOamVcState,
       "catmxVclOamEndCCStatus": catmxVclOamEndCCStatus,
       "catmxVclOamSegCCStatus": catmxVclOamSegCCStatus,
       "catmxVclOamEndCCVcState": catmxVclOamEndCCVcState,
       "catmxVclOamSegCCVcState": catmxVclOamSegCCVcState,
       "catmxVclOamCellsReceived": catmxVclOamCellsReceived,
       "catmxVclOamCellsSent": catmxVclOamCellsSent,
       "catmxVclOamCellsDropped": catmxVclOamCellsDropped,
       "catmxVclOamInF5ais": catmxVclOamInF5ais,
       "catmxVclOamOutF5ais": catmxVclOamOutF5ais,
       "catmxVclOamInF5rdi": catmxVclOamInF5rdi,
       "catmxVclOamOutF5rdi": catmxVclOamOutF5rdi,
       "ciscoAal5ExtMIBConformance": ciscoAal5ExtMIBConformance,
       "ciscoAal5ExtMIBCompliances": ciscoAal5ExtMIBCompliances,
       "ciscoAal5ExtMIBCompliance": ciscoAal5ExtMIBCompliance,
       "ciscoAal5ExtMIBComplianceRev1": ciscoAal5ExtMIBComplianceRev1,
       "ciscoAal5ExtMIBGroups": ciscoAal5ExtMIBGroups,
       "ciscoAal5ExtMIBGroup": ciscoAal5ExtMIBGroup,
       "ciscoAtmExtVclOamGroup": ciscoAtmExtVclOamGroup}
)
