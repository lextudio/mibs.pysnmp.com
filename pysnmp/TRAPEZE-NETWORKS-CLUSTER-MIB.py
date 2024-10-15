# SNMP MIB module (TRAPEZE-NETWORKS-CLUSTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRAPEZE-NETWORKS-CLUSTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:31 2024
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

(TrpzApNum,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-AP-TC",
    "TrpzApNum")

(trpzMibs,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-ROOT-MIB",
    "trpzMibs")


# MODULE-IDENTITY

trpzClusterMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 21)
)
trpzClusterMib.setRevisions(
        ("2011-02-24 00:01",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TrpzClusterMibObjects_ObjectIdentity = ObjectIdentity
trpzClusterMibObjects = _TrpzClusterMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 21, 1)
)
_TrpzClusterApAssignmentTable_Object = MibTable
trpzClusterApAssignmentTable = _TrpzClusterApAssignmentTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 21, 1, 1)
)
if mibBuilder.loadTexts:
    trpzClusterApAssignmentTable.setStatus("current")
_TrpzClusterApAssignmentEntry_Object = MibTableRow
trpzClusterApAssignmentEntry = _TrpzClusterApAssignmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 21, 1, 1, 1)
)
trpzClusterApAssignmentEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-CLUSTER-MIB", "trpzClusterApAssignApNum"),
)
if mibBuilder.loadTexts:
    trpzClusterApAssignmentEntry.setStatus("current")
_TrpzClusterApAssignApNum_Type = TrpzApNum
_TrpzClusterApAssignApNum_Object = MibTableColumn
trpzClusterApAssignApNum = _TrpzClusterApAssignApNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 21, 1, 1, 1, 1),
    _TrpzClusterApAssignApNum_Type()
)
trpzClusterApAssignApNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzClusterApAssignApNum.setStatus("current")
_TrpzClusterApAssignPamIp_Type = IpAddress
_TrpzClusterApAssignPamIp_Object = MibTableColumn
trpzClusterApAssignPamIp = _TrpzClusterApAssignPamIp_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 21, 1, 1, 1, 2),
    _TrpzClusterApAssignPamIp_Type()
)
trpzClusterApAssignPamIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClusterApAssignPamIp.setStatus("current")
_TrpzClusterApAssignSamIp_Type = IpAddress
_TrpzClusterApAssignSamIp_Object = MibTableColumn
trpzClusterApAssignSamIp = _TrpzClusterApAssignSamIp_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 21, 1, 1, 1, 3),
    _TrpzClusterApAssignSamIp_Type()
)
trpzClusterApAssignSamIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClusterApAssignSamIp.setStatus("current")
_TrpzClusterApAssignConnectedToPam_Type = TruthValue
_TrpzClusterApAssignConnectedToPam_Object = MibTableColumn
trpzClusterApAssignConnectedToPam = _TrpzClusterApAssignConnectedToPam_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 21, 1, 1, 1, 4),
    _TrpzClusterApAssignConnectedToPam_Type()
)
trpzClusterApAssignConnectedToPam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClusterApAssignConnectedToPam.setStatus("current")
_TrpzClusterApAssignConnectedToSam_Type = TruthValue
_TrpzClusterApAssignConnectedToSam_Object = MibTableColumn
trpzClusterApAssignConnectedToSam = _TrpzClusterApAssignConnectedToSam_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 21, 1, 1, 1, 5),
    _TrpzClusterApAssignConnectedToSam_Type()
)
trpzClusterApAssignConnectedToSam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClusterApAssignConnectedToSam.setStatus("current")
_TrpzClusterConformance_ObjectIdentity = ObjectIdentity
trpzClusterConformance = _TrpzClusterConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 21, 2)
)
_TrpzClusterCompliances_ObjectIdentity = ObjectIdentity
trpzClusterCompliances = _TrpzClusterCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 21, 2, 1)
)
_TrpzClusterGroups_ObjectIdentity = ObjectIdentity
trpzClusterGroups = _TrpzClusterGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 21, 2, 2)
)

# Managed Objects groups

trpzClusterApAssignmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 21, 2, 2, 1)
)
trpzClusterApAssignmentGroup.setObjects(
      *(("TRAPEZE-NETWORKS-CLUSTER-MIB", "trpzClusterApAssignPamIp"),
        ("TRAPEZE-NETWORKS-CLUSTER-MIB", "trpzClusterApAssignSamIp"),
        ("TRAPEZE-NETWORKS-CLUSTER-MIB", "trpzClusterApAssignConnectedToPam"),
        ("TRAPEZE-NETWORKS-CLUSTER-MIB", "trpzClusterApAssignConnectedToSam"))
)
if mibBuilder.loadTexts:
    trpzClusterApAssignmentGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

trpzClusterCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14525, 4, 21, 2, 1, 1)
)
if mibBuilder.loadTexts:
    trpzClusterCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRAPEZE-NETWORKS-CLUSTER-MIB",
    **{"trpzClusterMib": trpzClusterMib,
       "trpzClusterMibObjects": trpzClusterMibObjects,
       "trpzClusterApAssignmentTable": trpzClusterApAssignmentTable,
       "trpzClusterApAssignmentEntry": trpzClusterApAssignmentEntry,
       "trpzClusterApAssignApNum": trpzClusterApAssignApNum,
       "trpzClusterApAssignPamIp": trpzClusterApAssignPamIp,
       "trpzClusterApAssignSamIp": trpzClusterApAssignSamIp,
       "trpzClusterApAssignConnectedToPam": trpzClusterApAssignConnectedToPam,
       "trpzClusterApAssignConnectedToSam": trpzClusterApAssignConnectedToSam,
       "trpzClusterConformance": trpzClusterConformance,
       "trpzClusterCompliances": trpzClusterCompliances,
       "trpzClusterCompliance": trpzClusterCompliance,
       "trpzClusterGroups": trpzClusterGroups,
       "trpzClusterApAssignmentGroup": trpzClusterApAssignmentGroup}
)
