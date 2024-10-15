# SNMP MIB module (HP-ICF-SFLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-SFLOW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:09 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(sFlowFsDataSource,
 sFlowFsInstance,
 sFlowRcvrEntry) = mibBuilder.importSymbols(
    "SFLOW-MIB",
    "sFlowFsDataSource",
    "sFlowFsInstance",
    "sFlowRcvrEntry")

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

hpicfSflowMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92)
)
hpicfSflowMIB.setRevisions(
        ("2012-08-22 00:00",
         "2012-04-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfSflowNotifications_ObjectIdentity = ObjectIdentity
hpicfSflowNotifications = _HpicfSflowNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 0)
)
_HpicfSflowObjects_ObjectIdentity = ObjectIdentity
hpicfSflowObjects = _HpicfSflowObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 1)
)
_HpicfSflowInfo_ObjectIdentity = ObjectIdentity
hpicfSflowInfo = _HpicfSflowInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 1, 1)
)
_HpicfSflowPortInfoTable_Object = MibTable
hpicfSflowPortInfoTable = _HpicfSflowPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfSflowPortInfoTable.setStatus("current")
_HpicfSflowPortInfoEntry_Object = MibTableRow
hpicfSflowPortInfoEntry = _HpicfSflowPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 1, 1, 1, 1)
)
hpicfSflowPortInfoEntry.setIndexNames(
    (0, "SFLOW-MIB", "sFlowFsDataSource"),
    (0, "SFLOW-MIB", "sFlowFsInstance"),
)
if mibBuilder.loadTexts:
    hpicfSflowPortInfoEntry.setStatus("current")


class _HpicfSflowPortMode_Type(Integer32):
    """Custom type hpicfSflowPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("determine", 2),
          ("invalid", 1),
          ("random", 3))
    )


_HpicfSflowPortMode_Type.__name__ = "Integer32"
_HpicfSflowPortMode_Object = MibTableColumn
hpicfSflowPortMode = _HpicfSflowPortMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 1, 1, 1, 1, 1),
    _HpicfSflowPortMode_Type()
)
hpicfSflowPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSflowPortMode.setStatus("current")


class _HpicfSflowPortStatus_Type(Integer32):
    """Custom type hpicfSflowPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("invalid", 1))
    )


_HpicfSflowPortStatus_Type.__name__ = "Integer32"
_HpicfSflowPortStatus_Object = MibTableColumn
hpicfSflowPortStatus = _HpicfSflowPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 1, 1, 1, 1, 2),
    _HpicfSflowPortStatus_Type()
)
hpicfSflowPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSflowPortStatus.setStatus("current")
_HpicfSflowRcvrTable_Object = MibTable
hpicfSflowRcvrTable = _HpicfSflowRcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfSflowRcvrTable.setStatus("current")
_HpicfSflowRcvrEntry_Object = MibTableRow
hpicfSflowRcvrEntry = _HpicfSflowRcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfSflowRcvrEntry.setStatus("current")


class _HpicfSflowRcvrOobm_Type(TruthValue):
    """Custom type hpicfSflowRcvrOobm based on TruthValue"""


_HpicfSflowRcvrOobm_Object = MibTableColumn
hpicfSflowRcvrOobm = _HpicfSflowRcvrOobm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 1, 1, 2, 1, 1),
    _HpicfSflowRcvrOobm_Type()
)
hpicfSflowRcvrOobm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSflowRcvrOobm.setStatus("current")
_HpicfSflowConformance_ObjectIdentity = ObjectIdentity
hpicfSflowConformance = _HpicfSflowConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 2)
)
_HpicfSflowGroups_ObjectIdentity = ObjectIdentity
hpicfSflowGroups = _HpicfSflowGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 2, 1)
)
_HpicfSflowCompliances_ObjectIdentity = ObjectIdentity
hpicfSflowCompliances = _HpicfSflowCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 2, 2)
)
sFlowRcvrEntry.registerAugmentions(
    ("HP-ICF-SFLOW-MIB",
     "hpicfSflowRcvrEntry")
)
hpicfSflowRcvrEntry.setIndexNames(*sFlowRcvrEntry.getIndexNames())

# Managed Objects groups

hpicfSflowInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 2, 1, 1)
)
hpicfSflowInfoGroup.setObjects(
      *(("HP-ICF-SFLOW-MIB", "hpicfSflowPortMode"),
        ("HP-ICF-SFLOW-MIB", "hpicfSflowPortStatus"))
)
if mibBuilder.loadTexts:
    hpicfSflowInfoGroup.setStatus("current")

hpicfSflowInfoGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 2, 1, 2)
)
hpicfSflowInfoGroup1.setObjects(
    ("HP-ICF-SFLOW-MIB", "hpicfSflowRcvrOobm")
)
if mibBuilder.loadTexts:
    hpicfSflowInfoGroup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfSflowCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfSflowCompliance.setStatus(
        "current"
    )

hpicfSflowCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfSflowCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-SFLOW-MIB",
    **{"hpicfSflowMIB": hpicfSflowMIB,
       "hpicfSflowNotifications": hpicfSflowNotifications,
       "hpicfSflowObjects": hpicfSflowObjects,
       "hpicfSflowInfo": hpicfSflowInfo,
       "hpicfSflowPortInfoTable": hpicfSflowPortInfoTable,
       "hpicfSflowPortInfoEntry": hpicfSflowPortInfoEntry,
       "hpicfSflowPortMode": hpicfSflowPortMode,
       "hpicfSflowPortStatus": hpicfSflowPortStatus,
       "hpicfSflowRcvrTable": hpicfSflowRcvrTable,
       "hpicfSflowRcvrEntry": hpicfSflowRcvrEntry,
       "hpicfSflowRcvrOobm": hpicfSflowRcvrOobm,
       "hpicfSflowConformance": hpicfSflowConformance,
       "hpicfSflowGroups": hpicfSflowGroups,
       "hpicfSflowInfoGroup": hpicfSflowInfoGroup,
       "hpicfSflowInfoGroup1": hpicfSflowInfoGroup1,
       "hpicfSflowCompliances": hpicfSflowCompliances,
       "hpicfSflowCompliance": hpicfSflowCompliance,
       "hpicfSflowCompliance1": hpicfSflowCompliance1}
)
