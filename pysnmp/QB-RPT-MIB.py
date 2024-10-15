# SNMP MIB module (QB-RPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QB-RPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:40:45 2024
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

(qbMibs,) = mibBuilder.importSymbols(
    "QUANTUMBRIDGE-REG",
    "qbMibs")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

qbSysRptMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QbSysRptObjects_ObjectIdentity = ObjectIdentity
qbSysRptObjects = _QbSysRptObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 8, 1)
)
_QbSysRptTables_ObjectIdentity = ObjectIdentity
qbSysRptTables = _QbSysRptTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 8, 2)
)
_QbSysRptTable_Object = MibTable
qbSysRptTable = _QbSysRptTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 8, 2, 1)
)
if mibBuilder.loadTexts:
    qbSysRptTable.setStatus("current")
_QbSysRptEntry_Object = MibTableRow
qbSysRptEntry = _QbSysRptEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 8, 2, 1, 1)
)
qbSysRptEntry.setIndexNames(
    (0, "QB-RPT-MIB", "qbSysRptId"),
    (0, "QB-RPT-MIB", "qbSysAid"),
    (0, "QB-RPT-MIB", "qbSysArg1"),
    (0, "QB-RPT-MIB", "qbSysArg2"),
    (0, "QB-RPT-MIB", "qbSysArg3"),
    (0, "QB-RPT-MIB", "qbSysArg4"),
    (0, "QB-RPT-MIB", "qbSysArg5"),
)
if mibBuilder.loadTexts:
    qbSysRptEntry.setStatus("current")
_QbSysRptId_Type = Integer32
_QbSysRptId_Object = MibTableColumn
qbSysRptId = _QbSysRptId_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 8, 2, 1, 1, 1),
    _QbSysRptId_Type()
)
qbSysRptId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbSysRptId.setStatus("current")
_QbSysAid_Type = Unsigned32
_QbSysAid_Object = MibTableColumn
qbSysAid = _QbSysAid_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 8, 2, 1, 1, 2),
    _QbSysAid_Type()
)
qbSysAid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbSysAid.setStatus("current")
_QbSysArg1_Type = Integer32
_QbSysArg1_Object = MibTableColumn
qbSysArg1 = _QbSysArg1_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 8, 2, 1, 1, 3),
    _QbSysArg1_Type()
)
qbSysArg1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysArg1.setStatus("current")
_QbSysArg2_Type = Integer32
_QbSysArg2_Object = MibTableColumn
qbSysArg2 = _QbSysArg2_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 8, 2, 1, 1, 4),
    _QbSysArg2_Type()
)
qbSysArg2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysArg2.setStatus("current")
_QbSysArg3_Type = Integer32
_QbSysArg3_Object = MibTableColumn
qbSysArg3 = _QbSysArg3_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 8, 2, 1, 1, 5),
    _QbSysArg3_Type()
)
qbSysArg3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysArg3.setStatus("current")
_QbSysArg4_Type = Integer32
_QbSysArg4_Object = MibTableColumn
qbSysArg4 = _QbSysArg4_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 8, 2, 1, 1, 6),
    _QbSysArg4_Type()
)
qbSysArg4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysArg4.setStatus("current")
_QbSysArg5_Type = Integer32
_QbSysArg5_Object = MibTableColumn
qbSysArg5 = _QbSysArg5_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 8, 2, 1, 1, 7),
    _QbSysArg5_Type()
)
qbSysArg5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysArg5.setStatus("current")
_QbSysRptSize_Type = Integer32
_QbSysRptSize_Object = MibTableColumn
qbSysRptSize = _QbSysRptSize_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 8, 2, 1, 1, 8),
    _QbSysRptSize_Type()
)
qbSysRptSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysRptSize.setStatus("current")
if mibBuilder.loadTexts:
    qbSysRptSize.setUnits("bytes")
_QbSysRpt_Type = Integer32
_QbSysRpt_Object = MibTableColumn
qbSysRpt = _QbSysRpt_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 8, 2, 1, 1, 9),
    _QbSysRpt_Type()
)
qbSysRpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysRpt.setStatus("current")
_QbSysRptConformance_ObjectIdentity = ObjectIdentity
qbSysRptConformance = _QbSysRptConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 8, 3)
)
_QbSysRptCompliances_ObjectIdentity = ObjectIdentity
qbSysRptCompliances = _QbSysRptCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 8, 3, 1)
)
_QbSysRptGroups_ObjectIdentity = ObjectIdentity
qbSysRptGroups = _QbSysRptGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 8, 3, 2)
)

# Managed Objects groups

qbSysRptAllGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 8, 3, 2, 1)
)
qbSysRptAllGroup.setObjects(
      *(("QB-RPT-MIB", "qbSysRptSize"),
        ("QB-RPT-MIB", "qbSysRpt"))
)
if mibBuilder.loadTexts:
    qbSysRptAllGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qbSysRptCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4323, 2, 8, 3, 1, 1)
)
if mibBuilder.loadTexts:
    qbSysRptCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QB-RPT-MIB",
    **{"qbSysRptMIB": qbSysRptMIB,
       "qbSysRptObjects": qbSysRptObjects,
       "qbSysRptTables": qbSysRptTables,
       "qbSysRptTable": qbSysRptTable,
       "qbSysRptEntry": qbSysRptEntry,
       "qbSysRptId": qbSysRptId,
       "qbSysAid": qbSysAid,
       "qbSysArg1": qbSysArg1,
       "qbSysArg2": qbSysArg2,
       "qbSysArg3": qbSysArg3,
       "qbSysArg4": qbSysArg4,
       "qbSysArg5": qbSysArg5,
       "qbSysRptSize": qbSysRptSize,
       "qbSysRpt": qbSysRpt,
       "qbSysRptConformance": qbSysRptConformance,
       "qbSysRptCompliances": qbSysRptCompliances,
       "qbSysRptCompliance": qbSysRptCompliance,
       "qbSysRptGroups": qbSysRptGroups,
       "qbSysRptAllGroup": qbSysRptAllGroup}
)
