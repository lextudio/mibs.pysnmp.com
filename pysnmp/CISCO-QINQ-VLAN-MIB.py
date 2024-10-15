# SNMP MIB module (CISCO-QINQ-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-QINQ-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:19 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoQinqVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 445)
)
ciscoQinqVlanMIB.setRevisions(
        ("2004-11-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CqvVlanIdOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )



class CqvEncapsulationType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1Q", 2),
          ("isl", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoQinqVlanMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoQinqVlanMIBNotifs = _CiscoQinqVlanMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 445, 0)
)
_CiscoQinqVlanMIBObjects_ObjectIdentity = ObjectIdentity
ciscoQinqVlanMIBObjects = _CiscoQinqVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 445, 1)
)
_CqvTermination_ObjectIdentity = ObjectIdentity
cqvTermination = _CqvTermination_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1)
)
_CqvTerminationTable_Object = MibTable
cqvTerminationTable = _CqvTerminationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cqvTerminationTable.setStatus("current")
_CqvTerminationEntry_Object = MibTableRow
cqvTerminationEntry = _CqvTerminationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1)
)
cqvTerminationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-QINQ-VLAN-MIB", "cqvTerminationPeVlanId"),
    (0, "CISCO-QINQ-VLAN-MIB", "cqvTerminationCeVlanId"),
)
if mibBuilder.loadTexts:
    cqvTerminationEntry.setStatus("current")
_CqvTerminationPeVlanId_Type = VlanId
_CqvTerminationPeVlanId_Object = MibTableColumn
cqvTerminationPeVlanId = _CqvTerminationPeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1, 1),
    _CqvTerminationPeVlanId_Type()
)
cqvTerminationPeVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cqvTerminationPeVlanId.setStatus("current")
_CqvTerminationCeVlanId_Type = VlanId
_CqvTerminationCeVlanId_Object = MibTableColumn
cqvTerminationCeVlanId = _CqvTerminationCeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1, 2),
    _CqvTerminationCeVlanId_Type()
)
cqvTerminationCeVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cqvTerminationCeVlanId.setStatus("current")
_CqvTerminationPeEncap_Type = CqvEncapsulationType
_CqvTerminationPeEncap_Object = MibTableColumn
cqvTerminationPeEncap = _CqvTerminationPeEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1, 3),
    _CqvTerminationPeEncap_Type()
)
cqvTerminationPeEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cqvTerminationPeEncap.setStatus("current")
_CqvTerminationRowStatus_Type = RowStatus
_CqvTerminationRowStatus_Object = MibTableColumn
cqvTerminationRowStatus = _CqvTerminationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1, 4),
    _CqvTerminationRowStatus_Type()
)
cqvTerminationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cqvTerminationRowStatus.setStatus("current")
_CqvTranslation_ObjectIdentity = ObjectIdentity
cqvTranslation = _CqvTranslation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2)
)
_CqvTranslationTable_Object = MibTable
cqvTranslationTable = _CqvTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cqvTranslationTable.setStatus("current")
_CqvTranslationEntry_Object = MibTableRow
cqvTranslationEntry = _CqvTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1)
)
cqvTranslationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-QINQ-VLAN-MIB", "cqvTranslationInternalPeVlanId"),
    (0, "CISCO-QINQ-VLAN-MIB", "cqvTranslationInternalCeVlanId"),
)
if mibBuilder.loadTexts:
    cqvTranslationEntry.setStatus("current")
_CqvTranslationInternalPeVlanId_Type = CqvVlanIdOrZero
_CqvTranslationInternalPeVlanId_Object = MibTableColumn
cqvTranslationInternalPeVlanId = _CqvTranslationInternalPeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 1),
    _CqvTranslationInternalPeVlanId_Type()
)
cqvTranslationInternalPeVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cqvTranslationInternalPeVlanId.setStatus("current")
_CqvTranslationInternalCeVlanId_Type = CqvVlanIdOrZero
_CqvTranslationInternalCeVlanId_Object = MibTableColumn
cqvTranslationInternalCeVlanId = _CqvTranslationInternalCeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 2),
    _CqvTranslationInternalCeVlanId_Type()
)
cqvTranslationInternalCeVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cqvTranslationInternalCeVlanId.setStatus("current")
_CqvTranslationTrunkPeVlanId_Type = CqvVlanIdOrZero
_CqvTranslationTrunkPeVlanId_Object = MibTableColumn
cqvTranslationTrunkPeVlanId = _CqvTranslationTrunkPeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 3),
    _CqvTranslationTrunkPeVlanId_Type()
)
cqvTranslationTrunkPeVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cqvTranslationTrunkPeVlanId.setStatus("current")
_CqvTranslationTrunkCeVlanId_Type = CqvVlanIdOrZero
_CqvTranslationTrunkCeVlanId_Object = MibTableColumn
cqvTranslationTrunkCeVlanId = _CqvTranslationTrunkCeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 4),
    _CqvTranslationTrunkCeVlanId_Type()
)
cqvTranslationTrunkCeVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cqvTranslationTrunkCeVlanId.setStatus("current")


class _CqvTranslationType_Type(Integer32):
    """Custom type cqvTranslationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("doubleToDouble", 2),
          ("doubleToDoubleOutOfRange", 3),
          ("doubleToSingle", 1))
    )


_CqvTranslationType_Type.__name__ = "Integer32"
_CqvTranslationType_Object = MibTableColumn
cqvTranslationType = _CqvTranslationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 5),
    _CqvTranslationType_Type()
)
cqvTranslationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cqvTranslationType.setStatus("current")


class _CqvTranslationCosPBits_Type(Integer32):
    """Custom type cqvTranslationCosPBits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copyFromInnerTag", 2),
          ("copyFromOuterTag", 1))
    )


_CqvTranslationCosPBits_Type.__name__ = "Integer32"
_CqvTranslationCosPBits_Object = MibTableColumn
cqvTranslationCosPBits = _CqvTranslationCosPBits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 6),
    _CqvTranslationCosPBits_Type()
)
cqvTranslationCosPBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cqvTranslationCosPBits.setStatus("current")
_CqvTranslationRowStatus_Type = RowStatus
_CqvTranslationRowStatus_Object = MibTableColumn
cqvTranslationRowStatus = _CqvTranslationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 7),
    _CqvTranslationRowStatus_Type()
)
cqvTranslationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cqvTranslationRowStatus.setStatus("current")
_CiscoQinqVlanMIBConform_ObjectIdentity = ObjectIdentity
ciscoQinqVlanMIBConform = _CiscoQinqVlanMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 445, 2)
)
_CiscoQinqVlanMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoQinqVlanMIBCompliances = _CiscoQinqVlanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 1)
)
_CiscoQinqVlanMIBGroups_ObjectIdentity = ObjectIdentity
ciscoQinqVlanMIBGroups = _CiscoQinqVlanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 2)
)

# Managed Objects groups

ciscoQinqVlanTerminationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 2, 1)
)
ciscoQinqVlanTerminationGroup.setObjects(
      *(("CISCO-QINQ-VLAN-MIB", "cqvTerminationPeEncap"),
        ("CISCO-QINQ-VLAN-MIB", "cqvTerminationRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoQinqVlanTerminationGroup.setStatus("current")

ciscoQinqVlanTranslationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 2, 2)
)
ciscoQinqVlanTranslationGroup.setObjects(
      *(("CISCO-QINQ-VLAN-MIB", "cqvTranslationTrunkPeVlanId"),
        ("CISCO-QINQ-VLAN-MIB", "cqvTranslationTrunkCeVlanId"),
        ("CISCO-QINQ-VLAN-MIB", "cqvTranslationType"),
        ("CISCO-QINQ-VLAN-MIB", "cqvTranslationCosPBits"),
        ("CISCO-QINQ-VLAN-MIB", "cqvTranslationRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoQinqVlanTranslationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoQinQVlanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoQinQVlanMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-QINQ-VLAN-MIB",
    **{"CqvVlanIdOrZero": CqvVlanIdOrZero,
       "CqvEncapsulationType": CqvEncapsulationType,
       "ciscoQinqVlanMIB": ciscoQinqVlanMIB,
       "ciscoQinqVlanMIBNotifs": ciscoQinqVlanMIBNotifs,
       "ciscoQinqVlanMIBObjects": ciscoQinqVlanMIBObjects,
       "cqvTermination": cqvTermination,
       "cqvTerminationTable": cqvTerminationTable,
       "cqvTerminationEntry": cqvTerminationEntry,
       "cqvTerminationPeVlanId": cqvTerminationPeVlanId,
       "cqvTerminationCeVlanId": cqvTerminationCeVlanId,
       "cqvTerminationPeEncap": cqvTerminationPeEncap,
       "cqvTerminationRowStatus": cqvTerminationRowStatus,
       "cqvTranslation": cqvTranslation,
       "cqvTranslationTable": cqvTranslationTable,
       "cqvTranslationEntry": cqvTranslationEntry,
       "cqvTranslationInternalPeVlanId": cqvTranslationInternalPeVlanId,
       "cqvTranslationInternalCeVlanId": cqvTranslationInternalCeVlanId,
       "cqvTranslationTrunkPeVlanId": cqvTranslationTrunkPeVlanId,
       "cqvTranslationTrunkCeVlanId": cqvTranslationTrunkCeVlanId,
       "cqvTranslationType": cqvTranslationType,
       "cqvTranslationCosPBits": cqvTranslationCosPBits,
       "cqvTranslationRowStatus": cqvTranslationRowStatus,
       "ciscoQinqVlanMIBConform": ciscoQinqVlanMIBConform,
       "ciscoQinqVlanMIBCompliances": ciscoQinqVlanMIBCompliances,
       "ciscoQinQVlanMIBCompliance": ciscoQinQVlanMIBCompliance,
       "ciscoQinqVlanMIBGroups": ciscoQinqVlanMIBGroups,
       "ciscoQinqVlanTerminationGroup": ciscoQinqVlanTerminationGroup,
       "ciscoQinqVlanTranslationGroup": ciscoQinqVlanTranslationGroup}
)
