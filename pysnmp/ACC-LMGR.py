# SNMP MIB module (ACC-LMGR) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-LMGR
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:31 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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

_AccLmgr_ObjectIdentity = ObjectIdentity
accLmgr = _AccLmgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 78)
)
_AccLicMgrParms_ObjectIdentity = ObjectIdentity
accLicMgrParms = _AccLicMgrParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 78, 1)
)


class _AccLicMgrMessageLevel_Type(Integer32):
    """Custom type accLicMgrMessageLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccLicMgrMessageLevel_Type.__name__ = "Integer32"
_AccLicMgrMessageLevel_Object = MibScalar
accLicMgrMessageLevel = _AccLicMgrMessageLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 78, 1, 1),
    _AccLicMgrMessageLevel_Type()
)
accLicMgrMessageLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accLicMgrMessageLevel.setStatus("mandatory")
_AccLicMgrParmTable_Object = MibTable
accLicMgrParmTable = _AccLicMgrParmTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 78, 2)
)
if mibBuilder.loadTexts:
    accLicMgrParmTable.setStatus("mandatory")
_AccLicMgrParmEntry_Object = MibTableRow
accLicMgrParmEntry = _AccLicMgrParmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 78, 2, 1)
)
accLicMgrParmEntry.setIndexNames(
    (0, "ACC-LMGR", "pysmiFakeCol1"),
)
if mibBuilder.loadTexts:
    accLicMgrParmEntry.setStatus("mandatory")


class _AccLicMgrLictype_Type(Integer32):
    """Custom type accLicMgrLictype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(53,
              78,
              86)
        )
    )
    namedValues = NamedValues(
        *(("acc56k", 53),
          ("none", 78),
          ("voip", 86))
    )


_AccLicMgrLictype_Type.__name__ = "Integer32"
_AccLicMgrLictype_Object = MibTableColumn
accLicMgrLictype = _AccLicMgrLictype_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 78, 2, 1, 1),
    _AccLicMgrLictype_Type()
)
accLicMgrLictype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLicMgrLictype.setStatus("mandatory")


class _AccLicMgrLicGroup_Type(Integer32):
    """Custom type accLicMgrLicGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(80,
              84)
        )
    )
    namedValues = NamedValues(
        *(("standard", 84),
          ("supplemental", 80))
    )


_AccLicMgrLicGroup_Type.__name__ = "Integer32"
_AccLicMgrLicGroup_Object = MibTableColumn
accLicMgrLicGroup = _AccLicMgrLicGroup_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 78, 2, 1, 2),
    _AccLicMgrLicGroup_Type()
)
accLicMgrLicGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLicMgrLicGroup.setStatus("mandatory")
_AccLicMgrLicKey_Type = OctetString
_AccLicMgrLicKey_Object = MibTableColumn
accLicMgrLicKey = _AccLicMgrLicKey_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 78, 2, 1, 3),
    _AccLicMgrLicKey_Type()
)
accLicMgrLicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLicMgrLicKey.setStatus("mandatory")
_AccLicMgrNumInst_Type = Integer32
_AccLicMgrNumInst_Object = MibTableColumn
accLicMgrNumInst = _AccLicMgrNumInst_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 78, 2, 1, 4),
    _AccLicMgrNumInst_Type()
)
accLicMgrNumInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLicMgrNumInst.setStatus("mandatory")
_PysmiFakeCol1_Type = Integer32
_PysmiFakeCol1_Object = MibTableColumn
pysmiFakeCol1 = _PysmiFakeCol1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 78, 2, 1, 4294967295),
    _PysmiFakeCol1_Type()
)
pysmiFakeCol1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol1.setStatus("mandatory")
_AccLicMgrStatTable_Object = MibTable
accLicMgrStatTable = _AccLicMgrStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 78, 3)
)
if mibBuilder.loadTexts:
    accLicMgrStatTable.setStatus("mandatory")
_AccLicMgrStatEntry_Object = MibTableRow
accLicMgrStatEntry = _AccLicMgrStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 78, 3, 1)
)
accLicMgrStatEntry.setIndexNames(
    (0, "ACC-LMGR", "pysmiFakeCol2"),
)
if mibBuilder.loadTexts:
    accLicMgrStatEntry.setStatus("mandatory")
_AccLicMgr56kAlloc_Type = Integer32
_AccLicMgr56kAlloc_Object = MibTableColumn
accLicMgr56kAlloc = _AccLicMgr56kAlloc_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 78, 3, 1, 1),
    _AccLicMgr56kAlloc_Type()
)
accLicMgr56kAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLicMgr56kAlloc.setStatus("mandatory")
_AccLicMgr56kAvails_Type = Counter32
_AccLicMgr56kAvails_Object = MibTableColumn
accLicMgr56kAvails = _AccLicMgr56kAvails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 78, 3, 1, 2),
    _AccLicMgr56kAvails_Type()
)
accLicMgr56kAvails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLicMgr56kAvails.setStatus("mandatory")
_AccLicMgr56kCurrents_Type = Counter32
_AccLicMgr56kCurrents_Object = MibTableColumn
accLicMgr56kCurrents = _AccLicMgr56kCurrents_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 78, 3, 1, 3),
    _AccLicMgr56kCurrents_Type()
)
accLicMgr56kCurrents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLicMgr56kCurrents.setStatus("mandatory")
_AccLicMgr56kTotals_Type = Counter32
_AccLicMgr56kTotals_Object = MibTableColumn
accLicMgr56kTotals = _AccLicMgr56kTotals_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 78, 3, 1, 4),
    _AccLicMgr56kTotals_Type()
)
accLicMgr56kTotals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLicMgr56kTotals.setStatus("mandatory")
_AccLicMgr56kPeaks_Type = Counter32
_AccLicMgr56kPeaks_Object = MibTableColumn
accLicMgr56kPeaks = _AccLicMgr56kPeaks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 78, 3, 1, 5),
    _AccLicMgr56kPeaks_Type()
)
accLicMgr56kPeaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLicMgr56kPeaks.setStatus("mandatory")
_AccLicMgr56kDenials_Type = Counter32
_AccLicMgr56kDenials_Object = MibTableColumn
accLicMgr56kDenials = _AccLicMgr56kDenials_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 78, 3, 1, 6),
    _AccLicMgr56kDenials_Type()
)
accLicMgr56kDenials.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLicMgr56kDenials.setStatus("mandatory")
_AccLicMgrVoIPAllocs_Type = Counter32
_AccLicMgrVoIPAllocs_Object = MibTableColumn
accLicMgrVoIPAllocs = _AccLicMgrVoIPAllocs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 78, 3, 1, 7),
    _AccLicMgrVoIPAllocs_Type()
)
accLicMgrVoIPAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLicMgrVoIPAllocs.setStatus("mandatory")
_AccLicMgrVoIPAvails_Type = Counter32
_AccLicMgrVoIPAvails_Object = MibTableColumn
accLicMgrVoIPAvails = _AccLicMgrVoIPAvails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 78, 3, 1, 8),
    _AccLicMgrVoIPAvails_Type()
)
accLicMgrVoIPAvails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLicMgrVoIPAvails.setStatus("mandatory")
_AccLicMgrVoIPCurrents_Type = Counter32
_AccLicMgrVoIPCurrents_Object = MibTableColumn
accLicMgrVoIPCurrents = _AccLicMgrVoIPCurrents_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 78, 3, 1, 9),
    _AccLicMgrVoIPCurrents_Type()
)
accLicMgrVoIPCurrents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLicMgrVoIPCurrents.setStatus("mandatory")
_AccLicMgrVoIPTotals_Type = Counter32
_AccLicMgrVoIPTotals_Object = MibTableColumn
accLicMgrVoIPTotals = _AccLicMgrVoIPTotals_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 78, 3, 1, 10),
    _AccLicMgrVoIPTotals_Type()
)
accLicMgrVoIPTotals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLicMgrVoIPTotals.setStatus("mandatory")
_AccLicMgrVoIPPeaks_Type = Counter32
_AccLicMgrVoIPPeaks_Object = MibTableColumn
accLicMgrVoIPPeaks = _AccLicMgrVoIPPeaks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 78, 3, 1, 11),
    _AccLicMgrVoIPPeaks_Type()
)
accLicMgrVoIPPeaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLicMgrVoIPPeaks.setStatus("mandatory")
_AccLicMgrVoIPDenials_Type = Counter32
_AccLicMgrVoIPDenials_Object = MibTableColumn
accLicMgrVoIPDenials = _AccLicMgrVoIPDenials_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 78, 3, 1, 12),
    _AccLicMgrVoIPDenials_Type()
)
accLicMgrVoIPDenials.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLicMgrVoIPDenials.setStatus("mandatory")
_PysmiFakeCol2_Type = Integer32
_PysmiFakeCol2_Object = MibTableColumn
pysmiFakeCol2 = _PysmiFakeCol2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 78, 3, 1, 4294967295),
    _PysmiFakeCol2_Type()
)
pysmiFakeCol2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol2.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-LMGR",
    **{"accLmgr": accLmgr,
       "accLicMgrParms": accLicMgrParms,
       "accLicMgrMessageLevel": accLicMgrMessageLevel,
       "accLicMgrParmTable": accLicMgrParmTable,
       "accLicMgrParmEntry": accLicMgrParmEntry,
       "accLicMgrLictype": accLicMgrLictype,
       "accLicMgrLicGroup": accLicMgrLicGroup,
       "accLicMgrLicKey": accLicMgrLicKey,
       "accLicMgrNumInst": accLicMgrNumInst,
       "pysmiFakeCol1": pysmiFakeCol1,
       "accLicMgrStatTable": accLicMgrStatTable,
       "accLicMgrStatEntry": accLicMgrStatEntry,
       "accLicMgr56kAlloc": accLicMgr56kAlloc,
       "accLicMgr56kAvails": accLicMgr56kAvails,
       "accLicMgr56kCurrents": accLicMgr56kCurrents,
       "accLicMgr56kTotals": accLicMgr56kTotals,
       "accLicMgr56kPeaks": accLicMgr56kPeaks,
       "accLicMgr56kDenials": accLicMgr56kDenials,
       "accLicMgrVoIPAllocs": accLicMgrVoIPAllocs,
       "accLicMgrVoIPAvails": accLicMgrVoIPAvails,
       "accLicMgrVoIPCurrents": accLicMgrVoIPCurrents,
       "accLicMgrVoIPTotals": accLicMgrVoIPTotals,
       "accLicMgrVoIPPeaks": accLicMgrVoIPPeaks,
       "accLicMgrVoIPDenials": accLicMgrVoIPDenials,
       "pysmiFakeCol2": pysmiFakeCol2}
)
