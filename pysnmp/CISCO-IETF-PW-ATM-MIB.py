# SNMP MIB module (CISCO-IETF-PW-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-PW-ATM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:52 2024
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

(AtmVcIdentifier,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVcIdentifier",
    "AtmVpIdentifier")

(cpwVcIndex,) = mibBuilder.importSymbols(
    "CISCO-IETF-PW-MIB",
    "cpwVcIndex")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cpwVcAtmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000)
)
cpwVcAtmMIB.setRevisions(
        ("2005-04-19 12:00",
         "2003-02-16 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CpwVcAtmNotifications_ObjectIdentity = ObjectIdentity
cpwVcAtmNotifications = _CpwVcAtmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 0)
)
_CpwVcAtmObjects_ObjectIdentity = ObjectIdentity
cpwVcAtmObjects = _CpwVcAtmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 1)
)
_CpwVcAtmTable_Object = MibTable
cpwVcAtmTable = _CpwVcAtmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 1)
)
if mibBuilder.loadTexts:
    cpwVcAtmTable.setStatus("current")
_CpwVcAtmEntry_Object = MibTableRow
cpwVcAtmEntry = _CpwVcAtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 1, 1)
)
cpwVcAtmEntry.setIndexNames(
    (0, "CISCO-IETF-PW-MIB", "cpwVcIndex"),
)
if mibBuilder.loadTexts:
    cpwVcAtmEntry.setStatus("current")
_CpwAtmIf_Type = InterfaceIndex
_CpwAtmIf_Object = MibTableColumn
cpwAtmIf = _CpwAtmIf_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 1, 1, 1),
    _CpwAtmIf_Type()
)
cpwAtmIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwAtmIf.setStatus("current")
_CpwAtmVpi_Type = AtmVpIdentifier
_CpwAtmVpi_Object = MibTableColumn
cpwAtmVpi = _CpwAtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 1, 1, 2),
    _CpwAtmVpi_Type()
)
cpwAtmVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwAtmVpi.setStatus("current")
_CpwAtmVci_Type = AtmVcIdentifier
_CpwAtmVci_Object = MibTableColumn
cpwAtmVci = _CpwAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 1, 1, 3),
    _CpwAtmVci_Type()
)
cpwAtmVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwAtmVci.setStatus("current")
_CpwAtmClpQosMapping_Type = TruthValue
_CpwAtmClpQosMapping_Object = MibTableColumn
cpwAtmClpQosMapping = _CpwAtmClpQosMapping_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 1, 1, 4),
    _CpwAtmClpQosMapping_Type()
)
cpwAtmClpQosMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwAtmClpQosMapping.setStatus("current")
_CpwAtmRowStatus_Type = RowStatus
_CpwAtmRowStatus_Object = MibTableColumn
cpwAtmRowStatus = _CpwAtmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 1, 1, 5),
    _CpwAtmRowStatus_Type()
)
cpwAtmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwAtmRowStatus.setStatus("current")
_CpwAtmOamCellSupported_Type = TruthValue
_CpwAtmOamCellSupported_Object = MibTableColumn
cpwAtmOamCellSupported = _CpwAtmOamCellSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 1, 1, 6),
    _CpwAtmOamCellSupported_Type()
)
cpwAtmOamCellSupported.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwAtmOamCellSupported.setStatus("current")


class _CpwAtmQosScalingFactor_Type(Integer32):
    """Custom type cpwAtmQosScalingFactor based on Integer32"""
    defaultValue = 100


_CpwAtmQosScalingFactor_Object = MibTableColumn
cpwAtmQosScalingFactor = _CpwAtmQosScalingFactor_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 1, 1, 7),
    _CpwAtmQosScalingFactor_Type()
)
cpwAtmQosScalingFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwAtmQosScalingFactor.setStatus("current")
_CpwAtmCellPacking_Type = TruthValue
_CpwAtmCellPacking_Object = MibTableColumn
cpwAtmCellPacking = _CpwAtmCellPacking_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 1, 1, 8),
    _CpwAtmCellPacking_Type()
)
cpwAtmCellPacking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwAtmCellPacking.setStatus("current")
_CpwAtmMncp_Type = Integer32
_CpwAtmMncp_Object = MibTableColumn
cpwAtmMncp = _CpwAtmMncp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 1, 1, 9),
    _CpwAtmMncp_Type()
)
cpwAtmMncp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwAtmMncp.setStatus("current")
_CpwAtmPeerMncp_Type = Integer32
_CpwAtmPeerMncp_Object = MibTableColumn
cpwAtmPeerMncp = _CpwAtmPeerMncp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 1, 1, 10),
    _CpwAtmPeerMncp_Type()
)
cpwAtmPeerMncp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwAtmPeerMncp.setStatus("current")


class _CpwAtmEncap_Type(Integer32):
    """Custom type cpwAtmEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("l2tpv3", 2),
          ("mpls", 1),
          ("unknown", 3))
    )


_CpwAtmEncap_Type.__name__ = "Integer32"
_CpwAtmEncap_Object = MibTableColumn
cpwAtmEncap = _CpwAtmEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 1, 1, 11),
    _CpwAtmEncap_Type()
)
cpwAtmEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwAtmEncap.setStatus("current")
_CpwAtmMcptTimeout_Type = Integer32
_CpwAtmMcptTimeout_Object = MibTableColumn
cpwAtmMcptTimeout = _CpwAtmMcptTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 1, 1, 12),
    _CpwAtmMcptTimeout_Type()
)
cpwAtmMcptTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwAtmMcptTimeout.setStatus("current")
_CpwVcAtmPerfTable_Object = MibTable
cpwVcAtmPerfTable = _CpwVcAtmPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 2)
)
if mibBuilder.loadTexts:
    cpwVcAtmPerfTable.setStatus("current")
_CpwVcAtmPerfEntry_Object = MibTableRow
cpwVcAtmPerfEntry = _CpwVcAtmPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cpwVcAtmPerfEntry.setStatus("current")
_CpwAtmCellsReceived_Type = Counter32
_CpwAtmCellsReceived_Object = MibTableColumn
cpwAtmCellsReceived = _CpwAtmCellsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 2, 1, 1),
    _CpwAtmCellsReceived_Type()
)
cpwAtmCellsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwAtmCellsReceived.setStatus("current")
_CpwAtmCellsSent_Type = Counter32
_CpwAtmCellsSent_Object = MibTableColumn
cpwAtmCellsSent = _CpwAtmCellsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 2, 1, 2),
    _CpwAtmCellsSent_Type()
)
cpwAtmCellsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwAtmCellsSent.setStatus("current")
_CpwAtmCellsRejected_Type = Counter32
_CpwAtmCellsRejected_Object = MibTableColumn
cpwAtmCellsRejected = _CpwAtmCellsRejected_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 2, 1, 3),
    _CpwAtmCellsRejected_Type()
)
cpwAtmCellsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwAtmCellsRejected.setStatus("current")
_CpwAtmCellsTagged_Type = Counter32
_CpwAtmCellsTagged_Object = MibTableColumn
cpwAtmCellsTagged = _CpwAtmCellsTagged_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 2, 1, 4),
    _CpwAtmCellsTagged_Type()
)
cpwAtmCellsTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwAtmCellsTagged.setStatus("current")
_CpwAtmHCCellsReceived_Type = Counter64
_CpwAtmHCCellsReceived_Object = MibTableColumn
cpwAtmHCCellsReceived = _CpwAtmHCCellsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 2, 1, 5),
    _CpwAtmHCCellsReceived_Type()
)
cpwAtmHCCellsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwAtmHCCellsReceived.setStatus("current")
_CpwAtmHCCellsRejected_Type = Counter64
_CpwAtmHCCellsRejected_Object = MibTableColumn
cpwAtmHCCellsRejected = _CpwAtmHCCellsRejected_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 2, 1, 6),
    _CpwAtmHCCellsRejected_Type()
)
cpwAtmHCCellsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwAtmHCCellsRejected.setStatus("current")
_CpwAtmHCCellsTagged_Type = Counter64
_CpwAtmHCCellsTagged_Object = MibTableColumn
cpwAtmHCCellsTagged = _CpwAtmHCCellsTagged_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 2, 1, 7),
    _CpwAtmHCCellsTagged_Type()
)
cpwAtmHCCellsTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwAtmHCCellsTagged.setStatus("current")
_CpwAtmAvgCellsPacked_Type = Counter32
_CpwAtmAvgCellsPacked_Object = MibTableColumn
cpwAtmAvgCellsPacked = _CpwAtmAvgCellsPacked_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 2, 1, 8),
    _CpwAtmAvgCellsPacked_Type()
)
cpwAtmAvgCellsPacked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwAtmAvgCellsPacked.setStatus("current")
_CpwAtmPktsReceived_Type = Counter32
_CpwAtmPktsReceived_Object = MibTableColumn
cpwAtmPktsReceived = _CpwAtmPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 2, 1, 9),
    _CpwAtmPktsReceived_Type()
)
cpwAtmPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwAtmPktsReceived.setStatus("current")
_CpwAtmPktsSent_Type = Counter32
_CpwAtmPktsSent_Object = MibTableColumn
cpwAtmPktsSent = _CpwAtmPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 2, 1, 10),
    _CpwAtmPktsSent_Type()
)
cpwAtmPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwAtmPktsSent.setStatus("current")
_CpwAtmPktsRejected_Type = Counter32
_CpwAtmPktsRejected_Object = MibTableColumn
cpwAtmPktsRejected = _CpwAtmPktsRejected_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 2, 1, 11),
    _CpwAtmPktsRejected_Type()
)
cpwAtmPktsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwAtmPktsRejected.setStatus("current")
_CpwVcAtmConformance_ObjectIdentity = ObjectIdentity
cpwVcAtmConformance = _CpwVcAtmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 2)
)
_CpwVcAtmGroups_ObjectIdentity = ObjectIdentity
cpwVcAtmGroups = _CpwVcAtmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 2, 1)
)
_CpwVcAtmCompliances_ObjectIdentity = ObjectIdentity
cpwVcAtmCompliances = _CpwVcAtmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 2, 2)
)
cpwVcAtmEntry.registerAugmentions(
    ("CISCO-IETF-PW-ATM-MIB",
     "cpwVcAtmPerfEntry")
)
cpwVcAtmPerfEntry.setIndexNames(*cpwVcAtmEntry.getIndexNames())

# Managed Objects groups

cpwVcAtmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 2, 1, 1)
)
cpwVcAtmGroup.setObjects(
      *(("CISCO-IETF-PW-ATM-MIB", "cpwAtmIf"),
        ("CISCO-IETF-PW-ATM-MIB", "cpwAtmVpi"),
        ("CISCO-IETF-PW-ATM-MIB", "cpwAtmVci"),
        ("CISCO-IETF-PW-ATM-MIB", "cpwAtmRowStatus"),
        ("CISCO-IETF-PW-ATM-MIB", "cpwAtmClpQosMapping"),
        ("CISCO-IETF-PW-ATM-MIB", "cpwAtmOamCellSupported"),
        ("CISCO-IETF-PW-ATM-MIB", "cpwAtmQosScalingFactor"),
        ("CISCO-IETF-PW-ATM-MIB", "cpwAtmCellPacking"),
        ("CISCO-IETF-PW-ATM-MIB", "cpwAtmMncp"),
        ("CISCO-IETF-PW-ATM-MIB", "cpwAtmPeerMncp"),
        ("CISCO-IETF-PW-ATM-MIB", "cpwAtmEncap"),
        ("CISCO-IETF-PW-ATM-MIB", "cpwAtmMcptTimeout"))
)
if mibBuilder.loadTexts:
    cpwVcAtmGroup.setStatus("current")

cpwAtmPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 2, 1, 2)
)
cpwAtmPerfGroup.setObjects(
      *(("CISCO-IETF-PW-ATM-MIB", "cpwAtmCellsReceived"),
        ("CISCO-IETF-PW-ATM-MIB", "cpwAtmCellsSent"),
        ("CISCO-IETF-PW-ATM-MIB", "cpwAtmCellsRejected"),
        ("CISCO-IETF-PW-ATM-MIB", "cpwAtmCellsTagged"),
        ("CISCO-IETF-PW-ATM-MIB", "cpwAtmHCCellsReceived"),
        ("CISCO-IETF-PW-ATM-MIB", "cpwAtmHCCellsRejected"),
        ("CISCO-IETF-PW-ATM-MIB", "cpwAtmHCCellsTagged"),
        ("CISCO-IETF-PW-ATM-MIB", "cpwAtmPktsReceived"),
        ("CISCO-IETF-PW-ATM-MIB", "cpwAtmPktsSent"),
        ("CISCO-IETF-PW-ATM-MIB", "cpwAtmPktsRejected"),
        ("CISCO-IETF-PW-ATM-MIB", "cpwAtmAvgCellsPacked"))
)
if mibBuilder.loadTexts:
    cpwAtmPerfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cpwVcAtmModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 9000, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cpwVcAtmModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-PW-ATM-MIB",
    **{"cpwVcAtmMIB": cpwVcAtmMIB,
       "cpwVcAtmNotifications": cpwVcAtmNotifications,
       "cpwVcAtmObjects": cpwVcAtmObjects,
       "cpwVcAtmTable": cpwVcAtmTable,
       "cpwVcAtmEntry": cpwVcAtmEntry,
       "cpwAtmIf": cpwAtmIf,
       "cpwAtmVpi": cpwAtmVpi,
       "cpwAtmVci": cpwAtmVci,
       "cpwAtmClpQosMapping": cpwAtmClpQosMapping,
       "cpwAtmRowStatus": cpwAtmRowStatus,
       "cpwAtmOamCellSupported": cpwAtmOamCellSupported,
       "cpwAtmQosScalingFactor": cpwAtmQosScalingFactor,
       "cpwAtmCellPacking": cpwAtmCellPacking,
       "cpwAtmMncp": cpwAtmMncp,
       "cpwAtmPeerMncp": cpwAtmPeerMncp,
       "cpwAtmEncap": cpwAtmEncap,
       "cpwAtmMcptTimeout": cpwAtmMcptTimeout,
       "cpwVcAtmPerfTable": cpwVcAtmPerfTable,
       "cpwVcAtmPerfEntry": cpwVcAtmPerfEntry,
       "cpwAtmCellsReceived": cpwAtmCellsReceived,
       "cpwAtmCellsSent": cpwAtmCellsSent,
       "cpwAtmCellsRejected": cpwAtmCellsRejected,
       "cpwAtmCellsTagged": cpwAtmCellsTagged,
       "cpwAtmHCCellsReceived": cpwAtmHCCellsReceived,
       "cpwAtmHCCellsRejected": cpwAtmHCCellsRejected,
       "cpwAtmHCCellsTagged": cpwAtmHCCellsTagged,
       "cpwAtmAvgCellsPacked": cpwAtmAvgCellsPacked,
       "cpwAtmPktsReceived": cpwAtmPktsReceived,
       "cpwAtmPktsSent": cpwAtmPktsSent,
       "cpwAtmPktsRejected": cpwAtmPktsRejected,
       "cpwVcAtmConformance": cpwVcAtmConformance,
       "cpwVcAtmGroups": cpwVcAtmGroups,
       "cpwVcAtmGroup": cpwVcAtmGroup,
       "cpwAtmPerfGroup": cpwAtmPerfGroup,
       "cpwVcAtmCompliances": cpwVcAtmCompliances,
       "cpwVcAtmModuleCompliance": cpwVcAtmModuleCompliance}
)
