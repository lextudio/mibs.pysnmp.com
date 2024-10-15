# SNMP MIB module (DIFFSERV-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DIFFSERV-POLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:11 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2",
    "zeroDotZero")

(DateAndTime,
 DisplayString,
 RowPointer,
 RowStatus,
 TextualConvention,
 TestAndIncr) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr")


# MODULE-IDENTITY

diffPolicyMib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 22222222)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DiffPolicyMIBObjects_ObjectIdentity = ObjectIdentity
diffPolicyMIBObjects = _DiffPolicyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22222222, 1)
)
_DiffPolicyDPCUnique_Type = TestAndIncr
_DiffPolicyDPCUnique_Object = MibScalar
diffPolicyDPCUnique = _DiffPolicyDPCUnique_Object(
    (1, 3, 6, 1, 2, 1, 22222222, 1, 1),
    _DiffPolicyDPCUnique_Type()
)
diffPolicyDPCUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffPolicyDPCUnique.setStatus("current")
_DiffPolicyDPCTable_Object = MibTable
diffPolicyDPCTable = _DiffPolicyDPCTable_Object(
    (1, 3, 6, 1, 2, 1, 22222222, 1, 2)
)
if mibBuilder.loadTexts:
    diffPolicyDPCTable.setStatus("current")
_DiffPolicyDPCEntry_Object = MibTableRow
diffPolicyDPCEntry = _DiffPolicyDPCEntry_Object(
    (1, 3, 6, 1, 2, 1, 22222222, 1, 2, 1)
)
diffPolicyDPCEntry.setIndexNames(
    (0, "DIFFSERV-POLICY-MIB", "diffPolicyDPCId"),
)
if mibBuilder.loadTexts:
    diffPolicyDPCEntry.setStatus("current")


class _DiffPolicyDPCId_Type(Integer32):
    """Custom type diffPolicyDPCId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DiffPolicyDPCId_Type.__name__ = "Integer32"
_DiffPolicyDPCId_Object = MibTableColumn
diffPolicyDPCId = _DiffPolicyDPCId_Object(
    (1, 3, 6, 1, 2, 1, 22222222, 1, 2, 1, 1),
    _DiffPolicyDPCId_Type()
)
diffPolicyDPCId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffPolicyDPCId.setStatus("current")
_DiffPolicyDPCDescr_Type = SnmpAdminString
_DiffPolicyDPCDescr_Object = MibTableColumn
diffPolicyDPCDescr = _DiffPolicyDPCDescr_Object(
    (1, 3, 6, 1, 2, 1, 22222222, 1, 2, 1, 2),
    _DiffPolicyDPCDescr_Type()
)
diffPolicyDPCDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffPolicyDPCDescr.setStatus("current")
_DiffPolicyDPCOwner_Type = SnmpAdminString
_DiffPolicyDPCOwner_Object = MibTableColumn
diffPolicyDPCOwner = _DiffPolicyDPCOwner_Object(
    (1, 3, 6, 1, 2, 1, 22222222, 1, 2, 1, 3),
    _DiffPolicyDPCOwner_Type()
)
diffPolicyDPCOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffPolicyDPCOwner.setStatus("current")
_DiffPolicyDPCLastChange_Type = DateAndTime
_DiffPolicyDPCLastChange_Object = MibTableColumn
diffPolicyDPCLastChange = _DiffPolicyDPCLastChange_Object(
    (1, 3, 6, 1, 2, 1, 22222222, 1, 2, 1, 4),
    _DiffPolicyDPCLastChange_Type()
)
diffPolicyDPCLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffPolicyDPCLastChange.setStatus("current")


class _DiffPolicyDPCConfiguration_Type(RowPointer):
    """Custom type diffPolicyDPCConfiguration based on RowPointer"""
    defaultValue = (0, 0)


_DiffPolicyDPCConfiguration_Object = MibTableColumn
diffPolicyDPCConfiguration = _DiffPolicyDPCConfiguration_Object(
    (1, 3, 6, 1, 2, 1, 22222222, 1, 2, 1, 5),
    _DiffPolicyDPCConfiguration_Type()
)
diffPolicyDPCConfiguration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffPolicyDPCConfiguration.setStatus("current")
_DiffPolicyDPCStatus_Type = RowStatus
_DiffPolicyDPCStatus_Object = MibTableColumn
diffPolicyDPCStatus = _DiffPolicyDPCStatus_Object(
    (1, 3, 6, 1, 2, 1, 22222222, 1, 2, 1, 11),
    _DiffPolicyDPCStatus_Type()
)
diffPolicyDPCStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffPolicyDPCStatus.setStatus("current")
_DiffPolicyMIBConformance_ObjectIdentity = ObjectIdentity
diffPolicyMIBConformance = _DiffPolicyMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22222222, 2)
)
_DiffPolicyMIBCompliances_ObjectIdentity = ObjectIdentity
diffPolicyMIBCompliances = _DiffPolicyMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22222222, 2, 1)
)
_DiffPolicyMIBGroups_ObjectIdentity = ObjectIdentity
diffPolicyMIBGroups = _DiffPolicyMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22222222, 2, 2)
)

# Managed Objects groups

diffPolicyMIBDPCGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 22222222, 2, 2, 1)
)
diffPolicyMIBDPCGroup.setObjects(
      *(("DIFFSERV-POLICY-MIB", "diffPolicyDPCUnique"),
        ("DIFFSERV-POLICY-MIB", "diffPolicyDPCDescr"),
        ("DIFFSERV-POLICY-MIB", "diffPolicyDPCOwner"),
        ("DIFFSERV-POLICY-MIB", "diffPolicyDPCLastChange"),
        ("DIFFSERV-POLICY-MIB", "diffPolicyDPCConfiguration"),
        ("DIFFSERV-POLICY-MIB", "diffPolicyDPCStatus"))
)
if mibBuilder.loadTexts:
    diffPolicyMIBDPCGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

diffPolicyMIBFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 22222222, 2, 1, 1)
)
if mibBuilder.loadTexts:
    diffPolicyMIBFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIFFSERV-POLICY-MIB",
    **{"diffPolicyMib": diffPolicyMib,
       "diffPolicyMIBObjects": diffPolicyMIBObjects,
       "diffPolicyDPCUnique": diffPolicyDPCUnique,
       "diffPolicyDPCTable": diffPolicyDPCTable,
       "diffPolicyDPCEntry": diffPolicyDPCEntry,
       "diffPolicyDPCId": diffPolicyDPCId,
       "diffPolicyDPCDescr": diffPolicyDPCDescr,
       "diffPolicyDPCOwner": diffPolicyDPCOwner,
       "diffPolicyDPCLastChange": diffPolicyDPCLastChange,
       "diffPolicyDPCConfiguration": diffPolicyDPCConfiguration,
       "diffPolicyDPCStatus": diffPolicyDPCStatus,
       "diffPolicyMIBConformance": diffPolicyMIBConformance,
       "diffPolicyMIBCompliances": diffPolicyMIBCompliances,
       "diffPolicyMIBFullCompliance": diffPolicyMIBFullCompliance,
       "diffPolicyMIBGroups": diffPolicyMIBGroups,
       "diffPolicyMIBDPCGroup": diffPolicyMIBDPCGroup}
)
